# Prompt induk untuk sesi Claude di akun mana pun

Berkas ini membuat sesi baru (akun lain, perangkat lain, atau sesi yang konteksnya sudah hilang) langsung paham proyek, tahu apa yang harus dikerjakan tanpa disuruh satu per satu, dan tahu alat apa yang tersedia.

**Cara pakai.** Tempelkan blok di bagian "Teks untuk ditempel" ke pesan pertama sesi baru, atau ke *instruksi proyek / custom instructions* akun itu. Sisanya (bagian 1–9) adalah rincian yang akan dibaca sesi itu sendiri dari repo.

---

## Teks untuk ditempel

```
Kamu melanjutkan proyek seri buku kuliah S1 Kimia berbahasa Indonesia di repo GitHub
anugrahyayan67-collab/Buku (cabang kerja: kimia-kuantum-bab01). Penyusun membaca hasilnya
di iPad dan berbicara santai dalam bahasa Indonesia; jawab juga santai, tetapi isi buku
ditulis dalam bahasa Indonesia baku yang enak dibaca.

Sebelum apa pun:
1. Siapkan repo (clone bila belum ada) dan jalankan `python3 status.py` di akar repo.
2. Baca, berurutan: CLAUDE.md, PROMPT-AKUN-LAIN.md, PROMPT-BUKU.md, PANDUAN-BUKU.md,
   ANTREAN.md, lalu RENCANA.md dan PEDOMAN.md di folder buku yang akan dikerjakan.

Cara kerja:
- Bila penyusun memberi perintah jelas, kerjakan itu.
- Bila penyusun hanya bilang "lanjut", "gas", "kerjakan", atau tidak memberi perintah
  khusus, ambil butir ☐ pertama di ANTREAN.md dan kerjakan sampai tuntas tanpa menunggu
  izin per langkah. Setelah selesai, centang butirnya, commit, push, kirim PDF, laporkan
  singkat, lalu lanjut ke butir berikutnya selama kuota masih cukup.
- Bertanya hanya bila benar-benar tidak bisa diputuskan dari berkas di repo.
- Kerjakan sendiri tanpa subagen. Semua angka dihitung dengan Python dulu.
- Setiap selesai satu bab atau satu tahap: commit + push, kirim PDF lewat SendUserFile.
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
| Kimia Fisika 1: Termodinamika Kimia | `termodinamika-kimia/` | Edisi 1.2 sedang dituntaskan: 14 bab selesai, Bab 15 Termodinamika Permukaan belum; 428 halaman |
| Kimia Organik 1: Senyawa Monofungsi | `kimia-organik/` | 16 bab selesai; PDF belum disalin ke `pdf/` |
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

## 3. Mengambil keputusan tanpa perintah

Urutan prioritas ketika penyusun tidak memberi perintah khusus:

1. Perbaiki dulu hal yang rusak: build gagal, rujukan `??`, `{{kunci}}` yang tidak terganti, gambar terpotong.
2. Butir ☐ pertama di `ANTREAN.md`.
3. Bila antrean kosong: buku berikutnya di `RENCANA-SERI.md` yang statusnya ☐ (rancangan dulu, lalu bab demi bab), dan tambahkan butir-butirnya ke `ANTREAN.md`.

Aturan tambahan:
- **Satu sesi = satu bab baru** (paling banyak dua). Pekerjaan kecil (gambar, soal, cetak ulang, baca ulang) boleh beberapa dalam satu sesi.
- Bila ada keputusan isi yang tidak tercatat di repo (misalnya memilih urutan bab buku baru), ambil pilihan yang paling sesuai dengan buku acuan, catat alasannya di `RENCANA.md`, dan sebutkan di laporan. Jangan berhenti hanya untuk bertanya.
- Bertanya hanya bila: perintah penyusun bisa berarti dua buku/pekerjaan yang berbeda, atau tindakan tidak bisa dibatalkan (menghapus berkas besar, menimpa PDF akhir dengan versi yang lebih buruk).
- Setiap butir selesai: centang di `ANTREAN.md` (☑ + tanggal + hash commit), perbarui status di `RENCANA.md` buku itu dan `RENCANA-SERI.md`.

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
3. Butir antrean berikutnya.

Kirim PDF terbaru lewat SendUserFile setiap ada perubahan isi yang berarti.

## 8. Yang tidak diinginkan

- Menunggu izin untuk langkah yang sudah jelas dari antrean atau pedoman.
- Menulis buku/bab yang tidak ada di antrean atau rencana tanpa alasan.
- Penjelasan tipis, langkah diloncati, kalimat pengisi untuk menebalkan.
- Label tingkat soal, latihan ujian, proyek.
- Menyalin teks atau soal dari buku acuan.
- Angka yang tidak dihitung ulang.
- Data pribadi penyusun selain nama.

## 9. Memperbarui berkas ini

Bila ada aturan baru dari penyusun, alat baru, atau buku baru selesai, perbarui berkas ini, `ANTREAN.md`, dan tabel di bagian 1 pada commit yang sama.
