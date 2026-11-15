## 5.4 Tingkat energi dan energi titik nol

### Tangga yang berjarak sama

Tingkat energi osilator harmonik (5.12) membentuk tangga dengan anak tangga yang sama tinggi, $\hbar\omega$. Ini berbeda dari partikel dalam kotak (selang membesar seperti $2n + 1$) dan dari atom hidrogen (selang mengecil seperti $1/n^3$). Jarak yang sama ini berasal dari bentuk parabola potensial: makin tinggi energi, makin lebar daerah yang tersedia, tepat dalam takaran yang membuat setiap tambahan simpul memerlukan energi yang sama.

Hasil Planck tahun 1900, $E_n = nh\nu$, ternyata hampir benar: yang kurang hanya energi titik nol $\tfrac12h\nu$. Karena semua tingkat bergeser sama banyak, energi titik nol tidak mengubah rumus radiasi benda hitam maupun kapasitas kalor Einstein (subbab 1.3); ia hanya menggeser titik nol energi. Tetapi dalam kimia, energi titik nol sangat penting, karena ia berbeda untuk molekul yang berbeda dan isotop yang berbeda.

### Energi titik nol dan energi disosiasi

Energi yang diperlukan untuk memutus ikatan dari keadaan dasar getaran disebut **energi disosiasi** $D_0$. Ia lebih kecil daripada kedalaman sumur energi potensial, $D_e$, sebesar energi titik nol:

$$
D_0 = D_e - E_0 \approx D_e - \tfrac12h\nu . \qquad \text{(5.14)}
$$

$D_e$ adalah besaran yang dihitung dalam kimia komputasi (energi elektronik dari dasar kurva); $D_0$ adalah yang diukur secara termokimia atau spektroskopi. Untuk H₂, selisihnya 0,27 eV (26 kJ/mol): selisih yang harus selalu diperhitungkan bila membandingkan hasil perhitungan dengan percobaan.

### Populasi termal

Pada suhu $T$, perbandingan populasi tingkat getaran mengikuti faktor Boltzmann (subbab 1.10). Karena semua tingkat berjarak sama, fungsi partisi getaran adalah deret geometri (subbab 1.3):

$$
q_\text{vib} = \sum_ve^{-v\hbar\omega/kT} = \frac{1}{1 - e^{-\hbar\omega/kT}} , \qquad \frac{N_v}{N} = \frac{e^{-v\hbar\omega/kT}}{q_\text{vib}} \qquad \text{(5.15)}
$$

(energi diukur dari tingkat $v = 0$). Untuk sebagian besar molekul pada suhu kamar, $\hbar\omega \gg kT$, sehingga hampir semua molekul berada di $v = 0$.

::: {.contoh}
**Contoh 5.12 · Energi titik nol beberapa molekul**

Hitung energi titik nol harmonik (cm⁻¹, kJ/mol, dan dalam satuan $kT$ pada 298 K) untuk H₂ (4401 cm⁻¹), HF (4138), N₂ (2359), dan CO (2170).

**Penyelesaian.** $E_0 = \tfrac12\tilde\nu$ (cm⁻¹); kalikan 0,011 963 untuk kJ/mol; bagi 207,2 untuk satuan $kT$.

| | H₂ | HF | N₂ | CO |
|---|---|---|---|---|
| $E_0$ (cm⁻¹) | 2201 | 2069 | 1179 | 1085 |
| $E_0$ (kJ/mol) | 26,3 | 24,8 | 14,1 | 13,0 |
| $E_0/kT$ | 10,6 | 10,0 | 5,7 | 5,2 |

**Memahami hasil.** Energi titik nol molekul hidrida 10 kali $kT$: ia sama sekali tidak dapat "dibekukan" dengan pendinginan. Bahkan pada nol mutlak, molekul H₂ menyimpan 26 kJ/mol energi getaran. Untuk molekul poliatom, energi titik nol dijumlahkan atas semua mode; untuk benzena (30 mode) jumlahnya sekitar 260 kJ/mol.
:::

::: {.contoh}
**Contoh 5.13 · $D_e$ dan $D_0$ molekul hidrogen**

Energi disosiasi H₂ yang terukur adalah $D_0 = 4{,}478$ eV. Dengan $\omega_e = 4401$ cm⁻¹, perkirakan $D_e$ dengan (5.14). Nilai perhitungan kuantum yang sangat teliti adalah 4,747 eV. Mengapa selisihnya?

**Penyelesaian.** $\tfrac12h\nu = \tfrac12(4401)(1{,}2398 \times 10^{-4}\ \text{eV}) = 0{,}273$ eV. $D_e \approx 4{,}478 + 0{,}273 = 4{,}751$ eV.

**Memahami hasil.** Selisih 0,004 eV berasal dari anharmonisitas: energi titik nol sebenarnya $\tfrac12\omega_e - \tfrac14\omega_ex_e = 0{,}269$ eV (subbab 5.9), sehingga $D_e = 4{,}747$ eV, cocok sempurna. Untuk perbandingan dengan ketelitian kimia (1 kcal/mol = 0,043 eV), koreksi harmonik sudah cukup; untuk spektroskopi presisi, tidak.
:::

::: {.contoh}
**Contoh 5.14 · Siapa yang bergetar pada suhu kamar?**

Hitung fraksi molekul pada $v = 1$ pada 298 K untuk HCl (2991 cm⁻¹), O₂ (1580), Cl₂ (560), dan I₂ (214,5), dan fungsi partisi getaran I₂.

**Penyelesaian.** $N_1/N_0 = e^{-1{,}4388\tilde\nu/298{,}15}$: HCl $5{,}4 \times 10^{-7}$; O₂ $4{,}9 \times 10^{-4}$; Cl₂ 0,067; I₂ 0,355. Untuk I₂, $q = 1/(1 - 0{,}355) = 1{,}55$, sehingga $N_0/N = 0{,}645$ dan $N_1/N = 0{,}229$.

**Memahami hasil.** Sepertiga molekul I₂ tereksitasi secara termal. Spektrum I₂ karena itu memperlihatkan **pita panas** (*hot bands*), transisi dari $v = 1$ dan $v = 2$, yang hampir sama kuat dengan pita dari $v = 0$. Untuk hidrida, spektrum IR pada suhu kamar hampir murni dari keadaan dasar. Hasil ini juga menjelaskan kapasitas kalor getaran di Contoh 1.4.
:::

### Energi titik nol dalam termokimia

Energi reaksi yang dihitung dari kurva potensial (beda $D_e$) harus dikoreksi dengan selisih energi titik nol hasil dan pereaksi sebelum dibandingkan dengan entalpi reaksi pada 0 K. Untuk molekul organik, koreksi ini dapat mencapai puluhan kJ/mol, karena energi titik nol dijumlahkan atas semua mode (subbab 5.11). Pada suhu yang lebih tinggi, energi getaran termal di atas $E_0$ juga ikut, dan menyumbang pada kapasitas kalor gas.

::: {.contoh}
**Contoh 5.15 · Koreksi energi titik nol reaksi H₂ + F₂ → 2HF**

Dengan $G(0) = \tfrac12\omega_e - \tfrac14\omega_ex_e$ dan data H₂ (4401,21; 121,34 cm⁻¹), F₂ (916,64; 11,24 cm⁻¹), HF (4138,32; 89,88 cm⁻¹), hitung $\Delta E_0 = 2E_0(\text{HF}) - E_0(\text{H}_2) - E_0(\text{F}_2)$.

**Penyelesaian.** $E_0(\text{H}_2) = 2170{,}3$; $E_0(\text{F}_2) = 455{,}5$; $E_0(\text{HF}) = 2046{,}7$ cm⁻¹. $\Delta E_0 = 4093{,}4 - 2625{,}8 = 1467{,}6$ cm⁻¹ $= 17{,}6$ kJ/mol.

**Memahami hasil.** Hasil reaksi mempunyai energi titik nol lebih besar, karena dua ikatan H–F yang kaku menggantikan satu ikatan F–F yang lunak. Koreksi 17,6 kJ/mol membuat reaksi kurang eksoterm dibandingkan selisih $D_e$ semata. Ketelitian kimia (sekitar 4 kJ/mol) tidak mungkin dicapai tanpa koreksi ini.
:::

::: {.contoh}
**Contoh 5.16 · Kapasitas kalor getaran N₂**

Kapasitas kalor getaran molar osilator harmonik adalah $C = R\,x^2e^x/(e^x - 1)^2$ dengan $x = hc\tilde\nu/kT$ (subbab 1.3). Hitung $C/R$ untuk N₂ ($\tilde\nu = 2358{,}6$ cm⁻¹) pada 300, 1000, dan 2000 K.

**Penyelesaian.** $x = 1{,}4388\tilde\nu/T$: 11,31; 3,39; 1,70. Hasilnya $C/R = 0{,}0016$; 0,414; 0,791.

**Memahami hasil.** Pada suhu kamar, getaran N₂ "membeku": kapasitas kalor $C_V$ gas nitrogen praktis $\tfrac52R$ (translasi dan rotasi saja). Getaran baru ikut menyerap kalor di atas sekitar 1000 K. Inilah teka-teki kapasitas kalor gas diatom yang tidak dapat dijelaskan fisika klasik (Contoh 1.4), dan kini dijelaskan oleh tingkat-tingkat osilator yang berjarak $\hbar\omega \gg kT$.
:::

::: {.kuis}
**Kuis cepat 5.4**

Selisih energi antara $v = 3$ dan $v = 4$ osilator harmonik dibandingkan selisih antara $v = 0$ dan $v = 1$: lebih besar, lebih kecil, atau sama?
:::

## 5.5 Fungsi gelombang: kuantum vs klasik

### Perbandingan rapat peluang

Gambar 5.2 membandingkan rapat peluang kuantum $|\psi_v|^2$ dengan rapat peluang klasik (5.5) pada energi yang sama. Tiga perbedaan menonjol:

1. Pada **keadaan dasar**, rapat kuantum terbesar di tengah, sedangkan klasik terbesar di titik balik.
2. Rapat kuantum mempunyai **simpul** ($v$ buah) tempat partikel tidak pernah ditemukan.
3. Rapat kuantum **menembus ke luar titik balik**, ke daerah yang terlarang secara klasik.

Untuk $v$ besar, rata-rata lokal rapat kuantum mendekati rapat klasik (asas korespondensi), tetapi penembusan ke luar titik balik dan simpul-simpulnya tetap ada.

![Gambar 5.2 Rapat peluang osilator harmonik untuk $v = 0$, 1, dan 10 (biru), dibandingkan dengan rapat peluang klasik pada energi yang sama (jingga putus-putus). Garis titik-titik menandai titik balik klasik. Pada $v = 10$ rapat kuantum sudah menyerupai klasik, kecuali di dekat dan di luar titik balik.](fig/c_korespondensi.png){width=90%}

### Penembusan ke daerah terlarang

Titik balik klasik untuk tingkat $v$ adalah $\xi_t = \pm\sqrt{2v + 1}$. Untuk keadaan dasar, $\xi_t = \pm1$, dan peluang partikel berada di luar titik balik adalah

$$
P(|\xi| > 1) = \frac{2}{\sqrt\pi}\int_1^\infty e^{-\xi^2}d\xi = \text{erfc}(1) = 0{,}157 .
$$

Hampir 16% waktu, ikatan dalam keadaan dasar lebih panjang atau lebih pendek daripada yang diizinkan fisika klasik untuk energi itu. Penembusan ini adalah wajah lain dari gejala yang membuat penerobosan mungkin (subbab 3.11).

### Nilai harap

Dengan simetri dan sifat Hermite (atau, lebih cepat, dengan operator tangga di subbab 5.6):

$$
\langle x\rangle = 0, \quad \langle x^2\rangle = \frac{\hbar}{\mu\omega}\left(v + \tfrac12\right), \quad \langle p\rangle = 0, \quad \langle p^2\rangle = \mu\hbar\omega\left(v + \tfrac12\right) . \qquad \text{(5.16)}
$$

Akibatnya $\langle T\rangle = \langle p^2\rangle/2\mu = \tfrac12E_v$ dan $\langle V\rangle = \tfrac12\mu\omega^2\langle x^2\rangle = \tfrac12E_v$: energi terbagi rata antara kinetik dan potensial (teorema virial untuk potensial kuadrat), dan $\Delta x\,\Delta p = (v + \tfrac12)\hbar$.

::: {.contoh}
**Contoh 5.17 · Seberapa jauh menembus?**

Hitung peluang berada di luar titik balik untuk $v = 0$, 1, 2, 5, dan 10.

**Penyelesaian.** Integrasi numerik $\int_{|\xi|>\sqrt{2v+1}}|\psi_v|^2d\xi$: $v = 0$: 0,157; $v = 1$: 0,112; $v = 2$: 0,095; $v = 5$: 0,074; $v = 10$: 0,060.

**Memahami hasil.** Peluang penembusan menurun perlahan dengan $v$, tetapi tidak pernah nol. Penembusan ini nyata secara kimia: ia menentukan seberapa jauh fungsi gelombang getaran keadaan dasar menjangkau geometri keadaan tereksitasi elektronik, yang mengatur intensitas pita serapan elektronik (faktor Franck–Condon, Bab 15).
:::

::: {.contoh}
**Contoh 5.18 · Getaran titik nol HCl dan H₂**

Hitung $\sqrt{\langle x^2\rangle}$ pada $v = 0$ untuk HCl ($\tilde\nu = 2991$ cm⁻¹, $\mu = 0{,}9796$ u) dan bandingkan dengan panjang ikatan 127,5 pm. Lakukan hal yang sama untuk H₂ (74,1 pm).

**Penyelesaian.** $\sqrt{\hbar/2\mu\omega}$: HCl $\omega = 5{,}634 \times 10^{14}$ s⁻¹, $\mu = 1{,}627 \times 10^{-27}$ kg, hasilnya 7,6 pm (6% panjang ikatan). H₂: 8,7 pm (12%; Contoh 1.46).

**Memahami hasil.** Molekul hidrogen pada keadaan dasarnya "bergoyang" dengan simpangan baku 12% panjang ikatannya. Inilah sebabnya panjang ikatan H₂ yang diukur dengan cara berbeda (difraksi, spektroskopi rotasi) memberikan nilai yang sedikit berbeda: masing-masing merata-ratakan besaran yang berbeda ($\langle r\rangle$, $\langle r^{-2}\rangle^{-1/2}$, ...) atas gerak titik nol ini.
:::

::: {.contoh}
**Contoh 5.19 · Teorema virial osilator**

Untuk $v = 0$, hitung $\langle T\rangle$ dan $\langle V\rangle$ langsung dengan $\psi_0 = (\alpha/\pi)^{1/4}e^{-\alpha x^2/2}$.

**Penyelesaian.** $\langle V\rangle = \tfrac12\mu\omega^2\langle x^2\rangle$ dengan $\langle x^2\rangle = \tfrac{1}{2\alpha}$ (Contoh 2.9), jadi $\langle V\rangle = \tfrac12\mu\omega^2\cdot\tfrac{\hbar}{2\mu\omega} = \tfrac14\hbar\omega$. $\langle T\rangle = \tfrac{\hbar^2}{2\mu}\int|\psi_0'|^2dx = \tfrac{\hbar^2}{2\mu}\alpha^2\langle x^2\rangle = \tfrac{\hbar^2}{2\mu}\cdot\tfrac\alpha2 = \tfrac14\hbar\omega$. Jumlahnya $\tfrac12\hbar\omega$.

**Memahami hasil.** Energi titik nol terbagi sama rata. Untuk potensial $V \propto x^n$, teorema virial umum menyatakan $2\langle T\rangle = n\langle V\rangle$; untuk $n = 2$ hasilnya $\langle T\rangle = \langle V\rangle$, dan untuk Coulomb ($n = -1$) $2\langle T\rangle = -\langle V\rangle$ (Contoh 4.20).
:::

### Paket gelombang: osilator yang bergerak

Keadaan stasioner $\psi_v$ tidak bergerak: rapat peluangnya tidak bergantung waktu (subbab 3.4). Untuk melihat ikatan yang benar-benar "bergetar", kita perlu superposisi beberapa keadaan, yang rapat peluangnya berosilasi dengan frekuensi Bohr $(E_{v'} - E_v)/h$ (Contoh 3.11). Karena semua selisih energi osilator harmonik adalah kelipatan $\hbar\omega$, superposisi apa pun kembali ke bentuk semula setelah tepat satu periode klasik $2\pi/\omega$: paket gelombang osilator tidak menyebar, tetapi berayun bolak-balik seperti partikel klasik.

::: {.contoh}
**Contoh 5.20 · Ikatan I₂ yang berayun**

Molekul I₂ disiapkan dalam superposisi $\Psi = (\psi_0e^{-iE_0t/\hbar} + \psi_1e^{-iE_1t/\hbar})/\sqrt2$. Hitung $\langle x\rangle(t)$, periodenya, dan amplitudonya ($\tilde\nu = 214{,}5$ cm⁻¹, $\mu = 63{,}45$ u).

**Penyelesaian.** $\langle x\rangle = \tfrac12[\langle 0|x|0\rangle + \langle 1|x|1\rangle] + \tfrac12[\langle 0|x|1\rangle e^{-i\omega t} + \langle 1|x|0\rangle e^{i\omega t}]$. Suku diagonal nol (paritas), dan $\langle 0|x|1\rangle = \sqrt{\hbar/2\mu\omega}$ riil, jadi $\langle x\rangle(t) = \sqrt{\hbar/2\mu\omega}\cos\omega t$. Periode $1/(c\tilde\nu) = 155{,}5$ fs; amplitudo $\sqrt{\hbar/2\mu\omega} = 3{,}5$ pm.

**Memahami hasil.** Pusat paket berayun dengan frekuensi klasik, sesuai teorema Ehrenfest (Contoh 4.23). Pada akhir 1980-an, Ahmed Zewail memakai pulsa laser berdurasi puluhan femtodetik untuk menyiapkan paket semacam ini dalam I₂ dan NaI dan "memfilmkan" gerak inti selama ikatan meregang dan putus. Kelahiran **femtokimia** (Hadiah Nobel 1999) ini bertumpu pada fakta sederhana bahwa superposisi keadaan getaran bergerak, sedangkan keadaan tunggal tidak.
:::

::: {.contoh}
**Contoh 5.21 · Seberapa jauh osilator menembus daerah terlarang?**

Hitung peluang osilator berada di luar titik balik klasiknya untuk $v = 0$ dan $v = 1$. Untuk $v = 0$, $P = \operatorname{erfc}(1)$; untuk $v = 1$, $P = \operatorname{erfc}(\sqrt3) + \tfrac{2\sqrt3}{\sqrt\pi}e^{-3}$.

**Penyelesaian.** $v = 0$: $P = 0{,}157$. $v = 1$: $P = 0{,}0143 + 0{,}0975 = 0{,}112$.

**Memahami hasil.** Pada keadaan dasar, hampir 16% waktu molekul berada di jarak yang secara klasik terlarang, dan peluang itu menurun perlahan dengan $v$. Penembusan seperti ini mendasari penerobosan atom hidrogen dalam reaksi transfer proton dan inversi amonia (subbab 3.12): fungsi gelombang yang "bocor" ke daerah terlarang dapat menyambung ke sumur di seberangnya.
:::

::: {.kuis}
**Kuis cepat 5.5**

Di titik mana rapat peluang keadaan $v = 1$ bernilai nol? Mengapa rapat peluang klasik tidak pernah nol di dalam daerah gerak?
:::

## 5.6 Operator tangga

Ada cara yang sama sekali berbeda untuk menyelesaikan osilator harmonik, tanpa deret pangkat, hanya dengan aljabar operator. Metode ini, yang dikembangkan Dirac, sangat kuat: ia memberikan seluruh spektrum dalam beberapa baris, memberi unsur matriks tanpa integral, dan menjadi dasar teori medan kuantum (foton adalah "kuanta" osilator mode-mode medan).

### Definisi

Dalam variabel tak berdimensi $\xi$ (satuan $\hbar = \mu = \omega = 1$ untuk sementara), $\hat H = \tfrac12(\hat p^2 + \hat\xi^2)$ dengan $\hat p = -i\,d/d\xi$ dan $[\hat\xi, \hat p] = i$. Definisikan

$$
\hat a = \frac{1}{\sqrt2}\left(\hat\xi + i\hat p\right) = \frac{1}{\sqrt2}\left(\xi + \frac{d}{d\xi}\right), \qquad \hat a^\dagger = \frac{1}{\sqrt2}\left(\hat\xi - i\hat p\right) = \frac{1}{\sqrt2}\left(\xi - \frac{d}{d\xi}\right) . \qquad \text{(5.17)}
$$

Kalikan: $\hat a^\dagger\hat a = \tfrac12(\hat\xi^2 + \hat p^2 + i[\hat\xi, \hat p]) = \tfrac12(\hat\xi^2 + \hat p^2) - \tfrac12$. Jadi

$$
\hat H = \hat a^\dagger\hat a + \tfrac12, \qquad [\hat a, \hat a^\dagger] = 1 . \qquad \text{(5.18)}
$$

(Komutatornya dihitung dengan cara yang sama.) Dalam satuan biasa, $\hat H = \hbar\omega(\hat a^\dagger\hat a + \tfrac12)$.

### Mengapa "tangga"

Misalkan $\psi_E$ fungsi eigen $\hat H$ dengan energi $E$. Dengan (5.18), $[\hat H, \hat a^\dagger] = \hat a^\dagger$ dan $[\hat H, \hat a] = -\hat a$. Maka

$$
\hat H(\hat a^\dagger\psi_E) = \hat a^\dagger\hat H\psi_E + \hat a^\dagger\psi_E = (E + 1)\,\hat a^\dagger\psi_E .
$$

$\hat a^\dagger$ menaikkan energi satu anak tangga ($\hbar\omega$); dengan cara sama, $\hat a$ menurunkannya. Tangga ke bawah harus berhenti, karena energi tidak dapat negatif ($\hat H = \hat a^\dagger\hat a + \tfrac12$ dan $\langle\hat a^\dagger\hat a\rangle = \int|\hat a\psi|^2 \ge 0$). Jadi ada keadaan terendah $\psi_0$ dengan $\hat a\psi_0 = 0$, yang energinya $E_0 = \tfrac12$. Tangga ke atas memberi $E_v = v + \tfrac12$: persis (5.12), tanpa satu deret pun.

Persamaan $\hat a\psi_0 = 0$ adalah $\xi\psi_0 + \psi_0' = 0$, yang penyelesaiannya $\psi_0 = e^{-\xi^2/2}$, keadaan dasar yang sudah kita kenal.

### Unsur matriks

Dengan normalisasi yang tepat:

$$
\hat a^\dagger\psi_v = \sqrt{v + 1}\,\psi_{v+1}, \qquad \hat a\psi_v = \sqrt v\,\psi_{v-1} . \qquad \text{(5.19)}
$$

Karena $\hat\xi = (\hat a + \hat a^\dagger)/\sqrt2$, dan kembali ke satuan biasa ($x = \xi/\sqrt\alpha$):

$$
\langle v'|x|v\rangle = \sqrt{\frac{\hbar}{2\mu\omega}}\left(\sqrt v\,\delta_{v',v-1} + \sqrt{v + 1}\,\delta_{v',v+1}\right) . \qquad \text{(5.20)}
$$

Hanya unsur antara tingkat-tingkat yang **bertetangga** yang tidak nol. Inilah asal aturan seleksi inframerah $\Delta v = \pm1$ (subbab 5.8).

::: {.contoh}
**Contoh 5.22 · Membangun $\psi_1$ dan $\psi_2$ dengan $\hat a^\dagger$**

Mulai dari $\psi_0 = \pi^{-1/4}e^{-\xi^2/2}$, hitung $\hat a^\dagger\psi_0$ dan $\hat a^\dagger\psi_1$, lalu bandingkan dengan (5.13).

**Penyelesaian.** $\hat a^\dagger\psi_0 = \tfrac{1}{\sqrt2}(\xi\psi_0 - \psi_0') = \tfrac{1}{\sqrt2}(2\xi)\psi_0 = \pi^{-1/4}\sqrt2\,\xi e^{-\xi^2/2}$. Ini $\psi_1 = \pi^{-1/4}\tfrac{1}{\sqrt2}H_1e^{-\xi^2/2}$, dengan faktor $\sqrt{0 + 1} = 1$. Lalu $\hat a^\dagger\psi_1 = \tfrac{1}{\sqrt2}\pi^{-1/4}\sqrt2(\xi^2 - 1 + \xi^2)e^{-\xi^2/2} = \pi^{-1/4}(2\xi^2 - 1)e^{-\xi^2/2}$, dan $\sqrt2\,\psi_2 = \sqrt2\,\pi^{-1/4}\tfrac{1}{\sqrt8}(4\xi^2 - 2)e^{-\xi^2/2} = \pi^{-1/4}(2\xi^2 - 1)e^{-\xi^2/2}$. Cocok.

**Memahami hasil.** Operator naik menghasilkan seluruh keluarga fungsi eigen dari keadaan dasar dengan menurunkan dan mengalikan. Dalam teori medan kuantum, $\hat a^\dagger$ disebut **operator penciptaan**: ia menambah satu foton (atau satu fonon, kuantum getaran kisi) ke mode yang bersangkutan.
:::

::: {.contoh}
**Contoh 5.23 · Unsur matriks tanpa integral**

Dengan (5.20), hitung (a) $\langle 1|x|0\rangle$ untuk HCl, (b) $\langle 0|x^2|0\rangle$, (c) $\langle 0|x^4|0\rangle$ dalam satuan $(\hbar/2\mu\omega)$.

**Penyelesaian.** (a) $\sqrt{\hbar/2\mu\omega} = 7{,}6$ pm (Contoh 5.18).

(b) $\hat x^2 = \tfrac{\hbar}{2\mu\omega}(\hat a + \hat a^\dagger)^2$. Pada $\psi_0$: $(\hat a + \hat a^\dagger)\psi_0 = \psi_1$, lalu $(\hat a + \hat a^\dagger)\psi_1 = \psi_0 + \sqrt2\psi_2$. Proyeksi pada $\psi_0$: 1. Jadi $\langle x^2\rangle = \hbar/2\mu\omega$.

(c) $\langle 0|x^4|0\rangle = \|\hat x^2\psi_0\|^2 = (\hbar/2\mu\omega)^2\|\psi_0 + \sqrt2\psi_2\|^2 = 3(\hbar/2\mu\omega)^2$.

**Memahami hasil.** Perbandingan $\langle x^4\rangle/\langle x^2\rangle^2 = 3$ adalah sidik jari sebaran Gauss (Contoh 2.11). Nilai $\langle x^4\rangle$ dan $\langle x^3\rangle$ dalam keadaan tereksitasi diperlukan untuk menghitung koreksi anharmonik dengan teori perturbasi (Bab 8); dengan operator tangga, perhitungannya menjadi menghitung jalan di tangga.
:::

::: {.contoh}
**Contoh 5.24 · Komutator dan spektrum**

Buktikan $[\hat a, \hat a^\dagger] = 1$ dari $[\hat\xi, \hat p] = i$, lalu tunjukkan $[\hat H, \hat a] = -\hat a$.

**Penyelesaian.** $[\hat a, \hat a^\dagger] = \tfrac12[\hat\xi + i\hat p, \hat\xi - i\hat p] = \tfrac12(-i[\hat\xi, \hat p] + i[\hat p, \hat\xi]) = \tfrac12(-i\cdot i + i\cdot(-i)) = 1$. Lalu $[\hat H, \hat a] = [\hat a^\dagger\hat a, \hat a] = \hat a^\dagger[\hat a, \hat a] + [\hat a^\dagger, \hat a]\hat a = 0 - \hat a = -\hat a$.

**Memahami hasil.** Seluruh spektrum osilator mengikuti dari satu komutator. Metode serupa, dengan komutator momentum sudut $[\hat L_x, \hat L_y] = i\hbar\hat L_z$, memberikan nilai eigen momentum sudut tanpa menyelesaikan persamaan diferensial (Bab 6). Aljabar operator adalah cara paling ringkas untuk mengungkap struktur sebuah masalah kuantum.
:::

::: {.contoh}
**Contoh 5.25 · Simpangan rms dengan operator tangga**

Dengan $\hat x = (\hat a + \hat a^\dagger)/\sqrt{2\alpha}$, hitung $\langle v|\hat x^2|v\rangle$ tanpa integral, lalu nilai rms simpangan HCl untuk $v = 0$ dan $v = 1$ ($\alpha = 8{,}69 \times 10^{21}$ m⁻²).

**Penyelesaian.** $\hat x^2 = (\hat a^2 + \hat a\hat a^\dagger + \hat a^\dagger\hat a + \hat a^{\dagger2})/2\alpha$. Suku $\hat a^2$ dan $\hat a^{\dagger2}$ mengubah $v$ sebesar 2 sehingga nilai harapnya nol. Dengan $\hat a^\dagger\hat a|v\rangle = v|v\rangle$ dan $\hat a\hat a^\dagger|v\rangle = (v + 1)|v\rangle$:

$$
\langle\hat x^2\rangle = \frac{2v + 1}{2\alpha} .
$$

HCl: $v = 0$, $x_\text{rms} = 1/\sqrt{2\alpha} = 7{,}6$ pm; $v = 1$, $x_\text{rms} = \sqrt{3/2\alpha} = 13{,}1$ pm.

**Memahami hasil.** Satu baris aljabar operator menggantikan integral fungsi Hermite. Simpangan rms yang membesar dengan $v$ menjelaskan mengapa panjang ikatan rata-rata naik pada tingkat getaran lebih tinggi (dengan bantuan anharmonisitas, subbab 5.9), dan mengapa difraksi elektron gas memberi panjang ikatan "efektif" yang sedikit bergantung pada suhu.
:::

::: {.kuis}
**Kuis cepat 5.6**

Berapa $\hat a\psi_0$? Berapa $\hat a^\dagger\hat a\psi_3$? Mengapa operator $\hat N = \hat a^\dagger\hat a$ disebut operator bilangan?
:::
