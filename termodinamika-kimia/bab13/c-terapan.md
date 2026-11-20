## 13.6 Ketergantungan *E* pada suhu: ΔS dan ΔH dari pengukuran sel

Karena $\Delta_\text{r}G = -nFE$, semua sifat energi Gibbs dapat diterjemahkan menjadi sifat tegangan sel. Yang paling berguna adalah turunan terhadap suhu. Dari (7.9), $(\partial\Delta_\text{r}G/\partial T)_p = -\Delta_\text{r}S$. Dengan $\Delta_\text{r}G = -nFE$:

::: {.inti}
$$
\Delta_\text{r}S = nF\left(\frac{\partial E}{\partial T}\right)_p , \qquad \Delta_\text{r}H = \Delta_\text{r}G + T\Delta_\text{r}S = -nF\left[E - T\left(\frac{\partial E}{\partial T}\right)_p\right] . \qquad \text{(13.6)}
$$
**Entropi dan entalpi reaksi dari tegangan sel.** Cukup mengukur *E* pada beberapa suhu: kemiringannya memberi Δ*S*, dan bersama *E* sendiri memberi Δ*H*.
:::

Ini cara yang sangat elegan: tiga besaran termodinamika utama sebuah reaksi, $\Delta_\text{r}G$, $\Delta_\text{r}S$, dan $\Delta_\text{r}H$, diperoleh dari voltmeter dan termometer saja, tanpa kalorimeter. Dan karena tegangan dapat diukur sangat teliti, hasilnya sering lebih baik daripada pengukuran kalorimetri langsung.

![Gambar 13.3 Potensial standar sel Pt|H₂|HCl|AgCl|Ag terhadap suhu (titik: pengukuran klasik Bates dan Bower; kurva: polinom kuadrat). Garis putus-putus adalah garis singgung di 25 °C, yang kemiringannya memberi $\Delta_\text{r}S^\circ$.](fig/ET.png){width=70%}

::: {.contoh}
**Contoh 13.10 · Termodinamika lengkap dari satu sel**

Untuk sel Pt|H₂|HCl|AgCl|Ag (reaksi $\tfrac12\text{H}_2 + \text{AgCl} \rightarrow \text{Ag} + \text{H}^+ + \text{Cl}^-$, *n* = 1), $E^\circ = 0{,}2224$ V dan $dE^\circ/dT = -0{,}637$ mV K⁻¹ pada 25 °C (Gambar 13.3). Hitung $\Delta_\text{r}G^\circ$, $\Delta_\text{r}S^\circ$, dan $\Delta_\text{r}H^\circ$, lalu bandingkan dengan tabel: $\Delta_\text{f}H^\circ$ AgCl(s) = −127,07 dan HCl(aq) = −167,16 kJ mol⁻¹.

**Penyelesaian.**
$$
\Delta_\text{r}G^\circ = -(96\,485)(0{,}2224) = -21{,}46\ \text{kJ mol}^{-1} ,
$$
$$
\Delta_\text{r}S^\circ = (96\,485)(-6{,}37 \times 10^{-4}) = -61{,}5\ \text{J K}^{-1}\text{mol}^{-1} ,
$$
$$
\Delta_\text{r}H^\circ = -21{,}46 + (298{,}15)(-0{,}0615) = -39{,}8\ \text{kJ mol}^{-1} .
$$
Dari tabel: $\Delta_\text{r}H^\circ = -167{,}16 - (-127{,}07) = -40{,}1$ kJ mol⁻¹.

**Memahami hasil.** Selisihnya hanya 0,3 kJ mol⁻¹, kurang dari 1%. Entropi reaksi negatif: setengah mol gas H₂ hilang dan ion-ion yang terbentuk menata molekul air di sekitarnya. Karena tegangan turun ketika suhu naik, sel ini memberi kerja listrik sedikit lebih kecil pada hari panas.
:::

Ada akibat menarik dari (13.6). Bila sel bekerja secara reversibel, kerja listrik yang diberikannya adalah $-\Delta_\text{r}G$, dan kalor yang dipertukarkannya dengan lingkungan adalah $q_\text{rev} = T\Delta_\text{r}S$. Untuk sel dengan $dE/dT$ negatif, seperti di atas, sel melepaskan kalor walaupun bekerja sempurna. Untuk sel dengan $dE/dT$ positif, sel menyerap kalor dari lingkungan dan mengubahnya menjadi listrik, sehingga kerja listriknya **melebihi** $-\Delta_\text{r}H$, seperti pembakaran glukosa di Bab 7.

::: {.contoh}
**Contoh 13.11 · Kalor dari sel yang bekerja sempurna dan yang dihubung pendek**

Untuk sel pada Contoh 13.10, hitung kalor yang dilepaskan per mol reaksi bila sel (a) bekerja secara reversibel, (b) dihubung pendek sehingga tidak ada kerja listrik yang dilakukan.

**Penyelesaian.** (a) $q_\text{rev} = T\Delta_\text{r}S^\circ = (298{,}15)(-61{,}5) = -18{,}3$ kJ mol⁻¹: sel melepaskan 18,3 kJ kalor sambil memberikan 21,5 kJ kerja listrik.

(b) Tanpa kerja listrik, seluruh perubahan entalpi keluar sebagai kalor: $q = \Delta_\text{r}H^\circ = -39{,}8$ kJ mol⁻¹.

**Memahami hasil.** Jumlah kerja dan kalor pada (a), 21,5 + 18,3 = 39,8 kJ, sama dengan kalor pada (b): hukum pertama terpenuhi. Hubung pendek "membuang" 21,5 kJ yang seharusnya dapat menjadi kerja, dan mengubahnya menjadi kalor. Baterai yang dihubung pendek menjadi panas karena alasan ini, dan pada baterai litium yang besar, panas itu dapat memicu kebakaran.
:::

::: {.kuis}
**Kuis cepat 13.6** Bila potensial suatu sel tidak bergantung pada suhu, berapa $\Delta_\text{r}S$-nya? Apa hubungan $\Delta_\text{r}G$ dan $\Delta_\text{r}H$-nya?
:::

## 13.7 Sel konsentrasi dan pengukuran pH

Sel tidak harus memakai dua zat yang berbeda. Dua elektrode yang sama dalam larutan dengan konsentrasi berbeda juga menghasilkan tegangan, karena zat cenderung berpindah dari konsentrasi tinggi ke rendah. Sel seperti ini disebut **sel konsentrasi**. Untuk $\text{Ag}\,|\,\text{Ag}^+(a_1)\,\|\,\text{Ag}^+(a_2)\,|\,\text{Ag}$, reaksi selnya adalah $\text{Ag}^+(a_2) \rightarrow \text{Ag}^+(a_1)$, dengan *E*° = 0, sehingga

$$
E = -\frac{RT}{F}\ln\frac{a_1}{a_2} = \frac{RT}{F}\ln\frac{a_2}{a_1} . \qquad \text{(13.7)}
$$

Tegangan sel konsentrasi berasal sepenuhnya dari entropi pencampuran: dorongan untuk menyamakan konsentrasi diubah menjadi kerja listrik. Inilah jawaban Kuis 13.5: sel dengan *E*° = 0 tetap dapat menghasilkan listrik bila *Q* ≠ 1.

::: {.contoh}
**Contoh 13.12 · Sel konsentrasi perak**

Hitung potensial sel $\text{Ag}\,|\,\text{AgNO}_3(0{,}010\ \text{mol L}^{-1})\,\|\,\text{AgNO}_3(1{,}0\ \text{mol L}^{-1})\,|\,\text{Ag}$ pada 25 °C, dengan anggapan aktivitas sama dengan konsentrasi.

**Penyelesaian.** $E = (0{,}059\,16)\log(1{,}0/0{,}010) = 0{,}118$ V. Elektrode dalam larutan encer adalah anode: perak larut di sana dan mengendap di elektrode dalam larutan pekat.

**Memahami hasil.** Perbedaan konsentrasi seratus kali hanya memberi 0,12 V. Dalam pengukuran teliti, aktivitas harus dipakai: koefisien aktivitas AgNO₃ 1 mol L⁻¹ jauh di bawah satu, sehingga tegangan terukur lebih kecil. Sebaliknya, sel konsentrasi adalah cara klasik **mengukur** koefisien aktivitas ion, dengan membandingkan tegangan terukur dengan ramalan (13.7).
:::

Di dalam tubuh, sel konsentrasi bekerja di setiap sel saraf. Membran sel saraf lebih mudah dilewati ion K⁺ daripada ion lain, dan di dalam sel [K⁺] sekitar 140 mmol L⁻¹, sedangkan di luar sekitar 5 mmol L⁻¹. Ion K⁺ cenderung keluar menuruni gradien konsentrasinya, tetapi setiap ion yang keluar meninggalkan muatan negatif di dalam, sehingga terbentuk beda potensial yang menahan keluarnya K⁺ berikutnya. Kesetimbangan tercapai ketika beda potensial listrik tepat mengimbangi selisih potensial kimia: inilah **potensial Nernst**.

::: {.contoh}
**Contoh 13.13 · Tegangan sel saraf**

Hitung potensial Nernst untuk K⁺ di membran sel saraf pada 37 °C, dengan $[\text{K}^+]_\text{dalam} = 140$ dan $[\text{K}^+]_\text{luar} = 5{,}0$ mmol L⁻¹. Lakukan hal yang sama untuk Na⁺, dengan $[\text{Na}^+]_\text{dalam} = 12$ dan $[\text{Na}^+]_\text{luar} = 145$ mmol L⁻¹.

**Penyelesaian.** Potensial bagian dalam terhadap luar pada kesetimbangan untuk ion bermuatan +1: $E = (RT/F)\ln([\text{luar}]/[\text{dalam}])$, dengan $RT/F = 26{,}73$ mV pada 310 K.

K⁺: $E = (26{,}73)\ln(5{,}0/140) = -89$ mV. Na⁺: $E = (26{,}73)\ln(145/12) = +67$ mV.

**Memahami hasil.** Potensial istirahat sel saraf terukur sekitar −70 mV, dekat potensial Nernst K⁺, karena dalam keadaan istirahat membran terutama terbuka bagi K⁺. Ketika impuls saraf datang, saluran Na⁺ tiba-tiba terbuka, dan potensial membran melompat menuju +67 mV, potensial Nernst Na⁺. Lompatan itu, yang merambat sepanjang akson, adalah sinyal saraf. Pompa natrium–kalium, yang memakai ATP (Bab 12), terus mengembalikan perbedaan konsentrasi itu. Setiap pikiran kita adalah sel konsentrasi yang dinyalakan dan dimatikan.
:::

### Mengukur pH

Elektrode hidrogen memberi potensial yang bergantung langsung pada pH: $E = -0{,}059\,16\ \text{pH}$ pada 25 °C. Tetapi elektrode hidrogen merepotkan: memerlukan gas H₂ dan permukaan platina yang mudah teracuni. Dalam praktik dipakai **elektrode kaca**: membran kaca tipis khusus yang permukaannya menukar ion H⁺ dengan larutan. Beda aktivitas H⁺ di kedua sisi membran menghasilkan potensial seperti sel konsentrasi. Elektrode kaca dipasangkan dengan elektrode pembanding (biasanya Ag|AgCl), dan potensial selnya

$$
E = \text{tetapan} - 0{,}059\,16\ \text{V} \times \text{pH} \quad (25\ ^\circ\text{C}) . \qquad \text{(13.8)}
$$

Tetapan itu berbeda untuk setiap elektrode dan berubah perlahan, sehingga pH meter harus **dikalibrasi** dengan larutan penyangga yang pH-nya diketahui, biasanya dua penyangga (misalnya pH 4,01 dan 7,00) untuk menetapkan tetapan dan kemiringannya.

::: {.contoh}
**Contoh 13.14 · Membaca pH meter**

Pada 25 °C, sebuah pH meter menunjukkan 0,4120 V dalam penyangga pH 7,00. Dalam sampel, tegangannya 0,5890 V. Berapa pH sampel?

**Penyelesaian.** Dari (13.8), selisih tegangan $0{,}5890 - 0{,}4120 = 0{,}1770$ V. Karena *E* naik ketika pH turun: $\Delta\text{pH} = -0{,}1770/0{,}059\,16 = -2{,}99$. pH sampel = 7,00 − 2,99 = 4,01.

**Memahami hasil.** Satu satuan pH setara 59 mV. Untuk mengukur pH sampai 0,01, tegangan harus diukur sampai 0,6 mV, dan suhu harus diperhatikan, karena kemiringan $RT\ln10/F$ berubah 0,2 mV per derajat per satuan pH. pH meter yang baik menyertakan sensor suhu untuk mengoreksinya secara otomatis.
:::

::: {.kuis}
**Kuis cepat 13.7** Mengapa pH meter yang dikalibrasi pada 25 °C memberi pembacaan yang salah bila sampelnya pada 40 °C, walaupun tetapannya tidak berubah?
:::

## 13.8 Baterai dan sel bahan bakar

Baterai adalah sel elektrokimia yang dikemas. Termodinamika menentukan dua angka terpentingnya: **tegangan** (dari *E*° dan Nernst) dan **energi spesifik** maksimum, yaitu $-\Delta_\text{r}G$ dibagi massa pereaksi. Kimia bahan, teknik, dan laju reaksi menentukan seberapa dekat baterai nyata mendekati batas itu.

::: {.contoh}
**Contoh 13.15 · Aki timbal dan baterai litium**

(a) Aki kendaraan memakai reaksi $\text{Pb} + \text{PbO}_2 + 2\text{H}_2\text{SO}_4 \rightarrow 2\text{PbSO}_4 + 2\text{H}_2\text{O}$. Hitung *E*° dari Tabel 13.1 dan energi spesifik teoretisnya dalam Wh kg⁻¹, dihitung terhadap massa pereaksi. (b) Baterai litium-ion memakai reaksi $\text{LiC}_6 + \text{CoO}_2 \rightarrow \text{C}_6 + \text{LiCoO}_2$ dengan tegangan sekitar 3,7 V. Hitung energi spesifik teoretisnya dengan cara yang sama.

**Penyelesaian.** (a) $E^\circ = 1{,}691 - (-0{,}359) = 2{,}050$ V, *n* = 2. $-\Delta_\text{r}G^\circ = (2)(96\,485)(2{,}050) = 395{,}6$ kJ per mol reaksi. Massa pereaksi: $207{,}2 + 239{,}2 + 2(98{,}08) = 642{,}6$ g. Energi spesifik: $395{,}6/0{,}6426 = 615{,}6$ kJ kg⁻¹ $= 171$ Wh kg⁻¹ (1 Wh = 3,6 kJ).

(b) *n* = 1: $(96\,485)(3{,}7) = 357$ kJ per mol. Massa pereaksi: $72{,}06 + 6{,}94 + 90{,}93 = 169{,}9$ g. Energi spesifik: $357/0{,}1699 = 2101$ kJ kg⁻¹ $= 584$ Wh kg⁻¹.

**Memahami hasil.** Baterai litium unggul karena dua alasan sekaligus: litium adalah logam paling ringan dan paling elektropositif (*E*° paling negatif), sehingga tegangannya hampir dua kali aki timbal, sementara massa per elektron yang dipindahkan jauh lebih kecil. Aki timbal nyata hanya mencapai 30–40 Wh kg⁻¹ dan baterai litium-ion 150–270 Wh kg⁻¹, karena massa wadah, elektrolit, dan penghantar, serta karena tidak seluruh bahan aktif dapat dipakai tanpa merusak elektrode.
:::

**Sel bahan bakar** berbeda dari baterai karena pereaksinya dipasok terus dari luar. Sel bahan bakar hidrogen memakai reaksi $\text{H}_2 + \tfrac12\text{O}_2 \rightarrow \text{H}_2\text{O}(l)$ dengan *E*° = 1,229 V, yang di Bab 7 kita lihat terbatas pada 83% dari entalpi pembakaran. Di sini kita dapat melihat batas itu dari sisi tegangan. Entalpi pembakaran hidrogen, 285,83 kJ mol⁻¹, dinyatakan sebagai tegangan disebut **tegangan termonetral**: $\Delta_\text{r}H/nF = 285\,830/(2 \times 96\,485) = 1{,}481$ V. Efisiensi sel bahan bakar yang bekerja pada tegangan *V* terhadap entalpi bahan bakarnya adalah *V*/1,481.

::: {.contoh}
**Contoh 13.16 · Sel bahan bakar dan elektroliser**

(a) Sel bahan bakar hidrogen kendaraan bekerja pada sekitar 0,70 V per sel ketika menarik arus besar. Hitung efisiensinya terhadap entalpi pembakaran dan terhadap $\Delta_\text{r}G$. (b) Untuk membuat hidrogen dengan elektrolisis air, elektroliser industri bekerja pada sekitar 1,8 V. Hitung energi listrik per kilogram hidrogen, dan bandingkan dengan batas minimum termodinamika (1,229 V).

**Penyelesaian.** (a) Terhadap entalpi: 0,70/1,481 = 47%. Terhadap energi Gibbs: 0,70/1,229 = 57%.

(b) Per mol H₂ diperlukan muatan 2*F*. Pada 1,8 V: $(2)(96\,485)(1{,}8) = 347$ kJ per mol, atau per kilogram $347/0{,}002\,016 = 1{,}72 \times 10^5$ kJ = 47,9 kWh. Pada batas 1,229 V: 32,7 kWh kg⁻¹.

**Memahami hasil.** Sel bahan bakar kehilangan hampir separuh energinya sebagai kalor, karena reaksi di elektrode memerlukan "dorongan" tegangan tambahan supaya berjalan cukup cepat (disebut **overpotensial**), dan karena hambatan di dalam sel. Hal yang sama terjadi terbalik di elektroliser. Bila hidrogen dibuat dengan elektrolisis lalu dipakai di sel bahan bakar, hanya sekitar $0{,}70/1{,}8 = 39\%$ listrik awal yang kembali. Kehilangan ini, bukan batas termodinamika, adalah tantangan utama teknologi "hidrogen hijau". Termodinamika memberi batasnya; elektrokatalisis menentukan seberapa dekat kita mencapainya.
:::

::: {.terapan}
**Terapan: korosi dan perlindungan katodik.** Korosi besi adalah sel elektrokimia yang tidak kita inginkan. Di satu bagian permukaan, besi teroksidasi ($\text{Fe} \rightarrow \text{Fe}^{2+} + 2\text{e}^-$); di bagian lain, oksigen terlarut tereduksi ($\text{O}_2 + 2\text{H}_2\text{O} + 4\text{e}^- \rightarrow 4\text{OH}^-$). Pada pH 7, potensial setengah sel oksigen adalah 1,229 − 0,414 = 0,815 V, sehingga tegangan "sel korosi" sekitar 0,815 − (−0,447) = 1,26 V: sangat spontan. Air laut mempercepatnya karena ion-ionnya menghantarkan listrik dengan baik. Seng dapat melindungi besi karena *E*°-nya lebih negatif: bila keduanya bersentuhan, seng yang teroksidasi lebih dulu dan besi menjadi katode yang terlindung. Itulah prinsip besi galvanis (seng tetap melindungi walaupun lapisannya tergores) dan **anode korban**, blok seng atau magnesium yang dipasang di lambung kapal, tiang dermaga, dan pipa bawah tanah, lalu diganti ketika habis.
:::

::: {.kuis}
**Kuis cepat 13.8** Mengapa lapisan timah pada kaleng melindungi besi selama utuh, tetapi mempercepat karat bila tergores, sedangkan lapisan seng tidak?
:::

## Penutup: satu fungsi, banyak wajah

Kita memulai buku ini dengan molekul gas yang bergerak acak di dalam wadah, dan mengakhirinya dengan sinyal di sel saraf dan baterai di telepon genggam. Di antara keduanya, hampir setiap gejala yang kita bahas dapat ditelusuri ke satu besaran: energi Gibbs, dan turunannya, potensial kimia.

Hukum pertama memberi kita neraca energi: kalor dan kerja tidak hilang. Hukum kedua memberi arah: entropi alam semesta tidak berkurang. Energi Gibbs menggabungkan keduanya menjadi satu kriteria yang hanya memerlukan sifat sistem, dan potensial kimia memecahnya menjadi sumbangan setiap zat. Dari sana muncul semuanya: titik didih yang turun di gunung, es yang mencair ketika ditekan, garam yang menurunkan titik beku, osmosis yang memecah sel darah, distilasi yang memisahkan minyak bumi, kesetimbangan yang memberi makan dunia, dan tegangan sel yang mengukur semuanya dengan sebuah voltmeter.

Termodinamika mempunyai satu keterbatasan yang sudah kita temui berulang kali: ia mengatakan ke mana proses **dapat** berjalan, tetapi tidak seberapa cepat. Intan seharusnya berubah menjadi grafit, benzena seharusnya terurai, dan kayu di udara seharusnya terbakar; semuanya tidak terjadi karena **laju**. Pertanyaan tentang laju, tentang mengapa reaksi memerlukan energi aktivasi dan bagaimana katalis bekerja, adalah pokok buku berikutnya dalam seri ini: *Kimia Fisika 2: Kinetika Kimia*.
