# Prompt baku untuk sesi penulisan Kimia Kuantum

Salin teks di bawah ke sesi baru (model **Opus 5.5**, effort **high**; **xhigh** untuk Bab 9–16, 19, 20). Ganti `N` dengan nomor bab.

---

Tulis **Bab N** buku *Kimia Kuantum* di repo ini.

1. Baca `CLAUDE.md`, `kimia-kuantum/PEDOMAN.md`, dan `kimia-kuantum/RENCANA.md` (daftar subbab Bab N ada di sana). Untuk Bab 1, siapkan dulu alat cetak di `kimia-kuantum/` (lihat bagian *Penyiapan alat* di PEDOMAN.md).
2. Tulis materi lengkap Bab N di `kimia-kuantum/babNN/` (berkas `a-*.md`, `b-*.md`, ...) dengan semua subbab di RENCANA.md: penjelasan, penurunan langkah demi langkah, ≥ 40 contoh (Penyelesaian / Memahami hasil), kotak inti/dalam/awas/mat/terapan, satu kuis cepat tiap subbab.
3. Akhir bab: Ringkasan, ± 20 Pertanyaan, ≥ 80 Soal bertingkat per subbab beserta Jawaban, 6–10 Pembahasan, Bacaan lanjut.
4. Semua angka dihitung dengan Python dulu. Gambar dengan matplotlib (palet di CLAUDE.md).
5. Bangun PDF bab, periksa visual beberapa halaman (tidak ada MathML mentah, gambar tidak terpotong), lalu kirim PDF ke penyusun lewat SendUserFile.
6. Ubah status Bab N di RENCANA.md menjadi ☑, commit, dan dorong ke cabang kerja.

Target 50–60 halaman. Jangan menyalin teks atau soal dari buku acuan; tulis sendiri.
