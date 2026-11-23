#!/usr/bin/env python3
"""Alat bantu sistem menulis novel.

  python3 kit.py baru   <novel>          membuat folder novel dari templat
  python3 kit.py paket  <novel> <N>      merakit paket konteks untuk menulis bab N
  python3 kit.py cek    <novel> <N>      memeriksa bab N (kata, nama asing, klise, paragraf)
  python3 kit.py status <novel>          ringkasan kemajuan novel

<novel> adalah nama folder di dalam sistem-novel/ (mis. novel-contoh).
"""
import os, re, sys, shutil

AKAR = os.path.dirname(os.path.abspath(__file__))

KLISE = ["tanpa disadari", "waktu seolah berhenti", "detak jantungnya berpacu", "senyuman terukir",
         "tak bisa dipungkiri", "tidak bisa dipungkiri", "seolah-olah dunia runtuh", "dalam sekejap mata",
         "hatinya bergemuruh", "sebuah senyuman", "tak terlukiskan", "bagaikan disambar petir",
         "seakan waktu berhenti", "jantungnya berdegup kencang"]
BATAS_ULANG = {"menghela napas": 1, "menelan ludah": 2, "mengepalkan tangan": 2, "tersenyum tipis": 2}

# kata berhuruf besar yang wajar muncul di tengah kalimat dan bukan nama tokoh/tempat
UMUM = set("""Aku Kamu Dia Ia Mereka Kami Kita Anda Tuhan Allah Ya Tidak Bukan Apa Siapa Mengapa Kenapa Bagaimana
Di Ke Dari Dan Tapi Tetapi Lalu Kemudian Saat Ketika Sejak Setelah Sebelum Sementara Namun Itu Ini Sang Si
Pak Bu Bapak Ibu Mas Mbak Kak Dik Om Tante Nyonya Tuan Nona Dokter Mama Papa Ayah Bunda Nenek Kakek
Senin Selasa Rabu Kamis Jumat Sabtu Minggu Januari Februari Maret April Mei Juni Juli Agustus September
Oktober November Desember Indonesia Jakarta Bab Oke Halo Hai Astaga Ah Oh Eh Hm Hmm Ayo Tolong Maaf Terima""".split())


def baca(p):
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""


def folder(novel):
    d = os.path.join(AKAR, novel)
    if not os.path.isdir(d):
        sys.exit(f"Folder novel '{novel}' tidak ada. Buat dulu: python3 kit.py baru {novel}")
    return d


def bagian(teks, judul):
    """Isi bagian '## judul' sampai '## ' berikutnya."""
    m = re.search(rf"^## {re.escape(judul)}\s*$(.*?)(?=^## |\Z)", teks, re.M | re.S)
    return m.group(1).strip() if m else ""


def blok_bab(teks, n):
    """Blok '## Bab n: ...' sampai '## ' berikutnya (dari log-bab.md atau kerangka.md)."""
    m = re.search(rf"^## Bab {n}\b.*?(?=^## |\Z)", teks, re.M | re.S)
    return m.group(0).strip() if m else ""


def berkas_bab(d, n):
    return os.path.join(d, "bab", f"{n:03d}.md")


def isi_bab(teks, judul=True):
    """Buang bagian FAKTA BARU di akhir (dan baris judul bila judul=False)."""
    isi = re.split(r"^-{3,}\s*$", teks, flags=re.M)[0]
    if not judul:
        isi = re.sub(r"\A\s*Bab \d+[^\n]*\n", "", isi)
    return isi


def turunkan(teks):
    """Turunkan semua judul Markdown satu tingkat agar rapi di dalam paket."""
    return re.sub(r"^(#{1,5}) ", r"#\1 ", teks, flags=re.M)


def tanpa_bagian(teks, juduls):
    for j in juduls:
        teks = re.sub(rf"^## {re.escape(j)}\s*$.*?(?=^## |\Z)", "", teks, flags=re.M | re.S)
    return teks


def kata(teks):
    return re.findall(r"[A-Za-zÀ-ÿ0-9'-]+", teks)


def glosarium(bible):
    nama = set()
    for judul in ("Tokoh", "Tempat", "Istilah"):
        for m in re.finditer(r"^### (.+)$", bagian(bible, judul), re.M):
            nama.update(kata(m.group(1)))
    for m in re.finditer(r"^- Alias:(.*)$", bible, re.M):
        nama.update(kata(m.group(1)))
    return nama


def cmd_baru(novel):
    d = os.path.join(AKAR, novel)
    if os.path.exists(d):
        sys.exit(f"'{novel}' sudah ada.")
    os.makedirs(os.path.join(d, "bab"))
    for f in ("bible.md", "log-bab.md", "kerangka.md"):
        shutil.copy(os.path.join(AKAR, "templat", f), d)
    print(f"Folder {novel}/ dibuat. Isi bible.md (prompt 03) dan kerangka.md (prompt 04).")


def cmd_paket(novel, n):
    d = folder(novel)
    bible, log, kerangka = (baca(os.path.join(d, f)) for f in ("bible.md", "log-bab.md", "kerangka.md"))
    rencana = blok_bab(kerangka, n)
    if not rencana:
        print(f"PERINGATAN: rencana Bab {n} tidak ditemukan di kerangka.md")
    ringkasan = [blok_bab(log, i) for i in range(1, n)]
    hilang = [i for i, r in enumerate(ringkasan, 1) if not r]
    if hilang:
        print(f"PERINGATAN: ringkasan bab {hilang} belum ada di log-bab.md (jalankan prompt 07)")
    akhir = ""
    if n > 1:
        t = isi_bab(baca(berkas_bab(d, n - 1)))
        if t:
            k = t.split()
            akhir = " ".join(k[-500:])
            if len(k) > 500:
                akhir = "… " + akhir
        else:
            print(f"PERINGATAN: berkas bab {n - 1} tidak ada di bab/")
    lanjut = blok_bab(kerangka, n + 1)
    bagian_paket = [
        f"# PAKET KONTEKS — menulis Bab {n}",
        "Semua isi paket ini adalah fakta yang berlaku. FAKTA TERKUNCI tidak boleh dilanggar.",
        "## 1. FAKTA TERKUNCI\n" + (bagian(bible, "Fakta terkunci") or "(kosong)"),
        "## 2. STATUS TOKOH TERBARU\n" + (bagian(bible, "Status tokoh terbaru") or "(kosong)"),
        "## 3. UTAS TERBUKA (janji yang belum dibayar)\n" + (bagian(bible, "Utas terbuka") or "(kosong)"),
        "## 4. STORY BIBLE (tanpa bagian 1–3 di atas)\n" + turunkan(tanpa_bagian(bible, ["Fakta terkunci", "Status tokoh terbaru", "Utas terbuka"]).strip()),
        "## 5. RINGKASAN SEMUA BAB SEBELUMNYA\n" + (turunkan("\n\n".join(r for r in ringkasan if r)) or "(ini bab pertama)"),
        "## 6. AKHIR BAB SEBELUMNYA (± 500 kata terakhir, sambung dari sini)\n" + (akhir or "(tidak ada)"),
        f"## 7. RENCANA BAB {n}\n" + (turunkan(rencana) or "(tidak ada; tanyakan ke penulis)"),
        f"## 8. ARAH BAB {n + 1} (hanya agar kail akhir menyambung; jangan ditulis)\n" + (turunkan(lanjut) or "(belum direncanakan)"),
    ]
    out = os.path.join(d, "_paket", f"bab-{n:03d}.md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    teks = "\n\n".join(bagian_paket) + "\n"
    open(out, "w", encoding="utf-8").write(teks)
    print(f"Paket dibuat: {os.path.relpath(out, AKAR)} ({len(teks.split())} kata)")


def cmd_cek(novel, n):
    d = folder(novel)
    p = berkas_bab(d, n)
    teks = baca(p)
    if not teks:
        sys.exit(f"{os.path.relpath(p, AKAR)} tidak ada.")
    bible = baca(os.path.join(d, "bible.md"))
    isi = isi_bab(teks, judul=False)
    masalah = 0
    jml = len(kata(isi))
    m = re.search(r"Panjang bab:\s*(\d+)\s*-\s*(\d+)", bible)
    lo, hi = (int(m.group(1)), int(m.group(2))) if m else (1500, 2500)
    print(f"Bab {n}: {jml} kata (target {lo}-{hi})")
    if not lo <= jml <= hi:
        print("  ! panjang di luar target"); masalah += 1
    # nama asing: kata berhuruf besar yang tidak di awal kalimat dan tidak ada di Bible
    dikenal = glosarium(bible) | UMUM
    asing = {}
    for kalimat in re.split(r"(?<=[.!?…\"”])\s+|\n+", isi):
        k = kata(kalimat)
        for w in k[1:]:
            if w[:1].isupper() and w not in dikenal and not w.isupper():
                asing[w] = asing.get(w, 0) + 1
    if asing:
        print("  ? nama/kata berhuruf besar yang tidak ada di Bible (tokoh baru? salah ketik?):")
        for w, c in sorted(asing.items(), key=lambda x: -x[1]):
            print(f"      {w} ({c}x)")
        masalah += 1
    kecil = isi.lower()
    for f in KLISE:
        if f in kecil:
            print(f"  ! frasa klise: \"{f}\""); masalah += 1
    for f, batas in BATAS_ULANG.items():
        c = kecil.count(f)
        if c > batas:
            print(f"  ! \"{f}\" muncul {c}x (maks {batas})"); masalah += 1
    paragraf = [x for x in re.split(r"\n\s*\n", isi) if x.strip()]
    panjang = [i for i, x in enumerate(paragraf, 1) if len(re.findall(r"[.!?]+", x)) > 5]
    if panjang:
        print(f"  ! {len(panjang)} paragraf lebih dari 5 kalimat (layar ponsel): paragraf ke-{panjang[:8]}"); masalah += 1
    dialog = sum(1 for x in paragraf if x.lstrip()[:1] in "\"“")
    if paragraf:
        print(f"  dialog: {100 * dialog // len(paragraf)}% paragraf")
    if not re.search(r"^-{3,}\s*$", teks, re.M):
        print("  ! bagian FAKTA BARU (setelah ---) tidak ada"); masalah += 1
    if not blok_bab(baca(os.path.join(d, "log-bab.md")), n):
        print("  • ringkasan bab ini belum masuk log-bab.md (jalankan prompt 07 setelah final)")
    print("  BERSIH" if masalah == 0 else f"  {masalah} hal perlu dicek")


def cmd_status(novel):
    d = folder(novel)
    log = baca(os.path.join(d, "log-bab.md"))
    bible = baca(os.path.join(d, "bible.md"))
    kerangka = baca(os.path.join(d, "kerangka.md"))
    files = sorted(f for f in os.listdir(os.path.join(d, "bab")) if re.fullmatch(r"\d{3}\.md", f))
    total = 0
    for f in files:
        n = int(f[:3]); k = len(kata(isi_bab(baca(os.path.join(d, "bab", f)))))
        total += k
        print(f"Bab {n:3d}: {k:5d} kata  {'log ✓' if blok_bab(log, n) else 'log ✗'}")
    rencana = len(re.findall(r"^## Bab \d+", kerangka, re.M))
    utas = [x for x in bagian(bible, "Utas terbuka").splitlines() if x.strip().strip("-").strip()]
    print(f"Total {len(files)} bab, {total} kata; rencana di kerangka: {rencana} bab; utas terbuka: {len(utas)}")


if __name__ == "__main__":
    a = sys.argv[1:]
    try:
        if a[0] == "baru": cmd_baru(a[1])
        elif a[0] == "paket": cmd_paket(a[1], int(a[2]))
        elif a[0] == "cek": cmd_cek(a[1], int(a[2]))
        elif a[0] == "status": cmd_status(a[1])
        else: raise IndexError
    except (IndexError, ValueError):
        print(__doc__)
