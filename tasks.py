from invoke import task, call
from invoke import run as invoke_run
from termcolor import cprint
import shutil
from itertools import chain
from pathlib import Path
import glob
import os, sys
import time
from subprocess import PIPE, Popen
from pyppeteer import launch
import asyncio
import tempfile

import concurrent.futures

VERSION_TEMPLATE = """__version__ = "{version_string}"
"""

HERE = Path(__file__).parent

@task
def clean(c, docs=False, bytecode=False, extra=''):
    patterns = ['_build']
    if docs:
        patterns.append('docs/_build')
    if bytecode:
        patterns.append('**/*.pyc')
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
    #info(f"Write PDF {output_file}")
    try:
        browser = await launch(headless=True, args=["--no-sandbox"], handleSIGINT=False, handleSIGTERM=False, handleSIGHUP=False, autoClose=False)
        page = await browser.newPage()
        await page.setViewport(dict(width=1050, height=700))
        await page.emulateMedia("screen")
        await page.goto(url, {"waitUntil": ["networkidle2"]}) # 8910
        page_margins = {"left": "20px", "right": "20px", "top": "30px", "bottom": "30px"}
        await page.pdf(path=output_file, format="A4", printBackground=True, landscape= True) # , margin= page_margins
    except Exception as ex:
        error("Error "+str(ex))
    finally:
        if 'browser' in locals() and browser:
            await browser.close()


@task
def build_quarto(c):
    info("Build slides")
    files = [fn for fn in os.listdir("slides") if fn.endswith(".qmd")]
    os.makedirs("_build/html/slides", exist_ok=True)
    for fn in files:
        fni = os.path.join('slides',fn)
        fno = os.path.join('_build','html','slides', fn.replace('.qmd', '.html'))
        if not os.path.exists(fno) or os.path.getctime(fni) > os.path.getctime(fno):
            fno = fn.replace('.qmd', '.html')
            info(f"Convert slides {fn}")
            with c.cd(os.path.join('slides')):
                c.run(f"quarto render {fn} --output-dir ../_build/html/slides")
    files = [fn for fn in os.listdir("slides") if os.path.splitext(fn)[1] in [".html", ".js", ".css"]]
    for fn in files:
        fni = os.path.join('slides',fn)
        fno = os.path.join('_build','html','slides', fn)
        if not os.path.exists(fno) or os.path.getctime(fni) > os.path.getctime(fno):
            info(f"Copy {fni} to {fno}")
            shutil.copyfile(fni, fno)


@task(build_quarto)
def build_quarto_pdf(c):
    files = [fn for fn in os.listdir("_build/html/slides") if fn.endswith(".html")]
    os.makedirs("_build/pdf/slides", exist_ok=True)
    for fn in files:
        fni = os.path.abspath(os.path.join('_build','html','slides', fn))
        fno = os.path.join('_build','pdf','slides', fn.replace('.html', '.pdf'))
        if not os.path.exists(fno) or os.path.getctime(fni) > os.path.getctime(fno):
            pool = concurrent.futures.ThreadPoolExecutor()
            pool.submit(
                asyncio.run,
                html_to_pdf(
                    f"file://{fni}?print-pdf",
                    fno
                )
            ).result()

@task
def build_quarto_book(c):
    info("Build quarto book ALL")
    os.makedirs("_build/html_quarto", exist_ok=True)
    with c.cd(os.path.join('lectures')):
        c.run(f"quarto render  --output-dir ../_build/html_quarto")

@task
def build_book(c, all=False):
    if all:
        info("Build jupyter book ALL")
        c.run("jupyter-book build --all .")
    else:
        info("Build jupyter book")
        c.run("jupyter-book build .")


@task
def copy_images(c):
    info("Copy Images")
    #os.makedirs("_build/html/_images", exist_ok=True)
    #c.run("cp -Rf lectures/images/* _build/html/_images")
    shutil.copytree("lectures/images", "_build/html/_images", dirs_exist_ok=True)


@task
def build_book_slides(c):
    info("Build jupyter book html")
    os.makedirs("_build/html/lec_slides", exist_ok=True)
    shutil.copyfile("lectures/rise.css", "_build/html/lec_slides/rise.css")
    files = [fn for fn in os.listdir("lectures/") if fn.endswith(".ipynb")]
    for fn in files:
        fni = os.path.join('lectures', fn)
        fno = os.path.join('_build', 'html', 'lec_slides', fn.replace('.ipynb', '.slides.html'))
        if not os.path.exists(fno) or os.path.getctime(fni) > os.path.getctime(fno):
            info(f"Convert slides {fn}")
            c.run(f"jupyter nbconvert --to slides {fni} --output-dir=_build/html/lec_slides")
    files = [fn for fn in os.listdir("_build/html/lec_slides/") if fn.endswith(".html") or fn.endswith(".css")]
    for fn in files:
        fni = os.path.join('_build/html/lec_slides/', fn)
        with open(fni, "r") as fi:
            htmltxt = fi.read()
            htmltxt = htmltxt.replace('src="images/', 'src="../_images/')
            htmltxt = htmltxt.replace('id="theme" rel="stylesheet"/>', 'id="theme" rel="stylesheet"/>\n<link href="rise.css" rel="stylesheet"/>')
        with open(fni, 'w') as fo:
            fo.write(htmltxt)


@task
def build_excercise_slides(c):
    info("Build excercise html")
    os.makedirs("_build/html/excercise", exist_ok=True)
    for (dirpath, dirnames, filenames) in os.walk('excercise/source'):
        for file in filenames:
            if file.endswith('.ipynb') and ".ipynb_checkpoints" not in dirpath:
                fni = os.path.join(dirpath, file)
                fno = os.path.join('_build', 'html', 'excercise', file.replace('.ipynb', '.html'))
                if not os.path.exists(fno) or os.path.getctime(fni) > os.path.getctime(fno):
                    info(f"Convert slides {file}")
                    c.run(f"jupyter nbconvert --to html {fni} --output-dir=_build/html/excercise")


def ipynb_slides_to_pdf_old(c, file, output):
    info(f"Convert slides {file} to pdf {output}")
    serve = c.run(f"jupyter nbconvert --to slides {file} --post serve", asynchronous=True)
    time.sleep(10)  # ie do a bunch of work in the foreground
    c.run(f"open -a 'Google Chrome' --headless --print-to-pdf={output} http://127.0.0.1:8000/{file}?print-pdf")
    serve.runner.kill()


def ipynb_slides_to_pdf(c, filename, input_file, output_file):
    info(f"Convert slides {filename} to PDF {output_file}")
    serve = c.run(f"jupyter nbconvert --to slides {input_file} --post serve --ServePostProcessor.open_in_browser=False", asynchronous=True) # --ServePostProcessor.port=8910 
    time.sleep(3)  # ie do a bunch of work in the foreground
    pool = concurrent.futures.ThreadPoolExecutor()
    pool.submit(
        asyncio.run,
        html_to_pdf(
            f"http://127.0.0.1:8000/{filename.replace('.ipynb', '.slides.html')}?print-pdf",
            output_file
        )
    ).result()
    serve.runner.kill()


@task(build_book_slides)
def build_nbook_slides_pdf(c):
    info("Convert jupyter book slides to pdf")
    files = [fn for fn in os.listdir("lectures/") if fn.endswith(".ipynb")]
    os.makedirs("_build/pdf/slides", exist_ok=True)
    for fn in files:
        fni = os.path.join('lectures', fn)
        fno = os.path.join('_build', 'pdf', 'slides', fn.replace('.ipynb', '.pdf'))
        if not os.path.exists(fno) or os.path.getctime(fni) > os.path.getctime(fno):
            ipynb_slides_to_pdf(c, fn, fni, fno)


@task(build_book_slides, build_quarto)
def build_pdf(c):
    info("Convert jupyter book slides to pdf")
    os.makedirs("_build/pdf/slides", exist_ok=True)
    jobs = []
    slides = [fn for fn in os.listdir("slides") if fn.endswith(".qmd")]
    for fn in slides:
        fni = os.path.join('slides',fn)
        fno = os.path.join('_build','pdf','slides', "qmd_"+fn.replace('.qmd', '.pdf'))
        if not os.path.exists(fno) or os.path.getctime(fni) > os.path.getctime(fno):
            fno2 = fn.replace('.qmd', '.html')
            jobs.append((
                f"http://localhost:8080/slides/{fno2}?print-pdf",
                fno
            ))
    notebooks = [fn for fn in os.listdir("lectures/") if fn.endswith(".ipynb")]
    for fn in notebooks:
        fni = os.path.join('lectures', fn)
        fno = os.path.join('_build','pdf','slides', "nb_"+fn.replace('.ipynb', '.pdf'))
        if not os.path.exists(fno) or os.path.getctime(fni) > os.path.getctime(fno):
            fno2 = fn.replace('.ipynb', '.slides.html')
            jobs.append((
                f"http://localhost:8080/lec_slides/{fno2}?print-pdf",
                fno
            ))
    #info(f"Convert {len(jobs)} pdfs")
    if jobs:
        serve = c.run("weave_mac 8080 to ./_build/html", asynchronous=True) # --ServePostProcessor.port=8910 
        time.sleep(3)  # ie do a bunch of work in the foreground
        pool = concurrent.futures.ThreadPoolExecutor()
        futures = [pool.submit(asyncio.run, html_to_pdf(job[0], job[1])) for job in jobs]
        for future in futures:
            future.result()
        time.sleep(5)
        info(f"Stop server")
        serve.runner.kill()
    

@task()
def build(c, all=False):
    info("Build")
    build_book(c, all)
    copy_images(c)
    #build_quarto(c)
    build_book_slides(c)
    build_excercise_slides(c)


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
    if sys.platform == 'win32':
        c.run("weave 8080 to ./_build/html")
    elif sys.platform == 'darwin':
        c.run("weave_mac 8080 to ./_build/html")
    else:
        print("not supported ", sys.platform)

@task(serve)
def start(c):
    pass