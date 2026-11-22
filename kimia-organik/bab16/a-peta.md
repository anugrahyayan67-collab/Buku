# Bab 16 Strategi Sintesis

Pada tahun 1856, William Henry Perkin, mahasiswa berusia delapan belas tahun, mencoba membuat kina, obat malaria yang saat itu hanya dapat diperoleh dari kulit pohon kina di Amerika Selatan. Rencananya sederhana tetapi naif: rumus molekul kina adalah C₂₀H₂₄N₂O₂, dan ia berharap dua molekul aliltoluidina (C₁₀H₁₃N) dapat "digabungkan" dengan oksigen menjadi kina. Pada masa itu struktur kina belum diketahui, dan kimiawan belum memahami bahwa molekul bukan sekadar kumpulan atom yang dapat dijumlahkan seperti rumus. Percobaannya gagal total. Tetapi ketika ia mengulanginya dengan anilina yang tidak murni, ia memperoleh endapan hitam yang, bila dilarutkan dalam alkohol, memberi warna ungu cemerlang: **mauvein**, pewarna sintetik pertama di dunia, yang melahirkan industri kimia modern.

Kina sendiri baru berhasil disintesis secara meyakinkan hampir sembilan puluh tahun kemudian, setelah strukturnya diketahui dan setelah kimiawan memiliki dua hal yang tidak dimiliki Perkin: **kumpulan reaksi yang hasilnya dapat diramalkan** dan **cara berpikir untuk merangkainya**. Selama lima belas bab kita telah mengumpulkan bagian pertama: substitusi dan eliminasi, adisi pada alkena dan alkuna, oksidasi dan reduksi, substitusi aromatik, adisi pada karbonil, dan substitusi asil. Di bab terakhir buku ini kita mengumpulkan bagian kedua: **strategi sintesis**. Bagaimana memilih reaksi yang tepat, bagaimana menyusunnya dalam urutan yang benar, bagaimana merencanakan dari belakang, dan bagaimana menilai apakah sebuah rencana sintesis itu baik.

Bab ini tidak memperkenalkan banyak reaksi baru. Isinya adalah cara memakai reaksi-reaksi lama secara baru. Kalau bab-bab sebelumnya seperti mempelajari kosakata dan tata bahasa, bab ini seperti belajar menulis karangan.

::: {.kuis}
**Pertanyaan pembuka**

1. Bagaimana mengubah propan-1-ol menjadi propan-2-ol, padahal keduanya hanya berbeda letak gugus OH?
2. Mengapa pereaksi Grignard sering disebut "pisau serbaguna" kimiawan sintesis?
3. Bagaimana kita merencanakan sintesis sebuah molekul yang belum pernah dibuat, bila kita tidak tahu harus mulai dari bahan apa?
4. Mengapa urutan langkah penting dalam membuat *m*-bromonitrobenzena dan *p*-bromonitrobenzena?
5. Bagaimana mereduksi gugus ester dalam molekul yang juga mempunyai gugus keton, tanpa menyentuh ketonnya?
6. Sintesis sepuluh langkah dengan hasil 90% per langkah: berapa persen hasil keseluruhannya?
7. Mengapa reaksi yang hasilnya 95% belum tentu reaksi yang "hijau"?
:::

::: {.tujuan}
**Tujuan belajar**

Setelah mempelajari bab ini, kamu mampu:

1. Menjelaskan tujuan sintesis organik dan kriteria rencana sintesis yang baik.
2. Menyusun peta perubahan gugus fungsi berdasarkan tingkat oksidasi karbon dan memilih pereaksi untuk setiap perubahan.
3. Memilih reaksi pembentuk ikatan C–C yang sesuai untuk memperpanjang rantai atau membangun kerangka tertentu.
4. Melakukan analisis retrosintesis: memutus ikatan secara strategis, mengenali sinton dan padanan sintetiknya, dan menyusun rencana sintesis maju.
5. Memperhitungkan kemoselektivitas, regioselektivitas, dan stereoselektivitas dalam memilih pereaksi dan urutan langkah.
6. Merancang pemakaian gugus pelindung.
7. Menghitung hasil keseluruhan sintesis bertahap dan membandingkan sintesis linear dengan konvergen.
8. Menghitung ekonomi atom dan menilai sintesis menurut asas kimia hijau.
9. Menganalisis dan merancang sintesis obat sederhana.
:::

::: {.mat}
**Prasyarat**

Bab 7–13: semua reaksi utama yang akan dirangkai di bab ini. Terutama: substitusi dan eliminasi (subbab 7.4–7.13), organologam (subbab 7.14), adisi pada alkena dan alkuna (subbab 8.3–8.13), alkohol dan eter (subbab 9.2–9.11), substitusi aromatik (subbab 10.5–10.12), reaksi karbonil (subbab 11.2–11.11), turunan asam (subbab 12.4–12.10), dan amina (subbab 13.3–13.5). Bab 14–15: spektroskopi untuk memeriksa hasil.
:::

## 16.1 Mengapa sintesis

### Membuat molekul dengan sengaja

**Sintesis organik** adalah pembuatan senyawa organik yang diinginkan, disebut **molekul target**, dari bahan awal yang tersedia, melalui serangkaian reaksi yang direncanakan. Ada beberapa alasan mengapa kimiawan melakukannya.

1. **Membuat senyawa yang berguna dalam jumlah besar.** Banyak obat, pestisida, pewarna, wewangian, dan bahan polimer tidak dapat diperoleh dari alam dalam jumlah yang cukup, atau sama sekali tidak ada di alam. Hampir semua obat di apotek dibuat lewat sintesis bertahap.
2. **Membuat senyawa baru untuk diuji.** Dalam penemuan obat, ratusan sampai ribuan senyawa yang mirip dengan sebuah senyawa aktif disintesis untuk mencari yang paling manjur dan paling aman.
3. **Memastikan struktur.** Sebelum ada NMR, struktur senyawa alam baru dianggap terbukti bila senyawa itu berhasil disintesis dari bahan yang strukturnya diketahui, dan hasilnya identik dengan senyawa alam. Hari ini spektroskopi sudah jauh lebih andal, tetapi sintesis masih kadang membongkar struktur yang salah tetapkan.
4. **Menguji gagasan.** Senyawa yang dirancang untuk menguji teori, misalnya molekul tegang, aromatik nonbenzenoid, atau molekul untuk menguji mekanisme, hanya dapat diperoleh lewat sintesis.

Sejarah sintesis organik sering dianggap dimulai pada tahun 1828, ketika Friedrich Wöhler memanaskan amonium sianat (senyawa anorganik) dan memperoleh urea, senyawa yang sebelumnya hanya dikenal dari urin. Sejak itu sintesis berkembang dari pembuatan molekul sederhana menjadi seni dan ilmu yang mampu membuat molekul seperumit vitamin B₁₂ (sembilan puluhan langkah, dirampungkan oleh Woodward dan Eschenmoser pada 1972) dan obat antikanker taksol.

### Apa yang membuat rencana sintesis baik

Untuk hampir setiap molekul target ada banyak jalan sintesis yang mungkin. Kimiawan menilai jalan-jalan itu dengan beberapa kriteria:

- **Pendek.** Setiap langkah tambahan menurunkan hasil keseluruhan, menambah waktu, biaya, dan limbah (subbab 16.7).
- **Hasil tinggi dan selektif.** Setiap langkah sebaiknya menghasilkan satu produk utama, tanpa campuran isomer yang sulit dipisahkan.
- **Bahan awal murah dan mudah diperoleh.** Senyawa sederhana dari industri petrokimia (etena, propena, benzena, toluena, metanol, asam asetat) atau dari alam (glukosa, asam amino, minyak nabati).
- **Aman dan ramah lingkungan.** Menghindari pereaksi yang sangat beracun, pelarut berbahaya, dan limbah dalam jumlah besar (subbab 16.8).
- **Dapat diperbesar skalanya.** Reaksi yang berhasil dengan 100 mg di laboratorium belum tentu aman atau ekonomis pada skala ton di pabrik.

Tidak ada rencana yang sempurna pada semua kriteria sekaligus. Kemampuan menimbang kriteria-kriteria inilah yang membedakan kimiawan sintesis yang baik.

::: {.inti}
**Inti subbab 16.1**

- Sintesis organik membuat molekul target dari bahan awal yang tersedia melalui rangkaian reaksi yang direncanakan.
- Tujuannya: menyediakan senyawa berguna, membuat senyawa baru untuk diuji, memastikan struktur, dan menguji gagasan.
- Rencana yang baik: pendek, selektif, hasil tinggi, bahan awal murah, aman, ramah lingkungan, dapat diperbesar skalanya.
:::

::: {.kuis}
**Kuis cepat 16.1** (a) Mengapa sintesis dulu dipakai untuk membuktikan struktur senyawa alam? (b) Sebutkan tiga kriteria rencana sintesis yang baik.
:::

## 16.2 Mengubah gugus fungsi: peta reaksi

### Tingkat oksidasi karbon sebagai peta

Hampir setiap sintesis memerlukan dua jenis langkah: langkah yang **membentuk kerangka karbon** (ikatan C–C, subbab 16.3) dan langkah yang **mengubah gugus fungsi** tanpa mengubah kerangka. Langkah jenis kedua disebut **interkonversi gugus fungsi** (*functional group interconversion*, FGI).

Cara paling berguna untuk menata semua interkonversi ini adalah menurut **tingkat oksidasi** karbon pembawa gugus fungsi (subbab 9.5). Hitung jumlah ikatan karbon itu ke atom yang lebih elektronegatif (O, N, halogen); ikatan rangkap dihitung dua, rangkap tiga dihitung tiga:

| Tingkat | Ikatan ke heteroatom | Gugus fungsi |
|---|---|---|
| 0 | tidak ada | alkana (dan alkena/alkuna sebagai kasus khusus) |
| 1 | satu | alkohol, eter, alkil halida, amina, tiol |
| 2 | dua | aldehida, keton, asetal, imina, *gem*-dihalida |
| 3 | tiga | asam karboksilat, ester, amida, klorida asam, anhidrida, nitril |
| 4 | empat | CO₂, karbonat, urea |

Perubahan **dalam satu tingkat** (misalnya alkohol → alkil halida, atau ester → amida) tidak memerlukan oksidator atau reduktor; cukup substitusi. Perubahan **ke tingkat lebih tinggi** memerlukan oksidator, dan **ke tingkat lebih rendah** memerlukan reduktor. Alkena dan alkuna istimewa: adisi H–X atau H₂O pada alkena menghasilkan alkohol atau alkil halida tanpa oksidasi bersih, karena satu karbon mendapat heteroatom dan karbon tetangganya mendapat hidrogen.

![Gambar 16.1 Peta tingkat oksidasi. Gugus fungsi dalam satu kolom saling dihubungkan oleh substitusi (tanpa oksidator atau reduktor). Panah ke kanan memerlukan oksidator (PCC, asam kromat, KMnO₄), panah ke kiri memerlukan reduktor (NaBH₄, LiAlH₄, H₂/katalis). Alkena dan alkuna masuk ke peta lewat adisi.](fig/tingkat.png){width=96%}

### Peta reaksi

Peta berikut merangkum interkonversi terpenting yang telah kita pelajari. Hafalkan bukan sebagai daftar, melainkan sebagai jaringan: dari setiap gugus fungsi, tanyakan "ke mana saja saya dapat pergi dalam satu langkah, dan dengan pereaksi apa?"

![Gambar 16.2 Peta interkonversi gugus fungsi utama. Setiap panah adalah satu langkah dengan pereaksi khas di sampingnya; nomor subbab menunjukkan tempat reaksi itu dibahas. Perhatikan bahwa alkohol berada di pusat jaringan: hampir semua gugus fungsi dapat dicapai dari alkohol atau dapat diubah menjadi alkohol.](fig/peta.png){width=100%}

| Dari | Menjadi | Pereaksi khas | Subbab |
|---|---|---|---|
| alkena | alkohol (Markovnikov) | H₃O⁺; atau Hg(OAc)₂, H₂O lalu NaBH₄ | 8.5 |
| alkena | alkohol (anti-Markovnikov) | BH₃·THF lalu H₂O₂, NaOH | 8.6 |
| alkena | alkil halida | HBr (Markovnikov); HBr, peroksida (anti-Markovnikov) | 8.3, 8.11 |
| alkena | diol | OsO₄ (*syn*); epoksidasi lalu H₃O⁺ (*anti*) | 8.9 |
| alkena | aldehida/keton | O₃ lalu (CH₃)₂S | 8.10 |
| alkohol | alkil halida | HX; PBr₃; SOCl₂ | 9.3 |
| alkohol | tosilat (gugus pergi) | TsCl, piridina | 7.13 |
| alkohol | alkena | H₂SO₄, panas; atau TsCl lalu basa | 9.4 |
| alkohol 1° | aldehida | PCC atau oksidasi Swern | 9.5 |
| alkohol 1° | asam karboksilat | H₂CrO₄ (Jones) atau KMnO₄ | 9.5 |
| alkohol 2° | keton | PCC, H₂CrO₄ | 9.5 |
| alkil halida | alkohol, eter, nitril, amina | OH⁻, RO⁻, CN⁻, N₃⁻ lalu reduksi (SN2) | 7.4–7.6, 13.3 |
| alkil halida | alkena | basa kuat (E2) | 7.9 |
| aldehida/keton | alkohol | NaBH₄ atau LiAlH₄ | 11.7 |
| aldehida/keton | alkana (C=O → CH₂) | Wolff–Kishner atau Clemmensen | 11.7 |
| aldehida/keton | amina | amina, NaBH₃CN (aminasi reduktif) | 13.3 |
| asam karboksilat | klorida asam | SOCl₂ | 12.5 |
| klorida asam | ester, amida, anhidrida | ROH, amina, karboksilat | 12.5 |
| ester | asam | NaOH lalu H₃O⁺ (saponifikasi) | 12.7 |
| ester | alkohol 1° | LiAlH₄ | 12.10 |
| amida | amina | LiAlH₄ | 12.10 |
| nitril | asam; amina 1° | H₃O⁺, panas; LiAlH₄ | 12.9 |
| alkuna | alkena *cis*; *trans* | H₂, Lindlar; Na, NH₃ | 8.13 |
| alkuna terminal | metil keton; aldehida | H₂O, H₂SO₄, HgSO₄; disiamilboran lalu H₂O₂ | 8.13 |
| arena | nitroarena → anilina | HNO₃, H₂SO₄; lalu Fe, HCl atau H₂, Pd | 10.6, 13.3 |
| anilina | ArX, ArCN, ArOH | NaNO₂, HCl lalu CuX, CuCN, atau H₂O, panas | 13.5 |

::: {.contoh}
**Contoh 16.1 · Membaca tingkat oksidasi**

Tentukan apakah setiap perubahan berikut memerlukan oksidator, reduktor, atau tidak keduanya, lalu sebutkan pereaksinya: (a) butan-1-ol → butanal; (b) butanoil klorida → butanamida; (c) butanenitril → butan-1-amina; (d) but-1-ena → butan-2-ol.

**Penyelesaian.** (a) C1 naik dari tingkat 1 (satu ikatan C–O) ke tingkat 2 (C=O): **oksidasi**; PCC dalam CH₂Cl₂ (oksidator yang lebih kuat akan meneruskan ke asam). (b) Keduanya tingkat 3: **tanpa oksidasi atau reduksi**; NH₃ berlebih (substitusi asil). (c) C≡N tingkat 3 menjadi CH₂–NH₂ tingkat 1: **reduksi**; LiAlH₄ lalu H₂O. (d) Adisi air pada alkena: C2 mendapat O dan C1 mendapat H, tidak ada oksidasi bersih; **H₃O⁺** atau oksimerkurasi–demerkurasi (Markovnikov).

**Memahami hasil.** Pertanyaan "naik, turun, atau tetap?" langsung menyaring pereaksi yang mungkin. Bila sebuah perubahan memerlukan reduksi, tidak ada gunanya mencari jawabannya di antara substitusi atau oksidasi.
:::

::: {.contoh}
**Contoh 16.2 · Memindahkan gugus fungsi**

Tunjukkan cara mengubah (a) propan-1-ol menjadi propan-2-ol; (b) propan-2-ol menjadi propan-1-ol; (c) 1-bromobutana menjadi 2-bromobutana.

**Gambaran fisis.** Ketiga soal meminta gugus fungsi berpindah ke karbon tetangga. Tidak ada satu reaksi pun yang melakukannya langsung. Jalan yang umum: hilangkan gugus fungsi dengan eliminasi untuk membuat alkena, lalu tambahkan kembali dengan adisi yang regioselektivitasnya kita pilih.

**Penyelesaian.** (a) Propan-1-ol → (H₂SO₄, panas, atau TsCl lalu *t*-BuOK) propena → (H₃O⁺, Markovnikov) **propan-2-ol**. (b) Propan-2-ol → (H₂SO₄, panas) propena → (BH₃·THF lalu H₂O₂, NaOH; anti-Markovnikov) **propan-1-ol**. (c) 1-Bromobutana → (*t*-BuOK, E2) but-1-ena → (HBr tanpa peroksida, Markovnikov) **2-bromobutana**.

**Memahami hasil.** Pola "eliminasi lalu adisi" adalah salah satu taktik FGI yang paling sering dipakai. Pada (c), halida primer cenderung mengalami SN2; basa besar seperti *t*-BuOK dipakai agar eliminasi E2 menang (subbab 7.9 dan 7.12).
:::

::: {.inti}
**Inti subbab 16.2**

- Interkonversi gugus fungsi (FGI) mengubah gugus tanpa mengubah kerangka karbon.
- Tata FGI menurut tingkat oksidasi: dalam satu tingkat cukup substitusi; naik perlu oksidator; turun perlu reduktor.
- Alkohol adalah pusat jaringan FGI. Taktik "eliminasi lalu adisi" memindahkan gugus fungsi ke karbon tetangga.
:::

::: {.kuis}
**Kuis cepat 16.2** Tuliskan pereaksi untuk: (a) sikloheksanol → sikloheksanon; (b) sikloheksanon → sikloheksana; (c) asam benzoat → benzil alkohol; (d) 1-feniletanol → stirena.
:::

## 16.3 Membentuk ikatan C–C

### Nukleofil karbon bertemu elektrofil karbon

Ikatan C–C baru hampir selalu terbentuk ketika sebuah **nukleofil karbon** (karbon kaya elektron: karbanion, organologam, enol, cincin aromatik kaya elektron) bertemu sebuah **elektrofil karbon** (karbon miskin elektron: karbon pembawa gugus pergi, karbon karbonil, karbokation, epoksida). Di Kimia Organik 1 kita telah mempelajari nukleofil karbon berikut: ion sianida, ion asetilida, pereaksi Grignard dan organolitium, kuprat Gilman, ilida fosfor (Wittig), dan cincin aromatik (Friedel–Crafts). Reaksi enolat sebagai nukleofil karbon (aldol, Claisen, alkilasi α) adalah alat yang sangat penting tetapi akan dibahas di *Kimia Organik 2*.

| Nukleofil karbon | Elektrofil | Produk | Tambahan C | Subbab |
|---|---|---|---|---|
| ⁻C≡N | R–X (1°, 2°) | R–C≡N (→ asam, amina) | 1 | 7.4, 12.9 |
| R′C≡C⁻ | R–X (1°) | alkuna internal | 2 atau lebih | 8.12 |
| R′MgX, R′Li | H₂C=O | alkohol 1° | R′ | 11.8 |
| R′MgX, R′Li | RCHO | alkohol 2° | R′ | 11.8 |
| R′MgX, R′Li | R₂C=O | alkohol 3° | R′ | 11.8 |
| R′MgX (2 ekuivalen) | ester RCOOR″ | alkohol 3° dengan dua R′ sama | 2 × R′ | 12.10 |
| R′MgX | CO₂ | asam R′COOH | 1 | 12.2 |
| R′MgX | epoksida | alkohol (R′ + 2 C) | R′ + 2 | 9.11 |
| R′₂CuLi | R–X | R–R′ | R′ | 7.14 |
| ilida Ph₃P=CR₂ | aldehida/keton | alkena | CR₂ | 11.9 |
| arena | RCOCl, AlCl₃ | aril keton | RCO | 10.7 |
| ⁻CN | aldehida/keton | sianohidrin | 1 | 11.4 |

![Gambar 16.3 Satu pereaksi Grignard, banyak produk. Fenilmagnesium bromida bereaksi dengan formaldehida (alkohol 1°), asetaldehida (alkohol 2°), aseton (alkohol 3°), CO₂ (asam benzoat), dan oksirana (2-feniletanol, dua karbon bertambah). Ikatan C–C baru ditandai.](fig/grignard.png){width=98%}

### Memilih reaksi C–C menurut produk

Cara paling efektif memilih reaksi C–C adalah melihat **gugus fungsi yang ada di dekat ikatan C–C baru** dalam produk:

- Ikatan C–C di sebelah karbon pembawa **OH** (alkohol): pereaksi Grignard atau organolitium + aldehida/keton. Bila OH berada **dua karbon** dari ikatan baru: Grignard + epoksida.
- Ikatan C–C di sebelah **COOH**: Grignard + CO₂, atau R–X + CN⁻ lalu hidrolisis.
- Ikatan C–C di sebelah **C≡C**: alkilasi ion asetilida.
- Ikatan C=C baru: reaksi Wittig (menyambung dua potongan tepat di ikatan rangkap).
- Ikatan aril–C=O: asilasi Friedel–Crafts.
- Ikatan C–C tanpa gugus fungsi di dekatnya (misalnya dalam alkana): kuprat Gilman + R–X, atau bangun dulu dengan reaksi lain lalu hapus gugus fungsinya (misalnya hidrogenasi alkuna atau alkena, reduksi Wolff–Kishner).

::: {.contoh}
**Contoh 16.3 · Tiga cara membuat alkohol tersier**

Usulkan dua sintesis 2-metilheksan-2-ol, (CH₃)₂C(OH)CH₂CH₂CH₂CH₃, dari pereaksi Grignard dan keton, dan satu sintesis dari pereaksi Grignard dan ester.

**Rencana.** Karbon pembawa OH (C2) mempunyai tiga gugus alkil: dua CH₃ dan satu butil. Setiap ikatan C–C di sekitar C2 dapat dibentuk oleh Grignard: satu gugus datang dari pereaksi Grignard, dua gugus lainnya sudah terikat pada karbonil.

**Penyelesaian.** (1) Butilmagnesium bromida + **aseton**: CH₃CH₂CH₂CH₂MgBr + (CH₃)₂C=O → produk. (2) Metilmagnesium bromida + **heksan-2-on**: CH₃MgBr + CH₃COCH₂CH₂CH₂CH₃ → produk. Karena kedua metil pada C2 identik, hanya ada dua kombinasi Grignard + keton yang berbeda. (3) **Ester**: 2 ekuivalen CH₃MgBr + metil pentanoat, CH₃CH₂CH₂CH₂COOCH₃; Grignard pertama mengubah ester menjadi heksan-2-on, yang langsung bereaksi dengan Grignard kedua.

**Memahami hasil.** Dalam memilih di antara jalan-jalan ini, kimiawan melihat harga dan ketersediaan: aseton dan butil bromida sangat murah, sehingga jalan (1) biasanya dipilih. Jalan ester cocok bila dua gugus yang sama perlu dipasang sekaligus. Mengenali gugus yang identik di sekitar karbon target menghemat waktu: memutus salah satu dari dua ikatan C–CH₃ memberi rencana yang sama.
:::

::: {.contoh}
**Contoh 16.4 · Memperpanjang rantai**

Mulai dari 1-bromobutana dan pereaksi apa pun yang mengandung paling banyak dua atom karbon, buatlah (a) asam pentanoat; (b) pentan-1-amina; (c) heksan-1-ol; (d) pentan-1-ol.

**Penyelesaian.** (a) Dua cara: CH₃CH₂CH₂CH₂Br + NaCN (SN2) → pentanenitril → H₃O⁺, panas → **asam pentanoat**; atau Mg, eter → BuMgBr → CO₂ lalu H₃O⁺ → asam pentanoat. (b) Pentanenitril dari (a) → LiAlH₄ lalu H₂O → **pentan-1-amina** (CH₂NH₂ baru dari karbon nitril). (c) Perlu dua karbon tambahan dengan OH di ujung: BuMgBr + **oksirana** (epoksida dua karbon) lalu H₃O⁺ → **heksan-1-ol**. Tanpa oksirana, jalannya dua kali lebih panjang: BuMgBr + H₂C=O → pentan-1-ol → PBr₃ → 1-bromopentana → Mg → + H₂C=O → heksan-1-ol. (d) BuMgBr + **formaldehida** lalu H₃O⁺ → **pentan-1-ol**.

**Memahami hasil.** Sianida dan formaldehida dengan Grignard adalah dua cara standar menambah **satu** karbon; CO₂ juga menambah satu karbon tetapi langsung pada tingkat oksidasi asam. Epoksida menambah **dua** karbon dengan OH di ujung rantai. Mengulang "tambah satu karbon" berkali-kali dimungkinkan tetapi memperpanjang sintesis; lebih baik memilih reaksi yang menambah potongan sebesar mungkin sekaligus.
:::

::: {.contoh}
**Contoh 16.5 · Membangun dengan asetilida**

Buatlah (*Z*)-dek-5-ena dari asetilena dan alkil halida apa pun.

**Penyelesaian.** (*Z*)-Dek-5-ena, CH₃(CH₂)₃CH=CH(CH₂)₃CH₃, mempunyai ikatan rangkap *cis* di tengah dua gugus butil. Alkena *cis* dibuat dari alkuna dengan H₂/katalis Lindlar, sehingga kita perlu dek-5-una, CH₃(CH₂)₃C≡C(CH₂)₃CH₃. Alkuna ini dibuat dengan dua kali alkilasi asetilena: (1) HC≡CH + NaNH₂ → HC≡C⁻Na⁺; + CH₃CH₂CH₂CH₂Br → heks-1-una. (2) heks-1-una + NaNH₂ → asetilida; + CH₃CH₂CH₂CH₂Br → dek-5-una. (3) H₂, katalis Lindlar → **(*Z*)-dek-5-ena**.

**Memahami hasil.** Asetilena adalah "bata" dua karbon yang dapat disambung di kedua ujungnya, lalu ikatan rangkap tiganya diubah menjadi alkena *cis* (Lindlar), alkena *trans* (Na/NH₃), alkana (H₂, Pd), atau keton (hidrasi). Alkil halidanya harus primer, karena ion asetilida adalah basa kuat yang akan menyebabkan eliminasi E2 pada halida sekunder dan tersier (subbab 8.12).
:::

::: {.awas}
**Hati-hati: Grignard tidak tahan proton asam**

Pereaksi Grignard dan organolitium adalah basa yang sangat kuat (p*K*ₐ asam konjugatnya sekitar 50). Mereka langsung dihancurkan oleh air, alkohol, asam karboksilat, amina primer dan sekunder, dan alkuna terminal. Karena itu Grignard **tidak dapat dibuat** dari alkil halida yang juga mengandung OH, NH, atau COOH, dan tidak dapat direaksikan dengan karbonil yang molekulnya mengandung gugus-gugus itu, kecuali gugus tersebut dilindungi lebih dulu (subbab 16.6). Grignard juga bereaksi dengan C=O lain dalam molekul yang sama; jangan pernah membuat Grignard dari 4-bromobutan-2-on.
:::

::: {.inti}
**Inti subbab 16.3**

- Ikatan C–C terbentuk antara nukleofil karbon (CN⁻, asetilida, Grignard/organolitium, kuprat, ilida, arena) dan elektrofil karbon (R–X, C=O, CO₂, epoksida, ion asilium).
- Pilih reaksi menurut gugus fungsi di dekat ikatan baru: OH → Grignard + karbonil; OH dua karbon jauhnya → Grignard + epoksida; COOH → CO₂ atau CN⁻; C≡C → asetilida; C=C → Wittig; Ar–CO → Friedel–Crafts.
- Penambahan satu karbon: CN⁻, CO₂, atau H₂C=O; dua karbon: epoksida atau asetilena.
:::

::: {.kuis}
**Kuis cepat 16.3** Pereaksi Grignard dan karbonil apa yang memberi: (a) 1-fenilpropan-1-ol; (b) 2-fenilpropan-2-ol (dua cara); (c) 3-fenilpropan-1-ol (dari benzilmagnesium bromida)?
:::
