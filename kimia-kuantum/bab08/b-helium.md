## 8.3 Fungsi uji sederhana; atom helium dengan muatan efektif

### Memilih fungsi uji

Bagaimana menebak fungsi gelombang helium? Titik awal yang wajar adalah helium tanpa tolakan antarelektron (subbab 4.4): kedua elektron berada pada orbital 1s ion He⁺, sehingga fungsi gelombangnya adalah hasil kali

$$
\psi^{(0)} = \frac{Z^3}{\pi}e^{-Zr_1}e^{-Zr_2} , \qquad Z = 2 .
$$

Fungsi ini mengabaikan sesuatu yang secara fisika jelas penting. Setiap elektron menghabiskan sebagian waktunya lebih dekat ke inti daripada elektron yang lain, dan dari sudut pandang elektron yang berada di luar, muatan negatif elektron yang di dalam menutupi sebagian muatan inti. Elektron-elektron itu saling **memerisai** (*screening*). Akibatnya, setiap elektron seolah-olah merasakan inti yang muatannya kurang dari 2, dan orbitalnya seharusnya sedikit lebih mengembang daripada orbital He⁺.

Gagasan ini dimasukkan dengan cara yang paling sederhana: biarkan eksponen orbital menjadi parameter variasi $\zeta$,

$$
\phi(\mathbf r_1, \mathbf r_2) = \frac{\zeta^3}{\pi}e^{-\zeta r_1}e^{-\zeta r_2} . \qquad \text{(8.9)}
$$

Fungsi ini sudah ternormalisasi (setiap faktor adalah orbital 1s ternormalisasi dengan eksponen $\zeta$). Parameter $\zeta$ disebut **muatan inti efektif**. Perhatikan bahwa Hamiltonian tetap memakai muatan inti yang sebenarnya, $Z = 2$; hanya fungsi ujinya yang memakai $\zeta$.

### Menghitung integral variasi

Tuliskan Hamiltonian (8.1) sebagai jumlah lima suku dan hitung nilai rata-rata masing-masing.

**Energi kinetik.** Orbital $e^{-\zeta r}$ adalah fungsi eigen operator mirip hidrogen dengan muatan $\zeta$: $\left(-\tfrac12\nabla^2 - \zeta/r\right)e^{-\zeta r} = -\tfrac12\zeta^2e^{-\zeta r}$. Dari contoh penskalaan (Contoh 8.10), energi kinetik rata-rata satu elektron dalam orbital ini adalah $\tfrac12\zeta^2$. Untuk dua elektron:

$$
\left\langle -\tfrac12\nabla_1^2 - \tfrac12\nabla_2^2\right\rangle = \zeta^2 .
$$

**Tarikan inti.** Untuk orbital 1s dengan eksponen $\zeta$, $\langle 1/r\rangle = \zeta$ (subbab 7.9). Jadi

$$
\left\langle -\frac{Z}{r_1} - \frac{Z}{r_2}\right\rangle = -2Z\zeta .
$$

**Tolakan antarelektron.** Integral ini yang paling sulit, dan penurunannya diberikan dalam kotak "Lebih dalam" di bawah. Hasilnya:

$$
\left\langle\frac{1}{r_{12}}\right\rangle = \frac58\zeta . \qquad \text{(8.10)}
$$

Menjumlahkan ketiganya,

$$
W(\zeta) = \zeta^2 - 2Z\zeta + \frac58\zeta . \qquad \text{(8.11)}
$$

Bentuk ini persis bentuk penskalaan (8.7): energi kinetik berskala $\zeta^2$ dan semua energi potensial Coulomb berskala $\zeta$.

### Minimum dan muatan inti efektif

Syarat minimum:

$$
\frac{dW}{d\zeta} = 2\zeta - 2Z + \frac58 = 0 \quad\Longrightarrow\quad \zeta = Z - \frac{5}{16} , \qquad \text{(8.12)}
$$

dan memasukkannya kembali ke (8.11) memberi

$$
W_\text{min} = -\left(Z - \frac{5}{16}\right)^2 . \qquad \text{(8.13)}
$$

Untuk helium, $\zeta = 27/16 = 1{,}6875$ dan $W = -(27/16)^2 = -729/256 = -2{,}8477\ E_h = -77{,}49$ eV. Energi eksak (nonrelativistik) adalah $-2{,}9037\ E_h = -79{,}01$ eV. Galatnya $0{,}0561\ E_h = 1{,}53$ eV, atau 1,9%. Dengan satu parameter, kita telah menurunkan galat dari 38% (tanpa tolakan) dan 5,3% (perturbasi orde pertama, Contoh 8.1) menjadi kurang dari 2%.

![Gambar 8.1 Kiri: integral variasi helium $W(\zeta) = \zeta^2 - \tfrac{27}{8}\zeta$ terhadap eksponen orbital. Minimumnya di $\zeta = 27/16$; garis mendatar menandai energi Hartree–Fock dan energi eksak, yang tidak dapat dicapai oleh fungsi satu eksponen. Kanan: muatan inti efektif yang dirasakan satu elektron di jarak $r$, yaitu $2$ dikurangi bagian elektron lain yang berada di dalam bola berjari-jari $r$. Dekat inti perisai hampir nol, jauh dari inti perisai hampir penuh; nilai variasi 1,69 adalah kompromi rata-rata.](fig/c_zeta.png){width=92%}

Bilangan $5/16 = 0{,}3125$ adalah **tetapan perisai** $\sigma$: setiap elektron 1s mengurangi muatan inti yang dirasakan elektron 1s lainnya sebesar kira-kira sepertiga muatan elektron. Mengapa tidak satu penuh? Karena elektron yang lain tidak selalu berada di dalam; ia hanya memerisai sebagian waktu, dan rata-rata keadaan "di dalam" dan "di luar" memberi perisai efektif 0,31.

::: {.dalam}
**Lebih dalam: penurunan $\langle 1/r_{12}\rangle = 5\zeta/8$**

Gagasan kuncinya fisika listrik statis. Pandang elektron 2 sebagai awan muatan dengan kerapatan $\rho(r) = |\phi_{1s}(r)|^2 = (\zeta^3/\pi)e^{-2\zeta r}$ (muatan total 1). Integral $\langle 1/r_{12}\rangle$ sama dengan energi interaksi awan muatan elektron 1 dengan potensial listrik $\Phi(r_1)$ yang dibangkitkan awan elektron 2:

$$
\left\langle\frac{1}{r_{12}}\right\rangle = \int\rho(r_1)\Phi(r_1)\,d\tau_1 , \qquad \Phi(r_1) = \int\frac{\rho(r_2)}{r_{12}}\,d\tau_2 .
$$

Karena awan bersimetri bola, teorema kulit (*Fisika Umum*, Bab 12) memberi: muatan di dalam bola berjari-jari $r_1$ bertindak seolah-olah terkumpul di pusat, sedangkan setiap kulit tipis di luar $r_1$ menghasilkan potensial tetap sebesar muatannya dibagi jari-jarinya sendiri. Jadi

$$
\Phi(r_1) = \frac{1}{r_1}\int_0^{r_1}\rho\,4\pi r^2dr + \int_{r_1}^\infty\frac{\rho}{r}\,4\pi r^2dr .
$$

Dengan $\rho\,4\pi r^2 = 4\zeta^3r^2e^{-2\zeta r}$ dan integral parsial (subbab 2.2):

$$
\int_0^{r_1}4\zeta^3r^2e^{-2\zeta r}dr = 1 - e^{-2\zeta r_1}\left(1 + 2\zeta r_1 + 2\zeta^2r_1^2\right) , \qquad \int_{r_1}^\infty4\zeta^3re^{-2\zeta r}dr = e^{-2\zeta r_1}\left(\zeta + 2\zeta^2r_1\right) .
$$

Jumlahkan (suku pertama dibagi $r_1$); suku-suku $2\zeta^2r_1$ saling menghapus:

$$
\Phi(r_1) = \frac{1}{r_1} - e^{-2\zeta r_1}\left(\frac{1}{r_1} + \zeta\right) .
$$

Di jauh, $\Phi \to 1/r_1$, potensial muatan titik; di dekat inti, $\Phi \to \zeta$ (berhingga), karena di sana elektron 1 berada di dalam awan. Sekarang rata-ratakan atas awan elektron 1:

$$
\left\langle\frac{1}{r_{12}}\right\rangle = 4\zeta^3\int_0^\infty r^2e^{-2\zeta r}\left[\frac1r - e^{-2\zeta r}\left(\frac1r + \zeta\right)\right]dr = 4\zeta^3\left[\frac{1}{4\zeta^2} - \frac{1}{16\zeta^2} - \zeta\cdot\frac{2}{(4\zeta)^3}\right] .
$$

Kurung siku bernilai $(8 - 2 - 1)/32\zeta^2 = 5/32\zeta^2$, sehingga $\langle 1/r_{12}\rangle = 4\zeta^3\cdot5/32\zeta^2 = 5\zeta/8$. Untuk $\zeta = Z = 2$, nilainya $\tfrac54\ E_h = 34{,}0$ eV, yang kita pakai di Contoh 8.1.

Untuk orbital yang tidak bersimetri bola, cara ini diganti dengan **ekspansi Laplace** $1/r_{12} = \sum_\ell(r_<^\ell/r_>^{\ell+1})P_\ell(\cos\gamma)$, dengan $\gamma$ sudut antara $\mathbf r_1$ dan $\mathbf r_2$; untuk dua orbital s hanya suku $\ell = 0$ yang tersisa, dan hasilnya sama.
:::

::: {.contoh}
**Contoh 8.11 · Rincian energi helium di titik optimum**

Untuk fungsi uji (8.9) dengan $\zeta = 27/16$, hitung energi kinetik, tarikan inti, dan tolakan antarelektron secara terpisah. Bandingkan dengan nilai-nilai untuk $\zeta = 2$ (orbital He⁺ tanpa perubahan).

**Penyelesaian.**

| Suku | $\zeta = 2$ | $\zeta = 1{,}6875$ |
|---|---|---|
| $\langle T\rangle = \zeta^2$ | 4,0000 | 2,8477 |
| $\langle V_{ne}\rangle = -2Z\zeta$ | $-8{,}0000$ | $-6{,}7500$ |
| $\langle V_{ee}\rangle = 5\zeta/8$ | 1,2500 | 1,0547 |
| $W$ | $-2{,}7500$ | $-2{,}8477$ |

Energi potensial total di titik optimum $-6{,}7500 + 1{,}0547 = -5{,}6953$, dan $\langle V\rangle/\langle T\rangle = -2{,}0000$.

**Memahami hasil.** Mengembangnya orbital (dari $\zeta = 2$ ke 1,69) mengorbankan 1,25 $E_h$ tarikan inti, tetapi menghemat 1,15 $E_h$ energi kinetik dan 0,20 $E_h$ tolakan antarelektron. Neraca bersihnya $-0{,}098\ E_h = -2{,}66$ eV. Teorema virial terpenuhi tepat, sesuai (8.8): dengan satu parameter skala, metode variasi selalu memenuhi virial. Pada $\zeta = 2$ perbandingannya $-6{,}75/4 = -1{,}69$, tanda bahwa fungsi itu belum seimbang.
:::

::: {.contoh}
**Contoh 8.12 · Energi ionisasi pertama helium**

Energi ionisasi pertama adalah $I_1 = E(\text{He}^+) - E(\text{He})$, dengan $E(\text{He}^+) = -Z^2/2 = -2\ E_h$ (eksak). Hitung $I_1$ dari (a) model tanpa tolakan, (b) perturbasi orde pertama ($-2{,}75\ E_h$), (c) fungsi variasi dengan muatan efektif. Nilai eksperimen 24,59 eV.

**Penyelesaian.** (a) $-2 - (-4) = 2\ E_h = 54{,}4$ eV. (b) $-2 + 2{,}75 = 0{,}75\ E_h = 20{,}4$ eV. (c) $-2 + 2{,}8477 = 0{,}8477\ E_h = 23{,}07$ eV, terlalu rendah 1,52 eV (6,2%).

**Memahami hasil.** Galat relatif energi ionisasi (6,2%) tiga kali galat relatif energi total (1,9%), karena seluruh galat energi helium masuk ke selisih, sedangkan energi He⁺ eksak. Ini contoh situasi tanpa pembatalan galat. Meski begitu, nilai 23,1 eV sudah menjelaskan mengapa helium gas mulia: energi ionisasinya adalah yang tertinggi di antara semua unsur, hampir dua kali energi ionisasi hidrogen, padahal elektronnya sama-sama berada di kulit $n = 1$. Muatan inti efektif 1,69 jauh lebih besar daripada 1.
:::

::: {.contoh}
**Contoh 8.13 · Ion mirip helium dan kegagalan H⁻**

Terapkan (8.12) dan (8.13) pada deret isoelektron H⁻, He, Li⁺, Be²⁺, B³⁺. Bandingkan dengan energi eksak ($-0{,}52775$; $-2{,}90372$; $-7{,}27991$; $-13{,}65557$; $-22{,}03097\ E_h$). Apa yang diramalkan untuk H⁻?

**Penyelesaian.**

| Ion | $Z$ | $\zeta$ | $W$ ($E_h$) | Eksak ($E_h$) | Galat ($E_h$) |
|---|---|---|---|---|---|
| H⁻ | 1 | 0,6875 | $-0{,}47266$ | $-0{,}52775$ | 0,05509 |
| He | 2 | 1,6875 | $-2{,}84766$ | $-2{,}90372$ | 0,05607 |
| Li⁺ | 3 | 2,6875 | $-7{,}22266$ | $-7{,}27991$ | 0,05726 |
| Be²⁺ | 4 | 3,6875 | $-13{,}59766$ | $-13{,}65557$ | 0,05791 |
| B³⁺ | 5 | 4,6875 | $-21{,}97266$ | $-22{,}03097$ | 0,05832 |

Untuk H⁻, $W = -0{,}4727\ E_h$ lebih tinggi daripada energi atom H netral ditambah elektron bebas di jauh tak hingga, $-0{,}5\ E_h$. Model meramalkan bahwa H⁻ **tidak terikat**: elektron kedua akan lepas.

**Memahami hasil.** Galat mutlak hampir tetap, sekitar $0{,}056$–$0{,}058\ E_h$, untuk semua ion: ia mencerminkan sesuatu yang tidak bergantung pada $Z$, yaitu kegagalan fungsi hasil kali untuk menggambarkan bagaimana kedua elektron saling menghindar (korelasi elektron, subbab 9.10). Untuk ion bermuatan besar, galat ini kecil dibandingkan energi total; untuk H⁻ ia menentukan segalanya. Padahal H⁻ nyata ada: afinitas elektron hidrogen adalah 0,754 eV, ion ini menentukan keburaman atmosfer Matahari, dan hidrida logam seperti LiH dan NaH mengandungnya. Teorema variasi tidak salah; fungsi ujinya yang terlalu kaku.
:::

### Fungsi uji yang lebih lentur

Mengapa fungsi (8.9) gagal untuk H⁻? Fungsi itu memaksa kedua elektron menempati orbital yang **sama**. Dalam H⁻ yang sebenarnya, satu elektron terikat erat seperti dalam atom H, sedangkan elektron kedua mengembara jauh di luar, terikat lemah oleh polarisasi atom H. Gambaran "satu di dalam, satu di luar" ini dapat dimasukkan dengan memberi kedua elektron eksponen berbeda, sambil menjaga simetri terhadap pertukaran elektron (subbab 9.3):

$$
\phi = e^{-ar_1}e^{-br_2} + e^{-br_1}e^{-ar_2} . \qquad \text{(8.14)}
$$

Fungsi ini, yang dipakai Eckart (1930) untuk helium dan Chandrasekhar (1944) untuk H⁻, mempunyai dua parameter. Integral variasinya masih dapat dihitung secara analitis, karena semua suku adalah integral orbital 1s dengan eksponen berbeda. Minimisasi dua peubah paling mudah dikerjakan dengan komputer.

::: {.contoh}
**Contoh 8.14 · Fungsi dua eksponen dengan Python**

Hitung energi minimum fungsi (8.14) untuk H⁻ dan He. Integral yang diperlukan (untuk fungsi tak ternormalisasi $e^{-ar}$): tumpang tindih $\langle e^{-ar}|e^{-br}\rangle = 8\pi/(a + b)^3$; energi kinetik $\langle e^{-ar}|-\tfrac12\nabla^2|e^{-br}\rangle = -\tfrac12[b^2\cdot8\pi/(a+b)^3 - 2b\cdot4\pi/(a+b)^2]$; tarikan inti $-Z\cdot4\pi/(a + b)^2$; dan integral tolakan dua awan $e^{-pr_1}$ dan $e^{-qr_2}$, yaitu $32\pi^2(p^2 + 3pq + q^2)/[p^2q^2(p + q)^3]$.

**Penyelesaian.**

```python
import numpy as np
from scipy.optimize import minimize

S = lambda a, b: 8*np.pi/(a + b)**3                      # <e^-ar | e^-br>
T = lambda a, b: -0.5*(b*b*S(a, b) - 8*np.pi*b/(a + b)**2)
V = lambda a, b, Z: -4*np.pi*Z/(a + b)**2
J = lambda p, q: 32*np.pi**2*(p*p + 3*p*q + q*q)/(p*p*q*q*(p + q)**3)

def energi(x, Z):
    a, b = x
    h = lambda a, b: T(a, b) + V(a, b, Z)                 # Hamiltonian satu elektron
    HAA = h(a, a)*S(b, b) + S(a, a)*h(b, b) + J(2*a, 2*b) # <A|H|A>, A = e^-ar1 e^-br2
    HAB = 2*h(a, b)*S(a, b) + J(a + b, a + b)             # <A|H|B>, B = e^-br1 e^-ar2
    return (HAA + HAB)/(S(a, a)*S(b, b) + S(a, b)**2)

for Z in (1, 2):
    r = minimize(energi, [Z + 0.1, 0.5*Z], args=(Z,), method='Nelder-Mead')
    print(Z, r.x.round(4), round(r.fun, 5))
```

Keluarannya: untuk H⁻, $a = 1{,}039$, $b = 0{,}283$, $W = -0{,}51330\ E_h$; untuk He, $a = 2{,}183$, $b = 1{,}189$, $W = -2{,}87566\ E_h$.

**Memahami hasil.** Untuk H⁻, $W = -0{,}5133\ E_h$ kini **di bawah** $-0{,}5\ E_h$: fungsi dua eksponen membuktikan bahwa H⁻ terikat, dengan energi ikat sekurang-kurangnya $0{,}0133\ E_h = 0{,}36$ eV (nilai eksak 0,754 eV). Karena $W$ adalah batas atas, kesimpulan "terikat" ini dijamin oleh teorema variasi, tidak bergantung pada ketelitian lain. Eksponen dalamnya ($a = 1{,}04$) hampir sama dengan atom H, dan eksponen luarnya ($b = 0{,}28$) memberi orbital yang sangat menyebar, dengan jari-jari rata-rata $3/2b = 5{,}3\ a_0$. Untuk helium, perbaikannya $0{,}028\ E_h$ (0,76 eV): separuh galat fungsi satu eksponen hilang. Fungsi (8.14) menggambarkan sebagian **korelasi radial**: bila satu elektron dekat inti, yang lain cenderung jauh.
:::

::: {.contoh}
**Contoh 8.15 · Ukuran atom helium dan kerentanan diamagnetik**

Untuk orbital 1s dengan eksponen $\zeta$, $\langle r\rangle = 3/2\zeta$ dan $\langle r^2\rangle = 3/\zeta^2$. (a) Hitung $\langle r\rangle$ elektron helium dengan $\zeta = 27/16$, dan bandingkan dengan elektron He⁺ ($\zeta = 2$). (b) Kerentanan magnet molar atom diamagnetik adalah $\chi_m = -\mu_0N_Ae^2\sum_i\langle r_i^2\rangle/6m_e$ (SI). Hitung $\chi_m$ dan nyatakan dalam satuan cgs yang lazim di tabel ($\chi_m^\text{cgs} = \chi_m^\text{SI}\times10^6/4\pi$, dalam cm³/mol). Nilai terukur sekitar $-1{,}9 \times 10^{-6}$ cm³/mol.

**Penyelesaian.** (a) $\langle r\rangle = 3/(2 \times 1{,}6875) = 0{,}889\ a_0 = 47{,}0$ pm; untuk He⁺, $0{,}750\ a_0 = 39{,}7$ pm. Elektron helium 18% lebih jauh dari inti.

(b) $\sum\langle r^2\rangle = 2 \times 3/(1{,}6875)^2 = 2{,}107\ a_0^2 = 5{,}90 \times 10^{-21}$ m². Maka $\chi_m = -(4\pi \times 10^{-7})(6{,}022 \times 10^{23})(1{,}602 \times 10^{-19})^2(5{,}90 \times 10^{-21})/(6 \times 9{,}109 \times 10^{-31}) = -2{,}10 \times 10^{-11}$ m³/mol, atau $-1{,}67 \times 10^{-6}$ cm³/mol (cgs).

**Memahami hasil.** Fungsi satu parameter meramalkan kerentanan diamagnetik dengan galat sekitar 12%, lebih besar daripada galat energinya (1,9%). Ini sesuai dengan pesan (8.5): parameter dioptimumkan untuk energi, bukan untuk $\langle r^2\rangle$, dan $\langle r^2\rangle$ sangat peka terhadap ekor fungsi gelombang di jauh, tempat fungsi uji paling kurang tepat. Fungsi gelombang yang sangat teliti memberi $\sum\langle r^2\rangle = 2{,}387\ a_0^2$ dan $\chi_m = -1{,}89 \times 10^{-6}$ cm³/mol, sesuai pengukuran.
:::

::: {.contoh}
**Contoh 8.16 · Tangga energi helium**

Susun energi keadaan dasar helium menurut metode berikut dan hitung galatnya dalam eV: (a) tanpa tolakan; (b) satu eksponen $\zeta$; (c) orbital terbaik yang mungkin untuk fungsi hasil kali (batas Hartree–Fock, $-2{,}86168\ E_h$); (d) dua eksponen (Contoh 8.14); (e) fungsi Hylleraas tiga parameter yang memuat $r_{12}$ secara eksplisit ($-2{,}90243\ E_h$); (f) eksak, $-2{,}90372\ E_h$.

**Penyelesaian.**

| Metode | $E$ ($E_h$) | Galat (eV) |
|---|---|---|
| tanpa tolakan | $-4{,}00000$ | $-29{,}83$ |
| satu eksponen $\zeta$ | $-2{,}84766$ | 1,53 |
| Hartree–Fock | $-2{,}86168$ | 1,14 |
| dua eksponen | $-2{,}87566$ | 0,76 |
| Hylleraas (3 parameter) | $-2{,}90243$ | 0,035 |
| eksak | $-2{,}90372$ | 0 |

**Memahami hasil.** Semua metode variasi memberi energi di atas nilai eksak, dan galatnya turun ketika fungsi ujinya makin lentur. Langkah terbesar terjadi ketika jarak $r_{12}$ dimasukkan langsung ke fungsi gelombang (Hylleraas, 1929): fungsi semacam itu dapat "menggali lubang" di sekitar setiap elektron sehingga elektron lain menghindarinya. Selisih antara batas Hartree–Fock dan energi eksak, $-0{,}04204\ E_h = -1{,}14$ eV (sekitar 110 kJ/mol), disebut **energi korelasi** (subbab 9.10). Angka itu kecil dibandingkan energi total, tetapi sebanding dengan energi ikatan kimia, sehingga tidak boleh diabaikan dalam kimia komputasi yang teliti. Pekeris (1959) memakai 1078 suku Hylleraas; perhitungan modern dengan ribuan fungsi memberi energi helium sampai lebih dari 20 angka penting, jawaban atas teka-teki pembuka bab ini.
:::

### Makna kimia: muatan inti efektif

Hasil (8.12) adalah benih dari salah satu konsep terpenting kimia anorganik: **muatan inti efektif** $Z_\text{ef} = Z - \sigma$. Pada tahun 1930 Slater merumuskan aturan empiris untuk menaksir $\sigma$ bagi setiap elektron dalam atom apa pun; untuk sepasang elektron 1s ia memberikan $\sigma = 0{,}30$, sangat dekat dengan $5/16 = 0{,}3125$ hasil variasi. Clementi dan Raimondi (1963) kemudian mengoptimumkan eksponen orbital secara variasi untuk semua atom sampai kripton; untuk helium mereka memperoleh tepat 1,6875.

Muatan inti efektif menjelaskan kecenderungan periodik yang dipelajari di kimia dasar. Sepanjang satu periode, $Z$ naik satu demi satu tetapi elektron sekulit hanya saling memerisai sebagian (sekitar 0,35 per elektron menurut Slater), sehingga $Z_\text{ef}$ naik sekitar 0,65 setiap langkah: jari-jari atom mengecil dan energi ionisasi naik. Ketika kulit baru mulai diisi, elektron kulit dalam memerisai hampir sempurna, $Z_\text{ef}$ anjlok, dan energi ionisasi turun tajam dari gas mulia ke logam alkali. Bab 9 mengembangkan gagasan ini menjadi teori orbital atom berelektron banyak.

::: {.awas}
**Muatan inti efektif bukan muatan yang terukur**

$\zeta = 1{,}6875$ adalah parameter dalam fungsi uji tertentu, dipilih untuk meminimumkan energi. Ia tidak sama dengan muatan yang "benar-benar" dirasakan elektron di setiap titik, karena perisai bergantung pada jarak: di dekat inti elektron merasakan hampir 2, di jauh hampir 1 (lihat potensial $\Phi(r_1)$ dalam kotak di atas). Fungsi uji yang berbeda, atau sifat lain yang dioptimumkan (misalnya $\langle r^2\rangle$), memberi $Z_\text{ef}$ yang sedikit berbeda. Pakailah $Z_\text{ef}$ untuk membandingkan kecenderungan, bukan sebagai besaran mutlak.
:::

::: {.terapan}
**Muatan inti efektif dalam praktik kimia**

Basis minimal STO-3G, basis pertama yang dipakai luas dalam kimia komputasi, memakai eksponen Slater yang dioptimumkan untuk molekul, misalnya $\zeta = 1{,}24$ untuk hidrogen dalam molekul (lebih besar dari 1, karena dalam ikatan elektron ditarik dua inti). Model elektronegativitas Allred–Rochow menghitung elektronegativitas dari $Z_\text{ef}/r^2$, gaya elektrostatik yang dirasakan elektron valensi pada jari-jari kovalen. Dengan demikian, satu parameter variasi untuk atom helium berkembang menjadi alat untuk meramalkan polaritas ikatan.
:::

::: {.kuis}
**Kuis cepat 8.3**

(a) Mengapa $\zeta_\text{opt}$ helium lebih kecil daripada 2, tetapi lebih besar daripada 1? (b) Untuk ion Li⁺, berapa $\zeta$ optimum dan berapa energi ionisasi Li⁺ → Li²⁺ yang diramalkan (dalam eV)? (c) Mengapa fungsi satu eksponen gagal mengikat H⁻, padahal teorema variasi berlaku?
:::

