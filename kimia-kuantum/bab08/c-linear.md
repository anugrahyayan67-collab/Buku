## 8.4 Fungsi variasi linear dan persamaan sekuler

### Gagasan: parameter yang muncul secara linear

Fungsi uji di subbab 8.3 bergantung pada parameternya secara tidak linear (parameter berada di eksponen). Minimisasinya memerlukan kalkulus atau komputer, dan setiap fungsi uji memerlukan perhitungan tersendiri. Ada jenis fungsi uji yang jauh lebih sistematis: **kombinasi linear** dari $n$ fungsi tetap yang sudah dipilih,

$$
\phi = c_1f_1 + c_2f_2 + \cdots + c_nf_n = \sum_{j=1}^nc_jf_j . \qquad \text{(8.15)}
$$

Fungsi-fungsi $f_j$ disebut **fungsi basis** (atau himpunan basis), dan koefisien $c_j$ adalah parameter variasi. Fungsi basis tidak harus ortogonal, tidak harus fungsi eigen apa pun, dan boleh berupa apa saja yang memenuhi syarat batas: orbital atom yang berpusat di berbagai inti (metode LCAO, Bab 11), fungsi Gauss (subbab 8.5), polinom, atau fungsi gelombang osilator. Bentuk linear ini mempunyai keuntungan besar: minimisasinya selalu menghasilkan masalah aljabar linear, yang dapat diselesaikan dengan algoritme baku untuk berapa pun nilai $n$.

Untuk memudahkan penulisan, anggap fungsi basis dan koefisiennya riil (perluasan ke bilangan kompleks hanya mengganti $c_j$ dengan $c_j^*$ di tempat yang tepat). Definisikan dua jenis integral:

$$
H_{jk} = \int f_j\hat Hf_k\,d\tau , \qquad S_{jk} = \int f_jf_k\,d\tau . \qquad \text{(8.16)}
$$

$H_{jk}$ adalah **unsur matriks Hamiltonian** dan $S_{jk}$ adalah **integral tumpang tindih** (*overlap*). Karena $\hat H$ Hermitian, $H_{jk} = H_{kj}$; jelas pula $S_{jk} = S_{kj}$, dan $S_{jj} = 1$ bila setiap fungsi basis ternormalisasi.

### Penurunan persamaan sekuler

Masukkan (8.15) ke integral variasi (8.3):

$$
W = \frac{\sum_j\sum_kc_jc_kH_{jk}}{\sum_j\sum_kc_jc_kS_{jk}} , \qquad\text{atau}\qquad W\sum_j\sum_kc_jc_kS_{jk} = \sum_j\sum_kc_jc_kH_{jk} .
$$

Kita mencari koefisien yang meminimumkan $W$, jadi turunkan bentuk kedua terhadap satu koefisien $c_i$. Di ruas kiri, aturan perkalian memberi dua bagian: turunan $W$ dikali jumlah, ditambah $W$ dikali turunan jumlah. Turunan jumlah ganda terhadap $c_i$ adalah $\sum_kc_kS_{ik} + \sum_jc_jS_{ji} = 2\sum_kc_kS_{ik}$ (karena $S$ simetris); hal yang sama berlaku di ruas kanan. Jadi

$$
\frac{\partial W}{\partial c_i}\sum_j\sum_kc_jc_kS_{jk} + 2W\sum_kc_kS_{ik} = 2\sum_kc_kH_{ik} .
$$

Di minimum, $\partial W/\partial c_i = 0$ untuk setiap $i$, sehingga

$$
\sum_{k=1}^n\left(H_{ik} - WS_{ik}\right)c_k = 0 , \qquad i = 1, 2, \ldots, n . \qquad \text{(8.17)}
$$

Ini adalah $n$ persamaan linear **homogen** untuk $n$ koefisien. Sistem seperti itu selalu mempunyai penyelesaian trivial $c_k = 0$, yang tidak berarti apa-apa (fungsi gelombang nol). Menurut (2.33), penyelesaian tak trivial ada jika dan hanya jika determinan koefisiennya nol:

$$
\det\left(H_{ik} - WS_{ik}\right) = \begin{vmatrix} H_{11} - WS_{11} & H_{12} - WS_{12} & \cdots & H_{1n} - WS_{1n}\\ H_{21} - WS_{21} & H_{22} - WS_{22} & \cdots & H_{2n} - WS_{2n}\\ \vdots & \vdots & \ddots & \vdots\\ H_{n1} - WS_{n1} & H_{n2} - WS_{n2} & \cdots & H_{nn} - WS_{nn}\end{vmatrix} = 0 . \qquad \text{(8.18)}
$$

Persamaan (8.18) adalah **persamaan sekuler**. Namanya berasal dari mekanika langit abad ke-18, ketika persamaan serupa muncul dalam perhitungan gangguan "sekuler" (berjangka sangat panjang, dari kata Latin *saeculum*, abad) pada orbit planet. Penguraian determinan memberi polinom berderajat $n$ dalam $W$, yang mempunyai $n$ akar riil $W_1 \le W_2 \le \cdots \le W_n$.

Akar terkecil $W_1$ adalah energi variasi terbaik, dan menurut teorema variasi $W_1 \ge E_1$. Untuk memperoleh fungsi gelombangnya, masukkan $W_1$ ke (8.17) dan selesaikan untuk perbandingan koefisien; nilai mutlaknya ditentukan oleh normalisasi $\sum_j\sum_kc_jc_kS_{jk} = 1$.

### Teorema Hylleraas–Undheim–MacDonald

Bagaimana dengan akar-akar yang lain? Hylleraas dan Undheim (1930) serta MacDonald (1933) membuktikan bahwa setiap akar adalah batas atas untuk energi eksak yang bersesuaian:

$$
W_1 \ge E_1, \qquad W_2 \ge E_2, \qquad \ldots, \qquad W_n \ge E_n . \qquad \text{(8.19)}
$$

Lebih dari itu, bila satu fungsi basis ditambahkan, akar-akar baru **menyelang** akar-akar lama: setiap akar lama terletak di antara dua akar baru yang berurutan, sehingga semua akar bergerak turun (atau tetap) ketika basis diperbesar. Jadi satu perhitungan variasi linear memberi sekaligus batas atas untuk $n$ tingkat energi terendah, dan menambah basis tidak pernah memperburuk satu pun dari batas-batas itu. Teorema ini adalah dasar perhitungan keadaan tereksitasi dengan metode interaksi konfigurasi.

::: {.inti}
**Metode variasi linear**

Fungsi uji $\phi = \sum_jc_jf_j$ menghasilkan persamaan

$$
\sum_k(H_{ik} - WS_{ik})c_k = 0 , \qquad \det(\mathbf H - W\mathbf S) = 0 .
$$

Akar-akar persamaan sekuler $W_1 \le W_2 \le \cdots \le W_n$ adalah batas atas untuk $E_1, E_2, \ldots, E_n$, dan semuanya turun bila basis diperbesar. Bila basisnya ortonormal, $\mathbf S = \mathbf 1$ dan masalahnya menjadi masalah nilai eigen biasa.
:::

### Kasus dua fungsi basis

Kasus $n = 2$ dengan fungsi basis ternormalisasi dan tumpang tindih $S_{12} = S$ sudah memuat hampir semua gagasan penting. Persamaan sekulernya

$$
\begin{vmatrix} H_{11} - W & H_{12} - WS\\ H_{12} - WS & H_{22} - W\end{vmatrix} = (H_{11} - W)(H_{22} - W) - (H_{12} - WS)^2 = 0 . \qquad \text{(8.20)}
$$

**Basis setara.** Bila kedua fungsi basis setara karena simetri, $H_{11} = H_{22} \equiv \alpha$ dan $H_{12} \equiv \beta$, maka $(\alpha - W)^2 = (\beta - WS)^2$, sehingga $\alpha - W = \pm(\beta - WS)$:

$$
W_\pm = \frac{\alpha \pm \beta}{1 \pm S} , \qquad \phi_\pm = \frac{f_1 \pm f_2}{\sqrt{2(1 \pm S)}} . \qquad \text{(8.21)}
$$

Simetri menentukan fungsi gelombangnya (jumlah dan selisih yang sama besar) sebelum energi dihitung. Inilah bentuk orbital ikatan dan antiikatan H₂⁺ yang akan kita temui di Bab 11.

**Basis ortogonal tak setara.** Bila $S = 0$ tetapi $H_{11} \ne H_{22}$, (8.20) adalah persamaan kuadrat biasa dengan akar

$$
W_\pm = \frac{H_{11} + H_{22}}{2} \pm\sqrt{\left(\frac{H_{11} - H_{22}}{2}\right)^2 + H_{12}^2} . \qquad \text{(8.22)}
$$

Akar bawah selalu di bawah unsur diagonal yang lebih kecil, dan akar atas di atas yang lebih besar: interaksi **mendorong kedua tingkat menjauh**. Koefisien-koefisiennya dapat ditulis dengan sudut campuran $\theta$:

$$
\phi_- = \cos\theta\,f_1 + \sin\theta\,f_2 , \qquad \phi_+ = -\sin\theta\,f_1 + \cos\theta\,f_2 , \qquad \tan2\theta = \frac{2H_{12}}{H_{11} - H_{22}} . \qquad \text{(8.23)}
$$

Dua kasus batas sangat berguna. Bila $|H_{12}| \ll |H_{11} - H_{22}|$, akar kuadrat dapat diuraikan, dan untuk $H_{11} < H_{22}$:

$$
W_- \approx H_{11} - \frac{H_{12}^2}{H_{22} - H_{11}} , \qquad W_+ \approx H_{22} + \frac{H_{12}^2}{H_{22} - H_{11}} : \qquad \text{(8.24)}
$$

pergeseran sebanding dengan **kuadrat** kopling dibagi **selisih** energi, dan pencampurannya kecil. Rumus ini akan muncul lagi sebagai energi perturbasi orde kedua (subbab 8.7). Sebaliknya, bila $H_{11} = H_{22}$ (degenerat), $W_\pm = H_{11} \pm |H_{12}|$, pergeseran sebanding dengan kopling itu sendiri dan pencampurannya 50 : 50, berapa pun kecilnya $H_{12}$. Kopling kecil antara tingkat yang **berjauhan** hampir tidak berpengaruh; kopling kecil antara tingkat yang **berdekatan** mengubah segalanya. Inilah pelajaran kimia terpenting dari matriks 2 × 2.

::: {.contoh}
**Contoh 8.17 · Dua fungsi polinom untuk partikel dalam kotak**

Gunakan basis $f_1 = x(L - x)$ dan $f_2 = x^2(L - x)^2$ untuk partikel dalam kotak. (a) Hitung matriks $\mathbf H$ dan $\mathbf S$. (b) Selesaikan persamaan sekuler. (c) Bandingkan dengan energi eksak.

**Penyelesaian.** (a) Pakai $\hbar = m = L = 1$ dan $H_{jk} = \tfrac12\int_0^1f_j'f_k'\,dx$ (integral parsial, karena fungsi basis nol di dinding). Integral polinom elementer memberi

$$
\mathbf H = \begin{pmatrix} \tfrac16 & \tfrac{1}{30}\\[2pt] \tfrac{1}{30} & \tfrac{1}{105}\end{pmatrix} , \qquad \mathbf S = \begin{pmatrix} \tfrac{1}{30} & \tfrac{1}{140}\\[2pt] \tfrac{1}{140} & \tfrac{1}{630}\end{pmatrix} .
$$

(b) Uraian determinan $\det(\mathbf H - W\mathbf S)$, setelah dikalikan $529\,200$, menjadi $W^2 - 56W + 252 = 0$, dengan akar

$$
W = 28 \mp 2\sqrt{133} = 4{,}934\,874 \quad\text{dan}\quad 51{,}065\,13 \qquad (\hbar^2/mL^2) .
$$

Dari baris pertama (8.17), $c_2/c_1 = -(H_{11} - WS_{11})/(H_{12} - WS_{12}) = 1{,}133$ untuk akar terendah.

(c) $E_1 = \pi^2/2 = 4{,}934\,802$. Akar terendah hanya $1{,}5 \times 10^{-5}$ di atasnya relatif (galat 0,0015%). Kedua fungsi basis genap terhadap titik tengah, sehingga akar kedua adalah batas atas untuk keadaan genap berikutnya, $E_3 = 9\pi^2/2 = 44{,}41$; galatnya 15%.

**Memahami hasil.** Menambahkan satu fungsi basis mengecilkan galat dari 1,3% (parabola saja) menjadi 0,0015%, hampir seribu kali lipat. Koefisien $c_2/c_1 > 0$ berarti fungsi $x^2(1 - x)^2$ ditambahkan untuk "menggembungkan" bagian tengah parabola, sama dengan yang dicapai $p = 1{,}11$ di Contoh 8.8 dengan cara tidak linear. Perhatikan pula bahwa akar kedua jauh kurang teliti daripada akar pertama: basis yang dirancang untuk keadaan dasar selalu paling baik untuk keadaan dasar.
:::

::: {.contoh}
**Contoh 8.18 · Orbital ikatan polar**

Model sederhana ikatan H–F: orbital 2p fluor dengan $H_{11} = -18{,}7$ eV dan orbital 1s hidrogen dengan $H_{22} = -13{,}6$ eV, tumpang tindih diabaikan, dan $H_{12} = -4{,}0$ eV. (a) Hitung energi orbital ikatan dan antiikatan. (b) Hitung sudut campuran dan peluang elektron ikatan berada pada fluor. (c) Bandingkan dengan pendekatan (8.24).

**Penyelesaian.** (a) Rata-rata unsur diagonal $-16{,}15$ eV, setengah selisihnya $-2{,}55$ eV. Akar kuadrat (8.22): $\sqrt{2{,}55^2 + 4{,}0^2} = 4{,}744$ eV. Jadi $W_- = -20{,}89$ eV (ikatan) dan $W_+ = -11{,}41$ eV (antiikatan).

(b) $\tan2\theta = 2(-4{,}0)/(-18{,}7 + 13{,}6) = 1{,}569$, $2\theta = 57{,}5°$, $\theta = 28{,}7°$. Orbital ikatan $= 0{,}877f_\text{F} + 0{,}481f_\text{H}$; peluang pada F: $\cos^2\theta = 0{,}769$.

(c) $H_{12}^2/(H_{22} - H_{11}) = 16/5{,}1 = 3{,}14$ eV memberi $-21{,}84$ dan $-10{,}46$ eV, meleset hampir 1 eV.

**Memahami hasil.** Orbital ikatan terletak lebih dekat ke orbital atom yang energinya lebih rendah (fluor, unsur yang lebih elektronegatif) dan didominasi olehnya: 77% kerapatan elektron ikatan berada di fluor. Inilah asal mula kepolaran ikatan dan muatan parsial negatif pada atom elektronegatif (subbab 11.14). Pendekatan (8.24) kurang tepat karena $|H_{12}|$ = 4,0 eV tidak kecil dibandingkan selisih 5,1 eV; untuk ikatan C–H, yang selisih orbitalnya kecil, pencampurannya jauh lebih merata dan ikatannya hampir nonpolar.
:::

::: {.contoh}
**Contoh 8.19 · Akibat tumpang tindih: mengapa He₂ tidak terikat**

Dalam metode Hückel diperluas, $H_{12} = KS\,(H_{11} + H_{22})/2$ dengan $K = 1{,}75$. Ambil dua orbital setara dengan $\alpha = -11{,}4$ eV dan $S = 0{,}25$. (a) Hitung $W_\pm$ dengan (8.21). (b) Berapa penurunan energi orbital ikatan dan kenaikan energi orbital antiikatan, relatif terhadap $\alpha$? (c) Bila empat elektron mengisi kedua orbital, berapa perubahan energi totalnya?

**Penyelesaian.** (a) $\beta = 1{,}75(0{,}25)(-11{,}4) = -4{,}99$ eV. $W_+ = (-11{,}4 - 4{,}99)/1{,}25 = -13{,}11$ eV; $W_- = (-11{,}4 + 4{,}99)/0{,}75 = -8{,}55$ eV.

(b) Ikatan turun 1,71 eV; antiikatan naik 2,85 eV.

(c) $2(-13{,}11) + 2(-8{,}55) - 4(-11{,}4) = +2{,}28$ eV.

**Memahami hasil.** Dengan tumpang tindih, orbital antiikatan naik **lebih banyak** daripada orbital ikatan turun. Akibatnya, dua elektron (seperti dalam H₂) menghasilkan ikatan, tetapi empat elektron (seperti dalam He₂) menghasilkan tolakan bersih. Inilah dasar kuantum dari "tolakan sterik" antara dua kulit tertutup: dua molekul yang terlalu didesakkan saling tolak karena prinsip yang sama. Bila tumpang tindih diabaikan ($S = 0$), kenaikan dan penurunan sama besar dan efek ini hilang, satu alasan mengapa metode Hückel sederhana tidak dapat menjelaskan struktur ruang molekul.
:::

::: {.contoh}
**Contoh 8.20 · Gugus karbonil: polaritas dan tempat serangan nukleofil**

Model Hückel untuk ikatan π C=O: orbital 2p karbon dengan $H_{\text{CC}} = \alpha$, orbital 2p oksigen dengan $H_{\text{OO}} = \alpha + \beta$ (oksigen lebih elektronegatif), dan $H_{\text{CO}} = \beta$, tanpa tumpang tindih. (a) Tuliskan matriksnya dalam bentuk $E = \alpha + x\beta$ dan cari kedua akarnya. (b) Hitung koefisien orbital π (terisi) dan π* (kosong). (c) Berapa muatan π pada oksigen? (d) Di atom mana nukleofil seharusnya menyerang?

**Penyelesaian.** (a) Dengan urutan basis (O, C), matriks dalam satuan $\beta$ adalah $\begin{pmatrix}1 & 1\\ 1 & 0\end{pmatrix}$. Persamaan karakteristiknya $x(x - 1) - 1 = 0$, sehingga $x = (1 \pm \sqrt5)/2 = 1{,}618$ dan $-0{,}618$. Karena $\beta < 0$, orbital ikatan π adalah $E = \alpha + 1{,}618\beta$ dan π* adalah $E = \alpha - 0{,}618\beta$.

(b) Dari baris kedua, $c_\text{O} = xc_\text{C}$. Untuk π: $c_\text{O}/c_\text{C} = 1{,}618$, dan setelah normalisasi $c_\text{O} = 0{,}851$, $c_\text{C} = 0{,}526$. Untuk π*: $c_\text{O}/c_\text{C} = -0{,}618$, sehingga $c_\text{O} = -0{,}526$, $c_\text{C} = 0{,}851$.

(c) Dua elektron di orbital π: kerapatan π pada O $= 2(0{,}851)^2 = 1{,}447$, pada C $= 0{,}553$. Muatan π: O $-0{,}447$, C $+0{,}447$.

(d) LUMO (π*) 72% berada di karbon ($0{,}851^2$). Nukleofil, yang menyumbangkan pasangan elektron ke LUMO, menyerang **karbon**.

**Memahami hasil.** Matriks 2 × 2 yang sama menjelaskan dua fakta kimia karbonil sekaligus. Orbital terisi condong ke atom yang lebih elektronegatif, sehingga oksigen bermuatan parsial negatif dan gugus C=O sangat polar (momen dipol formaldehida 2,3 D). Orbital kosong condong ke arah sebaliknya, sehingga karbon adalah pusat elektrofilik tempat hidrida, reagen Grignard, dan amina menyerang. Polaritas dan reaktivitas karbonil adalah dua sisi dari pencampuran yang tidak setara, persis seperti Contoh 8.18 untuk ikatan σ H–F.
:::

::: {.contoh}
**Contoh 8.21 · Akar-akar yang menyelang**

Untuk partikel dalam kotak ($L = 1$), pakai basis yang diperbesar bertahap: $f_1 = x(1 - x)$, $f_3 = x(1 - x)(1 - 2x)$, $f_2 = x^2(1 - x)^2$, $f_4 = x^2(1 - x)^2(1 - 2x)$. Akar-akar persamaan sekuler (dihitung dengan Python, dalam satuan $E_1$) adalah:

| Basis | $W_1$ | $W_2$ | $W_3$ | $W_4$ |
|---|---|---|---|---|
| $\{f_1\}$ | 1,0132 | | | |
| $\{f_1, f_3\}$ | 1,0132 | 4,2555 | | |
| $\{f_1, f_2, f_3\}$ | 1,000015 | 4,2555 | 10,348 | |
| $\{f_1, f_2, f_3, f_4\}$ | 1,000015 | 4,0023 | 10,348 | 20,315 |
| eksak | 1 | 4 | 9 | 16 |

Periksa teorema Hylleraas–Undheim–MacDonald (lihat juga Gambar 8.2).

**Penyelesaian.** Setiap akar di atas nilai eksak yang bersesuaian, sesuai (8.19). Ketika $f_2$ ditambahkan ke $\{f_1, f_3\}$, akar-akar lama (1,0132 dan 4,2555) diselang akar-akar baru: $1{,}000015 \le 1{,}0132 \le 4{,}2555 \le 4{,}2555 \le 10{,}348$. Tidak ada akar yang naik.

**Memahami hasil.** Beberapa akar tidak berubah sama sekali ketika satu fungsi ditambahkan, misalnya $W_2 = 4{,}2555$ ketika $f_2$ masuk. Alasannya simetri: $f_2$ genap, sedangkan keadaan kedua ganjil; fungsi genap tidak dapat memperbaiki keadaan ganjil. Matriks $\mathbf H$ dan $\mathbf S$ dalam basis campuran ini terpecah menjadi dua blok yang tidak berhubungan, satu untuk fungsi genap dan satu untuk fungsi ganjil. Pemecahan matriks menjadi blok-blok menurut simetri adalah teknik penghemat kerja yang dipakai di setiap program kimia komputasi; teori grup (Bab 10) adalah cara sistematis untuk menemukannya.
:::

![Gambar 8.2 Teorema Hylleraas–Undheim–MacDonald untuk partikel dalam kotak (Contoh 8.21). Setiap kolom adalah satu basis; garis pendek adalah akar-akar persamaan sekuler, garis putus-putus energi eksak $n^2E_1$. Akar selalu di atas nilai eksak dan turun (atau tetap) ketika basis diperbesar; garis tipis menghubungkan akar yang bersesuaian.](fig/c_macdonald.png){width=72%}

::: {.kuis}
**Kuis cepat 8.4**

(a) Untuk basis tiga fungsi ortonormal, persamaan sekuler adalah polinom berderajat berapa, dan berapa batas atas yang diperoleh sekaligus? (b) Dua orbital setara mempunyai $\alpha = -10$ eV, $\beta = -2$ eV, dan $S = 0$. Berapa energi kedua orbital molekul? (c) Bagaimana jawaban (b) berubah bila $S = 0{,}1$?
:::

## 8.5 Matriks, nilai eigen, diagonalisasi (dengan Python)

### Bentuk matriks persamaan sekuler

Persamaan (8.17) dapat ditulis ringkas sebagai persamaan matriks. Kumpulkan unsur $H_{ik}$ dalam matriks $\mathbf H$ dan $S_{ik}$ dalam matriks $\mathbf S$ (keduanya $n \times n$, simetris), dan koefisien dalam vektor kolom $\mathbf c$. Maka

$$
\mathbf H\mathbf c = W\mathbf S\mathbf c . \qquad \text{(8.25)}
$$

Ini adalah **masalah nilai eigen umum** (*generalized eigenvalue problem*). Ada $n$ penyelesaian; susun vektor-vektor koefisien sebagai kolom-kolom matriks $\mathbf C$ dan akar-akarnya dalam matriks diagonal $\mathbf W$:

$$
\mathbf{HC} = \mathbf{SCW} , \qquad \mathbf C^T\mathbf{SC} = \mathbf 1 . \qquad \text{(8.26)}
$$

Syarat kedua adalah normalisasi dan ortogonalitas fungsi-fungsi hasil: dua fungsi variasi linear yang bersesuaian dengan akar berbeda otomatis ortogonal, sama seperti fungsi eigen operator Hermitian (subbab 4.8). Bila basisnya ortonormal, $\mathbf S = \mathbf 1$ dan (8.26) menjadi masalah nilai eigen biasa $\mathbf{HC} = \mathbf{CW}$, yang dapat ditulis ulang sebagai

$$
\mathbf C^T\mathbf{HC} = \mathbf W . \qquad \text{(8.27)}
$$

Kalimat "mendiagonalkan matriks Hamiltonian" berarti mencari matriks ortogonal $\mathbf C$ yang mengubah $\mathbf H$ menjadi matriks diagonal. Di subbab 4.14 kita sudah melihat bahwa persamaan Schrödinger dalam basis lengkap menjadi persamaan matriks; di sini basisnya berhingga, dan teorema variasi menjamin bahwa hasilnya adalah batas atas.

### Ortogonalisasi Löwdin

Masalah umum (8.26) dapat diubah menjadi masalah biasa dengan mengubah basis menjadi ortonormal. Cara yang paling simetris diusulkan Löwdin (1950): definisikan matriks $\mathbf X = \mathbf S^{-1/2}$. Untuk menghitungnya, diagonalkan dulu $\mathbf S = \mathbf U\mathbf s\mathbf U^T$, dengan $\mathbf s$ diagonal berisi nilai eigen $s_i > 0$, lalu ambil $\mathbf S^{-1/2} = \mathbf U\mathbf s^{-1/2}\mathbf U^T$. Fungsi-fungsi baru $f_i' = \sum_jf_jX_{ji}$ ortonormal, dan Hamiltonian dalam basis baru $\mathbf H' = \mathbf{XHX}$ cukup didiagonalkan biasa:

$$
\mathbf H'\mathbf C' = \mathbf C'\mathbf W , \qquad \mathbf C = \mathbf X\mathbf C' . \qquad \text{(8.28)}
$$

Di antara semua himpunan ortonormal yang dapat dibentuk dari basis asli, fungsi-fungsi Löwdin adalah yang **paling mirip** dengan fungsi asli, sehingga makna "orbital pada atom A" tetap terjaga. Sifat ini dipakai dalam analisis populasi Löwdin (Bab 17).

::: {.awas}
**Basis yang hampir bergantung linear**

Bila dua fungsi basis hampir sama, salah satu nilai eigen $\mathbf S$ mendekati nol, dan $\mathbf S^{-1/2}$ memuat bilangan yang sangat besar. Galat pembulatan di komputer lalu diperbesar, dan energi dapat menjadi tidak masuk akal (bahkan di bawah batas variasi, karena teorema variasi hanya berlaku untuk aritmetika eksak). Ukuran bahayanya adalah **bilangan kondisi** $\mathbf S$, perbandingan nilai eigen terbesar terhadap terkecil. Program kimia komputasi biasanya membuang kombinasi basis yang nilai eigen tumpang tindihnya di bawah sekitar $10^{-6}$.
:::

### Bagaimana komputer mendiagonalkan matriks

Untuk matriks 2 × 2 ortonormal, (8.23) memberi jawabannya langsung: rotasi dengan sudut $\theta$ menghapus unsur di luar diagonal. Algoritme **Jacobi** (1846) mengulangi gagasan ini untuk matriks besar: pilih unsur luar diagonal terbesar, putar pasangan baris dan kolomnya dengan sudut yang menghapusnya, ulangi. Setiap rotasi bisa menghidupkan kembali unsur yang sudah nol, tetapi jumlah kuadrat semua unsur luar diagonal selalu berkurang, sehingga matriks konvergen ke bentuk diagonal. Algoritme modern (reduksi Householder ke bentuk tridiagonal, lalu iterasi QR atau bagi-dan-taklukkan) jauh lebih cepat, tetapi semuanya memerlukan jumlah operasi yang tumbuh seperti $n^3$. Matriks 1000 × 1000 didiagonalkan dalam sepersekian detik di komputer pribadi; matriks interaksi konfigurasi dengan $10^9$ baris memerlukan metode iteratif khusus (Davidson) yang hanya mencari beberapa akar terendah.

Dalam Python, semua ini tersedia dalam satu baris:

```python
import numpy as np
from scipy.linalg import eigh

W, C = np.linalg.eigh(H)     # basis ortonormal: H C = C W
W, C = eigh(H, S)            # basis tak ortogonal: H C = S C W
```

Fungsi `eigh` (untuk matriks simetris atau Hermitian) mengembalikan akar-akar dalam urutan naik dan vektor-vektor koefisien sebagai kolom-kolom `C`, sudah dinormalisasi menurut (8.26).

::: {.contoh}
**Contoh 8.22 · Butadiena dan benzena dalam metode Hückel**

Dalam metode Hückel (Bab 13), orbital π dibangun dari orbital 2p karbon yang dianggap ortonormal, dengan $H_{ii} = \alpha$, $H_{ij} = \beta$ untuk atom bertetangga, dan nol untuk yang lain. Tuliskan $E = \alpha + x\beta$; maka $x$ adalah nilai eigen matriks keterhubungan. Diagonalkan matriks untuk butadiena (rantai empat atom) dan benzena (cincin enam atom) dengan Python, lalu hitung energi delokalisasi.

**Penyelesaian.**

```python
import numpy as np
A = np.diag([1, 1, 1], 1) + np.diag([1, 1, 1], -1)        # butadiena
x, C = np.linalg.eigh(A)
print(x)            # [-1.618 -0.618  0.618  1.618]
print(C[:, 3])      # orbital terendah: [0.372 0.602 0.602 0.372]

B = np.zeros((6, 6))
for i in range(6):                                         # benzena
    B[i, (i + 1) % 6] = B[(i + 1) % 6, i] = 1
print(np.linalg.eigvalsh(B))   # [-2 -1 -1  1  1  2]
```

Karena $\beta < 0$, orbital ikatan adalah yang $x$-nya positif. Butadiena: $E = \alpha + 1{,}618\beta$ dan $\alpha + 0{,}618\beta$ terisi, energi π total $4\alpha + 2(1{,}618 + 0{,}618)\beta = 4\alpha + 4{,}472\beta$. Dua ikatan rangkap terlokalisasi (dua etilena, masing-masing $2\alpha + 2\beta$) memberi $4\alpha + 4\beta$. Energi delokalisasi $0{,}472\beta$. Benzena: $\alpha + 2\beta$ (sekali) dan $\alpha + \beta$ (dua kali) terisi, energi π $6\alpha + 8\beta$, dibandingkan tiga etilena $6\alpha + 6\beta$: energi delokalisasi $2\beta$.

**Memahami hasil.** Dengan $\beta \approx -75$ kJ/mol (nilai empiris dari termokimia), energi delokalisasi benzena sekitar 150 kJ/mol, sesuai orde besaran "energi resonansi" dari kalor hidrogenasi. Pada orbital terendah butadiena, koefisien atom tengah (0,602) lebih besar daripada atom ujung (0,372): ikatan C2–C3 memperoleh sebagian karakter ikatan rangkap. Seluruh teori Hückel di Bab 13 adalah penerapan metode variasi linear dengan basis ortonormal.
:::

::: {.contoh}
**Contoh 8.23 · Atom hidrogen dalam basis Gauss**

Basis Gauss bersimetri bola $f_i = e^{-\alpha_ir^2}$ tidak ortogonal. Integral-integralnya sederhana: dengan $a = \alpha_i + \alpha_j$,

$$
S_{ij} = \left(\frac{\pi}{a}\right)^{3/2}, \qquad T_{ij} = \frac{3\alpha_i\alpha_j}{a}S_{ij} , \qquad V_{ij} = -\frac{2\pi}{a} .
$$

Tulis program yang menyelesaikan $\mathbf{Hc} = W\mathbf{Sc}$ dan mengoptimumkan eksponen-eksponennya untuk $n = 1$ sampai 4.

**Penyelesaian.**

```python
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import minimize

def energi(ln_alfa):
    al = np.exp(ln_alfa)                 # eksponen selalu positif
    a = al[:, None] + al[None, :]
    S = (np.pi/a)**1.5
    H = 3*al[:, None]*al[None, :]/a*S - 2*np.pi/a
    return eigh(H, S, eigvals_only=True)[0]

tebakan = ([0.3], [0.2, 1.3], [0.15, 0.7, 4.0],
           [0.12, 0.45, 2.0, 13.0])
for awal in tebakan:
    r = minimize(energi, np.log(awal), method='BFGS')
    print(len(awal), np.exp(r.x).round(4), round(r.fun, 5))
```

Hasilnya:

| $n$ | Eksponen optimum | $W$ ($E_h$) | Galat (m$E_h$) |
|---|---|---|---|
| 1 | 0,2829 | $-0{,}42441$ | 75,6 |
| 2 | 0,202; 1,33 | $-0{,}48581$ | 14,2 |
| 3 | 0,151; 0,681; 4,50 | $-0{,}49698$ | 3,0 |
| 4 | 0,122; 0,445; 1,97; 13,0 | $-0{,}49928$ | 0,72 |

**Memahami hasil.** Setiap fungsi Gauss tambahan memperkecil galat empat sampai lima kali. Eksponen-eksponen optimum membentuk deret yang hampir geometris (perbandingan berurutan sekitar 3,6–6,6): fungsi sempit untuk daerah dekat inti, fungsi lebar untuk ekor. Gagasan ini dipakai dalam basis **bertempera rata** (*even-tempered*), $\alpha_k = \alpha_0\beta^k$, yang hanya memerlukan dua parameter berapa pun banyaknya fungsi. Dengan enam fungsi Gauss teroptimum, galatnya tinggal 0,054 m$E_h$; kerapatan di inti naik dari 0,076 ($n = 1$) menjadi 0,299, tetapi masih 6% di bawah nilai eksak $1/\pi = 0{,}318$, karena tidak ada kombinasi berhingga fungsi Gauss yang dapat membentuk puncak lancip $e^{-r}$. Basis STO-3G yang terkenal adalah tiga fungsi Gauss dengan koefisien tetap yang dicocokkan pada orbital Slater; untuk atom hidrogen ($\zeta = 1$) energinya $-0{,}49491\ E_h$.
:::

![Gambar 8.3 Atom hidrogen dalam basis Gauss teroptimum. Kiri: fungsi gelombang $\psi(r)$ untuk basis 1, 2, dan 3 fungsi Gauss dibandingkan dengan fungsi eksak $e^{-r}/\sqrt\pi$; perbedaan terbesar di dekat inti. Kanan: galat energi terhadap jumlah fungsi basis (skala logaritma), untuk eksponen yang dioptimumkan bebas dan untuk basis bertempera rata.](fig/c_gauss.png){width=92%}

::: {.contoh}
**Contoh 8.24 · Osilator anharmonik dalam basis osilator harmonik**

Hamiltonian $\hat H = -\tfrac12d^2/dx^2 + \tfrac12x^2 + \lambda x^4$ dengan $\lambda = 0{,}1$ dapat ditulis dalam basis fungsi eigen osilator harmonik $|v\rangle$, yang ortonormal. Unsur matriks $x$ adalah $\langle v + 1|x|v\rangle = \sqrt{(v + 1)/2}$ (subbab 5.6), sehingga matriks $x^4$ dapat dihitung sebagai pangkat empat matriks $x$ (dengan basis yang sedikit lebih besar agar unsur di tepi benar). Hitung tiga energi terendah untuk ukuran basis $N = 1, 3, 6, 10, 20$.

**Penyelesaian.**

| $N$ | $W_1$ | $W_2$ | $W_3$ |
|---|---|---|---|
| 1 | 0,575000 | | |
| 3 | 0,559565 | 1,875000 | 3,490435 |
| 6 | 0,559386 | 1,770324 | 3,154777 |
| 10 | 0,559147 | 1,769516 | 3,139410 |
| 20 | 0,559146 | 1,769503 | 3,138624 |

Basis $N = 40$ tidak mengubah enam angka penting pertama dari baris $N = 20$, jadi energi-energi itu dapat dianggap eksak.

**Memahami hasil.** Dengan satu fungsi basis ($N = 1$), $W_1 = \langle 0|\hat H|0\rangle = \tfrac12 + 3\lambda/4$: ini persis energi perturbasi orde pertama (subbab 8.6), yang merupakan rata-rata gangguan dalam keadaan tak terganggu. Basis yang lebih besar memungkinkan fungsi gelombang menyesuaikan diri, dan energi turun ke nilai eksak. Konvergensi keadaan tereksitasi lebih lambat, karena keadaan itu lebih luas dan memerlukan lebih banyak fungsi basis. Metode ini, interaksi konfigurasi getaran (VCI), dipakai untuk menghitung spektrum inframerah molekul kecil dengan ketelitian di bawah 1 cm⁻¹, termasuk nada atas dan pita kombinasi yang berada di luar jangkauan model harmonik.
:::

::: {.contoh}
**Contoh 8.25 · Ortogonalisasi Löwdin untuk dua fungsi**

Dua fungsi ternormalisasi mempunyai tumpang tindih $S = 0{,}50$. (a) Hitung $\mathbf S^{-1/2}$. (b) Tuliskan fungsi-fungsi Löwdin dan periksa ortonormalitasnya.

**Penyelesaian.** (a) $\mathbf S = \begin{pmatrix}1 & 0{,}5\\ 0{,}5 & 1\end{pmatrix}$ mempunyai nilai eigen $1{,}5$ dan $0{,}5$ dengan vektor eigen $(1, 1)/\sqrt2$ dan $(1, -1)/\sqrt2$. Dengan $a = 1{,}5^{-1/2} = 0{,}8165$ dan $b = 0{,}5^{-1/2} = 1{,}4142$:

$$
\mathbf S^{-1/2} = \frac12\begin{pmatrix} a + b & a - b\\ a - b & a + b\end{pmatrix} = \begin{pmatrix} 1{,}1154 & -0{,}2989\\ -0{,}2989 & 1{,}1154\end{pmatrix} .
$$

(b) $f_1' = 1{,}1154f_1 - 0{,}2989f_2$ dan $f_2' = -0{,}2989f_1 + 1{,}1154f_2$. Periksa: $\langle f_1'|f_1'\rangle = 1{,}1154^2 + 0{,}2989^2 - 2(1{,}1154)(0{,}2989)(0{,}5) = 1{,}2441 + 0{,}0893 - 0{,}3334 = 1{,}000$; $\langle f_1'|f_2'\rangle = -2(1{,}1154)(0{,}2989) + (1{,}1154^2 + 0{,}2989^2)(0{,}5) = -0{,}6668 + 0{,}6667 = 0{,}000$.

**Memahami hasil.** Setiap fungsi Löwdin masih didominasi fungsi aslinya (koefisien 1,12) dan hanya "mengurangkan" sedikit fungsi tetangganya untuk menghapus tumpang tindih. Bandingkan dengan ortogonalisasi Gram–Schmidt, yang membiarkan $f_1$ utuh lalu mengubah $f_2$ saja; cara itu tidak simetris, sehingga dua atom yang setara mendapat perlakuan berbeda. Dalam metode Hückel, mengabaikan tumpang tindih dapat ditafsirkan sebagai bekerja dalam basis Löwdin yang sudah ortogonal.
:::

::: {.contoh}
**Contoh 8.26 · Sumur ganda: penerobosan dari diagonalisasi**

Model satu dimensi untuk inversi amonia (subbab 3.12): partikel dalam kotak ($L = 1$, $\hbar = m = 1$) dengan penghalang persegi setinggi $V_0$ dan selebar 0,2 di tengah. Dalam basis 80 fungsi kotak $\sqrt2\sin(n\pi x)$, unsur matriks penghalang dihitung dengan integrasi numerik, lalu matriksnya didiagonalkan. Hasil untuk dua tingkat terendah:

| $V_0$ | $E_1$ | $E_2$ | $E_2 - E_1$ |
|---|---|---|---|
| 0 | 4,935 | 19,739 | 14,80 |
| 100 | 21,055 | 22,937 | 1,882 |
| 200 | 24,016 | 24,488 | 0,472 |
| 400 | 25,956 | 26,024 | 0,0685 |

Tafsirkan hasilnya.

**Penyelesaian.** Penghalang menaikkan kedua tingkat, tetapi tingkat pertama (genap, tanpa simpul) naik jauh lebih banyak, karena fungsi genap besar di tengah, tempat penghalang berada; fungsi ganjil sudah mempunyai simpul di sana. Kedua tingkat mendekat membentuk **doblet penerobosan**. Setiap kali $V_0$ dilipatduakan, pemisahannya turun empat sampai tujuh kali, dan perbandingan itu sendiri makin besar: ciri peluruhan eksponensial terhadap $\sqrt{V_0}$, seperti peluang penerobosan di subbab 3.11.

**Memahami hasil.** Fungsi gelombang kedua tingkat adalah kombinasi genap dan ganjil dari "partikel di sumur kiri" dan "partikel di sumur kanan", tepat seperti (8.21) dengan $S \approx 0$. Pada amonia, kedua sumur adalah dua bentuk piramida yang saling bercermin, penghalangnya adalah bentuk datar (sekitar 2000 cm⁻¹), dan pemisahan doblet keadaan dasar 0,79 cm⁻¹ adalah frekuensi maser amonia yang pertama (24 GHz). Diagonalisasi menghasilkan pemisahan penerobosan tanpa perlu menghitung peluang tembus secara terpisah.
:::

::: {.contoh}
**Contoh 8.27 · Interaksi konfigurasi radial untuk helium**

Perluas fungsi dua eksponen (Contoh 8.14) menjadi basis linear: pilih $n$ eksponen $\zeta_k = \zeta_0\beta^k$ (bertempera rata), dan bentuk semua fungsi dua elektron simetris $e^{-\zeta_ir_1}e^{-\zeta_jr_2} + e^{-\zeta_jr_1}e^{-\zeta_ir_2}$ dengan $i \le j$. Ada $n(n + 1)/2$ fungsi. Semua unsur matriks adalah gabungan integral di Contoh 8.14. Hitung energi terendah untuk $n = 2$, 4, dan 6, dengan $\zeta_0$ dan $\beta$ yang dioptimumkan, dan bandingkan dengan batas Hartree–Fock $-2{,}86168\ E_h$ dan energi eksak $-2{,}90372\ E_h$.

**Penyelesaian.**

```python
import numpy as np
S = lambda a, b: 8*np.pi/(a + b)**3        # seperti Contoh 8.14
h = lambda a, b: (-0.5*(b*b*S(a, b) - 8*np.pi*b/(a + b)**2)
                  - 8*np.pi/(a + b)**2)
J = lambda p, q: (32*np.pi**2*(p*p + 3*p*q + q*q)
                  /(p*p*q*q*(p + q)**3))

def ci_radial(z):
    m = len(z)
    pas = [(z[i], z[j]) for i in range(m) for j in range(i, m)]
    n = len(pas); H = np.zeros((n, n)); M = np.zeros((n, n))
    for I, (a, b) in enumerate(pas):
        for K, (c, d) in enumerate(pas):
            for p, q in ((a, b), (b, a)):     # simetrisasi
                for r, s in ((c, d), (d, c)):
                    H[I, K] += (h(p, r)*S(q, s) + S(p, r)*h(q, s)
                                + J(p + r, q + s))
                    M[I, K] += S(p, r)*S(q, s)
    s, U = np.linalg.eigh(M)                # ortogonalisasi kanonik
    pakai = s > 1e-10*s.max()
    X = U[:, pakai]/np.sqrt(s[pakai])
    return np.linalg.eigvalsh(X.T @ H @ X)[0]

for n, z0, beta in ((2, 1.3252, 1.8541), (4, 1.4021, 1.5335),
                    (6, 1.3853, 1.4190)):
    print(n, round(ci_radial(z0*beta**np.arange(n)), 5))
```

| $n$ | Jumlah fungsi | $E$ ($E_h$) |
|---|---|---|
| 1 | 1 | $-2{,}84766$ |
| 2 | 3 | $-2{,}87689$ |
| 4 | 10 | $-2{,}87886$ |
| 6 | 21 | $-2{,}87899$ |

**Memahami hasil.** Energi turun monoton dan konvergen ke sekitar $-2{,}8790\ E_h$, yaitu **batas-s**: energi terbaik yang dapat dicapai fungsi yang hanya memuat orbital s. Batas ini $0{,}0173\ E_h$ di bawah Hartree–Fock, tetapi masih $0{,}0247\ E_h$ di atas nilai eksak. Fungsi berbasis orbital s hanya dapat menggambarkan korelasi **radial** (satu elektron dekat inti, yang lain jauh); untuk korelasi **sudut** (kedua elektron di sisi berlawanan inti), konfigurasi seperti $2p^2$ dan $3d^2$ harus ditambahkan. Ternyata korelasi sudut lebih besar daripada korelasi radial. Inilah alasan program kimia komputasi memerlukan fungsi polarisasi (p untuk hidrogen, d untuk karbon) agar energi korelasi dapat dihitung dengan baik (subbab 17.5). Perhatikan pula baris ortogonalisasi kanonik: dengan eksponen yang berdekatan, matriks tumpang tindih hampir singular, persis bahaya yang diperingatkan kotak di atas.
:::

::: {.terapan}
**Semua program kimia kuantum adalah pendiagonal matriks**

Program Hartree–Fock membangun matriks Fock dalam basis Gauss lalu menyelesaikan $\mathbf{FC} = \mathbf{SC\varepsilon}$, persis (8.26), berulang-ulang sampai konsisten diri (subbab 17.3). Program interaksi konfigurasi membangun matriks Hamiltonian dalam basis determinan Slater lalu mencari akar-akar terendahnya. Program dinamika getaran membangun matriks dalam basis osilator, seperti Contoh 8.24. Perbedaan antarprogram terutama terletak pada pilihan basis, cara menghitung unsur matriks, dan trik untuk menangani matriks yang sangat besar. Inti matematikanya adalah persamaan sekuler (8.18).
:::

::: {.kuis}
**Kuis cepat 8.5**

(a) Mengapa `eigh` dan bukan `eig` yang dipakai untuk matriks Hamiltonian? (b) Bila matriks tumpang tindih mempunyai nilai eigen $10^{-9}$, apa yang sebaiknya dilakukan? (c) Berapa kali lebih lama, kira-kira, mendiagonalkan matriks 2000 × 2000 dibandingkan 1000 × 1000?
:::

