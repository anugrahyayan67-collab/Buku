## 9.5 Potensial kimia gas ideal dan gas nyata

Untuk menghitung arah perpindahan zat, kita perlu rumus potensial kimia sebagai fungsi komposisi. Gas adalah tempat terbaik untuk memulai, karena rumusnya sudah hampir kita miliki.

### Gas ideal murni dan campuran gas ideal

Di subbab 7.8 kita menurunkan energi Gibbs molar gas ideal murni, $G_\text{m} = G_\text{m}^\circ + RT\ln(p/p^\circ)$. Untuk zat murni, $\mu = G_\text{m}$, sehingga

$$
\mu = \mu^\circ + RT\ln\frac{p}{p^\circ} . \qquad \text{(9.10)}
$$

Besaran $\mu^\circ$ disebut **potensial kimia standar**, yaitu potensial kimia gas pada tekanan standar $p^\circ = 1$ bar. Ia hanya bergantung pada suhu. Seluruh ketergantungan pada tekanan terkumpul di suku logaritma.

Bagaimana dengan gas dalam campuran? Dalam campuran gas ideal, molekul-molekul tidak saling berinteraksi, sehingga setiap komponen berperilaku seolah-olah ia sendirian di dalam wadah, dengan tekanan sama dengan tekanan parsialnya $p_\text{J} = x_\text{J}p$. Bayangkan campuran itu dipisahkan dari gas J murni oleh membran yang hanya dapat dilewati J. Molekul J akan mengalir melewati membran sampai tekanan J murni di sisi lain sama dengan tekanan parsial J di dalam campuran; tidak ada alasan lain bagi molekul J untuk lebih menyukai salah satu sisi, karena di kedua sisi ia tidak "merasakan" molekul lain. Pada kesetimbangan itu, potensial kimia J di kedua sisi sama, dan di sisi murni nilainya diberikan oleh (9.10) dengan $p = p_\text{J}$. Maka

::: {.inti}
$$
\mu_\text{J} = \mu_\text{J}^\circ + RT\ln\frac{p_\text{J}}{p^\circ} . \qquad \text{(9.11)}
$$
**Potensial kimia komponen campuran gas ideal.** Potensial kimia naik secara logaritmik dengan tekanan parsial. Ketika $p_\text{J} \to 0$, $\mu_\text{J} \to -\infty$: zat yang sangat encer mempunyai dorongan sangat kuat untuk masuk ke tempat yang belum memilikinya.
:::

Suku logaritma ini adalah sumber matematis semua gejala yang akan kita bahas di bab-bab berikutnya: tekanan uap larutan, sifat koligatif, tetapan kesetimbangan, dan persamaan Nernst. Ia juga menjelaskan mengapa tidak ada zat yang dapat dimurnikan sempurna: menghilangkan bagian terakhir suatu pengotor berarti melawan potensial kimia yang turun tanpa batas.

::: {.contoh}
**Contoh 9.11 · Pertukaran gas di paru-paru**

Pada 37 °C, tekanan parsial O₂ di dalam alveolus paru-paru sekitar 0,13 bar, sedangkan di dalam darah vena yang datang ke paru-paru sekitar 0,053 bar. Untuk CO₂, tekanan parsial di alveolus sekitar 0,053 bar dan di darah vena sekitar 0,061 bar. Anggap tekanan parsial gas terlarut dalam darah sama dengan tekanan parsial gas yang setimbang dengannya. Hitung selisih potensial kimia setiap gas antara alveolus dan darah, dan tentukan arah perpindahannya.

**Penyelesaian.** Dari (9.11), $\mu^\circ$ saling menghapus, sehingga $\Delta\mu = RT\ln(p_\text{akhir}/p_\text{awal})$, dengan *RT* = (8,314)(310,15) = 2579 J mol⁻¹.

O₂, dari alveolus ke darah: $\Delta\mu = 2579\ln(0{,}053/0{,}13) = -2{,}31$ kJ mol⁻¹. Negatif: O₂ masuk ke darah.

CO₂, dari darah ke alveolus: $\Delta\mu = 2579\ln(0{,}053/0{,}061) = -0{,}36$ kJ mol⁻¹. Negatif: CO₂ keluar dari darah.

**Memahami hasil.** Kedua gas menuruni lereng potensial kimia masing-masing melewati membran alveolus yang sama, dalam arah berlawanan. Lereng CO₂ jauh lebih landai, tetapi CO₂ larut dan berdifusi sekitar dua puluh kali lebih cepat daripada O₂ melewati jaringan, sehingga selisih kecil itu sudah cukup. Tubuh tidak memerlukan pompa untuk bernapas di tingkat molekul; termodinamika yang melakukannya.
:::

### Energi Gibbs pencampuran

Dengan (9.11), kita dapat menghitung energi Gibbs pencampuran gas ideal. Mula-mula, $n_\text{A}$ mol A dan $n_\text{B}$ mol B berada dalam wadah terpisah, masing-masing pada tekanan *p*. Energi Gibbs awal adalah $G_\text{awal} = n_\text{A}(\mu_\text{A}^\circ + RT\ln p/p^\circ) + n_\text{B}(\mu_\text{B}^\circ + RT\ln p/p^\circ)$. Sekat diangkat dan gas bercampur pada tekanan total *p* yang sama; kini tekanan parsialnya $x_\text{A}p$ dan $x_\text{B}p$. Energi Gibbs akhir sama dengan awal, tetapi dengan *p* diganti $p_\text{A}$ dan $p_\text{B}$. Selisihnya:

$$
\Delta_\text{mix}G = n_\text{A}RT\ln\frac{p_\text{A}}{p} + n_\text{B}RT\ln\frac{p_\text{B}}{p} = nRT\left(x_\text{A}\ln x_\text{A} + x_\text{B}\ln x_\text{B}\right) . \qquad \text{(9.12)}
$$

Karena fraksi mol kurang dari satu, logaritmanya negatif dan $\Delta_\text{mix}G < 0$: gas ideal selalu bercampur dengan sendirinya. Turunan terhadap suhu memberi $\Delta_\text{mix}S = -(\partial\Delta_\text{mix}G/\partial T)_p = -nR(x_\text{A}\ln x_\text{A} + x_\text{B}\ln x_\text{B})$, tepat entropi pencampuran yang kita peroleh di Bab 6 dengan cara yang sama sekali berbeda. Dan karena $\Delta_\text{mix}G = \Delta_\text{mix}H - T\Delta_\text{mix}S$, entalpi pencampurannya **nol**. Pencampuran gas ideal didorong sepenuhnya oleh entropi.

::: {.contoh}
**Contoh 9.12 · Membuat udara, dan memisahkannya kembali**

(a) Hitung $\Delta_\text{mix}G$ untuk membuat 1,00 mol udara ($x_{\text{N}_2} = 0{,}79$, $x_{\text{O}_2} = 0{,}21$) dari N₂ dan O₂ murni pada 25 °C dan 1 bar. (b) Berapa kerja minimum untuk mengambil 1,00 mol O₂ murni dari atmosfer yang sangat besar, pada tekanan yang sama?

**Penyelesaian.** (a) Dari (9.12):
$$
\Delta_\text{mix}G = (1{,}00)(8{,}314)(298{,}15)\left[0{,}79\ln0{,}79 + 0{,}21\ln0{,}21\right] = (2479)(-0{,}5139) = -1{,}27\ \text{kJ} .
$$
(b) Mengambil O₂ dari atmosfer yang sangat besar tidak mengubah komposisi atmosfer. Kita memindahkan 1 mol O₂ dari tekanan parsial 0,21 bar ke O₂ murni 1 bar, sehingga kerja minimumnya sama dengan kenaikan potensial kimia:
$$
w_\text{min} = \Delta\mu = RT\ln\frac{1}{0{,}21} = (2479)(1{,}561) = 3{,}87\ \text{kJ mol}^{-1} .
$$

**Memahami hasil.** Pemisahan adalah kebalikan pencampuran, dan termodinamika memberinya harga minimum. Konsentrator oksigen di rumah sakit dan pabrik oksigen industri memakai energi beberapa kali lebih banyak daripada batas ini, karena proses yang berjalan dengan laju yang wajar tidak pernah reversibel. Perhatikan bahwa jawaban (b) lebih besar per mol daripada (a): mengambil sedikit zat dari campuran besar lebih "mahal" per mol daripada memisahkan seluruh campuran.
:::

::: {.terapan}
**Biaya menangkap CO₂ dari udara.** Penangkapan karbon langsung dari udara (*direct air capture*) harus memisahkan CO₂ yang tekanan parsialnya hanya sekitar 0,00042 bar. Dengan cara Contoh 9.12, kerja minimumnya $RT\ln(1/0{,}000\,42) = 19{,}3$ kJ per mol CO₂ pada 25 °C, atau sekitar 120 kWh per ton CO₂. Menangkap CO₂ dari gas buang cerobong pembangkit listrik, tempat fraksi molnya sekitar 0,12, hanya memerlukan $RT\ln(1/0{,}12) = 5{,}3$ kJ mol⁻¹, hampir empat kali lebih murah. Karena itu penangkapan karbon pertama-tama diterapkan di cerobong. Batas termodinamika ini tidak dapat dikalahkan oleh teknologi apa pun; teknologi hanya dapat mendekatinya. Instalasi nyata saat ini memerlukan beberapa kali lipat energi minimum itu.
:::

::: {.contoh}
**Contoh 9.13 · Kerja minimum mengisi tabung selam**

Udara diisikan ke tabung selam dari 1 bar sampai 200 bar pada 25 °C. Anggap udara gas ideal. (a) Berapa kenaikan potensial kimia O₂ dan N₂ per mol? (b) Berapa kerja minimum per mol udara?

**Penyelesaian.** (a) Tekanan parsial setiap gas naik dengan faktor 200, karena komposisi tidak berubah. Dari (9.11), untuk setiap gas: $\Delta\mu = RT\ln200 = (2479)(5{,}298) = 13{,}1$ kJ mol⁻¹.

(b) Pada suhu dan tekanan yang berubah secara reversibel pada suhu tetap, kerja minimum sama dengan kenaikan energi Gibbs: $w_\text{min} = \sum n_\text{J}\Delta\mu_\text{J} = (0{,}79 + 0{,}21)(13{,}1) = 13{,}1$ kJ per mol udara.

**Memahami hasil.** Hasil ini tepat sama dengan kalor yang harus dibuang kompresor dalam Contoh 6.6: pada proses isotermal gas ideal, Δ*H* = 0, sehingga $\Delta G = -T\Delta S$, dan seluruh kerja yang masuk keluar lagi sebagai kalor. Energi yang "tersimpan" di dalam tabung bukan energi dalam yang lebih besar, tetapi energi Gibbs yang lebih besar, yaitu entropi yang lebih kecil. Ketika penyelam menghirup udara itu melalui regulator, kemampuan melakukan kerja tersebut terbuang sebagai pemuaian tak reversibel.
:::

### Gas nyata: fugasitas

Rumus (9.10) sangat elegan, tetapi hanya berlaku untuk gas ideal. Bab 2 menunjukkan bahwa gas nyata menyimpang, terutama pada tekanan tinggi. Bagaimana potensial kimia gas nyata dinyatakan?

G. N. Lewis memberi jawaban yang cerdik: **pertahankan bentuk rumusnya, dan ganti tekanan dengan besaran baru** yang disebut **fugasitas**, *f*:

::: {.inti}
$$
\mu = \mu^\circ + RT\ln\frac{f}{p^\circ} , \qquad f = \varphi p . \qquad \text{(9.13)}
$$
**Fugasitas** *f* adalah "tekanan efektif" gas nyata: tekanan yang harus dimiliki gas ideal agar potensial kimianya sama dengan gas nyata itu. **Koefisien fugasitas** φ mengukur penyimpangan dari keidealan; φ → 1 bila *p* → 0.
:::

Keadaan standar $\mu^\circ$ di sini adalah **gas ideal hipotetis** pada 1 bar: keadaan yang tidak pernah benar-benar ada, tetapi mempunyai nilai yang jelas, karena semua gas nyata menjadi ideal pada tekanan rendah. Dengan pilihan ini, semua penyimpangan dari keidealan terkumpul di dalam φ, dan semua tabel $\mu^\circ$ (yaitu tabel $\Delta_\text{f}G^\circ$) tetap berlaku untuk gas nyata.

Bagaimana φ dihitung? Bandingkan bagaimana potensial kimia gas nyata dan gas ideal berubah dengan tekanan pada suhu tetap. Untuk keduanya, $d\mu = V_\text{m}\,dp$ (dari (9.7) untuk zat murni). Untuk gas ideal $V_\text{m} = RT/p$; untuk gas nyata $V_\text{m} = ZRT/p$, dengan *Z* faktor kompresi dari Bab 2. Selisih kedua potensial kimia adalah $RT\ln\varphi$, dan selisih itu bertambah sebesar $(V_\text{m} - RT/p)\,dp = RT(Z - 1)\,dp/p$. Mulai dari tekanan nol, tempat kedua gas sama:

::: {.inti}
$$
\ln\varphi = \int_0^p\frac{Z - 1}{p}\,dp . \qquad \text{(9.14)}
$$
**Koefisien fugasitas dari persamaan keadaan.** Bila *Z* < 1 (tarikan dominan), φ < 1: gas nyata mempunyai potensial kimia **lebih rendah** daripada gas ideal pada tekanan yang sama. Bila *Z* > 1 (tolakan dominan), φ > 1.
:::

Untuk tekanan sedang, persamaan virial $Z = 1 + Bp/RT$ (subbab 2.7) membuat integralnya mudah: $(Z - 1)/p = B/RT$, tetap, sehingga

$$
\ln\varphi \approx \frac{Bp}{RT} . \qquad \text{(9.15)}
$$

::: {.contoh}
**Contoh 9.14 · Fugasitas CO₂ pada 10 bar**

Koefisien virial kedua CO₂ pada 25 °C adalah $B = -125$ cm³ mol⁻¹. Hitung koefisien fugasitas dan fugasitas CO₂ pada 10,0 bar, serta selisih potensial kimianya terhadap gas ideal pada tekanan yang sama.

**Penyelesaian.** Dalam satuan SI, $Bp = (-125 \times 10^{-6}\ \text{m}^3\ \text{mol}^{-1})(1{,}00 \times 10^6\ \text{Pa}) = -125$ J mol⁻¹. Dari (9.15):
$$
\ln\varphi = \frac{-125}{(8{,}314)(298{,}15)} = -0{,}0504 , \qquad \varphi = 0{,}951 , \qquad f = 9{,}51\ \text{bar} .
$$
Selisih potensial kimia: $\mu_\text{nyata} - \mu_\text{ideal} = RT\ln\varphi = Bp = -125$ J mol⁻¹.

**Memahami hasil.** Pada 10 bar, CO₂ "berperilaku" seperti gas ideal pada 9,51 bar. Tarikan antarmolekul menurunkan potensial kimianya, karena molekul-molekul yang saling menarik kurang "ingin" melepaskan diri. Nama fugasitas berasal dari kata Latin *fugere*, melarikan diri: fugasitas mengukur kecenderungan zat untuk lari dari fasanya. Pada 1 bar, φ = 0,995, sehingga untuk kebanyakan perhitungan pada tekanan atmosfer, menganggap CO₂ ideal hanya membawa kesalahan 0,5%.
:::

Pada tekanan tinggi, persamaan virial dua suku tidak cukup, dan (9.14) harus diintegralkan dengan persamaan keadaan yang lebih lengkap. Gambar 9.3 memperlihatkan hasilnya untuk tiga gas menurut persamaan van der Waals.

![Gambar 9.3 Koefisien fugasitas H₂, N₂, dan CH₄ pada 25 °C menurut persamaan van der Waals. Pada tekanan sedang, tarikan antarmolekul membuat φ < 1; pada tekanan sangat tinggi, tolakan (ukuran molekul) membuat φ naik melewati 1. Hidrogen berada di atas suhu Boyle-nya, sehingga φ > 1 pada semua tekanan.](fig/phi.png){width=72%}

Bentuk kurva-kurva itu adalah cerminan langsung dari Gambar 2.1 tentang faktor kompresi. Metana, yang tarikannya paling kuat, menyimpang paling jauh ke bawah. Hidrogen, yang tarikannya sangat lemah, didominasi tolakan sejak awal; menurut van der Waals, suhu Boyle-nya, $a/Rb = 112$ K, jauh di bawah suhu kamar.

::: {.dalam}
**Lebih dalam: fugasitas gas van der Waals.** Untuk persamaan van der Waals, integral (9.14) dapat diselesaikan dalam bentuk tertutup. Dengan $A' = ap/(RT)^2$ dan $B' = bp/RT$, faktor kompresi *Z* adalah akar terbesar persamaan kubik $Z^3 - (1 + B')Z^2 + A'Z - A'B' = 0$, dan
$$
\ln\varphi = Z - 1 - \ln(Z - B') - \frac{A'}{Z} .
$$
Suku $-\ln(Z - B')$ positif dan berasal dari ukuran molekul (tolakan); suku $-A'/Z$ negatif dan berasal dari tarikan. Gambar 9.3 dibuat dengan rumus ini.
:::

::: {.contoh}
**Contoh 9.15 · Metana dalam tangki gas alam terkompresi**

Gas alam terkompresi untuk kendaraan disimpan pada tekanan sekitar 200–300 bar. Untuk metana pada 300 bar dan 25 °C ($a = 2{,}283$ L² bar mol⁻², $b = 0{,}042\,78$ L mol⁻¹), faktor kompresi van der Waalsnya *Z* = 0,981. Hitung koefisien fugasitas dan fugasitasnya.

**Penyelesaian.** Dengan *RT* = (0,083 14)(298,15) = 24,79 L bar mol⁻¹:
$$
A' = \frac{(2{,}283)(300)}{(24{,}79)^2} = 1{,}115 , \qquad B' = \frac{(0{,}042\,78)(300)}{24{,}79} = 0{,}518 .
$$
$$
\ln\varphi = (0{,}981 - 1) - \ln(0{,}981 - 0{,}518) - \frac{1{,}115}{0{,}981} = -0{,}019 + 0{,}769 - 1{,}136 = -0{,}386 .
$$
Maka φ = 0,680 dan *f* = (0,680)(300) = 204 bar.

**Memahami hasil.** Menariknya, *Z* hampir tepat 1 pada tekanan ini, sehingga persamaan gas ideal memberi volume yang hampir benar. Tetapi potensial kimianya jauh dari ideal: metana pada 300 bar mempunyai "kecenderungan melarikan diri" setara dengan gas ideal pada hanya 204 bar. Sebabnya, φ bergantung pada **seluruh riwayat** penyimpangan dari tekanan nol sampai 300 bar (integral (9.14)), bukan hanya pada *Z* di tekanan akhir. Dalam perhitungan kesetimbangan reaksi pada tekanan tinggi, misalnya sintesis amonia pada 200–300 bar, perbedaan seperti ini menggeser hasil secara berarti, dan Bab 12 akan memakai fugasitas untuk menanganinya.
:::

::: {.kuis}
**Kuis cepat 9.5** Mengapa koefisien fugasitas semua gas mendekati 1 pada tekanan rendah? Untuk gas pada suhu di bawah suhu Boyle-nya, apakah φ pada tekanan sedang lebih besar atau lebih kecil dari 1?
:::

## Menuju larutan

Kita kini mempunyai tiga alat. Besaran molar parsial menjelaskan bagaimana setiap komponen menyumbang pada sifat campuran. Potensial kimia memberi tahu ke mana setiap zat bergerak, dan bahwa kesetimbangan tercapai ketika potensial kimia setiap zat sama di mana-mana. Persamaan Gibbs–Duhem mengikat potensial kimia semua komponen satu sama lain. Untuk gas, rumus (9.11) dan (9.13) memberi potensial kimia secara eksplisit.

Tetapi kebanyakan kimia terjadi dalam larutan cair, dan untuk cairan kita belum mempunyai rumus potensial kimia. Bab 10 memperolehnya dengan cara yang sangat sederhana: pada kesetimbangan, potensial kimia setiap zat di dalam larutan sama dengan potensial kimianya di dalam uap di atas larutan, dan potensial kimia uap sudah kita ketahui dari bab ini. Dari pengamatan Raoult tentang tekanan uap larutan, kita akan memperoleh rumus potensial kimia zat dalam larutan ideal, dan dari rumus itu seluruh sifat koligatif: penurunan tekanan uap, kenaikan titik didih, penurunan titik beku, dan tekanan osmotik yang sudah kita temui sekilas di Contoh 9.7.
