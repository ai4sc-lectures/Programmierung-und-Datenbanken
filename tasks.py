import asyncio
import concurrent.futures
import http.server
import os
import re
import shutil
import socket
import sys
import threading
from pathlib import Path

from ai4sc_style.preprocess import preprocess_lectures
from invoke import task
from pyppeteer import launch
from termcolor import cprint

HERE = Path(__file__).parent

_STAMP_DIR = HERE / "lectures" / ".stamps"

# Local clone of https://github.com/AI4SC/qi4sc-quarto-template (private repo).
# quarto's GitHub installer needs a valid GITHUB_TOKEN for private repos, so we
# pull this local clone instead and install the extension from disk.
AI4SC_TEMPLATE_DIR = os.environ.get(
    "AI4SC_TEMPLATE_DIR",
    "/Users/jplonnigs/Documents/code/Presentations/2026/template",
)


def _find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


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
            elif src.is_dir() and src.name == "site_libs":
                if dst.exists():
                    shutil.rmtree(str(dst))
                shutil.copytree(str(src), str(dst))


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

    _clean_lectures_artifacts(HERE / "lectures")
    for qmdx in stale:
        _mark_fresh(qmdx.stem, "quarto")


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

    _clean_lectures_artifacts(HERE / "lectures")
    for qmdx in stale:
        _mark_fresh(qmdx.stem, "quarto_quick")


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


@task()
def serve(c):
    if sys.platform == "win32":
        c.run("weave 8081 to ./_build/html_quarto")
    elif sys.platform == "darwin":
        c.run("./weave_mac 8081 to ./_build/html_quarto")
    else:
        print("not supported ", sys.platform)

@task()
def update_ai4sc(c):
    """Update the ai4sc-style python package and quarto extension from GitHub."""
    info("Update ai4sc-style python package")
    c.run("uv lock --upgrade-package ai4sc-style")
    c.run("uv sync")

    info(f"Pull latest qi4sc-quarto-template into {AI4SC_TEMPLATE_DIR}")
    with c.cd(AI4SC_TEMPLATE_DIR):
        c.run("git pull")

    info("Update ai4sc-style quarto extension")
    with c.cd(os.path.join("lectures")):
        c.run(f'quarto add "{AI4SC_TEMPLATE_DIR}/_extensions" --no-prompt')


@task()
def update(c):
    update_ai4sc(c)
