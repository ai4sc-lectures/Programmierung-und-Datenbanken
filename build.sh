#jupyter-book build .
#cp Vorlesung\images\*.* _build\html\_images
#ghp-import -n -p -f _build/html
#jupyter-book build . --builder pdfhtml

uv run invoke build