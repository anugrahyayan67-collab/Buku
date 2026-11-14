## 3.9 Sumur potensial terhingga

Dinding tak hingga adalah idealisasi. Elektron dalam molekul atau dalam nanokristal terikat oleh potensial yang dalamnya berhingga, beberapa elektronvolt. Model berikutnya adalah **sumur persegi terhingga** dengan lebar $2a$ dan kedalaman $V_0$:

$$
V(x) = \begin{cases}0, & |x| < a\\ V_0, & |x| \ge a\end{cases}
$$

Kita mencari keadaan terikat, $0 < E < V_0$. Titik asal sengaja diletakkan di tengah sumur agar paritas dapat dimanfaatkan.

### Penyelesaian di setiap daerah

**Di dalam** ($|x| < a$): $\psi'' = -k^2\psi$ dengan $k = \sqrt{2mE}/\hbar$. Penyelesaiannya kosinus (genap) atau sinus (ganjil).

**Di luar** ($|x| > a$): $V_0 > E$, sehingga $\psi'' = \kappa^2\psi$ dengan

$$
\kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar} .
$$

Penyelesaiannya $e^{\pm\kappa x}$. Agar $\psi$ dapat dinormalisasi, hanya $e^{-\kappa x}$ yang boleh dipakai untuk $x > a$ dan $e^{+\kappa x}$ untuk $x < -a$. Fungsi gelombang **menembus** daerah yang terlarang secara klasik dan meluruh di sana dengan panjang khas $1/\kappa$.

### Syarat sambung

Di $x = \pm a$ potensialnya melompat dengan besar berhingga. Persamaan Schrödinger, $\psi'' = (2m/\hbar^2)(V - E)\psi$, menunjukkan bahwa $\psi''$ melompat, sehingga $\psi'$ tetap malar (integral lompatan berhingga atas selang nol adalah nol), dan $\psi$ juga malar. Jadi di batas yang potensialnya melompat berhingga, **$\psi$ dan $d\psi/dx$ keduanya malar**. (Di dinding tak hingga hanya $\psi$ yang malar; turunannya boleh melompat.)

Untuk keadaan genap, $\psi = A\cos kx$ di dalam dan $Ce^{-\kappa x}$ untuk $x > a$. Kesinambungan di $x = a$:

$$
A\cos ka = Ce^{-\kappa a}, \qquad -kA\sin ka = -\kappa Ce^{-\kappa a} .
$$

Bagi persamaan kedua dengan yang pertama: $k\tan ka = \kappa$. Untuk keadaan ganjil dengan cara yang sama: $-k\cot ka = \kappa$. Dalam variabel tak berdimensi $z = ka$ dan

$$
z_0 = \frac{a\sqrt{2mV_0}}{\hbar}, \qquad \kappa a = \sqrt{z_0^2 - z^2} ,
$$

syarat kuantisasinya menjadi

$$
\tan z = \frac{\sqrt{z_0^2 - z^2}}{z}\ \ \text{(genap)}, \qquad -\cot z = \frac{\sqrt{z_0^2 - z^2}}{z}\ \ \text{(ganjil)} . \qquad \text{(3.18)}
$$

Persamaan transenden ini tidak mempunyai penyelesaian dalam bentuk tertutup. Ia diselesaikan secara grafis (Gambar 3.7 kiri) atau numerik. Seluruh fisikanya tersimpan dalam satu bilangan $z_0$, yang mengukur "kekuatan" sumur: makin lebar dan dalam sumurnya, makin besar $z_0$.

![Gambar 3.7 Sumur persegi terhingga untuk elektron dengan $V_0 = 5$ eV dan lebar 1,0 nm ($z_0 = 5{,}73$). Kiri: penyelesaian grafis (3.18); setiap perpotongan kurva jingga dengan cabang tan (genap) atau −cot (ganjil) adalah satu keadaan terikat. Kanan: keempat keadaan terikat. Fungsi gelombang menembus dinding dan meluruh secara eksponensial.](fig/c_sumur.png){width=92%}

### Sifat-sifat penyelesaian

1. **Banyaknya keadaan terikat berhingga.** Cabang-cabang tan dan −cot bergantian setiap $\pi/2$, dan kurva $\sqrt{z_0^2 - z^2}/z$ berakhir di $z = z_0$. Jadi banyaknya keadaan terikat adalah bilangan bulat terkecil yang tidak kurang dari $2z_0/\pi$. Di atas $V_0$, energinya malar (partikel tidak terikat).
2. **Selalu ada sedikitnya satu keadaan terikat**, sedangkal apa pun sumurnya, karena cabang tan pertama dimulai dari nol di $z = 0$. (Hal ini khusus untuk satu dimensi; dalam tiga dimensi sumur yang terlalu dangkal tidak mengikat apa pun.)
3. **Energi lebih rendah daripada sumur tak hingga** dengan lebar yang sama, karena fungsi gelombang "meluber" keluar sehingga panjang gelombangnya lebih panjang.
4. Untuk $z_0 \to \infty$, akar-akar mendekati $z = n\pi/2$, dan energinya mendekati sumur tak hingga dengan $L = 2a$.

::: {.contoh}
**Contoh 3.29 · Elektron dalam sumur 5 eV**

Elektron berada dalam sumur dengan $V_0 = 5{,}0$ eV dan lebar $2a = 1{,}0$ nm. (a) Hitung $z_0$ dan banyaknya keadaan terikat. (b) Penyelesaian numerik (3.18) memberikan energi 0,272; 1,077; 2,379; dan 4,059 eV. Bandingkan dengan sumur tak hingga 1,0 nm. (c) Hitung panjang penembusan $1/\kappa$ keadaan dasar.

**Penyelesaian.** (a) $z_0 = \dfrac{(0{,}5 \times 10^{-9})\sqrt{2(9{,}109 \times 10^{-31})(5{,}0 \times 1{,}602 \times 10^{-19})}}{1{,}0546 \times 10^{-34}} = 5{,}73$. Banyaknya keadaan: $2z_0/\pi = 3{,}65$, dibulatkan ke atas: 4.

(b) Sumur tak hingga: 0,376; 1,504; 3,384; 6,016 eV. Energi sumur terhingga 28–33% lebih rendah, dan keadaan keempat sumur tak hingga (6,0 eV) bahkan berada di atas $V_0$.

(c) $\kappa = \sqrt{2m_e(5{,}0 - 0{,}272)\,e}/\hbar = 1{,}11 \times 10^{10}$ m⁻¹, sehingga $1/\kappa = 0{,}090$ nm.

**Memahami hasil.** Fungsi gelombang keadaan dasar menembus sekitar 0,09 nm ke setiap dinding, sehingga "lebar efektif" sumurnya sekitar 1,18 nm. Memang, sumur tak hingga 1,18 nm memberi $E_1 = 0{,}27$ eV. Ini membenarkan trik dalam model elektron bebas (subbab 3.8) yang menambahkan sedikit panjang di kedua ujung rantai.
:::

::: {.contoh}
**Contoh 3.30 · Sumur dangkal hanya mengikat satu keadaan**

(a) Elektron dalam sumur $V_0 = 1{,}0$ eV selebar 0,50 nm. (b) Elektron dalam sumur $V_0 = 0{,}30$ eV selebar 1,0 nm. Hitung $z_0$ masing-masing dan berapa keadaan terikatnya.

**Penyelesaian.** $z_0 \propto a\sqrt{V_0}$. Dari Contoh 3.29 ($a = 0{,}5$ nm, $V_0 = 5$ eV, $z_0 = 5{,}73$): (a) $a = 0{,}25$ nm, $V_0 = 1$ eV: $z_0 = 5{,}73 \times 0{,}5 \times \sqrt{0{,}2} = 1{,}28$. (b) $a = 0{,}5$ nm, $V_0 = 0{,}3$ eV: $z_0 = 5{,}73\sqrt{0{,}06} = 1{,}40$. Keduanya kurang dari $\pi/2 = 1{,}571$, jadi masing-masing hanya **satu** keadaan terikat (genap). Penyelesaian numerik: (a) 0,438 eV, (b) 0,120 eV.

**Memahami hasil.** Pada sumur dangkal, satu-satunya keadaan terikat menyimpan sebagian besar peluangnya di luar sumur. Elektron yang terikat lemah semacam ini adalah model untuk anion yang elektron tambahannya terikat lemah dan untuk "elektron terlarut" dalam amonia cair, yang terperangkap dalam rongga pelarut.
:::

::: {.terapan}
**Kaitan kimia · Sumur kuantum buatan**

Dengan menumbuhkan lapisan GaAs setebal beberapa nanometer di antara dua lapisan AlGaAs (yang celah pitanya lebih besar), insinyur membuat sumur persegi terhingga hampir sempurna untuk elektron. Tingkat-tingkat energinya diatur dengan memilih ketebalan lapisan, persis seperti (3.18). Laser dioda dalam pemutar cakram dan penghubung serat optik, serta LED biru berbasis InGaN, bekerja dengan sumur kuantum semacam ini. Bahan-bahan itu ditumbuhkan dengan epitaksi uap kimia organologam (MOCVD), sebuah proses kimia yang dikendalikan sampai satu lapisan atom.
:::

::: {.contoh}
**Contoh 3.31 · Keadaan yang paling "bocor"**

Untuk sumur Contoh 3.29 ($V_0 = 5{,}0$ eV, lebar 1,0 nm), hitung panjang penembusan keadaan keempat ($E = 4{,}059$ eV) dan bandingkan dengan keadaan dasar.

**Penyelesaian.** $V_0 - E = 0{,}941$ eV, sehingga $\kappa = \sqrt{2m_e(0{,}941\ \text{eV})}/\hbar = 4{,}97 \times 10^9$ m⁻¹ dan $1/\kappa = 0{,}20$ nm, lebih dari dua kali panjang penembusan keadaan dasar (0,090 nm).

**Memahami hasil.** Keadaan yang energinya dekat bibir sumur menyebar jauh ke luar. Dalam atom, orbital Rydberg dan orbital elektron valensi yang terikat lemah, misalnya elektron 3s natrium, juga meluas jauh, dan itulah sebabnya atom-atom alkali besar dan mudah dipolarisasi. Dalam molekul, keadaan tereksitasi yang tinggi dan elektron tambahan anion sering memerlukan fungsi basis "difus" (Bab 17) untuk menggambarkan ekor panjang ini.
:::

### Penyelesaian numerik: metode beda hingga

Untuk potensial yang bentuknya sembarang, persamaan (3.8) diselesaikan secara numerik. Cara yang paling mudah dipahami adalah **metode beda hingga**. Bagilah sumbu $x$ menjadi $N$ titik berjarak $\Delta x$, dan hampiri turunan kedua dengan selisih (dari deret Taylor, subbab 2.9):

$$
\psi''(x_j) \approx \frac{\psi_{j+1} - 2\psi_j + \psi_{j-1}}{(\Delta x)^2} .
$$

Persamaan Schrödinger berubah menjadi sistem persamaan linear $\sum_jH_{ij}\psi_j = E\psi_i$, yaitu masalah nilai eigen matriks (subbab 2.8). Matriks Hamiltonnya tridiagonal: unsur diagonal $2t + V(x_j)$ dan unsur di sebelahnya $-t$, dengan $t = \hbar^2/2m(\Delta x)^2$. Nilai eigen terendahnya adalah energi keadaan terikat, dan vektor eigennya adalah fungsi gelombang di titik-titik kisi.

```python
import numpy as np
hb, me, e = 1.054571817e-34, 9.1093837015e-31, 1.602176634e-19
N = 1500; x = np.linspace(-1.5e-9, 1.5e-9, N); dx = x[1] - x[0]
V = np.where(np.abs(x) < 0.5e-9, 0.0, 5.0) * e        # sumur 5 eV, lebar 1 nm
t = hb**2 / (2*me*dx**2)
H = np.diag(2*t + V) - t*np.eye(N, k=1) - t*np.eye(N, k=-1)
E, psi = np.linalg.eigh(H)
print(E[:4] / e)        # [0.2715 1.0762 2.3766 4.0554]
```

::: {.contoh}
**Contoh 3.32 · Memeriksa metode numerik**

Bandingkan hasil kode di atas dengan penyelesaian tepat (3.18) untuk sumur 5,0 eV selebar 1,0 nm: 0,2718; 1,0774; 2,3792; 4,0593 eV. Berapa galat relatifnya, dan bagaimana galat itu dapat dikurangi?

**Penyelesaian.** Galat relatif: 0,11%; 0,11%; 0,11%; 0,10%. Galat berasal dari dua sumber: jarak kisi $\Delta x = 2$ pm (galat hampiran beda hingga sebanding $(\Delta x)^2$) dan tepi sumur yang jatuh di antara titik kisi. Memperkecil $\Delta x$ atau memakai rumus turunan orde lebih tinggi mengurangi galat.

**Memahami hasil.** Dengan sepuluh baris Python kita dapat menyelesaikan persamaan Schrödinger satu dimensi untuk potensial **apa pun**: sumur ganda amonia, potensial Morse, atau potensial rotasi internal. Metode ini adalah versi paling sederhana dari strategi kimia komputasi: ubah persamaan diferensial menjadi masalah nilai eigen matriks, lalu diagonalkan. Metode Numerov yang lebih teliti dibahas di Bab 5.
:::

::: {.kuis}
**Kuis cepat 3.9**

Sebuah sumur mempunyai $z_0 = 4{,}0$. Berapa banyak keadaan terikatnya? Jika kedalamannya dijadikan empat kali (lebar tetap), berapa banyak?
:::

## 3.10 Tangga potensial dan pantulan

Sejauh ini kita membahas keadaan terikat. Sekarang kita tinjau partikel yang **datang** dari jauh dan menumbuk perubahan potensial. Ini adalah masalah **hamburan**, dan pertanyaannya bukan "energi apa yang diizinkan" (semua energi diizinkan) melainkan "berapa peluang partikel dipantulkan atau diteruskan".

### Tangga dengan $E > V_0$

Misalkan $V = 0$ untuk $x < 0$ dan $V = V_0$ untuk $x > 0$, dan partikel datang dari kiri dengan energi $E > V_0$. Secara klasik partikel pasti melewati tangga, hanya diperlambat. Dalam mekanika kuantum:

- Di kiri: gelombang datang ditambah gelombang pantul, $\psi = e^{ik_1x} + re^{-ik_1x}$ dengan $k_1 = \sqrt{2mE}/\hbar$.
- Di kanan: hanya gelombang yang diteruskan, $\psi = te^{ik_2x}$ dengan $k_2 = \sqrt{2m(E - V_0)}/\hbar$.

Kesinambungan $\psi$ dan $\psi'$ di $x = 0$:

$$
1 + r = t, \qquad ik_1(1 - r) = ik_2t .
$$

Selesaikan: $r = \dfrac{k_1 - k_2}{k_1 + k_2}$ dan $t = \dfrac{2k_1}{k_1 + k_2}$. Peluang pantulan dan transmisi adalah perbandingan **arus** peluang (subbab 3.3), bukan sekadar perbandingan amplitudo kuadrat, karena kecepatan di kedua sisi berbeda:

$$
R = |r|^2 = \left(\frac{k_1 - k_2}{k_1 + k_2}\right)^2, \qquad T = \frac{k_2}{k_1}|t|^2 = \frac{4k_1k_2}{(k_1 + k_2)^2} . \qquad \text{(3.19)}
$$

Mudah diperiksa bahwa $R + T = 1$: peluang kekal.

Hasil ini mengejutkan: **partikel dapat dipantulkan oleh tangga yang dapat dilompatinya** (Gambar 3.8). Pantulan besar ketika $E$ hanya sedikit di atas $V_0$ ($k_2 \to 0$, $R \to 1$) dan kecil ketika $E \gg V_0$. Rumus (3.19) simetris terhadap pertukaran $k_1$ dan $k_2$, sehingga partikel yang **jatuh** ke tangga yang lebih rendah juga dapat dipantulkan, seperti cahaya yang sebagian dipantulkan ketika masuk dari udara ke kaca. Pantulan terjadi karena panjang gelombang berubah tiba-tiba; perubahan potensial yang landai (dibandingkan panjang gelombang) hampir tidak memantulkan.

### Tangga dengan $E < V_0$

Jika $E < V_0$, di kanan $\psi = te^{-\kappa x}$ meluruh. Arus yang diteruskan nol ($\psi$ riil di kanan, sampai faktor fase), sehingga $R = 1$: semua partikel akhirnya dipantulkan, seperti dalam fisika klasik. Tetapi peluang menemukan partikel di dalam daerah terlarang tidak nol; ia meluruh dengan panjang penembusan $1/\kappa$. Jika daerah terlarang itu hanya berupa penghalang tipis, partikel dapat muncul di seberangnya. Itulah penerobosan (subbab 3.11).

![Gambar 3.8 Peluang pantulan dan transmisi pada tangga potensial setinggi $V_0$, terhadap $E/V_0$. Untuk $E < V_0$ semua partikel dipantulkan. Untuk $E > V_0$ fisika klasik meramalkan $R = 0$, tetapi pantulan kuantum tetap terjadi, terutama di dekat $E = V_0$.](fig/c_tangga.png){width=60%}

::: {.contoh}
**Contoh 3.33 · Elektron pada tangga**

Elektron menumbuk tangga potensial setinggi 2,0 eV. Hitung $R$ dan $T$ untuk energi (a) 5,0 eV, (b) 2,1 eV.

**Penyelesaian.** Karena $k \propto \sqrt{E}$, perbandingan $k_2/k_1 = \sqrt{(E - V_0)/E}$.

(a) $k_2/k_1 = \sqrt{3/5} = 0{,}775$. $R = \left(\dfrac{1 - 0{,}775}{1 + 0{,}775}\right)^2 = 0{,}016$; $T = 0{,}984$.

(b) $k_2/k_1 = \sqrt{0{,}1/2{,}1} = 0{,}218$. $R = \left(\dfrac{0{,}782}{1{,}218}\right)^2 = 0{,}41$.

**Memahami hasil.** Elektron yang energinya hanya 5% di atas tangga dipantulkan 41% dari waktu. Efek semacam ini nyata dalam fisika permukaan: elektron berenergi rendah yang mendekati permukaan logam sebagian dipantulkan oleh perubahan potensial di permukaan, dan pola pantulan itu dipakai dalam LEED (subbab 1.7).
:::

::: {.contoh}
**Contoh 3.34 · Panjang penembusan**

Elektron berenergi 1,0 eV menumbuk tangga 5,0 eV. Hitung panjang penembusan $1/\kappa$. Pada jarak berapa rapat peluangnya turun menjadi 1% nilainya di tepi tangga?

**Penyelesaian.** $\kappa = \sqrt{2m_e(4{,}0\ \text{eV})}/\hbar = 1{,}02 \times 10^{10}$ m⁻¹, sehingga $1/\kappa = 0{,}098$ nm. Rapat peluang $\propto e^{-2\kappa x}$; turun menjadi 1% ketika $2\kappa x = \ln 100 = 4{,}61$, yaitu $x = 0{,}23$ nm.

**Memahami hasil.** Penembusan elektron ke daerah terlarang hanya beberapa per sepuluh nanometer, tetapi itu seukuran jarak antaratom. Elektron dalam molekul selalu "bocor" sedikit ke daerah yang secara klasik terlarang, misalnya ke luar molekul (asal ekor kerapatan elektron yang dipakai untuk mengukur ukuran molekul) dan ke celah antarmolekul (asal kopling elektronik dalam transfer elektron jarak jauh).
:::

::: {.contoh}
**Contoh 3.35 · Memeriksa kekekalan peluang**

Tunjukkan bahwa (3.19) memenuhi $R + T = 1$, dan bahwa $T = |t|^2$ akan memberikan jawaban yang salah.

**Penyelesaian.** $R + T = \dfrac{(k_1 - k_2)^2 + 4k_1k_2}{(k_1 + k_2)^2} = \dfrac{(k_1 + k_2)^2}{(k_1 + k_2)^2} = 1$. Sebaliknya $|r|^2 + |t|^2 = \dfrac{(k_1 - k_2)^2 + 4k_1^2}{(k_1 + k_2)^2}$, yang tidak sama dengan 1 kecuali $k_1 = k_2$.

**Memahami hasil.** Gelombang di kanan bergerak lebih lambat, jadi rapat peluang yang sama membawa arus yang lebih kecil. Peluang transmisi adalah perbandingan arus, bukan perbandingan amplitudo. Kesalahan ini mudah dibuat, dan pemeriksaan $R + T = 1$ menangkapnya.
:::

### Lewat di atas sumur: efek Ramsauer

Partikel yang melewati sumur (bukan tangga) dengan $E > 0$ juga sebagian dipantulkan, oleh dua tepi sumur. Gelombang yang dipantulkan tepi depan dan tepi belakang berinterferensi. Jika panjang gelombang di dalam sumur memenuhi $k_2a = n\pi$ (lebar sumur kelipatan setengah panjang gelombang), kedua pantulan saling meniadakan dan **transmisinya sempurna**. Peluang transmisi melalui sumur sedalam $V_0$ dan selebar $a$ adalah

$$
T = \left[1 + \frac{V_0^2\sin^2(k_2a)}{4E(E + V_0)}\right]^{-1}, \qquad k_2 = \frac{\sqrt{2m(E + V_0)}}{\hbar} .
$$

Pada tahun 1921 Carl Ramsauer dan John Townsend menemukan bahwa elektron sekitar 0,7 eV melewati gas argon, kripton, dan xenon hampir tanpa terhambur, sesuatu yang mustahil secara klasik. Atom gas mulia bertindak sebagai sumur tarik bagi elektron yang lewat, dan pada energi tertentu sumur itu "transparan".

::: {.contoh}
**Contoh 3.36 · Model efek Ramsauer**

Model atom argon sebagai sumur satu dimensi sedalam 3,5 eV dan selebar 0,30 nm. (a) Pada energi berapa elektron diteruskan sempurna ($n = 1$)? (b) Hitung $T$ pada 0,20 eV dan 2,0 eV.

**Penyelesaian.** (a) $k_2a = \pi$ berarti $E + V_0 = (\pi\hbar/a)^2/2m_e = 4{,}18$ eV (energi $E_1$ kotak 0,30 nm), jadi $E = 0{,}68$ eV.

(b) Dengan rumus di atas: $T(0{,}20\ \text{eV}) = 0{,}88$; $T(2{,}0\ \text{eV}) = 0{,}95$.

**Memahami hasil.** Model satu dimensi yang sangat kasar sudah menempatkan energi transparansi di sekitar 0,7 eV, dekat nilai teramati untuk argon. Gejala yang sama, interferensi antara pantulan di dua tepi, menjelaskan lapisan antipantul pada lensa kamera dan warna gelembung sabun. Dalam hamburan elektron oleh molekul, efek semacam ini mengatur laju pembentukan ion negatif dan kerusakan DNA oleh elektron berenergi rendah.
:::

::: {.kuis}
**Kuis cepat 3.10**

Sebuah elektron berenergi 3 eV datang dari daerah $V = 2$ eV menuju daerah $V = 0$ (tangga turun). Apakah elektron itu dapat dipantulkan? Hitung $R$.
:::
