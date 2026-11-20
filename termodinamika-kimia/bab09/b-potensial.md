## 9.3 Potensial kimia

Energi Gibbs molar parsial diberi nama dan lambang tersendiri, karena perannya jauh melampaui besaran molar parsial lain:

::: {.inti}
$$
\mu_\text{J} = \left(\frac{\partial G}{\partial n_\text{J}}\right)_{T,\,p,\,n'} . \qquad \text{(9.4)}
$$
**Potensial kimia** zat J: pertambahan energi Gibbs campuran bila satu mol J ditambahkan pada suhu, tekanan, dan komposisi tetap. Untuk zat murni, $\mu = G_\text{m}$.
:::

Menurut (9.3), energi Gibbs campuran adalah $G = \sum_\text{J} n_\text{J}\mu_\text{J}$. Potensial kimia adalah sumbangan per mol setiap zat terhadap energi Gibbs campuran, persis seperti volume molar parsial adalah sumbangan per mol terhadap volume.

Sekarang kita dapat menulis ulang persamaan fundamental untuk sistem yang komposisinya dapat berubah, karena reaksi kimia atau karena zat masuk dan keluar. Energi Gibbs kini bergantung pada *T*, *p*, dan banyaknya mol setiap zat, sehingga diferensial totalnya mempunyai suku tambahan untuk setiap zat:

::: {.inti}
$$
dG = -S\,dT + V\,dp + \sum_\text{J}\mu_\text{J}\,dn_\text{J} . \qquad \text{(9.5)}
$$
**Persamaan fundamental termodinamika kimia.** Dua suku pertama sudah kita kenal dari (7.8); suku ketiga menyatakan perubahan *G* karena perubahan komposisi.
:::

Persamaan (9.5) adalah titik awal hampir semua bab berikutnya. Pada suhu dan tekanan tetap ia menjadi $dG = \sum_\text{J}\mu_\text{J}\,dn_\text{J}$, dan karena $-dG$ adalah kerja bukan-ekspansi maksimum (subbab 7.4), potensial kimia juga mengukur kerja maksimum yang dapat diperoleh dari perubahan komposisi. Sel elektrokimia di Bab 13 mengubah selisih potensial kimia langsung menjadi kerja listrik.

::: {.dalam}
**Lebih dalam: empat wajah potensial kimia.** Suku $\sum\mu_\text{J}\,dn_\text{J}$ muncul dengan cara yang sama dalam keempat persamaan fundamental. Dengan menambahkannya ke $dU = T\,dS - p\,dV$ dan mengulang penurunan subbab 7.5, diperoleh
$$
\mu_\text{J} = \left(\frac{\partial U}{\partial n_\text{J}}\right)_{S,V,n'} = \left(\frac{\partial H}{\partial n_\text{J}}\right)_{S,p,n'} = \left(\frac{\partial A}{\partial n_\text{J}}\right)_{T,V,n'} = \left(\frac{\partial G}{\partial n_\text{J}}\right)_{T,p,n'} .
$$
Keempatnya adalah besaran yang sama, tetapi hanya yang terakhir merupakan besaran molar **parsial**, karena hanya *G* yang diturunkan pada *T* dan *p* tetap. Bentuk pertama menunjukkan bahwa potensial kimia mengukur berapa energi dalam bertambah bila satu mol zat ditambahkan tanpa mengubah entropi dan volume. Itulah sebabnya Gibbs, yang memperkenalkannya pada 1876, menyebutnya "potensial".
:::

### Ke mana zat bergerak

Arti paling penting dari potensial kimia adalah arah. Bayangkan zat J dapat berpindah antara dua daerah, α dan β, misalnya dua fasa, atau dua sisi sebuah membran, pada suhu dan tekanan tetap. Bila $dn$ mol J berpindah dari α ke β, menurut (9.5):

$$
dG = \mu_\text{J}(\beta)\,dn - \mu_\text{J}(\alpha)\,dn = \left[\mu_\text{J}(\beta) - \mu_\text{J}(\alpha)\right]dn . \qquad \text{(9.6)}
$$

Ini persis argumen subbab 8.2, kini untuk satu komponen di dalam campuran. Perpindahan spontan bila *dG* < 0, yaitu bila $\mu_\text{J}(\alpha) > \mu_\text{J}(\beta)$. Maka:

::: {.inti}
**Zat berpindah secara spontan dari tempat dengan potensial kimia tinggi ke tempat dengan potensial kimia rendah.** Kesetimbangan tercapai bila potensial kimia setiap zat sama di semua tempat yang dapat dijangkaunya.
:::

Perhatikan kata "setiap zat". Dalam campuran, setiap komponen mempunyai potensial kimianya sendiri, dan masing-masing bergerak menurut potensial kimianya sendiri. Oksigen dapat mengalir dari udara ke dalam darah sementara karbon dioksida mengalir ke arah sebaliknya, melewati membran yang sama pada saat yang sama, karena keduanya menuruni lereng potensial kimia masing-masing.

Analoginya dengan potensial listrik sangat dekat. Muatan listrik mengalir dari potensial tinggi ke rendah, dan aliran berhenti ketika potensial sama. Massa mengalir menuruni potensial gravitasi. Kalor mengalir dari suhu tinggi ke rendah. Potensial kimia adalah "suhu" bagi materi: ia memberi tahu ke mana setiap zat ingin pergi.

::: {.contoh}
**Contoh 9.6 · Iodin di antara dua pelarut**

Iodin larut sedikit dalam air dan jauh lebih baik dalam tetraklorometana (CCl₄). Larutan iodin dalam air dikocok bersama CCl₄ murni. Jelaskan dengan potensial kimia apa yang terjadi, dan kapan prosesnya berhenti.

**Penyelesaian.** Mula-mula tidak ada iodin dalam CCl₄. Seperti akan kita lihat di subbab 9.5 dan Bab 10, potensial kimia zat terlarut naik bila konsentrasinya naik dan turun tanpa batas bila konsentrasinya menuju nol. Jadi $\mu_{\text{I}_2}(\text{CCl}_4)$ sangat rendah dan iodin berpindah dari air ke CCl₄. Ketika konsentrasi di CCl₄ naik dan di air turun, kedua potensial kimia saling mendekati. Perpindahan berhenti ketika $\mu_{\text{I}_2}(\text{air}) = \mu_{\text{I}_2}(\text{CCl}_4)$.

**Memahami hasil.** Pada kesetimbangan, konsentrasi iodin dalam CCl₄ sekitar 85 kali konsentrasinya dalam air. Konsentrasi tidak sama, tetapi potensial kimia sama. Molekul iodin yang nonpolar lebih "nyaman" dikelilingi CCl₄ yang juga nonpolar, sehingga pada konsentrasi yang sama potensial kimianya dalam CCl₄ jauh lebih rendah. Inilah prinsip ekstraksi pelarut, yang akan kita bahas secara kuantitatif di Bab 11.
:::

### Potensial kimia, suhu, dan tekanan

Karena $\mu_\text{J}$ adalah besaran molar parsial dari *G*, ia mewarisi sifat-sifat *G*. Dari (9.5), turunan campuran $\partial^2 G/\partial p\,\partial n_\text{J}$ dapat dihitung dalam dua urutan, dan keduanya harus sama (uji eksak subbab 3.6). Hasilnya dua hubungan yang meniru (7.9):

$$
\left(\frac{\partial\mu_\text{J}}{\partial p}\right)_{T,n} = V_\text{J} , \qquad \left(\frac{\partial\mu_\text{J}}{\partial T}\right)_{p,n} = -S_\text{J} . \qquad \text{(9.7)}
$$

Potensial kimia zat dalam campuran naik bila tekanan naik, dengan laju sama dengan volume molar parsialnya, dan turun bila suhu naik, dengan laju sama dengan entropi molar parsialnya. Hubungan pertama memberi cara "mengangkat" potensial kimia yang terlalu rendah, yaitu dengan menekan.

::: {.contoh}
**Contoh 9.7 · Tekanan untuk melawan osmosis**

Pada 25 °C, potensial kimia air dalam air laut sekitar 47,5 J mol⁻¹ lebih rendah daripada air murni (Bab 10 akan menunjukkan cara menghitungnya dari komposisi). Air laut dan air murni dipisahkan oleh membran yang hanya dapat dilewati air. (a) Ke arah mana air mengalir? (b) Berapa tekanan tambahan yang harus diberikan pada air laut agar aliran berhenti? Volume molar parsial air dalam air laut praktis 18,07 cm³ mol⁻¹.

**Penyelesaian.** (a) Dari air murni (μ tinggi) ke air laut (μ rendah).

(b) Tekanan tambahan Δ*p* pada air laut menaikkan μ air di sana sebesar $V_\text{air}\Delta p$ menurut (9.7), karena $V_\text{air}$ hampir tetap. Aliran berhenti bila kenaikan itu tepat menutup selisih:
$$
\Delta p = \frac{\Delta\mu}{V_\text{air}} = \frac{47{,}5\ \text{J mol}^{-1}}{18{,}07 \times 10^{-6}\ \text{m}^3\ \text{mol}^{-1}} = 2{,}63 \times 10^6\ \text{Pa} = 26\ \text{bar} .
$$

**Memahami hasil.** Tekanan ini disebut **tekanan osmotik** air laut; nilai terukurnya sekitar 27 bar. Selisih potensial kimia yang tampak kecil, kurang dari 50 J mol⁻¹, memerlukan tekanan setara dengan kolom air setinggi 260 m untuk dilawan. Pabrik desalinasi **osmosis balik** memberikan tekanan lebih besar lagi, 55–80 bar, supaya air mengalir dari air laut **ke** sisi air tawar, melawan arah alaminya.
:::

::: {.kuis}
**Kuis cepat 9.3** Dalam campuran gas, oksigen mempunyai potensial kimia lebih tinggi di tabung A daripada di tabung B, sedangkan nitrogen sebaliknya. Bila kedua tabung dihubungkan, bagaimana arah aliran masing-masing gas?
:::

## 9.4 Persamaan Gibbs–Duhem

Gambar 9.2 memperlihatkan bahwa volume molar parsial etanol dan air bergerak berlawanan arah. Apakah itu kebetulan untuk campuran ini? Tidak. Ia akibat langsung dari (9.3), dan berlaku untuk setiap besaran molar parsial, termasuk potensial kimia.

Kita mempunyai dua ungkapan untuk perubahan *G*. Dari $G = \sum n_\text{J}\mu_\text{J}$, aturan perkalian memberi
$$
dG = \sum_\text{J}\mu_\text{J}\,dn_\text{J} + \sum_\text{J}n_\text{J}\,d\mu_\text{J} .
$$
Dari persamaan fundamental (9.5), pada suhu dan tekanan tetap, $dG = \sum_\text{J}\mu_\text{J}\,dn_\text{J}$. Kedua ungkapan hanya dapat sama bila suku kedua pada yang pertama nol:

::: {.inti}
$$
\sum_\text{J}n_\text{J}\,d\mu_\text{J} = 0 \qquad (T, p\ \text{tetap}). \qquad \text{(9.8)}
$$
**Persamaan Gibbs–Duhem.** Potensial kimia komponen-komponen suatu campuran tidak dapat berubah secara bebas. Untuk campuran dua zat: $d\mu_\text{B} = -(n_\text{A}/n_\text{B})\,d\mu_\text{A}$.
:::

Arti fisisnya: bila komposisi campuran dua zat berubah sedikit dan potensial kimia A naik, potensial kimia B harus turun, dan sebaliknya. Lebih dari itu, besarnya perubahan diatur oleh perbandingan mol. Penurunan yang sama berlaku untuk setiap besaran molar parsial, sehingga untuk volume:

$$
n_\text{A}\,dV_\text{A} + n_\text{B}\,dV_\text{B} = 0 . \qquad \text{(9.9)}
$$

::: {.contoh}
**Contoh 9.8 · Memeriksa Gambar 9.2**

Pada $x_\text{etanol} = 0{,}30$, kemiringan kurva volume molar parsial pada Gambar 9.2 adalah $dV_\text{etanol}/dx_\text{etanol} = +5{,}27$ cm³ mol⁻¹ dan $dV_\text{air}/dx_\text{etanol} = -2{,}26$ cm³ mol⁻¹. Tunjukkan bahwa keduanya memenuhi persamaan Gibbs–Duhem.

**Penyelesaian.** Bagi (9.9) dengan *n* total dan dengan $dx_\text{etanol}$:
$$
x_\text{etanol}\frac{dV_\text{etanol}}{dx_\text{etanol}} + x_\text{air}\frac{dV_\text{air}}{dx_\text{etanol}} = (0{,}30)(5{,}27) + (0{,}70)(-2{,}26) = 1{,}581 - 1{,}582 \approx 0 .
$$

**Memahami hasil.** Kemiringan kurva air lebih kecil, tetapi dikalikan fraksi mol yang lebih besar, sehingga keduanya tepat saling meniadakan. Dalam praktik, persamaan Gibbs–Duhem dipakai dua arah: untuk **memeriksa** apakah data terukur konsisten secara termodinamika, dan untuk **menghitung** besaran molar parsial satu komponen bila komponen lain sudah diketahui.
:::

Gibbs–Duhem mempunyai akibat yang sangat penting bagi larutan encer. Bila B adalah zat terlarut dalam jumlah sedikit, $n_\text{A}/n_\text{B}$ sangat besar, sehingga perubahan kecil pada potensial kimia pelarut berarti perubahan besar pada potensial kimia zat terlarut.

::: {.contoh}
**Contoh 9.9 · Pelarut yang tenang, zat terlarut yang peka**

Dalam larutan dengan $x_\text{A} = 0{,}90$ dan $x_\text{B} = 0{,}10$, sedikit B ditambahkan sehingga potensial kimia pelarut A turun 50 J mol⁻¹. Berapa perubahan potensial kimia B?

**Penyelesaian.** Dari (9.8) dalam fraksi mol: $d\mu_\text{B} = -(x_\text{A}/x_\text{B})\,d\mu_\text{A} = -(0{,}90/0{,}10)(-50) = +450$ J mol⁻¹.

**Memahami hasil.** Potensial kimia zat terlarut berubah sembilan kali lebih banyak daripada pelarut. Bila larutan makin encer, perbandingan ini makin besar. Dalam bahasa sehari-hari: pelarut hampir "tidak merasakan" kehadiran zat terlarut, sedangkan zat terlarut sangat merasakan setiap perubahan konsentrasinya sendiri. Di Bab 10 kita akan melihat bahwa sifat-sifat koligatif, seperti penurunan titik beku, berasal dari perubahan kecil potensial kimia pelarut ini.
:::

::: {.terapan}
**Terapan: mengukur zat yang tidak menguap lewat pelarutnya.** Potensial kimia sukrosa dalam air tidak dapat diukur langsung, karena sukrosa tidak menguap. Tetapi potensial kimia **air** dalam larutan sukrosa dapat diukur dengan mudah, dari tekanan uap air di atas larutan pada berbagai konsentrasi. Persamaan Gibbs–Duhem kemudian diintegralkan untuk memperoleh potensial kimia sukrosa. Cara inilah yang dipakai untuk memperoleh sebagian besar data termodinamika gula, protein, dan polimer dalam larutan. Prinsip yang sama mendasari **osmometer tekanan uap**, alat untuk menentukan massa molar polimer dan biomolekul.
:::

::: {.dalam}
**Lebih dalam: bentuk lengkap Gibbs–Duhem.** Bila suhu dan tekanan juga boleh berubah, penurunan yang sama dengan (9.5) lengkap memberi
$$
S\,dT - V\,dp + \sum_\text{J}n_\text{J}\,d\mu_\text{J} = 0 .
$$
Untuk satu zat murni, bentuk ini menjadi $d\mu = -S_\text{m}\,dT + V_\text{m}\,dp$, yang sudah kita pakai untuk menurunkan persamaan Clapeyron. Persamaan ini juga menjelaskan aturan fasa: dari *C* + 2 variabel intensif (*T*, *p*, dan *C* potensial kimia), setiap fasa memberikan satu persamaan Gibbs–Duhem yang mengikat mereka, sehingga yang tersisa bebas adalah *C* + 2 − *P*. Itulah aturan fasa (8.9), yang akan kita pakai lagi di Bab 11.
:::

Persamaan Gibbs–Duhem juga dapat dipakai untuk **membangun** potensial kimia satu komponen dari komponen lain. Contoh berikut melakukannya, dan hasilnya akan menjadi titik awal Bab 10.

::: {.contoh}
**Contoh 9.10 · Dari pelarut ke zat terlarut**

Misalkan dalam suatu campuran dua zat, pada suhu dan tekanan tetap, potensial kimia A mengikuti $\mu_\text{A} = \mu_\text{A}^* + RT\ln x_\text{A}$ pada semua komposisi. Pakai persamaan Gibbs–Duhem untuk menentukan bentuk $\mu_\text{B}$.

**Rencana.** Nyatakan $d\mu_\text{A}$ dengan $dx_\text{A}$, pakai $d\mu_\text{B} = -(x_\text{A}/x_\text{B})\,d\mu_\text{A}$, lalu integralkan.

**Penyelesaian.** $d\mu_\text{A} = RT\,dx_\text{A}/x_\text{A}$. Maka
$$
d\mu_\text{B} = -\frac{x_\text{A}}{x_\text{B}}\cdot\frac{RT\,dx_\text{A}}{x_\text{A}} = -\frac{RT\,dx_\text{A}}{x_\text{B}} = \frac{RT\,dx_\text{B}}{x_\text{B}} ,
$$
karena $dx_\text{A} = -dx_\text{B}$. Integralkan: $\mu_\text{B} = \text{tetapan} + RT\ln x_\text{B}$. Pada $x_\text{B} = 1$ (B murni), $\mu_\text{B} = \mu_\text{B}^*$, sehingga tetapannya $\mu_\text{B}^*$:
$$
\mu_\text{B} = \mu_\text{B}^* + RT\ln x_\text{B} .
$$

**Memahami hasil.** Bila satu komponen mengikuti hukum logaritma ini di seluruh rentang komposisi, komponen lain **harus** mengikutinya juga. Campuran seperti itu disebut **larutan ideal**, dan rumus $\mu = \mu^* + RT\ln x$ akan menjadi alat utama Bab 10. Perhatikan kemiripannya dengan (9.11) untuk gas: fraksi mol dalam larutan memainkan peran yang sama dengan tekanan parsial dalam gas.
:::

::: {.kuis}
**Kuis cepat 9.4** Seorang mahasiswa melaporkan bahwa dalam campuran dua cairan, ketika fraksi mol B dinaikkan, volume molar parsial A dan B **keduanya** naik. Apakah laporannya mungkin benar?
:::
