#!/usr/bin/env python3
"""
Convert a Jupyter notebook (.ipynb) with RISE slideshow metadata
to a Quarto markdown file (.qmd) with multi-format support.

Usage:
    python convert_nb_to_qmd.py <input.ipynb> [output.qmd]

If output path is omitted, the .qmd is written next to the .ipynb.
The stem of the output filename (e.g. "16_NN") becomes the lecture_id
used in YAML frontmatter and resource paths.
"""

import json
import re
import subprocess
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_slide_type(cell: dict) -> str:
    """Return the RISE slide_type, or '' if not set."""
    return cell.get("metadata", {}).get("slideshow", {}).get("slide_type") or ""


def get_tags(cell: dict) -> list:
    return cell.get("metadata", {}).get("tags", [])


def join_source(cell: dict) -> str:
    return "".join(cell.get("source", []))


def is_heading_only(source: str) -> bool:
    """True when every non-blank line is a Markdown heading."""
    lines = [l for l in source.strip().splitlines() if l.strip()]
    return bool(lines) and all(l.lstrip().startswith("#") for l in lines)


def split_heading(source: str) -> tuple[str, str]:
    """
    Split source into (leading_heading_lines, remaining_body).
    If the source doesn't start with a heading, returns ('', source).
    """
    lines = source.split("\n")
    heading_lines = []
    for line in lines:
        if line.lstrip().startswith("#") or not line.strip():
            if heading_lines or line.lstrip().startswith("#"):
                heading_lines.append(line)
                if line.lstrip().startswith("#"):
                    # collect only contiguous heading lines at the top
                    continue
        else:
            break
    # only keep if we actually found a heading
    heading = "\n".join(heading_lines).strip()
    body = "\n".join(lines[len(heading_lines):]).strip()
    if not heading or not heading.lstrip().startswith("#"):
        return "", source
    return heading, body


def extract_title(source: str) -> str:
    """Pull the lecture title out of the HTML title-slide cell."""
    # <p class="subtitle" ...>Künstliche Neuronale Netzwerke</p>
    m = re.search(r'class="subtitle"[^>]*>(.*?)</p>', source, re.DOTALL)
    if m:
        return re.sub(r"<[^>]+>", "", m.group(1)).strip()
    # Fallback: last non-empty <p> content
    for text in reversed(re.findall(r'<p[^>]*>(.*?)</p>', source, re.DOTALL)):
        clean = re.sub(r"<[^>]+>", "", text).strip()
        if clean:
            return clean
    return "Lecture Title"


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------

def make_frontmatter(title: str, lecture_id: str) -> str:
    return (
        f"---\n"
        f"title: {title}\n"
        f"format:\n"
        f"  revealjs:\n"
        f"    title-slide-attributes:\n"
        f"      data-background-video: images/{lecture_id}/mj_title.mp4\n"
        f"    output-file: {lecture_id}.slide.html\n"
        f"  html:\n"
        f"    output-file: {lecture_id}.page.html\n"
        f"  typst:\n"
        f"    output-file: {lecture_id}.page.pdf\n"
        f"#  pdf:\n"
        f"#    output-file: {lecture_id}.slide.pdf\n"
        f"resources:\n"
        f"  - data/{lecture_id}\n"
        f"#  - plotly-loader.js\n"
        f"---\n"
    )


# ---------------------------------------------------------------------------
# Content-visible wrappers
# ---------------------------------------------------------------------------

WRAP_UNLESS = 'unless-format="revealjs"'
WRAP_WHEN   = 'when-format="revealjs"'


def wrap(content: str, visibility: str) -> str:
    """Wrap content in a Quarto conditional block."""
    inner = content.strip()
    return f"::::: {{.content-visible {visibility}}}\n\n{inner}\n\n:::::\n"


def infer_lang(path: Path) -> str:
    """Infer lecture language from the filename."""
    return "en" if path.stem.endswith("_en") else "de"


def compress_to_qmdx(qmd_text: str, lang: str) -> str:
    """
    Postprocess QMD text into QMDX macros.

    Prefer the current interpreter when ai4sc_style is installed there.
    Otherwise fall back to the project's .venv Python so the script also works
    when invoked from a different environment.
    """
    try:
        from ai4sc_style.preprocess import compress_macros

        return compress_macros(qmd_text, lang=lang)
    except ModuleNotFoundError:
        pass

    venv_python = Path(__file__).resolve().parent.parent / ".venv" / "bin" / "python3"
    if not venv_python.exists():
        raise RuntimeError(
            "Could not import 'ai4sc_style.preprocess.compress_macros' and no "
            f"fallback interpreter was found at {venv_python}."
        )

    code = (
        "import sys\n"
        "from ai4sc_style.preprocess import compress_macros\n"
        "sys.stdout.write(compress_macros(sys.stdin.read(), lang=sys.argv[1]))\n"
    )
    result = subprocess.run(
        [str(venv_python), "-c", code, lang],
        input=qmd_text,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            "QMDX postprocessing failed via the project environment:\n"
            f"{result.stderr.strip()}"
        )
    return result.stdout


def choose_visibility(slide_type: str, tags: list) -> str | None:
    """
    Return the visibility string for content-visible wrapping,
    or None if no wrapping is needed.

    Priority:
      1. remove-cell / hide-cell tag → slides only (when-format)
      2. slide_type=skip             → docs only   (unless-format)
      3. everything else             → both formats (no wrapping)
         slide/subslide/fragment cells create slide breaks via the
         heading-split / --- logic, but their *content* is visible in
         both HTML docs and revealjs slides.
    """
    if "remove-cell" in tags:
        return WRAP_WHEN
    if slide_type == "skip":
        return WRAP_UNLESS
    return None  # appears in both formats


# ---------------------------------------------------------------------------
# Cell converters
# ---------------------------------------------------------------------------

def convert_code_cell(source: str, tags: list) -> str:
    """Render a code cell as a Quarto {python} block."""
    options = []

    SLIDE_LINE_LIMIT = 25  # lines that comfortably fit on one slide

    if "remove-input" in tags or "hide-cell" in tags:
        options.append("#| echo: false")
    else:
        options.append("#| echo: true")
        if source.count("\n") >= SLIDE_LINE_LIMIT:
            options.append("#| code-fold: true")

    if "remove-output" in tags or "hide-cell" in tags:
        options.append("#| output: false")

    if "raises-exception" in tags:
        options.append("#| error: true")

    if "scroll-output" in tags:
        options.append("#| max-height: 200")

    opts_block = "\n".join(options)
    return f"```{{python}}\n{opts_block}\n{source.strip()}\n```\n"


_FIGURE_RE = re.compile(
    r"```\{figure\}\s+(\S+)\n"    # opening fence + image path
    r"((?::[a-z_]+:[^\n]*\n)*)"   # option lines  (:key: value)
    r"\n?"                         # optional blank line before caption
    r"(.*?)\n```",                 # caption + closing fence
    re.DOTALL,
)


def _figure_replacement(m: re.Match) -> str:
    path = m.group(1)
    opts_raw = m.group(2)
    caption = m.group(3).strip()

    opts: dict[str, str] = {}
    for line in opts_raw.splitlines():
        mo = re.match(r":([a-z_]+):\s*(.*)", line)
        if mo:
            opts[mo.group(1)] = mo.group(2).strip()

    attrs: list[str] = []
    if "name" in opts:
        name = opts["name"]
        if not name.startswith("fig-"):
            name = "fig-" + name
        attrs.append(f"#{name}")
    if "alt" in opts:
        attrs.append(f'fig-alt="{opts["alt"]}"')
    if "align" in opts:
        attrs.append(f'fig-align="{opts["align"]}"')
    # figwidth (percentage) is preferred over width (pixels) for responsive output
    if "figwidth" in opts:
        attrs.append(f'width="{opts["figwidth"]}"')
    elif "width" in opts:
        attrs.append(f'width="{opts["width"]}"')

    attr_str = " ".join(attrs)
    suffix = f"{{{attr_str}}}" if attr_str else ""
    return f"![{caption}]({path}){suffix}"


def convert_myst_figures(source: str) -> str:
    """Replace MyST ```{figure}``` directives with Quarto-native ![]() syntax."""
    return _FIGURE_RE.sub(_figure_replacement, source)


_LECTURE_QUESTION_RE = re.compile(
    r'^(#{1,6})\s+([^\n]+?)\s*\n+'
    r'\s*<script>setSectionBackground\(\'([^\']+)\'(?:,[^)]*)?\);</script>\s*'
    r'<div class="flex-row">\s*'
    r'<div class="col(\d+)(?: [^"]*)?">\s*'
    r'(.*?)'
    r'\s*</div>\s*'
    r'<div class="col(\d+)(?: [^"]*)?">\s*'
    r'<figure class="mj-fig">\s*'
    r'<img src="([^"]+)" class="mj-fig-img">\s*'
    r'<figcaption class="mj-fig-cap">\s*'
    r'(.*?)\s*'
    r'</figcaption>\s*'
    r'</figure>\s*'
    r'</div>\s*'
    r'</div>\s*$',
    re.DOTALL,
)


_SECTION_MEDIA_RE = re.compile(
    r'^(#{1,6})\s+([^\n]+?)\s*\n+'
    r'\s*<figcaption class="mj-slide-cap">\s*(.*?)\s*</figcaption>\s*\n+'
    r'\s*<script>setSectionBackground\(\'([^\']+)\'\s*,\s*\'([^\']+)\'(?:,\s*true)?\);</script>\s*$',
    re.DOTALL,
)


_BOOK_BLOCK_RE = re.compile(
    r'^\s*<figure class="mj-tile-band">\s*'
    r"<img src=['\"]([^'\"]+)['\"]>\s*"
    r'<figcaption>\s*(.*?)\s*</figcaption>\s*'
    r'</figure>\s*'
    r'(>.*)\s*$',
    re.DOTALL,
)


_FINAL_SLIDE_RE = re.compile(
    r'^\s*<div class="vslide">\s*'
    r'(?:'
    r'<div class="vslide-title">\s*'
    r'<p[^>]*>\s*(fragen\?|questions\?)\s*</p>\s*'
    r'</div>'
    r'|'
    r'<div class="questions"[^>]*>\s*(fragen\?|questions\?)\s*</div>'
    r')\s*'
    r'<script>setSectionBackground\(\'([^\']+)\'\s*,\s*\'([^\']+)\'(?:,\s*true)?\);</script>\s*'
    r'</div>\s*$',
    re.DOTALL | re.IGNORECASE,
)


_MJ_FIGURE_RE = re.compile(
    r'<figure class="mj-fig">\s*'
    r'<img src="([^"]+)" class="mj-fig-img">\s*'
    r'<figcaption class="mj-fig-cap">\s*'
    r'(.*?)\s*'
    r'</figcaption>\s*'
    r'</figure>',
    re.DOTALL,
)


def convert_midjourney_figures(source: str) -> str:
    """Replace legacy Midjourney HTML figure blocks with Quarto image syntax."""
    def repl(match: re.Match) -> str:
        image_path = match.group(1).strip()
        caption = re.sub(r"\s+", " ", match.group(2)).strip()
        return f'![{caption}]({image_path}){{class="midjourneyXX"}}'

    return _MJ_FIGURE_RE.sub(repl, source)


def _normalize_heading_text(heading_text: str) -> str:
    heading_text = re.sub(r"\s+", " ", heading_text).strip()
    if ":" in heading_text:
        heading_text = heading_text.split(":", 1)[1].strip()
    return heading_text


def _normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _escape_shortcode_attr(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace('"', "&quot;")
        .replace("\n", " ")
    )


def _normalize_hex_color(color: str) -> str:
    color = color.strip()
    match = re.fullmatch(r"#([0-9a-fA-F]{6})", color)
    if not match:
        return color

    hex_value = match.group(1)
    if hex_value[0] == hex_value[1] and hex_value[2] == hex_value[3] and hex_value[4] == hex_value[5]:
        return f"#{hex_value[0]}{hex_value[2]}{hex_value[4]}".lower()
    return color


def convert_book_block(source: str) -> str:
    """Convert title-band figure plus quote block into %%book wrapper."""
    match = _BOOK_BLOCK_RE.match(source.strip())
    if not match:
        return source

    image_path, _caption, quote_block = match.groups()
    quote_block = quote_block.strip()
    return f"%%book\n\n![]({image_path.strip()})\n\n{quote_block}\n\n%%/book"


def convert_final_slide_block(source: str) -> str:
    """Convert final 'questions?' slide markup into %%final."""
    match = _FINAL_SLIDE_RE.match(source.strip())
    if not match:
        return source
    return "%%final"


def convert_section_media_block(source: str) -> str:
    """Convert heading + slide caption + background media into compact section syntax."""
    match = _SECTION_MEDIA_RE.match(source.strip())
    if not match:
        return source

    heading_level, heading_text, caption, background, media_path = match.groups()
    heading_text = _normalize_whitespace(heading_text)
    caption = _normalize_whitespace(caption)
    background = _normalize_hex_color(background)

    return (
        f'{heading_level} {heading_text} '
        f'{{colR '
        f'capR="{_escape_shortcode_attr(caption)}" '
        f'imgR="{_escape_shortcode_attr(media_path.strip())}" '
        f'background="{_escape_shortcode_attr(background)}"}}'
    )


def convert_lecture_question_block(source: str) -> str:
    """Convert the lecture-hall-question HTML layout into a compact shortcode heading."""
    match = _LECTURE_QUESTION_RE.match(source.strip())
    if not match:
        return source

    heading_level, heading_text, background, left_weight, left_text, right_weight, image_path, caption = match.groups()
    heading_text = _normalize_heading_text(heading_text)
    left_weight = int(left_weight)
    right_weight = int(right_weight)
    total_weight = left_weight + right_weight
    left_width = round(100 * left_weight / total_weight)
    right_width = round(100 * right_weight / total_weight)
    left_text = _normalize_whitespace(left_text)
    caption = _normalize_whitespace(caption)

    return (
        f'{heading_level} {heading_text} '
        f'{{background="{_escape_shortcode_attr(background)}" '
        f'cols{left_width}x{right_width} '
        f'txtL="{_escape_shortcode_attr(left_text)}" '
        f'capR="{_escape_shortcode_attr(caption)}" '
        f'imgR="{_escape_shortcode_attr(image_path.strip())}"}}'
    )


def _div_delta(line: str) -> int:
    """Net change in div nesting depth for a line."""
    return len(re.findall(r"<div\b", line)) - len(re.findall(r"</div>", line))


def _format_width(value: float) -> str:
    rounded = round(value)
    if abs(value - rounded) < 1e-9:
        return f"{rounded}%"
    return f"{value:.2f}".rstrip("0").rstrip(".") + "%"


def convert_flex_rows(source: str) -> str:
    """
    Convert legacy HTML flex-row blocks into Quarto columns blocks.

    Example:
      <div class="flex-row">
        <div class="col4">...</div>
        <div class="col6">...</div>
      </div>
    becomes:
      :::: {.columns}
      ::: {.column width="40%"}
      ...
      :::
      ::: {.column width="60%"}
      ...
      :::
      ::::
    """
    lines = source.splitlines()
    out: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]
        if not re.search(r'<div class="[^"]*\bflex-row\b[^"]*"', line):
            out.append(line)
            i += 1
            continue

        # Capture the full outer flex-row block.
        block_lines = [line]
        depth = _div_delta(line)
        i += 1
        while i < len(lines) and depth > 0:
            block_lines.append(lines[i])
            depth += _div_delta(lines[i])
            i += 1

        inner_lines = block_lines[1:-1]
        columns: list[tuple[int, str]] = []
        j = 0
        failed = depth != 0

        while j < len(inner_lines):
            inner = inner_lines[j]
            match = re.search(r'<div class="[^"]*\bcol(\d+)\b[^"]*"', inner)
            if not match:
                if inner.strip():
                    failed = True
                    break
                j += 1
                continue

            col_weight = int(match.group(1))
            col_depth = _div_delta(inner)
            column_lines: list[str] = []
            j += 1

            while j < len(inner_lines) and col_depth > 0:
                current = inner_lines[j]
                next_depth = col_depth + _div_delta(current)
                if next_depth == 0:
                    col_depth = 0
                    j += 1
                    break
                column_lines.append(current)
                col_depth = next_depth
                j += 1

            if col_depth != 0:
                failed = True
                break

            columns.append((col_weight, "\n".join(column_lines).strip()))

        if failed or not columns:
            out.extend(block_lines)
            continue

        total_weight = sum(weight for weight, _ in columns)
        out.append(":::: {.columns}")
        for weight, content in columns:
            width = _format_width(100 * weight / total_weight)
            out.append(f'::: {{.column width="{width}"}}')
            if content:
                out.append("")
                out.append(content)
                out.append("")
            out.append(":::")
        out.append("::::")

    return "\n".join(out)


def convert_markdown_cell(source: str) -> str:
    source = convert_final_slide_block(source)
    source = convert_book_block(source)
    source = convert_section_media_block(source)
    source = convert_lecture_question_block(source)
    source = convert_flex_rows(source)
    source = convert_midjourney_figures(source)
    source = convert_myst_figures(source)
    return source.strip() + "\n"



# ---------------------------------------------------------------------------
# Block merging
# ---------------------------------------------------------------------------

# Each item is either:
#   ("raw", content_str)          — emitted as-is
#   ("wrapped", visibility, content_str)  — wrapped in content-visible block
Item = tuple


def merge_blocks(items: list[Item]) -> list[Item]:
    """Merge consecutive wrapped items that share the same visibility."""
    merged: list[Item] = []
    for item in items:
        if (
            item[0] == "wrapped"
            and merged
            and merged[-1][0] == "wrapped"
            and merged[-1][1] == item[1]
        ):
            # Append content into the existing block
            prev = merged[-1]
            merged[-1] = ("wrapped", prev[1], prev[2].rstrip() + "\n\n" + item[2].strip())
        else:
            merged.append(list(item))  # mutable copy
    return merged


def render_blocks(items: list[Item]) -> str:
    parts = []
    for item in items:
        if item[0] == "raw":
            parts.append(item[1])
        else:  # "wrapped"
            parts.append(wrap(item[2], item[1]))
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Main converter
# ---------------------------------------------------------------------------

def convert(ipynb_path: Path, qmd_path: Path) -> None:
    try:
        with open(ipynb_path, encoding="utf-8") as f:
            nb = json.load(f)
    except json.JSONDecodeError as exc:
        preview = ipynb_path.read_text(encoding="utf-8", errors="replace")[:200].strip()
        hint = ""
        if preview.startswith("---"):
            hint = (
                " The file starts with YAML frontmatter ('---'), which suggests it "
                "contains Quarto/Markdown output instead of notebook JSON."
            )
        elif preview.startswith("<!DOCTYPE html") or preview.startswith("<html"):
            hint = " The file appears to contain HTML instead of notebook JSON."

        print(
            f"Error: '{ipynb_path}' is not a valid Jupyter notebook JSON file."
            f"{hint}\n"
            f"JSON parser message: {exc}\n"
            f"File preview: {preview[:120]!r}",
            file=sys.stderr,
        )
        sys.exit(1)

    cells = nb.get("cells", [])
    lecture_id = qmd_path.stem  # e.g. "16_NN"

    # ---- Pass 1: find and extract the title from the title slide -----------
    title = "Lecture Title"
    title_cell_idx = None
    for idx, cell in enumerate(cells):
        if cell["cell_type"] == "markdown" and "remove-cell" in get_tags(cell):
            src = join_source(cell)
            if "ML_video_w_s.webp" in src:
                title = extract_title(src)
                title_cell_idx = idx
                break

    # ---- Pass 2: convert cells -------------------------------------------
    items: list[Item] = [("raw", make_frontmatter(title, lecture_id))]

    for idx, cell in enumerate(cells):
        tags = get_tags(cell)
        slide_type = get_slide_type(cell)
        source = join_source(cell)

        # Skip empty cells
        if not source.strip():
            continue

        # Skip the title slide (already in frontmatter)
        if idx == title_cell_idx:
            continue

        # Skip old slide-embed iframes
        if cell["cell_type"] == "markdown" and "<iframe" in source and "slides.html" in source:
            continue

        # --- Speaker notes → Quarto ::: {.notes} block (never merged) ---
        if slide_type == "notes":
            items.append(("raw", f"::: {{.notes}}\n{source.strip()}\n:::\n"))
            continue

        # Determine visibility wrapping
        visibility = choose_visibility(slide_type, tags)

        # --- Code cell ---
        if cell["cell_type"] == "code":
            content = convert_code_cell(source, tags)
            if visibility:
                items.append(("wrapped", visibility, content))
            else:
                items.append(("raw", content))
            continue

        # --- Markdown cell ---
        if cell["cell_type"] == "markdown":
            # Heading-only cells:
            #   • skip → wrap unless-format (docs only, no slide break in revealjs)
            #   • remove-cell tag → wrap when-format (slides only)
            #   • slide/subslide/fragment/'' → emit raw (section marker in HTML
            #     AND slide break / heading in revealjs)
            if is_heading_only(source):
                content = convert_markdown_cell(source) + "\n"
                if slide_type == "skip" or "remove-cell" in tags:
                    items.append(("wrapped", visibility, content))
                else:
                    items.append(("raw", content))
                continue

            # slide_type="slide"/"subslide"/"fragment": create a slide break
            # for revealjs while keeping the content visible in all formats.
            # Only the --- separator is when-format; the body is raw so it
            # appears in HTML documentation and revealjs slides alike.
            if slide_type in ("slide", "subslide", "fragment") and "remove-cell" not in tags:
                heading, body = split_heading(source)
                if heading:
                    items.append(("raw", heading + "\n\n"))
                    if body:
                        items.append(("raw", convert_markdown_cell(body)))
                else:
                    # No heading — only the --- is revealjs-only; content is raw.
                    items.append(("wrapped", WRAP_WHEN, "---"))
                    items.append(("raw", convert_markdown_cell(source)))
                continue

            content = convert_markdown_cell(source)
            if visibility:
                items.append(("wrapped", visibility, content))
            else:
                items.append(("raw", content))
            continue

        # --- Raw cell ---
        if cell["cell_type"] == "raw":
            print(f"  Warning: skipping raw cell (idx {idx}): {source[:60]!r}", file=sys.stderr)
            continue

    # ---- Merge consecutive same-visibility blocks, then render -------------
    output = render_blocks(merge_blocks(items))
    qmdx_output = compress_to_qmdx(output, lang=infer_lang(ipynb_path))
    qmdx_path = qmd_path.with_suffix(".qmdx")

    # ---- Write output -------------------------------------------------------
    qmd_path.parent.mkdir(parents=True, exist_ok=True)
    with open(qmd_path, "w", encoding="utf-8") as f:
        f.write(output)
        if not output.endswith("\n"):
            f.write("\n")
    with open(qmdx_path, "w", encoding="utf-8") as f:
        f.write(qmdx_output)
        if not qmdx_output.endswith("\n"):
            f.write("\n")

    print(f"Converted:  {ipynb_path}")
    print(f"Output:     {qmd_path}")
    print(f"Postprocessed: {qmdx_path}")
    print(f"Cells processed: {len(cells)}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    if len(sys.argv) >= 2:
        ipynb_path = Path(sys.argv[1])
        if not ipynb_path.exists():
            print(f"Error: file not found: {ipynb_path}", file=sys.stderr)
            sys.exit(1)
        qmd_path = Path(sys.argv[2]) if len(sys.argv) >= 3 else ipynb_path.with_suffix(".qmd")
        convert(ipynb_path, qmd_path)
    else:
        notebooks = sorted(Path(".").glob("*.ipynb"))
        if not notebooks:
            print("No *.ipynb files found in the current directory.", file=sys.stderr)
            sys.exit(1)
        for ipynb_path in notebooks:
            convert(ipynb_path, ipynb_path.with_suffix(".qmd"))


if __name__ == "__main__":
    main()
