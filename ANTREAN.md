# Antrean kerja seri buku

Berkas ini adalah **daftar tugas berurutan**. Sesi Claude yang mendapat perintah umum ("lanjut", "gas", "kerjakan", atau tanpa perintah khusus) mengambil **butir ☐ pertama dari atas**, mengerjakannya sampai selesai, mencentangnya (☑ + tanggal + hash commit), lalu lanjut ke butir berikutnya selama kuota dan waktu sesi masih cukup. Butir yang dikerjakan sebagian ditandai ◐ dengan catatan di mana berhenti.

Penyusun boleh menambah, menghapus, atau mengubah urutan butir kapan saja. Perintah langsung dari penyusun selalu didahulukan dari antrean.

Status: ☐ belum · ◐ sebagian · ☑ selesai

## A. Kimia Fisika 1 (`termodinamika-kimia/`), menuntaskan Edisi 1.2

- ☐ **A1. Bab 15 Termodinamika Permukaan** (satu sesi penuh, Opus effort high). Subbab rencana: tegangan permukaan dan energi permukaan · persamaan Young–Laplace · kapilaritas dan sudut kontak · persamaan Kelvin dan nukleasi · persamaan adsorpsi Gibbs · surfaktan dan misel · isoterm adsorpsi (Langmuir, BET). Target dan susunan seperti Bab 14. Setelah selesai: pindahkan bagian "## Penutup: satu fungsi, banyak wajah" dari akhir `bab14/c-terapan.md` ke akhir Bab 15, ganti akhir Bab 14 dengan "### Menuju bab berikutnya", tambah entri pembuka 15 di `edisi/pembuka2.py`, dan tambahkan "Bab 15" di `RENCANA.md` (Bagian VI).
- ☐ **A2. Soal Bab 3, 6, 7, 8 dilengkapi sampai ± 80** (sekarang 77, 76, 78, 76). Pakai `alat/tebal.py` (`soal()`), semua jawaban dihitung dengan Python.
- ☐ **A3. Baca ulang kejelasan Bab 1–15**, satu bab per putaran: cari loncatan langkah, kalimat yang membingungkan, rujukan silang yang salah, istilah yang tidak konsisten. Perbaiki dengan kalimat penjelas pendek. Catat temuan dan perbaikan per bab di `termodinamika-kimia/REVISI.md` (bagian "Revisi 1.2"). Skill pedagogi (lihat `PROMPT-AKUN-LAIN.md` bagian 5) boleh dipakai untuk menilai beban kognitif dan bahasa.
- ☐ **A4. Cetak akhir**: `python3 termodinamika-kimia/edisi/cetak.py` dan `--cetak`, salin kedua PDF ke `pdf/`, perbarui `pdf/README.md` (jumlah halaman, revisi 1.2), kirim PDF digital ke penyusun.

## B. Kimia Organik 1 (`kimia-organik/`)

- ☐ **B1. Salin PDF Organik ke `pdf/`**: `kimia-organik/Kimia-Organik-1-Edisi-1.pdf` belum ada di `pdf/`. Cetak ulang bila perlu (`python3 kimia-organik/edisi/cetak.py`, juga `--cetak`), salin, perbarui `pdf/README.md` dan baris Organik di `RENCANA-SERI.md` menjadi ☑.
- ☐ **B2. Baca ulang kejelasan Bab 1–16** (sama seperti A3), catat di `kimia-organik/REVISI.md`.

## C. Buku berikutnya (urutan dari `RENCANA-SERI.md`)

- ☐ **C1. Persiapan TEP** (`persiapan-tep/`): Bab 1–4 (kosakata) dulu, ikuti `persiapan-tep/PEDOMAN.md`. Siapkan alat cetak dengan menyalin pola `kimia-organik/edisi/` (palet ungu di PEDOMAN).
- ☐ **C2. Matematika untuk Kimia**: buat folder, `RENCANA.md` (bandingkan acuan: misalnya Steiner *The Chemistry Maths Book*, Cockett–Doggett *Maths for Chemists*), `PEDOMAN.md`, alat cetak; lalu bab demi bab.
- ☐ **C3. Kimia Anorganik 1** dan **Kimia Analitik 1** (rancangan dulu, sesuai `RENCANA-SERI.md`).

## Selesai (riwayat singkat)

- ☑ Kimia Fisika 1: perbaikan total Edisi 1.2 tahap 1 (subbab 4.11, 8.9, 9.6, 9.7, 10.8, 11.9, 12.9, 13.9; Bab 14 Termodinamika Statistik; gambar tiap bab 7–9; soal Bab 9–14 ≥ 81), 21-11-2026, sampai commit `77cec33`.
- ☑ Kimia Organik 1 Bab 1–16 dan perombakan gambar, November 2026.
- ☑ Fisika Umum Edisi 1 dan Kimia Kuantum Edisi 1.
