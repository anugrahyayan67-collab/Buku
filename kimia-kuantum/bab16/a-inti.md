# Bab 16 Resonansi Magnetik

Masukkan beberapa miligram etil asetat ke dalam tabung kaca tipis, letakkan di dalam magnet superkonduktor, dan dalam dua menit layar menampilkan tiga kelompok garis: satu garis tunggal, satu kelompok empat garis, dan satu kelompok tiga garis. Dari pola itu seorang kimiawan langsung membaca bahwa molekulnya mengandung gugus asetil dan gugus etil, dan bahwa CH₂ etil terikat pada oksigen. Yang mengherankan adalah skala energinya. Pada spektrometer 400 MHz, selisih energi yang diukur hanya sekitar $2{,}7 \times 10^{-25}$ joule, kira-kira enam belas ribu kali lebih kecil daripada energi termal pada suhu kamar. Dari setiap sejuta proton dalam sampel, hanya sekitar tiga puluh dua yang "berlebih" di tingkat energi bawah. Bagaimana mungkin spektroskopi dengan kuantum sekecil itu, dengan selisih populasi setipis itu, menjadi alat penentu struktur paling ampuh dalam kimia, cukup tajam untuk membedakan proton yang terpisah empat ikatan dan cukup peka untuk memetakan otak manusia yang sedang berpikir?

Jawabannya adalah gabungan tiga hal yang semuanya bersumber dari mekanika kuantum momentum sudut. Pertama, inti atom mempunyai spin dan momen magnet, sehingga dalam medan magnet tingkat energinya terpecah secara teratur (efek Zeeman inti). Kedua, awan elektron di sekitar inti sedikit melindungi inti dari medan luar, dan perlindungan itu bergantung pada lingkungan kimia; selisih yang kecil ini, beberapa per sejuta, adalah **geseran kimia**. Ketiga, spin-spin inti saling "merasakan" melalui elektron ikatan, sehingga garis-garis terpecah menurut pola yang mencerminkan tetangga-tetangganya: **kopling spin–spin**. Ketiganya dibaca dengan teknik pulsa dan transformasi Fourier yang mengubah kelemahan menjadi keunggulan: karena tingkat energinya begitu rapat, spin inti dapat dikendalikan dengan sangat tepat dan hidup lama sebelum "lupa" fasenya.

Di bab ini kita membangun resonansi magnetik inti (NMR) dari dasar: spin dan momen magnet inti, tingkat Zeeman, populasi dan kepekaan, geseran kimia, kopling, spektrum orde satu dan orde dua, kesetaraan spin, model vektor dan pulsa, relaksasi, dan gagasan NMR dua dimensi. Kemudian kita beralih ke saudaranya, resonansi spin elektron (ESR), yang membaca radikal bebas dan ion logam transisi, dan menutup dengan pencitraan resonansi magnetik (MRI). Hampir semua yang diperlukan sudah tersedia di bab-bab sebelumnya: operator momentum sudut (Bab 6), sistem dua tingkat (Bab 4), perturbasi (Bab 8), dan spin (Bab 9).

::: {.strategi}
**Pertanyaan pembuka**

1. Mengapa ¹H, ¹³C, dan ³¹P "terlihat" dalam NMR, sedangkan ¹²C dan ¹⁶O tidak?
2. Mengapa NMR jauh kurang peka daripada spektroskopi UV-Vis, dan mengapa magnet yang makin kuat begitu berharga?
3. Mengapa proton yang terikat pada karbon dekat oksigen beresonansi pada frekuensi yang sedikit berbeda dari proton gugus metil biasa?
4. Mengapa CH₃ dalam gugus etil tampak sebagai tiga garis, padahal ketiga protonnya tidak saling memecah garis?
5. Bagaimana sebuah pulsa gelombang radio beberapa mikrodetik dapat menghasilkan seluruh spektrum sekaligus?
6. Bagaimana prinsip yang sama dipakai untuk membaca radikal bebas dan untuk memotret jaringan lunak di dalam tubuh?
:::

::: {.tujuan}
**Tujuan belajar**

Setelah mempelajari bab ini, kamu mampu:

1. Menentukan spin inti, menghitung momen magnet, faktor $g$ inti, dan frekuensi Larmor dari rasio giromagnetik.
2. Menurunkan tingkat energi Zeeman inti, syarat resonansi, dan aturan seleksi $\Delta m_I = \pm1$.
3. Menghitung selisih populasi, magnetisasi kesetimbangan, dan kepekaan relatif berbagai inti.
4. Menjelaskan asal perisai diamagnetik dan paramagnetik, menghitung geseran kimia dalam ppm dan Hz, dan menafsirkan pengaruh keelektronegatifan dan arus cincin.
5. Menurunkan spektrum orde satu sistem AX, menyusun pola multiplet, dan memakai hubungan Karplus.
6. Menyusun dan mendiagonalkan Hamiltonian spin sistem AB, serta menjelaskan efek atap dan perubahan spektrum dengan kuat medan.
7. Membedakan kesetaraan kimia dan kesetaraan magnetik, dan menganalisis pengaruh pertukaran kimia pada bentuk garis.
8. Memakai model vektor dalam kerangka berputar untuk menjelaskan pulsa, FID, dan transformasi Fourier.
9. Menjelaskan relaksasi $T_1$ dan $T_2$, mengukurnya dengan pemulihan inversi dan gema spin, serta mengaitkannya dengan waktu korelasi gerak molekul dan efek Overhauser inti.
10. Menafsirkan spektrum dua dimensi COSY, HSQC, dan NOESY secara konseptual.
11. Menghitung faktor $g$, medan resonansi, dan pola hiperhalus spektrum ESR, serta memakai hubungan McConnell.
12. Menjelaskan cara gradien medan mengubah frekuensi menjadi posisi dalam MRI, dan asal kontras $T_1$ dan $T_2$.
:::

::: {.mat}
**Prasyarat**

Dari Bab 1: skala energi dan populasi tingkat NMR (Contoh 1.53). Dari Bab 4: komutator, notasi Dirac, dan evolusi sistem dua keadaan (Contoh 4.44). Dari Bab 6: momen magnet orbital (subbab 6.1), kuantisasi ruang (6.6), operator tangga dan unsur matriksnya (6.7), arus cincin benzena (6.3), sudut ajaib (Contoh 6.17). Dari Bab 7: efek Zeeman (7.12) dan rapat peluang di inti (7.5). Dari Bab 8: teori perturbasi (subbab 8.6–8.7) dan aturan emas Fermi (8.12). Dari Bab 9: spin elektron dan matriks Pauli (subbab 9.1–9.2). Dari Bab 15: koefisien Einstein dan lebar garis (subbab 15.1 dan 15.3).
:::

## 16.1 Momen magnet spin inti

### Inti juga mempunyai spin

Proton dan neutron, seperti elektron, adalah fermion bersepin $\tfrac12$. Di dalam inti, spin-spin nukleon dan momentum sudut orbitalnya bergabung menjadi satu momentum sudut total yang disebut **spin inti**, dengan bilangan kuantum $I$. Operator spin inti $\hat{\mathbf I}$ mematuhi aljabar momentum sudut yang sama persis dengan $\hat{\mathbf L}$ (subbab 6.2 dan 6.7):

$$
\hat I^2\,|I, m_I\rangle = I(I+1)\hbar^2\,|I, m_I\rangle , \qquad \hat I_z\,|I, m_I\rangle = m_I\hbar\,|I, m_I\rangle , \qquad m_I = -I, -I+1, \ldots, I . \qquad \text{(16.1)}
$$

Bedanya, $I$ boleh bilangan bulat atau setengah bulat, dan ia adalah sifat tetap setiap nuklida pada keadaan dasarnya. Struktur inti terlalu rumit untuk diramalkan dengan mudah, tetapi ada tiga aturan empiris yang hampir selalu benar:

1. Nomor massa ganjil: $I$ setengah bulat ($\tfrac12$, $\tfrac32$, $\tfrac52$, …). Contoh: ¹H, ¹³C, ¹⁵N, ¹⁹F, ³¹P berspin $\tfrac12$; ¹¹B dan ²³Na berspin $\tfrac32$; ¹⁷O berspin $\tfrac52$.
2. Nomor massa genap dengan jumlah proton genap dan neutron genap: $I = 0$. Contoh: ¹²C, ¹⁶O, ³²S. Nuklida ini **tidak terlihat** dalam NMR.
3. Nomor massa genap dengan jumlah proton ganjil dan neutron ganjil: $I$ bilangan bulat positif. Contoh: ²H dan ¹⁴N berspin 1, ¹⁰B berspin 3.

Aturan kedua mencerminkan kecenderungan nukleon sejenis untuk berpasangan dengan spin berlawanan, mirip elektron yang berpasangan dalam orbital. Karena itulah kerangka karbon dan oksigen molekul organik "tak terlihat" bagi NMR, dan yang kita amati adalah proton yang menempel padanya, ditambah ¹³C yang kelimpahannya hanya 1,1%.

### Momen magnet sebanding dengan spin

Partikel bermuatan yang berputar menghasilkan momen magnet. Untuk elektron yang mengorbit (subbab 6.1), momen magnet sebanding dengan momentum sudut: $\boldsymbol\mu = -(e/2m_e)\mathbf L$. Untuk spin inti berlaku hubungan serupa,

$$
\hat{\boldsymbol\mu} = \gamma\,\hat{\mathbf I} , \qquad \text{(16.2)}
$$

dengan $\gamma$ **rasio giromagnetik** inti, besaran yang diukur, bukan diturunkan. Sering ditulis dengan **faktor $g$ inti** $g_N$ dan **magneton inti** $\mu_N$:

$$
\gamma = \frac{g_N\mu_N}{\hbar}, \qquad \mu_N = \frac{e\hbar}{2m_p} = 5{,}0508 \times 10^{-27}\ \text{J T}^{-1} . \qquad \text{(16.3)}
$$

Magneton inti memakai massa proton sebagai pengganti massa elektron, sehingga ia 1836 kali lebih kecil daripada magneton Bohr. Inilah alasan pertama mengapa energi NMR kecil: momen magnet inti ribuan kali lebih lemah daripada momen magnet elektron.

Jika proton adalah bola bermuatan sederhana yang berputar, faktor $g$-nya akan 1 (atau 2 menurut teori Dirac untuk partikel titik). Nilai terukur $g_p = 5{,}586$ dan nilai neutron $g_n = -3{,}826$ (neutron netral pun bermagnet!) adalah bukti bahwa nukleon tersusun dari partikel yang lebih kecil, yaitu kuark. Bagi kimiawan, angka-angka ini cukup diterima sebagai data.

Komponen-$z$ momen magnet terkuantisasi bersama $\hat I_z$:

$$
\mu_z = \gamma m_I\hbar , \qquad |\boldsymbol\mu| = \gamma\hbar\sqrt{I(I+1)} . \qquad \text{(16.4)}
$$

Tanda $\gamma$ menentukan arah momen terhadap spin. Hampir semua inti penting mempunyai $\gamma > 0$, tetapi ¹⁵N, ¹⁷O, ²⁹Si, dan ¹²⁹Xe bertanda negatif: momen magnetnya berlawanan arah dengan spinnya.

| Nuklida | $I$ | γ (10⁷ rad s⁻¹ T⁻¹) | ν pada 9,395 T (MHz) | Kelimpahan (%) | Kepekaan relatif |
|---|---|---|---|---|---|
| ¹H | $\tfrac12$ | 26,752 | 400,00 | 99,99 | 1 |
| ²H | 1 | 4,107 | 61,40 | 0,0115 | $1{,}1 \times 10^{-6}$ |
| ¹³C | $\tfrac12$ | 6,728 | 100,60 | 1,07 | $1{,}7 \times 10^{-4}$ |
| ¹⁴N | 1 | 1,934 | 28,91 | 99,63 | $1{,}0 \times 10^{-3}$ |
| ¹⁵N | $\tfrac12$ | −2,713 | 40,56 | 0,37 | $3{,}8 \times 10^{-6}$ |
| ¹⁷O | $\tfrac52$ | −3,628 | 54,25 | 0,038 | $1{,}1 \times 10^{-5}$ |
| ¹⁹F | $\tfrac12$ | 25,181 | 376,51 | 100 | 0,83 |
| ²⁹Si | $\tfrac12$ | −5,319 | 79,53 | 4,69 | $3{,}7 \times 10^{-4}$ |
| ³¹P | $\tfrac12$ | 10,839 | 162,07 | 100 | 0,067 |
| ¹⁹⁵Pt | $\tfrac12$ | 5,839 | 87,30 | 33,8 | $3{,}5 \times 10^{-3}$ |

Tabel di atas memuat data inti yang paling sering dipakai kimiawan. Kolom frekuensi adalah frekuensi resonansi dalam magnet yang membuat proton beresonansi pada 400 MHz; kolom terakhir akan dijelaskan di subbab 16.3.

### Presesi Larmor klasik

Bayangkan dulu momen magnet sebagai vektor klasik. Medan magnet $\mathbf B$ memberi momen gaya $\boldsymbol\tau = \boldsymbol\mu \times \mathbf B$, dan momen gaya mengubah momentum sudut: $d\mathbf I/dt = \boldsymbol\tau$. Dengan $\boldsymbol\mu = \gamma\mathbf I$,

$$
\frac{d\boldsymbol\mu}{dt} = \gamma\,\boldsymbol\mu \times \mathbf B . \qquad \text{(16.5)}
$$

Jika $\mathbf B = B_0\hat{\mathbf z}$, komponennya: $\dot\mu_x = \gamma B_0\mu_y$, $\dot\mu_y = -\gamma B_0\mu_x$, $\dot\mu_z = 0$. Dua persamaan pertama adalah persamaan osilator yang terkopel; penyelesaiannya $\mu_x = \mu_\perp\cos\omega_0t$, $\mu_y = -\mu_\perp\sin\omega_0t$, dengan

$$
\omega_0 = \gamma B_0 , \qquad \nu_0 = \frac{\gamma B_0}{2\pi} . \qquad \text{(16.6)}
$$

Momen magnet tidak berbalik searah medan seperti jarum kompas yang diredam, melainkan berputar pada kerucut di sekitar medan dengan sudut tetap, seperti gasing yang miring dalam medan gravitasi. Gerak ini adalah **presesi Larmor**, dan $\omega_0$ adalah **frekuensi Larmor**. Hasil pentingnya: frekuensi presesi tidak bergantung pada sudut kemiringan, hanya pada $\gamma$ dan $B_0$. Kita akan melihat di subbab 16.2 bahwa frekuensi yang sama persis muncul sebagai syarat resonansi kuantum.

::: {.inti}
**Inti subbab 16.1**

- Spin inti $I$ adalah sifat tetap nuklida; inti dengan proton genap dan neutron genap berspin nol dan tidak terlihat dalam NMR.
- Momen magnet inti $\hat{\boldsymbol\mu} = \gamma\hat{\mathbf I}$, dengan $\gamma = g_N\mu_N/\hbar$; magneton inti 1836 kali lebih kecil daripada magneton Bohr.
- Dalam medan $B_0$, momen magnet berpresesi dengan frekuensi Larmor $\omega_0 = \gamma B_0$.
:::

::: {.contoh}
**Contoh 16.1 · Siapa yang terlihat dalam NMR?**

Tentukan apakah nuklida berikut berspin nol, setengah bulat, atau bulat, lalu kelompokkan menurut cocok tidaknya untuk NMR resolusi tinggi: ¹²C, ¹³C, ²H, ¹⁴N, ¹⁶O, ¹⁷O, ³¹P, ³²S, ³⁵Cl.

**Penyelesaian.** Hitung proton ($Z$) dan neutron ($N = A - Z$).

- ¹²C ($Z = 6$, $N = 6$), ¹⁶O (8, 8), ³²S (16, 16): genap–genap, $I = 0$, tidak terlihat.
- ¹³C (6, 7), ³¹P (15, 16): massa ganjil, $I = \tfrac12$.
- ¹⁷O (8, 9), ³⁵Cl (17, 18): massa ganjil, $I$ setengah bulat; data: $\tfrac52$ dan $\tfrac32$.
- ²H (1, 1), ¹⁴N (7, 7): ganjil–ganjil, $I$ bulat; data: keduanya 1.

**Memahami hasil.** Yang paling nyaman untuk NMR resolusi tinggi adalah inti berspin $\tfrac12$ (¹³C, ³¹P). Inti dengan $I \geq 1$ (²H, ¹⁴N, ¹⁷O, ³⁵Cl) mempunyai **momen kuadrupol listrik**, karena sebaran muatannya tidak bulat sempurna; kuadrupol ini berinteraksi dengan gradien medan listrik dari elektron di sekitarnya, sehingga spin kehilangan orientasinya dengan cepat dan garisnya melebar. Itulah sebabnya kimiawan organik memakai ¹⁵N yang langka ($I = \tfrac12$) alih-alih ¹⁴N yang melimpah.
:::

::: {.contoh}
**Contoh 16.2 · Momen magnet proton**

Rasio giromagnetik proton $\gamma = 26{,}7522 \times 10^7$ rad s⁻¹ T⁻¹. Hitung $g_N$, komponen-$z$ momen magnetnya, dan besar momennya dalam satuan $\mu_N$.

**Penyelesaian.** $g_N = \gamma\hbar/\mu_N = (2{,}67522 \times 10^8)(1{,}05457 \times 10^{-34})/(5{,}05078 \times 10^{-27}) = 5{,}586$. Untuk $m_I = +\tfrac12$: $\mu_z = \tfrac12g_N\mu_N = 2{,}793\,\mu_N = 1{,}411 \times 10^{-26}$ J/T. Besar momen $g_N\mu_N\sqrt{3/4} = 4{,}837\,\mu_N$.

**Memahami hasil.** Nilai 2,793 $\mu_N$ yang tercantum di tabel data inti sebagai "momen magnet proton" adalah komponen maksimum $\mu_z$, bukan panjang vektornya; panjang vektornya tidak pernah teramati langsung. Bandingkan dengan komponen-$z$ momen magnet spin elektron, sekitar 1 $\mu_B$: sekitar 658 kali lebih besar.
:::

::: {.contoh}
**Contoh 16.3 · NMR dalam medan bumi**

Medan magnet bumi di permukaan sekitar 50 μT. Berapa frekuensi Larmor proton dalam medan ini? Bandingkan dengan magnet 9,4 T.

**Penyelesaian.** $\nu_0 = \gamma B_0/2\pi = (2{,}67522 \times 10^8)(50 \times 10^{-6})/2\pi = 2{,}13$ kHz. Dalam 9,395 T: 400 MHz, hampir 190 000 kali lebih tinggi.

**Memahami hasil.** Frekuensi 2 kHz berada di rentang audio. Magnetometer proton yang dipakai dalam survei geofisika dan arkeologi bekerja dengan prinsip ini: air atau kerosin dipolarisasi sejenak oleh kumparan, lalu frekuensi presesinya dalam medan bumi diukur untuk mendapatkan kuat medan lokal dengan ketelitian nanotesla. Tetapi untuk kimia, medan bumi terlalu lemah; selain sinyalnya amat kecil (subbab 16.3), geseran kimia beberapa ppm hanya beberapa milihertz.
:::

::: {.contoh}
**Contoh 16.4 · Inti dengan $\gamma$ negatif**

¹⁵N mempunyai $\gamma = -2{,}7126 \times 10^7$ rad s⁻¹ T⁻¹. Hitung $g_N$ dan frekuensi resonansinya dalam magnet 14,09 T. Ke arah mana momen magnetnya bila spinnya menunjuk ke $+z$?

**Penyelesaian.** $g_N = \gamma\hbar/\mu_N = -0{,}566$. $|\nu_0| = |\gamma|B_0/2\pi = (2{,}7126 \times 10^7)(14{,}092)/2\pi = 60{,}8$ MHz. Momen magnet menunjuk ke $-z$.

**Memahami hasil.** Tanda negatif berarti presesi berlangsung dengan arah putar yang berlawanan dan tingkat $m_I = -\tfrac12$, bukan $+\tfrac12$, yang berenergi lebih rendah. Spektrometer hanya mengukur besar frekuensi, sehingga dalam praktik tanda $\gamma$ jarang terasa, kecuali pada efek Overhauser inti (subbab 16.9), yang untuk ¹⁵N justru dapat membalik tanda sinyal.
:::

::: {.kuis}
**Kuis cepat 16.1**

Di antara ¹²C, ¹⁴N, ¹⁶O, ¹⁹F, dan ³²S, nuklida mana yang memberi sinyal NMR? Mana yang berspin $\tfrac12$?
:::

## 16.2 Tingkat energi Zeeman inti

### Hamiltonian dan tingkat energi

Energi momen magnet dalam medan $\mathbf B$ adalah $-\boldsymbol\mu\cdot\mathbf B$. Untuk medan statis $B_0$ sepanjang $z$, Hamiltonian spin inti

$$
\hat H = -\hat{\boldsymbol\mu}\cdot\mathbf B = -\gamma B_0\hat I_z . \qquad \text{(16.7)}
$$

Karena $\hat H$ sebanding dengan $\hat I_z$, keadaan eigennya adalah $|I, m_I\rangle$, dan energinya

$$
E_{m_I} = -m_I\gamma\hbar B_0 , \qquad m_I = -I, \ldots, +I . \qquad \text{(16.8)}
$$

Ada $2I + 1$ tingkat berjarak sama, terpisah $\gamma\hbar B_0$, dan selisihnya bertambah lurus dengan medan (Gambar 16.1). Untuk inti berspin $\tfrac12$ ada dua tingkat: $m_I = +\tfrac12$, ditulis $\alpha$ atau $|{\uparrow}\rangle$, dan $m_I = -\tfrac12$, ditulis $\beta$ atau $|{\downarrow}\rangle$. Bila $\gamma > 0$, tingkat $\alpha$ (momen searah medan) lebih rendah.

![Gambar 16.1 Tingkat energi Zeeman inti. Kiri: inti berspin ½ (¹H dan ¹³C); tingkat α dan β memisah lurus dengan medan, dan pada medan yang sama celah ¹³C hanya seperempat celah ¹H. Kanan: inti berspin 1 (²H); tiga tingkat berjarak sama, sehingga hanya ada satu frekuensi transisi.](fig/c_zeeman.png){width=92%}

### Syarat resonansi dan aturan seleksi

Transisi diinduksi oleh medan magnet gelombang radio $B_1$ yang berosilasi tegak lurus $B_0$, misalnya $\mathbf B_1(t) = 2B_1\cos(\omega t)\,\hat{\mathbf x}$. Ia menambahkan perturbasi

$$
\hat H'(t) = -2\gamma B_1\cos(\omega t)\,\hat I_x . \qquad \text{(16.9)}
$$

Menurut teori perturbasi bergantung waktu (subbab 8.11–8.12), laju transisi antara $m_I$ dan $m_I'$ sebanding dengan $|\langle m_I'|\hat I_x|m_I\rangle|^2$ dan hanya besar bila $\hbar\omega$ sama dengan selisih energi. Operator $\hat I_x = \tfrac12(\hat I_+ + \hat I_-)$ hanya menaikkan atau menurunkan $m_I$ sebesar satu (subbab 6.7):

$$
\langle m_I \pm 1|\hat I_x|m_I\rangle = \frac\hbar2\sqrt{I(I+1) - m_I(m_I \pm 1)} . \qquad \text{(16.10)}
$$

Jadi aturan seleksinya $\Delta m_I = \pm1$, dan semua transisi yang diizinkan mempunyai frekuensi yang sama:

$$
h\nu_0 = \gamma\hbar B_0 \quad\Longleftrightarrow\quad \nu_0 = \frac{\gamma B_0}{2\pi} . \qquad \text{(16.11)}
$$

Inilah **syarat resonansi**. Frekuensi kuantumnya sama dengan frekuensi presesi Larmor klasik (16.6); kesamaan ini bukan kebetulan, seperti yang segera kita lihat. Perhatikan juga bahwa medan $B_1$ harus tegak lurus $B_0$: komponen yang sejajar $B_0$ hanya menghasilkan $\hat I_z$ dalam perturbasi, yang tidak mempunyai unsur matriks di luar diagonal.

Spektrometer NMR diberi nama menurut frekuensi proton dalam magnetnya: "spektrometer 400 MHz" berarti magnet 9,40 T; 600 MHz berarti 14,09 T; dan 1,2 GHz, magnet tertinggi yang tersedia secara komersial sekarang, berarti 28,2 T. Dalam magnet yang sama, inti lain beresonansi pada frekuensi yang sebanding dengan $\gamma$-nya, sehingga satu magnet melayani semua inti dengan mengganti frekuensi pemancar (tabel di subbab 16.1).

### Presesi Larmor dalam mekanika kuantum

Mengapa frekuensi kuantum (16.11) sama dengan frekuensi presesi klasik (16.6)? Ambil spin $\tfrac12$ dalam superposisi $\psi(0) = c_\alpha\alpha + c_\beta\beta$. Karena $\alpha$ dan $\beta$ adalah keadaan stasioner, masing-masing berevolusi dengan faktor fase sendiri (subbab 3.4):

$$
\psi(t) = c_\alpha e^{-iE_\alpha t/\hbar}\alpha + c_\beta e^{-iE_\beta t/\hbar}\beta , \qquad E_\alpha = -\tfrac12\gamma\hbar B_0, \quad E_\beta = +\tfrac12\gamma\hbar B_0 .
$$

Nilai harap $\langle\hat I_x\rangle$ melibatkan unsur matriks $\langle\alpha|\hat I_x|\beta\rangle = \langle\beta|\hat I_x|\alpha\rangle = \hbar/2$, sehingga

$$
\langle\hat I_x\rangle(t) = \frac\hbar2\left[c_\alpha^*c_\beta e^{-i(E_\beta - E_\alpha)t/\hbar} + \text{k.k.}\right] = \hbar|c_\alpha c_\beta|\cos(\omega_0t + \varphi) , \qquad \text{(16.12)}
$$

dengan $\omega_0 = (E_\beta - E_\alpha)/\hbar = \gamma B_0$ dan $\varphi$ fase awal. Dengan cara yang sama $\langle\hat I_y\rangle$ berosilasi dengan beda fase seperempat periode, sedangkan $\langle\hat I_z\rangle = \tfrac\hbar2(|c_\alpha|^2 - |c_\beta|^2)$ tetap. Vektor nilai harap $\langle\hat{\mathbf I}\rangle$ berpresesi pada kerucut dengan frekuensi Larmor: gambaran klasik ternyata tepat untuk nilai harap. Frekuensi presesi adalah frekuensi "denyut" antara dua tingkat energi, sama seperti pada sistem dua keadaan amonia (Contoh 4.44).

Hasil yang sama dapat diperoleh dengan persamaan gerak Heisenberg, $d\langle\hat A\rangle/dt = (i/\hbar)\langle[\hat H, \hat A]\rangle$. Dengan $[\hat I_z, \hat I_x] = i\hbar\hat I_y$:

$$
\frac{d\langle\hat{\mathbf I}\rangle}{dt} = \gamma\,\langle\hat{\mathbf I}\rangle \times \mathbf B , \qquad \text{(16.13)}
$$

persamaan klasik (16.5) yang berlaku untuk nilai harap. Karena Hamiltonian spin dalam medan bersifat linear dalam $\hat{\mathbf I}$, kesesuaian klasik–kuantum ini tepat, bukan pendekatan. Kenyataan inilah yang membuat **model vektor** (subbab 16.8) begitu berguna: kita dapat memikirkan magnetisasi sampel sebagai vektor klasik yang diputar-putar oleh pulsa.

::: {.dalam}
**Menurunkan (16.13) dari komutator**

Untuk $\hat H = -\gamma\mathbf B\cdot\hat{\mathbf I}$ dengan $\mathbf B$ sembarang, ambil komponen $x$: $[\hat H, \hat I_x] = -\gamma(B_y[\hat I_y, \hat I_x] + B_z[\hat I_z, \hat I_x]) = -\gamma(-i\hbar B_y\hat I_z + i\hbar B_z\hat I_y)$. Kalikan dengan $i/\hbar$:

$$
\frac{d\langle\hat I_x\rangle}{dt} = \gamma\left(B_z\langle\hat I_y\rangle - B_y\langle\hat I_z\rangle\right) = \gamma\left(\langle\hat{\mathbf I}\rangle \times \mathbf B\right)_x .
$$

Komponen $y$ dan $z$ diperoleh dengan permutasi siklis $x \to y \to z \to x$. Persamaan ini berlaku juga untuk $\mathbf B$ yang bergantung waktu, termasuk medan gelombang radio, sehingga menjadi dasar persamaan Bloch di subbab 16.8.
:::

::: {.awas}
**Proton tidak "menunjuk ke atas" atau "ke bawah"**

Gambar populer sering melukis spin dalam medan sebagai panah yang sebagian menunjuk ke atas dan sebagian ke bawah. Gambaran ini menyesatkan. Spin dalam keadaan $\alpha$ mempunyai $\langle\hat I_z\rangle = \hbar/2$ tetapi panjang vektornya $\hbar\sqrt{3}/2$, sehingga ia "miring" 54,7° dari sumbu $z$ dengan komponen tegak lurus yang tidak tertentu (model vektor, subbab 6.6). Lebih penting lagi, spin dalam sampel cair pada umumnya berada dalam superposisi $\alpha$ dan $\beta$ dengan fase acak. Yang teramati adalah jumlah semua spin, yaitu magnetisasi makroskopis, yang mematuhi persamaan klasik (16.13).
:::

::: {.contoh}
**Contoh 16.5 · Kuantum yang amat kecil**

Hitung selisih energi kedua tingkat proton dalam magnet 9,395 T (spektrometer 400 MHz), dalam J, J/mol, cm⁻¹, dan eV. Bandingkan dengan $k_BT$ pada 298 K.

**Penyelesaian.** $\Delta E = h\nu_0 = (6{,}626 \times 10^{-34})(4{,}00 \times 10^8) = 2{,}65 \times 10^{-25}$ J. Dikali $N_A$: 0,160 J/mol. Dibagi $hc$: 0,0133 cm⁻¹. Dalam eV: $1{,}65 \times 10^{-6}$ eV. $k_BT = 4{,}12 \times 10^{-21}$ J, sehingga $\Delta E/k_BT = 6{,}4 \times 10^{-5}$.

**Memahami hasil.** Energi transisi NMR sekitar $10^{-5}$ kali energi transisi getaran dan sekitar $10^{-6}$ kali energi transisi elektronik. Gelombang radio 400 MHz mempunyai panjang gelombang 75 cm; sampel jauh lebih kecil daripada panjang gelombangnya, sehingga NMR bekerja dengan kumparan dan rangkaian resonansi seperti radio, bukan dengan lensa dan kisi seperti spektroskopi optik.
:::

::: {.contoh}
**Contoh 16.6 · Satu magnet, banyak inti**

Sebuah spektrometer disebut "600 MHz". (a) Berapa kuat medannya? (b) Pada frekuensi berapa ¹³C, ¹⁹F, ³¹P, dan ¹⁵N beresonansi di magnet yang sama?

**Penyelesaian.** (a) $B_0 = 2\pi\nu_0/\gamma_\text{H} = 2\pi(6{,}00 \times 10^8)/(2{,}67522 \times 10^8) = 14{,}09$ T.

\(b) $\nu_X = 600\ \text{MHz} \times |\gamma_X|/\gamma_\text{H}$: ¹³C 150,9 MHz; ¹⁹F 564,8 MHz; ³¹P 243,1 MHz; ¹⁵N 60,8 MHz.

**Memahami hasil.** Frekuensi inti-inti ini terpisah jauh (puluhan sampai ratusan MHz), sehingga eksitasi satu jenis inti tidak mengganggu yang lain. Inilah yang memungkinkan percobaan **heteronuklir**: misalnya merekam ¹³C sambil terus menyinari proton untuk menghapus kopling C–H (dekopling), atau memindahkan polarisasi dari ¹H ke ¹³C (subbab 16.10).
:::

::: {.contoh}
**Contoh 16.7 · Deuterium: tiga tingkat, satu garis**

Deuterium ($I = 1$, $\gamma = 4{,}1066 \times 10^7$ rad s⁻¹ T⁻¹) dalam magnet 14,09 T. (a) Tuliskan energi ketiga tingkatnya dalam satuan $h\nu_0$ dan hitung $\nu_0$. (b) Hitung kuadrat unsur matriks $\hat I_x$ untuk transisi $-1 \to 0$ dan $0 \to +1$, serta untuk $-1 \to +1$.

**Penyelesaian.** (a) $E_{m} = -m\,h\nu_0$: $-h\nu_0$, 0, $+h\nu_0$ untuk $m = +1, 0, -1$. $\nu_0 = 92{,}1$ MHz.

\(b) Dari (16.10) dengan $I = 1$: $\langle 0|\hat I_x|{-1}\rangle = \tfrac\hbar2\sqrt{2 - (-1)(0)} = \hbar/\sqrt2$, kuadratnya $\hbar^2/2$. $\langle{+1}|\hat I_x|0\rangle = \tfrac\hbar2\sqrt{2 - 0} = \hbar/\sqrt2$, kuadrat $\hbar^2/2$. $\langle{+1}|\hat I_x|{-1}\rangle = 0$ karena $\hat I_x$ hanya mengubah $m$ sebesar satu.

**Memahami hasil.** Kedua transisi yang diizinkan sama kuat dan berfrekuensi sama, sehingga spektrum ²H dalam cairan hanya satu garis. Dalam padatan atau kristal cair, interaksi kuadrupol menggeser tingkat $m = 0$ relatif terhadap $m = \pm1$, dan garis itu terpecah menjadi dua; besar pemecahannya mengukur keteraturan orientasi ikatan C–D, misalnya dalam membran lipid.
:::

::: {.contoh}
**Contoh 16.8 · Unsur matriks spin $\tfrac12$ dan matriks Pauli**

Dalam basis $\{\alpha, \beta\}$, tuliskan matriks $\hat I_x$, $\hat I_y$, $\hat I_z$ untuk spin $\tfrac12$, lalu tunjukkan bahwa $[\hat I_x, \hat I_y] = i\hbar\hat I_z$.

**Penyelesaian.** Dari (16.10) dan $\hat I_y = (\hat I_+ - \hat I_-)/2i$:

$$
\hat I_x = \frac\hbar2\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}, \quad
\hat I_y = \frac\hbar2\begin{pmatrix}0 & -i\\ i & 0\end{pmatrix}, \quad
\hat I_z = \frac\hbar2\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix} .
$$

$\hat I_x\hat I_y = \tfrac{\hbar^2}{4}\begin{pmatrix}i & 0\\ 0 & -i\end{pmatrix}$ dan $\hat I_y\hat I_x = \tfrac{\hbar^2}{4}\begin{pmatrix}-i & 0\\ 0 & i\end{pmatrix}$; selisihnya $\tfrac{\hbar^2}{2}\begin{pmatrix}i & 0\\ 0 & -i\end{pmatrix} = i\hbar\hat I_z$.

**Memahami hasil.** Matriks dalam kurung adalah **matriks Pauli** $\sigma_x$, $\sigma_y$, $\sigma_z$, yang sama dengan matriks spin elektron (subbab 9.2). Seluruh "aljabar NMR" untuk inti berspin $\tfrac12$ adalah aljabar matriks 2 × 2 ini dan hasil kali tensornya; program simulasi spektrum di subbab 16.6 tidak memerlukan apa pun selain matriks-matriks ini.
:::

::: {.kuis}
**Kuis cepat 16.2**

Dalam medan yang sama, inti mana yang celah Zeemannya lebih besar: ¹⁹F atau ³¹P? Mengapa transisi $\Delta m_I = \pm2$ inti berspin 1 tidak teramati dengan medan $B_1$ biasa?
:::

## 16.3 Populasi dan kepekaan

### Selisih populasi yang amat tipis

Sinyal NMR berasal dari **selisih** antara serapan (dari $\alpha$ ke $\beta$) dan pancaran terstimulasi (dari $\beta$ ke $\alpha$). Koefisien Einstein untuk keduanya sama (subbab 15.1), sehingga sinyal bersih sebanding dengan selisih populasi. Pada kesetimbangan termal, populasi mengikuti distribusi Boltzmann:

$$
\frac{N_\beta}{N_\alpha} = e^{-\Delta E/k_BT}, \qquad \frac{N_\alpha - N_\beta}{N_\alpha + N_\beta} = \tanh\frac{\gamma\hbar B_0}{2k_BT} \approx \frac{\gamma\hbar B_0}{2k_BT} . \qquad \text{(16.14)}
$$

Pendekatan terakhir sangat baik, karena argumen tanh berorde $10^{-5}$. Untuk proton pada 400 MHz dan 298 K, selisih relatifnya $3{,}2 \times 10^{-5}$: dari satu juta proton, 500 016 berada di tingkat $\alpha$ dan 499 984 di tingkat $\beta$ (bandingkan Contoh 1.53). Hanya selisih 32 per sejuta inilah yang menghasilkan sinyal.

### Magnetisasi kesetimbangan

Jumlah momen magnet semua inti per satuan volume adalah **magnetisasi** $\mathbf M$. Dalam kesetimbangan, komponen tegak lurusnya nol (fase acak) dan komponen-$z$-nya

$$
M_0 = \mathcal N\langle\mu_z\rangle = \frac{\mathcal N\gamma^2\hbar^2I(I+1)}{3k_BT}\,B_0 , \qquad \text{(16.15)}
$$

dengan $\mathcal N$ banyaknya inti per satuan volume. Ini **hukum Curie** untuk paramagnetisme inti: magnetisasi sebanding dengan medan dan berbanding terbalik dengan suhu. Untuk spin $\tfrac12$, $I(I+1)/3 = \tfrac14$.

::: {.dalam}
**Menurunkan hukum Curie (16.15)**

Nilai harap termal $\mu_z$ untuk satu inti adalah rata-rata Boltzmann atas $2I + 1$ tingkat:

$$
\langle\mu_z\rangle = \frac{\sum_m \gamma\hbar m\,e^{mx}}{\sum_m e^{mx}}, \qquad x = \frac{\gamma\hbar B_0}{k_BT} .
$$

Untuk $x \ll 1$, uraikan $e^{mx} \approx 1 + mx$. Penyebut: $\sum_m(1 + mx) = 2I + 1$, karena $\sum_m m = 0$. Pembilang: $\gamma\hbar\sum_m(m + m^2x) = \gamma\hbar x\sum_m m^2$. Jumlah kuadrat $m$ dari $-I$ sampai $I$ adalah $\tfrac13I(I+1)(2I+1)$. Jadi $\langle\mu_z\rangle = \gamma\hbar x\,I(I+1)/3 = \gamma^2\hbar^2I(I+1)B_0/3k_BT$. Rumus yang sama, dengan $\gamma\hbar \to g\mu_B$, berlaku untuk paramagnetisme elektron (subbab 16.11) dan menjelaskan kerentanan magnet kompleks logam transisi (subbab 14.5).
:::

### Mengapa NMR kurang peka, dan apa yang dapat dilakukan

Sinyal NMR adalah tegangan yang diinduksi dalam kumparan oleh magnetisasi yang berpresesi. Menurut hukum Faraday, tegangan itu sebanding dengan laju perubahan fluks, yaitu dengan $\omega_0M_0$. Karena $M_0 \propto \gamma^2B_0$ dan $\omega_0 = \gamma B_0$, sinyal $\propto \gamma^3B_0^2$. Derau listrik di kumparan juga naik dengan frekuensi, kira-kira sebanding dengan $\omega_0^{1/2}$, sehingga perbandingan sinyal terhadap derau

$$
\frac SN \propto \mathcal N\,I(I+1)\,|\gamma|^{5/2}B_0^{3/2} . \qquad \text{(16.16)}
$$

Hubungan ini menerangkan tiga kenyataan praktis NMR.

**Inti dengan $\gamma$ besar lebih mudah.** Proton dan ¹⁹F mempunyai $\gamma$ terbesar di antara inti stabil, sehingga paling peka. Bila kelimpahan alami ikut diperhitungkan, besaran baku yang dipakai untuk membandingkan inti adalah **kepekaan relatif** (*receptivity*), $|\gamma|^3I(I+1)\times$kelimpahan, dinormalkan terhadap ¹H. Untuk ¹³C nilainya $1{,}7 \times 10^{-4}$, dan untuk ¹⁵N hanya $3{,}8 \times 10^{-6}$ (kolom terakhir tabel di subbab 16.1).

**Magnet yang lebih kuat lebih baik, dengan dua cara.** Kepekaan naik sebagai $B_0^{3/2}$, dan seperti akan kita lihat, geseran kimia dalam Hz juga sebanding dengan $B_0$ sementara kopling tidak, sehingga spektrum menjadi lebih sederhana (subbab 16.6). Itulah sebabnya laboratorium rela membayar mahal untuk magnet 800 MHz ke atas.

**Pengulangan menambah S/N sebagai akar.** Sinyal dari $n$ perekaman bertambah sebanding $n$, sedangkan derau acak sebanding $\sqrt n$. Jadi S/N naik sebagai $\sqrt n$. Melipatduakan S/N memerlukan empat kali lebih banyak perekaman.

Untuk melampaui batas Boltzmann, ada teknik **hiperpolarisasi**: memindahkan polarisasi elektron yang jauh lebih besar ke inti (*dynamic nuclear polarization*, DNP), memakai para-hidrogen yang spinnya sudah tertata, atau memompa ¹²⁹Xe dengan laser terpolarisasi. Teknik-teknik ini dapat menaikkan sinyal ribuan sampai puluhan ribu kali, dan memungkinkan, misalnya, pencitraan paru-paru dengan gas xenon terhiperpolarisasi.

::: {.contoh}
**Contoh 16.9 · Selisih populasi pada berbagai kondisi**

Hitung selisih populasi relatif proton $(N_\alpha - N_\beta)/N$ untuk (a) 400 MHz pada 298 K, (b) 1,2 GHz pada 298 K, (c) 400 MHz pada 4,2 K.

**Penyelesaian.** Dengan (16.14), $\Delta n/N = \tanh(h\nu_0/2k_BT)$: (a) $3{,}22 \times 10^{-5}$; (b) $9{,}66 \times 10^{-5}$; (c) $2{,}29 \times 10^{-3}$.

**Memahami hasil.** Menaikkan medan tiga kali menaikkan polarisasi tiga kali; mendinginkan sampel dari suhu kamar ke suhu helium cair menaikkannya 71 kali. Pendinginan sampel cair tidak praktis, tetapi pendinginan **kumparan penerima** dan penguat awal ke sekitar 20 K (*cryoprobe*) mengurangi derau termal dan menaikkan S/N sekitar empat kali, setara dengan enam belas kali penghematan waktu.
:::

::: {.contoh}
**Contoh 16.10 · Magnetisasi air**

Air murni mengandung $6{,}69 \times 10^{28}$ proton per m³. Hitung $M_0$ dalam magnet 9,4 T pada 298 K dan bandingkan medan magnet yang dihasilkannya, $\mu_0M_0$, dengan $B_0$.

**Penyelesaian.** Dengan (16.15) dan $I(I+1)/3 = \tfrac14$:

$$
M_0 = \frac{(6{,}69 \times 10^{28})(2{,}675 \times 10^8)^2(1{,}0546 \times 10^{-34})^2(9{,}4)}{4(1{,}381 \times 10^{-23})(298)} = 0{,}030\ \text{A/m} .
$$

$\mu_0M_0 = 3{,}8 \times 10^{-8}$ T, sekitar $4 \times 10^{-9}$ kali $B_0$.

**Memahami hasil.** Magnetisasi inti air hanya sepersejuta magnetisasi diamagnetik elektronnya, tetapi ia dapat dibedakan karena berpresesi pada frekuensi resonansinya sendiri. Kumparan penerima yang ditala tepat pada frekuensi itu "mendengar" magnetisasi kecil ini di tengah medan statis yang $10^8$ kali lebih kuat, mirip pesawat radio yang menangkap satu stasiun lemah di antara banyak stasiun lain.
:::

::: {.contoh}
**Contoh 16.11 · Mengapa spektrum ¹³C lama direkam**

Bandingkan S/N satu inti ¹³C dengan satu inti ¹H dalam magnet yang sama menurut (16.16), lalu masukkan kelimpahan alami ¹³C (1,07%). Berapa kali lebih banyak perekaman diperlukan agar spektrum ¹³C mencapai S/N yang sama dengan spektrum ¹H sekali rekam, untuk konsentrasi molekul yang sama dan satu atom C per satu atom H?

**Penyelesaian.** $(\gamma_\text{C}/\gamma_\text{H})^{5/2} = (0{,}2515)^{5/2} = 0{,}0317$. Dikali kelimpahan: $3{,}4 \times 10^{-4}$. Karena S/N $\propto \sqrt n$, banyaknya perekaman yang diperlukan $(1/3{,}4 \times 10^{-4})^2 \approx 9 \times 10^6$.

**Memahami hasil.** Sembilan juta perekaman tentu tidak praktis. Dalam kenyataan, spektrum ¹³C menjadi mungkin karena tiga hal: sampel yang lebih pekat, dekopling proton yang menyatukan multiplet menjadi satu garis, dan efek Overhauser inti yang memperkuat sinyal ¹³C hingga hampir tiga kali (subbab 16.9). Bahkan dengan bantuan itu, spektrum ¹³C sering memerlukan ratusan sampai ribuan perekaman.
:::

::: {.contoh}
**Contoh 16.12 · Waktu dan medan**

Sebuah spektrum memberi S/N = 10 setelah 16 perekaman di spektrometer 400 MHz. (a) Berapa perekaman diperlukan untuk S/N = 50? (b) Bila dipindah ke spektrometer 900 MHz dengan probe yang setara, berapa S/N untuk 16 perekaman, dan berapa kali waktu dihemat untuk S/N yang sama?

**Penyelesaian.** (a) $n = 16 \times (50/10)^2 = 400$ perekaman.

\(b) S/N $\propto B_0^{3/2}$: $(900/400)^{3/2} = 3{,}38$, jadi S/N $\approx 34$. Untuk S/N yang sama diperlukan $3{,}38^2 = 11{,}4$ kali lebih sedikit perekaman.

**Memahami hasil.** Penghematan waktu sebelas kali berarti percobaan semalam menjadi percobaan satu jam. Untuk sampel protein yang hanya stabil beberapa hari, atau untuk bahan alam yang hanya tersedia sedikit, perbedaan ini menentukan apakah percobaan dapat dikerjakan sama sekali.
:::

::: {.contoh}
**Contoh 16.13 · Polarisasi elektron untuk DNP**

Dalam percobaan DNP, sampel didinginkan sampai 1,2 K dalam medan 3,35 T. Hitung polarisasi elektron ($g = 2{,}0023$) dan polarisasi proton pada kondisi itu, serta polarisasi proton pada 298 K. Bandingkan dengan batas peningkatan $\gamma_e/\gamma_\text{H}$.

**Penyelesaian.** Polarisasi $P = \tanh(\Delta E/2k_BT)$. Elektron: $\Delta E = g\mu_BB_0 = 6{,}22 \times 10^{-23}$ J, $P_e = \tanh(1{,}88) = 0{,}954$. Proton pada 1,2 K: $P_\text{H} = 2{,}85 \times 10^{-3}$. Proton pada 298 K: $1{,}15 \times 10^{-5}$. Perbandingan $\gamma_e/\gamma_\text{H} = 658$.

**Memahami hasil.** Pada 1,2 K elektron hampir terpolarisasi penuh, sedangkan proton hanya 0,3%. Gelombang mikro yang menyinari transisi elektron memindahkan polarisasi ini ke inti di sekitarnya. Bila sampel kemudian dicairkan dengan cepat dan dipindahkan ke spektrometer suhu kamar, polarisasi ¹³C dapat mencapai puluhan persen, puluhan ribu kali nilai Boltzmann. Teknik ini dipakai untuk mengikuti metabolisme piruvat bertanda ¹³C dalam tumor secara langsung.
:::

::: {.kuis}
**Kuis cepat 16.3**

Bila suhu sampel dinaikkan dari 298 K ke 348 K, bagaimana selisih populasi dan sinyal NMR berubah? Mengapa pengulangan 100 kali hanya menaikkan S/N sepuluh kali?
:::
