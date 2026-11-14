## 11.3 Ion molekul hidrogen H₂⁺

### Molekul paling sederhana

Ion H₂⁺ terdiri atas dua proton dan satu elektron. Ion ini terbentuk ketika H₂ diionisasi (dalam lucutan gas, di atmosfer atas, dan di ruang antarbintang, tempat ia menjadi bahan awal pembentukan H₃⁺), dan energi ikatnya, 2,65 eV, adalah lebih dari separuh energi ikat H₂ meskipun elektronnya hanya satu. Bagi teori, H₂⁺ adalah molekul yang sama pentingnya dengan atom hidrogen bagi teori atom: karena tidak ada tolakan antarelektron, persamaan Schrödingernya (dengan inti diam) dapat diselesaikan secara eksak. Setiap gagasan tentang orbital molekul, ikatan dan antiikatan, σ dan π, dapat diuji di sini terhadap jawaban yang benar.

Letakkan proton $A$ dan $B$ pada sumbu $z$ dengan jarak $R$, dan sebut jarak elektron ke masing-masing proton $r_A$ dan $r_B$ (Gambar 11.1). Dalam satuan atom, Hamiltonian elektronik (11.2) adalah

$$
\hat H_\text{el} = -\frac12\nabla^2 - \frac{1}{r_A} - \frac{1}{r_B} + \frac1R . \qquad \text{(11.6)}
$$

Suku $1/R$ hanyalah tetapan untuk setiap $R$; ia menggeser energi tetapi tidak mengubah fungsi gelombang.

![Gambar 11.1 Koordinat ion H₂⁺. Kiri: proton $A$ dan $B$ pada sumbu $z$ berjarak $R$; elektron berjarak $r_A$ dan $r_B$ dari keduanya. Kanan: koordinat eliptik. Garis biru adalah elips dengan $\lambda = (r_A + r_B)/R$ tetap (fokus di kedua inti), garis jingga adalah hiperbola dengan $\mu = (r_A - r_B)/R$ tetap.](fig/c_koordinat.png){width=92%}

### Simetri dan bilangan kuantum

Potensial $-1/r_A - 1/r_B$ tidak bersimetri bola, sehingga $\hat L^2$ tidak lagi komut dengan $\hat H$ dan bilangan kuantum $\ell$ hilang. Namun potensial itu tidak berubah oleh putaran terhadap sumbu molekul, sehingga $\hat L_z$ komut dengan $\hat H$, dan fungsi gelombang dapat dipilih berbentuk $e^{im\phi}$ dengan $m = 0, \pm1, \pm2, \ldots$ Energi hanya bergantung pada $|m|$, karena pencerminan pada bidang yang memuat sumbu mengubah $m$ menjadi $-m$. Bilangan kuantum $\lambda = |m|$ memberi nama pada orbital molekul, dengan huruf Yunani yang meniru s, p, d atom:

| $\lambda = \lvert m\rvert$ | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Lambang | σ | π | δ | φ |
| Degenerasi | 1 | 2 | 2 | 2 |

Molekul homonuklir juga mempunyai pusat inversi di titik tengah antarinti, sehingga setiap orbital bersifat *gerade* ($g$) atau *ungerade* ($u$). Dalam bahasa Bab 10, grup titiknya $D_{\infty h}$, dan σ$_g$, σ$_u$, π$_u$, π$_g$ adalah irrep-irrepnya (dengan huruf kecil untuk orbital).

### Penyelesaian eksak dalam koordinat eliptik

Pada 1927, Øyvind Burrau menyelesaikan H₂⁺ secara numerik dengan memakai **koordinat eliptik** (sferoidal prolat):

$$
\lambda = \frac{r_A + r_B}{R}, \qquad \mu = \frac{r_A - r_B}{R}, \qquad \phi , \qquad \text{(11.7)}
$$

dengan $1 \le \lambda < \infty$, $-1 \le \mu \le 1$, dan $\phi$ sudut putar terhadap sumbu molekul. Permukaan $\lambda$ tetap adalah elipsoid dengan fokus di kedua inti, dan permukaan $\mu$ tetap adalah hiperboloid. Elemen volumenya

$$
d\tau = \frac{R^3}{8}(\lambda^2 - \mu^2)\,d\lambda\,d\mu\,d\phi . \qquad \text{(11.8)}
$$

Keistimewaan koordinat ini adalah bahwa potensial elektron–inti menjadi sederhana: $1/r_A + 1/r_B = (r_A + r_B)/(r_Ar_B)$, dan karena $r_Ar_B = R^2(\lambda^2 - \mu^2)/4$, maka $1/r_A + 1/r_B = 4\lambda/[R(\lambda^2 - \mu^2)]$. Penyebut $\lambda^2 - \mu^2$ yang sama juga muncul dalam Laplasian, sehingga persamaan Schrödinger dapat dikalikan dengannya dan dipisahkan. Dengan $\psi = \Lambda(\lambda)M(\mu)e^{im\phi}$ dan $p^2 = -R^2E_\text{el}/2$ (dengan $E_\text{el}$ energi tanpa suku $1/R$), diperoleh dua persamaan diferensial biasa:

$$
\frac{d}{d\lambda}\left[(\lambda^2 - 1)\frac{d\Lambda}{d\lambda}\right] + \left[A + 2R\lambda - p^2\lambda^2 - \frac{m^2}{\lambda^2 - 1}\right]\Lambda = 0 , \qquad \text{(11.9)}
$$

$$
\frac{d}{d\mu}\left[(1 - \mu^2)\frac{dM}{d\mu}\right] + \left[-A + p^2\mu^2 - \frac{m^2}{1 - \mu^2}\right]M = 0 , \qquad \text{(11.10)}
$$

dengan $A$ tetapan pemisahan. Persamaan untuk $\mu$ mirip persamaan Legendre (subbab 6.4) dengan suku tambahan $p^2\mu^2$; persamaan untuk $\lambda$ mirip persamaan radial atom hidrogen. Keduanya harus dipenuhi oleh pasangan $(A, p)$ yang sama, dan syarat fungsi berperilaku baik (berhingga di $\mu = \pm1$ dan $\lambda = 1$, menuju nol di $\lambda \to \infty$) hanya dapat dipenuhi untuk nilai-nilai $p$ tertentu: energinya terkuantisasi. Penyelesaiannya tidak dapat ditulis dalam fungsi elementer, tetapi dapat dihitung dengan ketelitian sebarang.

::: {.dalam}
**Lebih dalam · Pemisahan variabel dalam koordinat eliptik**

Dalam koordinat (11.7), Laplasian adalah

$$
\nabla^2 = \frac{4}{R^2(\lambda^2 - \mu^2)}\left[\frac{\partial}{\partial\lambda}(\lambda^2 - 1)\frac{\partial}{\partial\lambda} + \frac{\partial}{\partial\mu}(1 - \mu^2)\frac{\partial}{\partial\mu} + \frac{\lambda^2 - \mu^2}{(\lambda^2 - 1)(1 - \mu^2)}\frac{\partial^2}{\partial\phi^2}\right] .
$$

Tulis persamaan Schrödinger sebagai $\nabla^2\psi = 2(V - E_\text{el})\psi$ dengan $V = -4\lambda/[R(\lambda^2 - \mu^2)]$, lalu kalikan kedua ruas dengan $R^2(\lambda^2 - \mu^2)/4$:

$$
\left[\partial_\lambda(\lambda^2 - 1)\partial_\lambda + \partial_\mu(1 - \mu^2)\partial_\mu - \frac{m^2}{\lambda^2 - 1} - \frac{m^2}{1 - \mu^2}\right]\psi = \left[-2R\lambda + p^2(\lambda^2 - \mu^2)\right]\psi .
$$

Di sini $\partial_\phi^2 \to -m^2$ dan dipakai identitas $(\lambda^2 - \mu^2)/[(\lambda^2 - 1)(1 - \mu^2)] = 1/(1 - \mu^2) + 1/(\lambda^2 - 1)$. Semua suku kini terpisah menjadi bagian yang hanya bergantung pada $\lambda$ dan bagian yang hanya bergantung pada $\mu$. Masukkan $\psi = \Lambda M$, bagi dengan $\Lambda M$, dan samakan masing-masing bagian dengan tetapan $\mp A$: diperoleh (11.9) dan (11.10). Pemisahan ini berhasil hanya karena satu elektron; tolakan $1/r_{12}$ dalam H₂ merusaknya.
:::

::: {.contoh}
**Contoh 11.8 · Titik-titik istimewa dalam koordinat eliptik**

Tentukan $(\lambda, \mu)$ untuk (a) inti $A$, (b) inti $B$, (c) titik tengah antarinti, (d) titik pada sumbu di belakang $A$ sejauh $R/2$ dari $A$, dan (e) titik yang sangat jauh.

**Penyelesaian.** (a) $r_A = 0$, $r_B = R$: $\lambda = 1$, $\mu = -1$. (b) $\lambda = 1$, $\mu = 1$. (c) $r_A = r_B = R/2$: $\lambda = 1$, $\mu = 0$. (d) $r_A = R/2$, $r_B = 3R/2$: $\lambda = 2$, $\mu = -1$. (e) $r_A \approx r_B \approx r \to \infty$: $\lambda \approx 2r/R \to \infty$, $\mu \to \cos\theta$, dengan $\theta$ sudut terhadap sumbu.

**Memahami hasil.** Seluruh ruas garis antarinti mempunyai $\lambda = 1$; elipsoid $\lambda$ tetap mengecil menjadi ruas garis itu. Jauh dari molekul, $\lambda$ berperan seperti jarak radial dan $\mu$ seperti $\cos\theta$ dalam koordinat bola, sehingga fungsi gelombang molekul berubah mulus menjadi bentuk atom. (Pada butir (a) dan (b) tanda $\mu$ bergantung pada kesepakatan; di sini $\mu = (r_A - r_B)/R$.)
:::

::: {.contoh}
**Contoh 11.9 · Menyelesaikan H₂⁺ dengan Python**

Persamaan (11.10) untuk $M(\mu)$ dapat diselesaikan dengan menguraikan $M$ atas polinom Legendre, sehingga $A$ menjadi nilai eigen matriks. Persamaan (11.9) untuk $\Lambda(\lambda)$ diintegrasikan dari $\lambda = 1$ ke luar, dan $p$ disesuaikan sampai $\Lambda$ meluruh di tak hingga (metode tembak, seperti subbab 5.12). Tuliskan programnya untuk keadaan dasar ($m = 0$, $M$ genap) dan hitung energi pada $R = 2{,}00$ bohr.

**Penyelesaian.**

```python
import numpy as np
from scipy.special import eval_legendre
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
x, w = np.polynomial.legendre.leggauss(100)
def A_dari_p(p, nl=30):                    # M genap: l = 0, 2, 4, ...
    ls = range(0, 2 * nl, 2)
    P = np.array([np.sqrt(l + 0.5) * eval_legendre(l, x) for l in ls])
    Mat = (P * w * x**2) @ P.T * p**2 - np.diag([l * (l + 1) for l in ls])
    return np.linalg.eigvalsh(Mat).max()   # nilai eigen terbesar = keadaan terendah
def ujung(p, R):
    A = A_dari_p(p); lmax = 1 + 40 / p
    f = lambda l, y: [y[1], (-(A + 2*R*l - p*p*l*l) * y[0] - 2*l*y[1]) / (l*l - 1)]
    l0 = 1 + 1e-7
    s = solve_ivp(f, [l0, lmax], [1.0, -(A + 2*R - p*p) / 2], rtol=1e-11, atol=1e-14)
    return s.y[0, -1] * np.exp(-p * lmax)
R = 2.0
p = brentq(lambda p: ujung(p, R), 1.3, 1.7)
E_el = -2 * p**2 / R**2
print(E_el, E_el + 1 / R)                  # -1.1026342  -0.6026342
```

**Memahami hasil.** Energi elektronik $-1{,}1026342$ hartree dan energi total $-0{,}6026342$ hartree cocok dengan nilai baku dalam literatur sampai semua angka yang ditampilkan. Syarat awal di $\lambda = 1$ diperoleh dari persamaan itu sendiri: koefisien turunan kedua lenyap di sana, sehingga fungsi yang berhingga harus memenuhi $2\Lambda'(1) = -(A + 2R - p^2)\Lambda(1)$. Dengan program yang sama untuk banyak nilai $R$, diperoleh kurva energi potensial eksak (Gambar 11.2).
:::

![Gambar 11.2 Kurva energi potensial H₂⁺. Garis tebal: penyelesaian eksak untuk keadaan $1\sigma_g$ (bawah) dan $1\sigma_u$ (atas). Garis putus-putus: LCAO dengan dua orbital 1s ($\zeta = 1$). Energi diukur relatif terhadap H(1s) + H⁺ ($-0{,}5$ hartree). LCAO menangkap ikatan secara kualitatif, tetapi jarak setimbangnya terlalu panjang dan sumurnya terlalu dangkal.](fig/c_kurva_h2p.png){width=82%}

Hasil eksak untuk keadaan dasar: jarak setimbang $R_e = 1{,}997$ bohr $= 105{,}7$ pm, energi total $-0{,}60263$ hartree, sehingga $D_e = 0{,}10263$ hartree $= 2{,}793$ eV. Setelah dikurangi energi titik nol getaran (0,14 eV), $D_0 = 2{,}65$ eV, cocok dengan nilai spektroskopi 2,651 eV. Keadaan tereksitasi pertama, $1\sigma_u$, tidak mempunyai minimum sama sekali: energinya lebih tinggi daripada H + H⁺ di setiap $R$, sehingga ion yang dieksitasi ke keadaan ini langsung terurai.

::: {.contoh}
**Contoh 11.10 · Energi ikat H₂⁺ dalam berbagai satuan**

Dari energi eksak di $R_e$, $E = -0{,}60263$ hartree, hitung $D_e$ dalam eV, kJ/mol, dan cm⁻¹. Bandingkan dengan $D_e$ H₂ (4,747 eV).

**Penyelesaian.** $D_e = -0{,}5 - (-0{,}60263) = 0{,}10263$ hartree. Dalam eV: $0{,}10263 \times 27{,}211 = 2{,}793$ eV; dalam kJ/mol: $\times 96{,}485 = 269{,}5$ kJ/mol; dalam cm⁻¹: $\times 8065{,}5 = 22\,526$ cm⁻¹.

**Memahami hasil.** Satu elektron menghasilkan 59% energi ikat yang dihasilkan dua elektron dalam H₂. Bila setiap elektron ikatan menyumbang sama besar, H₂ semestinya berenergi ikat $2 \times 2{,}79 = 5{,}59$ eV; kekurangan sekitar 0,84 eV adalah harga tolakan antarelektron. Ikatan H₂⁺ juga lebih panjang (106 pm dibandingkan 74 pm): satu elektron menarik kedua proton lebih lemah daripada dua elektron.
:::

::: {.contoh}
**Contoh 11.11 · Batas atom bersatu dan atom terpisah**

Apa energi elektronik $E_\text{el}$ keadaan dasar H₂⁺ untuk $R \to 0$ dan $R \to \infty$? Bagaimana dengan energi total?

**Penyelesaian.** Untuk $R \to 0$, kedua proton bersatu menjadi inti bermuatan $+2$: sistemnya ion He⁺, dengan $E_\text{el} = -Z^2/2 = -2$ hartree. Energi total $E_\text{el} + 1/R \to +\infty$ karena tolakan antarinti. Untuk $R \to \infty$, elektron berada di salah satu proton: $E_\text{el} = -0{,}5$ hartree (atom H), dan $1/R \to 0$, sehingga energi total $\to -0{,}5$ hartree.

**Memahami hasil.** Energi elektronik turun dari $-0{,}5$ ke $-2$ hartree ketika inti didekatkan, dan tolakan antarinti naik dari 0 ke tak hingga. Minimum energi total adalah kompromi keduanya. Gagasan menghubungkan atom bersatu dan atom terpisah dengan kurva yang mulus, sambil mempertahankan simetri setiap orbital, adalah dasar **diagram korelasi** di subbab 11.6.
:::

::: {.kuis}
**Kuis cepat 11.3**

\(a) Bilangan kuantum apa yang tetap berlaku dalam H₂⁺, dan mana yang hilang dibandingkan atom H? (b) Mengapa persamaan Schrödinger H₂ tidak dapat dipisahkan dalam koordinat eliptik? (c) Mengapa orbital π berdegenerasi dua, sedangkan σ tidak?
:::

## 11.4 LCAO untuk H₂⁺: integral tumpang tindih, Coulomb, pertukaran

### Fungsi uji

Penyelesaian eksak H₂⁺ tidak dapat diperluas ke molekul lain. Yang dapat diperluas adalah pendekatan yang dibangun dari bahan atom. Ketika elektron dekat proton $A$, ia "merasakan" terutama proton $A$, dan fungsi gelombangnya mestinya mirip orbital 1s atom H di $A$; demikian pula di dekat $B$. Fungsi uji paling sederhana yang memenuhi kedua batas itu adalah **kombinasi linear orbital atom** (LCAO):

$$
\psi = c_A\,1s_A + c_B\,1s_B, \qquad 1s_A = \frac{1}{\sqrt\pi}e^{-r_A}, \quad 1s_B = \frac{1}{\sqrt\pi}e^{-r_B} . \qquad \text{(11.11)}
$$

Menurut metode variasi linear (subbab 8.4), koefisien terbaik diperoleh dari persamaan sekuler $\det(\mathbf H - E\mathbf S) = 0$, persamaan (2.37), dengan

$$
S = \langle 1s_A|1s_B\rangle, \qquad H_{AA} = H_{BB} = \langle 1s_A|\hat H_\text{el}|1s_A\rangle, \qquad H_{AB} = \langle 1s_A|\hat H_\text{el}|1s_B\rangle .
$$

Karena kedua inti setara, $H_{AA} = H_{BB}$, dan persamaan sekuler 2 × 2 memberi dua akar, persis seperti (2.38):

$$
E_\pm = \frac{H_{AA} \pm H_{AB}}{1 \pm S}, \qquad \psi_\pm = \frac{1s_A \pm 1s_B}{\sqrt{2(1 \pm S)}} . \qquad \text{(11.12)}
$$

Hasil yang sama diperoleh tanpa persamaan sekuler, dari simetri: fungsi gelombang harus $g$ atau $u$ terhadap inversi, sehingga $c_A = \pm c_B$ (subbab 10.7).

### Tiga integral

Unsur matriks Hamiltonian dapat diuraikan menjadi bagian-bagian yang bermakna. Karena $1s_A$ adalah fungsi eigen Hamiltonian atom H di $A$, $(-\tfrac12\nabla^2 - 1/r_A)1s_A = E_{1s}1s_A$ dengan $E_{1s} = -\tfrac12$ hartree. Maka

$$
H_{AA} = E_{1s} + J + \frac1R, \qquad H_{AB} = \left(E_{1s} + \frac1R\right)S + K , \qquad \text{(11.13)}
$$

dengan

$$
J = \left\langle 1s_A\left|-\frac{1}{r_B}\right|1s_A\right\rangle, \qquad K = \left\langle 1s_A\left|-\frac{1}{r_A}\right|1s_B\right\rangle . \qquad \text{(11.14)}
$$

Masukkan ke (11.12):

$$
\boxed{\ E_\pm = E_{1s} + \frac1R + \frac{J \pm K}{1 \pm S}\ } \qquad \text{(11.15)}
$$

Ketiga integral dapat dihitung dalam bentuk tertutup dengan koordinat eliptik (kotak *Lebih dalam* di bawah):

$$
S = e^{-R}\left(1 + R + \frac{R^2}{3}\right), \qquad J = -\frac1R\left[1 - (1 + R)e^{-2R}\right], \qquad K = -(1 + R)e^{-R} . \qquad \text{(11.16)}
$$

Makna masing-masing:

- **Integral tumpang tindih** $S$ mengukur seberapa banyak kedua orbital menempati ruang yang sama. Nilainya 1 untuk $R = 0$ dan meluruh eksponensial untuk $R$ besar; di $R = 2$ bohr nilainya 0,59.
- **Integral Coulomb** $J$ adalah energi tarikan klasik antara awan elektron 1s di $A$ (kerapatan $|1s_A|^2$) dan proton $B$. Untuk $R$ besar, awan itu tampak seperti muatan titik, sehingga $J \to -1/R$. Bila jaraknya lebih kecil, sebagian awan berada di sisi jauh $B$ dan tarikan sedikit kurang dari $-1/R$.
- **Integral pertukaran** (atau **resonansi**) $K$ tidak mempunyai padanan klasik. Ia adalah tarikan proton $A$ pada "kerapatan tumpang tindih" $1s_A1s_B$, yang hanya ada karena elektron dapat berada di kedua atom sekaligus. $K$ negatif dan, seperti $S$, meluruh eksponensial.

::: {.dalam}
**Lebih dalam · Menghitung $S$, $J$, dan $K$**

*Tumpang tindih.* Dengan $r_A + r_B = R\lambda$ dan elemen volume (11.8):

$$
S = \frac1\pi\int e^{-(r_A + r_B)}\,d\tau = \frac{R^3}{8\pi}\int_0^{2\pi}d\phi\int_{-1}^1d\mu\int_1^\infty e^{-R\lambda}(\lambda^2 - \mu^2)\,d\lambda .
$$

Integral $\phi$ memberi $2\pi$. Integral $\mu$: $\int_{-1}^1(\lambda^2 - \mu^2)\,d\mu = 2\lambda^2 - \tfrac23$. Integral $\lambda$ memakai $\int_1^\infty\lambda^ne^{-R\lambda}d\lambda$: untuk $n = 0$, $e^{-R}/R$; untuk $n = 2$, $e^{-R}(1/R + 2/R^2 + 2/R^3)$. Maka

$$
S = \frac{R^3}{4}\left[2e^{-R}\left(\frac1R + \frac{2}{R^2} + \frac{2}{R^3}\right) - \frac23\cdot\frac{e^{-R}}{R}\right] = e^{-R}\left(1 + R + \frac{R^2}{3}\right) .
$$

*Pertukaran.* $K = -\tfrac1\pi\int e^{-r_A}e^{-r_B}/r_A\,d\tau$. Dengan $r_A = R(\lambda + \mu)/2$, faktor $(\lambda^2 - \mu^2)/r_A = 2(\lambda - \mu)/R$:

$$
K = -\frac{R^2}{4\pi}\cdot2\pi\int_1^\infty e^{-R\lambda}\int_{-1}^1(\lambda - \mu)\,d\mu\,d\lambda = -R^2\int_1^\infty\lambda e^{-R\lambda}d\lambda = -(1 + R)e^{-R} .
$$

*Coulomb.* $J = -\tfrac1\pi\int e^{-2r_A}/r_B\,d\tau$ paling mudah dihitung dengan teorema kulit dari elektrostatika: awan bola $|1s_A|^2$ menarik muatan di jarak $R$ seperti muatan titik sebesar bagian awan yang berada di dalam bola berjari-jari $R$, ditambah sumbangan kulit-kulit di luar $R$, masing-masing dengan potensial tetap $1/r$:

$$
J = -\frac1R\int_0^R4r^2\,e^{-2r}\,dr - \int_R^\infty\frac{4r^2e^{-2r}}{r}\,dr = -\frac1R\left[1 - (1 + R)e^{-2R}\right] .
$$
:::

### Hasilnya

Dengan (11.16), energi (11.15) dapat dihitung untuk setiap $R$. Kurva $E_+$ mempunyai minimum di $R_e = 2{,}49$ bohr (132 pm) dengan $D_e = 0{,}0648$ hartree $= 1{,}76$ eV; kurva $E_-$ selalu menolak (Gambar 11.2 dan 11.3). Dibandingkan dengan hasil eksak (106 pm, 2,79 eV), LCAO sederhana menangkap gejala utamanya, yaitu bahwa satu kombinasi mengikat dan yang lain tidak, tetapi meleset banyak secara kuantitatif.

![Gambar 11.3 Integral LCAO H₂⁺ sebagai fungsi jarak antarinti (satuan atom). Kiri: tumpang tindih $S$, integral Coulomb $J$, dan integral pertukaran $K$; garis titik-titik adalah $-1/R$. Kanan: sumbangan klasik $J + 1/R$ (selalu positif) dan sumbangan pertukaran terhadap energi ikat.](fig/c_integral.png){width=95%}

::: {.contoh}
**Contoh 11.12 · Menghitung integral di $R = 2$ bohr**

Hitung $S$, $J$, $K$, $E_+$, dan $E_-$ untuk $R = 2{,}00$ bohr, serta perubahan energinya terhadap H + H⁺ dalam eV.

**Penyelesaian.** $e^{-2} = 0{,}13534$, $e^{-4} = 0{,}018316$.

- $S = 0{,}13534(1 + 2 + 4/3) = 0{,}5865$;
- $J = -\tfrac12[1 - 3(0{,}018316)] = -0{,}4725$;
- $K = -3(0{,}13534) = -0{,}4060$.

Dengan (11.15): $E_+ = -0{,}5 + 0{,}5 + (-0{,}4725 - 0{,}4060)/1{,}5865 = -0{,}5538$ hartree; $E_- = -0{,}5 + 0{,}5 + (-0{,}4725 + 0{,}4060)/0{,}4135 = -0{,}1608$ hartree. Relatif terhadap $-0{,}5$ hartree: $E_+$ lebih rendah 1,46 eV, $E_-$ lebih tinggi 9,23 eV.

**Memahami hasil.** Orbital antiikatan naik lebih dari enam kali sejauh orbital ikatan turun. Ketidaksimetrisan ini berasal dari penyebut $1 \pm S$: dengan $S = 0{,}59$, pembagi untuk antiikatan hanya 0,41, sedangkan untuk ikatan 1,59. Inilah alasan kuantitatif mengapa He₂, dengan dua elektron ikatan dan dua antiikatan, tidak terikat (subbab 11.7).
:::

::: {.contoh}
**Contoh 11.13 · Energi Coulomb klasik tidak mengikat**

Tunjukkan bahwa $J + 1/R = (1 + 1/R)e^{-2R}$ dan bahwa besaran ini positif untuk semua $R$. Apa artinya?

**Penyelesaian.** Dari (11.16), $J + 1/R = -\tfrac1R + \tfrac1R(1 + R)e^{-2R} + \tfrac1R = (1 + 1/R)e^{-2R}$. Kedua faktornya positif.

**Memahami hasil.** Bila elektron hanya berada di atom $A$ (tanpa tumpang tindih dengan $B$), energi sistem relatif terhadap H + H⁺ adalah $J + 1/R$: tarikan awan elektron $A$ oleh proton $B$, ditambah tolakan dua proton. Besaran ini positif di setiap jarak, karena awan elektron tidak pernah sepenuhnya melindungi proton $A$ dari proton $B$. Elektrostatika klasik tidak dapat menjelaskan ikatan. Semua energi ikat dalam (11.15) datang dari suku yang memuat $K$ dan $S$, yaitu dari interferensi kedua orbital atom.
:::

::: {.contoh}
**Contoh 11.14 · Mencari minimum dengan Python**

Tulis program untuk mencari $R_e$ dan $D_e$ kurva $E_+$ LCAO.

**Penyelesaian.**

```python
import numpy as np
from scipy.optimize import minimize_scalar
def E_ikat(R):
    S = np.exp(-R) * (1 + R + R**2 / 3)
    J = -(1 - (1 + R) * np.exp(-2 * R)) / R
    K = -(1 + R) * np.exp(-R)
    return -0.5 + 1 / R + (J + K) / (1 + S)
r = minimize_scalar(E_ikat, bounds=(1, 5), method='bounded')
print(r.x, -0.5 - r.fun, (-0.5 - r.fun) * 27.2114)   # 2.493  0.0648  1.764
```

**Memahami hasil.** $R_e = 2{,}49$ bohr dan $D_e = 1{,}76$ eV, yaitu 63% energi ikat eksak, dengan ikatan 25% terlalu panjang. Kelemahan utamanya adalah bahwa fungsi uji memakai orbital 1s atom H yang tidak diubah. Di dalam molekul, elektron ditarik oleh dua proton, sehingga awannya semestinya lebih rapat ke inti.
:::

::: {.contoh}
**Contoh 11.15 · Orbital yang menyusut: eksponen $\zeta$**

Ganti orbital atom dengan $1s = (\zeta^3/\pi)^{1/2}e^{-\zeta r}$ dan optimalkan $\zeta$ bersama $R$. Hasil optimasi numeriknya: $\zeta = 1{,}238$, $R_e = 2{,}003$ bohr, $E = -0{,}58651$ hartree. Hitung $D_e$ dan tafsirkan $\zeta$ di batas $R \to 0$ dan $R \to \infty$.

**Penyelesaian.** $D_e = (-0{,}5 + 0{,}58651) \times 27{,}211 = 2{,}354$ eV, yaitu 84% nilai eksak, dengan $R_e$ yang praktis tepat. Untuk $R \to \infty$, setiap atom adalah H biasa sehingga $\zeta \to 1$. Untuk $R \to 0$, sistem menjadi He⁺, yang orbital 1s-nya mempunyai $\zeta = Z = 2$.

**Memahami hasil.** Di jarak setimbang, $\zeta = 1{,}24$ berada di antara kedua batas: orbital menyusut karena elektron merasakan tarikan dua inti. Penyusutan ini menaikkan energi kinetik elektron tetapi menurunkan energi potensialnya lebih banyak lagi. Di subbab 11.15 kita akan melihat bahwa penyusutan orbital adalah bagian penting dari mekanisme ikatan, dan bahwa optimasi $\zeta$ membuat fungsi uji memenuhi teorema virial.
:::

::: {.contoh}
**Contoh 11.16 · Polarisasi: menambah orbital 2p**

Awan elektron dalam molekul tidak bersimetri bola di sekitar setiap inti; ia tertarik ke arah inti tetangga. Tambahkan pada setiap atom orbital $2p_z$ yang mengarah ke inti lain, dengan eksponennya sendiri, lalu selesaikan masalah variasi 4 × 4 secara numerik. Hasil optimasi: $\zeta_{1s} = 1{,}246$, $\zeta_{2p} = 1{,}48$, $R_e = 2{,}001$ bohr, $E = -0{,}60036$ hartree. Hitung $D_e$ dan bandingkan dengan nilai eksak.

**Penyelesaian.** $D_e = (0{,}60036 - 0{,}5) \times 27{,}211 = 2{,}731$ eV, yaitu 97,8% dari 2,793 eV.

**Memahami hasil.** Fungsi $2p_z$ sendiri hampir tidak mengubah energi atom H terpisah, tetapi dalam molekul ia memungkinkan awan 1s bergeser ke daerah antarinti. Fungsi seperti ini disebut **fungsi polarisasi**, dan menjadi bagian baku setiap himpunan basis dalam kimia komputasi (subbab 17.5, basis seperti 6-31G** atau cc-pVDZ). Urutan perbaikan 1,76 → 2,35 → 2,73 → 2,79 eV memperlihatkan pola yang umum: fungsi uji yang lebih lentur selalu memberi energi lebih rendah (teorema variasi), dan setiap tambahan fisis yang tepat membawa sebagian besar sisa kesalahan.
:::

::: {.awas}
**Awas · "Pertukaran" di sini bukan pertukaran elektron**

Nama "integral pertukaran" untuk $K$ dalam H₂⁺ adalah peninggalan sejarah yang menyesatkan: hanya ada satu elektron, jadi tidak ada yang dipertukarkan. Integral ini sering juga disebut **integral resonansi**, dan dalam teori Hückel ia menjadi parameter $\beta$ (Bab 13). Dalam molekul berelektron banyak ada integral yang benar-benar timbul dari pertukaran dua elektron identik (integral $K_{ij}$ Hartree–Fock, subbab 9.8). Keduanya berbeda, meskipun sama-sama dilambangkan $K$ dalam banyak buku.
:::

::: {.kuis}
**Kuis cepat 11.4**

\(a) Berapa nilai $S$, $J$, dan $K$ untuk $R \to 0$ dan $R \to \infty$? (b) Mengapa orbital antiikatan naik lebih jauh daripada orbital ikatan turun? (c) Integral mana yang menjadi sumber energi ikat?
:::
