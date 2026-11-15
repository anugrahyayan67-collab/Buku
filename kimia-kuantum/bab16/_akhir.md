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

%%SOAL%%

# Jawaban

%%JAWABAN%%

# Pembahasan soal terpilih

**Soal {{dnp}}.** Polarisasi Boltzmann ¹³C pada 9,40 T ($\nu_0 = 100{,}6$ MHz) dan 298 K adalah $P = \tanh(h\nu_0/2k_BT) = 8{,}10 \times 10^{-6}$. Perbandingannya $0{,}30/8{,}10 \times 10^{-6} = 3{,}7 \times 10^4$. Karena S/N sebanding dengan $\sqrt n$, satu perekaman hiperpolarisasi setara dengan $(3{,}7 \times 10^4)^2 \approx 1{,}4 \times 10^9$ perekaman biasa; dengan jeda 10 s per perekaman, itu lebih dari empat abad.

*Cara berpikir:* hiperpolarisasi tidak mengubah batas Boltzmann; ia "meminjam" polarisasi dari sistem lain (elektron pada suhu rendah) lalu membawanya ke suhu kamar lebih cepat daripada spin sempat berelaksasi. Akibatnya polarisasi itu fana: ia meluruh dengan $T_1$ ¹³C, biasanya beberapa puluh detik, sehingga percobaan harus diselesaikan dalam satu atau beberapa pulsa kecil. Itulah sebabnya karbon karbonil piruvat, yang $T_1$-nya panjang karena tidak mengikat proton, dipilih untuk pencitraan metabolik.

**Soal {{gauss}}.** Fungsi ternormalisasi $\psi = (2\alpha/\pi)^{3/4}e^{-\alpha r^2}$ memberi

$$
\left\langle\frac1r\right\rangle = 4\pi\left(\frac{2\alpha}{\pi}\right)^{3/2}\int_0^\infty r\,e^{-2\alpha r^2}dr = 4\pi\left(\frac{2\alpha}{\pi}\right)^{3/2}\frac{1}{4\alpha} = 2\sqrt{\frac{2\alpha}{\pi}} .
$$

Dengan $\alpha = 8/9\pi$: $2\alpha/\pi = 16/9\pi^2$, sehingga $\langle 1/r\rangle = 8/3\pi = 0{,}849$ (satuan atom). Maka $\sigma_d = 0{,}849 \times 17{,}75 = 15{,}1$ ppm, 15% di bawah nilai tepat.

*Cara berpikir:* energi fungsi uji Gauss ini hanya 15% di atas energi tepat, dan galat perisainya sama besar, karena keduanya bergantung pada $\langle 1/r\rangle$ (melalui teorema virial, $E = -\tfrac12\langle 1/r\rangle$ di titik optimum). Fungsi Gauss tidak mempunyai taring di inti, sehingga rapat elektronnya di dekat inti terlalu kecil. Sifat yang peka terhadap daerah dekat inti, seperti perisai NMR dan kopling hiperhalus, karena itu memerlukan basis Gauss yang diperkaya fungsi-fungsi curam (Bab 17).

**Soal {{orde2}}.** Energi orde nol $E_{\alpha\beta}/h = -\tfrac12\Delta\nu - \tfrac14J$ dan $E_{\beta\alpha}/h = \tfrac12\Delta\nu - \tfrac14J$, dengan selisih $E_{\alpha\beta} - E_{\beta\alpha} = -h\Delta\nu$. Unsur matriks penghubungnya $\tfrac12J$. Menurut teori perturbasi orde dua (subbab 8.7):

$$
E^{(2)}_{\alpha\beta} = \frac{(\tfrac12J)^2}{-\Delta\nu} = -\frac{J^2}{4\Delta\nu}, \qquad E^{(2)}_{\beta\alpha} = +\frac{J^2}{4\Delta\nu}
$$

(dalam satuan frekuensi). Dari rumus tepat, $D = \Delta\nu\sqrt{1 + J^2/\Delta\nu^2} \approx \Delta\nu + J^2/2\Delta\nu$, sehingga $-\tfrac14J \mp \tfrac12D \approx -\tfrac14J \mp \tfrac12\Delta\nu \mp J^2/4\Delta\nu$: sama.

*Cara berpikir:* kedua tingkat tengah "saling tolak", sehingga garis-garis bergeser sebesar $J^2/4\Delta\nu$. Untuk gugus etil pada 60 MHz ($J = 7$ Hz, $\Delta\nu = 148$ Hz), pergeserannya 0,08 Hz, kecil dibandingkan lebar garis; efek orde dua yang terlihat lebih dahulu adalah perubahan intensitas (atap), yang sebanding dengan $J/\Delta\nu$, bukan $(J/\Delta\nu)^2$.

**Soal {{abeig}}.** Matriks (16.26) berbentuk $-\tfrac14J\,\mathbf 1 + \begin{pmatrix}-\tfrac12\Delta\nu & \tfrac12J\\ \tfrac12J & \tfrac12\Delta\nu\end{pmatrix}$. Matriks kedua mempunyai jejak nol dan determinan $-\tfrac14(\Delta\nu^2 + J^2)$, sehingga nilai eigennya $\pm\tfrac12D$; seluruhnya $-\tfrac14J \pm \tfrac12D$. Untuk nilai eigen bawah $-\tfrac14J - \tfrac12D$, baris pertama persamaan eigen memberi $\tfrac12(D - \Delta\nu)v_1 + \tfrac12Jv_2 = 0$, jadi $v_2/v_1 = -(D - \Delta\nu)/J$. Dengan $\cos2\theta = \Delta\nu/D$ dan $\sin2\theta = J/D$, identitas $\tan\theta = \sin2\theta/(1 + \cos2\theta) = J/(D + \Delta\nu) = (D - \Delta\nu)/J$ (karena $(D - \Delta\nu)(D + \Delta\nu) = J^2$) memberi $v_2/v_1 = -\tan\theta$, yaitu $|2\rangle = \cos\theta|\alpha\beta\rangle - \sin\theta|\beta\alpha\rangle$. Vektor eigen atas tegak lurus padanya.

*Cara berpikir:* masalah dua tingkat yang terkopel ini muncul berulang-ulang dalam kimia kuantum: orbital ikatan dan antiikatan (subbab 11.4), sistem dua keadaan amonia (Contoh 4.49), dan pencampuran konfigurasi (Bab 17). Selalu ada sudut pencampuran dengan $\tan2\theta$ = kopling/selisih energi, dan tingkat-tingkat selalu saling menolak.

**Soal {{koal}}.** Dari soal sebelumnya, $k_c = \pi(20)/\sqrt2 = 44{,}4$ s⁻¹ dan $\Delta G^\ddagger = (8{,}314)(320)\ln[(1{,}381 \times 10^{-23})(320)/(6{,}626 \times 10^{-34})(44{,}4)] = 68{,}5$ kJ/mol. Dengan $\Delta\nu = 40$ Hz, $k_c = 88{,}9$ s⁻¹. Suhu koalesensi baru memenuhi $RT_c\ln(k_BT_c/hk_c) = 68{,}5$ kJ/mol; penyelesaian numerik (misalnya dengan `scipy.optimize.brentq`) memberi $T_c = 329$ K.

*Cara berpikir:* melipatduakan laju yang diperlukan hanya menaikkan $T_c$ sekitar 9 K, karena laju bergantung eksponensial pada suhu. Merekam pada dua kuat medan dan memeriksa bahwa $\Delta G^\ddagger$ yang diperoleh sama adalah cara sederhana menguji konsistensi analisis; analisis bentuk garis lengkap pada banyak suhu memberi $\Delta H^\ddagger$ dan $\Delta S^\ddagger$ secara terpisah.

**Soal {{lorentz}}.** Dengan $\omega = 2\pi\nu$:

$$
S(\omega) = \int_0^\infty e^{i(\Omega - \omega)t - t/T_2}\,dt = \frac{1}{1/T_2 - i(\Omega - \omega)} = \frac{T_2}{1 + i(\omega - \Omega)T_2} = \frac{T_2 - i(\omega - \Omega)T_2^2}{1 + (\omega - \Omega)^2T_2^2} .
$$

Bagian riil $T_2/[1 + (\omega - \Omega)^2T_2^2]$ adalah fungsi Lorentz (garis serapan) dengan puncak $T_2$ di $\omega = \Omega$; ia turun ke setengahnya bila $|\omega - \Omega| = 1/T_2$. Lebar penuh setengah tinggi $2/T_2$ dalam $\omega$, yaitu $1/\pi T_2$ dalam $\nu$. Bagian imajiner adalah garis dispersi.

*Cara berpikir:* bila FID tidak dimulai tepat dengan fase nol (karena keterlambatan penerima atau ofset fase), spektrum riil menjadi campuran serapan dan dispersi. "Koreksi fase" yang dilakukan setiap operator spektrometer adalah perkalian spektrum kompleks dengan $e^{i\phi}$ untuk memulihkan bentuk serapan murni.

**Soal {{bpp}}.** Dengan $x = \omega_0\tau_c$, laju $1/T_1 \propto f(x)/\omega_0$, dengan $f(x) = \dfrac{x}{1 + x^2} + \dfrac{4x}{1 + 4x^2}$. Turunannya

$$
f'(x) = \frac{1 - x^2}{(1 + x^2)^2} + \frac{4(1 - 4x^2)}{(1 + 4x^2)^2} .
$$

Persamaan $f'(x) = 0$ diselesaikan secara numerik: $x = 0{,}616$, dengan $f = 1{,}425$. Untuk dua proton berjarak 1,52 Å pada 400 MHz, minimum itu terjadi pada $\tau_c = 0{,}245$ ns, dengan $T_1 = 0{,}127$ s (Gambar 16.8, panel c).

*Cara berpikir:* suku kedua (transisi dua kuanta pada $2\omega_0$) menggeser minimum dari $x = 1$, letak maksimum $x/(1 + x^2)$ saja, ke nilai yang lebih kecil. Mengukur $T_1$ pada beberapa suhu (yang mengubah $\tau_c$) dan menemukan minimumnya adalah cara klasik menentukan waktu korelasi dan energi pengaktifan gerak molekul dalam cairan dan padatan.

**Soal {{he3}}.** Untuk ion mirip hidrogen, $|\psi_{1s}(0)|^2 = Z^3/\pi a_0^3$, dan $a = \tfrac23\mu_0g_e\mu_Bg_N\mu_N|\psi(0)|^2$ sebanding dengan $g_NZ^3$. Untuk ³He⁺ ($Z = 2$):

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
