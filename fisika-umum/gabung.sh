#!/bin/bash
# Menyatukan semua bab (bab01, bab02, ...) menjadi satu buku: fisika-umum.pdf dan fisika-umum.docx
set -e
cd "$(dirname "$0")"
out=_buku.md
cat > $out <<M
---
title: "Fisika Umum"
subtitle: "15 bab · naskah gabungan"
author: "Edisi kerja · $(date +%Y-%m-%d)"
lang: id
---

M
for d in bab[0-9][0-9]; do
  for f in $(ls $d/[a-z]-*.md | sort); do
    sed "s#](fig/#]($d/fig/#g" "$f" >> $out; printf '\n\n' >> $out
  done
done
pandoc $out -s --mathml --highlight-style=monochrome --toc --toc-depth=2 -c buku.css -o _buku.html 2>/dev/null
perl -0pi -e 's#<mn>(\d+)</mn><mo>,</mo><mn>(\d+)</mn>#<mn>$1,$2</mn>#g; s#<mn>(\d+)</mn><mo>,</mo><msup><mn>(\d+)</mn>#<msup><mn>$1,$2</mn>#g' _buku.html
python3 gaya.py _buku.html
node topdf.cjs "$PWD/_buku.html" "$PWD/fisika-umum.pdf" "Fisika Umum"
pandoc $out -o fisika-umum.docx 2>/dev/null
echo "buku: $(ls -d bab[0-9][0-9] | wc -l) bab"
