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


def extract_image_credit(source: str) -> str:
    """Pull the image credit out of the title-slide figcaption."""
    match = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", source, re.DOTALL)
    if not match:
        return ""
    return _normalize_whitespace(re.sub(r"<[^>]+>", "", match.group(1)))


def extract_background_video(source: str) -> str:
    """Pull the title-slide background video path out of setSectionBackground(...)."""
    match = re.search(
        r"setSectionBackground\(\s*'[^']*'\s*,\s*'([^']+)'",
        source,
        re.DOTALL,
    )
    if not match:
        return ""
    return match.group(1).strip()


def is_title_slide(source: str) -> bool:
    """Detect the HTML title slide cell."""
    return 'class="vslide-title"' in source and 'class="subtitle"' in source


def yaml_quote(value: str) -> str:
    """Safely quote a scalar value for YAML frontmatter."""
    return json.dumps(value, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------

def make_frontmatter(title: str, lecture_id: str, image_credit: str, background_video: str) -> str:
    parts = [
        "---\n",
        f"title: {yaml_quote(title)}\n",
    ]
    if image_credit:
        parts.append(f"image-credit: {yaml_quote(image_credit)}\n")
    parts.extend([
        f"format:\n"
        f"  revealjs:\n"
        f"    title-slide-attributes:\n"
        f"      data-background-video: {background_video or f'images/{lecture_id}/mj_title.mp4'}\n"
        f"    output-file: {lecture_id}.slide.html\n"
        f"  html:\n"
        f"    output-file: {lecture_id}.page.html\n"
        f"  typst:\n"
        f"    output-file: {lecture_id}.page.pdf\n"
        f"resources:\n"
        f"  - data/{lecture_id}\n"
        f"---\n"
    ])
    return "".join(parts)


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


_LECTURE_QUESTION_MD_IMAGE_RE = re.compile(
    r'^(#{1,6})\s+([^\n]+?)\s*\n+'
    r'\s*<script>setSectionBackground\(\'([^\']+)\'(?:,[^)]*)?\);</script>\s*'
    r'<div class="flex-row">\s*'
    r'<div[^>]*width:\s*([0-9]+)%[^>]*>\s*'
    r'(.*?)'
    r'\s*</div>\s*'
    r'<div[^>]*width:\s*([0-9]+)%[^>]*>\s*'
    r'!\[(.*?)\]\(([^)]+)\)(?:\{[^}]*\})?'
    r'\s*</div>\s*'
    r'</div>\s*$',
    re.DOTALL,
)


_LECTURE_QUESTION_STYLE_FIGURE_RE = re.compile(
    r'^(#{1,6})\s+([^\n]+?)\s*\n+'
    r'\s*<script>setSectionBackground\(\'([^\']+)\'(?:,[^)]*)?\);</script>\s*'
    r'<div class="flex-row">\s*'
    r'<div[^>]*width:\s*([0-9]+)%[^>]*>\s*'
    r'(.*?)'
    r'\s*</div>\s*'
    r'<div[^>]*width:\s*([0-9]+)%[^>]*>\s*'
    r'<figure class="mj-fig">\s*'
    r'<img src="([^"]+)" class="mj-fig-img">\s*'
    r'(?:<figcaption class="mj-fig-cap">\s*'
    r'(.*?)\s*'
    r'</figcaption>\s*)?'
    r'</figure>\s*'
    r'</div>\s*'
    r'</div>\s*$',
    re.DOTALL,
)


_SECTION_MEDIA_RE = re.compile(
    r'(^|\n)'
    r'(#{1,6})\s+([^\n]+?)\s*\n+'
    r'\s*<figcaption class="mj-slide-cap">\s*(.*?)\s*</figcaption>\s*\n+'
    r'\s*<script>setSectionBackground\(\'([^\']+)\'\s*,\s*\'([^\']+)\'(?:,\s*true)?\);</script>'
    r'(?=\n|$)',
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


_BACKGROUND_SCRIPT_RE = re.compile(
    r'\s*<script>setSectionBackground\(.*?\);</script>\s*',
    re.DOTALL,
)


_DEFINITION_BLOCK_RE = re.compile(
    r'\s*(?:-\s+)?<div class="alert alert-block alert-success">\s*'
    r'<b>[^:]+:\s*(.*?)</b>\s*'
    r'(.*?)'
    r'</div>\s*',
    re.DOTALL,
)


_WARNING_BLOCK_RE = re.compile(
    r'\s*<div class="alert alert-block alert-warning">\s*'
    r'(?:<b>(.*?)</b>\s*)?'
    r'(.*?)'
    r'</div>\s*',
    re.DOTALL,
)


_INFO_BLOCK_RE = re.compile(
    r'\s*<div class="alert alert-block alert-info">\s*'
    r'(?:<b>(.*?)</b>\s*)?'
    r'(.*?)'
    r'</div>\s*',
    re.DOTALL,
)


_MJ_FIGURE_RE = re.compile(
    r'<figure class="mj-fig">\s*'
    r'<img src="([^"]+)" class="mj-fig-img">\s*'
    r'(?:<figcaption class="mj-fig-cap">\s*'
    r'(.*?)\s*'
    r'</figcaption>\s*)?'
    r'</figure>',
    re.DOTALL,
)


_HTML_FIGURE_RE = re.compile(
    r'(?:<center>\s*)?'
    r'<figure(?:\s+class="[^"]*")?>\s*'
    r'<img src="([^"]+)"[^>]*>\s*'
    r'(?:<figcaption>\s*(.*?)\s*</figcaption>\s*)?'
    r'</figure>[ \t]*'
    r'(?:</center>)?',
    re.DOTALL,
)


_VIDEO_RE = re.compile(
    r'<video\b[^>]*>\s*'
    r"<source src=['\"]([^'\"]+)['\"][^>]*>\s*"
    r'.*?'
    r'</video>',
    re.DOTALL,
)


_HTML_LIST_RE = re.compile(
    r'<ul>\s*(.*?)\s*(?:</ul>|<ul>(?=\s*</div>|\s*$)|$)',
    re.DOTALL | re.IGNORECASE,
)


_HTML_IMG_RE = re.compile(
    r'<img src="([^"]+)"[^>]*>',
    re.DOTALL,
)


def convert_midjourney_figures(source: str) -> str:
    """Replace legacy Midjourney HTML figure blocks with Quarto image syntax."""
    def repl(match: re.Match) -> str:
        image_path = match.group(1).strip()
        caption = _normalize_whitespace(match.group(2) or "")
        if caption:
            return f'![{caption}]({image_path}){{class="midjourneyXX"}}'
        return f'![]({image_path}){{class="midjourney"}}'

    return _MJ_FIGURE_RE.sub(repl, source)


def convert_html_figures(source: str) -> str:
    """Replace generic HTML figure blocks with Quarto image syntax."""
    def repl(match: re.Match) -> str:
        image_path = match.group(1).strip()
        caption = _normalize_whitespace(match.group(2) or "")
        return f'![{caption}]({image_path})' if caption else f'![]({image_path})'

    return _HTML_FIGURE_RE.sub(repl, source)


def convert_videos(source: str) -> str:
    """Replace simple HTML video blocks with markdown media syntax."""
    def repl(match: re.Match) -> str:
        media_path = match.group(1).strip()
        return f"![]({media_path})"

    return _VIDEO_RE.sub(repl, source)


def convert_html_images(source: str) -> str:
    """Replace standalone HTML img tags with markdown image syntax."""
    def repl(match: re.Match) -> str:
        image_path = match.group(1).strip()
        return f"![]({image_path})"

    return _HTML_IMG_RE.sub(repl, source)


_CENTER_BLOCK_RE = re.compile(
    r"<center>\s*(.*?)\s*</center>",
    re.DOTALL | re.IGNORECASE,
)


def unwrap_center_wrappers(source: str) -> str:
    """Unwrap legacy center wrappers around already-converted markdown or media."""
    source = _CENTER_BLOCK_RE.sub(lambda match: match.group(1).strip(), source)
    source = re.sub(r"(?im)^[ \t]*<center>[ \t]*\n?", "", source)
    source = re.sub(r"(?im)^[ \t]*</center>[ \t]*\n?", "", source)
    return source


def remove_stray_list_tags(source: str) -> str:
    """Drop stray list wrapper tags left behind after HTML list conversion."""
    source = re.sub(r"</ul>", "", source, flags=re.IGNORECASE)
    source = re.sub(r"<ul>", "", source, flags=re.IGNORECASE)
    return source


def convert_html_lists(source: str) -> str:
    """Replace simple HTML unordered lists with markdown bullet lists."""
    def items_to_lines(inner: str) -> list[str]:
        lines: list[str] = []
        for match in re.finditer(r'<li([^>]*)>(.*?)</li>', inner, re.DOTALL | re.IGNORECASE):
            attrs, item = match.groups()
            text = re.sub(r"<br\s*/?>", "\n", item, flags=re.IGNORECASE)
            text = re.sub(r"<[^>]+>", "", text)
            text = _normalize_whitespace(text)
            if text:
                if re.search(r"color\s*:\s*orange", attrs, re.IGNORECASE) or text.startswith("Problem:"):
                    text = f"*{text}*"
                lines.append(f"- {text}")
        return lines

    def repl(match: re.Match) -> str:
        lines = items_to_lines(match.group(1))
        return "\n".join(lines) if lines else match.group(0)

    source = re.sub(r"<br\s*/?>", "\n", source, flags=re.IGNORECASE)
    source = _HTML_LIST_RE.sub(repl, source)
    if "<li" in source and not re.search(r"<div\b|<figure\b|<img\b|<video\b", source, re.IGNORECASE):
        lines = items_to_lines(source)
        if lines:
            source = re.sub(r"</?ul>", "", source, flags=re.IGNORECASE)
            source = re.sub(r"<li\b[^>]*>.*?</li>", "", source, flags=re.DOTALL | re.IGNORECASE)
            source = source.strip()
            list_block = "\n".join(lines)
            source = f"{source}\n\n{list_block}" if source else list_block
    return source


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


_QMD_COLUMNS_RE = re.compile(
    r':::: \{\.columns\}\n'
    r'((?:::: \{\.column(?: width="([^"]+)")?\}\n.*?\n:::\n)+)'
    r'::::',
    re.DOTALL,
)


_QMD_COLUMN_RE = re.compile(
    r'::: \{\.column(?: width="([^"]+)")?\}\n(.*?)\n:::',
    re.DOTALL,
)


def _parse_column_width(width: str | None, fallback: float) -> float:
    if not width:
        return fallback
    match = re.fullmatch(r"([0-9]+(?:\.[0-9]+)?)%", width.strip())
    if not match:
        return fallback
    return float(match.group(1))


def convert_qmd_columns_to_macros(text: str) -> str:
    """Convert simple Quarto columns blocks into %%col macros for QMDX export."""
    def repl(match: re.Match) -> str:
        columns_block = match.group(1)
        columns = _QMD_COLUMN_RE.findall(columns_block)
        if len(columns) < 2:
            return match.group(0)

        fallback_width = 100 / len(columns)
        widths = [round(_parse_column_width(width, fallback_width)) for width, _ in columns]
        parts = [f"%%col {' '.join(str(width) for width in widths)}", ""]
        for index, (_, content) in enumerate(columns):
            parts.append(content.strip())
            parts.append("")
            if index < len(columns) - 1:
                parts.append("%%sep")
                parts.append("")
        parts.append("%%/col")
        return "\n".join(parts)

    return _QMD_COLUMNS_RE.sub(repl, text)


def cleanup_qmdx(text: str) -> str:
    """Apply small QMDX-specific cleanup rewrites after macro compression."""
    text = re.sub(
        r"%%slides\s*\n\s*%%final\s*\n\s*%%/slides",
        "%%final",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"%%book\s*\n\s*%%book\s*\n",
        "%%book\n\n",
        text,
    )
    text = re.sub(
        r"%%book\s*\n\s*(#{1,2}\s+[^\n]+)\s*\n\s*%%book\s*\n",
        r"\1\n\n%%book\n",
        text,
    )
    text = re.sub(
        r"%%/book\s*\n\s*%%/book",
        "%%/book",
        text,
    )
    return text


def ensure_heading_spacing(text: str) -> str:
    """Ensure level-1/2 headings and %%final are preceded by two blank lines."""
    lines = text.splitlines()
    out: list[str] = []

    for line in lines:
        if re.match(r"^#{1,2}\s", line) or line.strip() == "%%final":
            trailing_blanks = 0
            idx = len(out) - 1
            while idx >= 0 and out[idx] == "":
                trailing_blanks += 1
                idx -= 1
            needed = 2 if out else 0
            while trailing_blanks < needed:
                out.append("")
                trailing_blanks += 1
        out.append(line)

    return "\n".join(out)


def ensure_list_spacing(text: str) -> str:
    """Ensure bullet and ordered lists are preceded by exactly one blank line."""
    lines = text.splitlines()
    out: list[str] = []

    for idx_in, line in enumerate(lines):
        if re.match(r"^(?:-\s|\d+\.\s)", line):
            prev_input = lines[idx_in - 1] if idx_in > 0 else ""
            if re.match(r"^(?:-\s|\d+\.\s)", prev_input):
                out.append(line)
                continue
            trailing_blanks = 0
            idx = len(out) - 1
            while idx >= 0 and out[idx] == "":
                trailing_blanks += 1
                idx -= 1
            if idx >= 0 and trailing_blanks == 0:
                out.append("")
            elif trailing_blanks > 1:
                del out[-(trailing_blanks - 1):]
        out.append(line)

    return "\n".join(out)


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


def remove_background_scripts(source: str) -> str:
    """Drop leftover standalone background script tags after higher-level rewrites."""
    return _BACKGROUND_SCRIPT_RE.sub("\n", source)


def convert_definition_block(source: str) -> str:
    """Convert legacy HTML definition alerts into %%def blocks."""
    def repl(match: re.Match) -> str:
        term, body = match.groups()
        term = _normalize_whitespace(term)
        body = body.strip()
        return f"\n%%def {term}\n{body}\n%%/def\n"

    converted = _DEFINITION_BLOCK_RE.sub(repl, source)
    return converted.lstrip("\n")


def convert_warning_block(source: str) -> str:
    """Convert legacy HTML warning alerts into warning macros."""
    def repl(match: re.Match) -> str:
        raw_title, body = match.groups()
        raw_title = raw_title or ""
        title = _normalize_whitespace(re.sub(r"<[^>]+>", "", raw_title))
        title = re.sub(r"^[^A-Za-zÄÖÜäöüß]*", "", title).rstrip(":").strip()
        body = body.strip()
        title_part = f" {title}" if title else ""
        return f"\n%%warning{title_part}\n{body}\n%%/warning\n"

    converted = _WARNING_BLOCK_RE.sub(repl, source)
    return converted.lstrip("\n")


def convert_info_block(source: str) -> str:
    """Convert legacy HTML info alerts into note macros."""
    def repl(match: re.Match) -> str:
        raw_title, body = match.groups()
        raw_title = raw_title or ""
        title = _normalize_whitespace(re.sub(r"<[^>]+>", "", raw_title))
        title = re.sub(r"^[^A-Za-zÄÖÜäöüß]*", "", title).rstrip(":").strip()
        body = body.strip()
        if title.lower() == "warning":
            return f"\n%%warning {title}\n{body}\n%%/warning\n"
        title_part = f" {title}" if title else ""
        return f"\n%%note{title_part}\n{body}\n%%/note\n"

    converted = _INFO_BLOCK_RE.sub(repl, source)
    return converted.lstrip("\n")


def convert_section_media_block(source: str) -> str:
    """Convert heading + slide caption + background media into compact section syntax."""
    def repl(match: re.Match) -> str:
        prefix, heading_level, heading_text, caption, background, media_path = match.groups()
        heading_text = _normalize_whitespace(heading_text)
        caption = _normalize_whitespace(caption)
        background = _normalize_hex_color(background)
        replacement = (
            f'{heading_level} {heading_text} '
            f'{{colR '
            f'capR="{_escape_shortcode_attr(caption)}" '
            f'imgR="{_escape_shortcode_attr(media_path.strip())}" '
            f'background="{_escape_shortcode_attr(background)}"}}'
        )
        return f"{prefix}{replacement}"

    return _SECTION_MEDIA_RE.sub(repl, source)


def convert_lecture_question_block(source: str) -> str:
    """Convert the lecture-hall-question HTML layout into a compact shortcode heading."""
    match = _LECTURE_QUESTION_RE.match(source.strip())
    if match:
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

    match = _LECTURE_QUESTION_MD_IMAGE_RE.match(source.strip())
    if match:
        heading_level, heading_text, background, left_width, left_text, right_width, caption, image_path = match.groups()
        heading_text = _normalize_heading_text(heading_text)
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

    match = _LECTURE_QUESTION_STYLE_FIGURE_RE.match(source.strip())
    if not match:
        return source

    heading_level, heading_text, background, left_width, left_text, right_width, image_path, caption = match.groups()
    heading_text = _normalize_heading_text(heading_text)
    left_text = _normalize_whitespace(left_text)
    caption = _normalize_whitespace(caption or "")

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


def _extract_malformed_flex_columns(block_text: str) -> list[tuple[int, str]]:
    """Fallback extractor for malformed nested flex-row markup."""
    matches = re.findall(
        r'<div class="[^"]*\bcol(\d+)\b[^"]*">\s*(.*?)\s*</div>',
        block_text,
        re.DOTALL,
    )
    if len(matches) < 2:
        return []
    return [(int(weight), content.strip()) for weight, content in matches]


def convert_style_columns(source: str) -> str:
    """Convert generic inline-style width columns into Quarto columns blocks."""
    lines = source.splitlines()
    out: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]
        if not re.search(r'<div style="[^"]*overflow:\s*hidden;?[^"]*">', line):
            out.append(line)
            i += 1
            continue

        block_lines = [line]
        depth = _div_delta(line)
        i += 1
        while i < len(lines) and depth > 0:
            block_lines.append(lines[i])
            depth += _div_delta(lines[i])
            i += 1

        inner_lines = block_lines[1:-1]
        columns: list[tuple[str, str]] = []
        j = 0
        failed = depth != 0

        while j < len(inner_lines):
            inner = inner_lines[j]
            match = re.search(r'<div style="[^"]*width:\s*([0-9]+)%[^"]*">', inner)
            if not match:
                if inner.strip():
                    failed = True
                    break
                j += 1
                continue

            width = match.group(1)
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

            columns.append((width, "\n".join(column_lines).strip()))

        if failed or len(columns) < 2:
            out.extend(block_lines)
            continue

        out.append(":::: {.columns}")
        for width, content in columns:
            out.append(f'::: {{.column width="{width}%"}}')
            if content:
                out.append("")
                out.append(content)
                out.append("")
            out.append(":::")
        out.append("::::")

    return "\n".join(out)


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
            columns = _extract_malformed_flex_columns("\n".join(block_lines))
        if not columns:
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
    source = convert_definition_block(source)
    source = convert_warning_block(source)
    source = convert_info_block(source)
    source = remove_background_scripts(source)
    source = convert_html_lists(source)
    source = remove_stray_list_tags(source)
    source = convert_style_columns(source)
    source = convert_flex_rows(source)
    source = convert_midjourney_figures(source)
    source = convert_html_figures(source)
    source = convert_videos(source)
    source = convert_html_images(source)
    source = unwrap_center_wrappers(source)
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
    """Preserve wrapped block boundaries to keep book/slide flow close to notebook cell order."""
    return items


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
    image_credit = ""
    background_video = f"images/{lecture_id}/mj_title.mp4"
    title_cell_idx = None
    for idx, cell in enumerate(cells):
        if cell["cell_type"] == "markdown":
            src = join_source(cell)
            if is_title_slide(src):
                title = extract_title(src)
                image_credit = extract_image_credit(src)
                extracted_video = extract_background_video(src)
                if extracted_video:
                    background_video = extracted_video
                title_cell_idx = idx
                break

    # ---- Pass 2: convert cells -------------------------------------------
    items: list[Item] = [("raw", make_frontmatter(title, lecture_id, image_credit, background_video))]

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
            full_cell_conversion = convert_markdown_cell(source)

            # Heading-only cells:
            #   • skip → wrap unless-format (docs only, no slide break in revealjs)
            #   • remove-cell tag → wrap when-format (slides only)
            #   • slide/subslide/fragment/'' → emit raw (section marker in HTML
            #     AND slide break / heading in revealjs)
            if is_heading_only(source):
                content = full_cell_conversion + "\n"
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
                if full_cell_conversion.strip() != source.strip() and full_cell_conversion.lstrip().startswith("#"):
                    items.append(("raw", full_cell_conversion))
                    continue
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

            content = full_cell_conversion
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
    output = ensure_list_spacing(ensure_heading_spacing(render_blocks(merge_blocks(items))))
    qmdx_source = convert_qmd_columns_to_macros(output)
    qmdx_output = compress_to_qmdx(qmdx_source, lang=infer_lang(ipynb_path))
    qmdx_output = cleanup_qmdx(qmdx_output)
    qmdx_output = ensure_list_spacing(ensure_heading_spacing(qmdx_output))
    qmdx_path = qmd_path.with_suffix(".qmdx")

    # ---- Write output -------------------------------------------------------
    qmd_path.parent.mkdir(parents=True, exist_ok=True)
    with open(qmdx_path, "w", encoding="utf-8") as f:
        f.write(qmdx_output)
        if not qmdx_output.endswith("\n"):
            f.write("\n")

    print(f"Converted:  {ipynb_path}")
    print(f"Internal QMD: {qmd_path} (not saved)")
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
