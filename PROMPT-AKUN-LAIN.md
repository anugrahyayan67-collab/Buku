# Prompt induk untuk sesi Claude di akun mana pun

Berkas ini membuat sesi baru (akun lain, perangkat lain, atau sesi yang konteksnya sudah hilang) langsung paham proyek, tahu apa yang harus dikerjakan tanpa disuruh satu per satu, dan tahu alat apa yang tersedia.

**Cara pakai di akun lain.**

1. Kirim ke akun itu (unggah ke chat atau ke *Project knowledge*):
   - `sumber.zip`: semua berkas repo kecuali PDF (naskah Markdown, `_soal.txt`, `_akhir.md`, skrip `alat/` dan `edisi/`, gambar `fig/`, semua pedoman). Dibuat dengan `git ls-files | grep -v '\.pdf$' | zip -@ sumber.zip`.
   - PDF akhir dari `pdf/` (Fisika Umum, Kimia Kuantum, Kimia Fisika 1, Kimia Organik 1) sebagai bacaan dan pembanding hasil.
   - `DESAIN-BUKU.md` (juga ada di dalam zip): spesifikasi lengkap huruf, ukuran, margin, warna, dan tata letak.
   - Berkas ini juga ada di dalam zip, tetapi boleh diunggah terpisah supaya langsung terbaca.
2. Tempelkan blok "Teks untuk ditempel" ke pesan pertama, atau ke instruksi proyek/custom instructions akun itu.
3. Bila akun itu memakai **Claude Code** (web atau terminal), sebaiknya buat repo GitHub baru dari isi `sumber.zip` (atau beri akses ke repo lama), supaya alat cetak dan commit berjalan seperti biasa. Bila hanya **chat claude.ai** dengan eksekusi kode, naskah dan gambar tetap bisa dikerjakan, tetapi cetak PDF utuh (pandoc + Chromium) mungkin tidak tersedia; dalam hal itu kirim berkas `.md` dan gambar yang berubah, lalu cetak di sesi yang punya alat lengkap.

Sisanya (bagian 1–9) adalah rincian yang dibaca sesi itu sendiri.

---

## Teks untuk ditempel

```
Kamu melanjutkan proyek seri buku kuliah S1 Kimia berbahasa Indonesia milik penyusun.
Penyusun membaca hasilnya di iPad dan berbicara santai dalam bahasa Indonesia; jawab juga
santai, tetapi isi buku ditulis dalam bahasa Indonesia baku yang enak dibaca.

Bahan yang kuberikan: sumber.zip (seluruh naskah, skrip, gambar, dan pedoman) dan
PDF akhir buku. Langkah pertama:
1. Ekstrak sumber.zip (atau pakai repo GitHub bila tersedia) dan jalankan
   `python3 status.py` di akar folder.
2. Baca, berurutan: CLAUDE.md, PROMPT-AKUN-LAIN.md, PROMPT-BUKU.md, PANDUAN-BUKU.md,
   DESAIN-BUKU.md (semua ukuran huruf, margin, warna, tata letak), lalu RENCANA.md dan PEDOMAN.md di folder buku yang akan dikerjakan.

Cara kerja:
- Bila aku memberi perintah jelas, kerjakan itu.
- Bila aku hanya bilang "lanjut", "gas", "kerjakan", atau tidak memberi perintah
  khusus, ambil pekerjaan pertama yang belum selesai di bagian 3 PROMPT-AKUN-LAIN.md
  dan kerjakan sampai tuntas tanpa menunggu izin per langkah, lalu lanjut ke berikutnya.
- Bertanya hanya bila benar-benar tidak bisa diputuskan dari berkas yang ada.
- Kerjakan sendiri tanpa subagen. Semua angka dihitung dengan Python dulu.
- Setiap selesai satu bab atau satu tahap: kirim PDF (atau berkas hasil) kepadaku,
  perbarui catatan status di PROMPT-AKUN-LAIN.md dan RENCANA.md, dan bila ada repo,
  commit + push.
```

---

## 1. Proyek dan keadaannya

- **Isi repo**: naskah Markdown + alat cetak (pandoc → HTML → Playwright/Chromium → PDF) untuk seri buku S1 Kimia. Daftar buku, urutan, dan status: `RENCANA-SERI.md`. Keadaan terkini selalu dicek dengan `python3 status.py`.
- **Penyusun**: mahasiswa kimia. Yang boleh ditulis di berkas hanya namanya (sudah ada di `README.md`); jangan menulis surel, tanggal lahir, atau data pribadi lain.
- **Buku yang sudah ada** (per 21-11-2026):

| Buku | Folder | Keadaan |
|---|---|---|
| Fisika Umum | `fisika-umum/` | Edisi 1 selesai (15 bab); alat cetak `fisika-umum/edisi2/cetak.py`, catatan teknis `fisika-umum/CATATAN.md` |
| Kimia Kuantum | `kimia-kuantum/` | Edisi 1 selesai (17 bab) |
| Kimia Fisika 1: Termodinamika Kimia | `termodinamika-kimia/` | Edisi 1.2: 15 bab selesai; sisa soal Bab 3, 6, 7, 8, baca ulang, dan cetak akhir |
| Kimia Organik 1: Senyawa Monofungsi | `kimia-organik/` | 16 bab selesai; PDF digital di `pdf/` |
| Persiapan TEP | `persiapan-tep/` | rancangan dan pedoman ada, bab belum |
| Buku lain di `RENCANA-SERI.md` | belum ada | belum |

- **PDF akhir** disimpan di `pdf/` (digital dan `-cetak` bolak-balik), dicatat di `pdf/README.md`. PDF lain tidak di-commit.

## 2. Standar isi (ringkas; rinciannya di `PROMPT-BUKU.md`)

- Selengkap buku teks internasional (Atkins, Levine, Klein, McMurry, Clayden, Harris, Housecroft, dsb.), tetapi semua teks, contoh, dan soal ditulis sendiri.
- Per bab: ± 35–50 halaman, ± 15–25 contoh, ± 80–100 soal tanpa label tingkat, ± 20 pertanyaan konsep, 6–11 pembahasan (masing-masing dengan paragraf *Cara berpikir:*), gambar sebanyak yang dibutuhkan (biasanya 6–12).
- Gaya: mengapa sebelum bagaimana; tidak ada langkah yang diloncati; gambaran sebelum rumus; sapaan "kamu/kita"; contoh dari kimia nyata; kesalahan umum di kotak `.awas`.
- Susunan bab: teka-teki pembuka → Pertanyaan pembuka, Tujuan belajar, Prasyarat → subbab `## N.k` masing-masing dengan kuis cepat → "Menuju bab berikutnya" → akhir bab (Ringkasan + jawaban kuis, Pertanyaan per subbab, Soal per subbab, Jawaban, Pembahasan, Bacaan lanjut ≤ 6).
- Label contoh: **Gambaran fisis** (opsional) · **Rencana** (opsional) · **Penyelesaian** · **Memahami hasil**.
- LaTeX: koma desimal `9{,}8`; tanpa `\cancel` dan `\tag`.
- Gambar: matplotlib, Liberation Sans, 220 dpi, palet seri (`CLAUDE.md`), label sumbu dengan koma desimal; setiap gambar diperiksa visual sebelum dipakai.
- Desain halaman (huruf, ukuran, margin, kotak, pembuka bab, kepala halaman, sampul): `DESAIN-BUKU.md`.

## 3. Pekerjaan berikutnya dan cara memutuskan sendiri

Daftar pekerjaan yang belum selesai, **berurutan**. Bila tidak ada perintah khusus, kerjakan butir ☐ pertama. Setelah selesai, ubah menjadi ☑ (dengan tanggal) di daftar ini juga.

1. ☑ (21-11-2026) **Kimia Fisika 1, Bab 15 Termodinamika Permukaan** (`termodinamika-kimia/`). Lihat catatan status di `termodinamika-kimia/RENCANA.md`; bila sudah ☑ di sana, lewati. Subbab: tegangan permukaan dan energi permukaan · persamaan Young–Laplace · kapilaritas dan sudut kontak · persamaan Kelvin dan nukleasi · persamaan adsorpsi Gibbs · surfaktan dan misel · isoterm adsorpsi (Langmuir, BET). Setelah selesai, "Penutup" buku ada di akhir Bab 15 (bukan Bab 14).
2. ☐ **Kimia Fisika 1: soal Bab 3, 6, 7, 8 dilengkapi sampai ± 80** (pakai `alat/tebal.py`).
3. ☐ **Kimia Fisika 1: baca ulang kejelasan Bab 1–15**, satu bab per putaran; catat temuan dan perbaikan di `termodinamika-kimia/REVISI.md`.
4. ☐ **Kimia Fisika 1: cetak akhir** digital dan `--cetak`, salin ke `pdf/`, perbarui `pdf/README.md`, kirim PDF.
5. ◐ **Kimia Organik 1**: versi digital dan cetak sudah di `pdf/` (21-11-2026); ilustrasi sampul diganti motif organik (☑ 24-11-2026: parasetamol + panah lengkung, halaman sampul di kedua PDF ditukar tanpa cetak ulang); belum: baca ulang kejelasan Bab 1–16.
6. ☐ **Persiapan TEP** (`persiapan-tep/`): Bab 1–4 dulu, ikuti `persiapan-tep/PEDOMAN.md`; siapkan alat cetak dengan pola `kimia-organik/edisi/`.
7. ◐ **Kimia Anorganik 1: Teori Dasar** (`kimia-anorganik/`, dimulai 25-11-2026 atas permintaan penyusun): Bab 1–4 ☑ (Bab 3 menambah Lampiran B tabel karakter dan mesin `alat/grup.py`; Bab 4 memakai PySCF di `alat/hitung_bab04.py`, `pip install pyscf`); lanjutkan Bab 5–13 berurutan menurut `kimia-anorganik/RENCANA.md` dan `PEDOMAN.md`, satu bab per sesi. Tambah gambar pembuka bab di `edisi/pembuka2.py` dan istilah di `edisi/indeks_tambah.txt` setiap bab.
8. ☐ **Matematika untuk Kimia**, lalu buku berikutnya di `RENCANA-SERI.md` (rancangan dulu, lalu bab demi bab).

Aturan memutuskan sendiri:
- Perbaiki dulu hal yang rusak (build gagal, rujukan `??`, `{{kunci}}` yang tidak terganti, gambar terpotong), baru lanjut ke daftar.
- **Satu sesi = satu bab baru** (paling banyak dua). Pekerjaan kecil (gambar, soal, cetak ulang, baca ulang) boleh beberapa dalam satu sesi.
- Keputusan isi yang tidak tercatat (misalnya urutan bab buku baru): pilih yang paling sesuai dengan buku acuan, catat alasannya di `RENCANA.md`, sebutkan di laporan. Jangan berhenti hanya untuk bertanya.
- Bertanya hanya bila perintah bisa berarti dua pekerjaan berbeda, atau tindakan tidak bisa dibatalkan (menghapus berkas besar, menimpa PDF akhir dengan versi yang lebih buruk).
- Setiap butir selesai: perbarui daftar di atas, status di `RENCANA.md` buku itu, dan `RENCANA-SERI.md`.

## 4. Alat di repo dan jebakannya

Penyiapan sesi baru (lihat juga `CLAUDE.md`):
```bash
pip install reportlab pypdf matplotlib 2>/dev/null   # pandoc dan Playwright biasanya sudah ada
ln -sfn "$PWD/fisika-umum" ~/fisika-umum              # hanya untuk Fisika Umum
```

Alat per buku (contoh `termodinamika-kimia/`; buku lain berpola sama):

| Alat | Fungsi |
|---|---|
| `alat/nomor.py babNN N` | menomori Contoh, Gambar, persamaan dari label sementara (`Contoh N.xabc ·`, `Gambar N.gabc`, `\text{(N.eabc)}`), dan memperbarui rujukan di bab lain |
| `alat/soal.py babNN` | menyusun `z-akhir.md` dari `_akhir.md` + `_soal.txt` (soal `teks ||| jawaban`, soal dibahas `@kunci [P] teks ||| jawaban`, rujukan `**Soal {{kunci}}.**`) |
| `alat/periksa.py N` | statistik dan pemeriksaan bab (kata, contoh, soal, gambar, kotak) |
| `alat/tebal.py` | fungsi `sisip`, `soal`, `tanya`, `bahas`, `ringkas` untuk menambah isi ke bab yang sudah ada |
| `alat/gambar/babNN*.py` | skrip gambar per bab |
| `edisi/cetak.py` | cetak buku utuh (± 10 menit; jalankan dengan timeout ≥ 595 detik atau di latar belakang); `--lewati-bab` bila isi bab tidak berubah; `--cetak` untuk versi bolak-balik |
| `edisi/pembuka2.py`, `edisi/sampul.py`, `edisi/indeks_tambah.txt` | gambar pembuka bab, sampul, istilah indeks |

Jebakan yang sudah pernah terjadi:
- Jangan menulis nomor final (misalnya "Gambar 8.4") untuk butir yang belum dinomori; pakai label sementara, lalu jalankan `nomor.py`. Kalau tidak, muncul galat `??N` atau rujukan bergeser.
- `nomor.py` menganggap setiap `(N.k)` sebagai rujukan persamaan. Rujukan subbab ditulis "subbab N.k", jangan "(N.k)".
- Tabel tidak dinomori otomatis; nomori manual.
- `{{kunci}}` hanya diganti di `z-akhir.md`. Di naskah bab, rujuk soal dengan nomornya (lihat `z-akhir.md`).
- `tebal.soal()` mengembalikan `'sudah'` bila 40 karakter pertama butir pertama sudah ada; ubah urutan atau kalimat pembuka.
- Setelah `nomor.py`, periksa `git status`: rujukan di bab lain (`_akhir.md`) mungkin ikut berubah dan harus ikut di-commit.
- Sebelum menyerahkan PDF, cari teks `{{`, `??`, `Gambar N.g`, `Contoh N.x` di PDF dengan pypdf; hasilnya harus nol.
- Periksa gambar dengan melihat PNG-nya (beberapa digabung dalam satu lembar); perbaiki teks yang menimpa garis sebelum dipakai.

Git: commit dengan pesan yang menjelaskan isi, diakhiri baris atribusi yang diminta lingkungan sesi; push `git push -u origin kimia-kuantum-bab01` (ulangi bila gagal jaringan). Jangan menulis nama model di pesan commit.

## 5. Plugin dan konektor Anthropic (anggap sudah tersambung)

Gunakan bila memang membantu; pekerjaan inti tetap dengan alat repo.

| Plugin / konektor | Penerbit | Dipakai untuk |
|---|---|---|
| **PDF Viewer** (skill `view-pdf`, perintah `open`, `annotate`) | Anthropic | Membuka PDF buku di penampil interaktif agar penyusun bisa memberi coretan/anotasi revisi. Bila penyusun mengirim PDF beranotasi, baca semua anotasinya, kelompokkan per bab, kerjakan, lalu laporkan anotasi mana yang sudah ditangani. |
| **math-olympiad** | Anthropic | Memverifikasi penurunan atau bukti yang sulit (Kimia Kuantum, Matematika untuk Kimia, penurunan termodinamika statistik) dengan pemeriksa terpisah. Tidak dipakai untuk hitungan rutin; itu tetap Python. |
| **Claude Education Skills Library** (165 skill) | komunitas, lolos review direktori | Merancang dan menilai bagian pedagogis. Yang paling berguna: `practice-problem-sequence-designer` (urutan soal per subbab), `worked-example-fading-designer` (contoh → soal), `hinge-question-designer` dan `erroneous-example-designer` (pertanyaan konsep dan kotak `.awas`), `cognitive-load-analyser` dan `language-demand-analyser` (baca ulang kejelasan), `retrieval-practice-generator` (kuis cepat). Hasilnya disesuaikan dengan format buku; jangan menambah label tingkat atau proyek. |
| **Google Drive** (bila tersambung di akun itu) | konektor | Mengunggah PDF akhir ke Drive supaya mudah dibuka di iPad, selain lewat SendUserFile. |
| **Canva** (bila tersambung) | konektor | Opsional: sampul atau slide ringkasan bab bila penyusun meminta. |

Nama skill dari plugin muncul dengan awalan kode plugin (`<kode>:nama-skill`); cari nama lengkapnya di daftar skill sesi sebelum memanggil.

## 6. Model dan effort

Ikuti `PEMETAAN-MODEL.md`: menulis isi dan revisi isi dengan Opus 5.5 (effort high; xhigh untuk bab tersulit), pekerjaan mesin (gambar, cetak, perbaikan kecil) boleh Sonnet 5.5. Fable dan Haiku tidak dipakai.

## 7. Laporan ke penyusun

Setelah setiap tahap, laporkan dalam bahasa Indonesia santai, singkat, berurutan:
1. Apa yang selesai, dengan angka (subbab, contoh, soal, gambar, halaman).
2. Hal yang perlu diketahui penyusun (angka yang dikoreksi, keputusan yang diambil sendiri beserta alasannya, data yang perlu dicek).
3. Pekerjaan berikutnya menurut bagian 3.

Kirim PDF terbaru lewat SendUserFile setiap ada perubahan isi yang berarti.

## 8. Yang tidak diinginkan

- Menunggu izin untuk langkah yang sudah jelas dari bagian 3 atau pedoman.
- Menulis buku/bab yang tidak ada di bagian 3 atau rencana tanpa alasan.
- Penjelasan tipis, langkah diloncati, kalimat pengisi untuk menebalkan.
- Label tingkat soal, latihan ujian, proyek.
- Menyalin teks atau soal dari buku acuan.
- Angka yang tidak dihitung ulang.
- Data pribadi penyusun selain nama.

## 9. Memperbarui berkas ini

Bila ada aturan baru dari penyusun, alat baru, atau buku baru selesai, perbarui berkas ini (tabel bagian 1 dan daftar bagian 3) pada commit yang sama.
