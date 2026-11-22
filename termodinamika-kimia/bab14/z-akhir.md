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

## Subbab 14.1: Keadaan mikro dan konfigurasi dominan

Pakai $k = 1{,}380\,649 \times 10^{-23}$ J K⁻¹, $h = 6{,}626 \times 10^{-34}$ J s, $hc/k = 1{,}4388$ cm K, $R = 8{,}3145$ J K⁻¹ mol⁻¹, $N_\text{A} = 6{,}022 \times 10^{23}$ mol⁻¹, dan $1\ \text{u} = 1{,}6605 \times 10^{-27}$ kg. Tekanan standar 1 bar. Data molekul ada di Tabel 14.1 dan di dalam teks. Soal bertanda **[P]** dibahas di akhir bab.

**1.** Hitung bobot konfigurasi enam molekul dengan $n_0 = 3$, $n_1 = 2$, $n_2 = 1$.

**2.** Pada Gambar 14.1 (kiri), tiga kuantum dibagi di antara tiga molekul. Periksa bahwa bobot ketiga konfigurasi adalah 3, 6, dan 1, dan bahwa jumlahnya sama dengan banyaknya cara meletakkan 3 kuantum ke dalam 3 molekul.

**3.** [P] Lima kuantum energi dibagi di antara tiga molekul (A, B, C), masing-masing bertingkat $0, \varepsilon, 2\varepsilon, \ldots$ Daftarkan semua konfigurasi beserta bobotnya, dan tentukan konfigurasi yang paling mungkin.

**4.** Untuk 20 koin, hitung banyaknya cara memperoleh 10 kepala, perbandingannya terhadap 15 kepala, dan peluang memperoleh tepat 10 kepala.

**5.** Bandingkan $\ln 10!$ dengan pendekatan Stirling $N\ln N - N$ dan dengan bentuk yang lebih teliti $N\ln N - N + \tfrac12\ln(2\pi N)$.

**6.** Hitung entropi pencampuran bila 1 mol atom A dan 3 mol atom B disusun acak di atas kisi.

**7.** Berapa peluang semua molekul gas berada di separuh kiri wadah bila jumlahnya 10, 100, dan satu mol?

**8.** Dalam satu sistem, fraksi molekul di tiga tingkat adalah 0,5; 0,3; dan 0,2. Hitung $-\sum p_i\ln p_i$ dan entropi per mol yang bersesuaian.

**9.** Kristal satu mol molekul yang masing-masing dapat menghadap ke salah satu dari dua arah secara acak mempunyai berapa entropi tambahan?

## Subbab 14.2: Sebaran Boltzmann

**10.** Nyatakan *kT* dalam cm⁻¹ pada 77 K dan 1000 K.

**11.** Hitung perbandingan populasi dua tingkat tanpa degenerasi yang berjarak 500 cm⁻¹ pada 298,15 K dan 1000 K.

**12.** Pada suhu berapa populasi tingkat atas tinggal separuh populasi tingkat bawah, bila keduanya tanpa degenerasi dan berjarak 1000 cm⁻¹?

**13.** Tiga tingkat tanpa degenerasi berenergi 0, 200, dan 400 cm⁻¹. Hitung fraksi molekul di setiap tingkat pada 298,15 K.

**14.** Atom hidrogen di permukaan Matahari (5800 K): hitung perbandingan banyaknya atom di tingkat *n* = 2 (degenerasi 8) terhadap *n* = 1 (degenerasi 2), yang berjarak 82 259 cm⁻¹.

**15.** [P] Konformasi *gauche* butana 3,8 kJ mol⁻¹ lebih tinggi daripada konformasi *anti*, dan ada dua konformasi *gauche* (kiri dan kanan). Hitung fraksi butana dalam konformasi *anti* pada 298,15 K dan 400 K.

**16.** Konformasi metilsikloheksana dengan gugus metil aksial 7,3 kJ mol⁻¹ lebih tinggi daripada ekuatorial. Hitung fraksi aksial pada 298,15 K.

**17.** Laser bekerja dengan populasi terbalik. Bila populasi tingkat atas dua kali tingkat bawah (keduanya tanpa degenerasi, berjarak 1000 cm⁻¹), berapa "suhu" yang harus dimasukkan ke rumus Boltzmann? Apa artinya?

**18.** Mengapa tingkat dasar selalu paling padat pada kesetimbangan, tetapi tingkat *J* = 0 HCl bukan tingkat rotasi yang paling padat?

## Subbab 14.3: Fungsi partisi molekul

**19.** Hitung fungsi partisi molekul yang mempunyai tiga keadaan berenergi 0, 100, dan 300 cm⁻¹ pada 298,15 K.

**20.** Sistem dua tingkat mempunyai $\varepsilon/k = 200$ K. Hitung *q* dan $\langle\varepsilon\rangle/k$ pada 100 K dan 300 K.

**21.** [P] Turunkan kapasitas kalor sistem dua tingkat (energi 0 dan ε, tanpa degenerasi) dari persamaan (14.9). Tunjukkan bahwa ia memuncak pada $kT \approx 0{,}42\varepsilon$ dengan nilai $0{,}44k$ per molekul, dan taksir suhu puncak serta nilai maksimum per mol untuk NO (Contoh 14.6).

**22.** Untuk osilator harmonik pada $kT = \varepsilon$, hitung *q* dan energi rata-rata (diukur dari tingkat dasar).

**23.** Atom oksigen mempunyai tingkat dasar ³P yang terbelah menjadi *J* = 2 (degenerasi 5, energi 0), *J* = 1 (degenerasi 3, 158,3 cm⁻¹), dan *J* = 0 (degenerasi 1, 227 cm⁻¹). Hitung $q^\text{E}$ dan fraksi atom di *J* = 2 pada 298,15 K dan 1000 K.

**24.** [P] Dua wadah bervolume sama masing-masing berisi 1 mol argon pada suhu dan tekanan yang sama. Sekat di antaranya diangkat. Hitung perubahan entropi bila (a) $Q = q^N$ dipakai (tanpa *N*!), dan (b) $Q = q^N/N!$ dipakai. Mana yang benar?

**25.** Molekul mempunyai tingkat dasar tanpa degenerasi dan satu tingkat tereksitasi berdegenerasi 3. Berapa energi rata-rata pada suhu sangat tinggi, dinyatakan dalam selisih energi ε?

**26.** Bila semua energi dinaikkan sebesar tetapan *c*, bagaimana *q* dan populasi berubah?

**27.** Tuliskan *Q* untuk tiga sistem dua tingkat yang terbedakan, lalu jabarkan dan tafsirkan setiap sukunya.

## Subbab 14.4: Fungsi partisi translasi

**28.** Hitung panjang gelombang termal H₂ dan Xe pada 298,15 K.

**29.** Hitung Λ untuk N₂ pada 77 K.

**30.** Hitung $q^\text{T}$ untuk N₂ di dalam wadah 1,00 L pada 298,15 K.

**31.** [P] Hitung panjang gelombang termal elektron pada 298 K dan bandingkan dengan jarak antaratom tembaga (kerapatan 8,96 g cm⁻³, *M* = 63,55 g mol⁻¹), dengan anggapan setiap atom melepas satu elektron. Apakah elektron di dalam logam dapat diperlakukan sebagai gas klasik?

**32.** Pada suhu berapa panjang gelombang termal helium pada 1 bar sama dengan jarak rata-rata antaratomnya, $(kT/p)^{1/3}$? (Anggap tetap gas.)

**33.** Berapa kali $q^\text{T}/N$ argon pada 1 bar bertambah bila suhu dinaikkan dari 298,15 K ke 1000 K?

**34.** Hitung energi tingkat translasi terendah N₂ di dalam kubus bersisi 1 cm, dinyatakan dalam kelvin.

**35.** Berapa perbandingan $q^\text{T}$ kripton terhadap argon pada suhu dan volume yang sama?

**36.** Mengapa rumus (14.12) tidak bergantung pada bentuk wadah, hanya pada volumenya?

## Subbab 14.5: Fungsi partisi rotasi, getaran, dan elektronik

**37.** Hitung $\theta_\text{R}$ dan $q^\text{R}$ CO (*B* = 1,931 cm⁻¹) pada 298,15 K.

**38.** Hitung $q^\text{R}$ O₂ pada 1000 K.

**39.** Tingkat rotasi mana yang paling padat untuk N₂ pada 298,15 K?

**40.** Hitung $q^\text{R}$ NH₃ pada 298,15 K, dengan *A* = *B* = 9,444 cm⁻¹, *C* = 6,196 cm⁻¹, dan σ = 3.

**41.** Hitung $q^\text{V}$ Br₂ ($\tilde\nu$ = 325,3 cm⁻¹) pada 298,15 K dan fraksi molekul di tingkat *v* = 0.

**42.** Hitung fraksi molekul O₂ di tingkat getaran *v* = 1 atau lebih pada 298,15 K, 1000 K, dan 2000 K.

**43.** Hitung $q^\text{V}$ CO₂ pada 298,15 K dari keempat modenya: 1333, 667 (dua mode), dan 2349 cm⁻¹.

**44.** Mengapa bilangan simetri CO₂ (O=C=O) adalah 2, sedangkan N₂O (N=N=O) adalah 1?

**45.** Pada suhu berapa *J* = 5 menjadi tingkat rotasi paling padat untuk HCl?

**46.** Dalam spektrum CO dari awan antarbintang, garis yang berasal dari *J* = 6 paling kuat. Taksir suhu gas.

## Subbab 14.6: Energi dalam dan kapasitas kalor

**47.** Hitung $U_\text{m} - U_\text{m}(0)$ argon dan nitrogen pada 298,15 K.

**48.** Hitung $C_{V,\text{m}}$ HCl pada 298,15 K dan 2000 K.

**49.** [P] Hitung $C_{p,\text{m}}$ Br₂(g) pada 298,15 K dan bandingkan dengan nilai terukur 36,0 J K⁻¹ mol⁻¹. Berapa persen nilai klasik yang disumbangkan getaran?

**50.** Hitung sumbangan getaran pada $C_{V,\text{m}}$ I₂ pada 298,15 K dan 600 K.

**51.** Hitung $C_{V,\text{m}}$ timbal ($\theta_\text{E}$ = 70 K) pada 298 K, dan intan ($\theta_\text{E}$ = 1320 K) pada 1000 K.

**52.** [P] Pada suhu berapa kapasitas kalor tembaga ($\theta_\text{E}$ = 240 K) menurut model Einstein tinggal separuh nilai Dulong–Petit?

**53.** Hitung $C_{p,\text{m}}$ H₂O(g) pada 1000 K dari ketiga mode getarannya (3657, 1595, 3756 cm⁻¹). Nilai terukur 41,3 J K⁻¹ mol⁻¹.

**54.** Hitung energi getaran molar Cl₂ pada 298,15 K (di atas energi titik nol).

**55.** Mengapa $C_{V,\text{m}}$ helium tetap $\tfrac32 R$ dari 10 K sampai ribuan kelvin?

## Subbab 14.7: Entropi statistik

**56.** Hitung entropi molar standar kripton dan xenon pada 298,15 K. Nilai tabel: 164,08 dan 169,68 J K⁻¹ mol⁻¹.

**57.** Hitung entropi molar argon pada 500 K dan 1 bar dengan Sackur–Tetrode, dan periksa bahwa kenaikannya dari 298,15 K sama dengan $C_{p,\text{m}}\ln(T_2/T_1)$.

**58.** Hitung entropi molar argon pada 298,15 K dan 1 kPa.

**59.** Hitung $S^\circ_\text{m}$ HCl pada 298,15 K (translasi dan rotasi; getaran diabaikan).

**60.** Hitung $S^\circ_\text{m}$ Cl₂ pada 298,15 K, termasuk getaran. Nilai tabel 223,08 J K⁻¹ mol⁻¹.

**61.** [P] Turunkan entropi residu es menurut Pauling. Setiap atom O dikelilingi empat ikatan hidrogen; pada setiap ikatan, H dekat ke salah satu dari dua O. Dari $2^4 = 16$ susunan di sekitar satu O, hanya 6 yang membentuk molekul H₂O.

**62.** Berapa entropi residu yang diharapkan untuk N₂O padat, dan untuk CH₃D padat (setiap molekul dapat menghadap ke empat arah yang setara)?

**63.** Hitung entropi molar standar neon pada 298,15 K.

**64.** Mengapa entropi rotasi CO lebih besar daripada N₂ sebesar $R\ln2$?

## Subbab 14.8: Energi Gibbs dan tetapan kesetimbangan

**65.** Hitung $G^\circ_\text{m} - G_\text{m}(0)$ helium pada 298,15 K.

**66.** Hitung $G^\circ_\text{m} - G_\text{m}(0)$ argon pada 1000 K.

**67.** [P] Uap natrium mengandung sedikit molekul Na₂. Hitung *K* untuk $\text{Na}_2(g) \rightleftharpoons 2\text{Na}(g)$ pada 1000 K. Data: $D_0$ = 0,720 eV (69,5 kJ mol⁻¹), *B* = 0,1547 cm⁻¹, $\tilde\nu$ = 159,1 cm⁻¹; atom Na mempunyai $g_0 = 2$. Berapa fraksi partikel yang berupa Na₂ bila tekanan total 0,010 bar?

**68.** Hitung *K* untuk H₂ + D₂ ⇌ 2HD pada 1000 K.

**69.** Mengapa *K* untuk ³⁵Cl₂ + ³⁷Cl₂ ⇌ 2 ³⁵Cl³⁷Cl hampir tepat 4 pada suhu kamar, sedangkan untuk H₂ + D₂ ⇌ 2HD hanya 3,25?

**70.** Hitung derajat disosiasi I₂ pada 1000 K bila tekanan awal I₂ adalah 0,10 bar (volume tetap).

**71.** Zat A (keadaan dasar tanpa degenerasi) dan zat B (keadaan dasar berdegenerasi 3, 2,0 kJ mol⁻¹ lebih tinggi) berada dalam kesetimbangan; tingkat lain dapat diabaikan. Hitung *K* = [B]/[A] pada 298,15 K dan suhu ketika *K* = 1.

**72.** Dalam persamaan (14.24), di mana letak "entalpi" dan "entropi" reaksi?

**73.** Mengapa energi titik nol harus disertakan dalam $\Delta_\text{r}E_0$?

## Subbab 14.9: Faktor Boltzmann dalam kimia

**74.** [P] Turunkan rumus barometrik (14.25) dari keseimbangan gaya pada lapisan udara tipis setebal *dh*, dengan anggapan udara gas ideal pada suhu tetap.

**75.** Taksir tekanan udara pada ketinggian 5 km (isotermal 288 K, 101,3 kPa di permukaan laut).

**76.** Hitung tinggi skala O₂ dan N₂ pada 250 K.

**77.** Hitung selisih populasi relatif elektron tak berpasangan dalam spektrometer ESR 9,5 GHz pada 298 K. Bandingkan dengan NMR 400 MHz.

**78.** Berapa energi aktivasi yang membuat laju reaksi naik tiga kali dari 25 °C ke 35 °C?

**79.** Hitung fraksi $e^{-E_\text{a}/RT}$ untuk $E_\text{a}$ = 100 kJ mol⁻¹ pada 500 K, dan bandingkan dengan nilai pada 298 K.

**80.** Hitung fraksi HCl di tingkat getaran *v* = 1 pada 298,15 K. Mengapa spektrum inframerah HCl pada suhu kamar tidak memperlihatkan pita panas?

**81.** Mengapa rumus barometrik gagal memerikan perbandingan O₂ terhadap N₂ di troposfer, padahal tinggi skala keduanya berbeda?

**82.** Mengapa sampel NMR yang lebih dingin memberi sinyal yang lebih kuat?


# Jawaban

::: {.panjang}
| No. | Jawaban | No. | Jawaban |
|---|---|---|---|
| 1 | 60 | 42 | 4,9 × 10⁻⁴; 0,103; 0,321 |
| 2 | 3 + 6 + 1 = 10 = C(5, 2) | 43 | 1,087 |
| 3 | (5,0,0) 3; (4,1,0) 6; (3,2,0) 6; (3,1,1) 3; (2,2,1) 3; total 21; paling mungkin (4,1,0) dan (3,2,0) | 44 | CO₂ simetris terhadap putaran 180°; N₂O tidak |
| 4 | 184 756; 11,9; 0,176 | 45 | 922 K |
| 5 | 15,104; 13,026; 15,096 | 46 | 235 K |
| 6 | 18,70 J K⁻¹ | 47 | 3,72 kJ mol⁻¹; 6,20 kJ mol⁻¹ |
| 7 | 9,8 × 10⁻⁴; 7,9 × 10⁻³¹; $10^{-1{,}8 \times 10^{23}}$ | 48 | 20,79; 26,52 J K⁻¹ mol⁻¹ |
| 8 | 1,030; 8,56 J K⁻¹ mol⁻¹ | 49 | 35,90 J K⁻¹ mol⁻¹; 82 persen |
| 9 | $R\ln2 = 5{,}76$ J K⁻¹ mol⁻¹ | 50 | 7,61; 8,13 J K⁻¹ mol⁻¹ |
| 10 | 53,5 cm⁻¹; 695 cm⁻¹ | 51 | 24,8; 21,6 J K⁻¹ mol⁻¹ |
| 11 | 0,0896; 0,487 | 52 | 80 K |
| 12 | 2076 K | 53 | 41,0 J K⁻¹ mol⁻¹ |
| 13 | 0,655; 0,250; 0,095 | 54 | 482 J mol⁻¹ |
| 14 | 5,5 × 10⁻⁹ | 55 | hanya translasi; tingkat elektronik tereksitasi sangat tinggi |
| 15 | 0,698; 0,611 | 56 | 164,09; 169,68 J K⁻¹ mol⁻¹ |
| 16 | 0,050 | 57 | 165,59 J K⁻¹ mol⁻¹; kenaikan 10,75 |
| 17 | −2076 K; populasi terbalik bukan keadaan kesetimbangan termal | 58 | 193,14 J K⁻¹ mol⁻¹ |
| 18 | degenerasi 2*J* + 1 naik dengan *J*; yang selalu paling padat adalah **keadaan** dasar, bukan tingkat | 59 | 186,75 J K⁻¹ mol⁻¹ |
| 19 | 1,852 | 60 | 222,82 J K⁻¹ mol⁻¹ |
| 20 | 1,135 dan 23,8 K; 1,513 dan 67,8 K | 61 | $W = 2^{2N}(6/16)^N = (3/2)^N$; $S = R\ln\tfrac32 = 3{,}37$ J K⁻¹ mol⁻¹ |
| 21 | $C/k = x^2e^x/(1+e^x)^2$, $x = \varepsilon/kT$; NO: sekitar 73 K, 3,65 J K⁻¹ mol⁻¹ | 62 | 5,76; 11,53 J K⁻¹ mol⁻¹ |
| 22 | 1,582; 0,582ε | 63 | 146,33 J K⁻¹ mol⁻¹ |
| 23 | 6,73 dan 0,743; 8,11 dan 0,616 | 64 | σ = 1 untuk CO dan 2 untuk N₂; *q*$^\text{R}$ CO dua kali lipat |
| 24 | (a) 11,53 J K⁻¹ (salah, paradoks Gibbs); (b) 0 | 65 | −31,4 kJ mol⁻¹ |
| 25 | $\tfrac34\varepsilon$ | 66 | −159,2 kJ mol⁻¹ |
| 26 | *q* dikali $e^{-c/kT}$; populasi tidak berubah | 67 | *K* = 2,74; 0,36 persen |
| 27 | $(1 + x)^3 = 1 + 3x + 3x^2 + x^3$, $x = e^{-\varepsilon/kT}$; koefisien = banyaknya keadaan mikro dengan 0, 1, 2, 3 tereksitasi | 68 | 3,92 |
| 28 | 71,2 pm; 8,82 pm | 69 | beda massa isotop Cl sangat kecil, sehingga beda energi titik nol dan *B* dapat diabaikan; yang tersisa hanya faktor simetri 4 |
| 29 | 37,6 pm | 70 | 0,086 |
| 30 | 1,43 × 10²⁹ | 71 | 1,34; 219 K |
| 31 | Λ = 4,32 nm; jarak 0,228 nm; Λ 19 kali lebih besar; tidak | 72 | eksponen $-\Delta_\text{r}E_0/RT$ memuat sisi energi; perbandingan fungsi partisi memuat sisi entropi (banyaknya keadaan) |
| 32 | 1,9 K | 73 | energi diukur dari tingkat dasar setiap molekul; tingkat dasar itu sudah memuat energi titik nol yang berbeda antar-zat |
| 33 | 20,6 | 74 | $dp = -\rho g\,dh$, $\rho = pM/RT$, sehingga $p = p_0e^{-Mgh/RT}$ |
| 34 | 2,6 × 10⁻¹⁵ K | 75 | 56,0 kPa |
| 35 | 3,04 | 76 | 6,62 km; 7,56 km |
| 36 | karena tingkat-tingkatnya sangat rapat sehingga jumlah menjadi integral; hanya banyaknya keadaan per volume yang penting | 77 | 7,6 × 10⁻⁴; sekitar 24 kali lebih besar |
| 37 | 2,778 K; 107,3 | 78 | 83,9 kJ mol⁻¹ |
| 38 | 240 | 79 | 3,6 × 10⁻¹¹; sekitar 10⁷ kali lebih besar |
| 39 | *J* = 7 ($J_\text{maks}$ = 6,7) | 80 | 5,4 × 10⁻⁷; hampir tidak ada molekul di *v* = 1 |
| 40 | 75,0 | 81 | troposfer diaduk oleh angin dan konveksi jauh lebih cepat daripada pemisahan oleh difusi |
| 41 | 1,263; 0,792 | 82 | selisih populasi sebanding dengan 1/*T* |
:::


# Pembahasan soal terpilih

**Soal 3.** Konfigurasi adalah cara menulis 5 sebagai jumlah tiga bilangan bulat tak negatif. Bobotnya $W = 3!/(n_0!\,n_1!\cdots)$, dengan $n_j$ banyaknya molekul yang memegang *j* kuantum:

| Konfigurasi | (5, 0, 0) | (4, 1, 0) | (3, 2, 0) | (3, 1, 1) | (2, 2, 1) |
|---|---|---|---|---|---|
| *W* | 3!/(2!1!) = 3 | 3! = 6 | 3! = 6 | 3!/(1!2!) = 3 | 3!/(2!1!) = 3 |

Jumlahnya 21, sama dengan banyaknya cara meletakkan 5 kuantum ke dalam 3 molekul, $\binom{7}{2} = 21$. Konfigurasi (4, 1, 0) dan (3, 2, 0), yang memakai tiga tingkat berbeda, paling mungkin. Rata-rata fraksi molekul di tingkat 0 sampai 5 adalah 0,286; 0,238; 0,190; 0,143; 0,095; 0,048.

*Cara berpikir:* bobot terbesar dimiliki konfigurasi yang molekul-molekulnya tersebar di sebanyak mungkin tingkat berbeda, karena setiap tingkat yang terisi satu molekul tidak mengurangi *N*! di pembilang. Dengan tiga molekul, populasi rata-rata turun **lurus**, bukan eksponensial; bentuk eksponensial baru muncul bila molekulnya banyak (Gambar 14.1, kanan). Sebaran Boltzmann adalah hukum untuk sistem besar.

**Soal 15.** Anggap butana mempunyai tiga konformasi: satu *anti* (energi 0) dan dua *gauche* (energi 3,8 kJ mol⁻¹). Fungsi partisi konformasi $q = 1 + 2e^{-\Delta E/RT}$. Pada 298,15 K, $e^{-3800/(8{,}3145 \times 298{,}15)} = 0{,}216$, sehingga $q = 1{,}432$ dan fraksi *anti* $= 1/q = 0{,}698$. Pada 400 K, $e^{-\Delta E/RT} = 0{,}319$, $q = 1{,}638$, dan fraksi *anti* 0,611.

*Cara berpikir:* degenerasi 2 membuat *gauche* mendapat "dua tiket" dalam undian Boltzmann. Pada suhu sangat tinggi, fraksi *anti* menuju 1/3, bukan 1/2. Inilah contoh kecil persaingan energi dan entropi: energi menyukai *anti*, banyaknya keadaan menyukai *gauche*. Perhitungan yang sama dipakai dalam analisis konformasi di *Kimia Organik*, misalnya untuk fraksi metil aksial pada metilsikloheksana (5 persen).

**Soal 21.** Dari subbab 14.3, $\langle\varepsilon\rangle = \varepsilon/(e^{x} + 1)$ dengan $x = \varepsilon/kT$. Karena $dx/dT = -x/T$,

$$
C = \frac{d\langle\varepsilon\rangle}{dT} = \frac{\varepsilon e^{x}}{(e^{x}+1)^2}\cdot\frac{x}{T} = k\,\frac{x^2e^{x}}{(1+e^{x})^2} .
$$

Menurunkan terhadap *x* dan menyamakan dengan nol memberi $x\tanh(x/2) = 2$, yang diselesaikan secara numerik: $x = 2{,}40$, atau $kT = 0{,}417\varepsilon$. Di sana $C = 0{,}439k$. Untuk NO, kedua tingkat berdegenerasi sama (2), sehingga rumusnya tidak berubah. Dengan $\varepsilon/k = 174{,}2$ K, puncaknya pada 72,6 K dengan nilai $0{,}439R = 3{,}65$ J K⁻¹ mol⁻¹.

*Cara berpikir:* kapasitas kalor mengukur seberapa banyak energi yang terserap untuk kenaikan suhu satu kelvin. Pada suhu rendah, tidak ada yang dapat naik ke tingkat atas; pada suhu tinggi, kedua tingkat sudah hampir sama padat dan tidak dapat diisi lagi. Hanya di sekitar $kT \sim \varepsilon$ populasi berubah cepat, sehingga muncul puncak. Puncak semacam ini (anomali Schottky) dipakai untuk mengukur celah energi kecil dalam padatan magnetik.

**Soal 24.** Dengan $S = (U - U_0)/T + k\ln Q$ dan $U$ tidak berubah (suhu sama), hanya suku $k\ln Q$ yang penting, dan hanya $q^\text{T} \propto V$ yang berubah.

(a) Tanpa *N*!: sebelum, $k\ln Q = 2Nk\ln(V/\Lambda^3)$; sesudah, $2Nk\ln(2V/\Lambda^3)$. Jadi $\Delta S = 2Nk\ln2 = 2R\ln2 = 11{,}53$ J K⁻¹.

(b) Dengan *N*!: $k\ln Q = Nk\ln(q/N) + Nk$. Sebelum, setiap wadah memberi $Nk\ln(V/N\Lambda^3)$; sesudah, $2Nk\ln(2V/2N\Lambda^3)$, sama persis. Jadi $\Delta S = 0$.

Jawaban (b) yang benar. Mengangkat sekat di antara dua gas **identik** tidak mengubah apa pun yang dapat diukur, dan sekat dapat dipasang kembali tanpa kerja. Proses yang dapat dibalik tanpa jejak tidak menghasilkan entropi.

*Cara berpikir:* hasil (a) adalah **paradoks Gibbs**: rumus tanpa *N*! memperlakukan atom argon seolah-olah setiap atom mempunyai nama, sehingga "pencampuran" atom kiri dan kanan dianggap menghasilkan keadaan baru. Bila kedua gas berbeda (argon dan neon), hasil 11,53 J K⁻¹ justru benar (Contoh 14.3). Ketakterbedaan partikel identik adalah fakta kuantum, dan ia yang membuat entropi ekstensif.

**Soal 31.** $\Lambda = h/(2\pi m_\text{e}kT)^{1/2} = (6{,}626 \times 10^{-34})/[2\pi(9{,}109 \times 10^{-31})(1{,}381 \times 10^{-23})(298)]^{1/2} = 4{,}32 \times 10^{-9}$ m. Volume per atom tembaga $M/\rho N_\text{A} = (63{,}55)/(8{,}96 \times 6{,}022 \times 10^{23})$ cm³ $= 1{,}18 \times 10^{-23}$ cm³, sehingga jaraknya $(1{,}18 \times 10^{-29}\ \text{m}^3)^{1/3} = 0{,}228$ nm. Λ sekitar 19 kali lebih besar, dan $q^\text{T}/N \approx (d/\Lambda)^3 \approx 1/6800 \ll 1$. Elektron sama sekali bukan gas klasik.

*Cara berpikir:* syarat klasik adalah "banyak keadaan per partikel". Elektron 70 000 kali lebih ringan daripada atom argon, sehingga Λ-nya besar, dan di dalam logam ia sangat rapat. Akibatnya elektron mengisi keadaan-keadaan satu per satu dari bawah (asas Pauli), dan hanya sebagian kecil di dekat puncak yang dapat menyerap energi termal. Inilah alasan elektron logam hampir tidak menyumbang kapasitas kalor, sehingga hukum Dulong–Petit tetap berlaku untuk logam.

**Soal 49.** $\theta_\text{V} = (1{,}4388)(325{,}3) = 468{,}0$ K, $x = \theta_\text{V}/T = 1{,}570$, dan fungsi Einstein $x^2e^x/(e^x - 1)^2 = 0{,}818$. Maka $C_{V,\text{m}} = \tfrac52 R + 0{,}818R = 27{,}58$ J K⁻¹ mol⁻¹ dan $C_{p,\text{m}} = 35{,}90$ J K⁻¹ mol⁻¹, hanya 0,3 persen di bawah nilai terukur. Getaran menyumbang 82 persen dari nilai klasiknya *R*.

*Cara berpikir:* letakkan molekul pada Gambar 14.6. $T/\theta_\text{V} = 0{,}64$ menempatkan Br₂ di bahu kurva, di antara Cl₂ (0,37) dan I₂ (0,97). Urutan halogen ini mengikuti massa atom dan kekuatan ikatan: atom yang lebih berat dan ikatan yang lebih lemah menurunkan frekuensi getaran.

**Soal 52.** Yang dicari adalah *T* sehingga $x^2e^x/(e^x - 1)^2 = \tfrac12$, dengan $x = 240\ \text{K}/T$. Persamaan ini tidak dapat diselesaikan secara aljabar; dengan coba-coba atau metode numerik, $x = 2{,}983$, sehingga $T = 240/2{,}983 = 80$ K.

*Cara berpikir:* separuh nilai klasik dicapai ketika $T \approx \theta_\text{E}/3$, aturan praktis yang berguna untuk semua osilator: getaran mulai "bangun" di sekitar sepertiga suhu karakteristiknya, dan menyumbang penuh di atas sekitar $\theta$. Untuk Cl₂ ($\theta_\text{V}/3 \approx 270$ K) itu berarti sekitar suhu kamar, sesuai dengan Contoh 14.10.

**Soal 61.** Untuk *N* molekul air ada 2*N* atom H, masing-masing terletak pada satu ikatan hidrogen dan boleh berada di dekat salah satu dari dua atom O. Tanpa syarat apa pun, ada $2^{2N}$ susunan. Syaratnya: setiap O harus mempunyai tepat dua H di dekatnya. Dari 16 susunan empat H di sekitar satu O, yang memenuhi hanya $\binom{4}{2} = 6$. Bila setiap O dianggap memenuhi syarat secara bebas, peluangnya $6/16$ per O, sehingga

$$
W = 2^{2N}\left(\frac{6}{16}\right)^N = \left(\frac32\right)^N , \qquad S = Nk\ln\frac32 = R\ln\frac32 = 3{,}37\ \text{J K}^{-1}\,\text{mol}^{-1} .
$$

Nilai terukur (selisih entropi kalorimetri dan spektroskopi uap air) sekitar 3,4 J K⁻¹ mol⁻¹.

*Cara berpikir:* entropi residu muncul bila kristal mempunyai banyak susunan dengan energi hampir sama yang tidak sempat dipilih ketika didinginkan. Argumen Pauling sedikit kasar, karena syarat di setiap O tidak benar-benar bebas, tetapi koreksinya kurang dari 1 persen. Bahwa angka sederhana ini cocok dengan pengukuran adalah salah satu bukti bahwa atom H di es memang tidak tersusun teratur.

**Soal 67.** Pada 1000 K dan 1 bar:

- Na: $q^\text{T}/N = 9{,}04 \times 10^7$; dengan $g_0 = 2$, $q^\circ_\text{m}/N_\text{A} = 1{,}809 \times 10^8$.
- Na₂: $q^\text{T}/N = 2{,}56 \times 10^8$, $q^\text{R} = T/(2\theta_\text{R}) = 1000/(2 \times 0{,}2226) = 2246$, $q^\text{V} = 1/(1 - e^{-0{,}2289}) = 4{,}88$; hasil kalinya $2{,}81 \times 10^{12}$.
- $e^{-D_0/RT} = e^{-69\,470/8314} = 2{,}35 \times 10^{-4}$.

$K = (1{,}809 \times 10^8)^2/(2{,}81 \times 10^{12}) \times 2{,}35 \times 10^{-4} = (1{,}165 \times 10^4)(2{,}35 \times 10^{-4}) = 2{,}74$.

Dengan $p_\text{Na} + p_{\text{Na}_2} = 0{,}010$ bar dan $p_{\text{Na}_2} = p_\text{Na}^2/K$: $p_\text{Na} = 0{,}009\,96$ bar dan $p_{\text{Na}_2} = 3{,}6 \times 10^{-5}$ bar, sehingga 0,36 persen partikel berupa Na₂.

*Cara berpikir:* ikatan Na₂ lemah (69 kJ mol⁻¹, kurang dari separuh ikatan I₂), sehingga faktor energinya tidak terlalu kecil, sedangkan faktor fungsi partisi tetap besar. Akibatnya *K* sudah lebih dari 1 pada 1000 K. Pada tekanan rendah, atom bebas mendominasi; pada 1 bar, perhitungan yang sama memberi 22 persen Na₂. Ini juga menjelaskan mengapa lampu natrium bertekanan tinggi menunjukkan pita molekul Na₂ di samping garis atom.

**Soal 74.** Pandang lapisan udara setebal *dh* dengan luas alas *A*. Berat lapisan, $\rho gA\,dh$, ditahan oleh selisih tekanan di bawah dan di atasnya: $[p - (p + dp)]A = \rho gA\,dh$, sehingga $dp = -\rho g\,dh$. Untuk gas ideal, $\rho = pM/RT$. Maka

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
