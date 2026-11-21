#!/bin/bash
# Pakai: ./build.sh bab01 "Bab 1"   -> kimia-organik/bab01.pdf
# (soal.py menyusun z-akhir.md dari _soal.txt dan _akhir.md bila ada)
set -e
cd "$(dirname "$0")"
[ -f "$1/_soal.txt" ] && python3 alat/soal.py "$1"
python3 alat/bangun.py "$1"
echo built
