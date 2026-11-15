# Panduan dan templat buku (versi terbaru, November 2026)

Panduan ini merangkum susunan isi, gaya penulisan, desain, dan alur kerja yang dipakai **Fisika Umum Edisi 1** dan **Kimia Kuantum Edisi 1**. Buku baru di repo ini mengikuti panduan ini supaya semua buku terlihat satu seri.

Contoh pelaksanaan paling lengkap: `kimia-kuantum/` (alat cetak di `kimia-kuantum/edisi/`).

---

## 1. Susunan buku

**Bagian depan** (dibuat otomatis oleh `edisi/cetak.py`)
1. Sampul depan
2. Halaman judul (judul, subjudul, nama penyusun, edisi)
3. Halaman keterangan (edisi, tahun, penyusun, catatan pembuatan)
4. Isi Ringkas (satu halaman, dikelompokkan per Bagian)
5. Daftar Isi (bab, subbab, ringkasan, jawaban; semua baris bisa diketuk)
6. Kata Pengantar dan Cara Memakai Buku Ini (`edisi/depan.md`)

**Isi**: 15–17 bab, dikelompokkan dalam Bagian (I, II, ...). Target 50–60 halaman tiap bab (± 20 000 kata).

**Bagian belakang**: Lampiran (A, B, ...), Indeks otomatis, sampul belakang.

## 2. Susunan setiap bab

1. **Halaman pembuka** (otomatis): nama Bagian, gambar sesuai isi bab beserta keterangan, "BAB" + nomor besar, judul bab kapital, kotak **Isi bab** berisi daftar subbab.
2. Paragraf pembuka berupa teka-teki.
3. Kotak **Pertanyaan pembuka** (`.kuis`), **Tujuan belajar** (`.tujuan`), **Prasyarat** (`.mat`, menunjuk bab/subbab).
4. Subbab `## N.k Judul`, sub-subbab `### Judul`. Setiap subbab: penjelasan "mengapa", penurunan langkah demi langkah, 2–5 contoh, kotak, dan satu kuis cepat.
5. Paragraf penutup "Menuju bab berikutnya".
6. **Akhir bab** (`z-akhir.md` / `c-akhir.md`, dibuat dari `_soal.txt` oleh `alat/soal.py`): Ringkasan (tabel rumus) · Pertanyaan konsep (± 20) · Soal per subbab (≥ 80; tingkat Dasar, Menengah, Tantangan ★; [P] = dibahas) · Jawaban semua soal (tabel) · Pembahasan soal terpilih · Bacaan lanjut (≤ 6 judul).

## 3. Kotak dan label (Markdown + div semantik saja)

| Div | Dipakai untuk |
|---|---|
| `::: {.contoh}` | `**Contoh N.n1 · Judul**`, lalu **Gambaran fisis.** (opsional), **Rencana.** (opsional), **Penyelesaian.**, **Memahami hasil.** |
| `::: {.kuis}` | `**Kuis cepat N.k**` atau pertanyaan pembuka |
| `::: {.inti}` | hasil terpenting |
| `::: {.dalam}` | penurunan panjang / perluasan ("Lebih dalam") |
| `::: {.awas}` | kesalahan umum |
| `::: {.mat}` | alat matematika, prasyarat |
| `::: {.terapan}` | kaitan kimia / terapan |
| `::: {.strategi}` | langkah memecahkan soal |
| `::: {.tujuan}` | tujuan belajar |

Naskah **netral terhadap desain**: tanpa HTML, CSS, warna, atau rujukan ke letak halaman.

## 4. Aturan penulisan

- Bahasa Indonesia baku tetapi enak dibaca; jelaskan **mengapa**, bukan sekadar rumus.
- Semua angka dihitung dengan Python dulu. Koma desimal (`9{,}8` di LaTeX).
- LaTeX tanpa `\cancel` dan `\tag`. Persamaan bernomor: `\text{(N.n1)}`; contoh dan gambar memakai label sementara (`N.n1`), dinomori `alat/nomor.py`.
- Konfigurasi elektron ditulis berpisah: `1s^2 2s^2 2p^6` (jangan `1s^22s^2`).
- Istilah baku: getaran (bukan vibrasi), rotasi–getaran, pendekatan, asas (ketidakpastian, Pauli, Franck–Condon), rapat peluang, metode Hückel, tiga pusat dua elektron.
- Rujukan antarbab ditulis "subbab x.y" dan dicek dengan grep.
- Jangan menyalin teks atau soal dari buku acuan.

## 5. Desain

**Huruf**: isi Caladea 10 pt, baris 1,4, paragraf menjorok; judul Inter.

**Palet** (berkas CSS per buku menimpa `:root`):

| Buku | Tua | Utama | Muda | Aksen |
|---|---|---|---|---|
| Fisika Umum (`fisika-umum/edisi2/fu.css`) | `#0e2748` | `#1b75bc` | `#7fc0f0` | jingga `#f0a060` |
| Kimia Kuantum (`kimia-kuantum/edisi/kk.css`) | `#1e1548` | `#4a3ab0` | `#5ce1e6` | emas `#f2c25b` |
| Buku baru | pilih satu warna tua, satu warna utama, satu warna muda, satu aksen hangat | | | |

**Unsur yang diseragamkan** (semua sudah ada di `kk.css`, salin lalu ganti palet):
- Judul subbab 12,5 pt, tebal sedang, huruf besar di awal saja, garis bawah tipis.
- Sub-subbab: teks tebal berwarna utama, tanpa kotak.
- Pita judul akhir bab (Soal, Jawaban, Ringkasan, ...): kotak warna tua, sudut tegas, teks putih di tengah 12,5 pt.
- Bagian Soal: judul subbab kapital, nomor serif tebal menggantung, rapat.
- Judul contoh tebal sedang dengan nomor berwarna utama; label "Penyelesaian.", "Memahami hasil." huruf biasa.
- Kotak Tujuan dan Inti: latar muda, garis warna tua, sudut membulat.
- Tanda tanya kuis: huruf Inter putih di kotak warna tua.
- Nomor halaman: kotak warna tua bersudut membulat, angka putih; judul berjalan warna tua.
- Lampiran: huruf besar + "LAMPIRAN" kecil, judul tebal, garis bawah.

**Halaman pembuka bab**: latar putih, garis warna tua di tepi kiri, panel gambar muda di atas, nomor bab warna tua, judul kapital berjarak, kotak Isi bab. Gambar dibuat `edisi/pembuka2.py`: ilustrasi gaya terang yang **menggambarkan isi bab** (alat, molekul, grafik, fenomena), bukan hiasan yang sama terus.

**Sampul** (`edisi/sampul.py`): latar terang, garis warna tua di kiri, EDISI dan NAMA PENYUSUN sebaris di atas, judul dua baris (baris kedua berwarna utama), subjudul dengan garis aksen, **kotak gambar gelap** di setengah bawah berisi satu ilustrasi bercahaya yang mewakili buku (Fisika: garis medan listrik; Kimia Kuantum: jaringan heksagon grafena). Hindari text-shadow (menimbulkan belang di PDF). Sampul belakang: judul kapital, tiga paragraf deskripsi, daftar bab dua kolom (baris kedua menjorok), kotak Tentang Penyusun.

## 6. Alat dan perintah

```bash
# satu bab (pemeriksaan cepat)
cd <buku> && ./build.sh babNN "Bab N"
# buku utuh, versi digital (iPad, tanpa halaman kosong)
python3 <buku>/edisi/cetak.py            # --lewati-bab bila isi bab tidak berubah
# versi cetak (bab mulai di halaman kanan, jumlah halaman genap)
python3 <buku>/edisi/cetak.py --cetak --lewati-bab
# gambar pembuka bab dan sampul
python3 <buku>/edisi/pembuka2.py && python3 <buku>/edisi/sampul.py
```

Hasil: `<Buku>-Edisi-1.pdf` dan `<Buku>-Edisi-1-cetak.pdf`. Salin ke `pdf/`, commit, lalu kirim ke penyusun.

## 7. Memulai buku baru

1. Buat folder `<buku-baru>/` dengan `RENCANA.md` (bab dan subbab, status ☐/◐/☑) dan `PEDOMAN.md` (pembaca, notasi khusus).
2. Salin dari `kimia-kuantum/`: `build.sh`, `gaya.py`, `buku*.css`, `pembuka.css`, `alat/`, dan seluruh `edisi/`.
3. Ganti di `edisi/`: nama buku dan subjudul (`cetak.py`, `sampul.py`), palet (`kk.css` → nama baru), ilustrasi (`pembuka2.py`, `sampul.py`), `depan.md`, `indeks_tambah.txt`.
4. Tulis bab demi bab (materi dulu, desain belakangan), satu sesi untuk satu atau dua bab, commit tiap bab.
5. Setelah semua bab selesai: cetak buku utuh, periksa visual (pembuka bab, soal, lampiran, sampul), cetak versi cetak, salin ke `pdf/`.

## 8. Model dan penghematan

Lihat `PEMETAAN-MODEL.md`: isi ditulis dengan Opus 5.5 (high; xhigh untuk bab tersulit), pekerjaan mesin (gambar, cetak, tata letak) dengan Sonnet 5.5. Jangan menjalankan terlalu banyak sesi paralel; jangan menjadwalkan pemantauan berkala.
