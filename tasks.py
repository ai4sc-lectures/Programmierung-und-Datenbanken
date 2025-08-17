from invoke import task, call
from termcolor import cprint
import shutil
from pathlib import Path
import os, sys
import time
from pyppeteer import launch
import asyncio
import re
import json

import concurrent.futures

VERSION_TEMPLATE = """__version__ = "{version_string}"
"""

HERE = Path(__file__).parent


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


def make_and_clean_dir(dir_, glob="*"):
    info(f"Cleaning {dir_}/{glob}")
    (HERE / dir_).mkdir(exist_ok=True)
    for file_ in (HERE / dir_).glob(glob):
        if file_.is_file():
            file_.unlink()
        elif file_.is_dir():
            shutil.rmtree(file_)


def error(text):
    cprint(text, "red")


def info(text):
    cprint(text, "blue")


@task
def clean(c):
    make_and_clean_dir("_build")


async def html_to_pdf(url, output_file):
    """Convert a HTML file to a PDF"""
    info(f"Convert {url} to {output_file}")
    # info(f"Write PDF {output_file}")
    try:
        browser = await launch(
            headless=True,
            args=["--no-sandbox"],
            handleSIGINT=False,
            handleSIGTERM=False,
            handleSIGHUP=False,
            autoClose=False,
        )
        page = await browser.newPage()
        await page.setViewport(dict(width=1050, height=700))
        await page.emulateMedia("print") # "screen"
        await page.goto(url, {"waitUntil": ["networkidle2","load"]})  # 8910
        await page.pdf(
            path=output_file, format="A4", printBackground=True, landscape=True
        )  # , margin= page_margins
    except Exception as ex:
        error("Error " + str(ex))
    finally:
        if "browser" in locals() and browser:
            await browser.close()


@task
def build_quarto(c):
    info("Build slides")
    files = [fn for fn in os.listdir("slides") if fn.endswith(".qmd")]
    os.makedirs("_build/html/slides", exist_ok=True)
    for fn in files:
        fni = os.path.join("slides", fn)
        fno = os.path.join("_build", "html", "slides", fn.replace(".qmd", ".html"))
        if not os.path.exists(fno) or os.path.getctime(fni) > os.path.getctime(fno):
            fno = fn.replace(".qmd", ".html")
            info(f"Convert slides {fn}")
            with c.cd(os.path.join("slides")):
                c.run(f"quarto render {fn} --output-dir ../_build/html/slides")
    files = [
        fn
        for fn in os.listdir("slides")
        if os.path.splitext(fn)[1] in [".html", ".js", ".css"]
    ]
    for fn in files:
        fni = os.path.join("slides", fn)
        fno = os.path.join("_build", "html", "slides", fn)
        if not os.path.exists(fno) or os.path.getctime(fni) > os.path.getctime(fno):
            info(f"Copy {fni} to {fno}")
            shutil.copyfile(fni, fno)


@task(build_quarto)
def build_quarto_pdf(c):
    files = [fn for fn in os.listdir("_build/html/slides") if fn.endswith(".html")]
    os.makedirs("_build/pdf/slides", exist_ok=True)
    for fn in files:
        fni = os.path.abspath(os.path.join("_build", "html", "slides", fn))
        fno = os.path.join("_build", "pdf", "slides", fn.replace(".html", ".pdf"))
        if not os.path.exists(fno) or os.path.getctime(fni) > os.path.getctime(fno):
            pool = concurrent.futures.ThreadPoolExecutor()
            pool.submit(
                asyncio.run, html_to_pdf(f"file://{fni}?view=print-pdf", fno)
            ).result()


@task
def build_quarto_book(c):
    info("Build quarto book ALL")
    os.makedirs("_build/html_quarto", exist_ok=True)
    with c.cd(os.path.join("lectures")):
        c.run(f"quarto render  --output-dir ../_build/html_quarto")


@task
def config_book(c):
    c.run("jupyter-book config sphinx .")

# load dictionary from JSON
with open("toc_translations.json", "r", encoding="utf-8") as f:
    translations = json.load(f)

def replace_anchor_text(m: re.Match) -> str:
    s = m.group(1)
    return ">" + translations.get(s,s) + m.group(2)

@task
def build_book(c, all=False):
    if all:
        info("Build jupyter book ALL")
        os.environ["PYDEVD_DISABLE_FILE_VALIDATION"] = "1"
        c.run("jupyter-book build --all .")
    else:
        info("Build jupyter book")
        os.environ["PYDEVD_DISABLE_FILE_VALIDATION"] = "1"
        c.run("jupyter-book build .")
    
    files = [
        os.path.join("_build/html/lectures/", fn)
        for fn in os.listdir("_build/html/lectures/")
        if fn.endswith(".html") or fn.endswith(".css")
    ]+["_build/html/intro.html","_build/html/intro_en.html"]
    for fni in files:
        fn = os.path.basename(fni)
        with open(fni, "r") as fi:
            htmltxt = fi.read()
            # htmltxt = re.sub(r'(<style type="text/css">\s*pre \{ line-height: 125%; \})(.*?)(</style>\s*<!-- Load mathjax -->)', '<link href="jp-notebook-style.css" rel="stylesheet"/>', htmltxt, flags=re.DOTALL)
            htmltxt = htmltxt.replace('src="images/', 'src="../_images/')
            htmltxt = htmltxt.replace("src='images/", "src='../_images/")
            htmltxt = htmltxt.replace(", 'images/", ", '../_images/")
            htmltxt = htmltxt.replace(", 'images/", ", '../_images/")
            if "_en." not in fn:
                htmltxt = htmltxt.replace('<div class="dropdown dropdown-download-buttons">', f'<a href="{fn.replace('.html','_en.html')}" class="button btn btn-sm" title="en" data-bs-placement="bottom" data-bs-toggle="tooltip"><span class="btn__icon-container"><i class="fas fa-language "></i></span></a><div  class="dropdown dropdown-download-buttons">')
            else:
                htmltxt = htmltxt.replace('.html"', '_en.html"')
                htmltxt = htmltxt.replace('_en_en.html"', '_en.html"')
                htmltxt = htmltxt.replace('.slides.html"', '_en.slides.html"')
                htmltxt = htmltxt.replace('.slides_en.html"', '_en.slides.html"')
                htmltxt = htmltxt.replace('_en_en.slides.html"', '_en.slides.html"')
                htmltxt = htmltxt.replace('_en_en.slides.html"', '_en.slides.html"')
                htmltxt = htmltxt.replace('.pdf"', '_en.pdf"')
                htmltxt = htmltxt.replace('_en_en.pdf"', '_en.pdf"')
                htmltxt = htmltxt.replace('<div class="dropdown dropdown-download-buttons">', f'<a href="{fn.replace('_en.html','.html')}" class="button btn btn-sm" title="en" data-bs-placement="bottom" data-bs-toggle="tooltip"><span class="btn__icon-container"><i class="fas fa-language "></i></span></a><div  class="dropdown dropdown-download-buttons">')
                apat1 = re.compile(r">(?!\s*<)([^<]*)(</a>)")
                htmltxt = apat1.sub(replace_anchor_text, htmltxt)
                apat2 = re.compile(r">(?!\s*<)([^<]*)(</span>)")
                htmltxt = apat2.sub(replace_anchor_text, htmltxt)

        with open(fni, "w") as fo:
            fo.write(htmltxt)


@task
def copy_images(c):
    info("Copy Images")
    # os.makedirs("_build/html/_images", exist_ok=True)
    # c.run("cp -Rf lectures/images/* _build/html/_images")
    shutil.copytree("lectures/images", "_build/html/_images", dirs_exist_ok=True)


@task
def build_book_slides(c):
    info("Build jupyter book html")
    os.makedirs("_build/html/lec_slides", exist_ok=True)
    shutil.copyfile("lectures/rise.css", "_build/html/lec_slides/rise.css")
    shutil.copyfile(
        "lectures/jp-notebook-style.css", "_build/html/lec_slides/jp-notebook-style.css"
    )
    files = [fn for fn in os.listdir("lectures/") if fn.endswith(".ipynb")]
    for fn in files:
        fni = os.path.join("lectures", fn)
        fno = os.path.join(
            "_build", "html", "lec_slides", fn.replace(".ipynb", ".slides.html")
        )
        if not os.path.exists(fno) or os.path.getctime(fni) > os.path.getctime(fno):
            info(f"Convert slides {fn}")
            c.run(
                f"jupyter nbconvert --to slides {fni} --output-dir=_build/html/lec_slides"
            )
    files = [
        fn
        for fn in os.listdir("_build/html/lec_slides/")
        if fn.endswith(".html") or fn.endswith(".css")
    ]
    for fn in files:
        fni = os.path.join("_build/html/lec_slides/", fn)
        with open(fni, "r") as fi:
            htmltxt = fi.read()
            # htmltxt = re.sub(r'(<style type="text/css">\s*pre \{ line-height: 125%; \})(.*?)(</style>\s*<!-- Load mathjax -->)', '<link href="jp-notebook-style.css" rel="stylesheet"/>', htmltxt, flags=re.DOTALL)
            htmltxt = htmltxt.replace('src="images/', 'src="../_images/')
            htmltxt = htmltxt.replace("src='images/", "src='../_images/")
            htmltxt = htmltxt.replace(", 'images/", ", '../_images/")
            htmltxt = htmltxt.replace(", 'images/", ", '../_images/")
            htmltxt = htmltxt.replace(
                'id="theme" rel="stylesheet"/>',
                'id="theme"  rel="stylesheet"/>\n<link href="rise.css" rel="stylesheet"/>',
            )
            #htmltxt = htmltxt.replace("document.getElementsByTagName( 'head' )[0].appendChild( link );", "document.getElementsByTagName( 'head' )[0].appendChild( link );window.addEventListener('load', () => {window.print();});")
            htmltxt = htmltxt.replace('slideNumber: "",', 'slideNumber: "c/t",')
            htmltxt = htmltxt.replace("width: 960,", "width: 1050,")  # 1200
            htmltxt = htmltxt.replace("height: 700,", "height: 700,")  # 800
            if "mouseWheel: true" not in htmltxt:
                htmltxt = htmltxt.replace(
                    "plugins: [RevealNotes]",
                    """            progress: true,
            keyboard: true,
            overview: true,
            center: false,
            disableLayout: false,
            touch: true,
            loop: false,
            rtl: false,
            navigationMode: 'default',
            pause: true,
            autoPlayMedia: true,
            mouseWheel: true,
            display: 'block',
            pdfSeparateFragments: true,
            previewLinks: false,
            transition: 'convex',
            transitionSpeed: 'fast',
            backgroundTransition: 'none',
            viewDistance: 3,
            mobileViewDistance: 2,
            margin: 0.01,
            plugins: [RevealNotes]""",
                )  # plugins: [RevealNotes, PdfExport, Verticator, RevealMenu, RevealChalkboard, RevealMath, RevealSearch, RevealZoom]
            htmltxt = htmltxt.replace(
                """
</div>
</div>
</main>""",
                """
<img src="../_images/ai4sc_logo_v2.svg" class="slide-logo">
<div class="footer footer-default" style="display: block;">
<span style="letter-spacing: .04rem;">programmierung</span><br><span style="letter-spacing: .0rem;">und datenbanken</span>
</div></div></div>
</main>""",
            )
            htmltxt = htmltxt.replace(
                """
  --jp-content-font-family: system-ui, -apple-system, blinkmacsystemfont,
    'Segoe UI', helvetica, arial, sans-serif, 'Apple Color Emoji',
    'Segoe UI Emoji', 'Segoe UI Symbol';
""",
                """
  --jp-content-font-family: "IBM Plex Sans", sans-serif;""",
            )
            htmltxt = htmltxt.replace(
                '/dist/theme/simple.css" id="theme"  rel="stylesheet"/>',
                """/dist/theme/simple.css" id="theme"  rel="stylesheet"/>""",
            )
            if (
                "https://unpkg.com/reveal.js@4.0.2/plugin/markdown/markdown.js"
                not in htmltxt
            ):
                htmltxt = htmltxt.replace(
                    '"https://unpkg.com/reveal.js@4.0.2/plugin/notes/notes.js"',
                    """ "https://unpkg.com/reveal.js@4.0.2/plugin/notes/notes.js",
      "https://unpkg.com/reveal.js@4.0.2/plugin/markdown/markdown.js",
      "https://unpkg.com/reveal.js@4.0.2/plugin/math/math.js",
      "https://unpkg.com/reveal.js@4.0.2/plugin/search/search.js",
      "https://unpkg.com/reveal.js@4.0.2/plugin/zoom/zoom.js",
      "https://unpkg.com/reveal.js@4.0.2/plugin/highlight/highlight.js" """,
                )

        with open(fni, "w") as fo:
            fo.write(htmltxt)


@task
def build_excercise_slides(c):
    info("Build excercise html")
    os.makedirs("_build/html/excercises", exist_ok=True)
    for dirpath, _, filenames in os.walk("excercises/source"):
        for file in filenames:
            if file.endswith(".ipynb") and ".ipynb_checkpoints" not in dirpath:
                fni = os.path.join(dirpath, file)
                fno = os.path.join(
                    "_build", "html", "excercises", file.replace(".ipynb", ".html")
                )
                if not os.path.exists(fno) or os.path.getctime(fni) > os.path.getctime(
                    fno
                ):
                    info(f"Convert slides {file}")
                    c.run(
                        f"jupyter nbconvert --to html {fni} --output-dir=_build/html/excercises"
                    )


def ipynb_slides_to_pdf_old(c, file, output):
    info(f"Convert slides {file} to pdf {output}")
    serve = c.run(
        f"jupyter nbconvert --to slides {file} --post serve", asynchronous=True
    )
    time.sleep(10)  # ie do a bunch of work in the foreground
    c.run(
        f"open -a 'Google Chrome' --headless --print-to-pdf={output} http://127.0.0.1:8000/{file}?print-pdf"
    )
    serve.runner.kill()


def ipynb_slides_to_pdf2(c, filename, input_file, output_file):
    info(f"Convert slides {filename} to PDF {output_file}")
    serve = c.run(
        f"jupyter nbconvert --to slides {input_file} --post serve --ServePostProcessor.open_in_browser=False",
        asynchronous=True,
    )  # --ServePostProcessor.port=8910
    time.sleep(3)  # ie do a bunch of work in the foreground
    pool = concurrent.futures.ThreadPoolExecutor()
    pool.submit(
        asyncio.run,
        html_to_pdf(
            f"http://127.0.0.1:8000/{filename.replace('.ipynb', '.slides.html')}?view=print-pdf",
            output_file,
        ),
    ).result()
    serve.runner.kill()


def ipynb_slides_to_pdf(c, filename, input_file, output_file):
    info(f"Convert slides {filename} to PDF {output_file}")
    pool = concurrent.futures.ThreadPoolExecutor()
    pool.submit(
        asyncio.run,
        html_to_pdf(
            f"http://127.0.0.1:8080/lec_slides/{filename.replace('.ipynb', '.slides.html')}?view=print-pdf",
            output_file,
        ),
    ).result()


@task(build_book_slides)
def build_nbook_slides_pdf(c):
    info("Convert jupyter book slides to pdf")
    if sys.platform == "win32":
        serve = c.run("weave 8080 to ./_build/html", asynchronous=True)
    elif sys.platform == "darwin":
        serve = c.run("./weave_mac 8080 to ./_build/html", asynchronous=True)
    time.sleep(3)  # ie do a bunch of work in the foreground
    files = [fn for fn in os.listdir("lectures/") if fn.endswith(".ipynb")]
    #os.makedirs("_build/pdf/slides", exist_ok=True)
    os.makedirs("_build/html/pdf/slides", exist_ok=True)
    pool = concurrent.futures.ThreadPoolExecutor()
    for fn in files:
        fni = os.path.join("lectures", fn)
        fno = os.path.join("_build", "html", "pdf", "slides", fn.replace(".ipynb", ".pdf"))
        if not os.path.exists(fno) or os.path.getctime(fni) > os.path.getctime(fno):
            ##ipynb_slides_to_pdf(c, fn, fni, fno)
            info(f"Convert slides {fni} to PDF {fno}")
            pool.submit(
                asyncio.run,
                html_to_pdf(
                    f"http://127.0.0.1:8080/{fni.replace('lectures', 'lec_slides').replace('.ipynb', '.slides.html')}?view=print-pdf",
                    fno,
                ),
            )
    pool.shutdown()
    serve.runner.kill()


@task(build_book_slides, build_quarto)
def build_pdf(c):
    info("Convert jupyter book slides to pdf")
    os.makedirs("_build/pdf/slides", exist_ok=True)
    jobs = []
    slides = [fn for fn in os.listdir("slides") if fn.endswith(".qmd")]
    for fn in slides:
        fni = os.path.join("slides", fn)
        fno = os.path.join(
            "_build", "pdf", "slides", "qmd_" + fn.replace(".qmd", ".pdf")
        )
        if not os.path.exists(fno) or os.path.getctime(fni) > os.path.getctime(fno):
            fno2 = fn.replace(".qmd", ".html")
            jobs.append((f"http://localhost:8080/slides/{fno2}?print-pdf", fno))
    notebooks = [fn for fn in os.listdir("lectures/") if fn.endswith(".ipynb")]
    for fn in notebooks:
        fni = os.path.join("lectures", fn)
        fno = os.path.join(
            "_build", "pdf", "slides", "nb_" + fn.replace(".ipynb", ".pdf")
        )
        if not os.path.exists(fno) or os.path.getctime(fni) > os.path.getctime(fno):
            fno2 = fn.replace(".ipynb", ".slides.html")
            jobs.append((f"http://localhost:8080/lec_slides/{fno2}?print-pdf", fno))
    # info(f"Convert {len(jobs)} pdfs")
    if jobs:
        serve = c.run(
            "weave_mac 8080 to ./_build/html", asynchronous=True
        )  # --ServePostProcessor.port=8910
        time.sleep(3)  # ie do a bunch of work in the foreground
        pool = concurrent.futures.ThreadPoolExecutor()
        futures = [
            pool.submit(asyncio.run, html_to_pdf(job[0], job[1])) for job in jobs
        ]
        for future in futures:
            future.result()
        time.sleep(5)
        info(f"Stop server")
        serve.runner.kill()


@task()
def build(c, all=False):
    info("Build")
    config_book(c)
    build_book(c, all)
    copy_images(c)
    build_quarto(c)
    build_book_slides(c)
    build_excercise_slides(c)


@task()
def pdf(c, all=False):
    info("Build PDF")
    build_nbook_slides_pdf(c)


@task(build)
def build_book_pdf(c):
    info("Build jupyter book pdf")
    c.run("jupyter-book build . --builder pdfhtml")


@task(build)
def ghp_import(c):
    c.run("ghp-import -n -p -f _build/html")


@task(pre=[call(build, all=True)])
def publish(c):
    ghp_import(c)


@task()
def serve(c):
    if sys.platform == "win32":
        c.run("weave 8080 to ./_build/html")
    elif sys.platform == "darwin":
        c.run("./weave_mac 8080 to ./_build/html")
    else:
        print("not supported ", sys.platform)


@task(serve)
def start(c):
    pass
