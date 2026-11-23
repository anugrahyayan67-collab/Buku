# Rancangan perbaikan total *Termodinamika Kimia* Edisi 1 → Edisi 1.1

Disusun setelah seluruh 13 bab selesai. Rancangan ini **berdasarkan pemeriksaan nyata**, bukan perkiraan:

- skrip pemeriksa otomatis `alat/periksa.py` (rujukan silang, kelengkapan, ejaan, sapaan, statistik isi);
- pembacaan ulang beberapa bagian inti (3.1–3.3, 1.7, 5.6);
- pemeriksaan bagian depan, indeks, dan sampul;
- uji ulang beberapa jawaban soal dengan Python.

Jalankan `python3 alat/periksa.py N` di awal dan akhir setiap sesi revisi.

## 1. Temuan

### 1.1 Kesalahan yang harus diperbaiki (wajib)

| No | Letak | Masalah | Perbaikan |
|---|---|---|---|
| K1 | `edisi/depan.md`, "Penomoran dan satuan" | Sisa teks Kimia Kuantum: "Sejak Bab 7 … satuan atom (hartree, bohr) … spektroskopi …". Salah untuk buku ini. | Tulis ulang: satuan SI, *p*° = 1 bar, konvensi tanda IUPAC, koma desimal. |
| K2 | `edisi/depan.md`, tabel kotak | Tabel menyebut "Kaitan kimia", padahal buku memakai kotak **Terapan**. Kotak **Pertanyaan pembuka**, **Tujuan belajar**, dan **Prasyarat** tidak dijelaskan. | Samakan tabel dengan kotak yang benar-benar dipakai. |
| K3 | Indeks (hlm. 313–316) | Indeks rusak. Kata biasa ikut masuk ("apakah", "asalkan", "awal", "bebas", "efisiensinya", "ditambah"). Istilah inti hilang atau tidak lengkap (entalpi, entropi, energi Gibbs, potensial kimia, fugasitas, aktivitas, …). Hanya ±3 halaman. | Susun ulang `indeks_tambah.txt` dan `indeks_buang.txt` dengan daftar istilah pilihan (±250 istilah), lalu periksa halaman setiap istilah. |
| K4 | Bab 6 → Bab 7 | Janji di 6.1: "Bab 7 akan menunjukkan $dS = (C_V/T)dT + (\partial p/\partial T)_V dV$". Bab 7 memuat hubungan Maxwell, tetapi rumus *dS* umum ini tidak pernah ditulis eksplisit. | Tambahkan di 7.6 satu paragraf + rumus *dS*(*T*, *V*) dan *dS*(*T*, *p*), dengan rujukan balik ke 6.1. |
| K5 | Bab 9 → Bab 12 | Janji di 9.5: "Bab 12 akan memakai fugasitas" untuk amonia bertekanan tinggi. Di Bab 12 fugasitas hanya muncul di satu soal tantangan dan satu kalimat. | Tambahkan satu contoh singkat di 12.8: *K*_φ dan pengaruhnya pada hasil amonia 300 bar. |
| K6 | Bab 1 (3×) | Ejaan tidak baku "milyar/milyaran". | Ganti menjadi "miliar/miliaran". |
| K7 | Bab 4, Bab 7 | Sapaan campur: "Anda" (3×), padahal di bagian lain buku memakai "kita" dan "kamu". | Samakan menjadi "kamu"/"kita". |

### 1.2 Bagian yang kurang jelas (contoh nyata dari pembacaan)

Inilah jenis "loncatan" yang membuat pikiran pembaca tidak terarah. Setiap temuan sejenis diperbaiki dengan satu atau dua **kalimat penjelas**, bukan dengan paragraf tambahan yang panjang.

| Letak | Yang membingungkan | Kalimat penjelas yang perlu ditambahkan |
|---|---|---|
| 3.3, paragraf pertama | Angka 1,24 bar dan 1,65 bar muncul tanpa asal. Pembaca tidak tahu bahwa itu tekanan gas pada 20 L dan 15 L. Tekanan awal (2,48 bar) juga tidak disebut. | "Tekanan awal gas 2,48 bar; pada 15 L dan 20 L tekanannya 1,65 dan 1,24 bar (dari *pV* = *nRT*)." |
| 3.3, proses reversibel | Definisi abstrak ("perubahan sekecil apa pun …") tanpa gambaran yang bisa dibayangkan. | Gambaran fisis: piston dibebani tumpukan pasir, lalu butir pasir diambil satu per satu. |
| 1.7, penurunan tekanan | Molekul dianggap memantul bolak-balik tanpa menumbuk molekul lain. Mahasiswa yang teliti akan bertanya mengapa itu boleh. | Satu kalimat: tumbukan antarmolekul hanya menukar momentum di antara molekul, sehingga rata-rata yang sampai ke dinding tidak berubah. |
| 1.7, setelah (1.15) | "Nol mutlak adalah keadaan ketika gerak translasi berhenti" (gambaran klasik). | Catatan singkat bahwa mekanika kuantum menyisakan energi titik nol (rujuk *Kimia Kuantum*). |
| 5.6, persamaan (5.6) | Tidak disebut bahwa kedua tahap adiabatik menyumbang nol karena *q* = 0. Pembaca bisa bingung mengapa hanya dua suku. | Satu kalimat eksplisit tentang tahap adiabatik. |
| 5.6, argumen Clausius | Siklus sembarang "dipecah menjadi siklus Carnot kecil" hanya dengan kata-kata. Ini sulit dibayangkan. | Satu **gambar** baru (siklus dipetak oleh isoterm dan adiabat), bukan kalimat tambahan. |

Bagian lain belum dibaca kalimat demi kalimat. Itulah pekerjaan utama revisi (lihat rubrik di bagian 3).

### 1.3 Ketimpangan isi antarbab (hasil `periksa.py`)

| Bab | Kata | Contoh | Soal (★) | Gambar | Kotak inti / dalam / terapan / awas |
|---|---|---|---|---|---|
| 1 | 5672 | 16 | 55 (7) | 1 | 6/0/1/2 |
| 2 | 5475 | 12 | 48 (7) | 3 | 2/1/0/0 |
| 3 | 4878 | 14 | 43 (4) | 2 | 4/0/0/1 |
| 4 | 4707 | 18 | 43 (2) | 2 | 4/0/0/0 |
| 5 | 6065 | 18 | 53 (5) | 2 | 7/2/1/1 |
| 6 | 5196 | 20 | 45 (1) | 1 | 5/2/1/1 |
| 7 | 5267 | 19 | 46 (2) | 1 | 8/1/1/0 |
| 8 | 7100 | 19 | 45 (2) | 3 | 4/1/3/2 |
| 9 | 5955 | 15 | 42 (4) | 3 | 8/3/2/1 |
| 10 | 6443 | 16 | 42 (3) | 3 | 7/1/3/1 |
| 11 | 6574 | 17 | 41 (2) | 6 | 5/0/5/0 |
| 12 | 4961 | 17 | 38 (2) | 3 | 4/1/1/2 |
| 13 | 4493 | 16 | 37 (3) | 3 | 4/0/1/0 |

Cara membaca tabel ini dengan benar:

- **Jumlah kata dan halaman bukan masalah.** Semua bab sudah lengkap menurut RPS. Target lama "35–40 halaman, ≥ 25 contoh, ≥ 60 soal" di `RENCANA.md` dihapus, karena mengejarnya hanya akan menghasilkan contoh dan soal yang mengulang tipe yang sama.
- **Yang benar-benar timpang:**
  - Bab 2–4 hampir tanpa kotak **Terapan** dan **Awas**, padahal di situlah salah paham mahasiswa paling sering terjadi (tanda kerja, Δ*H* vs Δ*U*, isotermal vs adiabatik).
  - Bab 1, 6, 7 hanya punya satu gambar.
  - Soal tantangan ★ sangat sedikit di Bab 4 dan 6–13. Soal tantangan inilah yang melatih penalaran untuk UTS/UAS.
- **Yang sudah cukup** (tidak ditambah): jumlah contoh di semua bab, kuis (setiap subbab sudah punya), dan "Memahami hasil" (semua contoh sudah punya).

### 1.4 Yang sudah benar (tidak diubah)

- Semua rujukan silang Contoh/Gambar/Tabel/subbab/persamaan valid (cek otomatis).
- Uji ulang acak terhadap jawaban soal Bab 2 dan 4 cocok.
- Urutan bab sesuai RPS.

## 2. Prinsip perbaikan: tidak asal menebalkan

Sesuatu **ditambahkan** hanya bila memenuhi salah satu dari lima alasan berikut:

1. Ada **loncatan penalaran**: langkah penurunan atau asal angka tidak dijelaskan. Tambahkan 1–2 kalimat penjelas.
2. Ada **konsep yang dipakai sebelum dijelaskan**, atau janji ke bab lain yang tidak ditepati.
3. Ada **salah paham umum mahasiswa** yang belum diantisipasi. Tambahkan kotak Awas.
4. Ada **tipe soal RPS/ujian** yang belum pernah dicontohkan. Tambahkan satu contoh, bukan tiga.
5. Ada gagasan yang **jauh lebih mudah dilihat daripada dibaca**. Tambahkan gambar.

Sesuatu **dikurangi atau dipadatkan** bila:

- mengulang hal yang sama dengan kata lain;
- contoh hanya mengganti angka dari contoh sebelumnya;
- paragraf tidak menjawab pertanyaan apa pun.

Yang **tidak** dilakukan:

- menambah halaman demi target;
- memindah urutan bab (sudah sesuai RPS);
- menulis ulang bagian yang sudah jelas hanya demi gaya.

## 3. Rubrik baca kritis (dipakai di setiap subbab)

Pembaca revisi membaca setiap subbab sambil menjawab sembilan pertanyaan berikut. Setiap jawaban "tidak" = satu perbaikan.

1. Apakah setiap lambang **didefinisikan** saat pertama muncul, beserta satuannya?
2. Apakah setiap angka dalam teks dan contoh **jelas asalnya** (data, hitungan sebelumnya, atau tabel)?
3. Apakah setiap langkah penurunan disertai **alasan** ("karena …", "dengan memakai …"), bukan hanya urutan rumus?
4. Apakah **anggapan** setiap rumus disebut (gas ideal, *T* tetap, reversibel, larutan encer, Δ*H* tetap)?
5. Apakah ada **gambaran fisis atau molekul** sebelum rumus abstrak?
6. Apakah paragraf berikutnya **menyambung** dari pertanyaan yang ditinggalkan paragraf sebelumnya?
7. Apakah istilah baru dicetak tebal **sekali**, di tempat ia didefinisikan?
8. Apakah ada kalimat yang **terlalu padat** (lebih dari dua gagasan)? Pecah.
9. Apakah "Memahami hasil" benar-benar **menambah pemahaman**, bukan mengulang jawaban?

## 4. Jenis pekerjaan dan peta model

Revisi ini hanya memakai **Opus 5.5**, dengan effort disesuaikan jenis pekerjaannya. Tanpa subagen.

| Kode | Pekerjaan | Model · effort | Alasan |
|---|---|---|---|
| P1 | Baca kritis memakai rubrik bagian 3; menulis kalimat penjelas; memecah kalimat padat | **Opus · high** | Butuh pemahaman konsep dan kepekaan bahasa; kesalahan di sini menyesatkan pembaca. |
| P2 | Menambah isi yang lolos prinsip bagian 2: paragraf konsep, penurunan, contoh baru, kotak Awas/Terapan, menepati janji K4–K5 | **Opus · high** | Menulis materi ilmiah baru. |
| P3 | Soal tantangan ★ baru dan pembahasannya | **Opus · high** | Soal yang baik butuh penalaran; jawabannya tetap dihitung dengan Python. |
| P4 | Verifikasi ulang **semua** angka contoh dan jawaban soal satu bab dengan Python; catat dan perbaiki yang salah | **Opus · medium** | Pekerjaan teliti tetapi mekanis. |
| P5 | Perbaikan cepat global: K1, K2, K6, K7, ejaan, sapaan, notasi (*V*_m, *p*°, tanda kerja), konsistensi istilah | **Opus · medium** | Mekanis, mudah diperiksa. |
| P6 | Gambar baru dan perbaikan gambar (matplotlib, palet, koma desimal) | **Opus · medium** | Teknis. |
| P7 | Indeks (K3) dan Lampiran B (lihat bagian 5) | **Opus · medium** | Penyusunan daftar dan tabel dari data yang sudah ada. |
| P8 | Desain: gambar pembuka bab 1–13 dirapikan, sampul belakang dicek, tampilan kotak | **Opus · medium** | Desain dan kode. |
| P9 | Cetak buku, periksa halaman PDF secara visual, `periksa.py`, commit dan push | **Opus · medium** | Rutin. |

Alur satu sesi (dua bab per sesi):

1. **Opus high**:
   - jalankan `periksa.py`;
   - baca kritis memakai rubrik (P1);
   - tambah isi yang memang perlu (P2) dan soal tantangan (P3).
2. **Opus medium**:
   - verifikasi angka (P4);
   - gambar (P6);
   - cetak, periksa, commit (P9).

## 5. Rencana per bab

Kolom "jangan" sengaja diisi supaya tidak terjadi penebalan asal.

| Bab | Perbaikan yang perlu (P1–P3, P6) | Jangan |
|---|---|---|
| 1 | Kejelasan 1.7 (tumbukan antarmolekul, energi titik nol). Gambar molekul memantul di dinding (1.7). Ejaan K6. | Jangan tambah contoh. Isi bab ini sebagian besar ulangan *Fisika Umum* Bab 10, cukup dipertajam ke sudut kimia. |
| 2 | Kotak Terapan: tabung elpiji, yaitu tekanan uap propana/butana dan kenapa isinya cair (Bab 2 ↔ Bab 8). Kotak Awas: *Z* < 1 tidak berarti molekul "lebih kecil". Cek kejelasan konstruksi Maxwell. | Jangan tambah persamaan keadaan baru. |
| 3 | Kejelasan 3.3 (asal tekanan, gambaran pasir). Kotak Awas: tanda *w* dan *q* dalam soal cerita. Kotak Terapan: pompa sepeda panas dan penyalaan mesin diesel (adiabatik). 2 soal ★. | Jangan tambah contoh kerja isotermal lagi (sudah 3 cara). |
| 4 | Kotak Awas: Δ*H* vs Δ*U* (kapan Δ*n*_gas*RT* penting). Kotak Lebih dalam: siklus Born–Haber dan entalpi kisi (tipe soal Kimia Dasar/UTS yang belum ada). Gambar kalorimeter bom. 3 soal ★. | Jangan tambah contoh hukum Hess sederhana lagi. |
| 5 | Kalimat tahap adiabatik di 5.6. Gambar argumen Clausius (siklus dipetak). | — |
| 6 | Satu gambar (Δ_mix*S* terhadap fraksi mol, atau *S*° tren molekul). 3 soal ★. | — |
| 7 | Tepati K4: *dS*(*T*,*V*) dan *dS*(*T*,*p*) di 7.6. Satu contoh di 7.1 (Δ*S*_total dan Δ*G* untuk reaksi yang sama, menunjukkan keduanya sepakat). Gambar "kotak termodinamika" sebagai alat ingat hubungan Maxwell. Sapaan K7. 2 soal ★. | — |
| 8 | Baca kritis saja; bab ini sudah lengkap. 1 soal ★. | Jangan tambah contoh. |
| 9 | Ganti kurva pendekatan etanol–air (Gambar 9.1–9.2) dengan **data terukur** dari tabel rapatan campuran, supaya contoh 9.1, 9.3, 9.4 memakai data nyata. 1 soal ★. | — |
| 10 | Baca kritis 10.7 (aktivitas: bagian paling abstrak). 1 soal ★. | — |
| 11 | Diagram segitiga (Gambar 11.6) diganti data binodal nyata air–kloroform–asam asetat bila datanya dapat diperoleh; bila tidak, tetap skematis. 1 soal ★. | Jangan tambah jenis diagram baru. |
| 12 | Tepati K5: contoh *K*_φ amonia di 12.8. 3 soal ★ (jumlah soal paling sedikit). | — |
| 13 | Contoh koreksi aktivitas (Debye–Hückel) pada persamaan Nernst, yang menghubungkan Bab 10 dan 13. 2 soal ★. | Jangan menambah subbab elektrolisis/hukum Faraday (sudah di Kimia Dasar, bukan RPS mata kuliah ini). |

Bagian di luar bab:

- **Bagian depan.** Perbaiki K1 dan K2.
- **Indeks.** Perbaiki K3.
- **Lampiran B (baru): Tabel data termodinamika.** Satu tabel gabungan Δ_f*H*°, *S*°, Δ_f*G*°, *C*_p untuk semua zat yang dipakai di buku. Saat ini data tersebar di Tabel 4.1, 6.1, 7.1, dan banyak contoh, sehingga mahasiswa harus membolak-balik saat mengerjakan soal. Ini tambahan yang benar-benar memudahkan, bukan penebal.
- **Gambar pembuka bab.** Dirapikan dengan gaya yang seragam.
- **`RENCANA.md`.** Target diganti dengan kriteria mutu (bagian 7).

## 6. Urutan kerja dan perkiraan sesi

| Tahap | Isi | Effort | Sesi |
|---|---|---|---|
| 0 | P5 global (K1, K2, K6, K7, notasi), perbarui `RENCANA.md` | medium | 1 (pendek) |
| 1 | Bab 1–2 | high → medium | 1 |
| 2 | Bab 3–4 | high → medium | 1 |
| 3 | Bab 5–6 | high → medium | 1 |
| 4 | Bab 7–8 | high → medium | 1 |
| 5 | Bab 9–10 (termasuk data etanol–air) | high → medium | 1 |
| 6 | Bab 11–13 | high → medium | 1–2 |
| 7 | Lampiran B dan indeks (K3) | medium | 1 |
| 8 | Desain pembuka dan sampul, cetak digital dan cetak, salin ke `pdf/` | medium | 1 |

Total sekitar 9–10 sesi. Setiap sesi ditutup dengan commit, push, dan PDF dikirim.

## 7. Kriteria selesai per bab

Satu bab dianggap selesai direvisi bila:

- `periksa.py N` bersih (tanpa rujukan rusak, label sementara, ejaan tidak baku);
- semua angka contoh dan jawaban soal sudah dihitung ulang dengan Python (P4);
- rubrik bagian 3 sudah dijalankan untuk setiap subbab, dan perubahan dicatat di log di bawah;
- setiap tambahan dapat ditunjuk alasannya (salah satu dari lima alasan di bagian 2);
- PDF bab diperiksa secara visual: rumus tampil, gambar tidak terpotong, kotak tidak pecah.

## 8. Log revisi

Isi setiap sesi: tanggal, bab, ringkasan perubahan, angka yang dikoreksi.

| Tanggal | Bab | Perubahan |
|---|---|---|
| 20-11-2026 | global (medium) | Sistem kotak seragam di `tk.css` (tiga kotak pembuka identik; semua kotak bergaris aksen kiri, sudut membulat, palet buku). Sampul: celah di bawah judul dirapatkan. K1–K2 bagian depan ditulis ulang; halaman judul tidak lagi menyebut buku ini lanjutan dirinya sendiri. K3 indeks: panen otomatis dimatikan, diganti 251 istilah pilihan. K6–K7 ejaan dan sapaan. Lampiran B (data termodinamika, 4 tabel). Keterangan tabel tidak lagi terpisah dari tabelnya. Skrip `periksa.py`. |
| 20-11-2026 | 1, 3, 4, 5, 6, 7 (medium) | Gambar baru: molekul memantul (1.7), piston berpasir (3.3), bom kalorimeter (4.3), siklus Clausius dipetak (5.6), entropi pencampuran (6.3), kotak termodinamika (7.6). Kalimat penjelas yang menyertai: tumbukan antarmolekul (1.7), asal tekanan 2,48/1,65/1,24 bar dan gambaran pasir (3.3), tahap adiabatik q = 0 (5.6). K4 ditepati: dS(T,V) dan dS(T,p) umum di 7.6. Contoh baru 7.1 (entropi total vs energi Gibbs). |
| 20-11-2026 | 1–6 (medium, P4) | Semua jawaban numerik soal Bab 1–6 dihitung ulang dengan Python: cocok (selisih hanya pembulatan, mis. Soal 2.19 memakai b = 0,04267). Bab 7–13 sudah dihitung saat ditulis. |
| 20-11-2026 | lampiran (medium) | Kepala lampiran diganti gaya kepala bab (LAMPIRAN kecil, huruf besar, judul kapital di kanan), juga di *Kimia Kuantum* dan *Fisika Umum*. Tabel panjang boleh menyambung halaman dengan kepala tabel diulang (menghapus halaman setengah kosong di lampiran). |
| 20-11-2026 | 1–2 (high) | Baca kritis seluruh subbab. Bab 1: catatan 273,16 vs 273,15 (1.2); Contoh 1.2 dikoreksi (selisih 1,1 °C dulu dijelaskan sebagai ketakidealan gas, padahal pada 27 kPa efeknya hanya ±0,07 K; kini data laboratorium di Bandung, titik didih 97,5 °C karena tekanan udara); catatan energi titik nol (1.7, rujuk *Kimia Kuantum* 5.4); asal $v_\text{rms} = \sqrt{3RT/M}$ dari (1.15) dan $N/V = p/kT$ di (1.22) dijelaskan; satu kalimat janggal di 1.8. Bab 2: kotak Awas *Z* < 1 (2.2); kotak Terapan tabung elpiji (2.5; tekanan uap propana/butana 30 °C dihitung dari persamaan Antoine); konstruksi Maxwell dijelaskan dan digambar di Gambar 2.3 (garis putus-putus, dua luas berarsir; `alat/gambar/bab02.py`); langkah $Z = Z_\text{c}p_\text{r}V_\text{r}/T_\text{r}$ di Contoh 2.7. |
| 20-11-2026 | 3–4 (high) | Baca kritis seluruh subbab. Bab 3: kotak Awas tanda *q* dan *w* dalam soal cerita (3.5); kotak Terapan pendinginan adiabatik udara gunung, $dT/dz = -Mg/C_{p,\text{m}} = -9{,}8$ K km⁻¹ (3.8) — pompa sepeda dan mesin diesel **tidak** dibuat kotak karena sudah menjadi Contoh 3.10–3.11; Kuis 3.8 diganti angin gending (supaya tidak dijawab oleh kotak); langkah integral adiabat dituliskan; 2 soal ★ (diferensial $dq_\text{rev}/T$ eksak → jembatan ke entropi; adiabatik tak reversibel argon, 192 K vs 119 K). Bab 4: kotak Awas $\Delta H = \Delta U + \Delta n_\text{gas}RT$ (4.1); kotak Lebih dalam siklus Born–Haber NaCl, $\Delta_\text{L}H = 787{,}4$ kJ mol⁻¹ (4.8); 3 soal ★ (Born–Haber KCl 717,6; Kirchhoff dengan $C_p(T)$, −106,7 vs −111,5 kJ mol⁻¹; kalor pembakaran per mol O₂ ≈ 450 kJ). |
| 20-11-2026 | 5–6 (high) | Baca kritis seluruh subbab. Bab 5: kalimat rujukan RPS di 5.3 diganti; Δ*S* = $q_\text{rev}/T$ diperkenalkan di Rencana Contoh 5.4 (dulu muncul tanpa definisi); paragraf skala suhu termodinamika di 5.4 dihapus karena mengulang kotak Lebih dalam; rujukan rumus pencampuran dibetulkan (5.8 dan 6.3, bukan Bab 10). Bab 6: asal $dq_\text{rev} = nC_{V,\text{m}}dT + p\,dV$ dijelaskan; rujukan maju Contoh 6.13 dirapikan; alasan $C_p \to 0$ di Contoh 6.14 dikoreksi (dulu "tidak dapat menyerap kalor", kini: agar $\int C_p\,dT/T$ berhingga); 3 soal ★ (kerja minimum memisahkan O₂ dari udara 3,87 kJ mol⁻¹; pembekuan adiabatik air lewat dingin, *f* = 0,125, Δ*S* = +0,05 J K⁻¹; entropi residu es cara Pauling). Pembahasan soal baru Bab 3, 4, 6 yang semula tertempel sesudah Bacaan lanjut dipindahkan (`alat/rapikan_pembahasan.py`). |
| 20-11-2026 | 7–8 (high) | Baca kritis seluruh subbab. Bab 7: penurunan $|w_\text{tambahan}|_\text{maks} = -\Delta G$ dituliskan (dulu "dengan penurunan yang serupa"); tanda $-T\Delta S$ di Contoh 7.7; penurunan suhu ekspansi Joule di Contoh 7.13 dinyatakan langsung (≈ 6 K); 2 soal ★ ($(\partial H/\partial p)_T = V(1 - \alpha T)$, air +170 J mol⁻¹ per 100 bar; Δ*G* gas virial, jembatan ke fugasitas). Bab 8: rujukan kriteria spontanitas (7.3, bukan 7.5); 1 soal ★ (tekanan uap air 25 °C dengan $\Delta C_p$: 3,27 kPa vs 3,75 kPa). Global: awalan "Awas:"/"Terapan:" di judul kotak Bab 8–13 dibuang (21 kotak) supaya sama dengan Bab 1–7. Rujukan nomor soal lintas bab disesuaikan (Bab 6 Soal 42 → 45; Bab 7 Soal 34 → 35). |
| 20-11-2026 | 9–10 (high) | Baca kritis seluruh subbab. Bab 9: **data etanol–air terukur tidak dipakai**, karena tabelnya (Benson & Kiyohara 1980, *J. Solution Chem.* 9, 791) tidak dapat diperiksa dari sumber terbuka; kurva pendekatan dengan keterangannya dibiarkan. Rujukan maju (9.11) diperjelas; kalimat janggal Contoh 9.13(b) diperbaiki; 1 soal ★ (Gibbs–Duhem untuk $V_\text{A} = V^*_\text{m,A} + a\,x_\text{B}^2$). Bab 10: langkah $x_\text{B} \to b_\text{B}/b^\circ$ di (10.8) dijelaskan; kotak Awas "aktivitas selalu terhadap apa" (10.7); 1 soal ★ (titik beku glikol–air tanpa pendekatan encer −11,6 °C; dari titik beku terukur $a_\text{air} = 0{,}857$, γ = 0,964). Soal ★ baru Bab 6 (pemisahan O₂) diganti soal pencampuran He 300 K + Ar 400 K (Δ*S* = 11,78 J K⁻¹), karena ternyata sama dengan Contoh 9.12(b). Penutup Bab 8–12 diseragamkan menjadi "### Menuju bab berikutnya" (dulu "## Menuju …", ikut terbaca sebagai subbab). |
| 20-11-2026 | 11–12 (high) | Baca kritis seluruh subbab. Bab 11: penurunan syarat dua lapisan (11.6) dari $\mu_\text{B}$ larutan reguler dituliskan; binodal nyata air–kloroform–asam asetat tidak dipakai (data tidak dapat dipastikan), Gambar 11.6 tetap skematis; 1 soal ★ (kelarutan ideal antrasena 0,0097 vs fenantrena 0,265). Bab 12: **K5 ditepati**, Contoh 12.16 koreksi fugasitas amonia 723 K/300 bar (φ van der Waals N₂ 1,099, H₂ 1,121, NH₃ 0,857; $K_\varphi = 0{,}474$; hasil naik 29% → 35%, cocok dengan pengukuran), Contoh 9.15 kini merujuk ke sana; alasan pengaruh tekanan di 12.5 dibetulkan (kenaikan $RT\ln p$ per mol gas, bukan "kerja *p*Δ*V* yang dihemat"); 3 soal ★ (minimum *G*(ξ) numerik; van 't Hoff dengan $\Delta C_p$, 0,094 dan 3,6 × 10⁻⁵; konversi SO₂ proses kontak 98,7%) dan soal *K*_φ lama dilengkapi. `cetak.py`: tanda petik ʼ/’ dinormalkan, sehingga subbab 12.6 kembali masuk daftar isi. |
| 20-11-2026 | 13 (high) | Baca kritis seluruh subbab. Paragraf "menjumlahkan potensial setengah sel" dijadikan kotak Awas (13.3). Contoh 13.7 baru: koreksi aktivitas pada persamaan Nernst untuk sel Harned Pt\|H₂\|HCl(0,0100 mol kg⁻¹)\|AgCl\|Ag (tanpa koreksi 0,4589 V; Debye–Hückel 0,4650 V; γ± terukur 0,904 → 0,4641 V), termasuk cara ekstrapolasi √*b* untuk menentukan *E*°; Contoh 13.13 merujuk ke sana. 2 soal ★ (Debye–Hückel pembatas vs diperluas pada 0,0500 mol kg⁻¹; *E*° sel bahan bakar pada 80 °C (1,182 V) dan SOFC 800 °C (1,006 V)). |
| 20-11-2026 | semua | `periksa.py` bersih untuk Bab 1–13. Cetak ulang versi digital (331 hlm.) dan versi cetak (340 hlm.), disalin ke `pdf/`. |

### Status pekerjaan sesi high

Semua butir yang dulu tercatat sebagai sisa pekerjaan sudah dikerjakan (20-11-2026):

- ☑ P1 baca kritis Bab 1–13 dengan rubrik bagian 3 (rincian per bab di log).
- ☑ K5: Contoh 12.16, koreksi fugasitas amonia.
- ☑ Kotak Awas/Terapan Bab 2–4: tabung elpiji, *Z* < 1, tanda *q* dan *w*, Δ*H* vs Δ*U*, Born–Haber (kotak Lebih dalam). Pompa sepeda dan mesin diesel sudah menjadi Contoh 3.10–3.11, sehingga kotak Terapan Bab 3 diganti pendinginan adiabatik udara gunung.
- ☑ Catatan energi titik nol (1.7) dan 273,16 vs 273,15 (1.2).
- ☑ Soal tantangan ★: Bab 3 (+2), 4 (+3), 6 (+3), 7 (+2), 8 (+1), 9 (+1), 10 (+1), 11 (+1), 12 (+2, satu soal lama dilengkapi), 13 (+2).
- ☑ Bab 13: koreksi Debye–Hückel pada Nernst (Contoh 13.7).
- ✗ Bab 9: data etanol–air terukur, dan Bab 11: binodal nyata air–kloroform–asam asetat. Keduanya tidak dikerjakan karena datanya tidak dapat dipastikan dari sumber terbuka. Kurva pendekatan (Gambar 9.1–9.2) dan diagram skematis (Gambar 11.6) dipertahankan dengan keterangan yang sudah ada. Bila tabel Benson & Kiyohara (1980) atau data binodal terukur tersedia, keduanya dapat diganti tanpa mengubah teks lain selain angka Contoh 9.1, 9.3, 9.4, 9.8.

Catatan alat: `alat/rapikan_pembahasan.py babNN` memindahkan pembahasan soal yang tertempel sesudah "Bacaan lanjut" ke bagian Pembahasan dan mengurutkannya menurut nomor soal. Rujukan nomor soal lintas bab ("Bab 6, Soal 45"; "Bab 7, Soal 35") harus dicek ulang setiap kali soal ditambah.
