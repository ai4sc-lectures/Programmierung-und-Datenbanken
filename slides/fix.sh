#!/bin/bash
for file in *.qmd; do
  name="${file%.*}"
  sed -i '' "s|(images/|(images/${name}/|g" "$file"
done