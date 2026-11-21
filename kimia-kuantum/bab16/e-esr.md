## 16.11 ESR: faktor g dan kopling hiperhalus

### Resonansi spin elektron

Semua yang telah kita bahas untuk spin inti berlaku pula untuk spin elektron, dengan dua perbedaan besar. Pertama, momen magnet elektron sekitar 658 kali momen proton, sehingga pada medan yang sama frekuensi resonansinya ratusan kali lebih tinggi: daerah gelombang mikro, bukan gelombang radio. Kedua, hanya molekul dengan **elektron tak berpasangan** yang memberi sinyal: radikal bebas, ion logam transisi, molekul dalam keadaan triplet, dan cacat dalam padatan. Molekul biasa dengan semua elektron berpasangan tidak terlihat sama sekali. Kelemahan ini sekaligus kekuatan: **resonansi spin elektron** (ESR, juga disebut EPR, *electron paramagnetic resonance*) melihat radikal pada konsentrasi mikromolar di tengah lautan molekul diamagnetik tanpa gangguan latar.

Hamiltonian Zeeman elektron ditulis dengan **faktor $g$** dan magneton Bohr $\mu_B = e\hbar/2m_e$:

$$
\hat H = g\mu_BB_0\hat S_z, \qquad E_{m_S} = g\mu_BB_0m_S, \quad m_S = \pm\tfrac12 . \qquad \text{(16.43)}
$$

Tanda positif karena elektron bermuatan negatif: momen magnetnya berlawanan dengan spinnya, sehingga keadaan $m_S = -\tfrac12$ ($\beta$) berenergi lebih rendah. Syarat resonansinya

$$
h\nu = g\mu_BB_0 . \qquad \text{(16.44)}
$$

Untuk elektron bebas, $g_e = 2{,}00232$; nilai 2 diramalkan oleh persamaan Dirac, dan kelebihan 0,00232 berasal dari elektrodinamika kuantum. Spektrometer ESR biasanya bekerja pada frekuensi gelombang mikro tetap (pita X, sekitar 9,5 GHz; pita Q, 35 GHz; pita W, 94 GHz) dan **menyapu medan** magnet; pada pita X resonansi terjadi di sekitar 0,34 T. Untuk menekan derau, medan dimodulasi sedikit dan sinyal dideteksi secara fase-peka, sehingga spektrum ESR lazim ditampilkan sebagai **turunan pertama** kurva serapan: setiap garis serapan tampak sebagai lengkung naik-turun yang memotong nol tepat di pusat garis.

### Faktor g sebagai sidik jari

Dalam molekul, $g$ menyimpang dari $g_e$ karena kopling spin–orbit (subbab 9.13) mencampurkan sedikit momentum sudut orbital ke dalam keadaan spin. Menurut teori perturbasi orde kedua,

$$
g \approx g_e - \frac{n\lambda}{\Delta E} , \qquad \text{(16.45)}
$$

dengan $\lambda$ tetapan kopling spin–orbit atom, $\Delta E$ jarak ke keadaan tereksitasi yang dapat dicampurkan, dan $n$ bilangan kecil yang bergantung pada orbital. Radikal organik yang tersusun dari atom ringan ($\lambda$ kecil) mempunyai $g$ sangat dekat dengan $g_e$: 2,0026 untuk radikal metil, 2,0028 untuk anion benzena, sekitar 2,004–2,006 untuk radikal dengan oksigen atau belerang. Ion logam transisi dengan $\lambda$ besar dan $\Delta E$ kecil (selisih tingkat d, subbab 14.2) mempunyai $g$ yang menyimpang jauh dan bergantung pada arah (anisotrop). Untuk Cu²⁺ ($d^9$) dalam oktahedron yang memanjang, $g_\parallel \approx 2{,}2$–2,4 dan $g_\perp \approx 2{,}05$. Pengukuran $g$ karena itu memberi informasi tentang susunan orbital d dan geometri koordinasi.

### Kopling hiperhalus

Elektron tak berpasangan berinteraksi dengan spin inti di sekitarnya. Dalam cairan, bagian yang bertahan dari perataan rotasi adalah interaksi kontak Fermi isotrop:

$$
\hat H = g\mu_BB_0\hat S_z + a\,\hat{\mathbf S}\cdot\hat{\mathbf I} , \qquad a = \frac23\mu_0g_e\mu_Bg_N\mu_N|\psi(0)|^2 . \qquad \text{(16.46)}
$$

**Tetapan kopling hiperhalus** $a$ sebanding dengan rapat spin elektron tepat di inti, $|\psi(0)|^2$, yang hanya tidak nol untuk karakter s (subbab 7.5). Karena $a \ll g\mu_BB_0$, pendekatan orde satu (seperti AX pada NMR) cukup: $E = g\mu_BB_0m_S + am_Sm_I$. Aturan seleksi ESR adalah $\Delta m_S = \pm1$ dengan $\Delta m_I = 0$ (gelombang mikro tidak membalik spin inti), sehingga pada frekuensi tetap garis-garis muncul pada medan

$$
B = B_0 - a'm_I , \qquad a' = \frac{a}{g\mu_B} , \qquad \text{(16.47)}
$$

dengan $a'$ tetapan hiperhalus dalam satuan medan (biasanya mT; 1 mT setara 28,0 MHz untuk $g = 2$). Satu inti berspin $I$ memecah garis menjadi $2I + 1$ garis sama kuat. Untuk $n$ inti setara berspin $\tfrac12$, berlaku aturan $n + 1$ dengan intensitas binomial, persis seperti multiplet NMR; untuk beberapa kelompok inti, pola dipecah bertahap. Banyaknya garis dan perbandingan intensitasnya langsung menunjukkan inti mana yang "dikunjungi" elektron tak berpasangan.

### Rapat spin dan hubungan McConnell

Dalam radikal π aromatik, elektron tak berpasangan menempati orbital π yang mempunyai simpul di bidang molekul, tempat proton berada. Bagaimana mungkin ia memberi kontak Fermi di proton? Jawabannya adalah **polarisasi spin**: elektron π tak berpasangan pada karbon sedikit mempolarisasi pasangan elektron ikatan C–H (menurut aturan Hund, elektron σ pada karbon yang sejajar dengan elektron π lebih disukai), sehingga di proton tertinggal sedikit rapat spin bertanda berlawanan. Harden McConnell (1956) merumuskan hubungan sederhana:

$$
a_\text{H} = Q\,\rho_\text{C} , \qquad Q \approx -2{,}3\ \text{sampai}\ -2{,}7\ \text{mT} , \qquad \text{(16.48)}
$$

dengan $\rho_\text{C}$ **rapat spin** elektron π pada atom karbon pembawa proton. Dalam teori orbital Hückel (subbab 13.4), rapat spin pada atom $r$ sama dengan kuadrat koefisien orbital yang ditempati satu elektron, $\rho_r = c_r^2$. Spektrum ESR karena itu adalah "foto" langsung orbital molekul tak berpasangan: SOMO (orbital terisi tunggal) radikal anion adalah LUMO molekul netral.

![Gambar 16.10 Spektrum ESR (turunan pertama) simulasi pada pita X. (a) Radikal metil: kuartet 1 : 3 : 3 : 1 dengan a = 2,30 mT. (b) Anion benzena: septet 1 : 6 : 15 : 20 : 15 : 6 : 1 dengan a = 0,375 mT. (c) Radikal nitroksida: triplet 1 : 1 : 1 dari ¹⁴N (I = 1) dengan a = 1,6 mT.](fig/c_esr.png){width=92%}

::: {.terapan}
**ESR dalam kimia, biologi, dan arkeologi**

ESR mendeteksi radikal antara dalam reaksi kimia dan polimerisasi. Radikal yang terlalu singkat umurnya ditangkap dengan **perangkap spin** seperti DMPO, yang bereaksi membentuk radikal nitroksida yang stabil; pola hiperhalus nitroksida itu mengungkap radikal asalnya. Dalam biologi, **label spin** nitroksida yang dipasang pada protein mengukur gerak lokal (bentuk garis) dan jarak antara dua label sampai sekitar 8 nm (teknik pulsa DEER). Radikal tirosil dalam fotosistem II dan ribonukleotida reduktase ditemukan dengan ESR. Dalam padatan, radiasi pengion menciptakan radikal yang terperangkap: konsentrasinya dalam alanina dipakai sebagai dosimeter radiasi, dan dalam email gigi fosil sebagai jam untuk penanggalan arkeologis sampai jutaan tahun.
:::

::: {.contoh}
**Contoh 16.48 · Medan resonansi dan faktor g**

(a) Hitung medan resonansi elektron bebas pada 9,500 GHz, 35,00 GHz, dan 94,00 GHz. (b) Suatu radikal pada 9,400 GHz beresonansi di 335,50 mT. Berapa $g$-nya?

**Penyelesaian.** (a) $B = h\nu/g_e\mu_B$: 339,0 mT; 1,249 T; 3,354 T. Faktor konversi $g_e\mu_B/h = 28{,}02$ GHz/T.

\(b) $g = h\nu/\mu_BB = (6{,}6261 \times 10^{-34})(9{,}400 \times 10^9)/(9{,}2740 \times 10^{-24})(0{,}33550) = 2{,}0018$.

**Memahami hasil.** Penentuan $g$ sampai empat desimal memerlukan pengukuran frekuensi dan medan yang teliti; dalam praktik dipakai bahan rujukan seperti DPPH ($g = 2{,}0036$). Selisih $g$ yang kecil lebih mudah dibedakan pada pita W, karena pemisahan medan antara dua garis dengan $g$ berbeda sebanding dengan frekuensi, sedangkan pemisahan hiperhalus tidak, analog dengan geseran kimia dan $J$ dalam NMR.
:::

::: {.contoh}
**Contoh 16.49 · Hiperhalus atom hidrogen dan garis 21 cm**

Hitung $a$ untuk atom hidrogen pada keadaan 1s dengan (16.46), memakai $|\psi_{1s}(0)|^2 = 1/\pi a_0^3$. Nyatakan dalam MHz, mT, dan panjang gelombang transisi antara tingkat $F = 1$ dan $F = 0$ dalam medan nol.

**Penyelesaian.**

$$
\frac ah = \frac{\tfrac23(1{,}2566 \times 10^{-6})(2{,}0023)(9{,}2740 \times 10^{-24})(5{,}5857)(5{,}0508 \times 10^{-27})}{\pi(5{,}2918 \times 10^{-11})^3(6{,}6261 \times 10^{-34})} = 1{,}4228 \times 10^9\ \text{Hz} .
$$

Dalam satuan medan $a' = a/g_e\mu_B = 50{,}8$ mT. Dalam medan nol, $a\hat{\mathbf S}\cdot\hat{\mathbf I}$ memisahkan triplet $F = 1$ ($+a/4$) dan singlet $F = 0$ ($-3a/4$) sebesar $a$, sehingga $\lambda = c/(a/h) = 21{,}1$ cm.

**Memahami hasil.** Nilai terukur 1420,406 MHz; selisih 0,2% hilang bila massa tereduksi elektron–proton dipakai dalam $a_0$, yang memperbesar jari-jari dan mengecilkan $|\psi(0)|^2$ dengan faktor $(1 + m_e/m_p)^{-3}$, memberi 1420,5 MHz. Inilah garis 21 cm radioastronomi (subbab 7.11), salah satu frekuensi yang paling teliti diketahui manusia. Dalam spektrum ESR atom H yang terperangkap, kedua garis terpisah 50,7 mT, jauh lebih lebar daripada pemisahan hiperhalus radikal organik, karena di sini elektron sepenuhnya berada di orbital s di sekitar proton.
:::

::: {.contoh}
**Contoh 16.50 · Radikal metil**

Radikal ·CH₃ ($g = 2{,}0026$, $a_\text{H} = -2{,}30$ mT untuk ketiga proton) direkam pada 9,500 GHz. Tentukan pusat spektrum dan letak garis-garisnya.

**Penyelesaian.** $B_0 = h\nu/g\mu_B = 338{,}94$ mT. Tiga proton setara: $M_I = \pm\tfrac32, \pm\tfrac12$, empat garis berintensitas 1 : 3 : 3 : 1 pada $B_0 \pm 3{,}45$ dan $B_0 \pm 1{,}15$ mT: 335,49; 337,79; 340,09; 342,39 mT.

**Memahami hasil.** Tanda negatif $a_\text{H}$ (polarisasi spin, bukan rapat langsung) tidak terlihat pada spektrum orde satu; ia ditentukan dengan teknik lain, misalnya ENDOR. Besarnya, 2,30 mT, memberi $\rho_\text{C} \approx 1$ menurut McConnell: elektron tak berpasangan sepenuhnya pada orbital 2p karbon. Radikal metil yang datar (sp²) adalah asal nilai $Q$; bila radikal menjadi piramidal, karakter s masuk ke orbital SOMO dan kopling ¹³C naik tajam, sehingga ESR juga mengukur geometri radikal.
:::

::: {.contoh}
**Contoh 16.51 · Anion benzena dan nilai Q**

Spektrum ESR anion radikal benzena terdiri atas tujuh garis dengan jarak 0,375 mT. Tentukan intensitas relatif garis dan taksir $Q$ dengan menganggap elektron tersebar merata pada enam karbon.

**Penyelesaian.** Enam proton setara: tujuh garis 1 : 6 : 15 : 20 : 15 : 6 : 1. Dengan $\rho = \tfrac16$: $|Q| = 0{,}375 \times 6 = 2{,}25$ mT.

**Memahami hasil.** Keenam proton setara karena elektron tambahan "berputar" di seluruh cincin: LUMO benzena terdegenerasi ganda ($e_{2u}$), dan rata-rata rapat spinnya sama pada semua karbon. Garis terluar hanya $1/64$ dari total intensitas, sehingga sering hilang dalam derau; menghitung garis yang tampak tanpa memperhitungkan intensitas binomial adalah kesalahan umum.
:::

::: {.contoh}
**Contoh 16.52 · Anion naftalena dari Hückel**

Hitung rapat spin anion naftalena dengan teori Hückel: diagonalkan matriks keterhubungan sepuluh atom karbon, ambil LUMO molekul netral, dan kuadratkan koefisiennya. Ramalkan $a_\text{H}$ untuk proton α (posisi 1, 4, 5, 8) dan β (2, 3, 6, 7) dengan $Q = -2{,}7$ mT. Berapa banyak garis yang diharapkan? Data: $|a_\alpha| = 0{,}495$ mT, $|a_\beta| = 0{,}183$ mT.

**Penyelesaian.** Diagonalisasi (dengan `numpy.linalg.eigh`) memberi LUMO berenergi $\alpha - 0{,}618\beta$, dengan $c^2 = 0{,}181$ pada keempat posisi α, $0{,}069$ pada posisi β, dan nol pada dua karbon jembatan. Maka $|a_\alpha| = 2{,}7 \times 0{,}181 = 0{,}49$ mT dan $|a_\beta| = 2{,}7 \times 0{,}069 = 0{,}19$ mT. Dua kelompok empat proton setara: $(4 + 1)(4 + 1) = 25$ garis, berupa kuintet dari kuintet.

**Memahami hasil.** Teori orbital molekul paling sederhana meramalkan kopling dengan galat beberapa persen. Kesesuaian semacam ini, pada tahun 1950-an, adalah salah satu bukti percobaan paling meyakinkan bahwa orbital molekul Hückel bukan sekadar alat hitung, tetapi menggambarkan sebaran elektron yang nyata. Rapat spin nol pada karbon jembatan juga sesuai: kopling ¹³C pada posisi itu sangat kecil.
:::

::: {.contoh}
**Contoh 16.53 · Label spin nitroksida**

Radikal nitroksida TEMPO mempunyai elektron tak berpasangan terutama pada gugus N–O, dengan $a_\text{N} = 1{,}6$ mT. (a) Ramalkan spektrumnya. (b) Bagaimana spektrumnya bila ¹⁴N diganti ¹⁵N ($\gamma_{^{15}\text{N}}/\gamma_{^{14}\text{N}} = -1{,}403$)?

**Penyelesaian.** (a) ¹⁴N berspin 1: triplet 1 : 1 : 1 dengan jarak 1,6 mT (proton metil memberi kopling sangat kecil yang hanya melebarkan garis). (b) ¹⁵N berspin $\tfrac12$: doblet dengan $|a| = 1{,}6 \times 1{,}403 = 2{,}2$ mT.

**Memahami hasil.** Karena $a$ sebanding dengan $g_N$ inti, penggantian isotop menunjukkan dengan pasti inti mana yang menyebabkan pemecahan. Bentuk garis nitroksida sangat peka terhadap gerak: label yang berputar bebas memberi tiga garis tajam sama tinggi, sedangkan label yang terikat kaku pada protein memberi garis lebar dan tak simetris karena anisotropi $g$ dan $a$ tidak lagi dirata-ratakan. Inilah dasar pemakaian label spin untuk mengukur dinamika makromolekul.
:::

::: {.contoh}
**Contoh 16.54 · Faktor g tembaga(II)**

Untuk ion Cu²⁺ ($d^9$) dalam oktahedron yang memanjang sepanjang $z$, lubang tunggal berada pada orbital $d_{x^2-y^2}$, dan $g_\parallel \approx g_e - 8\lambda/\Delta$, dengan $\Delta$ jarak energi ke orbital $d_{xy}$. Taksir $g_\parallel$ untuk $\lambda = -830$ cm⁻¹ dan $\Delta = 15\,000$ cm⁻¹. Nilai terukur kompleks Cu(II) dengan ligan N dan O biasanya 2,2–2,3. Apa yang menyebabkan selisihnya?

**Penyelesaian.** $g_\parallel = 2{,}0023 + 8(830)/15\,000 = 2{,}0023 + 0{,}443 = 2{,}45$.

**Memahami hasil.** Tanda $\lambda$ negatif untuk kulit yang lebih dari setengah penuh (berperilaku sebagai "lubang") membuat $g > g_e$. Taksiran ion bebas terlalu besar karena ikatan kovalen dengan ligan menyebarkan orbital d ke ligan dan mengurangi momentum sudut orbital efektifnya (faktor reduksi orbital, biasanya 0,6–0,8 bila dikalikan pada suku koreksi). Perbandingan $g_\parallel$ dengan nilai ion bebas menjadi ukuran kovalensi ikatan logam–ligan, misalnya pada protein tembaga biru.
:::

::: {.kuis}
**Kuis cepat 16.11**

Berapa banyak garis ESR radikal ·CD₃ (deuterium berspin 1)? Mengapa molekul O₂ dalam gas memberi sinyal ESR, sedangkan N₂ tidak?
:::

## 16.12 MRI

### Dari frekuensi ke posisi

Pencitraan resonansi magnetik (MRI) memakai proton air dan lemak dalam tubuh. Gagasan dasarnya, yang dikemukakan Paul Lauterbur pada tahun 1973, sangat sederhana: tambahkan pada medan $B_0$ yang seragam suatu **gradien medan** yang membuat medan berubah lurus terhadap posisi, misalnya $B(x) = B_0 + G_xx$. Maka frekuensi resonansi bergantung pada posisi:

$$
\nu(x) = \frac{\gamma}{2\pi}(B_0 + G_xx) . \qquad \text{(16.49)}
$$

Spektrum NMR sampel yang direkam selama gradien menyala menjadi **proyeksi** banyaknya proton sepanjang $x$: setiap frekuensi berasal dari satu irisan bidang $x$ = tetap. Gradien biasanya 10–40 mT/m, yang untuk proton ($\gamma/2\pi = 42{,}58$ MHz/T) berarti beberapa kilohertz per sentimeter. Karena perbedaan geseran kimia (beberapa ppm, yaitu ratusan Hz pada 1,5 T) kecil dibandingkan sebaran frekuensi karena gradien, geseran kimia hampir diabaikan dalam pencitraan biasa; yang dicitrakan adalah sebaran air.

Untuk citra tiga dimensi, tiga gradien yang tegak lurus dipakai dengan tiga peran berbeda:

1. **Pemilihan irisan.** Gradien $G_z$ menyala selama pulsa yang pita frekuensinya sempit (pulsa berbentuk, berdurasi beberapa milidetik). Hanya proton dalam irisan $z$ yang frekuensinya jatuh dalam pita pulsa yang tereksitasi. Tebal irisan $\Delta z = \Delta f/(\gamma G_z/2\pi)$.
2. **Pengkodean frekuensi.** Gradien $G_x$ menyala selama FID direkam, sehingga posisi $x$ dikodekan sebagai frekuensi.
3. **Pengkodean fase.** Gradien $G_y$ menyala sebentar sebelum perekaman, sehingga spin pada posisi $y$ yang berbeda mendapat fase yang berbeda. Percobaan diulang dengan besar $G_y$ yang berbeda-beda, misalnya 256 kali.

### Ruang-k dan transformasi Fourier

Sinyal yang direkam dapat ditulis sebagai

$$
s(k_x, k_y) = \iint\rho(x, y)\,e^{-i2\pi(k_xx + k_yy)}\,dx\,dy, \qquad k_x = \frac{\gamma}{2\pi}\int G_x\,dt , \qquad \text{(16.50)}
$$

dan $k_y$ serupa. Data mentah MRI adalah transformasi Fourier dua dimensi citra $\rho(x, y)$, diambil titik demi titik di **ruang-k**; citranya diperoleh dengan transformasi Fourier balik. Ini adalah gagasan yang sama dengan NMR 2D (subbab 16.10): satu sumbu direkam langsung, sumbu lain dibangun dari percobaan berulang. Langkah ruang-k menentukan medan pandang (FOV = $1/\Delta k$) dan jangkauan ruang-k menentukan resolusi ($\Delta x$ = FOV/$N$). Sumbangan Peter Mansfield, yang mempercepat perekaman ruang-k hingga satu citra dalam puluhan milidetik (pencitraan gema-planar), dan gagasan Lauterbur diganjar Hadiah Nobel Fisiologi atau Kedokteran 2003.

### Kontras: T₁, T₂, dan bahan kontras

Kerapatan proton dalam jaringan lunak hanya berbeda beberapa puluh persen, sehingga citra kerapatan saja kurang kontras. Kekuatan MRI terletak pada perbedaan **waktu relaksasi** antarjaringan (subbab 16.9). Pada urutan gema spin dengan waktu ulang $T_R$ dan waktu gema $T_E$, sinyal suatu jaringan kira-kira

$$
S \propto \rho\left(1 - e^{-T_R/T_1}\right)e^{-T_E/T_2} . \qquad \text{(16.51)}
$$

$T_R$ pendek dan $T_E$ pendek menghasilkan citra **berbobot T₁**: jaringan dengan $T_1$ pendek (lemak, materi putih) terang, cairan serebrospinal (CSS, $T_1$ panjang) gelap. $T_R$ panjang dan $T_E$ panjang menghasilkan citra **berbobot T₂**: cairan dengan $T_2$ panjang terang. Banyak penyakit, seperti peradangan dan tumor, menambah kandungan air bebas jaringan dan memanjangkan $T_2$, sehingga tampak terang pada citra berbobot T₂.

**Bahan kontras** gadolinium memperpendek $T_1$ air di sekitarnya. Ion Gd³⁺ mempunyai tujuh elektron f tak berpasangan ($S = \tfrac72$), momen magnet yang sangat besar, dan relaksasi elektron yang cukup lambat sehingga fluktuasi medannya efektif merelaksasi proton air. Agar tidak beracun, Gd³⁺ dibungkus dalam kelat yang sangat stabil, tetapi satu molekul air tetap terkoordinasi langsung dan bertukar cepat dengan air ruah: setiap ion Gd³⁺ "melayani" jutaan molekul air per detik. Kemampuan memperpendek $T_1$ dinyatakan sebagai **relaksivitas** $r_1$, sekitar 4 mM⁻¹ s⁻¹ untuk kelat klinis: $1/T_1 = 1/T_{1,0} + r_1[\text{Gd}]$. Perancangan kelat yang relaksivitasnya lebih besar adalah bidang kimia koordinasi yang aktif.

**MRI fungsional** (fMRI) memanfaatkan sifat magnet darah. Deoksihemoglobin mengandung Fe²⁺ spin tinggi ($S = 2$, paramagnetik), sedangkan oksihemoglobin diamagnetik. Daerah otak yang aktif menerima darah beroksigen lebih banyak daripada yang dikonsumsinya, sehingga kadar deoksihemoglobin turun, ketidakseragaman medan lokal berkurang, $T_2^*$ memanjang, dan sinyal naik beberapa persen. Kontras **BOLD** (*blood-oxygen-level dependent*) ini memetakan aktivitas otak tanpa zat apa pun yang disuntikkan.

![Gambar 16.11 Prinsip MRI. (a) Gradien G_x membuat frekuensi resonansi bergantung lurus pada posisi; spektrum sampel berisi dua tabung air menjadi proyeksi kerapatan proton. (b) Sinyal relatif materi putih, materi abu-abu, dan CSS menurut (16.51) untuk pembobotan T₁ (T_R = 500 ms, T_E = 15 ms) dan T₂ (T_R = 4000 ms, T_E = 100 ms).](fig/c_mri.png){width=94%}

::: {.contoh}
**Contoh 16.55 · Gradien dan sebaran frekuensi**

Dalam magnet 1,5 T, gradien $G_x = 10$ mT/m dipasang. Hitung frekuensi Larmor pusat, sebaran frekuensi per sentimeter, dan selisih frekuensi antara dua titik berjarak 20 cm. Bandingkan dengan selisih geseran kimia air dan lemak (3,5 ppm).

**Penyelesaian.** $\nu_0 = 42{,}58 \times 1{,}5 = 63{,}9$ MHz. Sebaran: $42{,}58\ \text{MHz/T} \times 0{,}010\ \text{T/m} = 425{,}8$ kHz/m $= 4{,}26$ kHz/cm. Pada 20 cm: 85 kHz. Selisih air–lemak: $3{,}5 \times 63{,}9 = 224$ Hz.

**Memahami hasil.** Geseran kimia 224 Hz setara dengan pergeseran posisi sekitar 0,5 mm pada gradien ini. Pada citra beresolusi tinggi, pergeseran ini tampak sebagai "artefak geseran kimia": jaringan lemak sedikit bergeser terhadap jaringan berair di sekitarnya. Teknik penekanan lemak memanfaatkan selisih frekuensi yang sama untuk mengeksitasi air saja.
:::

::: {.contoh}
**Contoh 16.56 · Tebal irisan dan resolusi**

(a) Pulsa pemilih irisan mempunyai lebar pita 1,0 kHz dan $G_z = 10$ mT/m. Hitung tebal irisan. (b) Citra dengan medan pandang 24 cm direkam dengan 256 langkah pengkodean fase. Berapa ukuran piksel?

**Penyelesaian.** (a) $\Delta z = 1000/(425\,800\ \text{Hz/m}) = 2{,}3$ mm. (b) $240/256 = 0{,}94$ mm.

**Memahami hasil.** Voksel berukuran sekitar 1 × 1 × 2 mm berisi sekitar $10^{20}$ proton air, cukup untuk sinyal yang baik dalam beberapa menit pada 1,5 T. Resolusi yang lebih halus memerlukan voksel yang lebih kecil, sehingga sinyal per voksel berkurang dan waktu perekaman harus naik; itulah alasan peralihan ke magnet 3 T dan 7 T untuk pencitraan otak beresolusi tinggi.
:::

::: {.contoh}
**Contoh 16.57 · Pembobotan T₁ dan T₂**

Pada 1,5 T, kira-kira: materi putih ($T_1 = 600$ ms, $T_2 = 80$ ms, $\rho = 0{,}70$), materi abu-abu (950 ms, 100 ms, 0,80), CSS (4000 ms, 2000 ms, 1,00). Hitung sinyal relatif menurut (16.51) untuk (a) $T_R = 500$ ms, $T_E = 15$ ms, dan (b) $T_R = 4000$ ms, $T_E = 100$ ms.

**Penyelesaian.** (a) Materi putih $0{,}70(1 - e^{-500/600})e^{-15/80} = 0{,}33$; materi abu-abu 0,28; CSS 0,12. (b) Materi putih 0,20; materi abu-abu 0,29; CSS 0,60.

**Memahami hasil.** Urutan kecerahan terbalik sama sekali: pada citra berbobot T₁ materi putih paling terang dan CSS gelap, sehingga anatomi tampak jelas; pada citra berbobot T₂ CSS paling terang, sehingga cairan dan edema menonjol. Dokter radiologi membaca kedua jenis citra bersama, karena keduanya mengungkap sifat jaringan yang berbeda. Semua ini bersumber dari teori relaksasi yang sama dengan Contoh 16.40: air yang terikat pada makromolekul bergerak lebih lambat, sehingga relaksasinya lebih cepat.
:::

::: {.contoh}
**Contoh 16.58 · Bahan kontras gadolinium**

Jaringan dengan $T_1 = 1{,}0$ s menyerap bahan kontras sampai [Gd] = 0,50 mM. Dengan $r_1 = 4{,}0$ mM⁻¹ s⁻¹, berapa $T_1$ yang baru? Berapa kenaikan sinyal pada citra berbobot T₁ dengan $T_R = 500$ ms (abaikan pengaruh $T_2$)?

**Penyelesaian.** $1/T_1 = 1{,}0 + 4{,}0 \times 0{,}50 = 3{,}0$ s⁻¹, $T_1 = 0{,}33$ s. Sinyal sebanding dengan $1 - e^{-T_R/T_1}$: sebelum $1 - e^{-0{,}5} = 0{,}39$; sesudah $1 - e^{-1{,}5} = 0{,}78$. Sinyal naik dua kali.

**Memahami hasil.** Jaringan yang menyerap bahan kontras, misalnya tumor dengan pembuluh darah yang bocor, menjadi terang. Konsentrasi setengah milimolar sangat kecil dibandingkan konsentrasi air (55 M), tetapi cukup karena setiap ion Gd³⁺ bekerja sebagai katalis relaksasi bagi banyak sekali molekul air yang bergantian singgah di dekatnya.
:::

::: {.kuis}
**Kuis cepat 16.12**

Mengapa MRI tidak memerlukan radiasi pengion? Bila gradien $G_x$ dilipatduakan dengan lebar pita penerima tetap, bagaimana medan pandang sepanjang $x$ berubah?
:::

### Menuju bab berikutnya

Semua bab sebelumnya memakai model yang dapat dihitung dengan tangan. Bab 17 menutup buku ini dengan kimia komputasi, cara program modern menyelesaikan persamaan Schrödinger untuk molekul nyata.
