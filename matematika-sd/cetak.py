#!/usr/bin/env python3
"""Cetak buku rangkuman Matematika SD menjadi satu PDF.

python3 matematika-sd/cetak.py  ->  matematika-sd/Matematika-SD-Rangkuman.pdf
Langkah: sampul (HTML, tanpa margin) + isi (daftar isi, bab, kunci) dirender Chromium
lewat Playwright; nomor halaman daftar isi dicari dari PDF isi (dua putaran).
"""
import html, json, re, subprocess, sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter

D = Path(__file__).resolve().parent
KERJA = D / "_kerja"; KERJA.mkdir(exist_ok=True)
HASIL = D / "Matematika-SD-Rangkuman.pdf"
JUDUL = "Pintar Matematika Dasar"
SUB = "Rangkuman untuk Anak SD"
PENYUSUN = "Septian Anugrah Dwi Putra"

RENDER = r"""
const { chromium } = require('playwright');
const [inp, out, mode] = process.argv.slice(2);
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + inp, { waitUntil: 'networkidle' });
  const o = { path: out, format: 'A4', printBackground: true, preferCSSPageSize: true };
  if (mode === 'isi') {
    o.displayHeaderFooter = true;
    o.headerTemplate = '<div></div>';
    o.footerTemplate = `<div style="width:100%;font-family:Inter,sans-serif;font-size:8.5pt;color:#12406a;
      display:flex;justify-content:center;"><span style="background:#12406a;color:#fff;border-radius:3px;
      padding:1px 7px;font-weight:700"><span class="pageNumber"></span></span></div>`;
  }
  await p.pdf(o);
  await b.close();
})();
"""


def pandoc(md: str) -> str:
    r = subprocess.run(["pandoc", "-f", "markdown+fenced_divs+raw_html", "-t", "html", "--mathml"],
                       input=md, capture_output=True, text=True, check=True)
    return r.stdout


def bab(path: Path):
    teks = path.read_text(encoding="utf-8")
    m = re.match(r"# Bab (\d+) · (.+)\n", teks)
    no, judul = m.group(1), m.group(2).strip()
    isi = pandoc(teks[m.end():])
    kepala = (f'<div class="babkepala"><div class="no">{no}</div><div class="judul">'
              f'<span class="kecil">BAB {no}</span>{html.escape(judul)}</div></div>')
    return no, judul, f'<section class="bab" id="bab{no}">{kepala}{isi}</section>'


def daftar_isi(babs, hal):
    baris = []
    for no, judul, _ in babs:
        h = hal.get(no, "")
        baris.append(f'<a class="baris" href="#bab{no}"><span class="n">{no}</span><span class="t">{html.escape(judul)}</span>'
                     f'<span class="d"></span><span class="h">{h}</span></a>')

    hk = hal.get("kunci", "")
    baris.append(f'<a class="baris" href="#kunci"><span class="n">✓</span><span class="t">Kunci Jawaban</span>'
                 f'<span class="d"></span><span class="h">{hk}</span></a>')
    catatan = ('<div class="catatan"><b>Cara memakai buku ini.</b> Baca berurutan dari Bab 1, karena setiap bab '
               'memakai bab sebelumnya. Baca penjelasannya, coba contoh sendiri dulu sebelum melihat caranya, '
               'lalu kerjakan latihan di kertas. Cocokkan jawabanmu dengan kunci di akhir buku. Kalau salah, '
               'baca lagi kotak <b>Ingat!</b> dan <b>Hati-hati!</b> di bab itu.</div>')
    return f'<section class="toc"><h2>Daftar Isi</h2>{"".join(baris)}{catatan}</section>'


def halaman_html(body, css_extra=""):
    css = (D / "gaya.css").read_text(encoding="utf-8")
    return (f'<!doctype html><html lang="id"><head><meta charset="utf-8"><style>{css}{css_extra}</style>'
            f'</head><body>{body}</body></html>')


def render(html_teks, nama, mode):
    f = KERJA / f"{nama}.html"; f.write_text(html_teks, encoding="utf-8")
    js = KERJA / "render.cjs"; js.write_text(RENDER, encoding="utf-8")
    out = KERJA / f"{nama}.pdf"
    subprocess.run(["node", str(js), str(f), str(out), mode], check=True)
    return out


def sampul():
    css = """@page{size:A4;margin:0} body{margin:0}
    .s{width:210mm;height:297mm;position:relative;overflow:hidden;background:#f4f9fe}
    .pita{position:absolute;left:0;top:0;bottom:0;width:10mm;background:#12406a}
    .atas{position:absolute;top:22mm;left:24mm;right:18mm;font-weight:800;font-size:9.5pt;letter-spacing:5px;color:#1f7fc4}
    .j{position:absolute;top:38mm;left:24mm;right:18mm;font-size:52pt;font-weight:900;line-height:.95;color:#12406a}
    .j span{color:#1f7fc4}
    .sub{position:absolute;top:104mm;left:24mm;font-size:16pt;font-weight:600;color:#33475b;border-left:5px solid #e07b22;padding-left:4mm}
    .kotak{position:absolute;left:24mm;right:18mm;top:122mm;height:128mm;border-radius:6mm;background:#12406a}
    .kotak svg{position:absolute;left:0;top:0}
    .nama{position:absolute;bottom:22mm;left:24mm;font-size:12pt;font-weight:800;letter-spacing:2px;color:#12406a}
    .kls{position:absolute;bottom:22mm;right:18mm;font-size:11pt;font-weight:800;color:#fff;background:#e07b22;border-radius:3mm;padding:2mm 4mm}"""
    gambar = """<svg width="168mm" height="128mm" viewBox="0 0 168 128">
      <g fill="none" stroke-width="2.2" stroke-linejoin="round">
        <rect x="16" y="18" width="38" height="38" rx="2" fill="#1f7fc4" stroke="#7fc0f0"/>
        <polygon points="78,58 100,18 122,58" fill="#e07b22" stroke="#ffd2a6"/>
        <circle cx="146" cy="38" r="17" fill="#1a8a6a" stroke="#8fe0c0"/>
        <rect x="16" y="76" width="56" height="30" rx="2" fill="#6a4fb3" stroke="#c9b8f2"/>
        <polygon points="92,106 104,76 150,76 138,106" fill="#c0392b" stroke="#f3a99f"/>
      </g>
      <g font-family="Inter,sans-serif" font-weight="900" fill="#ffffff" text-anchor="middle">
        <text x="35" y="44" font-size="15">×</text><text x="100" y="52" font-size="14">÷</text>
        <text x="146" y="44" font-size="15">+</text><text x="44" y="96" font-size="13">½</text>
        <text x="121" y="96" font-size="13">□ = ?</text>
      </g>
      <g font-family="Inter,sans-serif" font-size="4.6" fill="#cfe6fb" text-anchor="middle" font-weight="700">
        <text x="84" y="124">bilangan · perkalian · pembagian · pecahan · aljabar · bangun datar</text>
      </g></svg>"""
    body = (f'<div class="s"><div class="pita"></div><div class="atas">RANGKUMAN MATEMATIKA</div>'
            f'<div class="j">PINTAR<br><span>MATEMATIKA</span><br>DASAR</div>'
            f'<div class="sub">{SUB}</div><div class="kotak">{gambar}</div>'
            f'<div class="nama">{PENYUSUN.upper()}</div><div class="kls">Kelas 3–6</div></div>')
    return render(halaman_html(body, css), "sampul", "sampul")


def cari_halaman(pdf, babs):
    r = PdfReader(str(pdf)); hal = {}
    for i, pg in enumerate(r.pages, 1):
        t = pg.extract_text() or ""
        for no, _, _ in babs:
            if no not in hal and re.search(rf"BAB {no}\b", t):
                hal[no] = i
        if "kunci" not in hal and "KUNCI JAWABAN" in t:
            hal["kunci"] = i
    return hal


def main():
    babs = [bab(p) for p in sorted(D.glob("bab*.md"))]
    kunci = pandoc((D / "kunci.md").read_text(encoding="utf-8"))
    kunci = (f'<section class="bab kunci" id="kunci"><div class="babkepala"><div class="no">✓</div><div class="judul">'
             f'<span class="kecil">KUNCI JAWABAN</span>Jawaban Semua Latihan</div></div>{kunci}</section>')
    hal = {}
    for putaran in range(2):
        body = daftar_isi(babs, hal) + "".join(b[2] for b in babs) + kunci
        isi = render(halaman_html(body), "isi", "isi")
        baru = cari_halaman(isi, babs)
        if baru == hal:
            break
        hal = baru
    s = sampul()
    w = PdfWriter()
    w.append(str(s))
    w.append(str(isi), import_outline=False)
    w.add_metadata({"/Title": f"{JUDUL}: {SUB}", "/Author": PENYUSUN})
    # penanda bab
    for no, judul, _ in babs:
        if no in hal:
            w.add_outline_item(f"Bab {no} {judul}", hal[no])
    if "kunci" in hal:
        w.add_outline_item("Kunci Jawaban", hal["kunci"])
    with open(HASIL, "wb") as fh:
        w.write(fh)
    n = len(PdfReader(str(HASIL)).pages)
    print(f"{HASIL.name}: {n} halaman; halaman bab {json.dumps(hal)}")


if __name__ == "__main__":
    sys.exit(main())
