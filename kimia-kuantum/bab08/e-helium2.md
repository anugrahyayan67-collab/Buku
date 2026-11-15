## 8.8 Helium: perturbasi vs variasi

### Helium sebagai masalah perturbasi

Atom helium adalah batu uji yang ideal untuk membandingkan kedua metode, karena energi eksaknya diketahui sangat teliti. Dalam bahasa perturbasi, pilihan alaminya adalah

$$
\hat H^{(0)} = \left(-\tfrac12\nabla_1^2 - \frac{Z}{r_1}\right) + \left(-\tfrac12\nabla_2^2 - \frac{Z}{r_2}\right) , \qquad \hat H' = \frac{1}{r_{12}} .
$$

$\hat H^{(0)}$ adalah dua ion He⁺ yang tidak saling melihat. Keadaan dasarnya $\psi^{(0)} = 1s(1)1s(2)$ dengan eksponen $Z$, dan energinya $E^{(0)} = 2(-Z^2/2) = -Z^2$. Koreksi orde pertama adalah tolakan rata-rata dalam keadaan itu, yang sudah kita hitung (8.10) dengan $\zeta = Z$:

$$
E^{(1)} = \left\langle 1s^2\left|\frac{1}{r_{12}}\right|1s^2\right\rangle = \frac58Z . \qquad \text{(8.38)}
$$

Untuk helium, $E^{(0)} + E^{(1)} = -4 + 1{,}25 = -2{,}75\ E_h = -74{,}83$ eV, terlalu tinggi $0{,}154\ E_h$ (4,2 eV).

### Deret $1/Z$

Ada cara elegan untuk melihat struktur seluruh deret perturbasi helium. Ubah skala koordinat dengan $\boldsymbol\rho = Z\mathbf r$. Karena $\nabla^2$ berskala $Z^2$ dan $1/r$ berskala $Z$,

$$
\hat H = Z^2\left[\left(-\tfrac12\nabla_{\rho_1}^2 - \frac{1}{\rho_1}\right) + \left(-\tfrac12\nabla_{\rho_2}^2 - \frac{1}{\rho_2}\right) + \frac1Z\cdot\frac{1}{\rho_{12}}\right] .
$$

Dalam kurung siku, perturbasinya dikalikan $1/Z$: bilangan $1/Z$ berperan sebagai parameter $\lambda$! Jadi energinya berbentuk $Z^2(\varepsilon_0 + \varepsilon_1/Z + \varepsilon_2/Z^2 + \cdots)$, atau

$$
E = -Z^2 + \frac58Z + \varepsilon_2 + \frac{\varepsilon_3}{Z} + \frac{\varepsilon_4}{Z^2} + \cdots \qquad \text{(8.39)}
$$

dengan koefisien $\varepsilon_k$ yang **sama untuk semua ion mirip helium**. Koreksi orde kedua tidak bergantung pada $Z$, orde ketiga turun seperti $1/Z$, dan seterusnya. Makin besar muatan inti, makin kecil peran tolakan antarelektron relatif terhadap tarikan inti, dan makin cepat deretnya konvergen.

Menghitung $\varepsilon_2$ tidak mudah, karena jumlah (8.35) melibatkan semua keadaan tereksitasi ganda dan kontinu dua elektron. Hylleraas (1930) menghindarinya dengan prinsip variasi khusus untuk fungsi orde pertama: untuk keadaan dasar, fungsional

$$
J[\tilde\psi^{(1)}] = \langle\tilde\psi^{(1)}|\hat H^{(0)} - E^{(0)}|\tilde\psi^{(1)}\rangle + 2\langle\tilde\psi^{(1)}|\hat H' - E^{(1)}|\psi^{(0)}\rangle
$$

selalu lebih besar atau sama dengan $E^{(2)}$, dan sama bila fungsi uji $\tilde\psi^{(1)}$ tepat sama dengan $\psi^{(1)}$. Dengan fungsi uji yang makin lentur, Hylleraas dan para penerusnya memperoleh $\varepsilon_2 = -0{,}157\,666$. Koefisien-koefisien berikutnya: $\varepsilon_3 = +0{,}008\,699$, $\varepsilon_4 = -0{,}000\,889$, $\varepsilon_5 = -0{,}001\,036$, $\varepsilon_6 = -0{,}000\,613$.

### Mengapa variasi unggul pada orde rendah

Bandingkan (8.11) dengan (8.38): integral variasi pada $\zeta = Z$ adalah $W(Z) = Z^2 - 2Z^2 + \tfrac58Z = -Z^2 + \tfrac58Z$, **tepat** $E^{(0)} + E^{(1)}$. Teori perturbasi orde pertama tidak lain adalah metode variasi dengan fungsi uji yang tidak dioptimumkan. Karena metode variasi mencari minimum, hasilnya pasti tidak lebih buruk. Menguraikan (8.13),

$$
W_\text{min} = -\left(Z - \frac{5}{16}\right)^2 = -Z^2 + \frac58Z - \frac{25}{256} , \qquad \text{(8.40)}
$$

terlihat bahwa optimasi eksponen menambahkan suku tetap $-25/256 = -0{,}0977$, yang meniru suku orde kedua $\varepsilon_2 = -0{,}1577$ dan menangkap 62% darinya. Bagian ini adalah **relaksasi orbital**: orbital mengembang karena perisai. Sisanya, 38%, berasal dari korelasi elektron yang tidak dapat digambarkan oleh fungsi hasil kali apa pun.

Pelajarannya umum. Bila gangguan mengubah ukuran atau bentuk orbital, metode variasi dengan parameter yang tepat menangkap perubahan itu secara langsung, sedangkan perturbasi memerlukan orde kedua (yang melibatkan banyak keadaan tereksitasi) untuk mencapainya. Sebaliknya, teori perturbasi memberi struktur deret (8.39) yang menunjukkan dengan jelas bagaimana energi bergantung pada $Z$, dan orde keduanya (bila dapat dihitung) mengalahkan fungsi variasi sederhana.

::: {.inti}
**Helium: dua jalan, satu jawaban**

| Metode | Energi helium | Galat |
|---|---|---|
| Orde nol, $-Z^2$ | $-4{,}0000\ E_h$ | 38% |
| Orde pertama, $-Z^2 + \tfrac58Z$ | $-2{,}7500\ E_h$ | 5,3% |
| Variasi, $-(Z - \tfrac{5}{16})^2$ | $-2{,}8477\ E_h$ | 1,9% |
| Orde kedua, $+\varepsilon_2$ | $-2{,}9077\ E_h$ | $-0{,}14$% |
| Eksak | $-2{,}9037\ E_h$ | |

Orde pertama adalah variasi tanpa optimasi. Optimasi eksponen meniru 62% suku orde kedua.
:::

::: {.contoh}
**Contoh 8.38 · Menjumlahkan deret $1/Z$ untuk helium**

Dengan koefisien di atas, jumlahkan deret (8.39) untuk $Z = 2$ orde demi orde dan bandingkan dengan nilai eksak $-2{,}903\,724\ E_h$.

**Penyelesaian.**

| Orde $k$ | Suku $\varepsilon_kZ^{2-k}$ | Jumlah ($E_h$) | Galat ($E_h$) |
|---|---|---|---|
| 0 | $-4$ | $-4{,}000\,000$ | $-1{,}096$ |
| 1 | $+1{,}25$ | $-2{,}750\,000$ | $+0{,}1537$ |
| 2 | $-0{,}157\,666$ | $-2{,}907\,666$ | $-0{,}003\,94$ |
| 3 | $+0{,}004\,350$ | $-2{,}903\,317$ | $+0{,}000\,41$ |
| 4 | $-0{,}000\,222$ | $-2{,}903\,539$ | $+0{,}000\,19$ |
| 5 | $-0{,}000\,130$ | $-2{,}903\,669$ | $+0{,}000\,056$ |
| 6 | $-0{,}000\,038$ | $-2{,}903\,707$ | $+0{,}000\,017$ |

**Memahami hasil.** Berbeda dengan osilator kuartik (Contoh 8.35), deret helium konvergen dengan baik: setiap orde memperkecil galat. Perhatikan bahwa jumlah orde kedua ($-2{,}9077$) **di bawah** energi eksak. Ini bukan pelanggaran teorema variasi, karena teori perturbasi bukan metode variasi; energi perturbasi dapat jatuh di kedua sisi nilai eksak. Pada orde keenam, galatnya tinggal $1{,}7 \times 10^{-5}\ E_h$, sekitar 0,05 kJ/mol.
:::

::: {.contoh}
**Contoh 8.39 · Fungsi orde pertama dan relaksasi orbital**

Tunjukkan bahwa perubahan kecil eksponen dari $Z$ ke $Z - \delta$ pada fungsi $1s(1)1s(2)$ setara dengan menambahkan koreksi fungsi gelombang orde pertama yang mencampurkan keadaan-keadaan tereksitasi $ns$. Gunakan untuk menafsirkan suku $-25/256$ di (8.40).

**Penyelesaian.** Untuk satu orbital, $e^{-(Z - \delta)r} = e^{-Zr}e^{\delta r} \approx e^{-Zr}(1 + \delta r)$. Fungsi $re^{-Zr}$ dapat diuraikan dalam orbital-orbital $ns$ ion He⁺ (dan kontinu $s$), karena bersimetri bola. Jadi mengubah eksponen sama dengan mencampurkan keadaan tereksitasi tunggal $1s\,ns$ dengan koefisien sebanding $\delta$. Pada fungsi dua elektron, kedua orbital berubah, sehingga terjadi campuran $1s\,ns$ untuk masing-masing elektron. Energinya berubah pada orde $\delta^2$ (sesuai (8.5)), dan (8.40) menunjukkan bahwa pilihan terbaik $\delta = 5/16$ menurunkan energi sebesar $\delta^2 = 25/256$.

**Memahami hasil.** Teori perturbasi orde kedua untuk helium memuat tiga jenis sumbangan: eksitasi tunggal $1s \to ns$ (relaksasi orbital, yang diwakili oleh perubahan eksponen), eksitasi ganda $1s^2 \to n\ell\,n'\ell$ dengan $\ell \ge 1$ (korelasi sudut: kedua elektron cenderung berada di sisi berlawanan dari inti), dan eksitasi ganda $1s^2 \to ns\,n's$ (korelasi radial: satu dekat, satu jauh). Fungsi satu eksponen hanya memuat jenis pertama; fungsi dua eksponen (Contoh 8.14) menambahkan sebagian jenis ketiga; fungsi Hylleraas yang memuat $r_{12}$ memuat ketiganya.
:::

::: {.contoh}
**Contoh 8.40 · Deret isoelektron: perturbasi orde kedua**

Hitung $E^{(0)} + E^{(1)} + E^{(2)} = -Z^2 + \tfrac58Z - 0{,}157\,666$ untuk H⁻, He, Li⁺, Be²⁺, dan B³⁺, lalu bandingkan galatnya dengan galat metode variasi satu eksponen (Contoh 8.13). Apa yang dikatakan hasil orde kedua tentang H⁻?

**Penyelesaian.**

| Ion | Orde kedua ($E_h$) | Eksak ($E_h$) | Galat orde kedua | Galat variasi |
|---|---|---|---|---|
| H⁻ | $-0{,}53267$ | $-0{,}52775$ | $-0{,}0049$ | $+0{,}0551$ |
| He | $-2{,}90767$ | $-2{,}90372$ | $-0{,}0039$ | $+0{,}0561$ |
| Li⁺ | $-7{,}28267$ | $-7{,}27991$ | $-0{,}0028$ | $+0{,}0573$ |
| Be²⁺ | $-13{,}65767$ | $-13{,}65557$ | $-0{,}0021$ | $+0{,}0579$ |
| B³⁺ | $-22{,}03267$ | $-22{,}03097$ | $-0{,}0017$ | $+0{,}0583$ |

Untuk H⁻, energi orde kedua $-0{,}5327\ E_h$ di bawah $-0{,}5\ E_h$, sehingga meramalkan ion yang terikat.

**Memahami hasil.** Galat orde kedua sekitar sepuluh kali lebih kecil daripada galat variasi satu eksponen dan mengecil seperti $1/Z$, sesuai suku $\varepsilon_3/Z$ yang terabaikan. Untuk H⁻ ramalannya benar (ion terikat), tetapi teori perturbasi tidak dapat **membuktikan** keterikatan, karena energinya bukan batas atas: galat $-0{,}0049\ E_h$ bisa saja lebih besar daripada selisih $0{,}033\ E_h$ di bawah ambang. Bukti keterikatan H⁻ datang dari metode variasi (Contoh 8.14). Kedua metode saling melengkapi: perturbasi untuk ketelitian, variasi untuk kepastian arah galat.
:::

![Gambar 8.6 Galat energi keadaan dasar ion mirip helium ($Z = 1$ sampai 6) untuk tiga metode: perturbasi orde pertama, variasi dengan muatan efektif, dan perturbasi orde kedua. Galat dua metode pertama hampir tidak bergantung pada $Z$; galat orde kedua kecil, bertanda negatif (energi di bawah nilai eksak), dan mengecil seperti $1/Z$. Garis putus-putus: energi korelasi (selisih Hartree–Fock dan eksak), batas yang tidak dapat dilampaui oleh fungsi hasil kali orbital mana pun.](fig/c_isoelektron.png){width=78%}

::: {.contoh}
**Contoh 8.41 · Energi ionisasi ion mirip helium**

Energi ionisasi ion mirip helium ($\text{X}^{(Z-2)+} \to \text{X}^{(Z-1)+} + e^-$) adalah $I = -Z^2/2 - E$. (a) Tuliskan $I$ menurut deret (8.39) sampai orde kedua. (b) Hitung untuk Li⁺, Be²⁺, dan C⁴⁺ dan bandingkan dengan nilai eksak 75,645; 153,896; dan 392,014 eV. (c) Bandingkan dengan ramalan variasi.

**Penyelesaian.** (a) $I \approx Z^2/2 - \tfrac58Z + 0{,}157\,666$ (dalam $E_h$).

(b) Li⁺ ($Z = 3$): $4{,}5 - 1{,}875 + 0{,}1577 = 2{,}7827\ E_h = 75{,}72$ eV. Be²⁺: $8 - 2{,}5 + 0{,}1577 = 5{,}6577\ E_h = 153{,}95$ eV. C⁴⁺: $18 - 3{,}75 + 0{,}1577 = 14{,}4077\ E_h = 392{,}05$ eV. Galatnya 0,07; 0,06; dan 0,04 eV.

(c) Variasi: $I = Z^2/2 - (Z - \tfrac{5}{16})^2$, memberi 74,09; 152,32; dan 390,42 eV, terlalu rendah sekitar 1,6 eV untuk semua ion.

**Memahami hasil.** Energi ionisasi ion mirip helium tumbuh hampir seperti $Z^2/2$, dikurangi suku linear $\tfrac58Z$ yang mencerminkan tolakan antarelektron. Hubungan ini, yang dapat diuji dengan spektroskopi sinar-X lunak pada plasma panas, adalah bentuk modern hukum Moseley. Galat variasi yang hampir tetap (1,6 eV) mencerminkan energi korelasi yang hampir tidak bergantung pada $Z$, seperti terlihat pada Gambar 8.6.
:::

::: {.terapan}
**Teori perturbasi Møller–Plesset**

Untuk molekul, Møller dan Plesset (1934) memilih $\hat H^{(0)}$ sebagai jumlah operator Fock satu elektron (Hamiltonian Hartree–Fock, subbab 9.8 dan 17.2), sehingga $E^{(0)} + E^{(1)}$ sama dengan energi Hartree–Fock. Koreksi orde kedua, **MP2**, adalah jumlah atas eksitasi ganda dari orbital terisi $i, j$ ke orbital kosong $a, b$:

$$
E_\text{MP2} = -\sum_{i<j}\sum_{a<b}\frac{|\langle ij\|ab\rangle|^2}{\varepsilon_a + \varepsilon_b - \varepsilon_i - \varepsilon_j} ,
$$

persis bentuk (8.35) dengan penyebut berupa selisih energi orbital. Untuk helium dengan basis yang sangat besar, MP2 memulihkan sekitar 0,037 dari $0{,}042\ E_h$ energi korelasi, hampir 90%. MP2 adalah metode korelasi termurah yang memperhitungkan gaya dispersi London, sehingga dipakai luas untuk interaksi antarmolekul (subbab 17.11).
:::

::: {.kuis}
**Kuis cepat 8.8**

(a) Mengapa koefisien $\varepsilon_2$ deret helium sama untuk semua ion mirip helium? (b) Energi perturbasi orde kedua helium di bawah nilai eksak. Apakah ini masalah? (c) Berapa persen $\varepsilon_2$ yang ditangkap oleh optimasi eksponen, dan mengapa tidak 100%?
:::

## 8.9 Perturbasi tingkat terdegenerasi; keadaan tereksitasi helium

### Masalah degenerasi

Rumus (8.34) dan (8.35) mempunyai penyebut $E_n^{(0)} - E_m^{(0)}$. Bila tingkat $n$ terdegenerasi, ada keadaan $m$ dengan penyebut nol, dan rumus-rumus itu meledak, kecuali $H'_{mn}$ kebetulan nol. Penyebabnya lebih dalam daripada sekadar soal aljabar. Bila $d$ fungsi $\psi_1^{(0)}, \ldots, \psi_d^{(0)}$ mempunyai energi tak terganggu yang sama, maka **setiap** kombinasi linearnya juga fungsi eigen $\hat H^{(0)}$ dengan energi itu. Kita tidak tahu kombinasi mana yang akan "dipilih" oleh perturbasi. Ketika $\lambda$ naik dari nol, setiap keadaan yang sebenarnya berubah secara malar menjadi fungsi tertentu di dalam ruang terdegenerasi itu, yaitu **fungsi orde nol yang benar**. Tugas pertama teori perturbasi terdegenerasi adalah menemukannya.

### Penurunan

Tulis fungsi orde nol yang benar sebagai kombinasi yang belum diketahui,

$$
\phi^{(0)} = \sum_{j=1}^dc_j\psi_j^{(0)} ,
$$

dan masukkan ke persamaan orde pertama (8.31) dengan $\psi_n^{(0)}$ diganti $\phi^{(0)}$:

$$
\left(\hat H^{(0)} - E^{(0)}\right)\psi^{(1)} = \left(E^{(1)} - \hat H'\right)\sum_jc_j\psi_j^{(0)} .
$$

Kalikan dari kiri dengan $\psi_i^{(0)*}$ untuk salah satu fungsi dalam himpunan terdegenerasi, dan integralkan. Ruas kiri nol (karena $\psi_i^{(0)}$ adalah fungsi eigen $\hat H^{(0)}$ dengan nilai eigen $E^{(0)}$ yang sama). Dengan fungsi-fungsi terdegenerasi yang ortonormal, ruas kanan memberi

$$
\sum_{j=1}^d\left(H'_{ij} - E^{(1)}\delta_{ij}\right)c_j = 0 , \qquad i = 1, \ldots, d , \qquad \text{(8.41)}
$$

dan penyelesaian tak trivial mensyaratkan

$$
\det\left(H'_{ij} - E^{(1)}\delta_{ij}\right) = 0 . \qquad \text{(8.42)}
$$

Ini adalah persamaan sekuler berukuran $d \times d$, yang hanya melibatkan unsur matriks perturbasi **di dalam** ruang terdegenerasi. Akar-akarnya $E_1^{(1)}, \ldots, E_d^{(1)}$ adalah koreksi energi orde pertama untuk $d$ keadaan yang berasal dari tingkat itu, dan vektor-vektor eigennya memberi fungsi orde nol yang benar. Bila akar-akarnya berbeda, degenerasi **pecah** seluruhnya; bila sebagian akar sama, degenerasi pecah sebagian. Fungsi-fungsi orde nol yang benar adalah fungsi-fungsi yang membuat matriks $H'_{ij}$ diagonal di dalam ruang terdegenerasi; setelah fungsi itu ditemukan, rumus tak terdegenerasi dapat dipakai untuk orde berikutnya dengan keadaan-keadaan di luar ruang itu.

Perhatikan kemiripannya dengan variasi linear (8.18): perturbasi terdegenerasi orde pertama adalah metode variasi linear dengan basis berupa fungsi-fungsi terdegenerasi. Di dalam ruang itu $\hat H^{(0)}$ hanya menambahkan tetapan $E^{(0)}$ pada diagonal, sehingga yang perlu didiagonalkan hanya $\hat H'$.

### Simetri sebagai jalan pintas

Bila ada operator $\hat A$ yang komut dengan $\hat H^{(0)}$ maupun $\hat H'$, dan fungsi-fungsi terdegenerasi dipilih sebagai fungsi eigen $\hat A$ dengan nilai eigen berbeda, maka unsur $H'_{ij}$ di antara fungsi-fungsi dengan nilai eigen $\hat A$ berbeda nol (subbab 4.10). Matriksnya sudah diagonal, atau terpecah menjadi blok-blok kecil. Dalam atom, operator itu biasanya momentum sudut; dalam molekul, operasi simetri (Bab 10). Contoh-contoh berikut memperlihatkan bagaimana pilihan basis yang cerdas mengubah determinan besar menjadi beberapa matriks 2 × 2.

::: {.inti}
**Perturbasi terdegenerasi**

Diagonalkan matriks perturbasi $H'_{ij}$ di dalam ruang terdegenerasi:

$$
\det\left(H'_{ij} - E^{(1)}\delta_{ij}\right) = 0 .
$$

Akar-akarnya adalah pemecahan tingkat pada orde pertama; vektor eigennya adalah fungsi orde nol yang benar. Simetri yang dimiliki bersama oleh $\hat H^{(0)}$ dan $\hat H'$ menentukan fungsi-fungsi itu sebelum perhitungan dimulai.
:::

::: {.contoh}
**Contoh 8.42 · Cincin yang dipipihkan**

Partikel pada cincin (subbab 6.3) mempunyai tingkat terdegenerasi ganda $E_m = m^2\hbar^2/2I$ untuk $m = \pm1, \pm2, \ldots$, dengan fungsi $e^{im\phi}/\sqrt{2\pi}$. Cincin dipipihkan sedikit menjadi elips, yang dimodelkan dengan $\hat H' = V_0\cos2\phi$. (a) Hitung matriks $\hat H'$ dalam ruang $m = \pm1$. (b) Tentukan pemecahan dan fungsi orde nol yang benar. (c) Apakah tingkat $m = \pm2$ pecah pada orde pertama?

**Penyelesaian.** (a) Tulis $\cos2\phi = \tfrac12(e^{2i\phi} + e^{-2i\phi})$. Unsur diagonal: $\langle\pm1|\cos2\phi|\pm1\rangle = \tfrac{1}{2\pi}\int_0^{2\pi}\cos2\phi\,d\phi = 0$. Unsur luar diagonal: $\langle +1|\hat H'|-1\rangle = \tfrac{V_0}{2\pi}\int_0^{2\pi}e^{-i\phi}\cdot\tfrac12(e^{2i\phi} + e^{-2i\phi})e^{-i\phi}d\phi = \tfrac{V_0}{2}$, karena hanya suku $e^{2i\phi}$ yang menghapus $e^{-2i\phi}$. Jadi matriksnya $\begin{pmatrix}0 & V_0/2\\ V_0/2 & 0\end{pmatrix}$.

(b) Akar $E^{(1)} = \pm V_0/2$, dengan vektor eigen $(1, 1)/\sqrt2$ dan $(1, -1)/\sqrt2$, yaitu $\cos\phi/\sqrt\pi$ (energi $+V_0/2$) dan $\sin\phi/\sqrt\pi$ (energi $-V_0/2$).

(c) Untuk $m = \pm2$, unsur luar diagonal memerlukan $e^{4i\phi}$, yang tidak ada di $\cos2\phi$; unsur diagonal juga nol. Pemecahannya baru muncul pada orde kedua.

**Memahami hasil.** Gangguan yang tadinya "tidak membedakan" arah putaran memilih dua gelombang berdiri: $\cos\phi$ yang padat di $\phi = 0, \pi$ (tempat $V$ tinggi) naik, dan $\sin\phi$ yang padat di $\phi = \pm\pi/2$ (tempat $V$ rendah) turun. Fungsi kompleks $e^{\pm i\phi}$, yang membawa momentum sudut, bukan lagi fungsi orde nol yang benar; pemipihan "memadamkan" momentum sudut. Hal yang sama terjadi pada orbital d ion logam transisi dalam medan ligan (Bab 14): medan ligan memecah degenerasi dan memadamkan momentum sudut orbital, sehingga momen magnet kompleks hampir seluruhnya berasal dari spin.
:::

::: {.contoh}
**Contoh 8.43 · Pasangan terdegenerasi benzena dalam piridina**

Kembali ke Contoh 8.30. Orbital benzena dengan $x = 1$ terdegenerasi ganda. Dua fungsi riil yang lazim adalah $\psi_a = (2\chi_1 + \chi_2 - \chi_3 - 2\chi_4 - \chi_5 + \chi_6)/\sqrt{12}$ dan $\psi_b = (\chi_2 + \chi_3 - \chi_5 - \chi_6)/2$. (a) Hitung matriks perturbasi $H'_{ij} = h\beta c_{1i}c_{1j}$ dalam ruang $\{\psi_a, \psi_b\}$. (b) Tentukan pemecahannya untuk $h = 0{,}5$ dan bandingkan dengan diagonalisasi eksak ($x = 1{,}1672$ dan $1{,}0000$). (c) Ulangi untuk pasangan antiikatan $x = -1$ (eksak: $-0{,}8410$ dan $-1{,}0000$), yang koefisien atom 1-nya juga $2/\sqrt{12}$ dan 0.

**Penyelesaian.** (a) $c_{1a} = 2/\sqrt{12}$ dan $c_{1b} = 0$. Matriksnya $h\beta\begin{pmatrix}1/3 & 0\\ 0 & 0\end{pmatrix}$: sudah diagonal.

(b) $\psi_a$ bergeser $h/3 = 0{,}1667$, menjadi $x = 1{,}1667$; $\psi_b$ tidak bergeser, $x = 1$. Eksak: 1,1672 dan 1,0000.

(c) Sama: $x = -1 + 0{,}1667 = -0{,}8333$ dan $-1$. Eksak $-0{,}8410$ dan $-1{,}0000$.

**Memahami hasil.** Pilihan $\psi_a$ dan $\psi_b$ tidak sembarang: $\psi_a$ simetris dan $\psi_b$ antisimetris terhadap bidang cermin yang melalui atom 1 dan atom 4. Bidang ini tetap menjadi unsur simetri piridina, sehingga ia menentukan fungsi orde nol yang benar. Orbital $\psi_b$ mempunyai simpul tepat di nitrogen, sehingga pergantian C dengan N sama sekali tidak terasa olehnya; energinya tetap **eksak** sama dengan benzena pada semua orde. Spektrum fotoelektron piridina memperlihatkan pecahnya pasangan ini: benzena mempunyai satu pita untuk dua orbital π teratas yang terdegenerasi, sedangkan piridina mempunyai dua pita π yang terpisah, ditambah pita pasangan elektron bebas nitrogen.
:::

### Keadaan tereksitasi helium

Kini kita terapkan teori ini pada masalah yang paling penting secara historis: konfigurasi tereksitasi $1s\,2s$ dan $1s\,2p$ helium. Dalam $\hat H^{(0)}$ (dua ion He⁺), energi orbital hanya bergantung pada $n$: $-Z^2/2n^2$. Mengeksitasi satu elektron ke $n = 2$ memberi

$$
E^{(0)} = -\frac{Z^2}{2} - \frac{Z^2}{8} = -\frac58Z^2 = -2{,}5\ E_h \qquad (Z = 2) .
$$

Berapa fungsi yang mempunyai energi ini? Elektron yang tereksitasi dapat berada di 2s atau di salah satu dari tiga orbital 2p, dan elektron yang tereksitasi dapat elektron 1 atau elektron 2. Jadi tingkat ini terdegenerasi **delapan kali lipat**:

$$
1s(1)2s(2),\ 2s(1)1s(2),\ 1s(1)2p_m(2),\ 2p_m(1)1s(2) \qquad (m = -1, 0, 1) .
$$

Degenerasi terhadap pertukaran elektron 1 dan 2 disebut **degenerasi pertukaran**, dan ia selalu ada bila dua elektron menempati orbital berbeda.

Determinan sekuler 8 × 8 tampak menakutkan, tetapi simetri menyederhanakannya. Operator $1/r_{12}$ tidak berubah bila seluruh sistem diputar, sehingga ia komut dengan momentum sudut total; fungsi dengan momentum sudut berbeda (S dan P) tidak terkopel, dan fungsi dengan $m$ berbeda juga tidak. Matriks 8 × 8 terpecah menjadi empat blok 2 × 2: satu untuk 1s2s dan tiga yang identik untuk 1s2p$_m$. Setiap blok berbentuk

$$
\begin{pmatrix} J & K\\ K & J\end{pmatrix} , \qquad J = \left\langle 1s(1)\,n\ell(2)\left|\frac{1}{r_{12}}\right|1s(1)\,n\ell(2)\right\rangle , \qquad K = \left\langle 1s(1)\,n\ell(2)\left|\frac{1}{r_{12}}\right|n\ell(1)\,1s(2)\right\rangle . \qquad \text{(8.43)}
$$

Kedua unsur diagonal sama karena memberi label "1" atau "2" pada elektron tidak mengubah tolakan. Akar-akarnya $E^{(1)} = J \pm K$, dan fungsi orde nol yang benar adalah kombinasi simetris dan antisimetris:

$$
\psi_\pm = \frac{1}{\sqrt2}\left[1s(1)\,n\ell(2) \pm n\ell(1)\,1s(2)\right] , \qquad E_\pm = E^{(0)} + J \pm K . \qquad \text{(8.44)}
$$

**Integral Coulomb** $J$ adalah tolakan klasik antara awan muatan $|1s|^2$ dan awan $|n\ell|^2$. **Integral pertukaran** $K$ tidak mempunyai padanan klasik: integrannya memuat hasil kali $1s(1)\,n\ell(1)$, "kerapatan tumpang tindih" yang muncul hanya karena elektron tidak dapat dibedakan dan kita harus menulis kedua kemungkinan penugasan. Untuk orbital riil, $K$ dapat dibuktikan positif. Untuk $Z = 2$, perhitungan (lihat kotak di bawah) memberi

$$
J_{1s2s} = \tfrac{17}{81}Z = 0{,}4198 , \quad K_{1s2s} = \tfrac{16}{729}Z = 0{,}0439 , \quad J_{1s2p} = \tfrac{59}{243}Z = 0{,}4856 , \quad K_{1s2p} = \tfrac{112}{6561}Z = 0{,}0341 .
$$

### Fungsi antisimetris lebih rendah: lubang pertukaran

Mengapa fungsi antisimetris $\psi_-$ lebih rendah energinya? Lihat apa yang terjadi bila kedua elektron berada di titik yang sama, $\mathbf r_1 = \mathbf r_2$: kedua suku dalam $\psi_-$ menjadi sama dan saling menghapus, $\psi_- = 0$. Dalam keadaan antisimetris, kedua elektron **tidak pernah** berada di tempat yang sama, dan peluangnya kecil bila keduanya berdekatan. Mereka secara otomatis saling menghindar, sehingga tolakan rata-ratanya lebih kecil: $J - K$. Sebaliknya, $\psi_+$ memperbesar peluang kedua elektron berdekatan, dan tolakannya $J + K$. Daerah di sekitar setiap elektron yang "dikosongkan" dari elektron lain dalam fungsi antisimetris disebut **lubang pertukaran**.

Di Bab 9 kita akan melihat bahwa fungsi gelombang total elektron, termasuk spin, harus antisimetris terhadap pertukaran. Fungsi ruang antisimetris $\psi_-$ karena itu harus berpasangan dengan fungsi spin simetris, yaitu tiga keadaan **triplet** (spin total $S = 1$); fungsi ruang simetris $\psi_+$ berpasangan dengan keadaan **singlet** ($S = 0$) yang spinnya antisimetris (subbab 9.4). Jadi triplet lebih rendah daripada singlet dari konfigurasi yang sama. Inilah dasar **aturan Hund pertama** (subbab 9.12), dan perlu dicatat bahwa penyebabnya bukan interaksi magnetik antarspin, yang terlalu lemah, melainkan tolakan Coulomb biasa yang diatur ulang oleh simetri pertukaran.

::: {.dalam}
**Lebih dalam: menghitung $J_{1s2s}$**

Pakai potensial awan 1s dari kotak di subbab 8.3 dengan $\zeta = Z$: $\Phi_{1s}(r) = 1/r - e^{-2Zr}(1/r + Z)$. Integral Coulomb adalah energi awan 2s dalam potensial itu:

$$
J_{1s2s} = \int_0^\infty R_{2s}^2\,\Phi_{1s}\,r^2dr , \qquad R_{2s}^2 = \frac{Z^3}{8}(2 - Zr)^2e^{-Zr} .
$$

Suku $1/r$ memberi $\langle 1/r\rangle_{2s} = Z/4$. Suku kedua, dengan $\rho = Zr$:

$$
\frac{Z}{8}\int_0^\infty(2 - \rho)^2(\rho + \rho^2)e^{-3\rho}d\rho = \frac{Z}{8}\int_0^\infty(4\rho - 3\rho^3 + \rho^4)e^{-3\rho}d\rho = \frac Z8\left(\frac49 - \frac{18}{81} + \frac{24}{243}\right) = \frac Z8\cdot\frac{26}{81} .
$$

Jadi $J_{1s2s} = Z/4 - 13Z/324 = 68Z/324 = 17Z/81$. Bandingkan dengan $\langle 1/r\rangle_{2s} = Z/4 = 81Z/324$: perisai 1s mengurangi tolakan "titik" sebesar 16%, karena sebagian awan 2s menembus ke dalam awan 1s. Integral pertukaran memerlukan potensial dari "awan tumpang tindih" $1s\cdot2s$, yang tidak bersimetri bola dalam arti yang sama sederhananya; hasilnya $K_{1s2s} = 16Z/729$. Untuk 1s2p, ekspansi Laplace diperlukan: $J$ hanya memakai suku $\ell = 0$ dan $K$ hanya suku $\ell = 1$ (dengan faktor $\tfrac13$).
:::

::: {.contoh}
**Contoh 8.44 · Singlet dan triplet 1s2s dan 1s2p**

Hitung energi orde pertama keempat suku $2^1$S, $2^3$S, $2^1$P, dan $2^3$P helium, dan energi eksitasinya dari keadaan dasar eksak ($-2{,}9037\ E_h$). Bandingkan dengan nilai eksak $-2{,}1460$; $-2{,}1752$; $-2{,}1238$; $-2{,}1332\ E_h$.

**Penyelesaian.**

| Suku | Rumus | $E$ hitung ($E_h$) | $E$ eksak ($E_h$) | Eksitasi hitung (eV) | Eksitasi eksak (eV) |
|---|---|---|---|---|---|
| $2^3$S | $-2{,}5 + J_s - K_s$ | $-2{,}1241$ | $-2{,}1752$ | 21,21 | 19,82 |
| $2^1$S | $-2{,}5 + J_s + K_s$ | $-2{,}0364$ | $-2{,}1460$ | 23,60 | 20,62 |
| $2^3$P | $-2{,}5 + J_p - K_p$ | $-2{,}0485$ | $-2{,}1332$ | 23,27 | 20,96 |
| $2^1$P | $-2{,}5 + J_p + K_p$ | $-1{,}9803$ | $-2{,}1238$ | 25,13 | 21,22 |

Pemecahan singlet–triplet: hitung $2K_s = 2{,}39$ eV dan $2K_p = 1{,}86$ eV; eksak 0,80 dan 0,25 eV.

**Memahami hasil.** Perturbasi orde pertama menghasilkan **urutan** keempat suku dengan benar: setiap triplet di bawah singletnya, dan S di bawah P. Nilai mutlaknya meleset 2–4 eV, karena orbital He⁺ ($\zeta = 2$) terlalu kompak untuk elektron 2s dan 2p yang sebenarnya terperisai hampir penuh oleh elektron 1s; tolakan dan pertukaran karena itu dilebih-lebihkan. Fungsi variasi dengan eksponen berbeda untuk orbital dalam dan luar (seperti Contoh 8.14) memperbaikinya jauh. Dua deret garis helium, yang dahulu dikira berasal dari dua unsur berbeda ("parhelium" dan "ortohelium"), adalah deret singlet dan deret triplet; transisi antara keduanya hampir terlarang (subbab 8.12), sehingga keadaan $2^3$S hidup sekitar 8000 detik dan menjadi salah satu keadaan tereksitasi paling awet di alam.
:::

![Gambar 8.7 Tingkat-tingkat helium dari konfigurasi 1s2s dan 1s2p. Kolom pertama: orde nol, delapan keadaan terdegenerasi pada $-2{,}5\ E_h$. Kolom kedua: integral Coulomb $J$ memisahkan 1s2s dan 1s2p. Kolom ketiga: integral pertukaran $\pm K$ memecah setiap konfigurasi menjadi triplet (bawah) dan singlet (atas). Kolom keempat: nilai eksak. Urutan keempat suku sudah benar pada orde pertama.](fig/c_hetereksitasi.png){width=82%}

::: {.contoh}
**Contoh 8.45 · Mengapa 2s di bawah 2p: penetrasi**

Dalam atom hidrogen, 2s dan 2p terdegenerasi. Dalam helium tereksitasi, $2^3$S lebih rendah daripada $2^3$P. (a) Dari tabel Contoh 8.44, hitung selisih $2^3$P − $2^3$S menurut perturbasi dan menurut nilai eksak. (b) Suku mana yang bertanggung jawab? (c) Apa artinya bagi atom berelektron banyak?

**Penyelesaian.** (a) Perturbasi: $-2{,}0485 - (-2{,}1241) = 0{,}0756\ E_h = 2{,}06$ eV. Eksak: $-2{,}1332 - (-2{,}1752) = 0{,}0421\ E_h = 1{,}14$ eV.

(b) $J_{1s2p} - J_{1s2s} = 0{,}4856 - 0{,}4198 = 0{,}0658\ E_h$, ditambah perubahan kecil $K$. Elektron 2p mengalami tolakan rata-rata yang lebih besar dari elektron 1s daripada elektron 2s.

(c) Orbital 2s mempunyai bagian dalam (di dalam simpul radialnya) yang **menembus** awan 1s, tempat ia merasakan muatan inti yang hampir tidak terperisai. Orbital 2p, yang nol di inti, tetap di luar dan terperisai lebih baik. Akibatnya, dalam atom berelektron banyak, energi orbital dengan $n$ sama naik menurut $\ell$: $ns < np < nd < nf$.

**Memahami hasil.** Penetrasi adalah alasan mengapa 4s terisi sebelum 3d pada kalium dan kalsium, dan mengapa tabel periodik mempunyai bentuk yang kita kenal (subbab 9.9). Seluruh "aturan Aufbau" berakar pada pemecahan degenerasi $\ell$ oleh tolakan antarelektron, yang pertama kali terlihat di sini sebagai selisih $J_{1s2p} - J_{1s2s}$.
:::

::: {.kuis}
**Kuis cepat 8.9**

(a) Mengapa tingkat $n = 2$ helium (dengan satu elektron di 1s) terdegenerasi delapan kali dalam $\hat H^{(0)}$? (b) Apa makna fisika integral pertukaran $K$, dan mengapa tidak ada padanannya dalam elektrostatika klasik? (c) Dalam Contoh 8.42, mengapa $\cos\phi$ naik dan $\sin\phi$ turun?
:::

