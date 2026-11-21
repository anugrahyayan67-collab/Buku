#!/bin/bash
# Pakai: ./build.sh bab01 "Bab 1 Fisika dan Pengukuran"
set -e
d=$1; t=$2; cd "$(dirname "$0")/$d"
cat > _meta.md <<M
---
title: "Fisika Umum"
subtitle: "$t"
author: "Naskah per bab · edisi kerja · November 2026"
lang: id
---

M
files=(_meta.md $(ls [a-z]-*.md | sort))
for f in "${files[@]}"; do cat "$f"; printf '\n\n'; done > _all.md
pandoc _all.md -s --mathml --highlight-style=monochrome --toc --toc-depth=2 -c ../buku.css -o _all.html 2>/dev/null
perl -0pi -e 's#<mn>(\d+)</mn><mo>,</mo><mn>(\d+)</mn>#<mn>$1,$2</mn>#g; s#<mn>(\d+)</mn><mo>,</mo><msup><mn>(\d+)</mn>#<msup><mn>$1,$2</mn>#g' _all.html
python3 ../gaya.py _all.html
node ../topdf.cjs "$PWD/_all.html" "$PWD/../$d.pdf" "Fisika Umum · $t"
pandoc _all.md -o "../$d.docx" --resource-path=. 2>/dev/null
echo built
