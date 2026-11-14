# Pedoman penulisan *Kimia Kuantum*

## Pembaca
Mahasiswa S1 kimia yang sudah membaca Fisika Umum (terutama Bab 8, 9, 14, 15) dan kalkulus dasar. Matematika yang lebih tinggi diajarkan di Bab 2 dan di tempat pertama kali dipakai.

## Prinsip isi
1. **Penurunan lengkap.** Setiap hasil penting diturunkan langkah demi langkah; langkah aljabar tidak dilompati. Penurunan panjang diletakkan di kotak `.dalam` ("Lebih dalam") supaya alur utama tetap terbaca.
2. **Selalu kembali ke kimia.** Setiap subbab ditutup dengan makna kimianya: spektrum, ikatan, reaktivitas, sifat periodik.
3. **Angka nyata.** Contoh memakai data molekul nyata (panjang ikatan, bilangan gelombang, energi ionisasi) dan dihitung dengan Python.
4. **Komputasi.** Sejak Bab 5, sebagian contoh menyertakan potongan Python singkat (NumPy) untuk penyelesaian numerik, diagonalisasi, dan grafik orbital.
5. **Orisinal.** Buku acuan dipakai untuk menentukan cakupan dan kedalaman. Teks, contoh, dan soal ditulis sendiri, tidak diterjemahkan atau disalin.

## Notasi baku
| Besaran | Lambang |
|---|---|
| Fungsi gelombang bergantung waktu / tak bergantung waktu | Ψ(x, t) / ψ(x) |
| Operator | huruf bertopi: Ĥ, p̂, L̂², Ŝ_z |
| Konjugat kompleks | ψ* |
| Nilai harap | ⟨A⟩ = ∫ ψ* Â ψ dτ |
| Notasi Dirac | dipakai sejak Bab 4.14 |
| Konstanta Planck tereduksi | ħ = h/2π |
| Massa tereduksi | μ |
| Satuan | SI di bagian awal; satuan atom (hartree, bohr) sejak Bab 7; bilangan gelombang dalam cm⁻¹ untuk spektroskopi |

Koma desimal di seluruh buku (`9{,}8`). Integral diberi batas dan elemen volume yang jelas (dτ, r² sin θ dr dθ dφ).

## Susunan setiap bab
1. Halaman pembuka (dibuat otomatis) dan paragraf pembuka berupa teka-teki kimia.
2. Pertanyaan pembuka, Tujuan belajar, Prasyarat (menunjuk bab Fisika Umum atau bab sebelumnya).
3. 10–15 subbab. Setiap subbab: penjelasan, penurunan, 2–5 contoh, kotak (`.inti`, `.dalam`, `.awas`, `.mat`, `.terapan`, `.strategi`), dan satu kuis cepat.
4. Akhir bab: Ringkasan (tabel rumus), Pertanyaan konsep (± 20), Soal per subbab (≥ 80, bertingkat: dasar, menengah, tantangan ★), Jawaban semua soal, Pembahasan soal terpilih (6–10).

## Label dan kotak
- Contoh: `Contoh N.n1 · Judul`, lalu **Gambaran fisis** (opsional), **Rencana** (opsional), **Penyelesaian**, **Memahami hasil**.
- Persamaan bernomor: `\text{(N.n1)}` di akhir baris; nomor final dibuat oleh `alat/nomor.py`.
- Gambar: `![Gambar N.n1 Keterangan.](fig/c_nama.png){width=…%}`.

## Pembagian kerja per sesi
Satu sesi = satu bab. Urutan: materi (Opus 5.5 · high) → gambar dan build (Sonnet 5.5 · medium) → pemeriksaan angka dan rujukan (Sonnet 5.5 · high) → commit, lalu perbarui status di `RENCANA.md`.

## Penyiapan alat (sekali, sebelum Bab 1)
Pakai ulang alat Fisika Umum:
1. Salin `fisika-umum/build.sh`, `gaya.py`, `topdf.cjs`, `buku.css`, `alat/` ke `kimia-kuantum/`.
2. Ganti judul di `build.sh` dan `topdf.cjs` menjadi "Kimia Kuantum"; ganti jalur `~/fisika-umum` di skrip `alat/` menjadi jalur `kimia-kuantum`.
3. Tambahkan `edisi2/buku3.css` dari Fisika Umum agar gaya isi sama (palet biru tua, kotak bersudut membulat, paragraf menjorok).
4. Uji dengan satu bab: `./build.sh bab01 "Bab 1"` harus menghasilkan PDF tanpa `class="math` di HTML.

Cetak buku utuh (sampul, daftar isi bertaut, indeks) dibuat setelah beberapa bab selesai, dengan menyesuaikan `fisika-umum/edisi2/cetak.py`.
