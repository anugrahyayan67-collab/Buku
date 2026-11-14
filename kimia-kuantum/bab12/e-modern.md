## 12.11 VSEPR dan dasar kuantumnya

### Aturan VSEPR

Model **tolakan pasangan elektron kulit valensi** (VSEPR; N. V. Sidgwick dan H. M. Powell 1940, R. J. Gillespie dan R. S. Nyholm 1957) meramalkan bentuk molekul golongan utama dengan aturan yang sangat sederhana:

1. Pasangan elektron valensi atom pusat (pasangan ikatan dan pasangan bebas, disebut **domain**) menyusun diri sejauh mungkin satu sama lain.
2. Tolakan berkurang menurut urutan: pasangan bebas–pasangan bebas > pasangan bebas–pasangan ikatan > pasangan ikatan–pasangan ikatan.
3. Ikatan rangkap dihitung sebagai satu domain, tetapi domainnya lebih besar daripada ikatan tunggal.
4. Domain ikatan ke substituen elektronegatif lebih kecil (elektronnya ditarik menjauh dari atom pusat).

Dengan notasi AX$_m$E$_n$ ($m$ ligan, $n$ pasangan bebas), susunan dasar domain adalah: 2 linear, 3 segitiga datar, 4 tetrahedron, 5 bipiramida segitiga, 6 oktahedron, 7 bipiramida segilima. Pasangan bebas tidak "terlihat" dalam bentuk molekul, sehingga AX₃E (NH₃) piramida segitiga, AX₂E₂ (H₂O) bengkok, AX₄E (SF₄) jungkat-jungkit, AX₃E₂ (ClF₃) bentuk T, AX₂E₃ (XeF₂) linear, AX₅E (BrF₅) piramida bujur sangkar, AX₄E₂ (XeF₄) bujur sangkar. Pada bipiramida segitiga, pasangan bebas menempati kedudukan ekuatorial, tempat ia hanya mempunyai dua tetangga pada 90° (bukan tiga seperti di kedudukan aksial).

Aturan 2–4 menjelaskan penyimpangan halus: sudut H–N–H (106,7°) dan H–O–H (104,5°) lebih kecil dari 109,47°; sudut H–C–H formaldehida (116,5°) lebih kecil dari 120° karena domain C=O yang besar; sudut F–N–F pada NF₃ (102,2°) lebih kecil daripada H–N–H. Semua ini sudah kita temui dalam bahasa hibridisasi (subbab 12.6). Kedua bahasa itu saling melengkapi: VSEPR meramalkan bentuk, hibridisasi melukiskan orbital yang sesuai dengan bentuk itu.

### Mengapa pasangan elektron saling menghindar? Asas Pauli

Nama VSEPR menyiratkan bahwa tolakan Coulomb antarpasangan elektron menentukan bentuk. Itu hanya separuh benar. Gaya penggerak yang lebih dasar adalah **asas Pauli**: elektron-elektron dengan spin yang sama tidak dapat berada di tempat yang sama, dan mereka cenderung saling menjauh **bahkan tanpa tolakan Coulomb**.

Bayangkan delapan elektron valensi atom pusat (oktet), empat dengan spin α dan empat dengan spin β. Fungsi gelombang empat elektron α adalah determinan Slater (subbab 9.6). Untuk melihat inti persoalannya, ambil empat orbital $s$, $p_x$, $p_y$, $p_z$ dengan bagian radial yang sama dan tinjau hanya bagian sudutnya. Bila elektron $i$ berada pada arah satuan $\mathbf r_i = (x_i, y_i, z_i)$, determinannya sebanding dengan

$$
D = \begin{vmatrix}1 & \sqrt3\,x_1 & \sqrt3\,y_1 & \sqrt3\,z_1\\ 1 & \sqrt3\,x_2 & \sqrt3\,y_2 & \sqrt3\,z_2\\ 1 & \sqrt3\,x_3 & \sqrt3\,y_3 & \sqrt3\,z_3\\ 1 & \sqrt3\,x_4 & \sqrt3\,y_4 & \sqrt3\,z_4\end{vmatrix} = 3\sqrt3\begin{vmatrix}1 & x_1 & y_1 & z_1\\ \vdots & & & \vdots\\ 1 & x_4 & y_4 & z_4\end{vmatrix} . \qquad \text{(12.36)}
$$

Determinan $4 \times 4$ terakhir sama dengan enam kali volume (bertanda) tetrahedron dengan titik-titik sudut $\mathbf r_1, \ldots, \mathbf r_4$: kurangkan baris pertama dari baris-baris lainnya, lalu uraikan menurut kolom pertama, dan yang tersisa adalah determinan tiga vektor sisi tetrahedron. Rapat peluang menemukan keempat elektron α pada arah-arah itu sebanding dengan $|D|^2$, yaitu dengan **kuadrat volume tetrahedron**.

Kesimpulannya langsung. Peluang nol bila dua elektron berimpit (dua baris sama) atau bila keempatnya terletak pada satu bidang (volume nol). Peluang **maksimum** bila volume tetrahedron yang titik-titik sudutnya pada bola satuan maksimum, yaitu tetrahedron beraturan. Empat elektron α "lebih suka" berada di sudut-sudut tetrahedron, semata-mata karena antisimetri fungsi gelombang. Hal yang sama berlaku untuk empat elektron β. Bila ada inti-inti (atom H) yang menarik elektron α dan β ke tempat yang sama, kedua tetrahedron berimpit dan membentuk empat pasangan: inilah empat pasangan elektron VSEPR. Untuk tiga elektron dalam $s$, $p_x$, $p_y$, $|D|^2$ sebanding dengan kuadrat luas segitiga, maksimum pada segitiga sama sisi (120°); untuk dua elektron dalam $s$ dan $p_z$, $|D|^2 \propto (z_1 - z_2)^2$, maksimum bila keduanya berlawanan (180°).

Gagasan bahwa oktet terdiri atas dua kuartet spin yang masing-masing tetrahedral adalah teori **kuartet ganda** J. W. Linnett (1961). Bila tidak ada inti yang memaksa kedua kuartet berimpit, kuartet α dan β dapat saling berputar. Linnett memakai gagasan ini untuk menjelaskan bahwa O₂ paramagnetik tanpa teori orbital molekul.

::: {.inti}
**Dasar kuantum VSEPR.** Antisimetri fungsi gelombang (asas Pauli) membuat elektron-elektron dengan spin sama saling menghindar: rapat peluang empat elektron sejenis dalam kulit $sp^3$ sebanding dengan kuadrat volume tetrahedron yang mereka bentuk, sehingga maksimum pada tetrahedron beraturan. Tolakan Coulomb memperkuat kecenderungan ini tetapi bukan penyebab utamanya. Analisis modern kerapatan elektron (laplasian kerapatan, fungsi lokalisasi elektron) memperlihatkan daerah-daerah konsentrasi pasangan elektron yang susunannya cocok dengan ramalan VSEPR.
:::

### Model titik pada bola

Versi kuantitatif VSEPR yang paling sederhana menempatkan $n$ titik (domain) pada bola dan mencari susunan yang meminimumkan energi tolakan $\sum_{i<j}1/r_{ij}^k$. Untuk $k = 1$ ini adalah **soal Thomson**. Hasilnya (Contoh 12.40): $n = 2$ linear, 3 segitiga, 4 tetrahedron, 5 bipiramida segitiga, 6 oktahedron, 7 bipiramida segilima, sesuai dengan aturan VSEPR. Menariknya, untuk $n = 5$ bipiramida segitiga hanya sedikit lebih stabil daripada piramida bujur sangkar (selisih 0,14% untuk $k = 1$). Selisih yang kecil ini adalah sebab molekul AX₅ bersifat fluksional: pada PF₅, atom F aksial dan ekuatorial bertukar tempat melalui piramida bujur sangkar (**pseudorotasi Berry**) dengan penghalang hanya sekitar 15 kJ/mol, sehingga spektrum NMR $^{19}$F pada suhu kamar hanya menunjukkan satu sinyal F.

### Keterbatasan VSEPR

VSEPR berhasil untuk molekul golongan utama, tetapi gagal dalam beberapa kasus yang mengajarkan banyak hal:

* **Hidrida unsur berat.** H₂S, PH₃, dan seterusnya bersudut hampir 90°, bukan "tetrahedral yang sedikit dimampatkan". Pasangan bebas $ns^2$ tidak terarah (subbab 12.6).
* **Pasangan bebas yang tidak aktif secara stereokimia.** [TeCl₆]²⁻, [SbCl₆]³⁻, dan [BrF₆]⁻ mempunyai pasangan bebas ketujuh (AX₆E), tetapi bentuknya oktahedron beraturan. Pasangan bebas berada dalam orbital $5s$ atau $4s$ yang bulat. XeF₆ (juga AX₆E) berbentuk oktahedron terdistorsi yang fluksional: kasus perbatasan.
* **Molekul ionik.** Li₂O linear (tolakan Li⁺···Li⁺), tetapi beberapa dihalida logam alkali tanah berat dalam fase gas (SrF₂, BaF₂) bengkok, karena polarisasi inti ion logam dan peran orbital $d$ logam.
* **Senyawa logam transisi.** W(CH₃)₆ berbentuk prisma segitiga, bukan oktahedron, meskipun tidak mempunyai pasangan bebas. VSEPR tidak meramalkan ini; hibrida $sd^5$ meramalkannya (subbab 12.14).
* **Bentuk molekul yang ditentukan oleh orbital, bukan oleh pasangan.** Diagram Walsh (subbab 13.3) menjelaskan sudut ikatan dari perubahan energi orbital molekul terhadap sudut, dan menangani juga keadaan tereksitasi dan radikal, tempat konsep "pasangan" kehilangan maknanya.

::: {.contoh}
**Contoh 12.39 · Meramalkan bentuk**

Tentukan rumus AX$_m$E$_n$ dan bentuk molekul: SF₄, ClF₃, BrF₅, XeF₄, I₃⁻, IF₇, SO₂. Pada SF₄, apakah sudut F$_\text{ak}$–S–F$_\text{ak}$ lebih besar atau lebih kecil dari 180°, dan mengapa?

**Penyelesaian.** SF₄: S mempunyai 6 elektron valensi, 4 ikatan, sisa 2 elektron = 1 pasangan bebas: AX₄E, jungkat-jungkit. ClF₃: Cl 7, 3 ikatan, 2 pasangan bebas: AX₃E₂, bentuk T. BrF₅: Br 7, 5 ikatan, 1 pasangan bebas: AX₅E, piramida bujur sangkar. XeF₄: Xe 8, 4 ikatan, 2 pasangan bebas: AX₄E₂, bujur sangkar. I₃⁻: I pusat 7 + 1 (muatan) = 8, 2 ikatan, 3 pasangan bebas: AX₂E₃, linear. IF₇: AX₇, bipiramida segilima. SO₂: S 6, dua ikatan rangkap (dua domain), 1 pasangan bebas: AX₂E, bengkok (119,5°).

Pada SF₄ pasangan bebas ekuatorial mendorong kedua F aksial menjauhinya, sehingga sudut F$_\text{ak}$–S–F$_\text{ak}$ kurang dari 180° (teramati 173,1°), dan sudut F$_\text{ek}$–S–F$_\text{ek}$ jauh kurang dari 120° (101,6°).

**Memahami hasil.** Bentuk-bentuk ini cocok dengan percobaan. Perhatikan bahwa pada AX₂E₃ (I₃⁻, XeF₂) dan AX₄E₂ (XeF₄) VSEPR dan model 3c-4e (subbab 12.8) memberi bentuk yang sama: ketiga pasangan bebas ekuatorial atau kedua pasangan bebas trans memang adalah orbital $s$ dan $p$ atom pusat yang tidak dipakai untuk ikatan 3c-4e.
:::

::: {.contoh}
**Contoh 12.40 · Soal Thomson dengan Python**

Tulis program yang meminimumkan $E = \sum_{i<j}1/|\mathbf r_i - \mathbf r_j|$ untuk $n$ titik pada bola satuan, untuk $n = 2$ sampai 7. Untuk $n = 5$, bandingkan bipiramida segitiga (BPS) dengan piramida bujur sangkar (PBS) terbaik.

**Penyelesaian.**

```python
import numpy as np
from scipy.optimize import minimize
def titik(v):                              # v = (theta_1..theta_n, phi_1..phi_n)
    t, p = np.split(v, 2)
    return np.stack([np.sin(t)*np.cos(p), np.sin(t)*np.sin(p), np.cos(t)], 1)
def energi(v):
    r = titik(v); d = np.linalg.norm(r[:, None] - r[None], axis=2)
    return np.sum(1/d[np.triu_indices(len(r), 1)])
rng = np.random.default_rng(1)
for n in range(2, 8):
    terbaik = min((minimize(energi, np.r_[np.arccos(rng.uniform(-1, 1, n)), rng.uniform(0, 2*np.pi, n)])
                   for _ in range(30)), key=lambda h: h.fun)
    print(n, round(terbaik.fun, 6))
```

Keluarannya: $E$ = 0,5 (2), 1,732051 (3), 3,674235 (4), 6,474691 (5), 9,985281 (6), 14,452977 (7). Sudut-sudut susunan terbaik adalah 180°; 120°; 109,47°; 90°, 120°, 180° (BPS); 90° dan 180° (oktahedron); 72°, 90°, 144°, 180° (bipiramida segilima). Untuk PBS dengan sudut puncak–basal dioptimasi (104,1°), $E = 6{,}483661$, lebih tinggi 0,0090 (0,14%) daripada BPS. Dengan tolakan yang lebih "keras", $1/r^6$, selisihnya 1,5%, dan dengan $1/r^{12}$ 1,1%.

**Memahami hasil.** Model titik pada bola mereproduksi semua susunan dasar VSEPR, dan memperlihatkan bahwa untuk lima domain dua susunan hampir berdegenerasi. Ramalannya pun sejalan dengan kimia: molekul AX₅ sering fluksional, dan beberapa (misalnya ion [Ni(CN)₅]³⁻ dalam garam tertentu) dijumpai dalam kedua bentuk dalam kristal yang sama.
:::

::: {.contoh}
**Contoh 12.41 · Determinan Pauli untuk tiga dan empat elektron**

(a) Hitung $|D|^2$ dari (12.36) untuk empat elektron pada sudut-sudut tetrahedron beraturan, dengan volume tetrahedron beraturan yang terinskripsi dalam bola satuan $V = 8/(9\sqrt3)$. (b) Berapa $|D|^2$ bila keempat elektron berada di sudut-sudut bujur sangkar di bidang $xy$? (c) Untuk dua elektron dalam $s$ dan $p_z$, pada sudut berapa $|D|^2$ maksimum?

**Penyelesaian.** (a) $D = 3\sqrt3 \times 6V = 3\sqrt3 \times 6 \times 0{,}5132 = 16{,}00$; $|D|^2 = 256$. Pencarian numerik maksimum $|D|^2$ atas semua susunan memberi nilai yang sama, dengan semua sudut 109,47°. (b) Keempat titik sebidang: volume nol, $|D|^2 = 0$. (c) $D = \sqrt3(z_2 - z_1)$, maksimum bila $z_1 = 1$, $z_2 = -1$ (atau sebaliknya): sudut 180°, $|D|^2 = 12$.

**Memahami hasil.** Susunan bujur sangkar, yang tampak "cukup terpisah" bila kita hanya memikirkan jarak, sama sekali dilarang oleh asas Pauli untuk empat elektron sejenis dalam kulit $sp^3$. Inilah sebabnya molekul AX₄ dengan delapan elektron valensi (CH₄, NH₄⁺, BF₄⁻) tidak pernah bujur sangkar; bentuk bujur sangkar muncul hanya bila ada dua belas elektron (XeF₄, AX₄E₂) atau bila orbital $d$ terlibat ([PtCl₄]²⁻, subbab 12.14).
:::

::: {.kuis}
**Kuis cepat 12.11**

Menurut VSEPR, mengapa pasangan bebas pada ClF₃ menempati kedudukan ekuatorial, bukan aksial? Ramalkan apakah sudut F$_\text{ak}$–Cl–F$_\text{ek}$ lebih besar atau lebih kecil dari 90°.
:::

## 12.12 Teori ikatan valensi modern (GVB, spin-coupled)

### Kelemahan teori Heitler–London klasik

Fungsi Heitler–London (12.1) memakai orbital atom yang tidak berubah sama sekali ketika molekul terbentuk. Hasilnya cukup baik secara kualitatif, tetapi energi ikatannya jauh terlalu kecil. Untuk H₂ dengan orbital $1s$ ($\zeta = 1$), Heitler–London memberi $D_e = 3{,}16$ eV pada $R = 1{,}64\,a_0$; dengan eksponen orbital yang dioptimasi ($\zeta = 1{,}166$, S. C. Wang 1928) diperoleh 3,79 eV. Nilai eksak adalah 4,75 eV pada $1{,}40\,a_0$. Yang hilang adalah kemampuan orbital untuk **berubah bentuk** di dalam molekul, dan sumbangan struktur ionik H⁻H⁺ dan H⁺H⁻.

Teori ikatan valensi tradisional menambahkan struktur ionik secara eksplisit: $\Psi = c_\text{kov}\Phi_\text{kov} + c_\text{ion}\Phi_\text{ion}$, dengan $\Phi_\text{ion} = a(1)a(2) + b(1)b(2)$. Untuk molekul besar, cara ini cepat meledak: banyaknya struktur ionik dan kovalen bertambah sangat cepat.

### Orbital yang boleh berubah bentuk: Coulson–Fischer dan GVB

C. A. Coulson dan I. Fischer (1949) mengusulkan jalan yang jauh lebih hemat: pertahankan **satu** struktur kovalen, tetapi biarkan kedua orbitalnya berubah bentuk. Untuk H₂, ambil

$$
\phi_1 = \frac{a + \lambda b}{\sqrt{1 + \lambda^2 + 2\lambda S}} , \qquad \phi_2 = \frac{b + \lambda a}{\sqrt{1 + \lambda^2 + 2\lambda S}} , \qquad \text{(12.37)}
$$

dua orbital yang masing-masing terutama berada pada satu atom tetapi mempunyai "ekor" kecil pada atom lain. Fungsi gelombangnya tetap berbentuk Heitler–London:

$$
\Psi_\text{GVB} \propto \left[\phi_1(1)\phi_2(2) + \phi_2(1)\phi_1(2)\right]\left[\alpha(1)\beta(2) - \beta(1)\alpha(2)\right] . \qquad \text{(12.38)}
$$

Sekarang uraikan bagian ruangnya. Dengan $\phi_1\phi_2 \propto (a + \lambda b)(b + \lambda a) = ab + \lambda aa + \lambda bb + \lambda^2ba$, dan suku tukarnya:

$$
\phi_1(1)\phi_2(2) + \phi_2(1)\phi_1(2) \propto (1 + \lambda^2)\underbrace{[a(1)b(2) + b(1)a(2)]}_\text{kovalen} + 2\lambda\underbrace{[a(1)a(2) + b(1)b(2)]}_\text{ionik} . \qquad \text{(12.39)}
$$

**Satu struktur kovalen dengan orbital yang terdeformasi sama dengan campuran struktur kovalen dan ionik**, dengan perbandingan $2\lambda/(1 + \lambda^2)$. Dalam basis minimal, campuran ini juga sama dengan interaksi konfigurasi dua konfigurasi orbital molekul, $c_g\sigma_g^2 - c_u\sigma_u^2$ (subbab 11.12). Jadi fungsi Coulson–Fischer memberi energi yang sama dengan perhitungan interaksi konfigurasi lengkap dalam basis minimal, tetapi dengan bahasa ikatan valensi: dua elektron dalam dua orbital lokal yang berpasangan spin.

W. A. Goddard (1967) memperumum gagasan ini menjadi metode **ikatan valensi teraplikasi umum** (*generalized valence bond*, GVB). Dalam GVB pasangan sempurna, setiap ikatan dan setiap pasangan bebas dilukiskan oleh sepasang orbital tak ortogonal seperti (12.37), yang bentuknya dioptimasi secara variasi tanpa batasan (tidak harus kombinasi dua orbital atom), dan pasangan-pasangan yang berbeda dibuat saling ortogonal. Metode **spin-coupled** (J. Gerratt, D. L. Cooper, M. Raimondi, 1980-an) melangkah lebih jauh: semua orbital boleh tak ortogonal satu sama lain, dan fungsi spin adalah kombinasi optimum dari semua cara memasangkan spin. Metode-metode sejenis yang kini dipakai (VBSCF, BOVB) memungkinkan perhitungan ikatan valensi dengan ketelitian yang sebanding dengan metode orbital molekul berkorelasi.

### H₂: hasil perhitungan

Gambar 12.9 dan tabel berikut menunjukkan hasil perhitungan dengan basis minimal orbital $1s$ Slater, dengan eksponen $\zeta$ dioptimasi pada setiap jarak (Contoh 12.43).

| Metode | $R_e$ ($a_0$) | $D_e$ (eV) | $\zeta$ optimum |
|---|---|---|---|
| Orbital molekul (RHF), $\sigma_g^2$ | 1,385 | 3,49 | 1,193 |
| Heitler–London | 1,414 | 3,79 | 1,166 |
| GVB (Coulson–Fischer) | 1,430 | 4,03 | 1,194 |
| Eksak | 1,401 | 4,75 | — |

![Gambar 12.9 Energi H₂ terhadap jarak antarinti dalam basis minimal $1s$ dengan eksponen dioptimasi: teori orbital molekul (RHF), Heitler–London, dan GVB (setara dengan interaksi konfigurasi lengkap dalam basis ini). Bintang menandai minimum eksak. Kurva RHF menuju limit yang salah karena memuat 50% struktur ionik pada semua jarak.](fig/c_h2gvb.png){width=76%}

Tiga hal patut dicatat. Pertama, GVB lebih rendah daripada keduanya pada **semua** jarak, karena ia memuat Heitler–London ($\lambda = 0$) dan RHF ($\lambda = 1$, yang membuat $\phi_1 = \phi_2 = \sigma_g$) sebagai kasus khusus. Kedua, pada jarak setimbang $\lambda = 0{,}135$: orbital GVB hanya sedikit berubah dari orbital atom, tetapi perubahan kecil itu menambah 0,24 eV energi ikatan dibanding Heitler–London. Ketiga, GVB menuju limit yang benar (dua atom H netral) ketika ikatan diputus, sedangkan RHF tidak (Contoh 12.44). Sisa selisih dengan nilai eksak (0,7 eV) berasal dari basis minimal, bukan dari bentuk fungsi gelombang.

### Gambaran GVB molekul poliatom

Orbital GVB dan spin-coupled yang dioptimasi tanpa prasangka ternyata menyerupai hibrida klasik, dan ini adalah pembenaran paling kuat bagi konsep hibridisasi:

* **Metana.** Untuk setiap ikatan C–H diperoleh satu orbital yang menyerupai hibrida sp³ karbon (dengan ekor kecil pada H) dan satu orbital yang menyerupai $1s$ hidrogen yang sedikit terpolarisasi ke arah karbon.
* **Air.** Kedua pasangan bebas keluar sebagai dua orbital setara "telinga kelinci" bila keduanya diperlakukan sebagai pasangan GVB, tetapi energi totalnya hampir sama dengan deskripsi σ/π, sesuai dengan kesetaraan yang dibahas di subbab 12.6.
* **Etilena.** Perhitungan GVB memberi dua deskripsi ikatan rangkap yang energinya hampir sama: σ + π, atau dua "ikatan pisang" (Ω) setara yang masing-masing melengkung di atas dan di bawah bidang molekul. Bagi fungsi gelombang yang sederhana, kedua gambaran itu berhubungan melalui transformasi $(\sigma \pm \pi)/\sqrt2$.
* **Benzena.** Perhitungan spin-coupled (Cooper, Gerratt, Raimondi, 1986) memberi enam orbital π, masing-masing menyerupai $2p_z$ pada satu karbon dengan ekor kecil ke tetangganya, dan fungsi spin yang didominasi oleh dua struktur Kekulé dengan sumbangan kecil struktur Dewar. Gambaran resonansi Pauling di subbab 12.10 ternyata bertahan dalam perhitungan modern yang jauh lebih teliti.

### Metilena: mengapa keadaan dasarnya triplet

Karbena paling sederhana, CH₂, mempunyai keadaan dasar triplet ($^3B_1$, sudut H–C–H sekitar 134°), dengan keadaan singlet terendah ($^1A_1$, sekitar 102°) 37,6 kJ/mol lebih tinggi. Dalam bahasa ikatan valensi, karbon memakai dua orbital untuk ikatan C–H, dan dua elektron sisanya berada dalam hibrida σ (di bidang molekul, menunjuk menjauhi kedua H) dan orbital $p$ π (tegak lurus bidang). Bila keduanya berspin sejajar (triplet), mereka mendapat energi pertukaran yang menurunkan energi, seperti dalam aturan Hund. Untuk singlet, kedua elektron lebih untung bila berpasangan dalam orbital σ yang kaya $s$, tetapi ini menambah tolakan elektron. Pasangan σ² singlet ternyata paling baik dilukiskan sebagai **pasangan GVB** dari dua cuping yang sedikit terpisah di bidang molekul: korelasi elektron dalam satu "pasangan bebas". Karena orbital σ lebih kaya $s$ bila sudut H–C–H mengecil (lebih banyak $s$ tersisa untuk pasangan bebas), singlet memilih sudut yang lebih kecil. Perbedaan sudut dan urutan keadaan ini menjelaskan mengapa karbena triplet bereaksi sebagai biradikal (bertahap, tidak stereospesifik) dan karbena singlet bereaksi secara serentak dan stereospesifik dengan alkena.

### Ikatan tiga elektron

Teori ikatan valensi modern juga mengenali **ikatan tiga elektron**: tiga elektron dalam dua orbital yang tumpang tindih, misalnya He₂⁺ atau radikal kation (R₂S∴SR₂)⁺. Ikatan ini berorde kira-kira setengah. Pauling melukiskan O₂ dengan satu ikatan σ biasa dan dua ikatan tiga elektron π yang saling tegak lurus. Setiap ikatan tiga elektron menyumbang satu elektron tak berpasangan, sehingga O₂ mempunyai dua elektron tak berpasangan (paramagnetik) dan orde ikatan $1 + \tfrac12 + \tfrac12 = 2$. Ini sesuai dengan teori orbital molekul (subbab 11.7) dan menunjukkan bahwa kegagalan "ikatan valensi" untuk O₂ yang sering disebut di buku-buku sebenarnya kegagalan struktur Lewis sederhana, bukan kegagalan teori ikatan valensi.

::: {.contoh}
**Contoh 12.42 · Dari λ ke bobot ionik**

Pada $R = 1{,}4\,a_0$ perhitungan GVB memberi $\lambda = 0{,}135$ dan tumpang tindih orbital atom $S = \langle a|b\rangle = 0{,}675$ (dengan $\zeta = 1{,}20$). (a) Hitung perbandingan koefisien ionik terhadap kovalen. (b) Hitung tumpang tindih kedua orbital GVB, $\langle\phi_1|\phi_2\rangle = [2\lambda + S(1 + \lambda^2)]/(1 + \lambda^2 + 2\lambda S)$. (c) Bobot Chirgwin–Coulson struktur ionik dari perhitungan ini adalah 0,20. Tafsirkan.

**Penyelesaian.** (a) $2\lambda/(1 + \lambda^2) = 0{,}270/1{,}0182 = 0{,}265$. (b) $[0{,}270 + 0{,}675(1{,}0182)]/[1{,}0182 + 2(0{,}135)(0{,}675)] = 0{,}957/1{,}200 = 0{,}797$.

\(c) Struktur ionik menyumbang 20% dan kovalen 80%.

**Memahami hasil.** Ekor kecil ($\lambda = 0{,}135$) pada setiap orbital menaikkan tumpang tindih dari 0,675 menjadi 0,797 dan memasukkan 20% karakter ionik. Bandingkan dengan RHF, yang memaksa bobot kovalen dan ionik sama (50 : 50) pada semua jarak. Nilai yang benar terletak jauh lebih dekat ke Heitler–London daripada ke RHF; itulah sebabnya Heitler–London memberi energi lebih baik daripada RHF dalam basis yang sama.
:::

::: {.contoh}
**Contoh 12.43 · Menghitung H₂ dengan GVB**

Dengan basis $\{a, b\}$ orbital $1s$ dan integral-integral satu dan dua elektron (dihitung numerik dengan ekspansi Gauss), susun matriks Hamiltonian dalam basis fungsi ruang $f_1 = ab + ba$ (kovalen) dan $f_2 = aa + bb$ (ionik), lalu hitung energi RHF, Heitler–London, dan GVB pada $R = 1{,}4\,a_0$ dengan $\zeta = 1$.

**Penyelesaian.** Unsur-unsur matriks fungsi dua elektron $\langle pq|\hat H|rs\rangle = h_{pr}S_{qs} + S_{pr}h_{qs} + (pr|qs) + S_{pr}S_{qs}/R$. Pada $R = 1{,}4$, $\zeta = 1$: $S = 0{,}7529$, $h_{aa} = -1{,}1100$, $h_{ab} = -0{,}9683$, $(aa|aa) = 0{,}6250$, $(aa|bb) = 0{,}5035$, $(ab|ab) = 0{,}3233$, $(aa|ab) = 0{,}4259$ hartree. Dengan matriks $2 \times 2$ yang dihasilkan:

* Heitler–London ($f_1$ saja): $E = -1{,}1055$ $E_h$.
* RHF ($f_1 + f_2$ dengan koefisien sama, karena $\sigma_g^2 \propto f_1 + f_2$): $E = -1{,}0909$ $E_h$.
* GVB (akar terendah persamaan sekuler $2 \times 2$): $E = -1{,}1066$ $E_h$, dengan $c_\text{ion}/c_\text{kov} = 0{,}117$.

**Memahami hasil.** Pada $\zeta = 1$, struktur ionik hanya menurunkan energi 0,0011 $E_h$ (0,03 eV) di bawah Heitler–London. Bila $\zeta$ juga dioptimasi, GVB turun jauh lebih banyak (ke $-1{,}1479$ $E_h$ pada $R = 1{,}43$), karena orbital yang lebih kompak dan struktur ionik bekerja sama. Pelajaran umumnya: perbaikan fungsi gelombang harus memperbolehkan orbital **dan** cara memasangkan elektron berubah bersama-sama.
:::

::: {.contoh}
**Contoh 12.44 · Memutus ikatan: GVB vs RHF**

Pada $R = 6\,a_0$, perhitungan (dengan $\zeta$ optimum) memberi $E_\text{GVB} = -1{,}0005$ $E_h$, $E_\text{HL} = -1{,}0005$ $E_h$, dan $E_\text{RHF} = -0{,}7953$ $E_h$. Energi dua atom H adalah $-1$ $E_h$. (a) Berapa galat RHF dalam eV? (b) Jelaskan asalnya.

**Penyelesaian.** (a) $(1 - 0{,}7953) \times 27{,}211 = 5{,}57$ eV. (b) $\sigma_g^2 \propto (ab + ba) + (aa + bb)$ memuat struktur kovalen dan ionik dengan bobot sama pada semua jarak. Pada jarak besar, struktur ionik H⁺···H⁻ jauh lebih tinggi energinya (selisih energi ionisasi H dan afinitas elektron H⁻, ditambah energi Coulomb yang kecil), sehingga separuh fungsi gelombang RHF berada pada keadaan yang salah.

**Memahami hasil.** Kegagalan RHF memutus ikatan bukan kecacatan kecil; galatnya beberapa eV, lebih besar daripada energi ikatan sendiri. Teori ikatan valensi tidak mengalami masalah ini karena ia dibangun dari atom-atom yang terpisah. Inilah salah satu alasan metode berbasis ikatan valensi (dan metode orbital molekul multikonfigurasi yang setara, seperti CASSCF) dipakai untuk reaksi pemutusan ikatan, biradikal, dan kopling magnetik (Bab 17).
:::

::: {.contoh}
**Contoh 12.45 · Celah singlet–triplet metilena**

Selisih energi $^1A_1$ dan $^3B_1$ metilena adalah 3147 cm⁻¹. (a) Nyatakan dalam kJ/mol dan eV. (b) Pada suhu 298 K, berapa perbandingan populasi singlet terhadap triplet dalam kesetimbangan termal (ingat degenerasi spin)? (c) Mengapa substituen donor π seperti F atau OCH₃ membalik urutan ini (CF₂ singlet)?

**Penyelesaian.** (a) $3147 \times 0{,}011963 = 37{,}6$ kJ/mol $= 0{,}390$ eV. (b) $\tfrac13e^{-37\,600/(8{,}314 \times 298)} = \tfrac13e^{-15{,}2} = 8 \times 10^{-8}$. (c) Pada CF₂, pasangan bebas $p$ fluor menyumbangkan kerapatan ke orbital $p$ π karbon yang (pada singlet) kosong, menstabilkan singlet; selain itu, menurut aturan Bent, ikatan C–F yang kaya $p$ meninggalkan lebih banyak karakter $s$ untuk orbital σ karbon, sehingga pasangan bebas σ² makin stabil.

**Memahami hasil.** Dalam kesetimbangan, hampir semua metilena berada sebagai triplet. Tetapi metilena yang dibuat dari fotolisis diazometana lahir sebagai singlet dan dapat bereaksi sebelum sempat berubah ke triplet; inilah sebabnya stereokimia produk adisi CH₂ ke alkena bergantung pada kondisi reaksi. Difluorokarbena (singlet, dengan celah lebih dari 200 kJ/mol) bereaksi secara stereospesifik.
:::

::: {.kuis}
**Kuis cepat 12.12**

Dalam fungsi GVB (12.37), berapa nilai $\lambda$ yang membuat fungsi menjadi fungsi Heitler–London? Berapa nilai yang membuatnya menjadi fungsi RHF? Ke nilai mana $\lambda$ menuju ketika $R \to \infty$?
:::

## 12.13 Ikatan valensi vs orbital molekul: spektrum fotoelektron metana sebagai uji

### Teka-teki

Teori ikatan valensi melukiskan metana dengan empat ikatan C–H yang setara, masing-masing berisi dua elektron dalam orbital yang terlokalisasi. Bila elektron-elektron valensi metana berada dalam empat orbital yang setara, energi ionisasinya seharusnya satu nilai: melepaskan elektron dari ikatan mana pun memerlukan energi yang sama. Spektrum fotoelektron (subbab 1.4) metana menunjukkan **dua** pita valensi: satu pita lebar di sekitar 14,4 eV dan satu pita di sekitar 22,9 eV, dengan perbandingan intensitas kira-kira 3 : 1 (Gambar 12.10(a)). Teori orbital molekul meramalkan persis pola ini: orbital $2a_1$ (dari $2s$ karbon dan kombinasi simetris keempat $1s$ hidrogen) dan tiga orbital $1t_2$ yang berdegenerasi (dari $2p$ karbon dan tiga kombinasi $1s$ hidrogen yang sesuai; subbab 13.2). Apakah spektrum fotoelektron membuktikan bahwa ikatan berpasangan elektron lokal itu fiksi?

![Gambar 12.10 Spektrum fotoelektron valensi skematik. (a) Metana: pita $1t_2$ (sekitar 14,4 eV, lebar dan bergelombang karena efek Jahn–Teller pada CH₄⁺) dan pita $2a_1$ (sekitar 22,9 eV). Garis putus-putus: rata-rata tertimbang 16,5 eV, energi ionisasi "satu ikatan C–H terlokalisasi" dalam model lubang. (b) Air: tiga pita valensi dengan foton He I; pita $2a_1$ (32,2 eV) berada di luar jangkauan.](fig/c_fotoelektron.png){width=94%}

### Jawaban pertama: fungsi gelombang yang sama

Fungsi gelombang Hartree–Fock metana adalah satu determinan Slater dari orbital-orbital terisi. Determinan mempunyai sifat yang sangat penting: bila kolom-kolom orbitalnya diganti dengan kombinasi linear $\phi'_i = \sum_jU_{ij}\phi_j$ dengan matriks $\mathbf U$ uniter (atau ortogonal), determinannya hanya dikalikan dengan $\det\mathbf U$, yang besarnya satu:

$$
\det[\phi'_1, \ldots, \phi'_N] = \det\mathbf U\cdot\det[\phi_1, \ldots, \phi_N] , \qquad |\det\mathbf U| = 1 . \qquad \text{(12.40)}
$$

Ini sifat dasar determinan (subbab 2.7): determinan hasil kali sama dengan hasil kali determinan. Akibatnya fungsi gelombang, kerapatan elektron, energi total, dan semua sifat keadaan dasar **sama persis** apakah kita memakai orbital molekul kanonik ($2a_1$, $1t_{2x}$, $1t_{2y}$, $1t_{2z}$) atau empat orbital ikatan terlokalisasi yang diperoleh dengan transformasi

$$
\lambda_i = \tfrac12\left(2a_1 \pm 1t_{2x} \pm 1t_{2y} \pm 1t_{2z}\right) , \qquad \text{(12.41)}
$$

dengan pola tanda yang sama seperti (12.23). Setiap $\lambda_i$ terlokalisasi pada satu ikatan C–H, dan bagian karbonnya adalah hibrida sp³ (dengan sedikit penyesuaian karena $2a_1$ dan $1t_2$ tidak memakai $2s$ dan $2p$ dalam perbandingan persis 1 : 3). Orbital terlokalisasi seperti ini dapat diperoleh secara sistematis dengan kriteria lokalisasi Boys atau Edmiston–Ruedenberg (subbab 17.8). **Keadaan dasar tidak dapat membedakan kedua deskripsi.**

### Jawaban kedua: ionisasi adalah sifat ion

Spektrum fotoelektron tidak mengukur "energi orbital" molekul netral; ia mengukur selisih energi antara molekul netral dan **ion** yang terbentuk, $E(\text{CH}_4^+) - E(\text{CH}_4)$. Pertanyaan yang tepat adalah: seperti apa keadaan-keadaan stasioner CH₄⁺?

Dalam bahasa ikatan lokal, kita dapat membuat lubang di salah satu dari empat ikatan C–H. Keempat keadaan "lubang terlokalisasi" $|1\rangle, |2\rangle, |3\rangle, |4\rangle$ berdegenerasi oleh simetri, dengan energi ionisasi $\varepsilon$. Tetapi keadaan-keadaan itu **bukan** keadaan stasioner: lubang dapat berpindah dari satu ikatan ke ikatan lain karena orbital-orbital ikatan pada atom karbon yang sama bertumpang tindih dan berinteraksi. Sebut unsur matriks perpindahan itu $\tau$; karena keempat ikatan setara, setiap pasangan mempunyai $\tau$ yang sama. Matriks energi ionisasinya

$$
\mathbf H^+ = \begin{pmatrix}\varepsilon & \tau & \tau & \tau\\ \tau & \varepsilon & \tau & \tau\\ \tau & \tau & \varepsilon & \tau\\ \tau & \tau & \tau & \varepsilon\end{pmatrix} = (\varepsilon - \tau)\,\mathbf I + \tau\,\mathbf J , \qquad \text{(12.42)}
$$

dengan $\mathbf J$ matriks yang semua unsurnya satu. Matriks $\mathbf J$ mempunyai nilai eigen 4 (vektor eigen $(1, 1, 1, 1)/2$) dan 0 (tiga kali, untuk semua vektor yang jumlah komponennya nol). Jadi nilai eigen $\mathbf H^+$:

$$
\text{IE}(a_1) = \varepsilon + 3\tau \quad (\text{sekali}) , \qquad \text{IE}(t_2) = \varepsilon - \tau \quad (\text{tiga kali}) . \qquad \text{(12.43)}
$$

**Model ikatan terlokalisasi, bila dipakai dengan benar untuk ion, juga meramalkan dua pita dengan perbandingan 1 : 3.** Keadaan stasioner ion adalah kombinasi simetri keempat keadaan lubang lokal, persis seperti orbital $a_1$ dan $t_2$ adalah kombinasi simetri orbital lokal. Dengan data percobaan, $4\tau = 22{,}9 - 14{,}4$, sehingga $\tau = 2{,}1$ eV dan $\varepsilon = 16{,}5$ eV. Lubang yang dibuat di satu ikatan C–H berpindah ke ikatan lain dalam waktu sekitar $h/4\tau \approx 0{,}5$ fs, jauh lebih cepat daripada waktu yang diperlukan untuk "melihat" ikatan mana yang terionisasi.

Pada H₂O kasusnya serupa. Bila kedua pasangan bebas dilukiskan sebagai dua "telinga kelinci" setara, ionisasi dari keduanya bercampur menjadi kombinasi simetris dan antisimetris, yang tidak lain adalah pasangan bebas σ dan π. Spektrum fotoelektron air memperlihatkan keduanya sebagai pita terpisah: $1b_1$ (π, 12,62 eV, sempit karena elektron π hampir tidak berikatan) dan $3a_1$ (σ, 14,74 eV, lebar karena turut berikatan O–H). Pita $1b_2$ (18,51 eV) adalah ikatan O–H, dan $2a_1$ (32,2 eV) hampir murni $2s$ oksigen.

::: {.inti}
**Ikatan valensi dan orbital molekul adalah dua bahasa untuk fungsi gelombang yang sama.**

* Orbital terisi dapat ditransformasi secara uniter tanpa mengubah fungsi gelombang total: orbital kanonik (terdelokalisasi, beradaptasi simetri) dan orbital terlokalisasi (ikatan, pasangan bebas, hibrida) adalah dua pilihan basis.
* Sifat-sifat **keadaan dasar** (geometri, kerapatan, momen dipol, energi total) tidak bergantung pada pilihan itu. Sifat-sifat yang melibatkan **perubahan banyaknya elektron atau eksitasi** (energi ionisasi, spektrum UV) paling alami dilukiskan dengan orbital kanonik, karena keadaan-keadaan stasioner ion dan keadaan tereksitasi mengikuti simetri molekul.
* Bila diperbaiki sampai tuntas (interaksi konfigurasi lengkap dalam basis yang sama), teori ikatan valensi dan orbital molekul memberikan hasil yang identik.
:::

### Kapan memakai yang mana

| Kebutuhan | Ikatan valensi lebih alami | Orbital molekul lebih alami |
|---|---|---|
| Struktur Lewis, geometri lokal, hibridisasi | ✓ | |
| Pemutusan ikatan, biradikal, kopling magnetik | ✓ | |
| Resonansi dalam bahasa struktur kimia | ✓ | |
| Spektrum fotoelektron, teorema Koopmans | | ✓ |
| Spektrum elektronik, keadaan tereksitasi | | ✓ |
| Aromatisitas, aturan $4n + 2$, reaksi perisiklik | | ✓ (Bab 13) |
| Perhitungan rutin molekul besar | | ✓ (Bab 17) |

Kimiawan yang mahir berpindah bahasa sesuai kebutuhan: menggambar panah lengkung dengan struktur Lewis, lalu menjelaskan selektivitas reaksi dengan orbital perbatasan.

::: {.contoh}
**Contoh 12.46 · Model lubang untuk metana**

(a) Dari energi ionisasi 14,4 eV ($t_2$) dan 22,9 eV ($a_1$), tentukan $\varepsilon$ dan $\tau$ dalam (12.42), dan periksa dengan diagonalisasi numerik. (b) Tunjukkan bahwa $\varepsilon$ sama dengan rata-rata tertimbang keempat energi ionisasi. (c) Bila sebuah lubang mula-mula berada di ikatan 1, berapa peluang menemukannya di ikatan 1 setelah waktu $t$?

**Penyelesaian.** (a) $4\tau = 8{,}5$ eV, $\tau = 2{,}125$ eV; $\varepsilon = 14{,}4 + 2{,}125 = 16{,}525$ eV. Dengan Python:

```python
import numpy as np
eps, tau = 16.525, 2.125
H = (eps - tau)*np.eye(4) + tau*np.ones((4, 4))
print(np.linalg.eigvalsh(H))      # [14.4 14.4 14.4 22.9]
```

\(b) $(22{,}9 + 3 \times 14{,}4)/4 = 16{,}525$ eV $= \varepsilon$: jejak matriks tidak berubah oleh diagonalisasi.

\(c) $|1\rangle = \tfrac12|a_1\rangle + \tfrac{\sqrt3}{2}|t_2'\rangle$, dengan $|t_2'\rangle$ kombinasi ternormalisasi $t_2$ yang sesuai. Amplitudo bertahan $A(t) = \tfrac14e^{-iE_at/\hbar} + \tfrac34e^{-iE_tt/\hbar}$, sehingga $P(t) = |A|^2 = \tfrac58 + \tfrac38\cos(4\tau t/\hbar)$, yang berosilasi antara 1 dan $\tfrac14$.

**Memahami hasil.** Lubang bolak-balik di antara keempat ikatan dengan periode $h/4\tau = 4{,}136 \times 10^{-15}\ \text{eV s}/8{,}5\ \text{eV} = 0{,}49$ fs. Pengukuran dengan resolusi energi lebih baik daripada beberapa eV, seperti spektrum fotoelektron, tidak dapat melihat lubang terlokalisasi; ia melihat keadaan-keadaan stasioner $a_1$ dan $t_2$. Lebar pita $t_2$ (lebih dari 1 eV) berasal dari distorsi Jahn–Teller CH₄⁺ (Bab 14), yang memecah degenerasi rangkap tiga dalam ion.
:::

::: {.contoh}
**Contoh 12.47 · Invariansi determinan**

Dua elektron berspin α menempati orbital ortonormal $\phi_1$ dan $\phi_2$. (a) Tulis determinan Slater dan tunjukkan bahwa penggantian $\phi'_{1,2} = (\phi_1 \pm \phi_2)/\sqrt2$ hanya mengalikan determinan dengan $-1$. (b) Hitung $\det\mathbf U$ untuk transformasi (12.23) dan jelaskan mengapa tandanya tidak penting.

**Penyelesaian.** (a) $\Psi = \tfrac{1}{\sqrt2}[\phi_1(1)\phi_2(2) - \phi_2(1)\phi_1(2)]$. Dengan $\phi'$:
$\phi'_1(1)\phi'_2(2) - \phi'_2(1)\phi'_1(2) = \tfrac12[(\phi_1 + \phi_2)_1(\phi_1 - \phi_2)_2 - (\phi_1 - \phi_2)_1(\phi_1 + \phi_2)_2]$. Suku $\phi_1\phi_1$ dan $\phi_2\phi_2$ saling meniadakan; yang tersisa $\tfrac12[-2\phi_1(1)\phi_2(2) + 2\phi_2(1)\phi_1(2)] = -[\phi_1(1)\phi_2(2) - \phi_2(1)\phi_1(2)]$. Jadi $\Psi' = -\Psi$, sesuai $\det\mathbf U = \det\tfrac{1}{\sqrt2}\begin{pmatrix}1 & 1\\ 1 & -1\end{pmatrix} = -1$.

\(b) Contoh 12.16 memberikan $\det\mathbf U = -1$. Fungsi gelombang yang hanya berbeda faktor fase global ($-1$) menggambarkan keadaan fisis yang sama, karena semua besaran teramati bergantung pada $|\Psi|^2$ atau pada $\langle\Psi|\hat A|\Psi\rangle$.

**Memahami hasil.** Untuk elektron dengan spin yang sama, mencampur orbital-orbital terisi tidak mengubah apa pun. Ini bukan kebetulan aljabar: asas Pauli membuat determinan hanya bergantung pada **ruang** yang direntang oleh orbital-orbital terisi, bukan pada pilihan basis di dalam ruang itu. "Orbital" individual dalam molekul berelektron banyak karena itu tidak mempunyai makna fisis yang tunggal; maknanya baru muncul ketika kita menanyakan besaran tertentu, seperti energi ionisasi.
:::

::: {.contoh}
**Contoh 12.48 · Pasangan bebas air dalam spektrum fotoelektron**

Dua pasangan bebas setara "telinga kelinci" pada H₂O diionisasi. (a) Dengan model lubang $2 \times 2$, $\begin{pmatrix}\varepsilon' & \tau'\\ \tau' & \varepsilon'\end{pmatrix}$, cari $\varepsilon'$ dan $\tau'$ yang mereproduksi pita $1b_1$ (12,62 eV) dan $3a_1$ (14,74 eV). (b) Kombinasi mana yang sesuai dengan masing-masing pita? (c) Mengapa pita $1b_1$ jauh lebih sempit daripada $3a_1$?

**Penyelesaian.** (a) Nilai eigen $\varepsilon' \pm \tau'$: $\varepsilon' = 13{,}68$ eV, $\tau' = 1{,}06$ eV. (b) Kombinasi simetris $(n_+ + n_-)/\sqrt2 = n_\sigma$ terletak di bidang molekul dan bersimetri $a_1$; kombinasi antisimetris $(n_+ - n_-)/\sqrt2 = n_\pi$ tegak lurus bidang, bersimetri $b_1$. Orbital $n_\sigma$ yang kaya $s$ lebih terikat: 14,74 eV ($3a_1$). Orbital $n_\pi$, $p$ murni, paling mudah diionisasi: 12,62 eV ($1b_1$). (c) Elektron $1b_1$ praktis tidak berikatan, sehingga geometri ion H₂O⁺ ($^2B_1$) hampir sama dengan molekul netral: transisi vertikal hanya mengeksitasi sedikit getaran (prinsip Franck–Condon, Bab 15). Elektron $3a_1$ ikut berikatan dan menentukan sudut H–O–H; melepasnya mengubah geometri ion banyak, sehingga pitanya lebar.

**Memahami hasil.** Spektrum fotoelektron tidak "membuktikan" bahwa air mempunyai pasangan bebas σ dan π dan bukan telinga kelinci; ia menunjukkan bahwa keadaan-keadaan stasioner **ion** H₂O⁺ mengikuti simetri $C_{2v}$. Untuk menjelaskan ikatan hidrogen di es (susunan tetrahedral), telinga kelinci tetap gambaran yang berguna.
:::

::: {.kuis}
**Kuis cepat 12.13**

Etana mempunyai enam ikatan C–H yang setara dan satu ikatan C–C. Apakah spektrum fotoelektronnya akan menunjukkan satu pita untuk semua elektron C–H? Jelaskan dengan model lubang.
:::

## 12.14 Ikatan dalam senyawa logam transisi menurut teori ikatan valensi

### Hibrida Pauling untuk ion kompleks

Sebelum teori medan kristal dan medan ligan menjadi umum (Bab 14), Pauling (1931) menjelaskan ion kompleks dengan hibridisasi. Ligan dianggap mendonorkan pasangan elektron ke orbital hibrida kosong ion logam; geometri ditentukan oleh jenis hibrida, dan sifat magnet oleh banyaknya elektron $d$ yang tetap tak berpasangan.

* **Oktahedral $d^2sp^3$** (kompleks "orbital dalam"): dua orbital $(n-1)d$, satu $ns$, tiga $np$. Contoh: [Co(NH₃)₆]³⁺ ($d^6$). Enam elektron $d$ dijejalkan berpasangan ke tiga orbital $d$ yang tersisa ($d_{xy}$, $d_{xz}$, $d_{yz}$), sehingga kompleks ini **diamagnetik**.
* **Oktahedral $sp^3d^2$** (kompleks "orbital luar"): $ns$, tiga $np$, dua $nd$. Contoh: [CoF₆]³⁻. Kelima orbital $3d$ tidak terpakai untuk ikatan, sehingga keenam elektron $d$ menyebar menurut aturan Hund: empat elektron tak berpasangan, **paramagnetik**.
* **Bujur sangkar $dsp^2$**: satu $d_{x^2-y^2}$, $s$, $p_x$, $p_y$. Contoh: [Ni(CN)₄]²⁻ ($d^8$, diamagnetik), [PtCl₄]²⁻.
* **Tetrahedral $sp^3$**: [NiCl₄]²⁻ ($d^8$, dua elektron tak berpasangan), [Ni(CO)₄] ($d^{10}$).

Sifat magnet diuji dengan momen magnet efektif. Bila hanya spin yang menyumbang, $n$ elektron tak berpasangan memberi

$$
\mu_\text{ef} = \sqrt{n(n + 2)}\ \mu_\text{B} , \qquad \text{(12.44)}
$$

yaitu 1,73; 2,83; 3,87; 4,90; 5,92 $\mu_\text{B}$ untuk $n = 1$ sampai 5. Pengukuran kerentanan magnet dengan neraca Gouy dapat membedakan [Fe(CN)₆]³⁻ (satu elektron tak berpasangan) dari [Fe(H₂O)₆]³⁺ (lima), dan [Ni(CN)₄]²⁻ (nol, bujur sangkar) dari [NiCl₄]²⁻ (dua, tetrahedral). Untuk masanya, ini keberhasilan yang mengesankan: satu konsep (hibridisasi) menjelaskan sekaligus geometri dan magnetisme.

### Keterbatasan model Pauling

Model hibrida untuk kompleks perlahan ditinggalkan karena beberapa kegagalan mendasar:

1. **Tidak menjelaskan warna dan spektrum.** Model tidak mempunyai tingkat energi $d$ yang terpisah, sehingga tidak dapat menjelaskan serapan $d$–$d$ yang memberi kompleks warnanya, atau deret spektrokimia.
2. **Orbital $nd$ "luar" tidak masuk akal secara energi.** Orbital $4d$ untuk kobalt jauh di atas $3d$, $4s$, dan $4p$; menggunakan mereka untuk ikatan sama tidak meyakinkannya dengan $3d$ untuk belerang (subbab 12.8).
3. **Kasus Cu(II).** [Cu(NH₃)₄]²⁺ bujur sangkar ($d^9$). Hibrida $dsp^2$ menuntut satu elektron $d$ dipindahkan ke $4p$, yang seharusnya membuat kompleks mudah teroksidasi, padahal tidak.
4. **Tidak ada ukuran kuantitatif.** Model tidak menjelaskan mengapa CN⁻ membuat kompleks spin rendah dan F⁻ spin tinggi, atau mengapa kompleks $d^4$ dan $d^9$ oktahedral terdistorsi (efek Jahn–Teller).

Teori medan ligan (Bab 14), yang menggabungkan teori orbital molekul dengan simetri, menjawab semua ini dan menggantikan model Pauling untuk kompleks klasik.

### Kebangkitan: hibrida sd

Untuk senyawa organologam dan hidrida logam transisi, teori ikatan valensi kembali berguna dalam bentuk baru (C. R. Landis dan F. Weinhold, 1990-an). Analisis fungsi gelombang modern menunjukkan bahwa orbital $np$ logam transisi berperan kecil dalam ikatan (mirip peran $d$ pada unsur golongan utama), sehingga orbital valensi yang penting hanyalah $ns$ dan $(n-1)d$. Ikatan logam–ligan karena itu dibentuk oleh hibrida **sd$^n$**.

Sudut antarhibrida sd dapat diturunkan seperti sudut hibrida sp. Hibrida yang paling terarah ke $\mathbf n$ adalah campuran $s$ dan orbital $d_\sigma$ yang simetris silinder di sekitar $\mathbf n$ (yaitu $d_{z^2}$ bila $\mathbf n$ adalah sumbu $z$): $h = \sqrt\alpha\,s + \sqrt{1 - \alpha}\,d_{\sigma}(\mathbf n)$. Analog dengan (12.8), tumpang tindih dua orbital $d_\sigma$ yang menunjuk ke $\mathbf n_1$ dan $\mathbf n_2$ adalah polinom Legendre $P_2(\cos\theta) = \tfrac12(3\cos^2\theta - 1)$ (teorema penjumlahan harmonik bola, subbab 6.5). Syarat ortogonalitas:

$$
\alpha + (1 - \alpha)\,\tfrac12\left(3\cos^2\theta - 1\right) = 0 . \qquad \text{(12.45)}
$$

Untuk hibrida sd$^n$ setara, $\alpha = 1/(n + 1)$. Penyelesaiannya (Contoh 12.50): sd² memberi 90°; sd³ memberi 70,5° atau 109,5°; sd⁵ memberi 63,4° atau 116,6°. Berbeda dengan hibrida sp, hibrida sd mengizinkan **sudut lancip**, dan tidak pernah memberi 180° (karena $P_2(\cos\theta) \ge -\tfrac12$, sudut 180° memerlukan $P_2 = 1$, yang tidak mungkin dibuat negatif).

Ramalan yang paling mencolok menyangkut molekul MX₆ dengan logam $d^0$ dan enam ligan σ sederhana, misalnya WH₆ dan W(CH₃)₆. VSEPR (tanpa pasangan bebas) meramalkan oktahedron. Hibrida sd⁵ tidak dapat membentuk sudut 90° dan 180°; mereka menuntut sudut 63,4° dan 116,6°, yang dipenuhi oleh struktur **prisma segitiga** terdistorsi ($C_{3v}$). Struktur W(CH₃)₆ yang ditentukan dengan difraksi elektron dan kristalografi sinar-X memang bukan oktahedron, melainkan prisma segitiga yang terdistorsi, sesuai dengan ramalan ini.

### Aturan 18 elektron dan ikatan balik

Bila $np$ ikut diperhitungkan, logam transisi mempunyai sembilan orbital valensi ($ns$, lima $(n-1)d$, tiga $np$), yang dapat menampung 18 elektron. **Aturan 18 elektron** untuk senyawa organologam (Cr(CO)₆, Fe(CO)₅, Ni(CO)₄, ferosena) adalah analog oktet untuk logam transisi; Bab 14 menurunkannya dengan teori orbital molekul.

Teori ikatan valensi memberi bahasa yang sangat berguna untuk ikatan logam–karbonil melalui resonansi:

$$
\text{M}^{-}\!-\!\text{C}\!\equiv\!\text{O}^{+} \;\longleftrightarrow\; \text{M}\!=\!\text{C}\!=\!\text{O} .
$$

Struktur pertama melukiskan donasi σ dari karbon ke logam; struktur kedua melukiskan **ikatan balik π**: elektron $d$ logam masuk ke orbital π* CO, memperkuat ikatan M–C dan melemahkan ikatan C–O. Makin kaya elektron logamnya, makin besar bobot struktur kedua, dan makin rendah frekuensi ulur C–O. Deret isoelektronik Ni(CO)₄, [Co(CO)₄]⁻, [Fe(CO)₄]²⁻ memperlihatkannya dengan jelas (Contoh 12.52).

::: {.contoh}
**Contoh 12.49 · Magnetisme dan hibrida Pauling**

Untuk setiap kompleks, tentukan konfigurasi $d$ ion logam, hibrida Pauling, banyaknya elektron tak berpasangan, dan momen magnet spin saja: (a) [Fe(CN)₆]⁴⁻; (b) [Fe(H₂O)₆]²⁺; (c) [Fe(CN)₆]³⁻; (d) [Ni(CN)₄]²⁻; (e) [NiCl₄]²⁻.

**Penyelesaian.** (a) Fe²⁺ $d^6$, $d^2sp^3$ (orbital dalam): 0 tak berpasangan, 0 $\mu_\text{B}$. (b) Fe²⁺ $d^6$, $sp^3d^2$ (orbital luar): 4, $\sqrt{24} = 4{,}90\ \mu_\text{B}$. (c) Fe³⁺ $d^5$, $d^2sp^3$: lima elektron dalam tiga orbital $d$, 1 tak berpasangan, $\sqrt3 = 1{,}73\ \mu_\text{B}$. (d) Ni²⁺ $d^8$, $dsp^2$: delapan elektron dalam empat orbital $d$, 0. (e) Ni²⁺ $d^8$, $sp^3$: 2, $\sqrt8 = 2{,}83\ \mu_\text{B}$.

**Memahami hasil.** Nilai teramati untuk (c) sekitar 2,3 $\mu_\text{B}$ dan untuk (e) sekitar 3,5 $\mu_\text{B}$, lebih besar daripada nilai spin saja karena momentum sudut orbital ikut menyumbang. Model Pauling meramalkan banyaknya elektron tak berpasangan dengan benar, tetapi menempatkan alasannya pada hibrida, bukan pada pemisahan energi orbital $d$ oleh ligan. Teori medan kristal (subbab 14.5) akan memberi alasan yang benar: ligan medan kuat (CN⁻) memecah tingkat $d$ cukup besar untuk memaksa elektron berpasangan.
:::

::: {.contoh}
**Contoh 12.50 · Sudut hibrida sd$^n$**

Dari (12.45), hitung sudut antara dua hibrida setara sd², sd³, sd⁴, dan sd⁵. Apakah dua hibrida sd (50% $s$) setara dapat ortogonal?

**Penyelesaian.** (12.45) memberi $P_2(\cos\theta) = -\alpha/(1 - \alpha) = -1/n$, sehingga $\cos^2\theta = (1 - 2/n)/3$.

* sd² ($n = 2$): $\cos^2\theta = 0$, $\theta = 90°$.
* sd³ ($n = 3$): $\cos^2\theta = \tfrac19$, $\theta = 70{,}53°$ atau $109{,}47°$.
* sd⁴ ($n = 4$): $\cos^2\theta = \tfrac16$, $\theta = 65{,}91°$ atau $114{,}09°$.
* sd⁵ ($n = 5$): $\cos^2\theta = \tfrac15$, $\theta = 63{,}43°$ atau $116{,}57°$.

Untuk sd ($n = 1$): $\cos^2\theta = -\tfrac13$, tidak mungkin. Dua hibrida sd setara dengan bagian $d_\sigma$ murni tidak dapat ortogonal.

**Memahami hasil.** Hibrida sd³ menghasilkan sudut tetrahedral 109,47° (dan juga 70,53°), sehingga logam $d^0$ dengan empat ligan seperti TiCl₄ dapat tetrahedral dengan hibrida sd³ tanpa memerlukan orbital $p$. Untuk sd⁵, keenam ligan tidak dapat menempati sudut-sudut oktahedron (90°, 180°); struktur yang memenuhi sudut 63,4° dan 116,6° untuk semua pasangan berdekatan adalah prisma segitiga terdistorsi, seperti yang teramati pada W(CH₃)₆. Untuk dua ligan (sd), bentuk yang diramalkan bengkok di sekitar 90°, dan memang dihidrida logam $d^0$ seperti fragmen MH₂ dalam perhitungan cenderung bengkok, bukan linear.
:::

::: {.contoh}
**Contoh 12.51 · Hibrida dsp² bujur sangkar**

Hibrida bujur sangkar yang menunjuk ke $+x$ adalah $h_{+x} = \tfrac12s + \tfrac{1}{\sqrt2}p_x + \tfrac12d_{x^2-y^2}$, dan yang menunjuk ke $+y$ adalah $h_{+y} = \tfrac12s + \tfrac{1}{\sqrt2}p_y - \tfrac12d_{x^2-y^2}$. (a) Periksa ortonormalitasnya. (b) Hitung "kekuatan" Pauling, dengan amplitudo sudut $d_{x^2-y^2}$ ke arah $+x$ sebesar $\sqrt{15}/2$. (c) Tuliskan $h_{-x}$ dan $h_{-y}$.

**Penyelesaian.** (a) $\tfrac14 + \tfrac12 + \tfrac14 = 1$; $\langle h_{+x}|h_{+y}\rangle = \tfrac14 + 0 - \tfrac14 = 0$. (b) $f = \tfrac12 + \tfrac{\sqrt3}{\sqrt2} + \tfrac12\cdot\tfrac{\sqrt{15}}{2} = 0{,}500 + 1{,}225 + 0{,}968 = 2{,}693$. (c) $h_{-x} = \tfrac12s - \tfrac{1}{\sqrt2}p_x + \tfrac12d_{x^2-y^2}$, $h_{-y} = \tfrac12s - \tfrac{1}{\sqrt2}p_y - \tfrac12d_{x^2-y^2}$.

**Memahami hasil.** Tanda $d_{x^2-y^2}$ positif ke arah $\pm x$ dan negatif ke arah $\pm y$, sesuai bentuk daun semanggi orbital itu yang cuping positifnya di sumbu $x$ dan negatifnya di sumbu $y$. Kompleks bujur sangkar $d^8$ ([Ni(CN)₄]²⁻, [PtCl₄]²⁻, cisplatin) mengosongkan $d_{x^2-y^2}$ justru karena orbital itulah yang menunjuk ke keempat ligan; teori medan ligan menyatakan hal yang sama dengan bahasa energi orbital.
:::

::: {.contoh}
**Contoh 12.52 · Ikatan balik dan frekuensi C–O**

Frekuensi ulur C–O: CO bebas 2143 cm⁻¹, Ni(CO)₄ 2057 cm⁻¹, [Co(CO)₄]⁻ 1890 cm⁻¹, [Fe(CO)₄]²⁻ 1790 cm⁻¹. (a) Hitung perbandingan tetapan gaya C–O terhadap CO bebas (anggap massa tereduksi tetap). (b) Tafsirkan dengan struktur resonansi M=C=O.

**Penyelesaian.** (a) $k/k_0 = (\tilde\nu/\tilde\nu_0)^2$: Ni(CO)₄ 0,921; [Co(CO)₄]⁻ 0,778; [Fe(CO)₄]²⁻ 0,698.

\(b) Ketiga kompleks isoelektronik ($d^{10}$, tetrahedral). Dari Ni(0) ke Co(−I) ke Fe(−II), logam makin kaya elektron dan makin mudah mendonorkan elektron $d$ ke π* CO. Bobot struktur M=C=O bertambah, orde ikatan C–O turun dari mendekati tiga ke arah dua, dan tetapan gaya turun 30% pada [Fe(CO)₄]²⁻.

**Memahami hasil.** Frekuensi C–O adalah "sensor" kerapatan elektron logam yang paling banyak dipakai dalam kimia organologam. Dalam bahasa ikatan valensi, ia mengukur bobot resonansi; dalam bahasa orbital molekul (Bab 14), ia mengukur populasi π* CO. Kedua bahasa menceritakan hal yang sama.
:::

::: {.kuis}
**Kuis cepat 12.14**

Menurut model Pauling, kompleks [Mn(CN)₆]⁴⁻ ($d^5$) adalah orbital dalam. Berapa elektron tak berpasangan dan momen magnet spin sajanya? Berapa elektron valensi Fe(CO)₅ menurut aturan 18 elektron?
:::
