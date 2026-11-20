## 7.7 Ketergantungan G pada suhu: persamaan Gibbs–Helmholtz

Dari (7.9) kita tahu bahwa $(\partial G/\partial T)_p = -S$. Rumus ini benar tetapi kurang praktis untuk reaksi kimia, karena kita lebih sering mengetahui entalpi reaksi daripada entropinya. Dapatkah ketergantungan *G* pada suhu dinyatakan dengan *H*?

Bisa, dengan memandang *G*/*T* sebagai ganti *G*. Turunan hasil bagi memberi

$$
\left(\frac{\partial (G/T)}{\partial T}\right)_p = \frac{1}{T}\left(\frac{\partial G}{\partial T}\right)_p - \frac{G}{T^2} = -\frac{S}{T} - \frac{G}{T^2} = -\frac{TS + G}{T^2} .
$$

Karena $G + TS = H$, pembilang ini tidak lain adalah *H*:

::: {.inti}
$$
\left(\frac{\partial (G/T)}{\partial T}\right)_p = -\frac{H}{T^2} \qquad \text{(7.12)}
$$
**Persamaan Gibbs–Helmholtz.** Untuk reaksi, berlaku hal yang sama dengan Δ*G* dan Δ*H*.
:::

Bila $\Delta H$ dianggap tidak bergantung pada suhu, persamaan ini dapat diintegralkan dari $T_1$ ke $T_2$:

$$
\frac{\Delta G(T_2)}{T_2} = \frac{\Delta G(T_1)}{T_1} + \Delta H\left(\frac{1}{T_2} - \frac{1}{T_1}\right) . \qquad \text{(7.13)}
$$

Mengapa bentuk ini lebih berguna daripada $\Delta G = \Delta H - T\Delta S$? Hasil keduanya sama bila Δ*H* dan Δ*S* dianggap tetap, tetapi (7.12) menunjukkan sesuatu yang lebih dalam: **perubahan Δ*G*/*T* terhadap suhu hanya ditentukan oleh entalpi reaksi**. Di Bab 12, karena $\Delta G^\circ/T = -R\ln K$, persamaan ini akan berubah menjadi persamaan van 't Hoff, yang menjelaskan mengapa tetapan kesetimbangan reaksi eksoterm turun bila suhu naik.

::: {.contoh}
**Contoh 7.14 · Sintesis amonia pada 500 K**

Untuk $\text{N}_2(g) + 3\text{H}_2(g) \to 2\text{NH}_3(g)$, $\Delta_\text{r}G^\circ(298\ \text{K}) = -32{,}90$ kJ mol⁻¹ dan $\Delta_\text{r}H^\circ = -92{,}22$ kJ mol⁻¹. Hitung $\Delta_\text{r}G^\circ$ pada 500 K dengan (7.13).

**Penyelesaian.**
$$
\frac{\Delta G(500)}{500} = \frac{-32{,}90}{298{,}15} + (-92{,}22)\left(\frac{1}{500} - \frac{1}{298{,}15}\right) = -0{,}1103 + 0{,}1249 = +0{,}0145\ \text{kJ K}^{-1}\text{mol}^{-1} ,
$$
sehingga $\Delta_\text{r}G^\circ(500\ \text{K}) = +7{,}3$ kJ mol⁻¹.

**Memahami hasil.** Pada suhu kamar sintesis amonia standar spontan, tetapi pada 500 K tidak lagi: Δ*G*° berganti tanda di sekitar 464 K (Bab 6, Soal 42). Hasil yang sama diperoleh dari $\Delta H - T\Delta S = -92{,}22 - (500)(-0{,}1988) = +7{,}2$ kJ mol⁻¹, dalam batas pembulatan. Reaksi eksoterm yang mengurangi jumlah gas selalu menjadi kurang menguntungkan pada suhu tinggi, dan Haber harus berkompromi antara laju (memerlukan suhu tinggi) dan hasil (memerlukan suhu rendah).
:::

::: {.kuis}
**Kuis cepat 7.7** Untuk reaksi endoterm, apakah Δ*G*/*T* bertambah atau berkurang bila suhu dinaikkan?
:::

## 7.8 Ketergantungan G pada tekanan

Hasil kedua (7.9), $(\partial G/\partial p)_T = V$, mengatakan bahwa *G* selalu naik bila tekanan naik, sebanding dengan volume. Seberapa banyak? Jawabannya sangat berbeda untuk fasa terkondensasi dan untuk gas, dan perbedaan itulah yang mendasari banyak gejala kimia.

**Cairan dan padatan.** Volume hampir tidak berubah dengan tekanan, sehingga integralnya sederhana:

$$
\Delta G = V\Delta p . \qquad \text{(7.14)}
$$

Volume molar cairan dan padatan kecil (puluhan cm³ mol⁻¹), sehingga perubahan *G* terhadap tekanan sangat kecil kecuali pada tekanan yang sangat tinggi.

**Gas ideal.** Volume bergantung kuat pada tekanan, $V = nRT/p$, sehingga

$$
\Delta G = \int_{p_1}^{p_2}\frac{nRT}{p}\,dp = nRT\ln\frac{p_2}{p_1} . \qquad \text{(7.15)}
$$

Bila $p_1$ adalah tekanan standar $p^\circ = 1$ bar, energi Gibbs molar gas ideal pada tekanan sembarang *p* adalah

::: {.inti}
$$
G_\text{m}(p) = G_\text{m}^\circ + RT\ln\frac{p}{p^\circ} \qquad \text{(7.16)}
$$
Energi Gibbs molar gas ideal naik secara logaritmik terhadap tekanan.
:::

Persamaan (7.16) mungkin tampak sederhana, tetapi ia adalah salah satu yang terpenting di seluruh termodinamika kimia. Di Bab 9 ia akan menjadi rumus potensial kimia, dan di Bab 12 suku logaritmanya akan berubah menjadi tetapan kesetimbangan.

::: {.contoh}
**Contoh 7.15 · Air dan uap di bawah tekanan**

Hitung kenaikan energi Gibbs molar pada 25 °C bila tekanan dinaikkan dari 1 bar ke 1000 bar untuk (a) air cair ($V_\text{m} = 18{,}07$ cm³ mol⁻¹), (b) gas ideal.

**Penyelesaian.** (a) $\Delta G_\text{m} = (18{,}07 \times 10^{-6}\ \text{m}^3)(999 \times 10^5\ \text{Pa}) = 1{,}81$ kJ mol⁻¹. (b) $\Delta G_\text{m} = RT\ln1000 = (8{,}314)(298{,}15)(6{,}908)$ J mol⁻¹ $= 17{,}1$ kJ mol⁻¹.

**Memahami hasil.** Untuk tekanan yang sama, *G* gas naik hampir sepuluh kali lebih banyak daripada *G* cairan, dan untuk tekanan sedang perbedaannya jauh lebih besar lagi. Inilah sebabnya tekanan tinggi mendorong gas menjadi cairan: memampatkan gas menaikkan *G*-nya jauh lebih cepat, sampai pada suatu tekanan *G* cairan menjadi lebih rendah dan gas mengembun. Perhitungan kuantitatifnya adalah persamaan Clapeyron di Bab 8.
:::

::: {.contoh}
**Contoh 7.16 · Membuat intan dari grafit**

Pada 298 K, $\Delta_\text{r}G^\circ = +2{,}90$ kJ mol⁻¹ untuk C(grafit) → C(intan): pada 1 bar, intan tidak stabil. Massa jenis grafit 2,267 g cm⁻³ dan intan 3,513 g cm⁻³. Taksir tekanan yang diperlukan agar intan menjadi stabil pada 298 K.

**Rencana.** Intan lebih rapat, sehingga volume molarnya lebih kecil. Menaikkan tekanan menaikkan *G* grafit lebih banyak daripada *G* intan, sehingga Δ*G* reaksi turun. Cari tekanan ketika Δ*G* = 0.

**Penyelesaian.** $V_\text{m}$(grafit) $= 12{,}011/2{,}267 = 5{,}298$ cm³ mol⁻¹, $V_\text{m}$(intan) $= 3{,}419$ cm³ mol⁻¹, sehingga $\Delta V_\text{m} = -1{,}879$ cm³ mol⁻¹. Dari (7.14) untuk reaksi, $\Delta G(p) = \Delta G^\circ + \Delta V(p - p^\circ)$. Δ*G* = 0 bila
$$
p - p^\circ = \frac{-\Delta G^\circ}{\Delta V} = \frac{-2900\ \text{J mol}^{-1}}{-1{,}879 \times 10^{-6}\ \text{m}^3\text{mol}^{-1}} = 1{,}54 \times 10^9\ \text{Pa} \approx 15\ \text{kbar} .
$$

**Memahami hasil.** Sekitar lima belas ribu atmosfer. Intan sintetis industri dibuat pada tekanan sekitar 50–60 kbar dan suhu 1500–2000 °C, jauh di atas batas termodinamika ini, karena pada suhu kamar perubahan grafit menjadi intan sangat lambat; suhu tinggi diperlukan untuk lajunya, dan suhu tinggi menggeser tekanan kesetimbangan ke atas. Di dalam Bumi, intan alam terbentuk pada kedalaman lebih dari 150 km, tempat tekanan dan suhu seperti itu terjadi secara alami.
:::

::: {.contoh}
**Contoh 7.17 · Tekanan uap air dari tabel energi Gibbs**

Untuk $\text{H}_2\text{O}(l) \to \text{H}_2\text{O}(g)$ pada 298,15 K, $\Delta_\text{vap}G^\circ = +8{,}55$ kJ mol⁻¹. Pada tekanan uap berapa air cair dan uapnya berada dalam kesetimbangan?

**Penyelesaian.** *G* cairan hampir tidak bergantung pada tekanan, sedangkan $G_\text{m}$ uap mengikuti $G_\text{m}^\circ + RT\ln(p/p^\circ)$. Kesetimbangan berarti $\Delta G = 0$:
$$
0 = \Delta_\text{vap}G^\circ + RT\ln\frac{p}{p^\circ} \quad\Rightarrow\quad p = p^\circ\exp\left(-\frac{\Delta_\text{vap}G^\circ}{RT}\right) = (1\ \text{bar})\exp\left(-\frac{8550}{(8{,}314)(298{,}15)}\right) = 0{,}0317\ \text{bar} .
$$

**Memahami hasil.** Hasilnya 3,17 kPa, tepat tekanan uap air pada 25 °C yang tercantum di tabel. $\Delta_\text{vap}G^\circ$ positif **tidak** berarti air tidak menguap; artinya air tidak menguap menjadi uap **bertekanan 1 bar**. Selama tekanan parsial uap di udara di bawah 3,17 kPa, Δ*G* penguapan negatif dan air di gelas terbuka terus menguap. Bab 8 dan Bab 12 mengembangkan gagasan ini: kesetimbangan tercapai ketika suku $RT\ln p$ tepat menghapus $\Delta G^\circ$.
:::

::: {.kuis}
**Kuis cepat 7.8** Es kurang rapat daripada air cair. Bila tekanan dinaikkan pada 0 °C, fasa mana yang *G*-nya naik lebih banyak? Apa akibatnya bagi titik leleh es?
:::

## 7.9 Energi bebas Gibbs reaksi standar

Seperti entalpi, energi Gibbs reaksi standar dapat dihitung dari tabel. **Energi Gibbs pembentukan standar** $\Delta_\text{f}G^\circ$ adalah energi Gibbs reaksi standar untuk membentuk satu mol zat dari unsur-unsurnya dalam keadaan acuan. Seperti entalpi pembentukan, ia bernilai nol untuk unsur dalam keadaan acuannya. Maka

::: {.inti}
$$
\Delta_\text{r}G^\circ = \sum_\text{hasil}\nu\,\Delta_\text{f}G^\circ - \sum_\text{pereaksi}\nu\,\Delta_\text{f}G^\circ \qquad \text{(7.17)}
$$
:::

Cara kedua adalah menghitung $\Delta_\text{r}H^\circ$ dari Tabel 4.1 dan $\Delta_\text{r}S^\circ$ dari Tabel 6.1, lalu memakai (7.5). Kedua cara memberi hasil yang sama, karena tabel $\Delta_\text{f}G^\circ$ memang disusun dengan cara kedua.

| Zat | $\Delta_\text{f}G^\circ$ (kJ mol⁻¹) | Zat | $\Delta_\text{f}G^\circ$ (kJ mol⁻¹) |
|---|---|---|---|
| H₂O(l) | −237,13 | CH₄(g) | −50,72 |
| H₂O(g) | −228,57 | NH₃(g) | −16,45 |
| CO₂(g) | −394,36 | NO(g) | +86,55 |
| CO(g) | −137,17 | NO₂(g) | +51,31 |
| CaCO₃(s) | −1128,8 | O₃(g) | +163,2 |
| CaO(s) | −604,03 | C(intan) | +2,90 |
| C₂H₅OH(l) | −174,78 | C₆H₆(l) | +124,3 |

Tabel 7.1 Energi Gibbs pembentukan standar pada 298,15 K.

Tanda $\Delta_\text{f}G^\circ$ memberi informasi tentang **kestabilan termodinamika** senyawa terhadap unsur-unsurnya. Senyawa dengan $\Delta_\text{f}G^\circ$ negatif, seperti air dan CO₂, stabil: mereka tidak terurai dengan sendirinya menjadi unsur. Senyawa dengan $\Delta_\text{f}G^\circ$ positif, seperti NO, ozon, dan benzena, secara termodinamika cenderung terurai menjadi unsur-unsurnya. Bahwa benzena tetap bertahan di botol laboratorium menunjukkan sekali lagi bahwa termodinamika hanya berbicara tentang arah, bukan laju: senyawa-senyawa itu **stabil secara kinetik**, karena penguraiannya memerlukan pemutusan ikatan dengan penghalang energi yang tinggi.

::: {.contoh}
**Contoh 7.18 · Memeriksa konsistensi tabel**

Hitung $\Delta_\text{f}G^\circ$ H₂O(l) dari $\Delta_\text{f}H^\circ = -285{,}83$ kJ mol⁻¹ dan entropi molar standar (Tabel 6.1), lalu bandingkan dengan Tabel 7.1.

**Penyelesaian.** $\Delta_\text{f}S^\circ = 69{,}91 - 130{,}68 - \tfrac12(205{,}14) = -163{,}34$ J K⁻¹ mol⁻¹. Maka $\Delta_\text{f}G^\circ = -285{,}83 - (298{,}15)(-0{,}163\,34) = -237{,}13$ kJ mol⁻¹, sama persis dengan tabel.

**Memahami hasil.** Ketiga tabel, entalpi pembentukan, entropi mutlak, dan energi Gibbs pembentukan, saling terikat oleh $G = H - TS$. Bila dua di antaranya diketahui, yang ketiga dapat dihitung. Kecocokan sempurna ini juga menjadi cara memeriksa salah ketik dalam tabel.
:::

::: {.contoh}
**Contoh 7.19 · Pembuatan asam nitrat dan nasib ozon**

Hitung $\Delta_\text{r}G^\circ$ pada 298 K untuk (a) $4\text{NH}_3(g) + 5\text{O}_2(g) \to 4\text{NO}(g) + 6\text{H}_2\text{O}(g)$; (b) $2\text{O}_3(g) \to 3\text{O}_2(g)$.

**Penyelesaian.** (a) $4(86{,}55) + 6(-228{,}57) - 4(-16{,}45) = -959{,}4$ kJ mol⁻¹. (b) $0 - 2(163{,}2) = -326{,}4$ kJ mol⁻¹.

**Memahami hasil.** (a) Oksidasi amonia sangat menguntungkan, tetapi pada industri ia tetap memerlukan katalis platina dan suhu tinggi untuk berlangsung cepat, dan katalis itu dipilih supaya hasilnya NO, bukan N₂ yang secara termodinamika lebih disukai lagi. (b) Ozon secara termodinamika tidak stabil dan cenderung berubah menjadi oksigen biasa. Lapisan ozon di stratosfer bertahan karena terus-menerus dibentuk kembali oleh sinar ultraviolet matahari, yang memberikan energi Gibbs yang diperlukan. Proses yang tidak spontan dapat terjadi bila ada sumber kerja dari luar, dalam hal ini cahaya.
:::

::: {.contoh}
**Contoh 7.20 · Metana yang terurai pada suhu tinggi**

Untuk metana, $\Delta_\text{f}H^\circ = -74{,}81$ kJ mol⁻¹; entropi standar CH₄(g), C(grafit), dan H₂(g) berturut-turut 186,26; 5,74; dan 130,68 J K⁻¹ mol⁻¹. Anggap Δ*H* dan Δ*S* tidak bergantung pada suhu. (a) Hitung $\Delta_\text{f}G^\circ$ CH₄ pada 1000 K. (b) Di atas suhu berapa metana tidak stabil terhadap unsur-unsurnya?

**Penyelesaian.** $\Delta_\text{f}S^\circ = 186{,}26 - 5{,}74 - 2(130{,}68) = -80{,}84$ J K⁻¹ mol⁻¹.

(a) $\Delta_\text{f}G^\circ(1000\ \text{K}) = -74{,}81 - (1000)(-0{,}080\,84) = +6{,}0$ kJ mol⁻¹.

(b) $T = 74{,}81/0{,}080\,84 = 925$ K.

**Memahami hasil.** Pada suhu kamar metana stabil ($\Delta_\text{f}G^\circ = -50{,}7$ kJ mol⁻¹), tetapi di atas sekitar 650 °C ia cenderung terurai menjadi karbon dan hidrogen, karena tiga molekul gas lebih kacau daripada satu molekul gas dan padatan. Kecenderungan ini dimanfaatkan dalam **pirolisis metana**, cara membuat hidrogen tanpa melepaskan CO₂: karbonnya tertinggal sebagai padatan. Stabilitas termodinamika bukan sifat tetap suatu senyawa; ia selalu "pada suhu berapa".
:::

::: {.kuis}
**Kuis cepat 7.9** Mengapa $\Delta_\text{f}G^\circ$ C(intan) positif, padahal intan terbentuk secara alami?
:::

### Menuju bab berikutnya

Gambar 7.1 sudah memberi kita petunjuk tentang perubahan fasa: pada setiap suhu, zat memilih fasa dengan energi Gibbs terendah, dan titik leleh serta titik didih adalah tempat garis-garis *G* berpotongan. Contoh 7.15 dan 7.16 menunjukkan bahwa tekanan juga menggeser titik-titik potong itu. Bab 8 menjadikan gambaran ini kuantitatif: persamaan Clapeyron dan Clausius–Clapeyron menjelaskan bagaimana titik didih bergantung pada tekanan, dan diagram fasa air dan CO₂ merangkum di mana setiap fasa stabil.
