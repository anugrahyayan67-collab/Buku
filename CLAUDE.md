# Pedoman kerja repo Buku

Repo ini berisi naskah buku sains berbahasa Indonesia untuk mahasiswa kimia, dibaca penyusun di iPad.

## Aturan tetap
- Bahasa buku: Indonesia baku tetapi enak dibaca. Bahasa percakapan dengan penyusun: santai.
- Kerjakan sendiri, **tanpa subagen** (hemat kuota).
- **Semua angka dihitung dengan Python dulu** sebelum ditulis. Koma desimal: `9{,}8` di LaTeX, `9,8` di teks.
- Tanpa `\cancel` dan `\tag` di LaTeX. Penomoran contoh/gambar/persamaan memakai label sementara lalu `alat/nomor.py`.
- Akhir bab: Ringkasan, Pertanyaan, Soal (dikelompokkan per subbab), Jawaban semua soal, Pembahasan soal terpilih. Tanpa proyek.
- Label contoh soal: **Gambaran fisis** (opsional), **Rencana** (opsional), **Penyelesaian**, **Memahami hasil**.
- Gambar: matplotlib, Liberation Sans, 220 dpi, palet biru tua `#0e2748`, biru `#1b75bc`, biru muda `#7fc0f0`, jingga `#f0a060`/`#b5541c`, hijau `#1a8a6a`; label sumbu memakai koma desimal.
- Hasil PDF dikirim ke penyusun lewat SendUserFile. PDF hasil akhir disimpan di folder `pdf/` (salin dari fisika-umum/ dan kimia-kuantum/ setelah cetak ulang); PDF lain tidak di-commit.
- Jangan memasukkan data pribadi penyusun selain nama (tanpa tanggal lahir, tanpa surel) ke berkas mana pun.

## Awal setiap sesi
Jalankan `python3 status.py`, lalu baca `PROMPT-AKUN-LAIN.md` (prompt induk: konteks, cara mengambil keputusan, alat, plugin) dan `ANTREAN.md`. Bila penyusun hanya bilang "lanjut" atau tidak memberi perintah khusus, kerjakan butir ☐ pertama di `ANTREAN.md` sampai tuntas, centang, commit, lalu lanjut.

## Panduan susunan dan desain
Semua buku mengikuti `PANDUAN-BUKU.md` (susunan bab, kotak, aturan penulisan, desain, alat cetak, langkah memulai buku baru) dan `PROMPT-BUKU.md` (standar kelengkapan dan gaya penjelasan yang diinginkan penyusun; wajib dibaca sebelum menulis atau merevisi).

## Model
Lihat `PEMETAAN-MODEL.md`. Ringkas: **isi ditulis dengan Opus 5.5 (effort high, xhigh untuk bab tersulit); pekerjaan mesin dengan Sonnet 5.5.** Fable dan Haiku tidak dipakai.

## Menyiapkan lingkungan (sesi baru)
Skrip Fisika Umum memakai jalur `~/fisika-umum`:
```bash
ln -sfn /home/user/buku/fisika-umum ~/fisika-umum
pip install reportlab pypdf matplotlib 2>/dev/null   # bila belum ada; pandoc dan Playwright sudah terpasang
```
- Bangun satu bab: `cd fisika-umum && ./build.sh babNN "Bab N"`
- Cetak buku utuh (versi digital, tanpa halaman kosong; gaya sama dengan Kimia Kuantum: edisi2/fu.css, pembuka2.py, sampul.py): `python3 fisika-umum/edisi2/cetak.py` (`--lewati-bab` bila isi bab tidak berubah, `--cetak` untuk versi cetak bolak-balik).
- Catatan teknis lengkap: `fisika-umum/CATATAN.md`.

## Kimia Kuantum
- Rencana bab dan subbab beserta status: `kimia-kuantum/RENCANA.md` (perbarui status setiap bab selesai).
- Pedoman isi, notasi, dan gaya: `kimia-kuantum/PEDOMAN.md`. Baca keduanya sebelum menulis.
- Satu sesi = satu bab (paling banyak dua). Materi dulu, desain belakangan.
- Commit setiap bab selesai, dorong ke cabang kerja, lalu perbarui RENCANA.md.
- Cetak buku utuh Edisi 1 (sampul, pembuka bab bergambar, daftar isi bertaut, indeks): `python3 kimia-kuantum/edisi/cetak.py` (`--lewati-bab` bila isi bab tidak berubah). Gambar pembuka (gaya terang, sesuai isi bab): `kimia-kuantum/edisi/pembuka2.py`; sampul: `edisi/sampul.py`; palet: `edisi/kk.css`.
