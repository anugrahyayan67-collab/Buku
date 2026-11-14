# Catatan kerja buku Fisika Umum (15 bab, tebal ~50-65 hlm/bab)

Selesai: Bab 1-3 (rakitan dari ~/fisika-dasar lewat rakit.py), Bab 4, 5, 6, 7, 8, 9, 10 (54 hlm), 11 (43 hlm), 12 (40 hlm), 13 (41), 14 (41), 15 (40) — BUKU SELESAI.
Berikut: 10 Suhu-kalor-teori kinetik, 11 Termodinamika,
12 Listrik statis, 13 Listrik dinamis, 14 Kemagnetan & induksi, 15 Fisika modern.

Pola per bab (babNN/):
- fig/gambar.py -> PNG (matplotlib, warna B=#1b75bc T=#17355e H=#b5541c W=#cfe3f5)
- a-*.md, b-*.md : materi. Label sementara bebas: "Contoh N.x1", "Gambar N.g1", "\text{(N.e1)}";
  alat/nomor.py babNN N menomori ulang semuanya (termasuk rujukan).
- _soal.txt : "## judul", "> pengantar", soal "teks ||| jawaban", kunci "@nama " di depan; [P] = dibahas.
- _akhir.md : ringkasan, jawaban kuis, pertanyaan, %%SOAL%%, %%JAWABAN%%, pembahasan ({{nama}} = nomor soal).
- alat/soal.py babNN -> c-akhir.md ; alat/sisip.py babNN menyisipkan _tambahan.txt ("@@ berkas | penanda").
- ./build.sh babNN "Bab N Judul" ; ./gabung.sh ; salin PDF ke /home/user/fisika-umum/ ; kirim.
Isi tiap bab: pembuka + pertanyaan, tujuan, prasyarat, 8-10 subbab, ~50 contoh (Kerjakan/Periksa),
kuis cepat tiap subbab, kotak awas/strategi/mat/terapan (kaitan kimia), ringkasan, ~20 pertanyaan,
~100 soal + jawaban, 4-6 pembahasan. Tanpa proyek. Semua angka dihitung Python dulu.

Catatan teknis:
- Tulis materi langsung tebal (target 45+ contoh, 95+ soal); kalau <45 hlm, tambah lewat _tambahan.txt.
- Di _tambahan.txt, rujukan ke rumus/contoh yang SUDAH dinomori pakai nomor akhirnya (bukan label lama).
- Rujukan lintas bab ditulis "Contoh 4.18 di Bab 4" -> cek nomor aslinya dengan grep dulu.
- Halaman: Bab4 63, Bab5 54, Bab6 48, Bab7 48, Bab8 46, Bab9 43.

## Edisi 2 (14 Nov 2026)
- Bab 1–3 disatukan dengan alat/satukan.py (sumber lama di _ed1/): tanpa Bagian A/B, tanpa Proyek, akhir bab = Ringkasan, Pertanyaan, Soal (bersambung), Jawaban, Pembahasan. Gambar Bab 1–3 diwarnai ulang (palet biru).
- Cetak buku utuh: `python3 edisi2/cetak.py` (atau `--lewati-bab` bila isi bab tidak berubah). Hasil: Fisika-Umum-Edisi-2.pdf (757 hlm, 15 MB).
  Isi: sampul (edisi2/sampul.py), judul, keterangan, isi ringkas, daftar isi bernomor, depan.md, 15 bab (mulai halaman ganjil), lampiran.md (A, B), indeks otomatis (indeks_tambah.txt, indeks_buang.txt), bookmark.
  Judul berjalan dibuat reportlab (Helvetica) dan ditumpuk sebagai stream tambahan (jangan merge_page: file membengkak).
- File kirim lama dipindah ke /home/user/fisika-umum/edisi-1/.

## Edisi 3 (14 Nov 2026)
- Pendalaman lewat subbab baru di akhir bab (nomor lama tidak bergeser): alat/tambah.py (Bab 4–15) atau alat/tambah13.py (Bab 1–3), lalu nomor.py, soal.py, build.sh. Kotak baru `.dalam` ("Lebih dalam").
- Tambahan: 3.4 kotak dp/dt + 3.15–3.16; 5.10–5.12; 6.10–6.11; 7.10–7.11; 8.11–8.12; 9.11–9.13; 11.11–11.12; 12.10–12.11; 13.10–13.11; 14.11 (AC/RLC) + 14.12 (NMR); 15.10 (kotak, penerobosan), 15.11 (ikatan kuantum, efek isotop), 15.12 (inti, radioaktivitas).
- Halaman bab: 67 70 63 63 67 52 54 53 53 54 50 46 45 51 50.
- Sampul baru (edisi2/sampul.py; versi lama di _kerja/sampul-ed2.py): awan elektron orbital 3d_z2, tanpa angka statistik di depan/belakang/halaman judul.
- Hasil: Fisika-Umum-Edisi-3.pdf (851 hlm, 19,6 MB, 765 contoh). Edisi 2 dipindah ke /home/user/fisika-umum/edisi-2/.

## Edisi 4 (14 Nov 2026)
- Gaya isi baru selaras sampul: edisi2/buku3.css (semua), edisi2/pembuka.css (khusus bab: @page:first margin 0).
- Halaman pembuka bab penuh: gambar orbital hidrogen tiap bab (edisi2/pembuka.py -> _kerja/pembuka/orbNN.png; 1s ... 5f). Fungsi pembuka() di cetak.py mengganti h1.bab.
- Label contoh diganti di sumber: Penyelesaian, Memahami hasil, Rencana, Gambaran fisis, Memahami soal.
- Hasil: Fisika-Umum-Edisi-4.pdf (871 hlm).
- Revisi Edisi 4: nomor halaman kotak membulat biru tua angka putih; Isi Ringkas bergaya Daftar Isi (huruf ringan); Tujuan/inti berlatar biru muda; tipografi padat gaya buku internasional (10 pt, baris 1,4, paragraf menjorok, margin 22/18/19/18 mm di render.cjs). Hasil 763 hlm.
- Nama penyusun: Septian Anugrah Dwi Putra (sampul depan, halaman judul, keterangan, tanda tangan Kata Pengantar, "Tentang Penyusun" di sampul belakang). Tanpa tanggal lahir.
- Versi digital (default) tanpa halaman kosong; `python3 edisi2/cetak.py --cetak` untuk versi cetak bolak-balik. Hasil digital 749 hlm.
- Rencana edisi berikutnya: pendalaman isi (diskusi besok).
- Daftar isi, isi ringkas, dan indeks bertaut (href https://hal/a|r/N diubah jadi GoTo di cetak.py).
- Judul subbab, judul pembuka bab, dan pita Ringkasan/Soal/Jawaban bertaut kembali ke halaman Daftar Isi bab itu (href https://hal/d/N).
