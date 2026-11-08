import asyncio
import concurrent.futures
import glob
import http.server
import os
import re
import shutil
import socket
import subprocess
import sys
import threading
import time
from pathlib import Path

from ai4sc_style.preprocess import preprocess_file, preprocess_lectures
from invoke import Exit, task
from pyppeteer import launch
from termcolor import cprint

HERE = Path(__file__).parent

_STAMP_DIR = HERE / "lectures" / ".stamps"

# Local clone of https://github.com/AI4SC/qi4sc-quarto-template (private repo).
# quarto's GitHub installer needs a valid GITHUB_TOKEN for private repos, so we
# pull this local clone instead. lectures/_extensions is a symlink to its
# _extensions folder (see link_extensions), so fixes made in the template apply directly.
AI4SC_TEMPLATE_DIR = os.environ.get(
    "AI4SC_TEMPLATE_DIR",
    "/Users/jplonnigs/Documents/code/Presentations/2026/template",
)


def _find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def _port_free(port: int) -> bool:
    """True if nothing listens on *port* and we can bind it."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.2)
        if s.connect_ex(("127.0.0.1", port)) == 0:
            return False
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("", port))
        return True
    except OSError:
        return False


def _pick_port(port: int, start: int) -> int:
    """Use *port* if given (fail if busy), else the first free port from *start* on."""
    if port:
        if not _port_free(port):
            raise Exit(f"Port {port} is already in use", code=2)
        return port
    for p in range(start, start + 50):
        if _port_free(p):
            return p
    return _find_free_port()


def _start_http_server(directory: str, port: int):
    class _Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

        def log_message(self, *args):
            pass

    class _Server(http.server.ThreadingHTTPServer):
        def handle_error(self, *_):
            pass  # silence BrokenPipeError when browsers abort mid-transfer

    srv = _Server(("localhost", port), _Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def _stamp_path(name: str) -> Path:
    _STAMP_DIR.mkdir(exist_ok=True)
    return _STAMP_DIR / name


def _is_stale(qmdx_stem: str, kind: str) -> bool:
    """True if the *kind* build for *qmdx_stem* is out of date."""
    stamp = _stamp_path(f"{qmdx_stem}.{kind}")
    if not stamp.exists():
        return True
    qmdx = HERE / "lectures" / f"{qmdx_stem}.qmdx"
    if not qmdx.exists():
        return False
    return qmdx.stat().st_mtime > stamp.stat().st_mtime


def _mark_fresh(qmdx_stem: str, kind: str) -> None:
    _stamp_path(f"{qmdx_stem}.{kind}").touch()


def _any_qmdx_stale(kind: str) -> bool:
    return any(_is_stale(q.stem, kind) for q in (HERE / "lectures").glob("*.qmdx"))


def _mark_all_fresh(kind: str) -> None:
    for q in (HERE / "lectures").glob("*.qmdx"):
        _mark_fresh(q.stem, kind)


def _inject_pdf_link(p: Path) -> None:
    fn = p.name
    fnspdf = fn.replace(".page.html", ".slide.pdf")
    text = p.read_text()
    # Quarto appends " (ext-name)" to format-link labels for extension formats
    text = re.sub(r'(</i>[^<]+?) \([^)]+\)(</a></li>)', r'\1\2', text)
    if fnspdf not in text:
        text = text.replace(
            '</i>Slides</a></li>',
            f'</i>Slides</a></li><li><a href="{fnspdf}">'
            f'<i class="bi bi-file-earmark-easel"></i>Slides PDF</a></li>'
        )
    p.write_text(text)


def _clean_lectures_artifacts(lecture_dir: Path) -> None:
    """Delete intermediate build artifacts from lectures/, preserving caches."""
    patterns = [
        "*.qmd", "*.slide.html", "*.slide.pdf",
        "*.page.html", "*.page.pdf",
        "*.quarto_ipynb", "*.quarto_ipynb_*", "*.typ",
    ]
    for pattern in patterns:
        for f in lecture_dir.glob(pattern):
            f.unlink()
    for d in lecture_dir.iterdir():
        if d.is_dir() and d.name.endswith("_files"):
            shutil.rmtree(d)


@task
def clean(c, docs=False, bytecode=False, extra=""):
    patterns = ["_build"]
    if docs:
        patterns.append("docs/_build")
    if bytecode:
        patterns.append("**/*.pyc")
    if extra:
        patterns.append(extra)
    for pattern in patterns:
        c.run("rm -rf {}".format(pattern))
    _clean_lectures_artifacts(HERE / "lectures")
    if _STAMP_DIR.exists():
        shutil.rmtree(str(_STAMP_DIR))


def _crop_pdf_pages(pdf_path, fx, fy, fw, fh):
    """Set CropBox on every page using fractions (0–1) of the MediaBox."""
    import pypdf
    from pypdf.generic import RectangleObject
    reader = pypdf.PdfReader(pdf_path)
    writer = pypdf.PdfWriter()
    for page in reader.pages:
        pw = float(page.mediabox.width)
        ph = float(page.mediabox.height)
        left = fx * pw
        right = (fx + fw) * pw
        top = ph - fy * ph          # PDF y=0 is at bottom
        bottom = ph - (fy + fh) * ph
        page.cropbox = RectangleObject([left, bottom, right, top])
        writer.add_page(page)
    with open(pdf_path, "wb") as f:
        writer.write(f)


def _detect_content_bounds_from_pdf(pdf_path: str) -> dict | None:
    """Render up to 5 pages via pdftoppm, detect the non-white content bounding box.

    Scans multiple pages and uses the one with the tallest dark area (most content),
    so a minimal title slide doesn't give misleading bounds.
    Returns fractions (0–1) of the PDF page dimensions, or None on failure.
    """
    import subprocess
    import tempfile
    import numpy as np
    from PIL import Image

    with tempfile.TemporaryDirectory() as tmp:
        try:
            subprocess.run(
                ["pdftoppm", "-r", "72", "-f", "1", "-l", "5", "-png", pdf_path, f"{tmp}/page"],
                check=True, capture_output=True,
            )
        except Exception:
            return None
        pages = sorted(Path(tmp).glob("*.png"))
        if not pages:
            return None

        best = None
        best_h = 0
        for png in pages:
            img = Image.open(png).convert("RGB")
            arr = np.array(img)
            content = ~np.all(arr >= 240, axis=2)
            row_counts = np.sum(content, axis=1)
            col_counts = np.sum(content, axis=0)
            # Threshold at 5% of the peak count — filters scattered noise while
            # keeping real content even on light slides with few dark pixels
            row_thresh = max(10, int(row_counts.max() * 0.05))
            col_thresh = max(10, int(col_counts.max() * 0.05))
            rows = row_counts >= row_thresh
            cols = col_counts >= col_thresh
            if not rows.any():
                continue
            y0 = int(np.argmax(rows))
            y1 = int(len(rows) - 1 - np.argmax(rows[::-1]))
            x0 = int(np.argmax(cols))
            x1 = int(len(cols) - 1 - np.argmax(cols[::-1]))
            h = y1 - y0
            if h > best_h:
                best_h = h
                best = (x0, y0, x1, y1, img.width, img.height)

        if best is None:
            return None
        x0, y0, x1, y1, iw, ih = best
        return {"fx": x0 / iw, "fy": y0 / ih, "fw": (x1 - x0 + 1) / iw, "fh": (y1 - y0 + 1) / ih}


def error(text):
    cprint(text, "red")


def info(text):
    cprint(text, "blue")


async def html_to_pdf(url, output_file):
    """Convert a HTML file to a PDF"""
    info(f"Convert {url} to {output_file}")
    try:
        browser = await launch(
            headless=True,
            args=["--no-sandbox"],
            handleSIGINT=False,
            handleSIGTERM=False,
            handleSIGHUP=False,
            autoClose=False,
            defaultViewport=dict(width=1920, height=1080, isLandscape=True),
        )
        page = await browser.newPage()
        await page.goto(url, {"waitUntil": ["load"], "timeout": 60000})
        # Reveal.js expands the print layout asynchronously after load — wait for it
        await page.waitForFunction("document.body.scrollHeight > window.innerHeight", timeout=10000)
        result = await page.evaluate(
            """async () => {
                // Wait for plotly-loader.js to finish loading Plotly and draining the queue
                if (window.PLOTLY_READY && typeof window.PLOTLY_READY.then === 'function') {
                    try { await window.PLOTLY_READY; } catch(e) {}
                }
                // Poll until every plot has a rendered SVG (drainQueuedPlotlyCalls is fire-and-forget)
                const allPlots = [...document.querySelectorAll('.plotly-graph-div')];
                const t0 = Date.now();
                while (allPlots.length > 0 && Date.now() - t0 < 20000) {
                    if (allPlots.every(el => el.querySelector('svg.main-svg'))) break;
                    await new Promise(r => setTimeout(r, 400));
                }
                // Videos do not print: replace each with its poster image (last frame)
                for (const v of [...document.querySelectorAll('video')]) {
                    if (!v.poster) continue;
                    const img = document.createElement('img');
                    img.src = v.poster;
                    img.style.cssText = v.getAttribute('style') || 'width:100%;display:block;';
                    v.replaceWith(img);
                }
                // Keep @media print from collapsing plot containers
                const style = document.createElement('style');
                style.textContent =
                    '@media print {' +
                    '  .plotly-graph-div, .cell-output-display, .cell-output, .quarto-figure' +
                    '  { display:block!important; visibility:visible!important; overflow:visible!important; }' +
                    '  .plotly-graph-div svg { display:block!important; }' +
                    '}';
                document.head.appendChild(style);
                // Replace each Plotly div with a static SVG image so it survives page.pdf()
                let converted = 0;
                const errors = [];
                const missing = [];
                for (const el of allPlots) {
                    try {
                        const svg = el.querySelector('svg.main-svg');
                        if (svg) {
                            const h = el.style.height || '450px';
                            const img = document.createElement('img');
                            img.src = 'data:image/svg+xml;charset=utf-8,'
                                + encodeURIComponent(new XMLSerializer().serializeToString(svg));
                            img.style.cssText = 'width:100%;height:' + h + ';display:block;';
                            el.replaceWith(img);
                            converted++;
                        } else {
                            missing.push(el.id || '?');
                        }
                    } catch(e) { errors.push(String(e)); }
                }
                return {plots: allPlots.length, converted,
                        missing: missing.slice(0, 5), errors: errors.slice(0, 5)};
            }"""
        )
        info(f"  plot conversion: {result}")
        await page.pdf(
            path=output_file,
            printBackground=True,
            width="1920px",
            height="1080px",
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        )
        # Render the first PDF page to a raster, detect the non-white content bounds,
        # and set a CropBox to remove the surrounding whitespace on every page.
        bounds = _detect_content_bounds_from_pdf(output_file)
        info(f"  detected content bounds: {bounds}")
        if bounds:
            _crop_pdf_pages(output_file, bounds["fx"], bounds["fy"], bounds["fw"], bounds["fh"])
            info(f"  cropped to {bounds['fw']*100:.1f}%×{bounds['fh']*100:.1f}% at ({bounds['fx']*100:.1f}%,{bounds['fy']*100:.1f}%)")
    except Exception as ex:
        error(f"PDF render failed for {output_file}: {ex}")
        raise
    finally:
        if "browser" in locals() and browser:
            await browser.close()


def _sync_site_to_build(site_dir: Path, build_dir: Path, stale: list[Path], full_render: bool) -> None:
    """Copy quarto's lectures/_site output into _build/html_quarto."""
    if full_render:
        info("Sync lectures/_site to _build/html_quarto")
        if build_dir.exists():
            shutil.rmtree(str(build_dir))
        shutil.copytree(str(site_dir), str(build_dir))
        for p in build_dir.glob("*.html"):
            _inject_pdf_link(p)
    else:
        info("Incrementally updating _build/html_quarto")
        build_dir.mkdir(parents=True, exist_ok=True)
        for qmdx in stale:
            stem = qmdx.stem
            for src in site_dir.iterdir():
                name = src.name
                if name == stem or name.startswith(stem + ".") or name.startswith(stem + "_"):
                    dst = build_dir / name
                    if src.is_dir():
                        if dst.exists():
                            shutil.rmtree(str(dst))
                        shutil.copytree(str(src), str(dst))
                    else:
                        shutil.copy2(str(src), str(dst))
                        if name.endswith(".html"):
                            _inject_pdf_link(dst)
        for src in site_dir.iterdir():
            dst = build_dir / src.name
            if src.is_file() and (not dst.exists() or src.stat().st_mtime > dst.stat().st_mtime):
                shutil.copy2(str(src), str(dst))
            elif src.is_dir() and not src.name.endswith("_files"):
                # Merge file by file: a directory's mtime does not change when files
                # inside a nested folder (images/<lecture>/x.png) are added or updated.
                for f in src.rglob("*"):
                    if not f.is_file():
                        continue
                    target = dst / f.relative_to(src)
                    if not target.exists() or f.stat().st_mtime > target.stat().st_mtime:
                        target.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(str(f), str(target))


@task()
def build_quarto_book(c):
    info("Build quarto book ALL")
    preprocess_lectures(HERE / "lectures")

    build_dir = HERE / "_build" / "html_quarto"
    stale = [q for q in sorted((HERE / "lectures").glob("*.qmdx"))
             if _is_stale(q.stem, "quarto")]
    if not stale and build_dir.exists():
        info("Quarto book up to date, skipping render")
        return

    site_dir = HERE / "lectures" / "_site"
    full_render = not build_dir.exists()

    if not full_render and not site_dir.exists():
        info("Restoring _site from _build/html_quarto for incremental render")
        shutil.copytree(str(build_dir), str(site_dir))

    render_list = sorted((HERE / "lectures").glob("*.qmdx")) if full_render else stale
    with c.cd(os.path.join("lectures")):
        for qmdx in render_list:
            c.run(f"quarto render {qmdx.stem}.qmd")
            _sync_site_to_build(site_dir, build_dir, [qmdx], False)
            # Stamp per lecture so an interrupted run keeps its progress
            _mark_fresh(qmdx.stem, "quarto")

    _clean_lectures_artifacts(HERE / "lectures")


@task()
def build_quarto_book_quick(c):
    info("Build quarto book QUICK")
    preprocess_lectures(HERE / "lectures")
    site_dir = HERE / "lectures" / "_site"
    build_dir = HERE / "_build" / "html_quarto"
    stale = [q for q in sorted((HERE / "lectures").glob("*.qmdx"))
             if _is_stale(q.stem, "quarto_quick")]
    if not stale and build_dir.exists():
        info("Quarto book up to date, skipping render")
        _clean_lectures_artifacts(HERE / "lectures")
        return
    full_render = not build_dir.exists()
    if not full_render and not site_dir.exists():
        info("Restoring _site from _build/html_quarto for incremental render")
        shutil.copytree(str(build_dir), str(site_dir))
    if full_render and not stale:
        stale = sorted((HERE / "lectures").glob("*.qmdx"))
    render_list = sorted((HERE / "lectures").glob("*.qmdx")) if full_render else stale
    with c.cd(os.path.join("lectures")):
        for qmdx in render_list:
            c.run(f"quarto render {qmdx.stem}.qmd --no-execute")
            _sync_site_to_build(site_dir, build_dir, [qmdx], False)
            # Stamp per lecture so an interrupted run keeps its progress
            _mark_fresh(qmdx.stem, "quarto_quick")

    _clean_lectures_artifacts(HERE / "lectures")


@task()
def build_quarto_pdf(c):
    if not os.path.isdir("_build/html_quarto"):
        return
    files = [fn for fn in os.listdir("_build/html_quarto") if fn.endswith(".slide.html")]
    jobs = []
    for fn in files:
        stem = Path(fn).stem.replace(".slide", "")
        fno = os.path.abspath(os.path.join("_build", "html_quarto", fn.replace(".slide.html", ".slide.pdf")))
        if _is_stale(stem, "pdf") or not Path(fno).exists():
            jobs.append((stem, fn, fno))
    if jobs:
        # Serve over HTTP so <script type="module"> (plotly-loader.js) works in headless Chrome.
        # file:// URLs block ES module loading due to CORS, causing Plotly to never initialise.
        serve_dir = os.path.abspath("_build/html_quarto")
        port = _find_free_port()
        srv = _start_http_server(serve_dir, port)
        try:
            pool = concurrent.futures.ThreadPoolExecutor()
            futures = {
                pool.submit(asyncio.run, html_to_pdf(f"http://localhost:{port}/{fn}?view=print", fno)): (stem, fn, fno)
                for stem, fn, fno in jobs
            }
            failed = []
            for future, (stem, fn, fno) in futures.items():
                try:
                    future.result()
                    _mark_fresh(stem, "pdf")
                except Exception as ex:
                    error(f"PDF render failed for {fn}: {ex}")
                    failed.append(fn)
            pool.shutdown()
        finally:
            srv.shutdown()
        if failed:
            error(f"PDF render failed for {len(failed)} file(s): {', '.join(failed)}")
    build_dir = HERE / "_build" / "html_quarto"
    for p in build_dir.glob("*.page.html"):
        _inject_pdf_link(p)


@task()
def build(c, all=False):
    info("Build Quarto")
    if all:
        build_quarto_book(c)
        build_quarto_pdf(c)
    else:
        build_quarto_book_quick(c)


@task()
def build_quarto_book_full(c):
    info("Build quarto book FULL (clears all caches)")
    build_dir = HERE / "_build" / "html_quarto"
    site_dir = HERE / "lectures" / "_site"
    if build_dir.exists():
        shutil.rmtree(str(build_dir))
    if site_dir.exists():
        shutil.rmtree(str(site_dir))
    if _STAMP_DIR.exists():
        shutil.rmtree(str(_STAMP_DIR))
    build_quarto_book(c)


@task()
def ghp_import_quarto(c):
    c.run("ghp-import -n -p -f _build/html_quarto")


@task()
def restart_book_ml2(c):
    """Restart the book-ml2 deployment pod on the ai4sc-lectures k8s cluster."""
    info("Restart book-ml2 pod on ai4sc-lectures")
    c.run("ssh ai4sc-lectures 'microk8s kubectl rollout restart deployment/book-ml2 -n books'")


@task()
def publish(c):
    build_quarto_book(c)
    build_quarto_pdf(c)
    ghp_import_quarto(c)
    restart_book_ml2(c)


@task(help={"port": "Port to use (default: 8081 or the next free one)"})
def serve(c, port=0):
    """Serve _build/html_quarto on a free port."""
    site = HERE / "_build" / "html_quarto"
    if not site.is_dir():
        raise Exit(f"{site} does not exist; run `invoke build` first", code=2)
    port = _pick_port(int(port), 8081)
    info(f"Serving {site} at http://localhost:{port}/")
    if sys.platform == "win32":
        c.run(f"weave {port} to ./_build/html_quarto")
    elif sys.platform == "darwin":
        c.run(f"./weave_mac {port} to ./_build/html_quarto")
    else:
        srv = _start_http_server(str(site), port)
        try:
            while True:
                time.sleep(3600)
        except KeyboardInterrupt:
            srv.shutdown()


# ---------------------------------------------------------------------------
# Single-deck pipeline (render / preview), meant for agents in git worktrees.
# Works only on lectures/<deck>.* and lectures/_site; never touches
# _build/html_quarto or the .stamps of the full build.
# ---------------------------------------------------------------------------

LECTURES = HERE / "lectures"
SITE_DIR = LECTURES / "_site"
_QUARTO_FORMATS = {
    "html": "ai4sc-style-html",
    "typst": "typst",
    "slides": "ai4sc-style-revealjs",
}
# Fixed order: the html render deletes _site/<deck>.slide.html, so slides come after it.
_TARGET_ORDER = ["lint", "html", "typst", "slides", "pdf", "shots", "check"]
_TARGETS_ALL = ["lint", "html", "slides", "pdf", "shots", "check"]  # typst only on demand
_LINT_JS = LECTURES / "_extensions" / "ai4sc-style" / "scripts" / "lint.js"


# Linter and preprocessor share the format `file:line:col severity [code] message`.
_DIAG_RE = re.compile(r":(\d+):\d+ (error|warning) \[([\w-]+)\]")


def _diag_key(diag: str) -> tuple:
    """(line, code) of a diagnostic, used to drop duplicates between lint and preprocess."""
    m = _DIAG_RE.search(diag)
    return (int(m.group(1)), m.group(3)) if m else (diag,)


def _is_error(diag: str) -> bool:
    m = _DIAG_RE.search(diag)
    return bool(m and m.group(2) == "error")


def _lint(qmdx: Path, log_dir: Path) -> tuple[list[str], str | None]:
    """Run the ai4sc-style linter on the .qmdx; return (diagnostics, skip reason)."""
    if not _LINT_JS.exists():
        return [], f"{_LINT_JS} not found"
    if not shutil.which("node"):
        return [], "node not installed"
    r = subprocess.run(["node", str(_LINT_JS), qmdx.name], cwd=LECTURES,
                       capture_output=True, text=True)
    out = r.stdout + r.stderr
    (log_dir / "lint.txt").write_text(out)
    issues = [ln for ln in out.splitlines() if _DIAG_RE.search(ln)]
    for ln in issues:
        (error if _is_error(ln) else print)(ln)
    return issues, None


def _resolve_lecture(name: str) -> Path:
    """Map '02b', '02b_Datentypen', '02b_Datentypen.qmdx' or 'lectures/…' to the .qmdx."""
    stem = Path(name).name
    for suffix in (".qmdx", ".qmd"):
        if stem.endswith(suffix):
            stem = stem[: -len(suffix)]
    exact = LECTURES / f"{stem}.qmdx"
    if exact.exists():
        return exact
    matches = sorted(q for q in LECTURES.glob("*.qmdx") if q.stem.startswith(stem))
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise Exit(f"No lecture matches '{name}'", code=2)
    raise Exit(f"'{name}' is ambiguous: " + ", ".join(m.stem for m in matches), code=2)


def _require_in_project(stem: str) -> None:
    """Quarto renders a file outside project.render as a standalone document into
    lectures/ (not _site), so refuse instead of reporting a misleading success."""
    import yaml

    cfg = yaml.safe_load((LECTURES / "_quarto.yaml").read_text(encoding="utf-8")) or {}
    listed = (cfg.get("project") or {}).get("render") or []
    if listed and f"{stem}.qmd" not in listed:
        raise Exit(
            f"{stem}.qmd is not in project.render of lectures/_quarto.yaml; add it there "
            "(and to the sidebar) before rendering, otherwise Quarto writes a standalone "
            "file into lectures/ instead of _site/",
            code=2,
        )


def _main_checkout() -> Path:
    """Root of the main checkout, also when called from a git worktree."""
    try:
        common = subprocess.run(
            ["git", "rev-parse", "--path-format=absolute", "--git-common-dir"],
            cwd=HERE, check=True, capture_output=True, text=True,
        ).stdout.strip()
        return Path(common).parent
    except (OSError, subprocess.CalledProcessError):
        return HERE


def _seed_site() -> None:
    """Fill a missing lectures/_site from the built site, so links to other decks work."""
    if SITE_DIR.exists():
        return
    for src in (HERE / "_build" / "html_quarto", _main_checkout() / "_build" / "html_quarto"):
        if src.is_dir():
            info(f"Seeding {SITE_DIR} from {src}")
            shutil.copytree(str(src), str(SITE_DIR))
            return
    info("No built site found to seed lectures/_site; links to other decks will 404")


def _preprocess_one(qmdx: Path) -> list[str]:
    """Run the macro preprocessor on one file; return its diagnostics (also printed)."""
    diags: list[str] = []
    preprocess_file(qmdx, diagnostics=diags)
    info(f"Preprocessed {qmdx.name}")
    return diags


def _render_one(c, stem: str, target: str, execute: bool, log_dir: Path) -> tuple[bool, int]:
    """quarto render one deck to one format; return (ok, number of WARNING lines)."""
    cmd = f"quarto render {stem}.qmd --to {_QUARTO_FORMATS[target]}"
    if not execute:
        cmd += " --no-execute"
    info(cmd)
    with c.cd(str(LECTURES)):
        r = c.run(cmd, warn=True)
    log = (r.stdout or "") + (r.stderr or "")
    (log_dir / f"quarto-{target}.log").write_text(log)
    return r.ok, sum("WARNING" in ln for ln in log.splitlines())


def _slide_pdf(stem: str) -> Path:
    out = SITE_DIR / f"{stem}.slide.pdf"
    port = _find_free_port()
    srv = _start_http_server(str(SITE_DIR), port)
    try:
        # pyppeteer hangs on navigation when driven from the main thread; run it in a
        # worker thread like build_quarto_pdf does.
        url = f"http://localhost:{port}/{stem}.slide.html?view=print"
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            pool.submit(asyncio.run, html_to_pdf(url, str(out))).result()
    finally:
        srv.shutdown()
    page = SITE_DIR / f"{stem}.page.html"
    if page.exists():
        _inject_pdf_link(page)
    return out


def _contact_sheets(pdf: Path, log_dir: Path, cols: int = 3, rows: int = 4) -> list[Path]:
    """Tile the slide PDF pages into cols x rows PNG contact sheets."""
    import tempfile
    from PIL import Image, ImageDraw

    for old in log_dir.glob("sheet-*.png"):
        old.unlink()
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["pdftoppm", "-r", "40", "-png", str(pdf), f"{tmp}/p"], check=True)
        pages = sorted(Path(tmp).glob("p-*.png"))
        sheets = []
        per = cols * rows
        for i in range(0, len(pages), per):
            imgs = [Image.open(p).convert("RGB") for p in pages[i:i + per]]
            w = max(im.width for im in imgs)
            h = max(im.height for im in imgs)
            sheet = Image.new("RGB", (cols * w, rows * h), "white")
            draw = ImageDraw.Draw(sheet)
            for j, im in enumerate(imgs):
                x, y = (j % cols) * w, (j // cols) * h
                sheet.paste(im, (x, y))
                draw.rectangle([x, y, x + w - 1, y + h - 1], outline="gray")
                draw.text((x + 4, y + 2), str(i + j + 1), fill="red")
            path = log_dir / f"sheet-{i // per + 1:02d}.png"
            sheet.save(path)
            sheets.append(path)
    return sheets


_REF_PATTERNS = [
    re.compile(r"!\[[^\]]*\]\(\s*<?([^)\s>]+)"),                       # ![](path)
    re.compile(r"\b(?:imgR|imgL|img|src|poster|data-background-image|data-background-video"
               r"|data-background-video-poster|background-image)\s*=\s*\"([^\"]+)\""),
    re.compile(r"\{\{<\s*include\s+([^\s>]+)\s*>\}\}"),
]


def _missing_refs(qmd: Path) -> list[str]:
    """Local files referenced in the expanded .qmd that do not exist."""
    text = qmd.read_text(encoding="utf-8")
    refs = set()
    for pat in _REF_PATTERNS:
        refs.update(m.group(1) for m in pat.finditer(text))
    fm = re.match(r"---\n(.*?)\n---", text, re.S)
    if fm:
        res = re.search(r"^resources:\s*\n((?:[ \t]+-.*\n?)+)", fm.group(1) + "\n", re.M)
        if res:
            for line in res.group(1).splitlines():
                item = line.strip().lstrip("-").strip().strip("\"'")
                if item and not glob.glob(str(LECTURES / item)):
                    refs.add(item)
    missing = []
    for ref in sorted(refs):
        if re.match(r"^(?:[a-z]+:|#|//|\{\{)", ref):
            continue
        path = ref.split("#")[0].split("?")[0]
        if path and not glob.glob(str(LECTURES / path)):
            missing.append(ref)
    return missing


def _stray_fences(html: Path) -> list[str]:
    if not html.exists():
        return []
    text = html.read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"<(script|style)\b.*?</\1>", "", text, flags=re.S)
    return [re.sub(r"\s+", " ", text[max(0, m.start() - 80):m.end() + 80])
            for m in re.finditer(r":::+", text)]


def _clean_deck_artifacts(stem: str) -> None:
    for pattern in [f"{stem}.qmd", f"{stem}.quarto_ipynb*", f"{stem}.typ",
                    f"{stem}.slide.html", f"{stem}.slide.pdf", f"{stem}.page.html", f"{stem}.page.pdf"]:
        for f in LECTURES.glob(pattern):
            f.unlink()
    files_dir = LECTURES / f"{stem}_files"
    if files_dir.is_dir():
        shutil.rmtree(files_dir)


@task(
    help={
        "deck": "Lecture name or unique prefix, e.g. 02b",
        "to": "Comma list of lint,html,slides,pdf,shots,check,typst or 'all' (= all but typst)",
        "execute": "Execute code cells (default); --no-execute skips them",
        "keep": "Keep lectures/<deck>.qmd after the run",
        "strict": "Lint warnings also fail the run (errors always do)",
    }
)
def render(c, deck, to="html,slides", execute=True, keep=False, strict=False):
    """Render one deck to selected targets into lectures/_site, without the full build."""
    qmdx = _resolve_lecture(deck)
    stem = qmdx.stem
    targets = set()
    for t in (x.strip() for x in to.split(",") if x.strip()):
        if t == "all":
            targets.update(_TARGETS_ALL)
        elif t in _TARGET_ORDER:
            targets.add(t)
        else:
            raise Exit(f"Unknown target '{t}' (choose from {', '.join(_TARGET_ORDER)}, all)", code=2)

    slide_html = SITE_DIR / f"{stem}.slide.html"
    slide_pdf = SITE_DIR / f"{stem}.slide.pdf"
    if "shots" in targets and "pdf" not in targets and (
        not slide_pdf.exists() or not slide_html.exists()
        or slide_pdf.stat().st_mtime < slide_html.stat().st_mtime
    ):
        targets.add("pdf")
    if "pdf" in targets and "slides" not in targets and (
        "html" in targets or not slide_html.exists()
        or slide_html.stat().st_mtime < qmdx.stat().st_mtime
    ):
        targets.add("slides")
    if "html" in targets and "slides" not in targets and slide_html.exists():
        info(f"Note: the html render removes {slide_html.name}; add 'slides' to keep it")
    ordered = [t for t in _TARGET_ORDER if t in targets]
    if targets & {"html", "typst", "slides", "pdf", "shots"}:
        _require_in_project(stem)

    log_dir = HERE / "_build" / "render" / stem
    log_dir.mkdir(parents=True, exist_ok=True)
    _seed_site()

    results: dict[str, str] = {}
    failed = False
    pre_diags = _preprocess_one(qmdx)
    pre_errors = sum(map(_is_error, pre_diags))
    if pre_errors or (strict and pre_diags):
        failed = True
    lint_diags: list[str] = []
    quarto_warnings = 0
    sheets: list[Path] = []
    try:
        for t in ordered:
            if t == "lint":
                lint_diags, skipped = _lint(qmdx, log_dir)
                n_err = sum(map(_is_error, lint_diags))
                n_warn = len(lint_diags) - n_err
                if skipped:
                    results[t] = f"skipped ({skipped})"
                else:
                    bad = n_err > 0 or (strict and n_warn > 0)
                    results[t] = f"{'FAILED' if bad else 'ok'}, {n_err} error(s), {n_warn} warning(s)"
                    failed |= bad
            elif t in _QUARTO_FORMATS:
                ok, n = _render_one(c, stem, t, execute, log_dir)
                quarto_warnings += n
                results[t] = f"{'ok' if ok else 'FAILED'}, {n} warning(s)"
                failed |= not ok
            elif t == "pdf":
                try:
                    results[t] = f"ok → {_slide_pdf(stem).relative_to(HERE)}"
                except Exception as ex:
                    results[t] = f"FAILED: {ex}"
                    failed = True
            elif t == "shots":
                if slide_pdf.exists():
                    sheets = _contact_sheets(slide_pdf, log_dir)
                    results[t] = f"ok, {len(sheets)} sheet(s)"
                else:
                    results[t] = "FAILED: no slide PDF"
                    failed = True
            elif t == "check":
                # Preprocessor diagnostics always; lint errors (warnings with --strict)
                # unless the preprocessor already reported the same line and code.
                pre_keys = {_diag_key(d) for d in pre_diags}
                problems = [f"preprocess: {d}" for d in pre_diags]
                problems += [f"lint: {d}" for d in lint_diags
                             if (strict or _is_error(d)) and _diag_key(d) not in pre_keys]
                if quarto_warnings:
                    problems.append(f"quarto: {quarto_warnings} WARNING line(s), see {log_dir.relative_to(HERE)}/*.log")
                for html in (slide_html, SITE_DIR / f"{stem}.page.html"):
                    problems += [f"stray ::: in {html.name}: …{ctx}…" for ctx in _stray_fences(html)]
                problems += [f"missing file: {m}" for m in _missing_refs(LECTURES / f"{stem}.qmd")]
                (log_dir / "check.txt").write_text("\n".join(problems) + "\n")
                results[t] = "ok" if not problems else f"FAILED, {len(problems)} problem(s)"
                for p in problems:
                    error(f"  {p}")
                failed |= bool(problems)
    finally:
        if not keep:
            _clean_deck_artifacts(stem)

    print()
    cprint(f"=== render {stem} ===", "green" if not failed else "red")
    print(f"{'preproc':7s} {'FAILED' if pre_errors else 'ok'}, {pre_errors} error(s), "
          f"{len(pre_diags) - pre_errors} warning(s)")
    for t in ordered:
        print(f"{t:7s} {results.get(t, 'skipped')}")
    for name in (f"{stem}.page.html", f"{stem}.slide.html", f"{stem}.slide.pdf"):
        if (SITE_DIR / name).exists():
            print(f"output  {(SITE_DIR / name).relative_to(HERE)}")
    for s in sheets:
        print(f"sheet   {s.relative_to(HERE)}")
    print(f"logs    {log_dir.relative_to(HERE)}")
    if failed:
        raise Exit(code=1)


@task(
    help={
        "deck": "Lecture name or unique prefix, e.g. 02b",
        "to": "slides (default) or html",
        "port": "Port to use (default: first free from 4200)",
        "execute": "Execute code cells (default); --no-execute skips them",
    }
)
def preview(c, deck, to="slides", port=0, execute=True):
    """Live preview of one deck: quarto preview plus re-preprocessing on .qmdx changes."""
    if to not in ("slides", "html"):
        raise Exit("--to must be 'slides' or 'html'", code=2)
    qmdx = _resolve_lecture(deck)
    stem = qmdx.stem
    _require_in_project(stem)
    _seed_site()
    _preprocess_one(qmdx)
    port = _pick_port(int(port), 4200)

    stop = threading.Event()

    def _watch():
        last = qmdx.stat().st_mtime
        while not stop.wait(1.0):
            try:
                m = qmdx.stat().st_mtime
            except FileNotFoundError:
                continue
            if m != last:
                last = m
                try:
                    _preprocess_one(qmdx)
                except Exception as ex:  # keep watching after a broken edit
                    error(f"Preprocess failed: {ex}")

    threading.Thread(target=_watch, daemon=True).start()
    page = f"{stem}.slide.html" if to == "slides" else f"{stem}.page.html"
    info(f"Preview of {stem} at http://localhost:{port}/{page}")
    cmd = f"quarto preview {stem}.qmd --to {_QUARTO_FORMATS[to]} --port {port} --no-browser"
    if not execute:
        cmd += " --no-execute"
    try:
        with c.cd(str(LECTURES)):
            c.run(cmd, pty=True, warn=True)
    finally:
        stop.set()
        _clean_deck_artifacts(stem)

def _link_extensions() -> None:
    """Make lectures/_extensions a symlink to the template clone's _extensions.

    The whole folder is linked, not only ai4sc-style: quarto lists extensions with
    readDir, where a symlink entry does not count as a directory, so a link to just
    lectures/_extensions/ai4sc-style makes quarto miss its shortcodes
    ("Shortcode 'ai4sc-icon' not found").
    An existing real folder is moved to lectures/_extensions.local-backup, never deleted.
    """
    link = HERE / "lectures" / "_extensions"
    target = Path(AI4SC_TEMPLATE_DIR) / "_extensions"
    if not target.is_dir():
        raise SystemExit(f"Template extensions not found: {target} (set AI4SC_TEMPLATE_DIR)")

    if link.is_symlink():
        if link.resolve() == target.resolve():
            info(f"{link} already links to {target}")
            return
        link.unlink()  # points somewhere else: re-point it
    elif link.exists():
        backup = link.with_name("_extensions.local-backup")
        n = 1
        while backup.exists():
            backup = link.with_name(f"_extensions.local-backup.{n}")
            n += 1
        info(f"Moving the existing copy {link} to {backup}")
        link.rename(backup)

    try:
        link.symlink_to(target, target_is_directory=True)
    except OSError as e:  # e.g. Windows without symlink privilege
        raise SystemExit(f"Could not create symlink {link} -> {target}: {e}")
    info(f"Linked {link} -> {target}")


@task()
def link_extensions(c):
    """Link lectures/_extensions to the template clone (see AI4SC_TEMPLATE_DIR)."""
    _link_extensions()


@task()
def update_ai4sc(c):
    """Update the ai4sc-style python package and pull the template that lectures/_extensions links to."""
    info("Update ai4sc-style python package")
    c.run("uv lock --upgrade-package ai4sc-style")
    c.run("uv sync")

    info(f"Pull latest qi4sc-quarto-template into {AI4SC_TEMPLATE_DIR}")
    with c.cd(AI4SC_TEMPLATE_DIR):
        c.run("git pull")

    # lectures/_extensions is a symlink to the template clone, so the pull above
    # already updated the extension (no `quarto add` copy, which would replace the link).
    info("Make sure lectures/_extensions links to the template")
    _link_extensions()


@task()
def update(c):
    update_ai4sc(c)
