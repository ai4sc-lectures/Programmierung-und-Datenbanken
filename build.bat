rem git submodule update --init --recursive
rem git submodule update --remote --merge
rem git submodule foreach "git fetch && git reset --hard origin/main"
jupyter-book build .
ghp-import -n -p -f _build/html
jupyter-book build . --builder pdfhtml