# Spesifikasi desain buku seri (berlaku untuk keempat buku: Fisika Umum, Kimia Kuantum, Kimia Fisika 1, Kimia Organik 1; diseragamkan 24-11-2026)

Dokumen ini mencatat **semua ukuran, huruf, warna, dan tata letak** yang dipakai buku seri, diambil dari berkas yang benar-benar dipakai untuk mencetak. Siapa pun (manusia atau AI) yang meneruskan atau membuat buku baru dalam seri ini cukup mengikuti dokumen ini supaya hasilnya serupa.

Sumber aturan (urutan berlaku, yang belakang menimpa yang depan):
`<buku>/buku.css` → `buku2.css` → `buku3.css` → `pembuka.css` → `<buku>/edisi/<palet>.css` (`ko.css` untuk Organik, `tk.css` untuk Kimia Fisika 1). Kepala dan nomor halaman digambar `edisi/cetak.py`; sampul oleh `edisi/sampul.py`; gambar pembuka bab oleh `edisi/pembuka2.py`; pengubahan HTML (kelas judul, label contoh) oleh `gaya.py`.

---

## 1. Halaman

| Unsur | Nilai |
|---|---|
| Ukuran kertas | A4, 210 × 297 mm, tegak |
| Margin isi | atas 22 mm · kanan 18 mm · bawah 19 mm · kiri 18 mm (`edisi/render.cjs`); sama di halaman ganjil dan genap |
| Lebar teks | 174 mm, satu kolom (bagian Pertanyaan dan Soal dua kolom, lihat 9) |
| Versi digital | tanpa halaman kosong; setiap bab langsung menyambung |
| Versi cetak (`--cetak`) | halaman kosong disisipkan agar setiap bab mulai di halaman kanan (ganjil); jumlah halaman genap |
| Mesin cetak | Markdown → pandoc (`--mathml`) → HTML + CSS → Chromium (Playwright) → PDF; kepala halaman ditumpangkan dengan reportlab + pypdf |

## 2. Huruf

| Pemakaian | Huruf | Ukuran | Lain-lain |
|---|---|---|---|
| Teks isi | **Caladea** (cadangan Liberation Serif) | 10 pt | baris 1,4; rata kanan-kiri; pemenggalan otomatis (`hyphens: auto`); warna `#141a24` |
| Paragraf | — | — | jarak antarparagraf 0; paragraf kedua dan seterusnya menjorok 1,5 em; paragraf tepat setelah persamaan peraga tidak menjorok |
| Semua judul, kepala tabel, daftar isi, indeks, label | **Inter** (cadangan Liberation Sans) | lihat tiap unsur | |
| Isi kotak (contoh, kuis, inti, dll.) | Caladea | 9,5 pt | baris 1,38; jarak antarparagraf 0,45 em |
| Keterangan gambar | Caladea | 8,5 pt | baris 1,4; rata kiri |
| Tabel | Caladea | 9,1 pt | baris 1,35; kepala 8,7 pt Inter tebal |
| Kode | JetBrains Mono / Liberation Mono | 8,5 pt | |
| Rumus | MathML (huruf matematika Chromium) | mengikuti teks | persamaan peraga berjarak 2,2 mm atas-bawah |
| Kepala halaman | Helvetica-Bold (dari reportlab) | 7 pt (teks), 8,5 pt (nomor) | |

Huruf Caladea dan Inter bebas lisensi (paket `fonts-crosextra-caladea` dan Inter dari rsms.me/inter); keduanya harus terpasang di mesin cetak.

## 3. Warna

Setiap buku punya palet sendiri yang menimpa variabel CSS `:root`. Tata letaknya identik; hanya warnanya yang berganti.

| Variabel | Peran | Kimia Organik 1 (`ko.css`) | Kimia Fisika 1 (`tk.css`) | Fisika Umum (`fu.css`) |
|---|---|---|---|---|
| `--tua` | warna tua: garis kotak, judul, pita | `#143d2a` hijau hutan | `#3d1418` merah anggur | `#0e2748` biru malam |
| `--biru` | warna utama: nomor, sub-subbab, kuis | `#2e8b57` hijau laut | `#b4442b` bata | `#1b75bc` biru |
| `--langit` | warna muda kuat | `#9fd8a8` | `#f4a261` | `#7fc0f0` |
| `--muda` | latar kotak | `#eff8f1` | `#fcf2ee` | `#edf5fc` |
| `--garis` | garis tipis | `#c9e6d0` | `#f0d0c4` | `#cfe0f0` |
| `--jingga` | aksen (nomor soal, label "Memahami hasil", penanda daftar) | `#b9801a` emas | `#b9801a` emas | `#c0601f` |
| `--jingga-t` | aksen terang | `#e9b949` | `#e9b949` | `#f0a060` |
| `--hangat` | kotak "Lebih dalam" | `#b5541c` | `#b5541c` | `#b5541c` |
| latar kotak umum | | `#f5fbf7` | `#fdf7f4` | |

Kimia Kuantum memakai palet ungu (`#1e1548`, `#4a3ab0`, `#5ce1e6`, emas `#f2c25b`). Buku baru memilih satu warna tua, satu utama, satu muda, dan satu aksen hangat.

**Gambar isi** (matplotlib) memakai satu palet tetap di semua buku, tidak mengikuti warna buku: biru tua `#0e2748`, biru `#1b75bc`, biru muda `#7fc0f0`, jingga `#f0a060` dan `#b5541c`, hijau `#1a8a6a`.

## 4. Judul

| Unsur | Gaya |
|---|---|
| Halaman pembuka bab | satu halaman penuh, lihat bagian 10 |
| **Subbab** `## N.k Judul` (`h2.sub`) | Inter 12,5 pt tebal 700, warna tua, huruf besar di awal saja; nomor sewarna judul berjarak 1,3 mm; garis bawah 1 px warna garis; jarak atas 8 mm, bawah 2,5 mm; baris 1,25; tidak boleh terpisah dari paragraf sesudahnya |
| **Sub-subbab** `### Judul` (`h3`) | Inter 10,8 pt tebal 700, warna utama, tanpa kotak/penanda; jarak atas 4,5 mm, bawah 1,5 mm |
| Judul kecil (`h2.kecil`, misalnya "Subbab N.k: …" di akhir bab) | Inter 10,5 pt tebal 700; di bagian Soal/Pertanyaan: kapital, 9,6 pt, jarak huruf 0,6 px |
| **Pita akhir bab** (Ringkasan, Pertanyaan, Soal, Jawaban, Pembahasan soal terpilih, Bacaan lanjut) (`h1.pita1`) | kotak warna tua, sudut tegas, teks putih Inter 12,5 pt tebal 700 di tengah; padding 1,8 × 4 mm; jarak bawah 4 mm; selalu mulai di halaman baru |
| Lampiran (`h1.bab`) | "LAMPIRAN" Inter 10 pt tebal 800, jarak huruf 7 px, warna aksen; huruf lampiran 60 pt tebal 900 warna tua; judul di kanannya 17 pt tebal 800 kapital, jarak huruf 1,2 px; garis bawah 0,4 mm warna garis |

## 5. Kotak

**Sejak 25-11-2026 (permintaan penyusun): semua kotak memakai satu kombinasi warna**: garis kiri warna tua, latar terang (warna muda 60 % dicampur putih), judul warna tua. Tabel di bawah mencatat warna lama sebelum penyeragaman; aturan baru ada di bagian akhir setiap `<palet>.css`.

Semua kotak memakai satu sistem: **bingkai tipis 0,3 mm warna garis, garis aksen kiri 1,6 mm, sudut kanan membulat 2 mm**, padding 3,4 mm (atas) 5,5 mm (kanan) 3 mm (bawah) 5,5 mm (kiri), jarak 4,5 mm atas-bawah. Judul kotak (kata tebal pertama, misalnya **Tujuan belajar**) Inter 9,8 pt tebal 700. Kotak tidak boleh terpotong ke halaman berikut (kecuali kotak contoh yang panjang).

| Kotak (Markdown) | Latar | Garis kiri | Warna judul | Isi |
|---|---|---|---|---|
| `.strategi` (Pertanyaan pembuka, Strategi) | latar kotak umum | tua | tua | daftar bernomor, penanda warna utama |
| `.tujuan` (Tujuan belajar) | latar kotak umum | tua | tua | "Setelah mempelajari bab ini, kamu mampu:" + 7–9 butir |
| `.mat` sesudah Tujuan (Prasyarat) | latar kotak umum | tua | tua | |
| `.mat` di dalam teks (matematika) | `#fdf9f0` | aksen | aksen | |
| `.inti` (hasil terpenting) | muda | utama | tua | rumus inti + satu kalimat tebal; jarak 4 mm, padding 3 × 6 mm |
| `.dalam` (Lebih dalam) | putih | hangat | hangat | |
| `.terapan` (Terapan) | `#fdf8ea` | aksen terang | aksen | |
| `.awas` (Awas: kesalahan umum) | `#fdefeb` | `#c0392b` | `#a5281b` | |
| `.kuis` (Kuis cepat N.k) | muda | utama | tua | kotak "?" 7 × 7 mm, sudut 1,6 mm, latar tua, huruf Inter 11,5 pt tebal putih, di kiri (4 mm dari tepi); padding kiri teks 15 mm |

**Kotak contoh** (`.contoh`), berbeda dari kotak lain:
- garis atas 0,7 mm warna tua; pita latar muda setinggi 9,5 mm di bagian atas tempat judul; garis bawah 0,3 mm warna garis; jarak 7 mm atas-bawah; padding samping 1 mm;
- judul "**Contoh N.k · Judul**": Inter 10,3 pt tebal 700 warna tua, nomor "Contoh N.k" warna utama;
- label bagian: **Gambaran fisis.** (opsional) · **Rencana.** (opsional) · **Penyelesaian.** · **Memahami hasil.**: Inter 9,6 pt tebal 700, warna utama; "Memahami hasil." warna aksen;
- isi Caladea 9,5 pt.

## 6. Tabel

- Keterangan tabel ditulis sebagai paragraf biasa **di atas** tabel: "Tabel N.k Judul." (dinomori manual), tidak menjorok, menempel pada tabelnya.
- Kepala: latar warna tua, teks putih Inter 8,7 pt tebal 700, padding 2 mm; kepala diulang bila tabel menyambung ke halaman berikut.
- Sel: padding 1,5 × 2 mm, garis bawah 0,3 px warna garis, baris genap berlatar muda 60 persen; baris tidak boleh terpotong.
- Garis penutup bawah 0,6 mm warna tua; lebar 100 persen; jarak 4 mm atas, 5 mm bawah.

## 7. Gambar

- Berkas PNG 220 dpi dari matplotlib, huruf Liberation Sans, label sumbu dengan koma desimal; lebar di naskah `{width=70%}` sampai `{width=96%}` (grafik tunggal biasanya 76–84 persen, dua panel 92–96 persen).
- Jarak 4 mm atas-bawah, di tengah, tidak terpotong halaman; sudut gambar dibulatkan 0,5 mm.
- Keterangan di bawah gambar: label "GAMBAR N.k" Inter 8,2 pt kapital tebal 800 warna aksen, lalu teks Caladea 8,5 pt rata kiri dengan margin samping 6 mm. Keterangan menjelaskan **apa yang harus dilihat**, bukan hanya judul.

## 8. Rumus, daftar, dan teks lain

- Persamaan peraga di tengah, nomor di kanan "(N.k)" dengan `\qquad \text{(N.k)}`; rumus berbingkai (`\boxed`) berbingkai 0,9 px warna utama berlatar muda.
- Daftar: menjorok 6 mm, penanda (angka/titik) warna aksen; jarak butir 0,15 em.
- Tautan tidak bergaris bawah dan berwarna teks.

## 9. Akhir bab

- **Ringkasan**: tabel tiga kolom (Gagasan · Rumus atau hasil · Subbab), lalu paragraf "**Jawaban kuis cepat.**" berisi jawaban semua kuis.
- **Pertanyaan** dan **Soal**: **dua kolom** (turun di kiri, lalu lanjut di kanan), jarak antarkolom 8 mm, garis pemisah 0,3 px warna garis; rata kanan-kiri. Catatan data (blockquote) di atas, selebar dua kolom. Judul tiap kelompok "SUBBAB N.K: JUDUL" kapital 9,6 pt. Nomor soal menggantung: kotak 7,5 mm, nomor rata kanan, Caladea tebal 10 pt; teks soal mulai di garis yang sama. Tanpa label tingkat kesulitan.
- **Jawaban**: daftar bernomor rapat.
- **Pembahasan soal terpilih**: "**Soal N.**" tebal, penyelesaian, lalu paragraf *Cara berpikir:* miring.
- **Bacaan lanjut**: daftar bernomor, paling banyak enam judul, masing-masing satu kalimat keterangan.

## 10. Halaman pembuka bab

Satu halaman A4 penuh tanpa margin (`section.pembuka`), semua posisi mutlak dari tepi kertas:

| Unsur | Letak dan gaya |
|---|---|
| Latar | putih; pita warna tua 7 mm di tepi kiri |
| Panel gambar | kiri 20 mm, kanan 18 mm, atas 22 mm, tinggi 98 mm; gradasi warna muda (Organik `#e6f4ea` → `#f7fcf8`; Kimia Fisika `#fbece6` → `#fef9f7`) |
| Ilustrasi | 160 × 90 mm, atas 26 mm, kiri 26 mm; PNG transparan dari `edisi/pembuka2.py` yang menggambarkan isi bab (alat, molekul, grafik, fenomena) dengan palet buku |
| Keterangan ilustrasi | atas 122 mm, rata kanan (kanan 18 mm); Caladea miring 8,5 pt |
| Nama bagian ("BAGIAN II · …") | atas 11 mm, kiri 20 mm; Inter 8,5 pt tebal 700, jarak huruf 3 px, kapital, warna utama |
| Kata "BAB" | atas 140 mm, kiri 20 mm; Inter 11 pt tebal 800, jarak huruf 8 px, warna aksen |
| Nomor bab | atas 145 mm, kiri 17 mm; Inter 70 pt tebal 900, jarak huruf −3 px, warna tua |
| Judul bab | atas 153 mm, kiri 55 mm, kanan 18 mm; Inter 17 pt tebal 800, kapital, jarak huruf 1,2 px, baris 1,25, warna tua |
| Kotak "Isi bab" | atas 182 mm, kiri 20 mm, kanan 18 mm; kepala pita warna tua, teks putih Inter 10,5 pt tebal 700, padding 1,4 × 4 mm; daftar subbab dua kolom (jarak 9 mm), Inter 9 pt, baris 1,35, nomor subbab lebar 9 mm warna utama |

Halaman pembuka tidak diberi kepala halaman; nomornya dicetak di tengah bawah (lihat 11).

## 11. Kepala dan nomor halaman

Digambar di atas setiap halaman isi oleh `edisi/cetak.py`:

| Unsur | Nilai |
|---|---|
| Garis dasar teks kepala | 13 mm dari tepi atas kertas; batas kiri dan kanan 18 mm |
| Nomor halaman | kotak warna tua bersudut 1,2 mm, tinggi 5 mm, lebar teks + 4 mm (paling kecil 7 mm); angka putih Helvetica-Bold 8,5 pt di tengah |
| Halaman ganjil (kanan) | nomor di kanan; di kirinya (berjarak 3 mm) judul berjalan "BAB N · JUDUL BAB" kapital, Helvetica-Bold 7 pt warna tua |
| Halaman genap (kiri) | nomor di kiri; di kanannya nama buku kapital ("KIMIA ORGANIK 1", "KIMIA FISIKA 1") |
| Garis kepala | 0,5 pt warna garis, 2,6 mm di bawah garis dasar, dari tepi kiri ke kanan teks |
| Halaman pembuka bab | tanpa kepala; nomor Helvetica-Bold 8,5 pt warna tua di tengah, 9 mm dari tepi bawah |
| Bagian depan | angka Romawi kecil |

## 12. Bagian depan dan belakang buku

Urutan: sampul depan → halaman judul → halaman keterangan → isi ringkas (satu halaman) → daftar isi → bagian depan (cara memakai buku, kotak, notasi) → bab-bab → lampiran → indeks → sampul belakang.

- **Halaman judul**: garis kiri 3 mm warna tua, mulai 25 mm dari atas; judul Inter 46 pt tebal 900, dua baris kapital ("KIMIA / ORGANIK 1"), jarak huruf −1 px; subjudul 15 pt tebal 600 warna utama; nama penyusun 12 pt tebal 700 kapital, jarak huruf 1,5 px; label "EDISI PERTAMA" putih di kotak warna tua, 10 pt tebal 800, jarak huruf 3 px.
- **Halaman keterangan**: Inter 8,6 pt di bagian bawah halaman: judul lengkap, edisi dan tahun, nama penyusun.
- **Isi ringkas dan daftar isi**: Inter; baris bab 11,2–11,6 pt tebal 800 warna tua dengan kotak nomor bab (latar tua, teks putih, sudut 1,5 mm, lebar paling kecil 9 mm); subbab 9,6 pt menjorok 12 mm, nomor subbab warna aksen; garis titik-titik ke nomor halaman; judul bagian buku 8,5 pt kapital, jarak huruf 2 px. Semua baris bertaut ke halamannya.
- **Indeks**: dua kolom (jarak 9 mm), Inter 8,6 pt, baris 1,38; huruf pembuka 13 pt putih di kotak warna tua; istilah dipilih dari `edisi/indeks_tambah.txt`.
- **Sampul depan** (`edisi/sampul.py`, HTML 210 × 297 mm tanpa margin, latar sangat muda): pita warna tua 9 mm di kiri; "EDISI PERTAMA" (kiri, 22 mm) dan nama penyusun (kanan, 18 mm) sebaris 24 mm dari atas, Inter 9 pt tebal 800, jarak huruf 6 px; judul 54 pt tebal 900, baris 0,88, dua baris, baris kedua warna utama, 36 mm dari atas; subjudul 13 pt, lebar 130 mm, 77 mm dari atas, dengan garis aksen 0,6 mm di atasnya; panel gelap (gradasi radial warna tua) dari 98 mm sampai 22 mm dari bawah berisi satu ilustrasi bercahaya yang mewakili buku (Fisika Umum: garis medan listrik; Kimia Kuantum: jaringan heksagon grafena; Kimia Fisika 1: isoterm dan siklus Carnot bercahaya; Kimia Organik 1: rumus kerangka parasetamol bercahaya dengan panah lengkung Nu⁻ → C=O dan kerangka molekul samar di latar). Catatan: sampul Kimia Organik 1 saat ini masih memakai ilustrasi isoterm dan siklus Carnot yang sama (diwarnai hijau); sebaiknya diganti motif organik, misalnya cincin benzena atau mekanisme bercahaya. Hindari bayangan teks.
- **Sampul belakang**: judul kapital 18 pt tebal 900 (kata kedua warna utama), tiga paragraf deskripsi Caladea 10,5 pt baris 1,6, daftar bab dua kolom Inter 9,2 pt (nomor warna aksen, baris kedua menjorok 8 mm, garis atas 0,5 mm warna tua), kotak "TENTANG PENYUSUN" di bawah berlatar muda.
- **Metadata PDF**: judul lengkap dan edisi, nama penyusun, subjek singkat; bookmark per bab dan subbab.

## 13. Gaya penulisan yang terlihat di halaman

- Contoh, gambar, dan persamaan dinomori per bab (N.k) oleh `alat/nomor.py`; tabel dinomori manual.
- Satuan dan angka: koma desimal, spasi tipis untuk ribuan di LaTeX (`96\,485`), satuan tegak.
- Sapaan "kamu" dan "kita"; bahasa Indonesia baku.

## 14. Berkas yang membentuk desain

| Berkas | Isi |
|---|---|
| `<buku>/buku.css`, `buku2.css`, `buku3.css`, `pembuka.css` | gaya dasar seri (sama di semua buku) |
| `<buku>/edisi/<palet>.css` | palet buku + semua penyesuaian terakhir (sistem kotak, soal dua kolom, pembuka bab terang, lampiran) |
| `<buku>/gaya.py` | menambah kelas HTML: `h1.bab`, `h1.pita1`, `h2.sub`, `h2.kecil`, `strong.lk`, label gambar |
| `<buku>/edisi/cetak.py` | merakit buku utuh, penomoran, kepala halaman, daftar isi, indeks, bookmark, versi cetak |
| `<buku>/edisi/render.cjs` | HTML → PDF dengan Chromium (ukuran A4 dan margin) |
| `<buku>/edisi/pembuka2.py`, `sampul.py`, `depan.md` | ilustrasi pembuka bab, sampul, bagian depan |

Untuk buku baru: salin seluruh folder `edisi/`, `gaya.py`, dan keempat `*.css` dari `kimia-organik/`, lalu ganti palet di `<palet>.css` dan di `cetak.py` (warna kepala halaman `BIRU, TUA, GARIS`), nama buku, ilustrasi, dan `depan.md`.
