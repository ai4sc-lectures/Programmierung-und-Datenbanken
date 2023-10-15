rem git submodule update --init --recursive
rem git submodule update --remote --merge
rem git submodule foreach "git fetch && git reset --hard origin/main"
jupyter-book build .
copy /Y Vorlesung\images\*.* _build\html\_images
ghp-import -n -p -f _build/html
jupyter-book build . --builder pdfhtml