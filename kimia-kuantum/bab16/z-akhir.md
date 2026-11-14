# Ringkasan Bab 16

| Gagasan | Rumus | Subbab |
|---|---|---|
| Spin dan momen magnet inti | $\hat{\boldsymbol\mu} = \gamma\hat{\mathbf I}$; $\ \gamma = g_N\mu_N/\hbar$; $\ \mu_N = e\hbar/2m_p$ | 16.1 |
| Presesi Larmor | $d\boldsymbol\mu/dt = \gamma\boldsymbol\mu \times \mathbf B$; $\ \omega_0 = \gamma B_0$ | 16.1 |
| Tingkat Zeeman inti | $E_{m_I} = -m_I\gamma\hbar B_0$; $\ \Delta m_I = \pm1$; $\ \nu_0 = \gamma B_0/2\pi$ | 16.2 |
| Populasi | $(N_\alpha - N_\beta)/N \approx \gamma\hbar B_0/2k_BT$ | 16.3 |
| Hukum Curie | $M_0 = \mathcal N\gamma^2\hbar^2I(I+1)B_0/3k_BT$ | 16.3 |
| Kepekaan | $S/N \propto \mathcal NI(I+1)|\gamma|^{5/2}B_0^{3/2}$; $\ S/N \propto \sqrt n$ | 16.3 |
| Perisai | $B_\text{lok} = (1 - \sigma)B_0$; $\ \sigma_d = (\mu_0e^2/12\pi m_e)\langle\sum1/r_i\rangle$; $\ \sigma = \sigma_d + \sigma_p$ | 16.4 |
| Geseran kimia | $\delta = 10^6(\nu - \nu_\text{ref})/\nu_\text{ref}$ | 16.4 |
| Hamiltonian dua spin | $\hat H/h = -\nu_A\hat I_{zA} - \nu_X\hat I_{zX} + J\hat{\mathbf I}_A\cdot\hat{\mathbf I}_X$ | 16.5 |
| Spektrum AX; multiplet | garis di $\nu_A \pm \tfrac12J$, $\ \nu_X \pm \tfrac12J$; $\ n + 1$ garis binomial; $\ 2nI + 1$ | 16.5 |
| Karplus | ${}^3J = A\cos^2\phi + B\cos\phi + C$ | 16.5 |
| Spektrum AB | $D = \sqrt{\Delta\nu^2 + J^2}$; $\ $garis $\bar\nu \pm \tfrac12(D \pm J)$; $\ $intensitas $1 \mp J/D$ | 16.6 |
| Koalesensi | $k_c = \pi\Delta\nu/\sqrt2$; $\ \Delta G^\ddagger = RT_c\ln(k_BT_c/hk_c)$ | 16.7 |
| Pulsa | $\theta = \gamma B_1t_p$; $\ \mathbf B_\text{ef} = (\Omega/\gamma)\hat{\mathbf z} + B_1\hat{\mathbf x}'$ | 16.8 |
| FID dan lebar garis | $s(t) = M_0\sin\theta\,e^{i\Omega t}e^{-t/T_2}$; $\ \Delta\nu_{1/2} = 1/\pi T_2$ | 16.8 |
| Persamaan Bloch | $\dot{\mathbf M} = \gamma\mathbf M \times \mathbf B - (M_x\hat{\mathbf x} + M_y\hat{\mathbf y})/T_2 - (M_z - M_0)\hat{\mathbf z}/T_1$ | 16.8 |
| Pemulihan inversi; gema | $M_z(\tau) = M_0(1 - 2e^{-\tau/T_1})$; $\ $gema $\propto e^{-2\tau/T_2}$ | 16.9 |
| BPP | $1/T_1 \propto J(\omega_0) + 4J(2\omega_0)$; $\ J(\omega) = 2\tau_c/(1 + \omega^2\tau_c^2)$; $\ $minimum $\omega_0\tau_c \approx 0{,}62$ | 16.9 |
| NOE | $\eta_\text{maks} = \gamma_S/2\gamma_I$; $\ $volume NOESY $\propto r^{-6}$ | 16.9, 16.10 |
| ESR | $h\nu = g\mu_BB_0$; $\ B = B_0 - a'm_I$; $\ a = \tfrac23\mu_0g_e\mu_Bg_N\mu_N|\psi(0)|^2$ | 16.11 |
| McConnell | $a_\text{H} = Q\rho_\text{C}$, $\ Q \approx -2{,}3$ sampai $-2{,}7$ mT | 16.11 |
| MRI | $\nu(x) = \tfrac{\gamma}{2\pi}(B_0 + G_xx)$; $\ S \propto \rho(1 - e^{-T_R/T_1})e^{-T_E/T_2}$ | 16.12 |

**Jawaban kuis cepat.** **16.1** ¹⁴N dan ¹⁹F; hanya ¹⁹F yang berspin $\tfrac12$. **16.2** ¹⁹F, karena $\gamma$-nya lebih dari dua kali $\gamma$ ³¹P; $\hat I_x$ hanya mengubah $m_I$ sebesar satu, sehingga unsur matriks untuk $\Delta m_I = \pm2$ nol. **16.3** Selisih populasi dan sinyal turun dengan faktor $298/348 = 0{,}86$; karena derau acak juga bertambah, sebanding dengan $\sqrt n$, sehingga S/N hanya naik $\sqrt{100} = 10$ kali. **16.4** 1000 Hz; garis medan imbas arus cincin berlawanan dengan $B_0$ di dalam dan di atas cincin, tetapi melingkar kembali searah $B_0$ di tepi luar cincin. **16.5** Septet 1 : 6 : 15 : 20 : 15 : 6 : 1; karena kopling $J$ ditentukan oleh interaksi di dalam molekul yang tidak melibatkan medan luar, sedangkan geseran dalam Hz sebanding dengan $B_0$. **16.6** Garis luar melemah dan hilang pada $\Delta\nu = 0$; tidak berubah, karena himpunan letak dan intensitas garis hanya bergantung pada $|J|$; tanda relatif kopling baru terlihat pada sistem tiga spin atau lebih. **16.7** Ya, karena tidak ada inti lain yang berkopling berbeda dengan keduanya; tidak, kedua proton orto setara secara kimia tetapi berkopling berbeda dengan proton meta yang sama; naik, karena laju yang diperlukan untuk koalesensi sebanding dengan $\Delta\nu$. **16.8** Nol, karena magnetisasi berada di $-z$ tanpa komponen transversal; setengahnya. **16.9** Ketidakseragaman statis memberi setiap spin frekuensi tetap, sehingga pembalikan fase oleh pulsa 180° membuat semua spin bertemu kembali; fluktuasi acak berubah setelah pulsa sehingga tidak terbalikkan. $T_1$ memendek, karena $\tau_c$ naik dan $1/T_1 \propto \tau_c$. **16.10** HSQC memindahkan magnetisasi melalui ¹J_CH, dan karbon kuaterner tidak mengikat proton; puncak COSY menunjukkan kopling $J$ melalui ikatan, biasanya dua atau tiga ikatan. **16.11** Tujuh garis ($2 \cdot 3 \cdot 1 + 1$); O₂ mempunyai dua elektron tak berpasangan pada keadaan dasar triplet, sedangkan semua elektron N₂ berpasangan. **16.12** MRI hanya memakai medan magnet statis, gradien, dan gelombang radio dengan energi foton sekitar $10^{-7}$ eV, jauh di bawah energi ionisasi; medan pandang menjadi setengahnya.

# Pertanyaan

1. Mengapa inti dengan jumlah proton genap dan neutron genap berspin nol? Apa akibatnya bagi NMR senyawa organik?
2. Mengapa frekuensi presesi Larmor tidak bergantung pada sudut kemiringan momen magnet? Apa padanannya dalam mekanika kuantum?
3. Mengapa medan gelombang radio dalam NMR harus tegak lurus medan statis?
4. Mengapa sinyal NMR sebanding dengan selisih populasi, bukan dengan populasi tingkat bawah saja?
5. Dengan dua cara apa magnet yang lebih kuat memperbaiki spektrum NMR?
6. Bedakan perisai diamagnetik dan paramagnetik. Mengapa rentang geseran ¹H sempit, sedangkan rentang ¹³C dan ¹⁹F lebar?
7. Mengapa geseran kimia lazim dinyatakan dalam ppm, sedangkan tetapan kopling dalam Hz?
8. Jelaskan dengan arus cincin mengapa proton benzena kurang terperisai, sedangkan proton di dalam cincin [18]anulena sangat terperisai.
9. Mengapa interaksi dipol–dipol langsung antarinti tidak tampak dalam spektrum cairan, tetapi kopling $J$ tampak?
10. Mengapa proton-proton yang setara secara magnetik tidak menampakkan kopling di antara mereka, padahal $J$ di antara mereka tidak nol?
11. Apa beda kesetaraan kimia dan kesetaraan magnetik? Berikan satu contoh yang setara secara kimia tetapi tidak secara magnetik.
12. Mengapa proton CH₂ yang bertetangga dengan pusat kiral tidak setara, meskipun ikatan di sekitarnya berputar bebas?
13. Bagaimana NMR dapat mengukur laju proses yang terlalu cepat untuk diikuti dengan metode pencampuran biasa?
14. Apa keuntungan kerangka berputar? Mengapa model vektor klasik memberi hasil yang tepat untuk spin yang tidak berkopling?
15. Mengapa FID dan spektrum memuat informasi yang sama? Apa keunggulan Fellgett?
16. Bedakan $T_1$, $T_2$, dan $T_2^*$. Mengapa $T_2$ tidak pernah lebih besar daripada $2T_1$?
17. Molekul kecil dalam pelarut encer dan protein besar dapat sama-sama mempunyai $T_1$ sekitar satu detik. Mengapa lebar garisnya sangat berbeda?
18. Bagaimana spektrum dua dimensi menunjukkan "siapa terhubung dengan siapa"? Bedakan informasi COSY, HSQC, dan NOESY.
19. Mengapa elektron tak berpasangan dalam orbital π dapat memberi kopling hiperhalus dengan proton yang terletak di bidang simpul orbital itu?
20. Bagaimana MRI mengubah frekuensi menjadi posisi, dan dari mana asal kontras antarjaringan?
21. Bagaimana teka-teki pembuka bab (kuantum energi yang amat kecil dan selisih populasi yang amat tipis, tetapi alat struktur yang paling ampuh) terjawab oleh isi bab ini?

# Soal

## Subbab 16.1: Momen magnet spin inti

Pakai data inti pada tabel subbab 16.1, $\mu_N = 5{,}0508 \times 10^{-27}$ J/T, $\mu_B = 9{,}2740 \times 10^{-24}$ J/T, dan $g_e = 2{,}0023$. Soal dikelompokkan menurut tingkat: **dasar**, **menengah**, dan **tantangan ★**. Soal bertanda **[P]** dibahas di akhir bab.

**Dasar**

**1.** Tentukan apakah spin inti berikut nol, setengah bulat, atau bulat: ¹⁰B, ¹¹B, ¹⁹F, ²⁸Si, ²⁹Si, ⁴⁰Ca. Mana yang tidak terlihat dalam NMR?

**2.** Rasio giromagnetik ¹⁹F adalah $25{,}181 \times 10^7$ rad s⁻¹ T⁻¹. Hitung $g_N$ dan $\mu_z$ maksimum dalam $\mu_N$.

**3.** Hitung frekuensi resonansi ³¹P dalam magnet 11,74 T.

**4.** Hitung perbandingan $\mu_N/\mu_B$ dan jelaskan asal angkanya.

**Menengah**

**5.** Deuteron mempunyai $g_N = 0{,}8574$ dan $I = 1$. Hitung panjang vektor momen magnetnya dan komponen-$z$ maksimumnya, dalam $\mu_N$.

**6.** Momen magnet proton dimiringkan 30° dari medan 1,000 T. Berapa periode presesinya? Apakah berubah bila sudutnya 60°?

**7.** Mengapa ¹⁴N, meskipun melimpah dan berspin tidak nol, jarang dipakai dalam NMR resolusi tinggi?

**Tantangan ★**

**8.** ★ Dari (16.5), tunjukkan bahwa $|\boldsymbol\mu|$ dan $\mu_z$ tetap selama presesi.

## Subbab 16.2: Tingkat energi Zeeman inti

**Dasar**

**9.** Hitung frekuensi resonansi ¹³C dan selisih energinya (dalam J dan J/mol) dalam magnet 14,09 T.

**10.** Berapa frekuensi proton dalam magnet 18,79 T?

**11.** ¹⁷O berspin $\tfrac52$. Berapa banyak tingkat Zeeman, berapa transisi yang diizinkan, dan berapa frekuensi berbeda yang muncul (tanpa interaksi kuadrupol)?

**12.** Berapa kuat medan agar ¹⁹F beresonansi pada 470,4 MHz?

**Menengah**

**13.** Untuk $I = \tfrac32$, hitung $|\langle m + 1|\hat I_x|m\rangle|^2$ (dalam $\hbar^2$) untuk ketiga transisi yang diizinkan. Bagaimana perbandingan intensitasnya?

**14.** Spin $\tfrac12$ mula-mula dalam keadaan $(\alpha + \beta)/\sqrt2$. Dengan (16.12), tentukan $\langle\hat I_x\rangle$, $\langle\hat I_y\rangle$, dan $\langle\hat I_z\rangle$ sebagai fungsi waktu.

**15.** Mengapa medan gelombang radio yang sejajar $B_0$ tidak dapat menginduksi transisi NMR?

**Tantangan ★**

**16.** ★ Tunjukkan bahwa medan linear $2B_1\cos\omega t\,\hat{\mathbf x}$ sama dengan jumlah dua medan berputar berlawanan arah beramplitudo $B_1$. Mengapa komponen yang berputar berlawanan dengan presesi hampir tidak berpengaruh?

## Subbab 16.3: Populasi dan kepekaan

**Dasar**

**17.** Hitung selisih populasi relatif ¹³C dalam magnet 14,09 T pada 298 K.

**18.** Hitung $N_\alpha/N_\beta$ untuk proton pada 600 MHz dan 298 K.

**19.** Spektrum memberi S/N = 20 dengan 64 perekaman. Berapa perekaman untuk S/N = 100?

**20.** Berapa kali ¹⁹F lebih peka daripada ³¹P (pada kelimpahan alami)?

**Menengah**

**21.** Benzena cair (0,876 g/mL) mengandung ¹³C alami (1,07%). Hitung banyaknya inti ¹³C per m³ dan magnetisasi ¹³C-nya dalam 14,09 T pada 298 K.

**22.** Menurut hukum Curie, berapa kali sinyal NMR pada 278 K lebih besar daripada pada 318 K (bila hal lain sama)?

**23.** Mengapa ESR, meskipun memakai elektron yang 658 kali lebih bermagnet, tidak dipakai untuk menentukan struktur molekul organik biasa?

**Tantangan ★**

**24.** ★ [P] Setelah DNP dan pelarutan, polarisasi ¹³C suatu sampel mencapai 30%. Berapa kali lebih besar daripada polarisasi Boltzmann ¹³C pada 9,40 T dan 298 K? Berapa perekaman biasa yang setara dengan satu perekaman hiperpolarisasi?

## Subbab 16.4: Perisai dan geseran kimia

**Dasar**

**25.** Sinyal pada $\delta = 3{,}40$ berjarak berapa Hz dari TMS pada spektrometer 300 MHz dan 800 MHz?

**26.** Pada spektrometer 500 MHz, sinyal muncul 1450 Hz dari TMS. Berapa $\delta$-nya?

**27.** Urutkan $\delta$ proton metil dalam CH₃CH₃, CH₃OH, CH₃F, dan Si(CH₃)₄.

**28.** Sinyal ¹³C CDCl₃ pada 77,16 ppm berjarak berapa Hz dari TMS pada 100,6 MHz?

**Menengah**

**29.** Dengan rumus Lamb, hitung $\sigma_d$ untuk ion mirip hidrogen He⁺ dan Li²⁺ pada keadaan 1s.

**30.** Dalam model Pople, $\Delta\sigma = \frac{\mu_0}{4\pi}\frac{e^2a^2}{2m_eR^3}(3\cos^2\theta - 1)$, dengan $\theta$ sudut terhadap sumbu cincin. Hitung $\Delta\sigma$ untuk proton tepat di atas pusat benzena pada jarak 3,0 Å, dan untuk proton di bidang cincin pada jarak yang sama.

**31.** Mengapa $\delta$ proton OH etanol dalam CCl₄ bergeser ke kanan (medan tinggi) bila larutan diencerkan?

**Tantangan ★**

**32.** ★ [P] Hitung $\sigma_d$ atom hidrogen dengan fungsi uji Gauss teroptimasi $\psi \propto e^{-\alpha r^2}$, $\alpha = 8/9\pi$ (satuan atom). Bandingkan dengan 17,75 ppm.

## Subbab 16.5: Kopling spin–spin: spektrum AX

**Dasar**

**33.** Ramalkan pola sinyal CH₂ dan CH₃ dalam CH₃CH₂Cl.

**34.** Berapa banyak garis dan berapa intensitas relatif sinyal CH dalam gugus isopropil?

**35.** Ramalkan spektrum ¹³C kloroform tanpa dekopling proton (¹J_CH = 209 Hz).

**36.** Proton vinil berkopling 17 Hz dengan satu tetangga dan 10 Hz dengan tetangga lain. Di mana letak keempat garisnya relatif terhadap pusat?

**Menengah**

**37.** Ramalkan spektrum ³¹P dan ¹⁹F ion PF₆⁻ (¹J_PF ≈ 710 Hz).

**38.** Sinyal sisa DMSO-$d_6$ berasal dari CHD₂. Ramalkan polanya (²J_HD ≈ 1,9 Hz).

**39.** Hitung ³J dengan (16.25) untuk $\phi = 30°$, 90°, dan 150°.

**40.** Dengan aturan ¹J_CH ≈ 500 Hz × s, taksir karakter s ikatan C–H benzena (158 Hz) dan siklobutana (134 Hz).

**Tantangan ★**

**41.** ★ [P] Dengan teori perturbasi orde dua, hitung koreksi energi keadaan $\alpha\beta$ dan $\beta\alpha$ sistem AX akibat suku penukar dalam (16.22). Tunjukkan bahwa hasilnya sama dengan uraian (16.27) untuk $J \ll \Delta\nu$.

## Subbab 16.6: Spektrum orde dua (AB)

**Dasar**

**42.** Sistem AB dengan $\Delta\nu = 40$ Hz dan $J = 8$ Hz. Hitung $D$, letak keempat garis relatif terhadap $\bar\nu$, dan perbandingan intensitas dalam : luar.

**43.** Garis-garis AB teramati di 520, 510, 490, dan 480 Hz. Tentukan $J$ dan $\Delta\nu$.

**44.** Pada $\Delta\nu/J$ berapa garis dalam AB tepat dua kali lebih kuat daripada garis luar?

**Menengah**

**45.** Tunjukkan bahwa jumlah intensitas keempat garis AB tidak bergantung pada $\theta$.

**46.** [P] Turunkan nilai eigen dan vektor eigen (16.27) dan (16.28) dari matriks (16.26).

**47.** Tuliskan keempat energi sistem A₂ (Zeeman ditambah kopling) dan tunjukkan bahwa spektrumnya hanya satu garis di $\nu_A$.

**Tantangan ★**

**48.** ★ Pakai program Contoh 16.27 untuk sistem A₂X dengan $\nu_A = 0$, $\nu_X = 100$ Hz, dan $J_{AX} = 7$ Hz. Bandingkan dengan aturan $n + 1$.

## Subbab 16.7: Kesetaraan kimia dan magnetik

**Dasar**

**49.** Tentukan notasi Pople untuk CH₃OCH₃, CH₂Cl₂, CH₃CH₂Br, dan CHF₃ (sertakan ¹⁹F).

**50.** Golongkan proton CH₂ berikut sebagai homotopik, enantiotopik, atau diastereotopik: CH₂Cl₂; CH₂ dalam CH₃CH₂OH; CH₂ dalam CH₃CHClCH₂CH₃.

**51.** Dua tapak berpopulasi sama terpisah 50 Hz. Hitung laju pertukaran pada koalesensi.

**Menengah**

**52.** Dua sinyal yang terpisah 20 Hz berkoalesensi pada 320 K. Hitung $\Delta G^\ddagger$.

**53.** [P] Proses pada soal sebelumnya direkam dengan magnet dua kali lebih kuat, sehingga $\Delta\nu = 40$ Hz. Berapa suhu koalesensi yang baru?

**54.** Satu proton bertukar cepat antara dua lingkungan: 70% pada $\delta = 3{,}0$ dan 30% pada $\delta = 3{,}5$. Di mana sinyal rata-ratanya?

**Tantangan ★**

**55.** ★ Pada pertukaran lambat, umur terbatas di setiap tapak melebarkan garis sebesar $k/\pi$. Berapa pelebaran untuk $k = 10$ s⁻¹? Jelaskan hubungannya dengan (16.36).

## Subbab 16.8: Model vektor, pulsa, dan FID

**Dasar**

**56.** Pulsa 90° proton lamanya 8,0 μs. Hitung $\omega_1$, $B_1$, dan $\nu_1$.

**57.** Dengan $B_1$ yang sama seperti soal sebelumnya, berapa lama pulsa 90° untuk ¹³C?

**58.** Pulsa 90° lamanya 12 μs. Berapa sudut balik pulsa 5 μs?

**59.** Hitung lebar garis untuk $T_2 = 0{,}50$ s.

**Menengah**

**60.** Spektrum ¹³C direkam pada 150,9 MHz dengan jendela 250 ppm dan 65 536 titik kompleks. Hitung SW, selang cuplikan, lama perekaman, dan resolusi digital.

**61.** Suatu garis berada 10 kHz dari pembawa, dan $\nu_1 = 25$ kHz. Berapa sudut kemiringan medan efektif dari sumbu $x'$ dan berapa frekuensi nutasi efektifnya?

**Tantangan ★**

**62.** ★ [P] Hitung transformasi Fourier (16.35) untuk $s(t) = e^{i\Omega t - t/T_2}$ dan tunjukkan bahwa bagian riilnya fungsi Lorentz dengan lebar setengah tinggi $1/\pi T_2$.

## Subbab 16.9: Relaksasi T₁ dan T₂

**Dasar**

**63.** Sinyal pemulihan inversi melewati nol pada 2,08 s. Berapa $T_1$?

**64.** Dalam percobaan gema spin, tinggi gema pada $2\tau = 100$ ms adalah 0,60 kali tinggi awal. Hitung $T_2$.

**65.** Berapa persen $M_z$ pulih setelah $3T_1$?

**Menengah**

**66.** Pada 600 MHz, berapa waktu korelasi yang memberi $T_1$ minimum menurut BPP?

**67.** Dalam rezim penyempitan ekstrem, apa yang terjadi pada $T_1$ suatu molekul kecil bila viskositas pelarut dilipatduakan?

**68.** Hitung faktor peningkatan NOE maksimum untuk ³¹P bila proton dijenuhkan.

**Tantangan ★**

**69.** ★ [P] Tunjukkan bahwa $T_1$ dalam (16.41) minimum pada $\omega_0\tau_c \approx 0{,}616$.

## Subbab 16.10: Konsep NMR dua dimensi

**Dasar**

**70.** Ramalkan puncak silang COSY etil propanoat, CH₃CH₂COOCH₂CH₃ ($\delta$ 1,14; 2,32; 4,12; 1,26).

**71.** Puncak NOE rujukan pada 2,5 Å bervolume 1,0. Puncak lain bervolume 0,20. Taksir jaraknya.

**72.** Berapa lama percobaan 2D dengan 512 nilai $t_1$, 4 perekaman per nilai, dan 1,5 s per perekaman?

**Menengah**

**73.** Berapa puncak dalam spektrum ¹H–¹³C HSQC etanol? Mengapa proton OH tidak muncul?

**74.** Hitung keuntungan kepekaan deteksi proton untuk ²⁹Si menurut faktor $(\gamma_\text{H}/|\gamma_X|)^{5/2}$.

**Tantangan ★**

**75.** ★ Galat 10% pada volume puncak NOE menimbulkan galat berapa persen pada jarak? Mengapa ini menguntungkan?

## Subbab 16.11: ESR: faktor g dan kopling hiperhalus

**Dasar**

**76.** Di medan berapa DPPH ($g = 2{,}0036$) beresonansi pada 9,75 GHz?

**77.** Berapa garis ESR suatu radikal dengan dua inti ¹⁴N setara, dan berapa intensitasnya?

**78.** Ramalkan spektrum ·CD₃ (banyak garis, intensitas, dan jarak), bila $a_\text{H}$ ·CH₃ = 2,30 mT.

**79.** Nyatakan $a = 1{,}00$ mT dalam MHz untuk $g = 2{,}0023$.

**Menengah**

**80.** Radikal etil ·CH₂CH₃ mempunyai $a(\text{CH}_2) = 2{,}24$ mT dan $a(\text{CH}_3) = 2{,}69$ mT. Berapa banyak garis yang diharapkan bila semuanya terurai?

**81.** Radikal alil mempunyai SOMO Hückel dengan koefisien $1/\sqrt2$, 0, $-1/\sqrt2$. Ramalkan $a_\text{H}$ proton ujung dan proton tengah dengan $Q = -2{,}7$ mT. Data: ujung ≈ 1,4 mT; tengah ≈ 0,41 mT. Apa yang gagal?

**82.** Hitung selisih populasi relatif elektron pada pita X (9,5 GHz) pada 298 K dan 77 K.

**Tantangan ★**

**83.** ★ [P] Tunjukkan bahwa tetapan hiperhalus ion mirip hidrogen sebanding dengan $g_NZ^3$. Ramalkan $a$ untuk ion ³He⁺ ($g_N = -4{,}2552$) dari nilai atom H (1422,8 MHz, tanpa koreksi massa tereduksi).

## Subbab 16.12: MRI

**Dasar**

**84.** Hitung frekuensi Larmor proton pada 3,0 T dan sebaran frekuensi sepanjang 25 cm dengan gradien 40 mT/m.

**85.** Hitung tebal irisan bila lebar pita pulsa 2,0 kHz dan $G_z = 20$ mT/m.

**86.** Medan pandang 25,6 cm dengan matriks 512. Berapa ukuran piksel?

**Menengah**

**87.** Dengan $T_R = 300$ ms, hitung faktor $1 - e^{-T_R/T_1}$ untuk lemak ($T_1 = 250$ ms) dan otot ($T_1 = 900$ ms). Jaringan mana yang terang pada citra berbobot T₁?

**88.** Jaringan dengan $T_1 = 1{,}2$ s mengandung 0,20 mM bahan kontras ($r_1 = 4{,}0$ mM⁻¹ s⁻¹). Hitung $T_1$ yang baru.

**Tantangan ★**

**89.** ★ Aktivitas otak memanjangkan $T_2^*$ jaringan dari 50 ms menjadi 52 ms. Hitung perubahan relatif sinyal pada $T_E = 30$ ms.


# Jawaban

::: {.panjang}
| No. | Jawaban | No. | Jawaban |
|---|---|---|---|
| 1 | bulat; setengah bulat; ½; nol; ½; nol. ²⁸Si dan ⁴⁰Ca tidak terlihat | 46 | lihat pembahasan |
| 2 | $g_N = 5{,}258$; $\mu_z = 2{,}629\,\mu_N$ | 47 | triplet: $-\nu_A + \tfrac J4$, $\tfrac J4$, $\nu_A + \tfrac J4$; singlet $-\tfrac{3J}4$; transisi hanya di dalam triplet |
| 3 | 202,5 MHz | 48 | X: garis di 93,25; 100,0; 100,49; 107,24 Hz (intensitas 0,29; 0,25; 0,25; 0,22): "triplet" condong; A: empat garis di sekitar ±3,5 Hz |
| 4 | $5{,}446 \times 10^{-4} = m_e/m_p$ | 49 | A₆; A₂; A₃X₂; AX₃ |
| 5 | $1{,}213\,\mu_N$; $0{,}857\,\mu_N$ | 50 | homotopik; enantiotopik; diastereotopik |
| 6 | 23,5 ns; tidak berubah | 51 | 111 s⁻¹ |
| 7 | momen kuadrupol: relaksasi cepat, garis lebar | 52 | 68,5 kJ/mol |
| 8 | $\tfrac{d}{dt}\mu^2 = 2\gamma\boldsymbol\mu\cdot(\boldsymbol\mu \times \mathbf B) = 0$; $\dot\mu_z = 0$ | 53 | 329 K |
| 9 | 150,9 MHz; $1{,}00 \times 10^{-25}$ J; 0,060 J/mol | 54 | 3,15 ppm |
| 10 | 800 MHz | 55 | 3,2 Hz; $1/T_2 \to 1/T_2 + k$ |
| 11 | 6 tingkat; 5 transisi; 1 frekuensi | 56 | $1{,}96 \times 10^5$ rad/s; 0,734 mT; 31,3 kHz |
| 12 | 11,74 T | 57 | 31,8 μs |
| 13 | $\tfrac34$, 1, $\tfrac34$; 3 : 4 : 3 | 58 | 37,5° |
| 14 | $\tfrac\hbar2\cos\omega_0t$; $\mp\tfrac\hbar2\sin\omega_0t$ (arah putar menurut tanda $\gamma$); 0 | 59 | 0,64 Hz |
| 15 | perturbasi $\propto \hat I_z$, diagonal dalam basis $|m\rangle$ | 60 | 37,7 kHz; 26,5 μs; 1,74 s; 0,58 Hz |
| 16 | dalam kerangka berputar ia berputar dengan $2\omega$; pergeseran Bloch–Siegert $\sim B_1^2/4B_0$ | 61 | 21,8° ke arah $z$; 26,9 kHz |
| 17 | $1{,}21 \times 10^{-5}$ | 62 | $S = T_2/[1 + i(\omega - \Omega)T_2]$ |
| 18 | 1,0000966 | 63 | 3,0 s |
| 19 | 1600 | 64 | 0,196 s |
| 20 | 12,5 kali | 65 | 95% |
| 21 | $4{,}34 \times 10^{26}$ m⁻³; $1{,}87 \times 10^{-5}$ A/m | 66 | 0,163 ns |
| 22 | 1,14 kali | 67 | $T_1$ menjadi setengahnya |
| 23 | molekul biasa tidak mempunyai elektron tak berpasangan | 68 | $\eta = 1{,}23$; faktor 2,23 |
| 24 | $3{,}7 \times 10^4$ kali; $\sim 1{,}4 \times 10^9$ perekaman | 69 | lihat pembahasan |
| 25 | 1020 Hz; 2720 Hz | 70 | (1,14; 2,32) dan (1,26; 4,12), masing-masing berpasangan simetris; tidak ada antara kedua gugus etil |
| 26 | 2,90 ppm | 71 | 3,27 Å |
| 27 | Si(CH₃)₄ < CH₃CH₃ < CH₃OH < CH₃F | 72 | 51,2 menit |
| 28 | 7762 Hz | 73 | 2; OH tidak terikat pada karbon |
| 29 | $Z \times 17{,}75$: 35,5 ppm; 53,3 ppm | 74 | 57 kali |
| 30 | +2,0 ppm (terperisai); −1,0 ppm | 75 | 1,6%; $r \propto V^{-1/6}$ |
| 31 | ikatan hidrogen berkurang, proton lebih terperisai | 76 | 347,7 mT |
| 32 | $\langle 1/r\rangle = 8/3\pi = 0{,}849$; 15,1 ppm | 77 | 5 garis, 1 : 2 : 3 : 2 : 1 |
| 33 | CH₂ kuartet 1 : 3 : 3 : 1; CH₃ triplet 1 : 2 : 1 | 78 | 7 garis 1 : 3 : 6 : 7 : 6 : 3 : 1; 0,353 mT |
| 34 | septet 1 : 6 : 15 : 20 : 15 : 6 : 1 | 79 | 28,0 MHz |
| 35 | doblet, pemisahan 209 Hz | 80 | $3 \times 4 = 12$ |
| 36 | $\pm13{,}5$ dan $\pm3{,}5$ Hz | 81 | ujung 1,35 mT; tengah 0; rapat spin negatif dari polarisasi spin |
| 37 | ³¹P: septet; ¹⁹F: doblet, pemisahan 710 Hz | 82 | $7{,}6 \times 10^{-4}$; $3{,}0 \times 10^{-3}$ |
| 38 | kuintet 1 : 2 : 3 : 2 : 1, jarak 1,9 Hz | 83 | $-8671$ MHz (terukur $-8665$ MHz) |
| 39 | 6,3; 1,4; 8,2 Hz | 84 | 127,7 MHz; 426 kHz |
| 40 | 0,32; 0,27 | 85 | 2,35 mm |
| 41 | $\mp J^2/4\Delta\nu$ | 86 | 0,50 mm |
| 42 | 40,79 Hz; $\pm24{,}40$, $\pm16{,}40$ Hz; 1,49 | 87 | 0,70; 0,28; lemak |
| 43 | 10 Hz; 28,3 Hz | 88 | 0,61 s |
| 44 | $2\sqrt2 = 2{,}83$ | 89 | +2,3% |
| 45 | $2(1 - \sin2\theta) + 2(1 + \sin2\theta) = 4$ |  |  |
:::


# Pembahasan soal terpilih

**Soal 24.** Polarisasi Boltzmann ¹³C pada 9,40 T ($\nu_0 = 100{,}6$ MHz) dan 298 K adalah $P = \tanh(h\nu_0/2k_BT) = 8{,}10 \times 10^{-6}$. Perbandingannya $0{,}30/8{,}10 \times 10^{-6} = 3{,}7 \times 10^4$. Karena S/N sebanding dengan $\sqrt n$, satu perekaman hiperpolarisasi setara dengan $(3{,}7 \times 10^4)^2 \approx 1{,}4 \times 10^9$ perekaman biasa; dengan jeda 10 s per perekaman, itu lebih dari empat abad.

*Cara berpikir:* hiperpolarisasi tidak mengubah batas Boltzmann; ia "meminjam" polarisasi dari sistem lain (elektron pada suhu rendah) lalu membawanya ke suhu kamar lebih cepat daripada spin sempat berelaksasi. Akibatnya polarisasi itu fana: ia meluruh dengan $T_1$ ¹³C, biasanya beberapa puluh detik, sehingga percobaan harus diselesaikan dalam satu atau beberapa pulsa kecil. Itulah sebabnya karbon karbonil piruvat, yang $T_1$-nya panjang karena tidak mengikat proton, dipilih untuk pencitraan metabolik.

**Soal 32.** Fungsi ternormalisasi $\psi = (2\alpha/\pi)^{3/4}e^{-\alpha r^2}$ memberi

$$
\left\langle\frac1r\right\rangle = 4\pi\left(\frac{2\alpha}{\pi}\right)^{3/2}\int_0^\infty r\,e^{-2\alpha r^2}dr = 4\pi\left(\frac{2\alpha}{\pi}\right)^{3/2}\frac{1}{4\alpha} = 2\sqrt{\frac{2\alpha}{\pi}} .
$$

Dengan $\alpha = 8/9\pi$: $2\alpha/\pi = 16/9\pi^2$, sehingga $\langle 1/r\rangle = 8/3\pi = 0{,}849$ (satuan atom). Maka $\sigma_d = 0{,}849 \times 17{,}75 = 15{,}1$ ppm, 15% di bawah nilai tepat.

*Cara berpikir:* energi fungsi uji Gauss ini hanya 15% di atas energi tepat, dan galat perisainya sama besar, karena keduanya bergantung pada $\langle 1/r\rangle$ (melalui teorema virial, $E = -\tfrac12\langle 1/r\rangle$ di titik optimum). Fungsi Gauss tidak mempunyai taring di inti, sehingga rapat elektronnya di dekat inti terlalu kecil. Sifat yang peka terhadap daerah dekat inti, seperti perisai NMR dan kopling hiperhalus, karena itu memerlukan basis Gauss yang diperkaya fungsi-fungsi curam (Bab 17).

**Soal 41.** Energi orde nol $E_{\alpha\beta}/h = -\tfrac12\Delta\nu - \tfrac14J$ dan $E_{\beta\alpha}/h = \tfrac12\Delta\nu - \tfrac14J$, dengan selisih $E_{\alpha\beta} - E_{\beta\alpha} = -h\Delta\nu$. Unsur matriks penghubungnya $\tfrac12J$. Menurut teori perturbasi orde dua (subbab 8.7):

$$
E^{(2)}_{\alpha\beta} = \frac{(\tfrac12J)^2}{-\Delta\nu} = -\frac{J^2}{4\Delta\nu}, \qquad E^{(2)}_{\beta\alpha} = +\frac{J^2}{4\Delta\nu}
$$

(dalam satuan frekuensi). Dari rumus tepat, $D = \Delta\nu\sqrt{1 + J^2/\Delta\nu^2} \approx \Delta\nu + J^2/2\Delta\nu$, sehingga $-\tfrac14J \mp \tfrac12D \approx -\tfrac14J \mp \tfrac12\Delta\nu \mp J^2/4\Delta\nu$: sama.

*Cara berpikir:* kedua tingkat tengah "saling tolak", sehingga garis-garis bergeser sebesar $J^2/4\Delta\nu$. Untuk gugus etil pada 60 MHz ($J = 7$ Hz, $\Delta\nu = 148$ Hz), pergeserannya 0,08 Hz, kecil dibandingkan lebar garis; efek orde dua yang terlihat lebih dahulu adalah perubahan intensitas (atap), yang sebanding dengan $J/\Delta\nu$, bukan $(J/\Delta\nu)^2$.

**Soal 46.** Matriks (16.26) berbentuk $-\tfrac14J\,\mathbf 1 + \begin{pmatrix}-\tfrac12\Delta\nu & \tfrac12J\\ \tfrac12J & \tfrac12\Delta\nu\end{pmatrix}$. Matriks kedua mempunyai jejak nol dan determinan $-\tfrac14(\Delta\nu^2 + J^2)$, sehingga nilai eigennya $\pm\tfrac12D$; seluruhnya $-\tfrac14J \pm \tfrac12D$. Untuk nilai eigen bawah $-\tfrac14J - \tfrac12D$, baris pertama persamaan eigen memberi $\tfrac12(D - \Delta\nu)v_1 + \tfrac12Jv_2 = 0$, jadi $v_2/v_1 = -(D - \Delta\nu)/J$. Dengan $\cos2\theta = \Delta\nu/D$ dan $\sin2\theta = J/D$, identitas $\tan\theta = \sin2\theta/(1 + \cos2\theta) = J/(D + \Delta\nu) = (D - \Delta\nu)/J$ (karena $(D - \Delta\nu)(D + \Delta\nu) = J^2$) memberi $v_2/v_1 = -\tan\theta$, yaitu $|2\rangle = \cos\theta|\alpha\beta\rangle - \sin\theta|\beta\alpha\rangle$. Vektor eigen atas tegak lurus padanya.

*Cara berpikir:* masalah dua tingkat yang terkopel ini muncul berulang-ulang dalam kimia kuantum: orbital ikatan dan antiikatan (subbab 11.4), sistem dua keadaan amonia (Contoh 4.44), dan pencampuran konfigurasi (Bab 17). Selalu ada sudut pencampuran dengan $\tan2\theta$ = kopling/selisih energi, dan tingkat-tingkat selalu saling menolak.

**Soal 53.** Dari soal sebelumnya, $k_c = \pi(20)/\sqrt2 = 44{,}4$ s⁻¹ dan $\Delta G^\ddagger = (8{,}314)(320)\ln[(1{,}381 \times 10^{-23})(320)/(6{,}626 \times 10^{-34})(44{,}4)] = 68{,}5$ kJ/mol. Dengan $\Delta\nu = 40$ Hz, $k_c = 88{,}9$ s⁻¹. Suhu koalesensi baru memenuhi $RT_c\ln(k_BT_c/hk_c) = 68{,}5$ kJ/mol; penyelesaian numerik (misalnya dengan `scipy.optimize.brentq`) memberi $T_c = 329$ K.

*Cara berpikir:* melipatduakan laju yang diperlukan hanya menaikkan $T_c$ sekitar 9 K, karena laju bergantung eksponensial pada suhu. Merekam pada dua kuat medan dan memeriksa bahwa $\Delta G^\ddagger$ yang diperoleh sama adalah cara sederhana menguji konsistensi analisis; analisis bentuk garis lengkap pada banyak suhu memberi $\Delta H^\ddagger$ dan $\Delta S^\ddagger$ secara terpisah.

**Soal 62.** Dengan $\omega = 2\pi\nu$:

$$
S(\omega) = \int_0^\infty e^{i(\Omega - \omega)t - t/T_2}\,dt = \frac{1}{1/T_2 - i(\Omega - \omega)} = \frac{T_2}{1 + i(\omega - \Omega)T_2} = \frac{T_2 - i(\omega - \Omega)T_2^2}{1 + (\omega - \Omega)^2T_2^2} .
$$

Bagian riil $T_2/[1 + (\omega - \Omega)^2T_2^2]$ adalah fungsi Lorentz (garis serapan) dengan puncak $T_2$ di $\omega = \Omega$; ia turun ke setengahnya bila $|\omega - \Omega| = 1/T_2$. Lebar penuh setengah tinggi $2/T_2$ dalam $\omega$, yaitu $1/\pi T_2$ dalam $\nu$. Bagian imajiner adalah garis dispersi.

*Cara berpikir:* bila FID tidak dimulai tepat dengan fase nol (karena keterlambatan penerima atau ofset fase), spektrum riil menjadi campuran serapan dan dispersi. "Koreksi fase" yang dilakukan setiap operator spektrometer adalah perkalian spektrum kompleks dengan $e^{i\phi}$ untuk memulihkan bentuk serapan murni.

**Soal 69.** Dengan $x = \omega_0\tau_c$, laju $1/T_1 \propto f(x)/\omega_0$, dengan $f(x) = \dfrac{x}{1 + x^2} + \dfrac{4x}{1 + 4x^2}$. Turunannya

$$
f'(x) = \frac{1 - x^2}{(1 + x^2)^2} + \frac{4(1 - 4x^2)}{(1 + 4x^2)^2} .
$$

Persamaan $f'(x) = 0$ diselesaikan secara numerik: $x = 0{,}616$, dengan $f = 1{,}425$. Untuk dua proton berjarak 1,52 Å pada 400 MHz, minimum itu terjadi pada $\tau_c = 0{,}245$ ns, dengan $T_1 = 0{,}127$ s (Gambar 16.8, panel c).

*Cara berpikir:* suku kedua (transisi dua kuanta pada $2\omega_0$) menggeser minimum dari $x = 1$, letak maksimum $x/(1 + x^2)$ saja, ke nilai yang lebih kecil. Mengukur $T_1$ pada beberapa suhu (yang mengubah $\tau_c$) dan menemukan minimumnya adalah cara klasik menentukan waktu korelasi dan energi pengaktifan gerak molekul dalam cairan dan padatan.

**Soal 83.** Untuk ion mirip hidrogen, $|\psi_{1s}(0)|^2 = Z^3/\pi a_0^3$, dan $a = \tfrac23\mu_0g_e\mu_Bg_N\mu_N|\psi(0)|^2$ sebanding dengan $g_NZ^3$. Untuk ³He⁺ ($Z = 2$):

$$
a = 1422{,}8\ \text{MHz} \times \frac{-4{,}2552}{5{,}5857} \times 2^3 = -8671\ \text{MHz} .
$$

*Cara berpikir:* nilai terukur $-8665{,}65$ MHz; selisih 0,06% berasal terutama dari koreksi massa tereduksi dan koreksi relativistik kecil. Tanda negatif berarti momen magnet ³He berlawanan dengan spinnya, sehingga tingkat $F = 1$ berada di bawah $F = 0$. Transisi ini, pada panjang gelombang 3,46 cm, diamati di nebula galaksi untuk mengukur kelimpahan ³He, salah satu saksi nukleosintesis awal alam semesta. Kopling hiperhalus sebanding dengan $Z^3$ juga menjelaskan mengapa kopling ESR atom berat (misalnya ion logam transisi dengan elektron s di inti) sangat besar.

# Bacaan lanjut

1. P. J. Hore, *Nuclear Magnetic Resonance*, edisi ke-2 (Oxford University Press, Oxford Chemistry Primers, 2015). Pengantar ringkas dan jernih: geseran, kopling, relaksasi, dan pulsa.
2. J. Keeler, *Understanding NMR Spectroscopy*, edisi ke-2 (Wiley, 2010). Model vektor, hasil kali operator, dan NMR dua dimensi dengan penurunan lengkap.
3. M. H. Levitt, *Spin Dynamics: Basics of Nuclear Magnetic Resonance*, edisi ke-2 (Wiley, 2008). Perlakuan kuantum yang teliti, dari spin tunggal sampai relaksasi.
4. T. D. W. Claridge, *High-Resolution NMR Techniques in Organic Chemistry*, edisi ke-3 (Elsevier, 2016). Rujukan praktis percobaan 1D dan 2D untuk penentuan struktur.
5. J. A. Weil dan J. R. Bolton, *Electron Paramagnetic Resonance: Elementary Theory and Practical Applications*, edisi ke-2 (Wiley, 2007). Faktor $g$, hiperhalus, hubungan McConnell, dan aplikasi ESR.
6. D. W. McRobbie, E. A. Moore, M. J. Graves, dan M. R. Prince, *MRI from Picture to Proton*, edisi ke-3 (Cambridge University Press, 2017). Prinsip MRI dari citra klinis sampai fisika spin.
