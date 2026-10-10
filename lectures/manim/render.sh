#!/usr/bin/env bash
# Render a Manim scene to slide videos (transparent WebM + MP4 fallback).
#
#   manim/render.sh <file.py> <Scene> <width,height> <out.mp4>
#   manim/render.sh manim/dilemma.py Dilemma1 1500,1000 images/01c_AgentischesProgrammieren/manim_dilemma_1.mp4
#
# Two outputs:
#   <out>.webm  VP9 with alpha: transparent background, the slide shows through (Chrome, Firefox)
#   <out>.mp4   fallback with the scene background; Manim writes BT.601 without tagging it, we
#               re-encode (30 fps) and tag it as BT.601
set -euo pipefail

file=$1 scene=$2 res=$3 out=$4
webm="${out%.mp4}.webm"
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

uv run --with manim manim -qh -t --progress_bar none --format mov --resolution "$res" --media_dir "$tmp/t" "$file" "$scene" >/dev/null
mov=$(find "$tmp/t/videos" -name "$scene.mov" -not -path "*partial*" | head -1)
ffmpeg -v error -y -i "$mov" -vf fps=30 -c:v libvpx-vp9 -pix_fmt yuva420p -b:v 0 -crf 32 -row-mt 1 -an "$webm"

uv run --with manim manim -qh --progress_bar none --resolution "$res" --media_dir "$tmp/o" "$file" "$scene" >/dev/null
mp4=$(find "$tmp/o/videos" -name "$scene.mp4" -not -path "*partial*" | head -1)
ffmpeg -v error -y -i "$mp4" -c:v libx264 -crf 24 -r 30 -pix_fmt yuv420p \
  -x264-params "colorprim=smpte170m:transfer=smpte170m:colormatrix=smpte170m:range=tv" \
  -colorspace smpte170m -color_primaries smpte170m -color_trc smpte170m -color_range tv \
  -movflags +faststart -an "$out"

# keep the built deck in sync
for f in "$out" "$webm"; do
  build="_site/${f}"
  [ -d "$(dirname "$build")" ] && cp "$f" "$build"
done
echo "$webm $out"
