# Bab 5 Osilator Harmonik

Ambil satu tetes air dan satu tetes air berat (D₂O). Keduanya tampak sama, berbau sama, dan hampir semua sifat kimianya sama, karena awan elektronnya identik. Tetapi D₂O mendidih pada 101,4 °C, membeku pada 3,8 °C, dan bila diminum dalam jumlah besar mengganggu pembelahan sel. Reaksi yang memutus ikatan O–D berjalan beberapa kali lebih lambat daripada yang memutus O–H. Spektrum inframerahnya bergeser: pita ulur O–H di sekitar 3400 cm⁻¹ pindah ke sekitar 2500 cm⁻¹. Mengapa satu neutron tambahan di inti, yang sama sekali tidak mengubah gaya-gaya listrik antara atom, mengubah begitu banyak hal?

Jawabannya terletak pada model yang paling penting untuk gerak inti dalam molekul: **osilator harmonik kuantum**. Ikatan kimia, di dekat panjang setimbangnya, berperilaku seperti pegas. Pegas kuantum tidak pernah diam; ia selalu mempunyai energi titik nol $\tfrac12h\nu$, dan frekuensi $\nu$ bergantung pada massa. Atom yang lebih berat bergetar lebih lambat, sehingga energi titik nolnya lebih kecil dan ikatannya "lebih dalam" di dasar sumur energi. Hampir seluruh efek isotop dalam kimia berawal dari sini (subbab 5.10).

Osilator harmonik juga satu dari sedikit sistem yang dapat diselesaikan secara tepat, dan penyelesaiannya indah: tingkat energinya berjarak sama, fungsi gelombangnya adalah polinom Hermite dikali fungsi Gauss, dan seluruh spektrumnya dapat diturunkan dengan aljabar operator tanpa menyelesaikan persamaan diferensial apa pun. Dari model ini kita akan sampai ke spektroskopi inframerah, potensial Morse, efek isotop, mode normal molekul poliatom, dan metode numerik untuk menyelesaikan persamaan Schrödinger dengan potensial apa pun.

::: {.strategi}
**Pertanyaan pembuka**

1. Mengapa hampir setiap ikatan kimia, di dekat panjang setimbangnya, dapat dimodelkan sebagai pegas?
2. Mengapa tingkat energi getaran berjarak sama, dan mengapa energi terendahnya tidak nol?
3. Mengapa N₂ dan O₂ tidak menyerap inframerah, tetapi CO₂ dan H₂O menyerap?
4. Mengapa nada atas getaran molekul tidak tepat dua kali frekuensi dasar, dan bagaimana kita menaksir energi disosiasi dari spektrum inframerah?
5. Mengapa ikatan C–D lebih sulit diputus daripada ikatan C–H?
:::

::: {.tujuan}
**Tujuan belajar**

Setelah mempelajari bab ini, kamu mampu:

1. Menganalisis osilator harmonik klasik dan memakai massa tereduksi untuk dua benda.
2. Menuliskan persamaan Schrödinger osilator dan mengubahnya ke bentuk tak berdimensi.
3. Menyelesaikannya dengan deret pangkat dan memakai sifat-sifat polinom Hermite.
4. Menghitung tingkat energi, energi titik nol, dan populasi termal tingkat getaran.
5. Membandingkan rapat peluang kuantum dan klasik, termasuk penembusan ke daerah terlarang.
6. Memakai operator tangga untuk menurunkan spektrum dan menghitung unsur matriks.
7. Menghitung tetapan gaya dan frekuensi getaran molekul diatom dari data spektroskopi.
8. Menurunkan aturan seleksi inframerah dan menentukan mode yang aktif IR.
9. Memakai potensial Morse dan anharmonisitas untuk menganalisis nada atas dan menaksir energi disosiasi.
10. Menghitung efek isotop pada frekuensi, energi titik nol, energi disosiasi, dan laju reaksi.
11. Menentukan banyaknya mode normal dan menganalisis mode normal molekul kecil.
12. Menyelesaikan persamaan Schrödinger satu dimensi secara numerik dengan metode Numerov.
:::

::: {.mat}
**Prasyarat**

Dari Bab 1: energi titik nol dan kapasitas kalor getaran (subbab 1.3 dan 1.9). Dari Bab 2: integral Gauss (2.2), deret pangkat dan persamaan Hermite (2.4), deret Taylor dan hampiran harmonik (2.9), nilai eigen matriks (2.8). Dari Bab 3: persamaan Schrödinger dan sumur terhingga (3.4, 3.9), penerobosan (3.11). Dari Bab 4: operator, komutator, nilai harap, paritas, representasi matriks.
:::

## 5.1 Osilator klasik

### Hukum Hooke dan gerak harmonik

Partikel bermassa $m$ yang ditarik ke posisi setimbang oleh gaya sebanding simpangan, $F = -kx$, mematuhi $m\ddot x = -kx$. Penyelesaiannya (subbab 2.3) adalah gerak harmonik

$$
x(t) = A\cos(\omega t + \varphi), \qquad \omega = \sqrt{\frac km}, \qquad \nu = \frac{\omega}{2\pi} . \qquad \text{(5.1)}
$$

Frekuensinya tidak bergantung pada amplitudo, sifat yang membuat jam pendulum dan garputala berguna. Energi potensialnya $V = \tfrac12kx^2$, dan energi totalnya

$$
E = \tfrac12m\dot x^2 + \tfrac12kx^2 = \tfrac12kA^2 , \qquad \text{(5.2)}
$$

yang dapat bernilai berapa saja, termasuk nol (partikel diam di dasar). Partikel berbalik arah di **titik balik** $x = \pm A$, tempat seluruh energinya potensial.

### Mengapa ikatan seperti pegas

Kurva energi potensial molekul diatom $V(r)$ mempunyai minimum di panjang setimbang $r_e$. Deret Taylor di sekitar minimum (subbab 2.9) memberikan

$$
V(r) = V(r_e) + \tfrac12k(r - r_e)^2 + \cdots, \qquad k = \left(\frac{d^2V}{dr^2}\right)_{r_e} , \qquad \text{(5.3)}
$$

karena turunan pertama nol di minimum. Apa pun bentuk persis kurvanya, untuk simpangan yang cukup kecil ikatan berperilaku seperti pegas dengan **tetapan gaya** $k$. Untuk getaran molekul pada tingkat-tingkat rendah, simpangannya beberapa persen panjang ikatan, sehingga hampiran harmonik cukup baik. Suku-suku berikutnya (anharmonisitas) dibahas di subbab 5.9.

### Dua benda dan massa tereduksi

Dalam molekul diatom kedua atom bergerak. Untuk dua massa $m_1$ dan $m_2$ yang dihubungkan pegas, gerak pusat massa terpisah dari gerak relatif, dan gerak relatif (perubahan panjang ikatan $x = r - r_e$) berperilaku seperti satu partikel bermassa **massa tereduksi**

$$
\mu = \frac{m_1m_2}{m_1 + m_2} . \qquad \text{(5.4)}
$$

Frekuensi getarannya $\omega = \sqrt{k/\mu}$. Jika satu atom jauh lebih berat, $\mu$ mendekati massa atom yang ringan: dalam HCl, $\mu = 0{,}980$ u, hampir massa atom H. Getaran HCl pada dasarnya adalah atom H yang bergoyang terhadap atom Cl yang hampir diam. Pemisahan gerak dua benda dibahas secara lengkap di Bab 6.

### Rapat peluang klasik

Jika kita memotret osilator klasik pada saat acak, di mana kemungkinan besar ia berada? Partikel bergerak lambat di dekat titik balik dan cepat di tengah, sehingga lebih lama berada di dekat titik balik. Peluang menemukannya dalam $dx$ sebanding dengan waktu yang dihabiskan di sana, $dt = dx/|v|$. Dengan $v = \omega\sqrt{A^2 - x^2}$ dan normalisasi atas setengah periode $\pi/\omega$:

$$
P_\text{klasik}(x) = \frac{1}{\pi\sqrt{A^2 - x^2}}, \qquad |x| < A . \qquad \text{(5.5)}
$$

Rapat ini terbesar (bahkan tak hingga, tetapi terintegralkan) di titik balik, dan nol di luar $|x| > A$. Kita akan membandingkannya dengan rapat peluang kuantum di subbab 5.5.

::: {.contoh}
**Contoh 5.1 · Pegas HCl**

Tetapan gaya ikatan H–³⁵Cl adalah 516 N/m. (a) Hitung massa tereduksi (massa atom 1,00783 u dan 34,96885 u). (b) Hitung frekuensi getaran klasik $\nu$, bilangan gelombang $\tilde\nu = \nu/c$, dan periodenya.

**Penyelesaian.** (a) $\mu = \dfrac{(1{,}00783)(34{,}96885)}{35{,}97668} = 0{,}97959$ u $= 1{,}6266 \times 10^{-27}$ kg.

(b) $\omega = \sqrt{516/1{,}6266 \times 10^{-27}} = 5{,}632 \times 10^{14}$ s⁻¹, $\nu = 8{,}96 \times 10^{13}$ Hz, $\tilde\nu = \nu/c = 2990$ cm⁻¹. Periode $1/\nu = 11{,}2$ fs.

**Memahami hasil.** Ikatan H–Cl bergetar hampir $10^{14}$ kali tiap detik, dengan frekuensi di daerah inframerah tengah. Nilai 2990 cm⁻¹ ini adalah bilangan gelombang harmonik $\omega_e$; serapan IR yang teramati, 2886 cm⁻¹, sedikit lebih rendah karena anharmonisitas (subbab 5.9).
:::

::: {.contoh}
**Contoh 5.2 · Massa tereduksi berbagai molekul**

Hitung massa tereduksi (dalam u) untuk H₂, HF, HI, CO, dan I₂. Apa polanya?

**Penyelesaian.** H₂: $1{,}0078^2/2{,}0157 = 0{,}504$. HF: $(1{,}0078)(18{,}998)/20{,}006 = 0{,}957$. HI: $(1{,}0078)(126{,}904)/127{,}912 = 1{,}000$. CO: $(12{,}000)(15{,}995)/27{,}995 = 6{,}856$. I₂: $126{,}904/2 = 63{,}45$.

**Memahami hasil.** Untuk semua hidrida, $\mu \approx 1$ u, karena atom H jauh lebih ringan; untuk molekul homonuklir, $\mu$ setengah massa atom. Massa tereduksi hidrida yang kecil menjelaskan mengapa getaran X–H selalu berfrekuensi tinggi (2000–4000 cm⁻¹), sehingga mudah dikenali dalam spektrum IR sebagai pita-pita terpisah dari "sidik jari" getaran kerangka.
:::

::: {.contoh}
**Contoh 5.3 · Amplitudo klasik dan rapat peluang**

Seandainya HCl berperilaku klasik dengan energi getaran sama dengan energi titik nol kuantumnya, $\tfrac12h\nu$, (a) berapa amplitudonya? (b) Berapa peluang klasik menemukan simpangan dalam $|x| < A/2$?

**Penyelesaian.** (a) Dengan $\tilde\nu = 2991$ cm⁻¹, $E = \tfrac12hc\tilde\nu = 2{,}97 \times 10^{-20}$ J. $A = \sqrt{2E/k} = \sqrt{2(2{,}97 \times 10^{-20})/516} = 1{,}07 \times 10^{-11}$ m $= 10{,}7$ pm, sama dengan $\sqrt{\hbar/\mu\omega}$.

(b) $\int_{-A/2}^{A/2}\dfrac{dx}{\pi\sqrt{A^2 - x^2}} = \dfrac{2}{\pi}\arcsin\dfrac12 = \dfrac13$.

**Memahami hasil.** Simpangan sekitar 10 pm, kira-kira 8% panjang ikatan (127 pm), membenarkan hampiran harmonik untuk tingkat dasar. Osilator klasik hanya menghabiskan sepertiga waktunya di separuh tengah lintasan; osilator kuantum pada keadaan dasar justru paling sering berada di tengah (subbab 5.5).
:::

::: {.kuis}
**Kuis cepat 5.1**

Jika massa kedua atom dalam molekul homonuklir dilipatduakan dan tetapan gayanya tetap, apa yang terjadi pada frekuensi getaran?
:::

## 5.2 Persamaan Schrödinger osilator

### Bentuk persamaan

Dengan $V = \tfrac12kx^2 = \tfrac12\mu\omega^2x^2$, persamaan Schrödinger tak bergantung waktu untuk gerak relatif adalah

$$
-\frac{\hbar^2}{2\mu}\frac{d^2\psi}{dx^2} + \frac12\mu\omega^2x^2\psi = E\psi . \qquad \text{(5.6)}
$$

Potensial ini naik tanpa batas di kedua sisi, sehingga semua keadaan terikat dan energinya diskret.

### Variabel tak berdimensi

Persamaan (5.6) memuat tiga tetapan, $\hbar$, $\mu$, $\omega$. Dari ketiganya hanya ada satu panjang, $\sqrt{\hbar/\mu\omega}$, dan satu energi, $\hbar\omega$. Ini mengusulkan perubahan variabel

$$
\xi = \sqrt\alpha\,x, \qquad \alpha = \frac{\mu\omega}{\hbar}, \qquad \varepsilon = \frac{2E}{\hbar\omega} . \qquad \text{(5.7)}
$$

Dengan $d^2/dx^2 = \alpha\,d^2/d\xi^2$, kalikan (5.6) dengan $2/\hbar\omega$:

$$
\frac{d^2\psi}{d\xi^2} + \left(\varepsilon - \xi^2\right)\psi = 0 . \qquad \text{(5.8)}
$$

Semua osilator harmonik, dari ikatan H–H sampai getaran kisi kristal, mematuhi persamaan tak berdimensi yang sama; perbedaan di antara mereka hanya pada skala panjang $1/\sqrt\alpha$ dan skala energi $\hbar\omega$.

### Perilaku asimtotik

Untuk $|\xi|$ besar, $\xi^2$ jauh lebih besar daripada $\varepsilon$, dan (5.8) menjadi $\psi'' \approx \xi^2\psi$. Coba $\psi = e^{\pm\xi^2/2}$: turunan keduanya $(\xi^2 \pm 1)e^{\pm\xi^2/2} \approx \xi^2e^{\pm\xi^2/2}$. Pilihan $e^{+\xi^2/2}$ meledak dan tidak dapat dinormalisasi, jadi perilaku yang diterima adalah $e^{-\xi^2/2}$. Ini mengusulkan bentuk

$$
\psi(\xi) = H(\xi)\,e^{-\xi^2/2} , \qquad \text{(5.9)}
$$

dengan $H(\xi)$ fungsi yang tumbuh lebih lambat dari $e^{\xi^2/2}$. Masukkan ke (5.8). Dengan $\psi' = (H' - \xi H)e^{-\xi^2/2}$ dan $\psi'' = (H'' - 2\xi H' - H + \xi^2H)e^{-\xi^2/2}$:

$$
H'' - 2\xi H' + (\varepsilon - 1)H = 0 . \qquad \text{(5.10)}
$$

Inilah **persamaan Hermite** (persamaan 2.18 di Bab 2) dengan $2\nu = \varepsilon - 1$.

::: {.contoh}
**Contoh 5.4 · Memeriksa keadaan dasar**

Tunjukkan bahwa $\psi_0 = e^{-\xi^2/2}$ memenuhi (5.8) dan tentukan energinya.

**Penyelesaian.** $\psi_0'' = (\xi^2 - 1)e^{-\xi^2/2}$. Masukkan: $(\xi^2 - 1) + (\varepsilon - \xi^2) = 0$ menuntut $\varepsilon = 1$, yaitu $E_0 = \tfrac12\hbar\omega$.

**Memahami hasil.** Suku $\xi^2$ dari energi kinetik meniadakan suku $\xi^2$ dari energi potensial; yang tersisa adalah tetapan, energi titik nol. Pola ini sama dengan atom hidrogen, tempat suku $1/r$ meniadakan (Contoh 2.53 di Bab 2). Fungsi Gauss adalah satu-satunya fungsi yang "pas" dengan potensial kuadrat.
:::

::: {.contoh}
**Contoh 5.5 · Skala panjang dan energi**

Hitung $1/\sqrt\alpha$ (dalam pm) dan $\hbar\omega$ (dalam eV dan cm⁻¹) untuk H₂ ($\tilde\nu = 4401$ cm⁻¹, $\mu = 0{,}504$ u) dan I₂ ($\tilde\nu = 214{,}5$ cm⁻¹, $\mu = 63{,}45$ u).

**Penyelesaian.** $\hbar\omega = hc\tilde\nu$: H₂ 0,546 eV; I₂ 0,0266 eV. Dalam cm⁻¹, sama dengan $\tilde\nu$. Panjang $1/\sqrt\alpha = \sqrt{\hbar/\mu\omega}$: H₂ $\sqrt{1{,}0546 \times 10^{-34}/(8{,}368 \times 10^{-28} \times 8{,}291 \times 10^{14})} = 12{,}3$ pm; I₂ 4,9 pm.

**Memahami hasil.** Getaran I₂ jauh lebih "lembut" (energi kuantum dua puluh kali lebih kecil, dan sebanding dengan $kT$) tetapi amplitudo titik nolnya lebih kecil karena atomnya berat. Kedua skala ini, $\hbar\omega$ dan $1/\sqrt\alpha$, adalah satuan alami setiap soal osilator.
:::

::: {.contoh}
**Contoh 5.6 · Osilator dalam medan listrik**

Ikatan bermuatan parsial $\pm q$ ditempatkan dalam medan listrik seragam $\mathcal E$ searah ikatan, sehingga $V = \tfrac12kx^2 - q\mathcal Ex$. Tentukan tingkat energinya. Hitung pergeseran posisi setimbang dan energi untuk HCl ($k = 516$ N/m, $q \approx 0{,}18e$) dalam medan $10^9$ V/m (sekitar medan di dekat ion dalam larutan).

**Penyelesaian.** Lengkapkan kuadrat: $V = \tfrac12k(x - x_0)^2 - \tfrac{q^2\mathcal E^2}{2k}$ dengan $x_0 = q\mathcal E/k$. Potensialnya adalah parabola yang sama, hanya tergeser. Dengan $y = x - x_0$, persamaan Schrödinger kembali ke (5.6), sehingga $E_v = (v + \tfrac12)\hbar\omega - q^2\mathcal E^2/2k$. Untuk HCl: $x_0 = (0{,}18)(1{,}602 \times 10^{-19})(10^9)/516 = 5{,}6 \times 10^{-14}$ m $= 0{,}056$ pm, dan pergeseran energi $-8{,}1 \times 10^{-25}$ J $= -0{,}041$ cm⁻¹.

**Memahami hasil.** Semua tingkat turun sama banyak, sehingga dalam model harmonik **frekuensi getaran tidak berubah** oleh medan. Pergeseran frekuensi yang teramati dalam medan listrik (efek Stark getaran, dipakai untuk mengukur medan listrik di situs aktif enzim dengan sonde C=O atau C≡N) berasal dari anharmonisitas (subbab 5.9): pada potensial yang tidak simetris, ikatan yang tergeser merasakan kelengkungan yang berbeda.
:::

::: {.kuis}
**Kuis cepat 5.2**

Mengapa $e^{+\xi^2/2}$ ditolak sebagai perilaku asimtotik, padahal ia juga memenuhi persamaan asimtotik?
:::

## 5.3 Penyelesaian deret dan polinom Hermite

### Rekursi dan kuantisasi

Persamaan (5.10) diselesaikan dengan deret pangkat, persis seperti di subbab 2.4. Dengan $H = \sum a_k\xi^k$, rekursinya

$$
a_{k+2} = \frac{2k + 1 - \varepsilon}{(k + 1)(k + 2)}\,a_k . \qquad \text{(5.11)}
$$

Untuk $k$ besar, $a_{k+2}/a_k \to 2/k$, sehingga deret yang tidak berhenti tumbuh seperti $e^{\xi^2}$, dan $\psi = He^{-\xi^2/2}$ meledak seperti $e^{\xi^2/2}$ (Contoh 2.19 di Bab 2). Satu-satunya jalan agar $\psi$ dapat dinormalisasi adalah deret berhenti: pembilang (5.11) harus nol untuk suatu $k = v$, yaitu $\varepsilon = 2v + 1$, dan deret yang lain (genap atau ganjil) dibuang. Dengan (5.7):

$$
\boxed{\ E_v = \left(v + \tfrac12\right)\hbar\omega = \left(v + \tfrac12\right)h\nu, \qquad v = 0, 1, 2, \ldots\ } \qquad \text{(5.12)}
$$

Bilangan bulat $v$ disebut **bilangan kuantum getaran**.

### Polinom Hermite

Polinom yang dihasilkan, dengan normalisasi baku (koefisien pangkat tertinggi $2^v$), adalah **polinom Hermite**:

$$
H_0 = 1, \quad H_1 = 2\xi, \quad H_2 = 4\xi^2 - 2, \quad H_3 = 8\xi^3 - 12\xi, \quad H_4 = 16\xi^4 - 48\xi^2 + 12 .
$$

Sifat-sifat yang berguna:

- **Rekursi**: $H_{v+1} = 2\xi H_v - 2vH_{v-1}$. Ini cara tercepat membangkitkan polinom berderajat tinggi.
- **Turunan**: $H_v' = 2vH_{v-1}$.
- **Rumus Rodrigues**: $H_v(\xi) = (-1)^ve^{\xi^2}\dfrac{d^v}{d\xi^v}e^{-\xi^2}$.
- **Paritas**: $H_v(-\xi) = (-1)^vH_v(\xi)$.
- **Ortogonalitas**: $\int_{-\infty}^\infty H_mH_ne^{-\xi^2}d\xi = \sqrt\pi\,2^nn!\,\delta_{mn}$.

### Fungsi gelombang ternormalisasi

Dengan ortogonalitas di atas, fungsi gelombang ternormalisasi dalam variabel $x$ adalah

$$
\psi_v(x) = N_vH_v\left(\sqrt\alpha\,x\right)e^{-\alpha x^2/2}, \qquad N_v = \left(\frac\alpha\pi\right)^{1/4}\frac{1}{\sqrt{2^vv!}} . \qquad \text{(5.13)}
$$

Gambar 5.1 memperlihatkan lima keadaan terendah.

![Gambar 5.1 Osilator harmonik. Kiri: fungsi gelombang lima keadaan terendah, masing-masing digambar pada ketinggian energinya di dalam potensial parabola. Kanan: rapat peluang. Garis putus-putus menandai energi; ujung-ujungnya adalah titik balik klasik. Tingkat-tingkat berjarak sama, $\hbar\omega$.](fig/c_osilator.png){width=90%}

::: {.contoh}
**Contoh 5.7 · Rekursi Hermite**

Dengan $H_{v+1} = 2\xi H_v - 2vH_{v-1}$, hitung $H_5$ dan $H_6$ dari $H_3$ dan $H_4$.

**Penyelesaian.** $H_5 = 2\xi H_4 - 8H_3 = 32\xi^5 - 96\xi^3 + 24\xi - 64\xi^3 + 96\xi = 32\xi^5 - 160\xi^3 + 120\xi$.

$H_6 = 2\xi H_5 - 10H_4 = 64\xi^6 - 320\xi^4 + 240\xi^2 - 160\xi^4 + 480\xi^2 - 120 = 64\xi^6 - 480\xi^4 + 720\xi^2 - 120$.

**Memahami hasil.** $H_5$ cocok dengan hasil dari rekursi deret pangkat (Soal di Bab 2). Rekursi tiga suku jauh lebih efisien daripada rumus Rodrigues, dan juga stabil secara numerik; program komputer membangkitkan fungsi gelombang osilator dengan cara ini.
:::

::: {.contoh}
**Contoh 5.8 · Normalisasi $\psi_1$**

Tunjukkan bahwa $\psi_1 = N_1(2\sqrt\alpha\,x)e^{-\alpha x^2/2}$ dengan $N_1 = (\alpha/\pi)^{1/4}/\sqrt2$ ternormalisasi.

**Penyelesaian.** $\int\psi_1^2dx = N_1^2\cdot 4\alpha\int x^2e^{-\alpha x^2}dx = N_1^2\cdot 4\alpha\cdot\dfrac{1}{2\alpha}\sqrt{\dfrac\pi\alpha} = 2N_1^2\sqrt{\dfrac\pi\alpha}$. Dengan $N_1^2 = \tfrac12\sqrt{\alpha/\pi}$, hasilnya 1.

**Memahami hasil.** Integral Gauss $\int x^2e^{-\alpha x^2} = \tfrac{1}{2\alpha}\sqrt{\pi/\alpha}$ (subbab 2.2) adalah satu-satunya alat yang diperlukan. Semua integral osilator harmonik dapat dihitung dengan integral Gauss, tetapi operator tangga (subbab 5.6) jauh lebih cepat.
:::

::: {.contoh}
**Contoh 5.9 · Ortogonalitas $\psi_0$ dan $\psi_2$**

Periksa bahwa $\int\psi_0\psi_2\,dx = 0$.

**Penyelesaian.** Dalam variabel $\xi$: $\int(4\xi^2 - 2)e^{-\xi^2}d\xi = 4\cdot\dfrac{\sqrt\pi}{2} - 2\sqrt\pi = 0$.

**Memahami hasil.** $\psi_0$ dan $\psi_2$ sama-sama genap, jadi ortogonalitasnya tidak berasal dari paritas, melainkan dari teorema operator Hermitian (subbab 4.8): fungsi eigen $\hat H$ dengan energi berbeda pasti ortogonal. $\psi_0$ dan $\psi_1$ ortogonal karena dua alasan sekaligus.
:::

::: {.kuis}
**Kuis cepat 5.3**

Berapa banyak simpul $\psi_7$? Apakah $\psi_7$ genap atau ganjil?
:::
