## 12.8 Orbital d dan hipervalensi: PCl₅, SF₆, ikatan tiga pusat empat elektron

### Molekul yang melampaui oktet

Nitrogen membentuk NCl₃ tetapi tidak NCl₅; fosfor membentuk PCl₃ **dan** PCl₅. Oksigen membentuk OF₂ tetapi tidak OF₄ atau OF₆; belerang membentuk SF₂, SF₄, **dan** SF₆. Gas mulia xenon membentuk XeF₂, XeF₄, dan XeF₆. Dalam struktur Lewis molekul-molekul ini, atom pusat dikelilingi lebih dari delapan elektron: sepuluh pada PCl₅, dua belas pada SF₆. Molekul seperti ini disebut **hipervalen** (J. I. Musher, 1969). Bagaimana teori ikatan valensi menjelaskannya?

### Model lama: hibrida sp³d dan sp³d²

Penjelasan klasik (Pauling) memakai orbital $3d$ yang kosong. Untuk PCl₅, satu elektron $3s$ dipromosikan ke $3d$: $3s^2 3p^3 \to 3s^1 3p^3 3d^1$, menghasilkan lima elektron tak berpasangan dan lima hibrida sp³d (sering ditulis dsp³) yang menunjuk ke sudut-sudut bipiramida segitiga. Untuk SF₆, dua elektron dipromosikan: $3s^2 3p^4 \to 3s^1 3p^3 3d^2$, menghasilkan enam hibrida sp³d² ($d^2sp^3$) yang menunjuk ke sudut-sudut oktahedron.

Hibrida oktahedral dapat diturunkan seperti hibrida sp³. Enam hibrida setara memerlukan karakter $s$ $\tfrac16$ masing-masing. Untuk hibrida yang menunjuk ke $\pm z$, hanya orbital yang simetris silinder di sekitar sumbu $z$ yang boleh ikut: $s$, $p_z$, dan $d_{z^2}$. Kekekalan orbital (setiap orbital $p$ dibagi ke dua hibrida yang berlawanan, dan kedua orbital $d$ yang dipakai, $d_{z^2}$ dan $d_{x^2-y^2}$, dibagi ke enam hibrida) memberikan

$$
h_{\pm z} = \frac{1}{\sqrt6}\,s \pm \frac{1}{\sqrt2}\,p_z + \frac{1}{\sqrt3}\,d_{z^2} , \qquad
h_{\pm x} = \frac{1}{\sqrt6}\,s \pm \frac{1}{\sqrt2}\,p_x - \frac{1}{\sqrt{12}}\,d_{z^2} + \frac12\,d_{x^2-y^2} , \qquad \text{(12.27)}
$$

dan $h_{\pm y}$ sama dengan $h_{\pm x}$ tetapi dengan $p_y$ dan $-\tfrac12d_{x^2-y^2}$. Keenam hibrida ini ortonormal (Contoh 12.30), dan "kekuatan" Pauling-nya 2,924, lebih besar daripada sp³.

Model ini rapi, tetapi menimbulkan pertanyaan yang tidak dapat diabaikan: apakah orbital $3d$ benar-benar cocok untuk ikatan?

### Mengapa model orbital d dipertanyakan

**Energi.** Keadaan atom belerang dengan konfigurasi $3s^2 3p^3 3d^1$ terletak jauh di atas keadaan dasar, tidak jauh di bawah batas ionisasi. Biaya promosi dua elektron ke $3d$ sangat besar dibanding energi yang dapat dikembalikan oleh dua ikatan tambahan.

**Ukuran.** Elektron $3d$ dalam atom netral hampir tidak merasakan muatan inti: semua elektron yang lebih dalam (termasuk elektron $3s$ dan $3p$) menyaringnya. Taksiran dengan aturan Slater memberikan jarak rata-rata elektron $3d$ belerang sekitar 5,6 Å, sedangkan $3p$ sekitar 1,0 Å (Contoh 12.28). Orbital yang begitu difus hampir tidak bertumpang tindih dengan orbital fluor pada jarak S–F 156 pm.

**Perhitungan modern.** Perhitungan *ab initio* untuk SF₆, PF₅, dan sejenisnya memang memerlukan fungsi basis $d$ untuk hasil yang baik, tetapi populasi elektron dalam fungsi $d$ itu hanya beberapa persepuluh elektron, bukan dua elektron penuh seperti yang dituntut sp³d². Fungsi $d$ berperan sebagai **fungsi polarisasi**: mereka membiarkan kerapatan elektron $p$ belerang sedikit berubah bentuk, bukan menyediakan orbital ikatan baru (Bab 17).

**Kimia.** Molekul hipervalen hampir selalu memerlukan ligan yang sangat elektronegatif (F, Cl, O). SF₆ sangat stabil, tetapi SH₆ tidak dikenal; PF₅ dan PCl₅ ada, tetapi PH₅ tidak. Jika ikatan dibentuk oleh hibrida sp³d² yang netral, tidak jelas mengapa ligan elektronegatif diperlukan. Model berikut menjelaskannya secara alami.

### Ikatan tiga pusat empat elektron

G. C. Pimentel dan R. E. Rundle (1951) mengusulkan model yang hanya memakai orbital $s$ dan $p$. Ambil molekul linear F–Xe–F. Xenon ($5s^2 5p^6$) mempunyai satu orbital $5p_z$ berisi dua elektron yang mengarah ke kedua F; setiap atom F mempunyai satu orbital $2p_z$ berisi satu elektron yang mengarah ke Xe. Tiga orbital dan empat elektron ini membentuk satu sistem **tiga pusat empat elektron** (3c-4e).

Dengan pendekatan sederhana yang akan dipakai lagi untuk sistem π di Bab 13, anggap setiap orbital mempunyai energi diagonal $\alpha$ (sama untuk semua, sebagai penyederhanaan pertama), unsur matriks $\beta < 0$ antara orbital-orbital yang bertetangga, nol antara kedua F, dan tumpang tindih diabaikan. Urutkan basisnya (F₁, Xe, F₂). Persamaan sekulernya

$$
\begin{vmatrix}\alpha - E & \beta & 0\\ \beta & \alpha - E & \beta\\ 0 & \beta & \alpha - E\end{vmatrix} = 0 . \qquad \text{(12.28)}
$$

Uraikan menurut baris pertama, dengan $x = \alpha - E$: $x(x^2 - \beta^2) - \beta(\beta x) = x(x^2 - 2\beta^2) = 0$. Jadi

$$
E_1 = \alpha + \sqrt2\,\beta , \qquad E_2 = \alpha , \qquad E_3 = \alpha - \sqrt2\,\beta . \qquad \text{(12.29)}
$$

Vektor eigennya, yang diperoleh dengan memasukkan setiap $E$ ke persamaan linear, adalah

$$
\psi_1 = \tfrac12\,\phi_{\text{F}_1} + \tfrac{1}{\sqrt2}\,\phi_\text{Xe} + \tfrac12\,\phi_{\text{F}_2} , \qquad
\psi_2 = \tfrac{1}{\sqrt2}\left(\phi_{\text{F}_1} - \phi_{\text{F}_2}\right) , \qquad
\psi_3 = \tfrac12\,\phi_{\text{F}_1} - \tfrac{1}{\sqrt2}\,\phi_\text{Xe} + \tfrac12\,\phi_{\text{F}_2} . \qquad \text{(12.30)}
$$

Orbital $\psi_1$ adalah orbital ikatan yang meliputi ketiga atom; $\psi_2$ adalah orbital **nonikatan** yang sama sekali tidak memuat Xe (koefisien Xe nol karena $\psi_2$ antisimetris terhadap pusat, sedangkan $p_z$ Xe, dengan pilihan tanda yang menunjuk ke masing-masing F, menyumbang secara simetris); $\psi_3$ antiikatan. Empat elektron mengisi $\psi_1$ dan $\psi_2$ (Gambar 12.7(a)).

![Gambar 12.7 Tingkat energi dan koefisien orbital (lingkaran; ukuran sebanding dengan besar koefisien, warna menunjukkan tanda) untuk sistem tiga orbital linear. (a) Ikatan tiga pusat empat elektron pada F–Xe–F: orbital ikatan dan nonikatan terisi. (b) Ikatan tiga pusat dua elektron pada jembatan B–H–B diborana: hanya orbital ikatan yang terisi.](fig/c_3pusat.png){width=86%}

Tiga akibat model ini menjelaskan kimia molekul hipervalen:

1. **Orde ikatan setengah.** Hanya satu pasangan ikatan yang dibagi ke dua ikatan Xe–F; setiap ikatan berorde $\tfrac12$. Ikatan 3c-4e lebih panjang dan lebih lemah daripada ikatan 2c-2e biasa.
2. **Muatan pindah ke ligan.** Populasi orbital dihitung dari kuadrat koefisien: setiap F mendapat $2(\tfrac14) + 2(\tfrac12) = 1{,}5$ elektron (semula 1), dan Xe mendapat $2(\tfrac12) = 1$ (semula 2). Ligan bermuatan $-\tfrac12$ masing-masing dan atom pusat $+1$. Struktur ini hanya stabil bila ligan cukup elektronegatif untuk menampung muatan negatif itu. Bila ligan dibuat lebih elektronegatif (energi $\alpha$ ligan diturunkan), pemindahan muatan makin besar dan orbital nonikatan makin terlokalisasi pada ligan (Contoh 12.29).
3. **Geometri linear.** Ikatan 3c-4e menggunakan satu orbital $p$ atom pusat untuk dua ligan yang saling berlawanan. Susunan X–A–X karena itu linear (atau hampir linear).

Dengan bahasa struktur resonansi, ikatan 3c-4e adalah resonansi antara F⁻ Xe⁺–F dan F–Xe⁺ F⁻: setiap struktur mematuhi oktet, dan resonansi membagi satu ikatan kovalen ke dua posisi. Kedua gambaran itu setara.

### Molekul hipervalen dalam bahasa 3c-4e

* **Trihalida dan bifluorida.** I₃⁻ linear, I–I sekitar 290 pm (I₂: 266,6 pm). HF₂⁻ linear dan simetris, F–H 113,9 pm (HF: 91,7 pm); inilah ikatan hidrogen terkuat yang dikenal, dan ia adalah ikatan 3c-4e dengan $1s$ hidrogen di pusat.
* **XeF₂, XeF₄.** XeF₂ satu sistem 3c-4e; XeF₄ (bujur sangkar) dua sistem 3c-4e yang saling tegak lurus, memakai $5p_x$ dan $5p_y$ Xe.
* **PF₅ dan PCl₅.** Tiga ikatan ekuatorial adalah ikatan 2c-2e biasa dengan hibrida sp² fosfor; dua ikatan aksial membentuk satu sistem 3c-4e dengan $3p_z$ fosfor. Ramalannya: ikatan aksial lebih panjang. Teramati: P–F aksial 157,7 pm vs ekuatorial 153,4 pm; P–Cl aksial 214 pm vs ekuatorial 202 pm. Karena ikatan aksial menumpuk muatan negatif di ligan, ligan elektronegatif memilih posisi aksial (aturan Bent di subbab 12.6 memberi kesimpulan yang sama).
* **SF₄ dan ClF₃.** SF₄ (jungkat-jungkit): dua S–F ekuatorial 154,5 pm (2c-2e) dan dua S–F aksial 164,6 pm (3c-4e). ClF₃ (bentuk T): satu Cl–F ekuatorial 159,8 pm dan dua aksial 169,8 pm.
* **SF₆.** Tiga sistem 3c-4e yang saling tegak lurus, dengan orbital $3s$ belerang menambah sedikit ikatan. Dalam bahasa orbital molekul: dari enam orbital σ ligan dan empat orbital valensi S ($s$, $p_x$, $p_y$, $p_z$), terbentuk empat orbital ikatan dan dua orbital nonikatan pada ligan (pasangan $e_g$). Dua belas elektron σ mengisi keenamnya: empat pasangan ikatan dibagi ke enam ikatan, sehingga orde setiap ikatan S–F $\tfrac23$, dan setiap F bermuatan negatif cukup besar.

::: {.inti}
**Hipervalensi tanpa orbital d.** Molekul hipervalen dapat dijelaskan dengan orbital $s$ dan $p$ saja melalui ikatan tiga pusat empat elektron. Ciri-cirinya: ikatan lebih panjang dan berorde kurang dari satu, pemindahan muatan ke ligan, kebutuhan akan ligan elektronegatif, dan susunan linear untuk setiap pasangan ligan yang berbagi satu orbital $p$. Orbital $d$ atom pusat berperan kecil sebagai fungsi polarisasi.
:::

::: {.contoh}
**Contoh 12.28 · Seberapa besar orbital 3d belerang?**

Pakai aturan Slater dan orbital Slater (dengan $\langle r\rangle = (2n + 1)/(2\zeta)$, $\zeta = Z_\text{ef}/n$, $n = 3$) untuk menaksir jarak rata-rata elektron (a) $3p$ belerang dalam keadaan dasar $3s^2 3p^4$; (b) $3d$ dalam $3s^2 3p^3 3d^1$; (c) $3d$ dalam ion S²⁺ dengan konfigurasi $3s^2 3p^1 3d^1$. Bandingkan dengan panjang ikatan S–F (156 pm).

**Penyelesaian.** (a) Penyaringan untuk $3p$: lima elektron $n = 3$ lainnya × 0,35, delapan elektron $n = 2$ × 0,85, dua elektron $n = 1$ × 1,00: $\sigma = 10{,}55$, $Z_\text{ef} = 5{,}45$, $\zeta = 1{,}817$, $\langle r\rangle = 7/(2 \times 1{,}817) = 1{,}93\,a_0 = 1{,}02$ Å.

\(b) Untuk elektron $d$, semua elektron di "bawahnya" (termasuk $3s$ dan $3p$) menyaring penuh: $\sigma = 15$, $Z_\text{ef} = 1$, $\zeta = \tfrac13$, $\langle r\rangle = 10{,}5\,a_0 = 5{,}56$ Å.

\(c) Dengan dua elektron lebih sedikit, $\sigma = 13$, $Z_\text{ef} = 3$, $\zeta = 1$, $\langle r\rangle = 3{,}5\,a_0 = 1{,}85$ Å.

**Memahami hasil.** Dalam atom netral orbital $3d$ lima kali lebih besar daripada $3p$ dan jauh melampaui panjang ikatan; ia praktis tidak dapat berikatan. Ketika ligan elektronegatif menarik elektron dari belerang, muatan inti efektif yang dirasakan $3d$ naik tajam dan orbitalnya mengerut ke ukuran ikatan. Ini satu-satunya cara orbital $d$ dapat sedikit berperan, dan sekali lagi ia menuntut ligan elektronegatif. Aturan Slater hanya kasar, tetapi selisih faktor lima tidak mungkin hilang karena perbaikan.
:::

::: {.contoh}
**Contoh 12.29 · Ikatan 3c-4e dengan ligan elektronegatif**

Ulangi perhitungan (12.28) dengan energi diagonal ligan diturunkan menjadi $\alpha - \delta|\beta|$ (ligan lebih elektronegatif). Untuk $\delta = 0$, 1, dan 2, hitung energi orbital, populasi elektron, dan muatan ligan bila empat elektron mengisi dua orbital terendah.

**Penyelesaian.** Dalam satuan $|\beta|$ dengan $\alpha = 0$ dan $\beta = -1$, matriksnya 
$$
\begin{pmatrix}-\delta & -1 & 0\\ -1 & 0 & -1\\ 0 & -1 & -\delta\end{pmatrix} .
$$

Diagonalisasi numerik memberikan:

| $\delta$ | Energi orbital | Populasi F, X, F | Muatan tiap F | Muatan X |
|---|---|---|---|---|
| 0 | $-1{,}414$; $0$; $+1{,}414$ | 1,50; 1,00; 1,50 | $-0{,}50$ | $+1{,}00$ |
| 1 | $-2{,}000$; $-1{,}000$; $+1{,}000$ | 1,67; 0,67; 1,67 | $-0{,}67$ | $+1{,}33$ |
| 2 | $-2{,}732$; $-2{,}000$; $+0{,}732$ | 1,79; 0,42; 1,79 | $-0{,}79$ | $+1{,}58$ |

Orbital nonikatan tetap $(\phi_{\text{F}_1} - \phi_{\text{F}_2})/\sqrt2$ dengan energi $\alpha - \delta|\beta|$, yaitu energi orbital ligan.

**Memahami hasil.** Makin elektronegatif ligan, makin rendah energi orbital nonikatan (yang berisi dua elektron), sehingga sistem 3c-4e makin stabil, dan makin besar pemindahan muatan ke ligan. Ini menjelaskan mengapa XeF₂ stabil sedangkan XeH₂ tidak dikenal, dan mengapa hampir semua senyawa gas mulia memakai F atau O.
:::

::: {.contoh}
**Contoh 12.30 · Hibrida oktahedral**

(a) Periksa bahwa $h_{+z}$ dan $h_{+x}$ dari (12.27) ternormalisasi dan saling ortogonal. (b) Hitung "kekuatan" Pauling $h_{+z}$ ke arah $+z$, dengan amplitudo sudut $s$ = 1, $p_z$ = $\sqrt3$, dan $d_{z^2}$ = $\sqrt5$ pada sumbu $z$.

**Penyelesaian.** (a) $\langle h_{+z}|h_{+z}\rangle = \tfrac16 + \tfrac12 + \tfrac13 = 1$. $\langle h_{+x}|h_{+x}\rangle = \tfrac16 + \tfrac12 + \tfrac{1}{12} + \tfrac14 = 1$. $\langle h_{+z}|h_{+x}\rangle = \tfrac16 + 0 + \tfrac{1}{\sqrt3}\left(-\tfrac{1}{\sqrt{12}}\right) + 0 = \tfrac16 - \tfrac16 = 0$.

\(b) $f = \tfrac{1}{\sqrt6} + \tfrac{\sqrt3}{\sqrt2} + \tfrac{\sqrt5}{\sqrt3} = 0{,}408 + 1{,}225 + 1{,}291 = 2{,}924$.

**Memahami hasil.** Secara matematis, hibrida $d^2sp^3$ sangat terarah, dan karena itu Pauling menganggapnya kuat. Masalahnya bukan bentuk sudutnya tetapi bagian radialnya: kekuatan 2,924 hanya bermakna bila $3d$ berukuran sama dengan $3s$ dan $3p$, yang tidak benar untuk unsur golongan utama (Contoh 12.28). Untuk logam transisi, yang orbital $(n-1)d$-nya kompak dan berenergi rendah, hibrida $d^2sp^3$ jauh lebih masuk akal (subbab 12.14).
:::

::: {.contoh}
**Contoh 12.31 · Panjang ikatan dan orde ikatan 3c-4e**

(a) Hitung perbandingan panjang ikatan aksial terhadap ekuatorial pada PF₅, PCl₅, SF₄, dan ClF₃, serta perbandingan I–I pada I₃⁻ terhadap I₂. (b) Pada SF₆ (S–F 156,1 pm), berapa orde ikatan S–F menurut hitungan orbital molekul di atas?

**Penyelesaian.** (a) PF₅: $157{,}7/153{,}4 = 1{,}028$. PCl₅: $214/202 = 1{,}059$. SF₄: $164{,}6/154{,}5 = 1{,}065$. ClF₃: $169{,}8/159{,}8 = 1{,}063$. I₃⁻/I₂: $290/266{,}6 = 1{,}088$. (b) Empat pasangan ikatan dibagi ke enam ikatan: orde $\tfrac46 = \tfrac23$.

**Memahami hasil.** Ikatan 3c-4e konsisten 3–9% lebih panjang daripada ikatan 2c-2e yang setara. PF₅ menunjukkan efek terkecil karena fluor ekuatorial dan aksial sama-sama sangat elektronegatif dan ikatan P–F sangat ionik. Orde ikatan $\tfrac23$ pada SF₆, ditambah tarikan elektrostatik antara S yang positif dan F yang negatif, menjelaskan kestabilan SF₆ yang luar biasa tanpa memerlukan dua belas elektron di sekitar belerang.
:::

::: {.kuis}
**Kuis cepat 12.8**

Berapa banyak sistem 3c-4e pada IF₅ (piramida bujur sangkar)? Mengapa NF₅ tidak ada walaupun PF₅ ada?
:::

## 12.9 Ikatan tiga pusat dua elektron: diborana

### Molekul yang "kekurangan" elektron

Boron membentuk hidrida yang paling sederhana, BH₃, hanya sebagai zat antara. Dua molekul BH₃ bergabung menjadi **diborana**, B₂H₆, dengan melepaskan sekitar 150 kJ/mol. Diborana mempunyai 12 elektron valensi (2 × 3 dari B, 6 × 1 dari H) dan delapan ikatan bila setiap pasangan B–H atau B–B digambar sebagai ikatan biasa. Dua belas elektron tidak cukup untuk delapan ikatan dua elektron. Senyawa seperti ini disebut **kekurangan elektron**.

### Struktur

Difraksi elektron menunjukkan struktur yang tidak mirip etana. Kedua atom boron dan empat atom H **ujung** terletak di satu bidang; dua atom H lainnya **menjembatani** kedua B, di atas dan di bawah bidang itu. Panjang B–H ujung 119 pm, B–H jembatan 133 pm, dan jarak B···B 176 pm. Setiap atom B dikelilingi empat H secara kira-kira tetrahedral: sudut H–B–H ujung sekitar 121°, sudut H–B–H jembatan sekitar 97°.

### Hibrida dan ikatan tiga pusat

Setiap boron dapat dilukiskan memakai empat hibrida kira-kira sp³ (setelah promosi $2s^2 2p \to 2s2p^2$, boron hanya mempunyai tiga elektron untuk empat hibrida). Dua hibrida membentuk ikatan 2c-2e biasa dengan H ujung, memakai 8 dari 12 elektron. Sisanya empat elektron untuk dua jembatan.

Di setiap jembatan, tiga orbital bertemu: satu hibrida dari B₁, orbital $1s$ dari H, dan satu hibrida dari B₂. Matriks Hamiltoniannya, dengan basis $(h_{B_1}, 1s_\text{H}, h_{B_2})$ dan interaksi langsung B–B diabaikan, sama dengan (12.28): tiga orbital tiga pusat $\alpha + \sqrt2\beta$, $\alpha$, $\alpha - \sqrt2\beta$. Bedanya, kini hanya **dua** elektron yang tersedia per jembatan. Keduanya mengisi orbital ikatan $\psi_1 = \tfrac12h_{B_1} + \tfrac{1}{\sqrt2}1s_\text{H} + \tfrac12h_{B_2}$ (Gambar 12.7(b)). Inilah **ikatan tiga pusat dua elektron** (3c-2e), yang biasa digambar sebagai busur atau "pisang" yang menghubungkan ketiga atom.

Populasi elektron: H jembatan mendapat $2 \times \tfrac12 = 1$ elektron (netral), setiap B mendapat $2 \times \tfrac14 = \tfrac12$ elektron dari jembatan ini. Orde setiap ikatan B–H jembatan $\tfrac12$, sesuai dengan panjangnya (133 pm) yang lebih besar daripada B–H ujung (119 pm).

### Mengapa 3c-2e melengkung dan 3c-4e lurus

Ada perbedaan mendasar antara kedua jenis ikatan tiga pusat. Pada jembatan B–H–B, kedua atom B cukup dekat (176 pm) sehingga hibrida-hibridanya juga bertumpang tindih langsung. Jika ketiga orbital saling berinteraksi (susunan segitiga), matriksnya menjadi 
$$
\begin{pmatrix}\alpha & \beta & \beta\\ \beta & \alpha & \beta\\ \beta & \beta & \alpha\end{pmatrix}
$$
 dengan nilai eigen $\alpha + 2\beta$ (sekali) dan $\alpha - \beta$ (dua kali). Dengan dua elektron, susunan segitiga memberi $2(\alpha + 2\beta)$, lebih rendah daripada susunan linear $2(\alpha + \sqrt2\beta)$. Dengan empat elektron sebaliknya: segitiga memberi $2(\alpha + 2\beta) + 2(\alpha - \beta) = 4\alpha + 2\beta$, sedangkan linear $4\alpha + 2\sqrt2\beta$, yang lebih rendah karena $\beta < 0$.

::: {.inti}
**Aturan ikatan tiga pusat.** Ikatan 3c-2e lebih stabil dalam susunan **tertutup** (melengkung, ketiga atom saling berdekatan): jembatan B–H–B, H₃⁺ segitiga. Ikatan 3c-4e lebih stabil dalam susunan **terbuka** (linear): F–Xe–F, I₃⁻, F–H–F⁻. Elektron ketiga dan keempat mengisi orbital yang bersifat antiikatan antara kedua atom ujung, sehingga atom-atom ujung lebih suka berjauhan.
:::

### Ikatan tiga pusat di tempat lain

* **H₃⁺**, ion paling sederhana dengan ikatan 3c-2e, berbentuk segitiga sama sisi (H–H 87 pm). Ion ini melimpah di ruang antarbintang dan memulai sebagian besar kimia awan molekul.
* **Trimetilaluminium** berupa dimer Al₂(CH₃)₆ dengan dua gugus metil jembatan; ikatan Al–C jembatan (sekitar 214 pm) lebih panjang daripada Al–C ujung (sekitar 196 pm).
* **Interaksi agostik**: ikatan C–H yang mendonorkan kerapatan ke atom logam yang kekurangan elektron, membentuk sistem tiga pusat M···H–C. Interaksi ini sering menjadi langkah awal pengaktifan C–H oleh logam transisi.
* **Karbokation nonklasik**: kation 2-norbornil dan CH₅⁺ distabilkan oleh ikatan 3c-2e C–H–C atau C–C–C.
* **Boran yang lebih besar**: B₄H₁₀, B₅H₉, B₁₀H₁₄, dan anion closo seperti B₁₂H₁₂²⁻ diikat oleh campuran ikatan 2c-2e dan 3c-2e (B–H–B dan B–B–B). W. N. Lipscomb menyusun pembukuan topologis untuk struktur-struktur ini (Contoh 12.33) dan memperoleh Hadiah Nobel 1976; K. Wade kemudian merumuskan aturan penghitungan pasangan elektron kerangka yang meramalkan bentuk polihedron boran.

::: {.contoh}
**Contoh 12.32 · Geometri jembatan diborana**

(a) Dari B–H jembatan 133,0 pm dan B···B 176,3 pm, hitung sudut B–H–B dan H–B–H jembatan. (b) Dari sudut H–B–H ujung 121°, hitung karakter $s$ hibrida B–H ujung dengan (12.17), lalu karakter $s$ hibrida jembatan dan sudut antara kedua hibrida jembatan. Bandingkan dengan sudut antarinti.

**Penyelesaian.** (a) Segi empat B–H–B–H adalah belah ketupat. Setengah sudut B–H–B: $\sin^{-1}(88{,}15/133{,}0) = 41{,}5°$, sehingga B–H–B $= 83{,}0°$ dan H–B–H jembatan $= 180° - 83{,}0° = 97{,}0°$.

\(b) $\cos121° = -0{,}5150$, $\alpha_\text{t} = 0{,}5150/1{,}5150 = 0{,}340$. Kekekalan: $\alpha_\text{b} = 0{,}5 - 0{,}340 = 0{,}160$. Sudut antarhibrida jembatan: $\arccos(-0{,}160/0{,}840) = 101{,}0°$, sedikit lebih besar daripada sudut antarinti 97,0°.

**Memahami hasil.** Hibrida jembatan miskin $s$ (16%) dan sedikit menyimpang dari garis B–H; tumpang tindih maksimumnya berada di dalam belah ketupat, ke arah atom B lawan. Inilah gambaran "pisang" ikatan 3c-2e. Sudut B–H–B yang kecil (83°) membawa kedua B cukup dekat (176 pm, hanya sedikit lebih panjang daripada ikatan B–B tunggal sekitar 170 pm) sehingga interaksi B···B ikut menstabilkan jembatan, sesuai aturan susunan tertutup untuk 3c-2e.
:::

::: {.contoh}
**Contoh 12.33 · Pembukuan styx Lipscomb**

Untuk boran B$_p$H$_{p+q}$, Lipscomb mendefinisikan $s$ = banyaknya jembatan B–H–B, $t$ = ikatan tiga pusat B–B–B, $y$ = ikatan B–B dua pusat, $x$ = gugus BH₂ (H ujung tambahan). Dengan anggapan setiap B mempunyai satu H ujung, kekekalan atom H, orbital, dan elektron memberikan

$$
s + x = q , \qquad s + t = p , \qquad t + y + \tfrac q2 = p .
$$

Tentukan $styx$ untuk B₂H₆, B₄H₁₀, dan B₅H₉.

**Penyelesaian.** B₂H₆ ($p = 2$, $q = 4$): $t + y = 0$, jadi $t = y = 0$, $s = 2$, $x = 2$: **2002**. B₄H₁₀ ($p = 4$, $q = 6$): $t + y = 1$; struktur dengan empat jembatan memberi $s = 4$, $t = 0$, $y = 1$, $x = 2$: **4012**. B₅H₉ ($p = 5$, $q = 4$): $t + y = 3$, $s + x = 4$, $s + t = 5$; dengan $x = 0$: $s = 4$, $t = 1$, $y = 2$: **4120**.

**Memahami hasil.** Persamaan Lipscomb adalah aturan kekekalan yang sama dengan kekekalan orbital dalam hibridisasi, diterapkan pada seluruh molekul. Mereka tidak menentukan struktur secara tunggal (B₄H₁₀ mempunyai beberapa penyelesaian bilangan bulat), tetapi menyaring kemungkinan, dan pilihan akhirnya ditentukan oleh simetri dan geometri yang diamati.
:::

::: {.contoh}
**Contoh 12.34 · H₃⁺: segitiga atau garis?**

Dengan model tiga orbital $1s$ (energi $\alpha$, interaksi tetangga $\beta$), hitung energi elektronik H₃⁺ (dua elektron) dalam bentuk segitiga sama sisi dan linear. Ulangi untuk H₃⁻ (empat elektron). Bentuk mana yang diramalkan?

**Penyelesaian.** Segitiga: nilai eigen $\alpha + 2\beta$, $\alpha - \beta$, $\alpha - \beta$. Linear: $\alpha + \sqrt2\beta$, $\alpha$, $\alpha - \sqrt2\beta$. Dua elektron: segitiga $2\alpha + 4\beta$, linear $2\alpha + 2{,}828\beta$; segitiga lebih rendah $1{,}17|\beta|$. Empat elektron: segitiga $4\alpha + 2\beta$, linear $4\alpha + 2{,}828\beta$; linear lebih rendah $0{,}83|\beta|$.

**Memahami hasil.** H₃⁺ segitiga sama sisi, sesuai percobaan. H₃⁻ (bila ada) linear, seperti F–H–F⁻ dan I₃⁻. Pola ini adalah versi paling sederhana dari aturan aromatisitas yang akan kita temui di Bab 13: sistem siklik dengan $4n + 2$ elektron (di sini $n = 0$, dua elektron) distabilkan oleh siklisasi, sedangkan sistem siklik dengan $4n$ elektron (empat) tidak.
:::

::: {.kuis}
**Kuis cepat 12.9**

Berapa elektron valensi pada Al₂Cl₆? Apakah jembatan Al–Cl–Al-nya ikatan 3c-2e atau ikatan dua pusat biasa? (Petunjuk: hitung pasangan bebas Cl.)
:::

## 12.10 Resonansi dalam teori ikatan valensi: benzena, karbonat, amida

### Struktur Kekulé sebagai fungsi gelombang

Untuk benzena, satu struktur Lewis tidak cukup: struktur Kekulé dengan ikatan tunggal dan rangkap bergantian meramalkan dua panjang ikatan C–C, padahal keenam ikatan benzena sama panjang (139,7 pm). Dalam teori ikatan valensi, setiap struktur Lewis adalah fungsi gelombang pasangan sempurna. Untuk enam elektron π dalam orbital $p_z$ yang diberi nomor 1 sampai 6 mengelilingi cincin, struktur Kekulé pertama memasangkan (1,2), (3,4), (5,6), dan struktur kedua (2,3), (4,5), (6,1). Masing-masing kita tulis $\Phi_\text{K1}$ dan $\Phi_\text{K2}$.

Fungsi gelombang yang lebih baik adalah kombinasi linear

$$
\Psi = c_1\Phi_\text{K1} + c_2\Phi_\text{K2} , \qquad \text{(12.31)}
$$

dengan koefisien yang ditentukan oleh metode variasi (subbab 8.4). Inilah arti kuantum **resonansi**: fungsi gelombang molekul adalah superposisi fungsi-fungsi gelombang struktur Lewis.

::: {.awas}
**Awas · Resonansi bukan kesetimbangan dan bukan getaran**

Benzena tidak berganti-ganti antara dua struktur Kekulé, dan tidak sebagian molekul berada dalam struktur satu dan sebagian dalam struktur lain. Setiap molekul benzena, setiap saat, berada dalam satu keadaan $\Psi$ yang tidak sama dengan $\Phi_\text{K1}$ maupun $\Phi_\text{K2}$. Struktur-struktur resonansi adalah fungsi basis untuk menyusun $\Psi$, sama seperti orbital $s$ dan $p$ adalah fungsi basis untuk menyusun hibrida. Analogi yang baik adalah bagal: keturunan kuda dan keledai, tetapi setiap saat bagal, bukan kadang kuda dan kadang keledai. Bandingkan dengan **tautomeri**, yang melibatkan perpindahan inti (misalnya keto–enol): tautomer-tautomer adalah molekul berbeda yang dapat dipisahkan, sedangkan struktur resonansi tidak.
:::

### Persamaan sekuler dua struktur

Fungsi pasangan sempurna dari struktur-struktur yang berbeda tidak ortogonal. Metode variasi untuk (12.31) menghasilkan persamaan sekuler

$$
\begin{vmatrix}H_{11} - ES_{11} & H_{12} - ES_{12}\\ H_{12} - ES_{12} & H_{22} - ES_{22}\end{vmatrix} = 0 , \qquad \text{(12.32)}
$$

dengan $H_{ij} = \langle\Phi_i|\hat H|\Phi_j\rangle$ dan $S_{ij} = \langle\Phi_i|\Phi_j\rangle$. Untuk benzena, simetri memberi $H_{11} = H_{22}$ dan $S_{11} = S_{22} = 1$, sehingga akar terendahnya (untuk $H_{12} < 0$)

$$
E = \frac{H_{11} + H_{12}}{1 + S_{12}} , \qquad c_1 = c_2 . \qquad \text{(12.33)}
$$

Unsur-unsur matriksnya dapat dihitung dengan Hamiltonian spin dari subbab 12.1, $\hat H = Q - J\sum_{\langle ij\rangle}(\tfrac12 + 2\hat{\mathbf s}_i\cdot\hat{\mathbf s}_j)$, dengan $J$ integral pertukaran antara orbital-orbital $p_z$ yang bertetangga (negatif). Hasilnya (Contoh 12.35):

$$
H_{11} = Q + \tfrac32J , \qquad S_{12} = \tfrac14 , \qquad H_{12} = \tfrac14\left(Q + 6J\right) . \qquad \text{(12.34)}
$$

Nilai $H_{11}$ mengikuti (12.4): tiga pasangan berikatan ($+3J$) dan tiga pasangan tetangga yang tidak berikatan ($-\tfrac32J$). Memasukkan ke (12.33):

$$
E = \frac{Q + \tfrac32J + \tfrac14Q + \tfrac32J}{\tfrac54} = Q + 2{,}4\,J . \qquad \text{(12.35)}
$$

Satu struktur Kekulé memberi $Q + 1{,}5J$; resonansi kedua struktur menurunkan energi sebesar $0{,}9|J|$. Inilah **energi resonansi** benzena dalam teori ikatan valensi. Bila tiga struktur Dewar (yang memasangkan dua atom yang berseberangan) ikut dimasukkan, kelima struktur bersama-sama merentang seluruh ruang singlet enam elektron (Contoh 12.4), dan energinya menjadi $Q + 2{,}606J$; energi resonansinya $1{,}106|J|$ (Gambar 12.8(b)). Struktur Kekulé menyumbang 64% fungsi gelombang dan struktur Dewar 36% (bobot Chirgwin–Coulson, Contoh 12.35).

![Gambar 12.8 Energi resonansi benzena. (a) Dari entalpi hidrogenasi: tiga kali entalpi hidrogenasi sikloheksena dibandingkan dengan entalpi hidrogenasi benzena. (b) Dari teori ikatan valensi dengan Hamiltonian spin: satu struktur Kekulé, resonansi dua struktur Kekulé, dan kelima struktur kovalen ($J < 0$).](fig/c_benzena.png){width=92%}

### Energi resonansi dari percobaan

Entalpi hidrogenasi sikloheksena menjadi sikloheksana adalah $-119{,}7$ kJ/mol. Bila benzena adalah "sikloheksatriena" dengan tiga ikatan rangkap yang tidak saling berinteraksi, hidrogenasinya akan melepaskan $3 \times 119{,}7 = 359{,}1$ kJ/mol. Nilai terukur hanya 208,4 kJ/mol. Selisihnya, 150,7 kJ/mol, adalah energi resonansi termokimia (Gambar 12.8(a)). Bila disamakan dengan $1{,}106|J|$, kita memperoleh $|J| \approx 136$ kJ/mol, besaran yang masuk akal untuk pertukaran antara dua orbital $p_z$ bertetangga.

### Aturan menulis struktur resonansi

Agar dapat dipakai sebagai fungsi basis dalam (12.31), struktur-struktur resonansi harus:

1. **mempunyai kedudukan inti yang sama**: hanya elektron yang dipindahkan;
2. **mempunyai banyaknya elektron tak berpasangan yang sama** (spin total yang sama), karena fungsi dengan spin berbeda ortogonal dan tidak bercampur;
3. **berenergi tidak terlalu berbeda**: struktur yang energinya jauh lebih tinggi hanya mendapat bobot kecil. Struktur dengan pemisahan muatan, muatan pada atom yang "salah" (positif pada atom elektronegatif), atau oktet yang tidak lengkap berbobot kecil.

Bila dua atau lebih struktur setara oleh simetri, bobotnya sama dan stabilisasi resonansinya paling besar (benzena, karbonat, karboksilat). Bila struktur-strukturnya tidak setara, struktur yang lebih stabil mendominasi, tetapi struktur minor tetap dapat menjelaskan sifat-sifat penting, seperti pada amida.

### Karbonat, nitrat, karboksilat

Ion karbonat CO₃²⁻ mempunyai tiga struktur setara, masing-masing dengan satu C=O dan dua C–O⁻. Resonansi memberi tiga ikatan C–O yang setara dengan orde $1\tfrac13$ dan muatan $-\tfrac23$ pada setiap O. Panjang C–O dalam kalsit, 129 pm, terletak di antara C–O tunggal (sekitar 134 pm untuk karbon sp²) dan C=O (sekitar 121 pm). Ion nitrat NO₃⁻ (N–O 125 pm) dan ion karboksilat RCO₂⁻ (dua C–O setara, sekitar 126 pm) mengikuti pola yang sama. Delokalisasi muatan pada dua atom O adalah sebab utama asam karboksilat (pK$_a$ sekitar 4–5) jauh lebih asam daripada alkohol (pK$_a$ sekitar 16): basa konjugatnya distabilkan resonansi.

### Amida dan ikatan peptida

Amida mempunyai dua struktur yang tidak setara: struktur utama R–C(=O)–NR₂ dan struktur dipolar R–C(–O⁻)=N⁺R₂. Struktur dipolar berbobot lebih kecil, tetapi akibatnya besar:

* **Ikatan C–N berkarakter rangkap parsial.** C–N amida (sekitar 133–135 pm) jauh lebih pendek daripada C–N amina (147 pm).
* **Kerangka datar dan rotasi terhalang.** Ikatan π parsial C=N menuntut atom O, C, N, dan kedua substituen N sebidang, dan rotasi di sekitar C–N memerlukan sekitar 70–90 kJ/mol. Pada dimetilformamida, kedua gugus metil terlihat sebagai dua sinyal NMR terpisah pada suhu kamar.
* **Nitrogen tidak basa.** Pasangan bebas N terdelokalisasi ke gugus karbonil; amida diprotonasi pada O, bukan N.
* **Struktur protein.** Kedataran ikatan peptida membatasi kebebasan konformasi rantai protein menjadi dua sudut puntir per residu ($\phi$ dan $\psi$), dasar diagram Ramachandran dan pembentukan heliks α dan lembaran β. Pauling memakai kedataran ini untuk meramalkan heliks α pada tahun 1951.

::: {.contoh}
**Contoh 12.35 · Benzena dengan Hamiltonian spin**

Susun ruang spin 6 elektron ($2^6 = 64$ keadaan), bangun $\hat H/|J| = -\sum_{\langle ij\rangle}(\tfrac12 + 2\hat{\mathbf s}_i\cdot\hat{\mathbf s}_j)$ untuk cincin (dengan $Q = 0$ dan energi dinyatakan sebagai $E = x\,J$), lalu hitung $S_{12}$, $H_{11}$, $H_{12}$ untuk struktur Kekulé, energi resonansi dua dan lima struktur, dan bobot struktur.

**Penyelesaian.**

```python
import numpy as np, itertools
from scipy.linalg import eigh
N = 6; I2 = np.eye(2)
s = [np.array([[0, 1], [1, 0]])/2, np.array([[0, -1j], [1j, 0]])/2, np.diag([.5, -.5])]
def op(o, i):                       # operator spin pada elektron i
    m = np.array([[1.]])
    for k in range(N): m = np.kron(m, o if k == i else I2)
    return m
H = sum(-(0.5*np.eye(64) + 2*sum(op(o, i) @ op(o, (i+1) % N) for o in s).real) for i in range(N))
def struktur(pasangan):             # hasil kali singlet (ab - ba)/sqrt2
    v = np.zeros(64)
    for b in itertools.product([0, 1], repeat=3):
        spin, tanda = [0]*N, 1
        for (i, j), bi in zip(pasangan, b):
            spin[i], spin[j] = bi, 1 - bi; tanda *= -1 if bi else 1
        v[int(''.join(map(str, spin)), 2)] += tanda
    return v / np.sqrt(8)
K1 = struktur([(0, 1), (2, 3), (4, 5)]); K2 = struktur([(1, 2), (3, 4), (5, 0)])
D = [struktur(p) for p in ([(0, 3), (1, 2), (4, 5)], [(1, 4), (2, 3), (5, 0)], [(2, 5), (3, 4), (0, 1)])]
print(K1 @ K2, K1 @ H @ K1, K1 @ H @ K2)            # S12, H11, H12
B = [K1, K2] + D
Hm = np.array([[a @ H @ b for b in B] for a in B]); Sm = np.array([[a @ b for b in B] for a in B])
for n in (2, 5):
    e, c = eigh(Hm[:n, :n], Sm[:n, :n]); print(n, e.max())
c = c[:, -1]; print(c * (Sm @ c))                     # bobot Chirgwin-Coulson
```

Keluarannya: $S_{12} = -0{,}25$, $H_{11} = 1{,}5$, $H_{12} = -1{,}5$ (tanda $S_{12}$ dan $H_{12}$ bergantung pada urutan pasangan; dengan konvensi Rumer keduanya positif dan $H_{12} = S_{12}(Q + 6J)$). Akar yang relevan (terbesar, karena $J < 0$): dua struktur $x = 2{,}400$, lima struktur $x = 2{,}606$. Bobot: setiap Kekulé 0,319, setiap Dewar 0,120.

**Memahami hasil.** Energi resonansi terhadap satu Kekulé: $0{,}900|J|$ (dua struktur) dan $1{,}106|J|$ (lima struktur). Hasil lima struktur sama dengan keadaan dasar eksak model Heisenberg cincin enam (nilai eigen terbesar $\hat H$ dalam ruang 64 dimensi), karena lima struktur merentang seluruh ruang singlet. Perbandingan koefisien Dewar terhadap Kekulé, 0,434, adalah hasil klasik Pauling dan Wheland (1933). Bobot Chirgwin–Coulson $w_i = c_i\sum_jS_{ij}c_j$ berjumlah satu walaupun fungsi basisnya tidak ortogonal.
:::

::: {.contoh}
**Contoh 12.36 · Energi resonansi termokimia**

(a) Hitung energi resonansi benzena dari entalpi hidrogenasi sikloheksena ($-119{,}7$ kJ/mol) dan benzena ($-208{,}4$ kJ/mol). (b) Taksir $|J|$ bila energi resonansi disamakan dengan $0{,}900|J|$ dan dengan $1{,}106|J|$. Nyatakan dalam eV.

**Penyelesaian.** (a) $3(119{,}7) - 208{,}4 = 150{,}7$ kJ/mol. (b) $150{,}7/0{,}900 = 167$ kJ/mol $= 1{,}74$ eV; $150{,}7/1{,}106 = 136$ kJ/mol $= 1{,}41$ eV.

**Memahami hasil.** Angka $|J|$ yang diperoleh bergantung pada model, dan "energi resonansi termokimia" bergantung pada pilihan senyawa pembanding (sikloheksena mempunyai karbon sp³ yang tidak ada pada benzena). Energi resonansi bukan besaran yang dapat diukur langsung; ia selalu selisih antara molekul nyata dan rujukan khayalan. Yang tidak bergantung pada pilihan rujukan adalah kesimpulan kualitatifnya: benzena distabilkan lebih dari 100 kJ/mol dibanding struktur dengan ikatan rangkap terlokalisasi, cukup untuk membuat reaksi adisi pada benzena jauh lebih sulit daripada pada alkena.
:::

::: {.contoh}
**Contoh 12.37 · Orde ikatan dari panjang ikatan**

Pakai rumus empiris $r(n) = r_1 - b\ln n$, dengan $n$ orde ikatan dan $b$ ditentukan dari $r_1$ (tunggal) dan $r_2$ (rangkap). (a) Untuk C–C, pakai $r_1 = 153{,}5$ pm (etana), $r_2 = 133{,}9$ pm; hitung orde ikatan benzena (139,7 pm). (b) Ulangi dengan rujukan tunggal sp²–sp², $r_1 = 146{,}7$ pm. (c) Pakai cara (b) untuk karbonat (C–O 129,0 pm; $r_1 = 134{,}0$, $r_2 = 120{,}8$ pm) dan amida (C–N 135,2 pm; $r_1 = 140{,}0$, $r_2 = 127{,}3$ pm).

**Penyelesaian.** (a) $b = 19{,}6/\ln2 = 28{,}3$ pm; $n = \exp[(153{,}5 - 139{,}7)/28{,}3] = 1{,}63$. (b) $b = 12{,}8/\ln2 = 18{,}5$ pm; $n = \exp[(146{,}7 - 139{,}7)/18{,}5] = 1{,}46$. (c) Karbonat: $b = 19{,}0$ pm, $n = \exp(5{,}0/19{,}0) = 1{,}30$. Amida: $b = 18{,}3$ pm, $n = \exp(4{,}8/18{,}3) = 1{,}30$.

**Memahami hasil.** Dengan rujukan sp³ (a), benzena tampak berorde 1,63, berlebihan. Dengan rujukan yang memperhitungkan hibridisasi (b), hasilnya 1,46, dekat dengan 1,5 dari resonansi dua struktur Kekulé. Pelajaran dari subbab 12.7 berlaku di sini: sebelum menafsirkan pemendekan ikatan sebagai resonansi, pisahkan dulu efek hibridisasi. Karbonat (1,30) dekat dengan $1\tfrac13$, dan amida berorde sekitar 1,3: struktur dipolar menyumbang sekitar 30%.
:::

::: {.contoh}
**Contoh 12.38 · Mengapa amida datar dan tidak basa**

Bila struktur dipolar amida berbobot 30%, (a) berapa muatan parsial yang diramalkan pada O dan N (dari struktur dipolar saja)? (b) Bila rotasi C–N memerlukan sekitar 80 kJ/mol, berapa laju rotasi pada 298 K menurut $k \approx (k_BT/h)e^{-\Delta G^\ddagger/RT}$? (c) Mengapa protonasi terjadi pada O?

**Penyelesaian.** (a) Struktur dipolar memberi $-1$ pada O dan $+1$ pada N; dengan bobot 0,30, muatan formal rata-ratanya $-0{,}3$ (O) dan $+0{,}3$ (N), di atas polarisasi C=O biasa. (b) $k_BT/h = 6{,}21 \times 10^{12}$ s⁻¹; $e^{-80/2{,}479} = 9{,}5 \times 10^{-15}$; $k \approx 0{,}06$ s⁻¹, sehingga satu rotasi memerlukan belasan detik. (c) Protonasi pada N menghancurkan resonansi (pasangan bebas N tidak lagi dapat didelokalisasi), sedangkan protonasi pada O mempertahankannya: kation yang terbentuk, R–C(OH)=N⁺R₂ ↔ R–C⁺(OH)–NR₂, masih distabilkan resonansi.

**Memahami hasil.** Laju rotasi di sekitar 0,1 s⁻¹ cukup lambat untuk dilihat sebagai dua sinyal NMR yang terpisah, dan cukup cepat untuk menyatu bila larutan dipanaskan sekitar 100 °C. Nitrogen amida yang positif sebagian dan oksigen yang negatif sebagian membuat N–H amida donor ikatan hidrogen yang baik dan C=O akseptor yang baik: pasangan donor–akseptor inilah yang menyusun struktur sekunder protein.
:::

::: {.kuis}
**Kuis cepat 12.10**

Tuliskan struktur resonansi ozon, O₃. Mengapa kedua ikatan O–O sama panjang (127,8 pm), dan mengapa panjangnya di antara O–O tunggal (147,5 pm pada H₂O₂) dan O=O (120,7 pm pada O₂)?
:::
