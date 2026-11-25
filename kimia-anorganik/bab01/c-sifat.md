## 1.11 Keelektronegatifan

Energi ionisasi dan afinitas elektron adalah sifat atom **bebas**. Dalam kimia, yang lebih sering kita perlukan adalah sifat atom **dalam ikatan**: ketika dua atom berbagi sepasang elektron, ke arah mana pasangan itu condong? Ukuran untuk kecenderungan ini disebut **keelektronegatifan**, χ (chi): kemampuan atom dalam molekul untuk menarik elektron ikatan ke arah dirinya.

Keelektronegatifan tidak dapat diukur langsung seperti energi ionisasi. Karena itu ada beberapa skala, masing-masing dibangun dari besaran yang berbeda. Yang mengagumkan, skala-skala itu hampir sepakat.

### Skala Pauling: dari energi ikatan

Linus Pauling (1932) memperhatikan bahwa ikatan antara dua atom yang berbeda, A–B, hampir selalu **lebih kuat** daripada rata-rata ikatan A–A dan B–B. Misalnya, energi ikatan H–H 436 kJ mol⁻¹, Cl–Cl 243 kJ mol⁻¹, dan rata-rata geometriknya $\sqrt{436 \times 243} = 325{,}5$ kJ mol⁻¹. Ikatan H–Cl ternyata 432 kJ mol⁻¹, lebih kuat 106 kJ mol⁻¹. Pauling menafsirkan kelebihan ini sebagai sumbangan **ionik**: karena klorin menarik elektron lebih kuat, ikatan H–Cl mempunyai sedikit sifat H^δ+^–Cl^δ−^, dan tarikan elektrostatik itu menambah kekuatan ikatan. Makin besar selisih kemampuan menarik elektron, makin besar kelebihan energinya. Pauling merumuskan

$$|\chi_\text{A} - \chi_\text{B}| = 0{,}102\sqrt{\Delta}, \qquad \Delta = D(\text{A–B}) - \sqrt{D(\text{A–A})\,D(\text{B–B})} \qquad \text{(1.5)}$$

dengan semua energi ikatan dalam kJ mol⁻¹. Persamaan ini hanya memberi **selisih**, sehingga satu titik acuan harus ditetapkan. Pada skala modern, fluorin diberi nilai 3,98.

::: {.contoh}
**Contoh 1.11 · Selisih keelektronegatifan H dan F**

Energi ikatan: H–H 436, F–F 159, H–F 570 kJ mol⁻¹. Hitung |χ_F − χ_H| dengan persamaan (1.5), lalu bandingkan dengan tabel (F 3,98; H 2,20).

**Penyelesaian.** Rata-rata geometrik: $\sqrt{436 \times 159} = 263{,}3$ kJ mol⁻¹. Kelebihan energi: $\Delta = 570 - 263{,}3 = 306{,}7$ kJ mol⁻¹. Maka

$$|\chi_\text{F} - \chi_\text{H}| = 0{,}102\sqrt{306{,}7} = 0{,}102 \times 17{,}51 = 1{,}79$$

Tabel memberi $3{,}98 - 2{,}20 = 1{,}78$.

**Memahami hasil.** Ikatan H–F lebih dari dua kali lebih kuat daripada rata-rata H–H dan F–F, dan kelebihan sebesar itu menunjukkan selisih keelektronegatifan yang besar. Untuk HCl dengan cara yang sama diperoleh 1,05, sedangkan tabel memberi 0,96. Kecocokan seperti ini cukup baik untuk skala yang dibangun dari rumus sederhana. Nilai tabel adalah hasil penyesuaian terhadap banyak sekali ikatan, bukan satu molekul.
:::

### Skala Mulliken: dari energi ionisasi dan afinitas elektron

Robert Mulliken (1934) mengusulkan definisi yang lebih langsung. Atom yang sulit melepas elektron (*I* besar) **dan** senang menerima elektron (*A* besar) pasti menarik elektron ikatan dengan kuat. Maka keelektronegatifan sebanding dengan rata-rata keduanya:

$$\chi_\text{M} = \tfrac{1}{2}(I + A) \qquad \text{(1.6)}$$

dalam eV. Nilai Mulliken dapat diubah ke skala Pauling dengan hubungan empiris $\chi_\text{P} \approx 0{,}187(I + A) + 0{,}17$. Untuk klorin, $I + A = 12{,}968 + 3{,}613 = 16{,}581$ eV, sehingga $\chi_\text{M} = 8{,}29$ eV dan $\chi_\text{P} \approx 3{,}27$, dekat dengan nilai Pauling 3,16. Kelebihan skala Mulliken: memakai besaran yang terukur dengan sangat tepat dan mempunyai arti fisis yang jelas. Kekurangannya: afinitas elektron belum diketahui untuk banyak unsur, dan atom dalam ikatan tidak persis sama dengan atom bebas.

### Skala Allred–Rochow: dari gaya tarik di permukaan atom

Allred dan Rochow (1958) mengambil pendekatan yang paling dekat dengan gagasan bab ini. Elektron ikatan berada kira-kira di "permukaan" atom, pada jarak jari-jari kovalen *r*. Gaya tarik yang dirasakannya sebanding dengan $Z_\text{ef}/r^2$ (hukum Coulomb). Setelah diskalakan agar cocok dengan nilai Pauling:

$$\chi_\text{AR} = 0{,}744 + \frac{3590\, Z_\text{ef}}{r^2} \qquad \text{(1.7)}$$

dengan *r* dalam pm. *Z*ₑf dihitung dengan aturan Slater, dengan **semua** elektron valensi atom ikut melindungi (karena elektron ikatan yang ditinjau berasal dari luar, misalnya dari atom pasangannya).

::: {.contoh}
**Contoh 1.12 · Keelektronegatifan fluorin dan klorin menurut Allred–Rochow**

Hitung χ_AR untuk F (*r* = 72 pm) dan Cl (*r* = 99 pm).

**Penyelesaian.** *Fluorin.* Elektron ikatan merasakan perisai dari tujuh elektron kulit kedua (0,35 masing-masing) dan dua elektron 1s (0,85): $S = 7(0{,}35) + 2(0{,}85) = 4{,}15$, sehingga $Z_\text{ef} = 9 - 4{,}15 = 4{,}85$. Maka

$$\chi_\text{AR} = 0{,}744 + \frac{3590 \times 4{,}85}{72^2} = 0{,}744 + 3{,}36 = 4{,}10$$

*Klorin.* $S = 7(0{,}35) + 8(0{,}85) + 2(1{,}00) = 11{,}25$, $Z_\text{ef} = 5{,}75$:

$$\chi_\text{AR} = 0{,}744 + \frac{3590 \times 5{,}75}{99^2} = 0{,}744 + 2{,}11 = 2{,}85$$

**Memahami hasil.** Klorin mempunyai *Z*ₑf **lebih besar** daripada fluorin, tetapi elektron ikatannya berada jauh lebih jauh dari inti (99 lawan 72 pm). Karena gaya berbanding terbalik dengan kuadrat jarak, faktor jarak menang. Inilah sebabnya keelektronegatifan turun ke bawah golongan.
:::

![Gambar 1.9 Tiga skala keelektronegatifan untuk enam unsur. Skala Pauling (dari energi ikatan), Mulliken (dari *I* + *A*, diskalakan; N dan Si tidak ditampilkan karena afinitas elektronnya sangat kecil atau tidak pasti), dan Allred–Rochow (dari $Z_\text{ef}/r^2$). Ketiganya dibangun dari besaran yang berbeda, tetapi urutannya hampir sama.](fig/c_en.png){width=82%}

### Memakai keelektronegatifan

Gambar 1.9 menunjukkan bahwa ketiga skala memberi urutan yang hampir sama, dan itu sangat meyakinkan: tiga cara pandang yang berbeda (kekuatan ikatan, energi atom bebas, dan gaya Coulomb) menunjuk ke sifat yang sama. Dalam praktik, skala Pauling paling banyak dipakai. Ada tiga kegunaan utama:

1. **Kepolaran ikatan.** Selisih keelektronegatifan menentukan ke mana elektron ikatan condong. Pauling memperkirakan persen sifat ionik ikatan dengan $1 - e^{-(\Delta\chi)^2/4}$: HI sekitar 5 persen, HCl 21 persen, HF 55 persen, NaCl 71 persen, CsF 92 persen.
2. **Bilangan oksidasi.** Dalam menghitung bilangan oksidasi, elektron ikatan diberikan seluruhnya kepada atom yang lebih elektronegatif (Bab 2 dan 9).
3. **Kekuatan asam.** Keelektronegatifan atom pusat mempengaruhi kekuatan asam okso dan asam biner (Bab 8).

::: {.awas}
**Awas: Δχ = 1,7 bukan garis batas.** Aturan praktis "selisih lebih dari 1,7 berarti ikatan ionik" sering diajarkan, tetapi tidak ada garis batas yang tajam antara ikatan kovalen dan ionik. HF mempunyai Δχ = 1,78, tetapi berupa gas molekuler pada suhu kamar. Yang penting adalah **seberapa besar** sifat ionik suatu ikatan, bukan menggolongkannya ke salah satu kotak.
:::

::: {.kuis}
**Kuis cepat 1.11** Mengapa keelektronegatifan naik sepanjang periode dan turun ke bawah golongan? Jawab dengan persamaan (1.7). Mengapa skala Pauling memerlukan satu nilai acuan?
:::

## 1.12 Polarisabilitas dan aturan Fajans

Dalam model ionik paling sederhana, ion dianggap bola keras bermuatan yang tidak berubah bentuk. Model itu bekerja baik untuk NaCl, tetapi gagal untuk banyak senyawa lain. Aluminium klorida, misalnya, menyublim pada 180 °C, sedangkan natrium klorida baru meleleh pada 801 °C, dan magnesium klorida pada 714 °C. Ketiganya "klorida logam", tetapi sifatnya bergeser dari ionik ke kovalen. Mengapa?

Kuncinya adalah **polarisabilitas**: seberapa mudah awan elektron sebuah ion atau atom berubah bentuk bila didekati muatan listrik. Ketika kation kecil bermuatan besar mendekati anion besar, kation itu menarik awan elektron anion ke arah dirinya. Elektron yang tertarik ke ruang di antara kedua inti adalah ciri ikatan **kovalen**. Jadi makin besar distorsi ini, makin besar sifat kovalen ikatan.

Kazimierz Fajans (1923) merangkum kapan sifat kovalen membesar:

::: {.strategi}
**Aturan Fajans: sifat kovalen senyawa ionik bertambah bila**

1. **Kation kecil dan bermuatan besar.** Kation seperti itu mempunyai **daya mempolarisasi** besar, kira-kira sebanding dengan $z/r^2$.
2. **Anion besar dan bermuatan besar.** Awan elektronnya longgar dan mudah dipolarisasi: I⁻ > Br⁻ > Cl⁻ > F⁻; S²⁻ > O²⁻.
3. **Kation tidak berkonfigurasi gas mulia.** Kation dengan kulit d penuh atau sebagian (Ag⁺, Cu⁺, Hg²⁺, Pb²⁺) lebih mempolarisasi daripada kation gas mulia berukuran sama, karena elektron d melindungi inti dengan buruk.
:::

Daya mempolarisasi beberapa kation, dalam satuan $10^{-4}$ pm⁻², adalah: Cs⁺ 0,36; Na⁺ 0,96; Li⁺ 1,73; Mg²⁺ 3,86; Al³⁺ 10,5; Be²⁺ 27,4. Dari Na⁺ ke Al³⁺, daya mempolarisasi naik lebih dari sepuluh kali. Inilah yang menjelaskan deret NaCl → MgCl₂ → AlCl₃: makin ke kanan, makin kovalen, makin mudah menguap. AlCl₃ dalam fase gas berupa molekul dimer Al₂Cl₆, bukan ion.

::: {.contoh}
**Contoh 1.13 · Perak halida**

Kelarutan perak halida dalam air pada 25 °C (dari *K*_sp): AgF sangat larut; AgCl 1,3 × 10⁻⁵ mol L⁻¹; AgBr 7,3 × 10⁻⁷ mol L⁻¹; AgI 9,2 × 10⁻⁹ mol L⁻¹. Warnanya juga berubah: AgF dan AgCl putih, AgBr kuning pucat, AgI kuning. Jelaskan dengan aturan Fajans.

**Penyelesaian.** Kationnya sama, Ag⁺ (konfigurasi 4d¹⁰, bukan gas mulia, daya mempolarisasi cukup besar). Dari F⁻ ke I⁻, anion makin besar dan makin mudah dipolarisasi (aturan 2). Akibatnya sifat kovalen ikatan Ag–X makin besar dari AgF ke AgI. Senyawa yang ikatannya lebih kovalen lebih sulit dipisahkan menjadi ion-ion terhidrasi, sehingga kelarutannya turun. Warna muncul karena makin mudah elektron berpindah dari anion ke kation (transfer muatan): AgI menyerap cahaya biru dan tampak kuning.

**Memahami hasil.** Bandingkan dengan natrium halida, yang semuanya larut baik dan tidak berwarna: Na⁺ adalah kation gas mulia dengan daya mempolarisasi lebih kecil. Ag⁺ (115 pm) dan Na⁺ (102 pm) berukuran mirip, jadi perbedaan sifat mereka hampir seluruhnya berasal dari kulit 4d¹⁰ yang buruk sebagai perisai. Bab 8 akan menjelaskan pola yang sama dari sudut pandang lain: Ag⁺ adalah asam **lunak** yang lebih menyukai basa lunak seperti I⁻.
:::

::: {.kuis}
**Kuis cepat 1.12** Urutkan sifat kovalen: LiF, LiI, NaI, CsF. Mengapa BeCl₂ padat berupa rantai polimer dengan atom Cl menjembatani dua atom Be, bukan kisi ionik?
:::

## 1.13 Efek relativistik dan efek pasangan inert

Kita kembali ke teka-teki pembuka. Emas dan natrium sama-sama mempunyai satu elektron s terluar, tetapi energi ionisasi emas 9,23 eV, hampir dua kali natrium (5,14 eV) dan jauh di atas cesium (3,89 eV), tetangganya di periode yang sama. Afinitas elektron emas 2,31 eV, lebih besar daripada oksigen. Separuh penjelasannya sudah kita temukan: di bawah elektron 6s emas terdapat kulit 4f¹⁴ dan 5d¹⁰ yang sangat buruk sebagai perisai, sehingga *Z*ₑf elektron 6s besar. Separuh lainnya datang dari teori relativitas Einstein.

### Elektron yang hampir secepat cahaya

Dalam model atom hidrogenik, kelajuan rata-rata elektron 1s adalah kira-kira $v \approx Z c / 137$, dengan *c* kelajuan cahaya. Untuk hidrogen, $v/c \approx 1/137$, sangat kecil. Untuk emas (*Z* = 79), $v/c \approx 79/137 = 0{,}58$. Pada kelajuan sebesar itu, massa relativistik elektron naik dengan faktor

$$\gamma = \frac{1}{\sqrt{1 - (v/c)^2}} = \frac{1}{\sqrt{1 - 0{,}58^2}} = 1{,}22$$

Jari-jari orbital berbanding terbalik dengan massa elektron (jari-jari Bohr $a_0 \propto 1/m$), sehingga orbital 1s emas **menyusut** sekitar 18 persen dibandingkan perhitungan tanpa relativitas. Orbital s lain, yang harus tetap tegak lurus (ortogonal) terhadap 1s dan juga menembus ke daerah dekat inti, ikut menyusut. Orbital 6s emas menyusut kira-kira sebesar itu juga, sehingga elektron 6s lebih dekat ke inti dan terikat lebih kuat.

Sebaliknya, orbital d dan f, yang hampir tidak menembus, justru **mengembang** sedikit, karena orbital s dan p yang menyusut melindungi inti lebih baik. Kombinasi ini menjelaskan tiga sifat emas yang terkenal:

* **Warna kuning.** Pada perak, selisih energi antara pita 4d penuh dan pita 5s sekitar 3,7 eV, sehingga perak hanya menyerap ultraungu dan memantulkan semua warna (putih keperakan). Pada emas, 6s turun dan 5d naik, sehingga selisihnya mengecil menjadi sekitar 2,4 eV. Emas menyerap cahaya biru dan memantulkan merah dan kuning.
* **Ketahanan terhadap korosi.** Elektron 6s yang terikat erat sukar dilepas, sehingga emas hampir tidak teroksidasi oleh udara dan air.
* **Ion auride.** Orbital 6s yang rendah dan setengah terisi dapat menerima satu elektron lagi. Dalam CsAu, emas menjadi anion Au⁻ dan cesium menjadi kation Cs⁺.

Raksa, tetangga emas, mengalami efek yang sama pada pasangan elektron 6s²-nya. Pasangan itu terikat begitu erat sehingga hampir tidak ikut membentuk ikatan logam antar-atom raksa. Akibatnya raksa adalah satu-satunya logam yang cair pada suhu kamar (titik leleh −38,8 °C), sedangkan tetangganya kadmium baru meleleh pada 321 °C.

### Efek pasangan inert

Di blok p bawah, efek relativistik dan perisai buruk dari kulit d dan f muncul sebagai **efek pasangan inert**: kecenderungan pasangan elektron *n*s² unsur berat untuk **tidak** ikut dilepas atau dipakai berikatan. Akibatnya unsur berat golongan 13–15 lebih stabil pada bilangan oksidasi **dua lebih rendah** daripada nomor golongannya:

| Golongan | Ringan | Berat | Bilangan oksidasi stabil unsur berat |
|---|---|---|---|
| 13 | Al³⁺ | Tl | +1 (Tl⁺ lebih stabil daripada Tl³⁺) |
| 14 | Si(IV), Sn(IV) | Pb | +2 (Pb²⁺; PbO₂ oksidator kuat) |
| 15 | P(V) | Bi | +3 (Bi³⁺; bismutat(V) oksidator kuat) |

![Gambar 1.10 Jumlah energi ionisasi kedua dan ketiga, $I_2 + I_3$, unsur golongan 13: energi yang diperlukan untuk melepaskan pasangan *n*s². Turun dari B ke Al seperti diharapkan, tetapi naik lagi di Ga (setelah kulit 3d) dan di Tl (setelah kulit 4f dan efek relativistik).](fig/c_inert.png){width=66%}

Gambar 1.10 menunjukkan sebagiannya: energi untuk melepaskan pasangan *n*s² **tidak** turun teratur ke bawah golongan. Galium dan talium memerlukan energi lebih besar daripada aluminium dan indium di atasnya, karena elektron *n*s-nya merasakan *Z*ₑf yang besar setelah kulit d (Ga) dan kulit f serta efek relativistik (Tl).

::: {.contoh}
**Contoh 1.14 · Mengapa talium(I) stabil?**

Potensial reduksi standar Tl³⁺/Tl⁺ adalah +1,25 V, Pb⁴⁺ (sebagai PbO₂)/Pb²⁺ +1,46 V, sedangkan Sn⁴⁺/Sn²⁺ hanya +0,15 V. Apa arti angka-angka ini, dan bagaimana hubungannya dengan efek pasangan inert?

**Penyelesaian.** Potensial reduksi yang besar dan positif berarti bentuk teroksidasi (Tl³⁺, PbO₂) sangat ingin direduksi, yaitu menerima kembali dua elektron untuk menjadi Tl⁺ dan Pb²⁺. Dengan kata lain, Tl(III) dan Pb(IV) adalah **oksidator kuat** yang tidak stabil, sedangkan Tl(I) dan Pb(II) stabil. Sebaliknya, Sn⁴⁺ hanya sedikit ingin direduksi, sehingga Sn(IV) stabil dan Sn²⁺ bahkan mudah dioksidasi menjadi Sn⁴⁺ oleh udara.

Selain energi ionisasi yang besar untuk melepaskan pasangan 6s², ada faktor kedua: ikatan unsur berat lebih lemah (orbitalnya besar dan tumpang tindihnya buruk), sehingga energi yang diperoleh kembali dari membentuk dua ikatan tambahan tidak cukup untuk membayar biaya melepaskan pasangan 6s².

**Memahami hasil.** Efek pasangan inert bukan karena pasangan 6s² benar-benar "lembam", tetapi karena keseimbangan biaya–untung bergeser untuk unsur berat. Akumulator timbal di mobil memanfaatkan sifat ini: PbO₂ (Pb(IV)) direduksi menjadi PbSO₄ (Pb(II)) sambil menghasilkan arus listrik. Bab 9 menghitung potensial seperti ini.
:::

::: {.kuis}
**Kuis cepat 1.13** Mengapa efek relativistik jauh lebih penting untuk emas (*Z* = 79) daripada perak (*Z* = 47)? Hitung $v/c$ dan $\gamma$ untuk elektron 1s perak.
:::

## 1.14 Anomali periode 2 dan hubungan diagonal

Unsur periode kedua (Li sampai F) sering berperilaku sangat berbeda dari unsur lain di golongannya. Litium lebih mirip magnesium daripada natrium, karbon membentuk ikatan rangkap dengan mudah sedangkan silikon hampir tidak, dan nitrogen berupa gas diatomik sedangkan fosfor berupa padatan. Semua keanehan ini berakar pada satu sifat: **atom periode kedua sangat kecil**.

### Akibat ukuran yang kecil

* **Bilangan koordinasi maksimum kecil.** Atom kecil hanya dapat dikelilingi sedikit tetangga. Nitrogen membentuk NF₃ tetapi tidak NF₅, sedangkan fosfor membentuk PF₅. Karbon tetravalen, silikon dapat membentuk ion SiF₆²⁻. Dahulu perbedaan ini dijelaskan dengan "orbital d kosong" pada periode 3. Perhitungan modern menunjukkan bahwa orbital d hampir tidak terlibat. Penjelasan yang lebih tepat adalah ukuran, dan ikatan tiga pusat empat elektron yang akan kita bahas di Bab 4.
* **Ikatan π kuat.** Orbital 2p kecil dan dapat mendekat cukup rapat untuk bertumpang tindih sisi ke sisi dengan baik. Orbital 3p lebih besar dan menyebar, dan pada panjang ikatan yang lebih besar tumpang tindih π-nya buruk. Karena itu C=C, C=O, N=N, dan N≡N kuat, sedangkan Si=Si, Si=O, dan P≡P relatif lemah.
* **Ikatan tunggal antar-atom berpasangan bebas lemah.** Ikatan F–F (159 kJ mol⁻¹) jauh lebih lemah daripada Cl–Cl (243 kJ mol⁻¹), dan N–N, O–O juga lemah. Pada ikatan yang pendek, pasangan elektron bebas di kedua atom berada sangat dekat dan saling menolak.

::: {.contoh}
**Contoh 1.15 · Mengapa N₂ tetapi P₄?**

Energi ikatan (kJ mol⁻¹): N≡N 945, N–N 160, P≡P 490, P–P 201. Molekul P₄ berbentuk tetrahedron dengan enam ikatan P–P. Bandingkan energi ikatan per dua atom untuk N₂ lawan N₄ (tetrahedron hipotetis) dan untuk P₂ lawan P₄.

**Penyelesaian.** Tetrahedron E₄ mempunyai enam ikatan tunggal untuk empat atom, yaitu tiga ikatan per dua atom.

*Nitrogen.* N₂: satu ikatan rangkap tiga, 945 kJ. N₄: tiga ikatan tunggal, $3 \times 160 = 480$ kJ. N₂ lebih stabil sebesar $945 - 480 = 465$ kJ per dua atom.

*Fosfor.* P₂: 490 kJ. P₄: $3 \times 201 = 603$ kJ. P₄ lebih stabil sebesar $603 - 490 = 113$ kJ per dua atom.

**Memahami hasil.** Untuk nitrogen, satu ikatan rangkap tiga jauh lebih kuat daripada tiga ikatan tunggal, karena ikatan π 2p–2p kuat dan ikatan tunggal N–N lemah (tolakan pasangan bebas). Untuk fosfor, kebalikannya: tiga ikatan tunggal mengalahkan satu ikatan rangkap tiga yang ikatan π-nya lemah. Pola yang sama menjelaskan CO₂ (molekul O=C=O, karena satu C=O 799 kJ lebih kuat daripada dua C–O, $2 \times 358 = 716$ kJ) lawan SiO₂ (jaringan Si–O tunggal, karena dua Si–O, $2 \times 452 = 904$ kJ, jauh lebih kuat daripada satu Si=O yang diperkirakan sekitar 640 kJ). Itulah sebabnya karbon dioksida gas dan silikon dioksida batuan pasir.
:::

### Hubungan diagonal

Unsur periode kedua sering lebih mirip unsur di **kanan bawah** dirinya daripada unsur tepat di bawahnya. Pasangan yang terkenal adalah Li–Mg, Be–Al, dan B–Si.

| Pasangan | Kemiripan |
|---|---|
| Li dan Mg | bereaksi langsung dengan N₂ membentuk nitrida (Li₃N, Mg₃N₂); karbonatnya terurai bila dipanaskan menjadi oksida; fluorida, karbonat, dan fosfatnya sukar larut; senyawa organologamnya (LiR, RMgX) sangat berguna |
| Be dan Al | hidroksidanya amfoter (larut dalam asam dan basa); kloridanya kovalen, menguap, dan bersifat asam Lewis; keduanya dipasivasi oleh asam nitrat pekat |
| B dan Si | oksidanya bersifat asam dan membentuk kaca (B₂O₃, SiO₂); hidridanya mudah menguap dan terbakar spontan; keduanya metaloid dan semikonduktor |

Penjelasannya: dari kiri ke kanan, *Z*ₑf naik sehingga atom mengecil dan keelektronegatifan naik. Ke bawah, atom membesar dan keelektronegatifan turun. Bergerak diagonal (ke kanan sekaligus ke bawah), kedua efek itu kira-kira saling meniadakan. Keelektronegatifan Pauling memperlihatkannya dengan jelas: Li 0,98 dan Mg 1,31; Be 1,57 dan Al 1,61; B 2,04 dan Si 1,90. Untuk ion, ukuran dan muatan juga bergeser bersamaan: Li⁺ kecil bermuatan satu, Mg²⁺ lebih besar bermuatan dua, sehingga daya mempolarisasi keduanya lebih mirip satu sama lain daripada Li⁺ dengan Na⁺.

::: {.terapan}
**Litium dalam pengobatan dan baterai**

Kemiripan litium dengan magnesium punya akibat biologis. Garam litium (litium karbonat) dipakai sebagai obat gangguan bipolar sejak 1949. Salah satu cara kerjanya diperkirakan adalah ion Li⁺ menggantikan Mg²⁺ pada beberapa enzim. Di sisi teknologi, ion Li⁺ yang kecil dan ringan dapat bergerak masuk–keluar di antara lapisan grafit dan oksida kobalt atau besi fosfat. Inilah dasar baterai litium-ion, yang dibahas lagi di Bab 7.
:::

::: {.kuis}
**Kuis cepat 1.14** Mengapa CO₂ berupa molekul gas, sedangkan SiO₂ berupa padatan jaringan? Sebutkan dua kemiripan berilium dengan aluminium.
:::

## Menuju bab berikutnya

Sekarang teka-teki natrium dan emas dapat dijawab. Elektron 3s natrium terlindung oleh kulit [Ne] yang hampir sempurna sebagai perisai: *Z*ₑf-nya hanya sekitar 2,2 (Slater) dan energi ionisasinya 5,14 eV. Elektron 6s emas terletak di atas kulit 4f¹⁴ dan 5d¹⁰ yang buruk sebagai perisai, sehingga merasakan tarikan inti yang jauh lebih besar. Di atas itu, elektron yang bergerak dekat inti emas mencapai lebih dari separuh kelajuan cahaya, dan efek relativistik menyusutkan orbital 6s lebih jauh lagi. Hasilnya energi ionisasi 9,23 eV, afinitas elektron 2,31 eV, warna kuning, dan ketahanan terhadap korosi. Natrium dan emas berbeda bukan karena elektron terluarnya, tetapi karena **apa yang ada di bawah elektron itu**.

Bab ini membangun satu alat utama, **muatan inti efektif**, dan memakainya untuk menjelaskan jari-jari, energi ionisasi, afinitas elektron, keelektronegatifan, dan berbagai keanehan tabel periodik. Semua itu adalah sifat atom sendiri-sendiri. Bab 2 menyatukan atom-atom itu: bagaimana elektron dibagi dalam ikatan kovalen, bagaimana menggambar struktur Lewis dan menghitung bilangan oksidasi, dan bagaimana model VSEPR meramalkan bentuk molekul dari jumlah pasangan elektron di sekitar atom pusat. Keelektronegatifan dari subbab 1.11 akan langsung dipakai untuk meramalkan kepolaran ikatan dan momen dipol.
