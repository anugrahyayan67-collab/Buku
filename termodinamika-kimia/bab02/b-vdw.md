## 2.3 Persamaan van der Waals

Kita sudah tahu apa yang perlu diperbaiki dari persamaan gas ideal: molekul mempunyai ukuran, dan molekul saling menarik. Pada 1873, Johannes Diderik van der Waals memasukkan kedua efek itu ke dalam persamaan gas ideal dengan dua koreksi yang sangat sederhana. Mari kita bangun keduanya satu per satu.

**Koreksi ukuran.** Karena molekul tidak dapat saling menembus, setiap molekul tidak bebas bergerak di seluruh volume wadah *V*. Sebagian volume itu "dipesan" oleh molekul-molekul lain. Bila setiap mol molekul memesan volume *b*, maka ruang yang benar-benar tersedia untuk gerak adalah $V - nb$, dan persamaan gas ideal menjadi

$$
p = \frac{nRT}{V - nb} .
$$

Koreksi ini menaikkan tekanan: ruang gerak yang lebih sempit membuat molekul menumbuk dinding lebih sering. Inilah pengaruh yang membuat $Z > 1$ pada tekanan tinggi.

**Koreksi tarikan.** Molekul yang hendak menumbuk dinding ditarik ke belakang oleh tetangga-tetangganya di dalam gas, sehingga ia menumbuk dengan kurang keras. Akibatnya tekanan **berkurang**. Seberapa banyak? Pengurangan itu sebanding dengan dua hal: banyaknya molekul yang menumbuk dinding, yang sebanding dengan konsentrasi *n*/*V*, dan kuatnya tarikan pada setiap molekul itu, yang juga sebanding dengan banyaknya tetangga yang menarik, *n*/*V*. Hasil kali keduanya sebanding dengan $(n/V)^2$. Menyebut tetapan kesebandingannya *a*, kita memperoleh

::: {.inti}
$$
p = \frac{nRT}{V - nb} - a\frac{n^2}{V^2} \qquad \text{atau} \qquad \left(p + \frac{a}{V_\text{m}^2}\right)(V_\text{m} - b) = RT \qquad \text{(2.3)}
$$
**Persamaan van der Waals.** Tetapan *a* mengukur kekuatan tarikan antarmolekul; tetapan *b* mengukur volume molekul itu sendiri.
:::

Tetapan *a* dan *b* adalah sifat masing-masing gas dan ditentukan dari percobaan (Tabel 2.1). Pola nilainya sesuai dengan dugaan dari gaya antarmolekul: *a* kecil untuk helium dan hidrogen yang tarikannya lemah, dan besar untuk molekul polar seperti NH₃ dan H₂O; *b* naik dengan ukuran molekul.

| Gas | *a* (L² bar mol⁻²) | *b* (L mol⁻¹) |
|---|---|---|
| He | 0,0346 | 0,0238 |
| H₂ | 0,2476 | 0,0266 |
| N₂ | 1,370 | 0,0387 |
| O₂ | 1,382 | 0,0319 |
| Ar | 1,355 | 0,0320 |
| CH₄ | 2,283 | 0,0428 |
| CO₂ | 3,640 | 0,0427 |
| NH₃ | 4,225 | 0,0371 |
| H₂O | 5,536 | 0,0305 |

Tabel 2.1 Tetapan van der Waals beberapa gas.

::: {.contoh}
**Contoh 2.3 · Empat gas dalam wadah yang sama**

Satu mol gas dikurung dalam wadah 0,500 L pada 300 K. Hitung tekanannya menurut persamaan gas ideal dan menurut persamaan van der Waals untuk He, N₂, CH₄, dan CO₂.

**Penyelesaian.** Gas ideal: $p = RT/V_\text{m} = (0{,}083\,14)(300)/0{,}500 = 49{,}9$ bar untuk semua gas. Untuk CO₂, dengan (2.3):
$$
p = \frac{(0{,}083\,14)(300)}{0{,}500 - 0{,}0427} - \frac{3{,}640}{(0{,}500)^2} = 54{,}5 - 14{,}6 = 40{,}0\ \text{bar} .
$$
Dengan cara yang sama: He 52,2 bar; N₂ 48,6 bar; CH₄ 45,4 bar.

**Memahami hasil.** Suku pertama (koreksi ukuran) selalu menaikkan tekanan sedikit di atas 49,9 bar. Suku kedua (tarikan) menurunkannya. Untuk helium, tarikannya begitu lemah sehingga koreksi ukuran menang dan $p$ lebih besar daripada gas ideal. Untuk CO₂, tarikan menang telak dan tekanannya 20% lebih rendah, cocok dengan Contoh 2.1. Urutan He > N₂ > CH₄ > CO₂ adalah urutan kekuatan tarikan antarmolekul.
:::

::: {.contoh}
**Contoh 2.4 · Berapa banyak metana dalam tabung CNG?**

Tabung gas alam terkompresi (CNG) bervolume 50,0 L diisi metana sampai 200 bar pada 25 °C. Berapa kilogram metana di dalamnya menurut (a) persamaan gas ideal, (b) persamaan van der Waals?

**Rencana.** Persamaan van der Waals tidak dapat diselesaikan langsung untuk $V_\text{m}$ karena berbentuk pangkat tiga. Kita mencari akarnya secara numerik, lalu $n = V/V_\text{m}$.

**Penyelesaian.** (a) $n = pV/RT = (200)(50{,}0)/[(0{,}083\,14)(298{,}15)] = 403$ mol, yaitu $403 \times 16{,}04$ g $= 6{,}47$ kg.

(b) Mengalikan (2.3) dengan $V_\text{m}^2$ menghasilkan persamaan pangkat tiga
$$
pV_\text{m}^3 - (pb + RT)V_\text{m}^2 + aV_\text{m} - ab = 0 .
$$
Akarnya dihitung dengan Python:
```python
import numpy as np
R, T, p = 0.08314, 298.15, 200.0
a, b = 2.283, 0.04278                  # CH4
print(np.roots([p, -(p*b + R*T), a, -a*b]))   # V_m = 0.1017 L/mol
```
Dengan $V_\text{m} = 0{,}1017$ L mol⁻¹, $n = 50{,}0/0{,}1017 = 492$ mol, atau 7,89 kg.

**Memahami hasil.** Tabung itu memuat 22% lebih banyak metana daripada ramalan gas ideal, karena tarikan antarmolekul "membantu" memampatkan gas ($Z = 403/492 = 0{,}82$). Perancang tabung dan stasiun pengisian harus memperhitungkan efek ini; perhitungan gas ideal akan meremehkan isi tabung hampir satu setengah kilogram.
:::

::: {.kuis}
**Kuis cepat 2.3** Dalam persamaan van der Waals, apa yang terjadi bila $a = 0$ dan $b = 0$? Bila hanya $a = 0$, apakah *Z* lebih besar atau lebih kecil dari 1?
:::

## 2.4 Isoterm gas nyata dan pencairan gas

Pada 1869, Thomas Andrews mengukur dengan teliti bagaimana volume karbon dioksida berubah ketika ditekan pada berbagai suhu tetap. Hasilnya menjadi salah satu percobaan paling penting dalam sejarah kimia fisika, karena untuk pertama kalinya memperlihatkan dengan jelas hubungan antara gas dan cairan.

Pada suhu tinggi, misalnya 50 °C, isoterm CO₂ mirip hiperbola Boyle, hanya sedikit melengkung. Pada suhu rendah, misalnya 20 °C, sesuatu yang baru terjadi. Mula-mula, ketika gas ditekan, volumenya berkurang dan tekanannya naik seperti biasa. Lalu, pada tekanan tertentu, tetes cairan pertama muncul. Sejak saat itu, menekan piston lebih jauh tidak menaikkan tekanan sama sekali: volume terus berkurang, tetapi yang terjadi hanyalah makin banyak gas berubah menjadi cairan. Isotermnya menjadi **garis mendatar**. Tekanan di sepanjang garis itu adalah **tekanan uap** cairan pada suhu tersebut. Baru setelah semua gas mencair, tekanan naik lagi, dan kali ini dengan sangat curam, karena cairan hampir tidak dapat dimampatkan.

Apa yang diramalkan persamaan van der Waals untuk keadaan ini? Gambar 2.3 menunjukkan isoterm van der Waals pada beberapa suhu. Pada suhu tinggi, kurvanya mirip isoterm Andrews. Pada suhu rendah, kurvanya membentuk **lengkungan** naik-turun, sesuatu yang tidak pernah teramati pada gas yang setimbang: di bagian tengah lengkungan, tekanan naik bila volume diperbesar, dan zat yang seperti itu akan langsung runtuh.

![Gambar 2.3 Isoterm van der Waals dalam variabel tereduksi (subbab 2.6). Di atas suhu kritis isotermnya mirip isoterm gas ideal. Di bawahnya muncul lengkungan; pada zat nyata, lengkungan itu diganti oleh garis mendatar pada tekanan uap, tempat gas dan cairan hidup berdampingan. Pada isoterm 0,85, garis putus-putus adalah konstruksi Maxwell: kedua luas berarsir sama besar, dan kedua ujung garis memberi volume molar cairan dan gas.](fig/isoterm.png){width=76%}

Lengkungan itu bukan kegagalan persamaan, melainkan petunjuk. Maxwell menunjukkan cara mengganti lengkungan dengan garis mendatar yang sebenarnya. Garis itu ditarik pada tekanan yang membuat luas yang terpotong di atas garis sama dengan luas di bawahnya (**konstruksi Maxwell**; lihat isoterm 0,85 pada Gambar 2.3). Ujung kiri garis itu adalah volume molar cairan, ujung kanannya volume molar gas, dan tingginya adalah tekanan uap yang diramalkan persamaan van der Waals. Pada $T_\text{r} = 0{,}85$, tekanan uap itu $0{,}50\,p_\text{c}$.

Mengapa luasnya harus sama? Alasan lengkapnya memerlukan energi Gibbs, yang baru kita kenal di Bab 7. Gas dan cairan hanya dapat setimbang bila energi Gibbs molarnya sama (subbab 8.2), dan untuk isoterm van der Waals syarat itu ternyata setara dengan dua luas yang sama. Untuk sekarang, cukup dipegang gambarannya: pada suhu tertentu, tinggi garis mendatar itu adalah satu-satunya tekanan tempat gas dan cairan dapat hidup berdampingan. Persamaan van der Waals, yang dibangun dari gagasan tentang gas, ternyata juga mengandung cairan.

::: {.contoh}
**Contoh 2.5 · Tiga akar persamaan van der Waals**

Untuk CO₂ pada 280 K dan 50 bar, persamaan van der Waals mempunyai tiga akar nyata. (a) Hitung ketiganya. (b) Apa arti masing-masing? (c) Hitung massa jenis yang bersesuaian dengan akar terkecil dan terbesar.

**Penyelesaian.** (a) Dengan kode Contoh 2.4 (diganti $a = 3{,}640$, $b = 0{,}042\,67$, $T = 280$, $p = 50$): $V_\text{m} = 0{,}0823$; 0,1257; 0,3003 L mol⁻¹.

(b) Akar terbesar adalah volume molar **gas**, akar terkecil volume molar **cairan**. Akar tengah terletak di bagian lengkungan tempat tekanan naik bila volume bertambah; keadaan itu tidak stabil dan tidak pernah teramati.

(c) Cairan: $44{,}01/0{,}0823 = 535$ g L⁻¹. Gas: $44{,}01/0{,}300 = 147$ g L⁻¹.

**Memahami hasil.** Pada 280 K, kedua fasa memang dapat ada. Mana yang benar-benar terbentuk pada 50 bar ditentukan oleh tekanan uap: bila 50 bar di atas tekanan uap (seperti di sini; tekanan uap CO₂ pada 280 K sekitar 42 bar), zat itu berupa cairan. Pemilihan akar yang tepat adalah pekerjaan rutin dalam perangkat lunak teknik kimia.
:::

::: {.kuis}
**Kuis cepat 2.4** Mengapa tekanan tidak naik ketika gas yang sedang mencair ditekan lebih lanjut pada suhu tetap?
:::

## 2.5 Titik kritis dan tetapan kritis

Kembali ke percobaan Andrews. Makin tinggi suhunya, makin pendek garis mendatar pada isoterm. Pada 31,0 °C, garis itu menyusut menjadi satu titik saja. Di atas suhu itu, garis mendatar lenyap: gas dapat ditekan sekuat apa pun dan tidak pernah muncul permukaan cairan yang terpisah. Suhu khusus ini disebut **suhu kritis** $T_\text{c}$, dan titik tempat garis mendatar lenyap disebut **titik kritis**, dengan tekanan kritis $p_\text{c}$ dan volume molar kritis $V_\text{c}$.

Inilah jawaban teka-teki pembuka. Suhu kritis CO₂ adalah 304,1 K (31,0 °C), sedikit di atas suhu kamar. Karena itu CO₂ pada suhu kamar dapat dicairkan, dan di dalam tabung pemadam ia berupa cairan yang setimbang dengan uapnya pada tekanan uap sekitar 64 bar. Suhu kritis oksigen adalah 154,6 K (−118,6 °C), jauh di bawah suhu kamar. Pada suhu kamar, oksigen **tidak mungkin** dicairkan, berapa pun tekanannya; untuk mencairkannya kita harus mendinginkannya lebih dulu di bawah suhu kritisnya.

Dapatkah persamaan van der Waals meramalkan titik kritis? Pada Gambar 2.3, isoterm kritis adalah isoterm tempat lengkungan baru saja mendatar menjadi satu titik belok yang landai. Di titik itu, kemiringan dan kelengkungan isoterm sama-sama nol:

$$
\left(\frac{\partial p}{\partial V_\text{m}}\right)_T = 0 , \qquad \left(\frac{\partial^2 p}{\partial V_\text{m}^2}\right)_T = 0 . \qquad \text{(2.4)}
$$

Menyelesaikan kedua syarat ini bersama persamaan (2.3) menghasilkan

::: {.inti}
$$
V_\text{c} = 3b , \qquad T_\text{c} = \frac{8a}{27Rb} , \qquad p_\text{c} = \frac{a}{27b^2} \qquad \text{(2.5)}
$$
:::

::: {.dalam}
**Lebih dalam: menurunkan tetapan kritis.** Dari (2.3), $p = RT/(V_\text{m} - b) - a/V_\text{m}^2$. Kedua turunannya:
$$
\frac{\partial p}{\partial V_\text{m}} = -\frac{RT}{(V_\text{m} - b)^2} + \frac{2a}{V_\text{m}^3} = 0 , \qquad \frac{\partial^2 p}{\partial V_\text{m}^2} = \frac{2RT}{(V_\text{m} - b)^3} - \frac{6a}{V_\text{m}^4} = 0 .
$$
Dari persamaan pertama, $RT = 2a(V_\text{m} - b)^2/V_\text{m}^3$. Memasukkannya ke persamaan kedua: $4a/[V_\text{m}^3(V_\text{m} - b)] = 6a/V_\text{m}^4$, sehingga $4V_\text{m} = 6(V_\text{m} - b)$, atau $V_\text{c} = 3b$. Lalu $RT_\text{c} = 2a(2b)^2/(3b)^3 = 8a/27b$. Akhirnya $p_\text{c} = RT_\text{c}/(2b) - a/(9b^2) = 4a/27b^2 - 3a/27b^2 = a/27b^2$.
:::

Persamaan (2.5) bekerja ke dua arah. Dari *a* dan *b* kita dapat meramalkan titik kritis; sebaliknya, dari $T_\text{c}$ dan $p_\text{c}$ yang terukur kita dapat menghitung *a* dan *b*. Cara kedua inilah yang biasanya dipakai untuk menyusun tabel tetapan van der Waals:

$$
a = \frac{27R^2T_\text{c}^2}{64p_\text{c}} , \qquad b = \frac{RT_\text{c}}{8p_\text{c}} . \qquad \text{(2.6)}
$$

| Gas | $T_\text{c}$ (K) | $p_\text{c}$ (bar) | $V_\text{c}$ (cm³ mol⁻¹) |
|---|---|---|---|
| He | 5,2 | 2,3 | 58 |
| N₂ | 126,2 | 34,0 | 90 |
| O₂ | 154,6 | 50,4 | 73 |
| Ar | 150,7 | 48,6 | 75 |
| CO₂ | 304,1 | 73,8 | 94 |
| H₂O | 647,1 | 220,6 | 56 |

Tabel 2.2 Tetapan kritis beberapa zat.

::: {.contoh}
**Contoh 2.6 · Meramalkan titik kritis CO₂**

Dari tetapan van der Waals CO₂ ($a = 3{,}640$ L² bar mol⁻², $b = 0{,}042\,67$ L mol⁻¹), hitung $T_\text{c}$, $p_\text{c}$, dan $V_\text{c}$, lalu bandingkan dengan Tabel 2.2.

**Penyelesaian.**
$$
T_\text{c} = \frac{8(3{,}640)}{27(0{,}083\,14)(0{,}042\,67)} = 304\ \text{K} , \qquad p_\text{c} = \frac{3{,}640}{27(0{,}042\,67)^2} = 74{,}0\ \text{bar} ,
$$
dan $V_\text{c} = 3b = 0{,}128$ L mol⁻¹ $= 128$ cm³ mol⁻¹.

**Memahami hasil.** Suhu dan tekanan kritis cocok sempurna, tetapi itu tidak mengherankan: *a* dan *b* dalam Tabel 2.1 memang dihitung dari $T_\text{c}$ dan $p_\text{c}$ dengan (2.6). Ujian yang jujur adalah volume kritis, yang tidak dipakai dalam perhitungan itu. Di sini persamaan van der Waals meleset 36% (128 dibanding 94 cm³ mol⁻¹). Persamaan van der Waals menangkap gambaran kualitatif dengan sangat baik, tetapi angkanya di sekitar titik kritis hanya kasar.
:::

::: {.terapan}
**Tabung elpiji: gas yang dijual dalam bentuk cair.** Elpiji (LPG) adalah campuran propana dan butana. Suhu kritis keduanya jauh di atas suhu kamar (propana 369,8 K, butana 425,1 K), sehingga keduanya dapat dicairkan hanya dengan menekannya, seperti CO₂ di tabung pemadam. Pada 30 °C, tekanan uap propana murni sekitar 10,8 bar dan butana murni sekitar 2,8 bar. Tekanan di dalam tabung elpiji terletak di antara keduanya, bergantung pada komposisinya (subbab 10.2 menghitungnya dengan hukum Raoult). Dalam bentuk cair, isi tabung 3 kg cukup kecil untuk dijinjing; sebagai gas pada 1 bar dan 25 °C, isi yang sama menempati sekitar 1,5 m³.

Isoterm Andrews (subbab 2.4) menjelaskan dua hal yang dikenal setiap orang yang memasak. Pertama, selama masih ada cairan di dalam tabung, tekanannya hampir tidak berubah sampai isinya nyaris habis, karena keadaan di dalam tabung berada di garis mendatar isoterm. Karena itu pengukur tekanan tidak dapat memberi tahu sisa isi tabung; cara yang benar adalah menimbangnya. Kedua, bila kompor menyala besar terus-menerus, dinding tabung terasa dingin dan kadang berembun, karena cairan yang menguap menyerap kalor (subbab 4.4). Tabung juga tidak pernah diisi penuh dengan cairan. Cairan memuai bila dipanaskan, dan tanpa ruang uap tekanan di dalam tabung tertutup akan naik sangat tajam.
:::

::: {.kuis}
**Kuis cepat 2.5** Suhu kritis NH₃ adalah 405,5 K. Dapatkah amonia dicairkan pada suhu kamar hanya dengan menekannya? Bagaimana dengan metana ($T_\text{c} = 190{,}6$ K)?
:::

## 2.6 Hukum keadaan sehubungan

Tetapan kritis memberi setiap gas "skala" alaminya sendiri. Nitrogen pada 300 K jauh di atas suhu kritisnya (2,4 kali), sedangkan CO₂ pada 300 K hampir tepat di suhu kritisnya. Tidak heran keduanya berperilaku sangat berbeda pada suhu yang sama. Bagaimana jika kita membandingkan gas-gas itu bukan pada suhu dan tekanan yang sama, tetapi pada **pecahan** yang sama dari nilai kritisnya masing-masing?

Gagasan itu dirumuskan dengan **variabel tereduksi**:

$$
T_\text{r} = \frac{T}{T_\text{c}} , \qquad p_\text{r} = \frac{p}{p_\text{c}} , \qquad V_\text{r} = \frac{V_\text{m}}{V_\text{c}} . \qquad \text{(2.7)}
$$

Van der Waals sendiri menemukan bahwa bila (2.5) dimasukkan ke persamaannya, semua tetapan khas gas lenyap, dan yang tersisa adalah persamaan yang sama untuk semua gas:

$$
\left(p_\text{r} + \frac{3}{V_\text{r}^2}\right)(3V_\text{r} - 1) = 8T_\text{r} . \qquad \text{(2.8)}
$$

Persamaan (2.8) menyatakan **hukum keadaan sehubungan**: gas-gas yang berada pada suhu tereduksi dan tekanan tereduksi yang sama mempunyai volume tereduksi yang sama, dan karena itu faktor kompresi yang sama. Hukum ini ternyata berlaku jauh lebih baik daripada persamaan van der Waals itu sendiri, terutama untuk molekul yang kira-kira bulat dan nonpolar. Insinyur kimia memanfaatkannya dengan grafik *Z* umum terhadap $p_\text{r}$ untuk berbagai $T_\text{r}$, yang dapat dipakai untuk gas apa pun yang tetapan kritisnya diketahui.

Ada satu ujian sederhana. Pada titik kritis, faktor kompresi $Z_\text{c} = p_\text{c}V_\text{c}/RT_\text{c}$. Persamaan van der Waals meramalkan $Z_\text{c} = 3/8 = 0{,}375$ untuk semua gas. Nilai terukur kebanyakan gas memang hampir sama satu sama lain, sekitar 0,27–0,29, yang mendukung hukum keadaan sehubungan, tetapi lebih kecil daripada ramalan van der Waals.

Hukum keadaan sehubungan paling berguna dalam bentuk grafik. Bila *Z* digambar terhadap $p_r$ untuk beberapa nilai $T_r$, kita memperoleh **diagram faktor kompresi umum** (Gambar 2.4): satu lembar grafik yang berlaku, secara pendekatan, untuk semua gas. Gambar ini dihitung dari persamaan van der Waals tereduksi; diagram yang dipakai di industri dibuat dari data terukur banyak gas, tetapi bentuknya sama. Tiga hal tampak sekaligus. Dekat suhu kritis ($T_r \approx 1$), *Z* turun tajam karena tarikan mendominasi. Pada $T_r$ yang tinggi, kurvanya hampir datar di sekitar 1. Pada tekanan sangat tinggi semua kurva naik di atas 1, karena volume molekul sendiri mulai menentukan.

![Gambar 2.4 Diagram faktor kompresi umum menurut persamaan van der Waals tereduksi. Setiap kurva berlaku untuk semua gas pada suhu tereduksi yang sama. Di dekat titik kritis ($T_r$ = 1) penyimpangan paling besar; makin tinggi $T_r$, makin dekat gas ke perilaku ideal.](fig/zumum.png){width=80%}

::: {.contoh}
**Contoh 2.7 · Metana di tabung bertekanan, dibaca dari diagram umum**

Tabung 50,0 L berisi metana ($T_\text{c}$ = 190,6 K, $p_\text{c}$ = 46,0 bar) pada 92,0 bar dan 250 K. Berapa kilogram metana di dalamnya menurut persamaan gas ideal dan menurut diagram faktor kompresi umum?

**Rencana.** Hitung variabel tereduksi, baca *Z*, lalu pakai $n = pV/ZRT$.

**Penyelesaian.** $T_r = 250/190{,}6 = 1{,}31$ dan $p_r = 92{,}0/46{,}0 = 2{,}00$. Kurva van der Waals pada keadaan itu memberi $Z = 0{,}66$. Menurut gas ideal,
$$
n_\text{ideal} = \frac{pV}{RT} = \frac{(92{,}0\ \text{bar})(50{,}0\ \text{L})}{(0{,}083\,14\ \text{L bar K}^{-1}\,\text{mol}^{-1})(250\ \text{K})} = 221\ \text{mol} \quad (3{,}55\ \text{kg}),
$$
sedangkan gas nyata memuat $n = n_\text{ideal}/Z = 333$ mol, yaitu 5,35 kg.

**Memahami hasil.** Pada keadaan ini tarikan antarmolekul begitu penting sehingga tabung memuat setengah lagi lebih banyak gas daripada ramalan gas ideal. Perusahaan gas yang menghitung isi tabung dengan *pV* = *nRT* akan salah besar. Nilai *Z* dari van der Waals hanya pendekatan; untuk pekerjaan teknik, *Z* dibaca dari diagram berdasarkan data terukur atau dihitung dengan persamaan Peng–Robinson (subbab 2.8). Pendekatannya tetap sama: dua angka tereduksi sudah cukup.
:::

::: {.contoh}
**Contoh 2.8 · Dua gas dalam keadaan yang "sama"**

(a) Pada suhu dan tekanan berapa N₂ dan CO₂ masing-masing berada pada $T_\text{r} = 2{,}0$ dan $p_\text{r} = 2{,}0$? (b) Hitung *Z* keduanya dari persamaan (2.8).

**Penyelesaian.** (a) N₂: $T = 2{,}0 \times 126{,}2 = 252$ K, $p = 2{,}0 \times 34{,}0 = 68$ bar. CO₂: $T = 608$ K, $p = 148$ bar.

(b) Persamaan (2.8) dengan $T_\text{r} = p_\text{r} = 2{,}0$ diselesaikan untuk $V_\text{r}$, memberi $V_\text{r} = 2{,}48$. Faktor kompresinya diperoleh dengan mengganti setiap variabel dengan variabel tereduksinya: $Z = pV_\text{m}/RT = (p_\text{r}p_\text{c})(V_\text{r}V_\text{c})/(RT_\text{r}T_\text{c}) = Z_\text{c}\,p_\text{r}V_\text{r}/T_\text{r}$. Dengan $Z_\text{c} = 3/8$ menurut van der Waals, $Z = (2{,}0)(2{,}48)(0{,}375)/2{,}0 = 0{,}93$, sama untuk kedua gas.

**Memahami hasil.** Nitrogen pada 252 K dan 68 bar dan CO₂ pada 608 K dan 148 bar tampak sebagai keadaan yang sama sekali berbeda, tetapi keduanya menyimpang dari perilaku ideal dengan cara yang sama. Itulah kekuatan hukum keadaan sehubungan: data satu gas dapat dipakai untuk meramalkan perilaku gas lain.
:::

::: {.kuis}
**Kuis cepat 2.6** Gas A mempunyai $T_\text{c} = 150$ K dan gas B $T_\text{c} = 300$ K. Pada 300 K dan tekanan tereduksi yang sama, gas mana yang lebih mendekati perilaku ideal?
:::
