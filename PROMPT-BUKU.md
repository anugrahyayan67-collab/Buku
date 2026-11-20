# Prompt lengkap: menulis buku kuliah kimia seperti yang diinginkan penyusun

Salin seluruh isi berkas ini ke sesi baru (atau minta sesi membaca berkas ini) sebelum menulis atau merevisi buku apa pun di repo ini. Contoh pelaksanaan terbaik saat ini: `kimia-organik/` Bab 1–3.

---

## 1. Tugas

Tulis buku pegangan kuliah S1 Kimia berbahasa Indonesia untuk mata kuliah **[NAMA MATA KULIAH]**, judul **[JUDUL BUKU]**, di folder `[folder]/`. Buku ini bagian dari satu seri (lihat `RENCANA-SERI.md`) dan harus terlihat serupa dengan buku lain dalam seri: susunan bab, kotak, desain, dan alat cetak mengikuti `PANDUAN-BUKU.md`.

Pembaca: mahasiswa kimia yang membaca sendiri di iPad, tanpa dosen di sampingnya. Buku harus bisa dipahami **tanpa penjelasan tambahan dari luar**.

## 2. Ukuran kelengkapan (wajib)

Buku harus **selengkap buku teks standar internasional** untuk mata kuliah itu, bukan ringkasan.

1. **Cari dulu buku acuan** (misalnya Klein, Clayden, McMurry untuk organik; Atkins, Levine untuk kimia fisika; Harris, Skoog untuk analitik; Housecroft, Miessler untuk anorganik). Catat jumlah bab, jumlah halaman, dan topik setiap bab. Buku acuan hanya dipakai untuk **cakupan**; teks, contoh, dan soal ditulis sendiri.
2. **Gabungkan beberapa acuan.** Rancangan boleh mengikuti susunan satu buku luar yang baik, atau menggabungkan susunan terbaik dari dua–tiga buku (misalnya urutan McMurry, bab radikal dan sintesis dari Klein, pendekatan orbital dari Clayden), asalkan hasilnya urutan belajar yang paling masuk akal. Catat buku acuan dan alasan pembagian di bagian atas `RENCANA.md`. Bila sebuah topik di buku acuan sengaja dipindah ke buku lain dalam seri (misalnya ke *Organik 2*), tulis itu juga.
3. **Susun rancangan lengkap** di `[folder]/RENCANA.md`: semua bab dan **semua subbab** (biasanya 9–14 subbab per bab), disusun dalam Bagian. Bandingkan dengan daftar isi buku acuan; setiap topik yang ada di buku acuan harus ada tempatnya. Bila perlu tambahkan bab (misalnya spektroskopi dan strategi sintesis untuk organik), letakkan di akhir supaya nomor bab yang sudah dirujuk tidak bergeser. Periksa ulang rancangan terhadap acuan **sebelum setiap bab ditulis**, karena topik yang terlewat paling mudah ditambahkan sebelum babnya ada.
4. **Target per bab**: ± 35–50 halaman, ± 15–25 contoh, ± 80–100 soal, ± 20 pertanyaan konsep, 3–5 gambar, 6–11 pembahasan soal terpilih. Bab tata nama atau pengantar boleh sedikit lebih tipis, tetapi tidak boleh kurang dari ± 28 halaman.
5. **Jangan menebalkan dengan kalimat kosong.** Ketebalan datang dari topik yang lengkap, langkah yang tidak diloncati, contoh yang beragam, dan kalimat penjelas yang memang menolong.

## 3. Gaya penjelasan (inti keinginan penyusun)

1. **Kalimat penjelas sebanyak yang diperlukan.** Setiap langkah diberi alasan ("kita kalikan kedua ruas dengan *V* supaya *V* hilang dari penyebut"; "panah ini berpangkal pada pasangan bebas karena basa yang menyerang proton"). Pembaca tidak boleh harus menebak dari mana sebuah baris, rumus, atau aturan datang. Lebih baik satu kalimat terlalu banyak daripada satu loncatan.
2. **Mengapa sebelum bagaimana.** Setiap subbab dibuka dengan masalah atau pertanyaan nyata, lalu konsep diperkenalkan sebagai jawabannya.
3. **Paragraf mengalir.** Setiap paragraf menjawab satu pertanyaan dan memancing pertanyaan berikutnya ("Pertanyaan berikutnya muncul dengan sendirinya: …"). Kalimat transisi menyambungkan subbab.
4. **Gambaran sebelum rumus.** Setiap konsep diberi gambaran yang bisa dibayangkan (molekul, grafik, perumpamaan sehari-hari) sebelum didefinisikan.
5. **Hubungkan ke depan dan ke belakang.** Sebut di mana konsep ini akan dipakai lagi ("Bab 7 memakai gagasan ini untuk …") dan dari mana asalnya ("subbab 1.8"). Rujuk buku lain dalam seri bila relevan (*Kimia Kuantum*, *Termodinamika Kimia*).
6. **Kesalahan umum ditunjukkan** dalam kotak `.awas`: kesalahan yang benar-benar sering dibuat mahasiswa, beserta cara menghindarinya.
7. **Aturan dan pengecualian.** Bila ada aturan praktis (misalnya ARIO), tunjukkan juga kapan aturan itu gagal dan apa yang menjadi hakim terakhir (data).
8. **Bahasa**: Indonesia baku tetapi enak dibaca, sapaan "kamu" dan "kita" (jangan "Anda"). Istilah baku seri: getaran, pendekatan, asas, rapat peluang, dsb. Ejaan baku (miliar, bukan milyar).
9. **Kimia nyata.** Contoh dari obat, bahan alam, industri, laboratorium, lingkungan, tubuh manusia. Kotak `.terapan` untuk kaitan ini.

## 4. Susunan setiap bab

1. Judul `# Bab N Judul`.
2. **Paragraf pembuka berupa teka-teki** (fenomena nyata yang membingungkan), lalu gagasan pokok bab, lalu peta isi bab, lalu mengapa bab ini penting.
3. Kotak **Pertanyaan pembuka** (`.kuis`, 5–6 pertanyaan), **Tujuan belajar** (`.tujuan`, 7–9 butir "Setelah mempelajari bab ini, kamu mampu: …"), **Prasyarat** (`.mat`, menunjuk bab/subbab dan buku lain).
4. Subbab `## N.k Judul`, sub-subbab `### Judul`. Setiap subbab berisi: penjelasan "mengapa", penurunan atau aturan langkah demi langkah, tabel data bila berguna, 1–3 contoh, kotak yang sesuai, dan **satu kuis cepat** di akhir.
5. Kotak **Strategi** (`.strategi`) berisi langkah-langkah bernomor untuk jenis soal yang sering muncul (menamai, menggambar struktur Lewis, membandingkan keasaman, merancang ekstraksi, dsb.).
6. Kotak **Inti** (`.inti`) untuk hasil terpenting.
7. Paragraf penutup **"Menuju bab berikutnya"**: menjawab teka-teki pembuka, meringkas alat yang sudah dibangun, dan menjembatani ke bab berikutnya.
8. **Akhir bab** (`_akhir.md` + `_soal.txt`, disusun oleh `alat/soal.py`):
   - Ringkasan berupa tabel (gagasan · isi pokok/rumus · subbab), lalu **Jawaban kuis cepat** semua subbab.
   - **Pertanyaan** konsep, dikelompokkan per subbab dengan judul `## Subbab N.k: Judul`.
   - **Soal** dikelompokkan per subbab, **tanpa label tingkat** (tanpa Dasar/Menengah/Tantangan/★). Satu catatan data di awal (blockquote). Soal yang dibahas diberi `@nama [P]`.
   - **Jawaban** semua soal.
   - **Pembahasan soal terpilih**: penyelesaian lengkap, lalu paragraf *Cara berpikir:* yang menjelaskan pola pikirnya dan kaitannya dengan topik lain.
   - **Bacaan lanjut** (≤ 6 judul, dengan satu kalimat keterangan).

## 5. Contoh soal

- Label: `**Contoh N.xK · Judul**` (label sementara, dinomori `alat/nomor.py`).
- Bagian: **Gambaran fisis.** (opsional) · **Rencana.** (opsional, untuk contoh panjang) · **Penyelesaian.** · **Memahami hasil.**
- *Penyelesaian* menulis setiap langkah dengan satuan. *Memahami hasil* tidak mengulang jawaban, tetapi menjelaskan **artinya**: apakah masuk akal, apa akibatnya, di mana dipakai lagi.
- Contoh beragam: hitungan, perbandingan/pengurutan, menggambar mekanisme, merancang prosedur, membaca data.

## 6. Angka, rumus, dan data

- **Semua angka dihitung dengan Python dulu** sebelum ditulis (Ka, Keq, ΔG°, persen, hasil, konversi). Data literatur (titik didih, pKa, momen dipol) dipakai dari sumber standar dan konsisten di seluruh buku.
- Koma desimal: `9{,}8` di LaTeX, `9,8` di teks. Satuan dibawa di setiap langkah.
- LaTeX tanpa `\cancel` dan `\tag`. Persamaan bernomor `\text{(N.eK)}`, gambar `![Gambar N.gK …](fig/x.png){width=..%}`, keduanya dinomori `alat/nomor.py`.
- Periksa ulang setiap jawaban soal dengan Python atau dengan menurunkannya kembali.

## 7. Gambar

- matplotlib (dan RDKit untuk struktur molekul), Liberation Sans, 220 dpi, palet seri: biru tua `#0e2748`, biru `#1b75bc`, biru muda `#7fc0f0`, jingga `#f0a060`/`#b5541c`, hijau `#1a8a6a`; label sumbu dengan koma desimal. Skrip di `[folder]/alat/gambar/babNN.py`.
- Setiap gambar harus menjelaskan sesuatu yang sulit dijelaskan dengan kata (diagram energi, kurva, skema prosedur, bentuk tiga dimensi), bukan hiasan. Keterangan gambar menjelaskan apa yang harus dilihat.
- Periksa setiap gambar secara visual (tumpang tindih teks, label terpotong) sebelum dipakai.
- Gambar pembuka bab (gaya terang, sesuai teka-teki bab) ditambahkan di `edisi/pembuka2.py`.

## 8. Daftar periksa "bab sudah lengkap"

Sebelum menyatakan sebuah bab selesai, periksa:

1. Semua subbab di `RENCANA.md` ada, dan setiap topik buku acuan untuk bab itu tercakup.
2. Teka-teki pembuka terjawab di "Menuju bab berikutnya".
3. Jumlah: halaman, contoh, soal, gambar, pertanyaan sesuai target bagian 2.
4. Setiap subbab mempunyai kuis cepat dan jawabannya ada di Ringkasan.
5. Tidak ada loncatan langkah: baca ulang setiap penurunan dan tanyakan "dari mana baris ini?".
6. Bagian yang sering membingungkan sudah diberi kotak `.awas` atau kalimat penjelas tambahan.
7. Semua rujukan silang (subbab, contoh, gambar, bab lain, buku lain) benar.
8. Semua angka sudah dicek dengan Python.
9. PDF dicetak dan diperiksa visual (pembuka bab, tabel, gambar, dua kolom soal).

Contoh pelengkapan yang pernah diminta penyusun (Kimia Organik Bab 1–2): menambah orbital atom dan elektron valensi, pasangan bebas tersirat dalam rumus garis, teori orbital molekul (ikatan/antiikatan, orde ikatan, HOMO/LUMO), lima pola resonansi, pasangan bebas terlokalisasi/terdelokalisasi, cara mencari isomer secara sistematis, senyawa bisiklik, amina N-tersubstitusi, turunan asam, gugus fungsi pada cincin, dan subbab turunan benzena. Pola ini berlaku untuk semua buku: bandingkan dengan buku acuan, lalu tambahkan topik yang belum ada.

## 9. Alur kerja

1. Baca `CLAUDE.md`, `PANDUAN-BUKU.md`, berkas ini, `[folder]/RENCANA.md`, dan `[folder]/PEDOMAN.md`.
2. Satu sesi = satu bab (paling banyak dua). Materi dulu, desain belakangan.
3. Hitung angka → tulis `a-*.md`, `b-*.md`, `c-*.md` → gambar → `_soal.txt` dan `_akhir.md` → `python3 alat/nomor.py babNN N` → `python3 alat/soal.py babNN` → tambah istilah ke `edisi/indeks_tambah.txt` → cetak `python3 [folder]/edisi/cetak.py` → periksa visual.
4. Tandai bab ☑ di `RENCANA.md` dan perbarui `RENCANA-SERI.md`.
5. Commit, dorong ke cabang kerja, kirim PDF ke penyusun lewat SendUserFile. PDF hasil akhir buku utuh disimpan di `pdf/`; PDF lain tidak di-commit.
6. Kerjakan sendiri tanpa subagen. Hemat token: jangan membaca ulang berkas besar tanpa perlu, jangan menebak buku mana yang diminta (tanyakan bila ragu), dan jangan menulis buku yang tidak diminta.

## 10. Yang tidak diinginkan

- Penjelasan tipis yang hanya memberi rumus dan definisi tanpa alasan.
- Langkah aljabar atau mekanisme yang diloncati.
- Teks tebal yang ditebalkan dengan kalimat yang tidak menambah pemahaman.
- Label tingkat kesulitan pada soal; latihan ujian; proyek.
- Data pribadi penyusun selain nama.
- Menyalin teks atau soal dari buku acuan.
