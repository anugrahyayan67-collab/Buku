# Ringkasan Bab 14

| Gagasan | Rumus atau hasil | Subbab |
|---|---|---|
| Bobot konfigurasi | $W = N!/\prod n_i!$; $\ln W = -N\sum p_i\ln p_i$ (Stirling); puncak selebar $1/\sqrt N$ | 14.1 |
| Sebaran Boltzmann | $p_i = e^{-\varepsilon_i/kT}/q$; $N_j/N_{j'} = (g_j/g_{j'})e^{-\Delta\varepsilon/kT}$; $kT = 207$ cm⁻¹ = 2,48 kJ mol⁻¹ pada 298 K | 14.2 |
| Fungsi partisi | $q = \sum g_je^{-\varepsilon_j/kT}$ = banyaknya keadaan terjangkau; $\langle\varepsilon\rangle = -\partial\ln q/\partial\beta$; $q = q^\text{T}q^\text{R}q^\text{V}q^\text{E}$; gas: $Q = q^N/N!$ | 14.3 |
| Translasi | $q^\text{T} = V/\Lambda^3$, $\Lambda = h/(2\pi mkT)^{1/2}$; klasik bila $q^\text{T}/N \gg 1$ | 14.4 |
| Rotasi dan getaran | $q^\text{R} = T/\sigma\theta_\text{R}$; $q^\text{V} = 1/(1 - e^{-\theta_\text{V}/T})$; $q^\text{E} = g_0$ | 14.5 |
| Energi dan kapasitas kalor | translasi $\tfrac32 R$, rotasi *R* (linear); getaran: fungsi Einstein; padatan $3R\,E(\theta_\text{E}/T)$ | 14.6 |
| Entropi | $S = (U - U_0)/T + Nk\ln(q/N) + Nk$; Sackur–Tetrode; entropi residu CO $\approx R\ln2$, es $R\ln\tfrac32$ | 14.7 |
| Energi Gibbs dan *K* | $G - G(0) = -NkT\ln(q/N)$; $K = \prod(q^\circ_\text{m}/N_\text{A})^{\nu}e^{-\Delta_\text{r}E_0/RT}$ | 14.8 |
| Faktor Boltzmann | atmosfer $p = p_0e^{-h/H}$, $H = RT/Mg$; NMR $\Delta N/N \approx h\nu/2kT$; laju $\propto e^{-E_\text{a}/RT}$ | 14.9 |

**Jawaban kuis cepat.** **14.1** Konfigurasi (3, 1, 0, 0) dan (2, 1, 1, 0), masing-masing 12 keadaan mikro. Konfigurasi (1, 1, 1, 1) hanya dapat diwujudkan dengan satu cara, karena semua molekul berada di tingkat yang sama sehingga menukar molekul tidak menghasilkan keadaan baru. **14.2** Tidak; untuk tingkat tanpa degenerasi perbandingannya $e^{-\Delta\varepsilon/kT} < 1$ pada suhu berapa pun. Bila tingkat atas berdegenerasi 3, perbandingannya $3e^{-\Delta\varepsilon/kT}$, yang melebihi 1 bila $kT > \Delta\varepsilon/\ln3$: **tingkat** atas dapat lebih padat, walaupun setiap **keadaan**nya tetap kurang padat. **14.3** Hampir semua molekul di keadaan dasar; keadaan lain hampir tidak terjangkau. Sumbangannya pada kapasitas kalor praktis nol. **14.4** (a) Berlipat dua; (b) naik $2^{3/2} = 2{,}83$ kali; (c) turun menjadi $(4{,}00/39{,}95)^{3/2} = 0{,}032$ kali, karena helium lebih ringan dan Λ-nya lebih besar. **14.5** Bilangan simetri: σ = 1 untuk CO dan 2 untuk N₂. Tetapan rotasi keduanya hampir sama (1,931 dan 1,998 cm⁻¹), sehingga $q^\text{R}$ CO sekitar dua kali $q^\text{R}$ N₂. **14.6** Paling dekat: H₂, karena getarannya sama sekali tidak terisi ($\theta_\text{V} = 6332$ K) sedangkan rotasinya sudah aktif. Paling jauh: I₂, karena getarannya menyumbang 0,92*R* sehingga $C_{V,\text{m}} \approx 3{,}4R$. **14.7** Tidak. HCl mempunyai dipol besar dan kedua ujungnya sangat berbeda, sehingga molekul tersusun rapi dalam kristal. Kecocokan perhitungan dan tabel (selisih 0,16) menunjukkan tidak ada entropi residu yang berarti, berbeda dengan CO yang kedua ujungnya hampir sama. **14.8** Bagian translasi, $q^\text{T} \propto V$. Disosiasi menambah satu partikel, dan setiap partikel tambahan membawa faktor volume per molekul. Bila tekanan turun, volume per molekul naik, sehingga sisi dengan lebih banyak partikel mendapat lebih banyak keadaan dan kesetimbangan bergeser ke arah atom (*K* tetap, tetapi $K_x$ naik). **14.9** Sebanding dengan 1/*T*: $298/77 = 3{,}9$ kali.

# Pertanyaan

## Subbab 14.1: Keadaan mikro dan konfigurasi dominan

1. Apa beda keadaan mikro dan konfigurasi? Berikan contoh dengan tiga molekul.
2. Mengapa asas peluang a priori sama tidak dapat dibuktikan, tetapi tetap dipercaya?
3. Mengapa sistem kecil (puluhan molekul) memperlihatkan fluktuasi yang berarti, sedangkan sistem makroskopik tidak?

## Subbab 14.2: Sebaran Boltzmann

4. Apa peran kedua pengali Lagrange α dan β dalam penurunan sebaran Boltzmann?
5. Jelaskan mengapa "suhu" adalah sifat sebaran, bukan sifat satu molekul.
6. Mengapa spektroskopi serapan atom lebih stabil terhadap perubahan suhu nyala daripada spektroskopi emisi?

## Subbab 14.3: Fungsi partisi molekul

7. Apa arti fisis fungsi partisi? Apa yang terjadi padanya ketika $T \to 0$ dan $T \to \infty$?
8. Mengapa fungsi partisi molekul dapat ditulis sebagai hasil kali, dan apa akibatnya bagi besaran termodinamika?
9. Kapan molekul harus dianggap terbedakan dan kapan tak terbedakan?

## Subbab 14.4: Fungsi partisi translasi

10. Apa arti panjang gelombang termal, dan kapan gas tidak lagi dapat diperlakukan secara klasik?

## Subbab 14.5: Fungsi partisi rotasi, getaran, dan elektronik

11. Mengapa tingkat rotasi yang paling padat bukan *J* = 0?
12. Apa arti suhu karakteristik $\theta_\text{R}$ dan $\theta_\text{V}$? Mengapa $\theta_\text{V}$ jauh lebih besar daripada $\theta_\text{R}$?
13. Dari mana bilangan simetri berasal, dan mengapa ia mempengaruhi entropi?

## Subbab 14.6: Energi dalam dan kapasitas kalor

14. Jelaskan Gambar 3.7 (kapasitas kalor H₂ terhadap suhu) dengan bahasa fungsi partisi.
15. Mengapa model Einstein berhasil menjelaskan kapasitas kalor intan yang rendah, tetapi gagal pada suhu sangat rendah?

## Subbab 14.7: Entropi statistik

16. Mengapa rumus Sackur–Tetrode memuat tetapan Planck, padahal entropi gas ideal adalah besaran klasik?
17. Apa yang dimaksud entropi residu? Mengapa kalorimetri tidak dapat mendeteksinya?
18. Mengapa nilai $S^\circ$ gas dalam tabel modern umumnya berasal dari spektroskopi, bukan kalorimetri?

## Subbab 14.8: Energi Gibbs dan tetapan kesetimbangan

19. Jelaskan Gambar 14.8: mengapa zat dengan energi lebih tinggi dapat menang pada suhu tinggi?
20. Mengapa efek isotop pada kesetimbangan hilang pada suhu tinggi?

## Subbab 14.9: Faktor Boltzmann dalam kimia

21. Mengapa kenaikan suhu yang kecil dapat menaikkan laju reaksi berlipat-lipat?
22. Mengapa NMR jauh kurang peka daripada spektroskopi UV–tampak?

# Soal

%%SOAL%%

# Jawaban

%%JAWABAN%%

# Pembahasan soal terpilih

**Soal {{mikro}}.** Konfigurasi adalah cara menulis 5 sebagai jumlah tiga bilangan bulat tak negatif. Bobotnya $W = 3!/(n_0!\,n_1!\cdots)$, dengan $n_j$ banyaknya molekul yang memegang *j* kuantum:

| Konfigurasi | (5, 0, 0) | (4, 1, 0) | (3, 2, 0) | (3, 1, 1) | (2, 2, 1) |
|---|---|---|---|---|---|
| *W* | 3!/(2!1!) = 3 | 3! = 6 | 3! = 6 | 3!/(1!2!) = 3 | 3!/(2!1!) = 3 |

Jumlahnya 21, sama dengan banyaknya cara meletakkan 5 kuantum ke dalam 3 molekul, $\binom{7}{2} = 21$. Konfigurasi (4, 1, 0) dan (3, 2, 0), yang memakai tiga tingkat berbeda, paling mungkin. Rata-rata fraksi molekul di tingkat 0 sampai 5 adalah 0,286; 0,238; 0,190; 0,143; 0,095; 0,048.

*Cara berpikir:* bobot terbesar dimiliki konfigurasi yang molekul-molekulnya tersebar di sebanyak mungkin tingkat berbeda, karena setiap tingkat yang terisi satu molekul tidak mengurangi *N*! di pembilang. Dengan tiga molekul, populasi rata-rata turun **lurus**, bukan eksponensial; bentuk eksponensial baru muncul bila molekulnya banyak (Gambar 14.1, kanan). Sebaran Boltzmann adalah hukum untuk sistem besar.

**Soal {{butana}}.** Anggap butana mempunyai tiga konformasi: satu *anti* (energi 0) dan dua *gauche* (energi 3,8 kJ mol⁻¹). Fungsi partisi konformasi $q = 1 + 2e^{-\Delta E/RT}$. Pada 298,15 K, $e^{-3800/(8{,}3145 \times 298{,}15)} = 0{,}216$, sehingga $q = 1{,}432$ dan fraksi *anti* $= 1/q = 0{,}698$. Pada 400 K, $e^{-\Delta E/RT} = 0{,}319$, $q = 1{,}638$, dan fraksi *anti* 0,611.

*Cara berpikir:* degenerasi 2 membuat *gauche* mendapat "dua tiket" dalam undian Boltzmann. Pada suhu sangat tinggi, fraksi *anti* menuju 1/3, bukan 1/2. Inilah contoh kecil persaingan energi dan entropi: energi menyukai *anti*, banyaknya keadaan menyukai *gauche*. Perhitungan yang sama dipakai dalam analisis konformasi di *Kimia Organik*, misalnya untuk fraksi metil aksial pada metilsikloheksana (5 persen).

**Soal {{schottky}}.** Dari subbab 14.3, $\langle\varepsilon\rangle = \varepsilon/(e^{x} + 1)$ dengan $x = \varepsilon/kT$. Karena $dx/dT = -x/T$,

$$
C = \frac{d\langle\varepsilon\rangle}{dT} = \frac{\varepsilon e^{x}}{(e^{x}+1)^2}\cdot\frac{x}{T} = k\,\frac{x^2e^{x}}{(1+e^{x})^2} .
$$

Menurunkan terhadap *x* dan menyamakan dengan nol memberi $x\tanh(x/2) = 2$, yang diselesaikan secara numerik: $x = 2{,}40$, atau $kT = 0{,}417\varepsilon$. Di sana $C = 0{,}439k$. Untuk NO, kedua tingkat berdegenerasi sama (2), sehingga rumusnya tidak berubah. Dengan $\varepsilon/k = 174{,}2$ K, puncaknya pada 72,6 K dengan nilai $0{,}439R = 3{,}65$ J K⁻¹ mol⁻¹.

*Cara berpikir:* kapasitas kalor mengukur seberapa banyak energi yang terserap untuk kenaikan suhu satu kelvin. Pada suhu rendah, tidak ada yang dapat naik ke tingkat atas; pada suhu tinggi, kedua tingkat sudah hampir sama padat dan tidak dapat diisi lagi. Hanya di sekitar $kT \sim \varepsilon$ populasi berubah cepat, sehingga muncul puncak. Puncak semacam ini (anomali Schottky) dipakai untuk mengukur celah energi kecil dalam padatan magnetik.

**Soal {{gibbs}}.** Dengan $S = (U - U_0)/T + k\ln Q$ dan $U$ tidak berubah (suhu sama), hanya suku $k\ln Q$ yang penting, dan hanya $q^\text{T} \propto V$ yang berubah.

(a) Tanpa *N*!: sebelum, $k\ln Q = 2Nk\ln(V/\Lambda^3)$; sesudah, $2Nk\ln(2V/\Lambda^3)$. Jadi $\Delta S = 2Nk\ln2 = 2R\ln2 = 11{,}53$ J K⁻¹.

(b) Dengan *N*!: $k\ln Q = Nk\ln(q/N) + Nk$. Sebelum, setiap wadah memberi $Nk\ln(V/N\Lambda^3)$; sesudah, $2Nk\ln(2V/2N\Lambda^3)$, sama persis. Jadi $\Delta S = 0$.

Jawaban (b) yang benar. Mengangkat sekat di antara dua gas **identik** tidak mengubah apa pun yang dapat diukur, dan sekat dapat dipasang kembali tanpa kerja. Proses yang dapat dibalik tanpa jejak tidak menghasilkan entropi.

*Cara berpikir:* hasil (a) adalah **paradoks Gibbs**: rumus tanpa *N*! memperlakukan atom argon seolah-olah setiap atom mempunyai nama, sehingga "pencampuran" atom kiri dan kanan dianggap menghasilkan keadaan baru. Bila kedua gas berbeda (argon dan neon), hasil 11,53 J K⁻¹ justru benar (Contoh 14.3). Ketakterbedaan partikel identik adalah fakta kuantum, dan ia yang membuat entropi ekstensif.

**Soal {{elektron}}.** $\Lambda = h/(2\pi m_\text{e}kT)^{1/2} = (6{,}626 \times 10^{-34})/[2\pi(9{,}109 \times 10^{-31})(1{,}381 \times 10^{-23})(298)]^{1/2} = 4{,}32 \times 10^{-9}$ m. Volume per atom tembaga $M/\rho N_\text{A} = (63{,}55)/(8{,}96 \times 6{,}022 \times 10^{23})$ cm³ $= 1{,}18 \times 10^{-23}$ cm³, sehingga jaraknya $(1{,}18 \times 10^{-29}\ \text{m}^3)^{1/3} = 0{,}228$ nm. Λ sekitar 19 kali lebih besar, dan $q^\text{T}/N \approx (d/\Lambda)^3 \approx 1/6800 \ll 1$. Elektron sama sekali bukan gas klasik.

*Cara berpikir:* syarat klasik adalah "banyak keadaan per partikel". Elektron 70 000 kali lebih ringan daripada atom argon, sehingga Λ-nya besar, dan di dalam logam ia sangat rapat. Akibatnya elektron mengisi keadaan-keadaan satu per satu dari bawah (asas Pauli), dan hanya sebagian kecil di dekat puncak yang dapat menyerap energi termal. Inilah alasan elektron logam hampir tidak menyumbang kapasitas kalor, sehingga hukum Dulong–Petit tetap berlaku untuk logam.

**Soal {{br2}}.** $\theta_\text{V} = (1{,}4388)(325{,}3) = 468{,}0$ K, $x = \theta_\text{V}/T = 1{,}570$, dan fungsi Einstein $x^2e^x/(e^x - 1)^2 = 0{,}818$. Maka $C_{V,\text{m}} = \tfrac52 R + 0{,}818R = 27{,}58$ J K⁻¹ mol⁻¹ dan $C_{p,\text{m}} = 35{,}90$ J K⁻¹ mol⁻¹, hanya 0,3 persen di bawah nilai terukur. Getaran menyumbang 82 persen dari nilai klasiknya *R*.

*Cara berpikir:* letakkan molekul pada Gambar 14.6. $T/\theta_\text{V} = 0{,}64$ menempatkan Br₂ di bahu kurva, di antara Cl₂ (0,37) dan I₂ (0,97). Urutan halogen ini mengikuti massa atom dan kekuatan ikatan: atom yang lebih berat dan ikatan yang lebih lemah menurunkan frekuensi getaran.

**Soal {{einsteinT}}.** Yang dicari adalah *T* sehingga $x^2e^x/(e^x - 1)^2 = \tfrac12$, dengan $x = 240\ \text{K}/T$. Persamaan ini tidak dapat diselesaikan secara aljabar; dengan coba-coba atau metode numerik, $x = 2{,}983$, sehingga $T = 240/2{,}983 = 80$ K.

*Cara berpikir:* separuh nilai klasik dicapai ketika $T \approx \theta_\text{E}/3$, aturan praktis yang berguna untuk semua osilator: getaran mulai "bangun" di sekitar sepertiga suhu karakteristiknya, dan menyumbang penuh di atas sekitar $\theta$. Untuk Cl₂ ($\theta_\text{V}/3 \approx 270$ K) itu berarti sekitar suhu kamar, sesuai dengan Contoh 14.10.

**Soal {{es}}.** Untuk *N* molekul air ada 2*N* atom H, masing-masing terletak pada satu ikatan hidrogen dan boleh berada di dekat salah satu dari dua atom O. Tanpa syarat apa pun, ada $2^{2N}$ susunan. Syaratnya: setiap O harus mempunyai tepat dua H di dekatnya. Dari 16 susunan empat H di sekitar satu O, yang memenuhi hanya $\binom{4}{2} = 6$. Bila setiap O dianggap memenuhi syarat secara bebas, peluangnya $6/16$ per O, sehingga

$$
W = 2^{2N}\left(\frac{6}{16}\right)^N = \left(\frac32\right)^N , \qquad S = Nk\ln\frac32 = R\ln\frac32 = 3{,}37\ \text{J K}^{-1}\,\text{mol}^{-1} .
$$

Nilai terukur (selisih entropi kalorimetri dan spektroskopi uap air) sekitar 3,4 J K⁻¹ mol⁻¹.

*Cara berpikir:* entropi residu muncul bila kristal mempunyai banyak susunan dengan energi hampir sama yang tidak sempat dipilih ketika didinginkan. Argumen Pauling sedikit kasar, karena syarat di setiap O tidak benar-benar bebas, tetapi koreksinya kurang dari 1 persen. Bahwa angka sederhana ini cocok dengan pengukuran adalah salah satu bukti bahwa atom H di es memang tidak tersusun teratur.

**Soal {{na2}}.** Pada 1000 K dan 1 bar:

- Na: $q^\text{T}/N = 9{,}04 \times 10^7$; dengan $g_0 = 2$, $q^\circ_\text{m}/N_\text{A} = 1{,}809 \times 10^8$.
- Na₂: $q^\text{T}/N = 2{,}56 \times 10^8$, $q^\text{R} = T/(2\theta_\text{R}) = 1000/(2 \times 0{,}2226) = 2246$, $q^\text{V} = 1/(1 - e^{-0{,}2289}) = 4{,}88$; hasil kalinya $2{,}81 \times 10^{12}$.
- $e^{-D_0/RT} = e^{-69\,470/8314} = 2{,}35 \times 10^{-4}$.

$K = (1{,}809 \times 10^8)^2/(2{,}81 \times 10^{12}) \times 2{,}35 \times 10^{-4} = (1{,}165 \times 10^4)(2{,}35 \times 10^{-4}) = 2{,}74$.

Dengan $p_\text{Na} + p_{\text{Na}_2} = 0{,}010$ bar dan $p_{\text{Na}_2} = p_\text{Na}^2/K$: $p_\text{Na} = 0{,}009\,96$ bar dan $p_{\text{Na}_2} = 3{,}6 \times 10^{-5}$ bar, sehingga 0,36 persen partikel berupa Na₂.

*Cara berpikir:* ikatan Na₂ lemah (69 kJ mol⁻¹, kurang dari separuh ikatan I₂), sehingga faktor energinya tidak terlalu kecil, sedangkan faktor fungsi partisi tetap besar. Akibatnya *K* sudah lebih dari 1 pada 1000 K. Pada tekanan rendah, atom bebas mendominasi; pada 1 bar, perhitungan yang sama memberi 22 persen Na₂. Ini juga menjelaskan mengapa lampu natrium bertekanan tinggi menunjukkan pita molekul Na₂ di samping garis atom.

**Soal {{barometrik}}.** Pandang lapisan udara setebal *dh* dengan luas alas *A*. Berat lapisan, $\rho gA\,dh$, ditahan oleh selisih tekanan di bawah dan di atasnya: $[p - (p + dp)]A = \rho gA\,dh$, sehingga $dp = -\rho g\,dh$. Untuk gas ideal, $\rho = pM/RT$. Maka

$$
\frac{dp}{p} = -\frac{Mg}{RT}\,dh \quad\Rightarrow\quad p(h) = p(0)\,e^{-Mgh/RT} .
$$

Karena $M/R = m/k$, eksponennya sama dengan $-mgh/kT$, persis faktor Boltzmann untuk energi potensial gravitasi.

*Cara berpikir:* dua cara, dua bahasa, satu hasil. Mekanika melihat keseimbangan gaya pada lapisan udara; termodinamika statistik melihat persaingan antara energi potensial *mgh*, yang mendorong molekul ke bawah, dan energi termal *kT*, yang menyebarkannya ke atas. Kecocokan keduanya adalah bukti lain bahwa sebaran Boltzmann berlaku untuk energi jenis apa pun, bukan hanya energi kuantum di dalam molekul.

# Bacaan lanjut

1. D. A. McQuarrie dan J. D. Simon, *Molecular Thermodynamics* (University Science Books, 1999), Bab 17–21. Penurunan fungsi partisi yang sangat jelas, dengan banyak perbandingan terhadap data.
2. P. Atkins, J. de Paula, dan J. Keeler, *Atkins' Physical Chemistry*, edisi ke-12 (Oxford University Press, 2023), Fokus 13. Termodinamika statistik untuk kimiawan, termasuk tetapan kesetimbangan.
3. T. L. Hill, *An Introduction to Statistical Thermodynamics* (Dover, 1986). Buku klasik yang tetap menjadi rujukan baku.
4. K. A. Dill dan S. Bromberg, *Molecular Driving Forces*, edisi ke-2 (Garland Science, 2010). Termodinamika statistik dengan banyak contoh dari kimia, biologi, dan nanosains.
5. L. Pauling, "The structure and entropy of ice and of other crystals with some randomness of atomic arrangement", *Journal of the American Chemical Society* 57, 2680–2684 (1935). Asal-usul argumen entropi residu es.
