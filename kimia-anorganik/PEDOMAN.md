# Pedoman penulisan *Kimia Anorganik 1: Teori Dasar*

Ikuti `../PANDUAN-BUKU.md`, `../PROMPT-BUKU.md`, dan `../DESAIN-BUKU.md`. Hal khusus buku ini:

## Pembaca
Mahasiswa semester 2 yang sudah mengikuti Kimia Dasar, Fisika Umum, dan Kimia Kuantum, serta sedang atau sudah mengikuti Termodinamika Kimia. Mekanika kuantum **tidak diturunkan ulang**: hasilnya dipakai dengan rujukan bab dan subbab *Kimia Kuantum* (misalnya "subbab 6.4 *Kimia Kuantum*").

## Gaya
1. **Data dulu, teori kemudian.** Setiap tren (jari-jari, energi ionisasi, pKa, potensial) dibuka dengan tabel atau grafik data nyata, lalu dijelaskan dengan model. Pembaca harus melihat polanya sebelum diberi penjelasannya.
2. **Model dan batasnya.** Setiap model sederhana (VSEPR, rasio jari-jari, aturan Pauling, HSAB, 18 elektron) ditunjukkan juga kapan gagal, dan data menjadi hakim terakhir (kotak `.awas`).
3. **Gambaran tiga dimensi.** Struktur kristal, bentuk molekul, dan operasi simetri digambar dari beberapa sudut.
4. **Kimia nyata.** Contoh dari mineral, industri (Haber–Bosch, proses kontak, ekstraksi logam), material (semikonduktor, baterai litium, katalis zeolit), lingkungan, dan biologi (hemoglobin, klorofil, sisplatin).
5. **Kalimat penjelas sebanyak yang diperlukan**, tanpa langkah yang dilompati.

## Notasi
- Koma desimal. Energi dalam kJ mol⁻¹; energi orbital dan ionisasi juga dalam eV bila berasal dari spektroskopi.
- Jari-jari ion Shannon (dengan bilangan koordinasi), dalam pm.
- Bilangan oksidasi dengan angka Romawi: Fe(III), [Fe(CN)₆]³⁻.
- Grup titik huruf miring dengan subskrip: *C*₂ᵥ, *D*₃ₕ, *T*_d, *O*_h; label simetri huruf kecil untuk orbital (a₁, t₂g), huruf besar untuk keadaan.
- Potensial standar *E*° dalam V terhadap SHE, pada 298 K.

## Gambar
matplotlib (dan RDKit bila perlu), palet gambar seri (`CLAUDE.md`). Struktur kristal dan molekul tiga dimensi dengan proyeksi sederhana di matplotlib. Skrip di `alat/gambar/babNN.py`, PNG di `babNN/fig/`.

## Desain
Gaya Edisi seri (`edisi/`), palet sendiri **tembaga–biru kobalt** (kesan logam dan mineral; dipilih penyusun 25-11-2026): tua `#4a2511`, utama `#c2611f`, muda `#f6c79b`, aksen biru kobalt `#2f5fb5` (terang `#6f93e0`).py`.

## Urutan kerja
Bab 1 → 13 berurutan (Bab 3–4 memakai Bab 2; Bab 6 memakai Bab 5; Bab 9 memakai Bab 8). Satu sesi satu bab.
