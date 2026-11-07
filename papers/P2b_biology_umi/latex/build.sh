#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
PAPER_ROOT="$(cd "$HERE/.." && pwd)"
cd "$HERE"

pandoc "$PAPER_ROOT/MANUSCRIPT_V0_1.md" \
  --from='markdown+tex_math_dollars+raw_tex' \
  --to=latex \
  --wrap=preserve \
  --natbib \
  --top-level-division=section \
  --output=body.tex

mkdir -p figures
for svg in "$PAPER_ROOT"/figures/*.svg; do
  [ -e "$svg" ] || continue
  base="$(basename "$svg" .svg)"
  inkscape "$svg" --export-type=pdf --export-filename="figures/${base}.pdf"
done

cp "$PAPER_ROOT/references.bib" references.bib
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
sha256sum main.pdf body.tex references.bib > BUILD_SHA256SUMS.txt
printf 'PASS_P2B_LATEX_BUILD\n' > BUILD_RECEIPT.txt
cat BUILD_SHA256SUMS.txt >> BUILD_RECEIPT.txt
