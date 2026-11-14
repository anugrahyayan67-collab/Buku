## 11.10 Molekul hidrogen: teori OM

### Hamiltonian dua elektron

Molekul H₂ menambahkan satu elektron pada H₂⁺, dan bersamanya satu suku baru yang mengubah segalanya: tolakan antarelektron. Dengan inti diam, dalam satuan atom,

$$
\hat H_\text{el} = \underbrace{-\tfrac12\nabla_1^2 - \frac{1}{r_{A1}} - \frac{1}{r_{B1}}}_{\hat h(1)} \underbrace{-\tfrac12\nabla_2^2 - \frac{1}{r_{A2}} - \frac{1}{r_{B2}}}_{\hat h(2)} + \frac{1}{r_{12}} + \frac1R . \qquad \text{(11.21)}
$$

Tanpa $1/r_{12}$, Hamiltonian ini adalah jumlah dua Hamiltonian H₂⁺, dan setiap elektron dapat menempati orbital H₂⁺ sendiri-sendiri. Suku $1/r_{12}$ mengikat gerak kedua elektron sehingga persamaannya tidak dapat diselesaikan eksak. Ada dua strategi pendekatan klasik, yang lahir hampir bersamaan pada akhir 1920-an: teori **orbital molekul** (OM; Hund, Mulliken) dan teori **ikatan valensi** (IV; Heitler, London, Pauling). Keduanya dibahas di subbab ini dan subbab berikutnya, lalu dibandingkan di subbab 11.12.

### Fungsi gelombang OM

Dalam teori OM, kedua elektron ditempatkan dalam orbital ikatan $\sigma_g$ yang sama dengan spin berlawanan, seperti dua elektron dalam orbital 1s helium. Fungsi gelombangnya, yang harus antisimetris terhadap pertukaran elektron (subbab 9.3), adalah determinan Slater

$$
\Psi_\text{OM} = \sigma_g(1)\sigma_g(2)\cdot\frac{1}{\sqrt2}\left[\alpha(1)\beta(2) - \beta(1)\alpha(2)\right], \qquad \sigma_g = \frac{1s_A + 1s_B}{\sqrt{2(1 + S)}} . \qquad \text{(11.22)}
$$

Bagian ruangnya simetris dan bagian spinnya adalah fungsi singlet yang antisimetris; hasil kalinya antisimetris sesuai asas Pauli. Karena $\hat H_\text{el}$ tidak memuat spin, energinya

$$
E_\text{OM} = \langle\sigma_g\sigma_g|\hat h(1) + \hat h(2) + \tfrac{1}{r_{12}}|\sigma_g\sigma_g\rangle + \frac1R = 2h_{\sigma\sigma} + J_{\sigma\sigma} + \frac1R , \qquad \text{(11.23)}
$$

dengan $h_{\sigma\sigma} = \langle\sigma_g|\hat h|\sigma_g\rangle$ energi satu elektron (energi orbital H₂⁺ tanpa $1/R$) dan

$$
J_{\sigma\sigma} = \iint\frac{|\sigma_g(1)|^2|\sigma_g(2)|^2}{r_{12}}\,d\tau_1d\tau_2
$$

tolakan Coulomb antara dua awan elektron yang identik. Dengan menguraikan $\sigma_g$ atas orbital atom, $J_{\sigma\sigma}$ menjadi kombinasi empat jenis **integral dua elektron**, yang ditulis dengan notasi $(ij|kl) = \iint\phi_i(1)\phi_j(1)\,r_{12}^{-1}\,\phi_k(2)\phi_l(2)\,d\tau_1d\tau_2$:

$$
J_{\sigma\sigma} = \frac{(aa|aa) + (aa|bb) + 2(ab|ab) + 4(aa|ab)}{2(1 + S)^2} , \qquad \text{(11.24)}
$$

dengan $a = 1s_A$ dan $b = 1s_B$. Keempatnya mempunyai makna yang jelas: $(aa|aa)$ tolakan dua elektron di atom yang sama (untuk 1s dengan eksponen $\zeta$, nilainya $5\zeta/8$); $(aa|bb)$ tolakan antara awan di $A$ dan awan di $B$; $(aa|ab)$ tolakan antara awan di $A$ dan kerapatan tumpang tindih; dan $(ab|ab)$ tolakan diri kerapatan tumpang tindih. Semuanya dapat dihitung dalam bentuk tertutup (yang terakhir memuat fungsi integral eksponensial), dan program kimia kuantum menghitung jutaan integral seperti ini dengan orbital Gauss (subbab 17.5).

::: {.contoh}
**Contoh 11.38 · Menyusun energi OM dari integral**

Pada $R = 1{,}4$ bohr dengan $\zeta = 1$: $S = 0{,}7529$, $H_{aa} = \langle a|\hat h|a\rangle = -1{,}1100$, $H_{ab} = -0{,}9683$, $(aa|aa) = 0{,}6250$, $(aa|bb) = 0{,}5035$, $(aa|ab) = 0{,}4259$, $(ab|ab) = 0{,}3233$ (semua dalam hartree). Hitung $E_\text{OM}$ dan energi ikat terhadap dua atom H.

**Penyelesaian.** $h_{\sigma\sigma} = (H_{aa} + H_{ab})/(1 + S) = (-1{,}1100 - 0{,}9683)/1{,}7529 = -1{,}1856$. Dengan (11.24): $J_{\sigma\sigma} = [0{,}6250 + 0{,}5035 + 2(0{,}3233) + 4(0{,}4259)]/[2(1{,}7529)^2] = 3{,}4787/6{,}1453 = 0{,}5660$. Maka $E_\text{OM} = 2(-1{,}1856) + 0{,}5660 + 1/1{,}4 = -2{,}3712 + 0{,}5660 + 0{,}7143 = -1{,}0909$ hartree. Energi ikat: $-1 - (-1{,}0909) = 0{,}0909$ hartree $= 2{,}47$ eV.

**Memahami hasil.** Dua elektron di orbital ikatan menurunkan energi sebanyak $2 \times 1{,}186$ hartree, tetapi tolakan di antara keduanya menaikkannya lagi 0,566 hartree: hampir sepertiga keuntungan dimakan tolakan antarelektron. Itulah sebabnya H₂ tidak terikat dua kali sekuat H₂⁺ (Contoh 11.10). Pada $R = 1{,}4$ bohr hasil OM ($\zeta = 1$) memberi 2,47 eV; minimumnya sedikit lebih dalam, 2,70 eV pada $R = 1{,}60$ bohr.
:::

### Hasil OM dan perbaikannya

Kurva $E_\text{OM}(R)$ dengan $\zeta = 1$ mempunyai minimum pada $R_e = 1{,}60$ bohr (85 pm) dengan $D_e = 2{,}70$ eV. Bila $\zeta$ dioptimalkan pada setiap $R$, diperoleh $\zeta = 1{,}19$, $R_e = 1{,}385$ bohr (73,3 pm), dan $D_e = 3{,}49$ eV. Bila orbital $\sigma_g$ diberi kebebasan penuh (basis yang sangat besar), hasilnya adalah **batas Hartree–Fock**: $D_e = 3{,}64$ eV. Nilai eksaknya 4,75 eV. Jadi bahkan orbital molekul terbaik masih kehilangan sekitar 1,1 eV, hampir seperempat energi ikat. Kehilangan ini bukan karena orbitalnya kurang baik, tetapi karena bentuk fungsi gelombang (11.22) itu sendiri, yang memperlakukan setiap elektron seolah bergerak dalam medan rata-rata elektron lain.

::: {.contoh}
**Contoh 11.39 · Energi orbital dan energi ionisasi**

Dengan $\zeta$ optimal pada jarak setimbang, energi orbital $\sigma_g$ H₂ (yaitu $\varepsilon = h_{\sigma\sigma} + J_{\sigma\sigma}$, energi satu elektron dalam medan inti dan medan rata-rata elektron lain) adalah $-0{,}5973$ hartree. Bandingkan $-\varepsilon$ dengan energi ionisasi vertikal H₂, sekitar 16,0 eV.

**Penyelesaian.** $-\varepsilon = 0{,}5973 \times 27{,}211 = 16{,}25$ eV.

**Memahami hasil.** Selisihnya dengan pengukuran hanya sekitar 0,3 eV (2%). Kesetaraan "energi ionisasi ≈ minus energi orbital" disebut **teorema Koopmans** (subbab 17.4): bila orbital yang tersisa tidak berubah setelah satu elektron dilepas, energi yang diperlukan tepat $-\varepsilon$. Inilah dasar penafsiran spektrum fotoelektron dengan diagram OM yang dipakai sepanjang bab ini dan Bab 10.
:::

### Kegagalan OM pada disosiasi

Masalah terbesar fungsi gelombang OM tampak ketika ikatan diputus. Uraikan bagian ruangnya atas orbital atom (tanpa faktor normalisasi):

$$
\sigma_g(1)\sigma_g(2) \propto [a(1) + b(1)][a(2) + b(2)] = \underbrace{a(1)b(2) + b(1)a(2)}_{\text{kovalen: H–H}} + \underbrace{a(1)a(2) + b(1)b(2)}_{\text{ionik: H}^-\text{H}^+\text{ dan H}^+\text{H}^-} . \qquad \text{(11.25)}
$$

Fungsi OM memberi bobot yang **sama** pada struktur kovalen (satu elektron di setiap atom) dan struktur ionik (kedua elektron di satu atom). Di dekat jarak setimbang, kesalahan ini tidak terlalu parah. Tetapi ketika $R \to \infty$, fungsi OM tetap bersikeras bahwa separuh waktu molekul berupa H⁺ + H⁻, padahal H₂ yang terdisosiasi semestinya menjadi dua atom H netral. Energi H⁻ jauh di atas energi dua atom H, sehingga kurva OM naik ke nilai yang salah (Gambar 11.9).

::: {.contoh}
**Contoh 11.40 · Seberapa salah OM pada disosiasi?**

Dengan basis minimal ($\zeta = 1$), energi H⁻ (dua elektron dalam 1s yang sama) adalah $2(-\tfrac12) + (aa|aa) = -1 + \tfrac58 = -0{,}375$ hartree. Hitung energi OM pada $R \to \infty$ dan kesalahannya terhadap $2E(\text{H}) = -1$ hartree. Bandingkan dengan nilai yang dihitung pada $R = 10$ dan 20 bohr: $-0{,}7386$ dan $-0{,}7125$ hartree.

**Penyelesaian.** Separuh kovalen ($-1$) dan separuh ionik ($-0{,}375$): $E_\text{OM}(\infty) = \tfrac12(-1) + \tfrac12(-0{,}375) = -0{,}6875$ hartree. Kesalahan: $0{,}3125$ hartree $= 8{,}50$ eV. Nilai pada $R = 10$ dan 20 bohr mendekati batas itu perlahan, karena tarikan Coulomb $-1/R$ antara H⁺ dan H⁻ pada bagian ionik masih terasa.

**Memahami hasil.** Kesalahan disosiasi sebesar 8,5 eV, hampir dua kali energi ikat itu sendiri, membuat teori OM sederhana tidak dapat dipakai untuk menggambarkan pemutusan ikatan, padahal pemutusan ikatan adalah inti setiap reaksi kimia. Kegagalan ini adalah contoh paling bersih dari **korelasi statik** (atau korelasi kiri–kanan): dua elektron "seharusnya" menghindari atom yang sama, tetapi fungsi gelombang satu determinan tidak dapat mengungkapkan penghindaran itu. Kita memperbaikinya di subbab 11.12.
:::

::: {.kuis}
**Kuis cepat 11.10**

\(a) Mengapa fungsi ruang OM H₂ simetris terhadap pertukaran elektron? (b) Apa makna fisis integral $(aa|aa)$? (c) Mengapa teori OM sederhana memberi energi yang terlalu tinggi pada $R$ besar?
:::

## 11.11 Teori ikatan valensi Heitler–London

### Mulai dari atom

Pada 1927, beberapa bulan setelah persamaan Schrödinger diterbitkan, Walter Heitler dan Fritz London mendekati H₂ dari arah sebaliknya. Bila dua atom H berjauhan, fungsi gelombang yang benar adalah hasil kali orbital atom: elektron 1 di $A$ dan elektron 2 di $B$, yaitu $a(1)b(2)$. Tetapi elektron tidak dapat dibedakan (subbab 9.3), sehingga $b(1)a(2)$ sama baiknya. Kombinasi yang dihasilkan simetri pertukaran adalah

$$
\Psi_\pm = \frac{a(1)b(2) \pm b(1)a(2)}{\sqrt{2(1 \pm S^2)}} , \qquad \text{(11.26)}
$$

dengan faktor normalisasi yang memuat $S^2$ karena $\langle a(1)b(2)|b(1)a(2)\rangle = S^2$. Asas Pauli menentukan pasangan spinnya: fungsi ruang simetris $\Psi_+$ harus disertai fungsi spin antisimetris (singlet, $S = 0$), dan fungsi ruang antisimetris $\Psi_-$ disertai fungsi spin simetris (triplet, $S = 1$). Fungsi ini adalah bagian kovalen (11.25) tanpa bagian ionik: elektron tidak pernah berdua di satu atom.

### Energi Heitler–London

Nilai harap $\hat H_\text{el}$ untuk $\Psi_\pm$ dapat dihitung dengan cara yang sama seperti H₂⁺. Hasilnya, relatif terhadap dua atom H terpisah,

$$
E_\pm - 2E_\text{H} = \frac{Q \pm X}{1 \pm S^2} , \qquad \text{(11.27)}
$$

dengan **integral Coulomb**

$$
Q = 2J + (aa|bb) + \frac1R
$$

(tarikan setiap awan atom oleh inti tetangga, tolakan antara kedua awan, dan tolakan antarinti) dan **integral pertukaran**

$$
X = 2SK + (ab|ab) + \frac{S^2}{R} ,
$$

dengan $J$ dan $K$ integral H₂⁺ (11.14). $Q$ adalah energi interaksi elektrostatik klasik dua atom H yang tidak berubah bentuk; $X$ tidak mempunyai padanan klasik, dan muncul hanya karena fungsi gelombang memuat kedua susunan $a(1)b(2)$ dan $b(1)a(2)$.

::: {.contoh}
**Contoh 11.41 · Dari mana energi ikat Heitler–London?**

Pada $R = 1{,}643$ bohr ($\zeta = 1$), perhitungan memberi $S = 0{,}685$, $Q = -0{,}0168$ hartree, dan $X = -0{,}1536$ hartree. Hitung energi ikat singlet dan energi keadaan triplet relatif terhadap dua atom H, dalam eV.

**Penyelesaian.** $S^2 = 0{,}4695$. Singlet: $(Q + X)/(1 + S^2) = -0{,}1704/1{,}4695 = -0{,}1160$ hartree $= -3{,}16$ eV. Triplet: $(Q - X)/(1 - S^2) = 0{,}1368/0{,}5305 = +0{,}2580$ hartree $= +7{,}02$ eV.

**Memahami hasil.** Integral Coulomb hanya menyumbang $-0{,}46$ eV; lebih dari 90% energi ikat berasal dari integral pertukaran ($-4{,}18$ eV). Ikatan kovalen adalah gejala kuantum murni, tidak dapat dijelaskan oleh tarikan elektrostatik dua atom yang tidak berubah. Keadaan triplet, dengan spin sejajar, menolak di semua jarak: dua atom H dengan spin sejajar tidak dapat membentuk ikatan. Inilah dasar kuantum gagasan Lewis bahwa ikatan kovalen adalah **pasangan elektron** dengan spin berlawanan.
:::

### Hasil dan perbaikan

Fungsi Heitler–London dengan $\zeta = 1$ memberi $R_e = 1{,}64$ bohr (87 pm) dan $D_e = 3{,}16$ eV, lebih baik daripada OM dengan $\zeta = 1$ (2,70 eV). S. C. Wang (1928) mengoptimalkan $\zeta$ dan memperoleh $\zeta = 1{,}166$, $R_e = 1{,}41$ bohr (75 pm), dan $D_e = 3{,}78$ eV, juga lebih baik daripada OM dengan $\zeta$ optimal (3,49 eV). Dan yang terpenting, fungsi Heitler–London terdisosiasi dengan benar: untuk $R \to \infty$, $S$, $Q$, dan $X$ semuanya lenyap, dan energinya tepat $2E_\text{H}$.

::: {.contoh}
**Contoh 11.42 · Asas Pauli dan ikatan**

Tunjukkan bahwa fungsi ruang $\Psi_+ = a(1)b(2) + b(1)a(2)$ harus berpasangan dengan spin singlet, dan jelaskan mengapa dua atom He tidak dapat membentuk ikatan valensi.

**Penyelesaian.** Pertukaran label elektron $1 \leftrightarrow 2$ mengubah $\Psi_+$ menjadi $b(2)a(1) + a(2)b(1) = \Psi_+$: simetris. Fungsi total harus antisimetris, sehingga fungsi spinnya harus antisimetris: $[\alpha(1)\beta(2) - \beta(1)\alpha(2)]/\sqrt2$, singlet. Atom He sudah mempunyai dua elektron berpasangan di 1s. Untuk membentuk pasangan baru antara $A$ dan $B$, sebuah elektron di $A$ harus berpasangan dengan elektron di $B$, tetapi setiap elektron di $A$ sudah berpasangan, dan elektron ketiga tidak dapat masuk ke 1s yang sama (Pauli). Interaksi He–He karena itu tolak-menolak.

**Memahami hasil.** Dalam bahasa ikatan valensi, **valensi** sebuah atom adalah banyaknya elektron tak berpasangan yang dapat dipasangkan dengan elektron atom lain. H bervalensi satu, He nol. Teori ini langsung menjelaskan valensi klasik dan menjadi dasar teori hibridisasi Pauling untuk molekul poliatom (Bab 12).
:::

::: {.contoh}
**Contoh 11.43 · Tolakan Pauli antara dua atom berkulit tertutup**

Dalam teori Heitler–London, energi triplet adalah $(Q - X)/(1 - S^2)$. Mengapa interaksi dua atom berkulit tertutup, seperti He + He atau Ne + Ne, selalu menolak pada jarak pendek, dan mengapa tolakan itu meluruh eksponensial?

**Penyelesaian.** Elektron-elektron dari dua atom berkulit tertutup tidak dapat membentuk pasangan baru; secara efektif setiap pasangan elektron $A$–$B$ dengan spin sejajar berperilaku seperti keadaan triplet H₂, dengan energi tolak sebanding dengan $-X$ dan $S^2$. Karena $S$ dan $X$ meluruh eksponensial dengan jarak (keduanya ditentukan oleh tumpang tindih), tolakannya juga meluruh eksponensial.

**Memahami hasil.** Inilah asal fisis suku tolak dalam potensial antarmolekul, misalnya potensial Born–Mayer $Ae^{-R/\rho}$, atau suku $R^{-12}$ potensial Lennard-Jones yang merupakan pendekatan praktisnya. Tolakan Pauli menentukan ukuran atom dan molekul ("jari-jari van der Waals") dan mengapa zat padat tidak dapat dimampatkan sembarangan. Di jarak lebih besar, tolakan ini kalah oleh tarikan dispersi yang lemah, sehingga gas mulia tetap dapat mencair.
:::

::: {.kuis}
**Kuis cepat 11.11**

\(a) Apa batas energi Heitler–London untuk $R \to \infty$, dan mengapa ini benar? (b) Mengapa keadaan triplet H₂ menolak? (c) Mana yang lebih besar sumbangannya pada energi ikat HL: $Q$ atau $X$?
:::

## 11.12 Perbandingan OM dan IV; interaksi konfigurasi

### Dua kesalahan yang berlawanan

Persamaan (11.25) memperlihatkan hubungan kedua teori dengan jelas. Fungsi OM adalah kovalen + ionik dengan bobot sama; fungsi Heitler–London adalah kovalen saja. Molekul H₂ yang sebenarnya berada di antara keduanya: terutama kovalen, dengan sedikit karakter ionik. Elektron-elektron memang kadang-kadang berada di atom yang sama, tetapi lebih jarang daripada yang diramalkan OM, karena mereka saling menolak. Fungsi gelombang yang lebih baik adalah

$$
\Psi = [a(1)b(2) + b(1)a(2)] + \lambda\,[a(1)a(2) + b(1)b(2)] , \qquad \text{(11.28)}
$$

dengan $\lambda$ parameter variasi. Untuk $\lambda = 0$ diperoleh Heitler–London, untuk $\lambda = 1$ diperoleh OM. S. Weinbaum (1933) mengoptimalkan $\lambda$ dan $\zeta$ dan memperoleh $\lambda \approx 0{,}26$ dan $D_e = 4{,}03$ eV.

### Interaksi konfigurasi

Fungsi yang sama dapat diperoleh dari arah OM. Selain konfigurasi dasar $(\sigma_g)^2$, ada konfigurasi tereksitasi $(\sigma_u)^2$ yang juga bersimetri $^1\Sigma_g^+$ (dua elektron $u$ memberi $g$). Karena kedua konfigurasi sesimetri, Hamiltonian mencampurnya. Fungsi

$$
\Psi_\text{CI} = c_1\,\sigma_g(1)\sigma_g(2) + c_2\,\sigma_u(1)\sigma_u(2) \qquad \text{(11.29)}
$$

disebut fungsi **interaksi konfigurasi** (CI), dan koefisiennya diperoleh dari persamaan sekuler 2 × 2. Uraikan $\sigma_u(1)\sigma_u(2) \propto [a(1) - b(1)][a(2) - b(2)] = (aa + bb) - (ab + ba)$, yaitu ionik *dikurangi* kovalen. Dengan $c_2$ bertanda berlawanan dengan $c_1$, penambahan $(\sigma_u)^2$ mengurangi bagian ionik dan menambah bagian kovalen. Jadi (11.29) dan (11.28) adalah fungsi yang sama, hanya ditulis dalam basis berbeda. Dengan basis minimal, CI 2 × 2 adalah penyelesaian paling baik yang mungkin, dan teori OM serta IV yang diperbaiki bertemu di titik yang sama.

::: {.inti}
**OM, IV, dan CI untuk H₂ (basis minimal 1s)**

- OM: $(\sigma_g)^2$ = kovalen + ionik (bobot sama). Baik di dekat $R_e$, gagal total pada disosiasi.
- IV (Heitler–London): kovalen saja. Disosiasi benar, sedikit kurang ionik di $R_e$.
- CI: $(\sigma_g)^2$ dicampur $(\sigma_u)^2$ = kovalen + $\lambda$ ionik. Terbaik dari ketiganya, dan benar di semua $R$.
:::

| Fungsi gelombang | $\zeta$ | $R_e$ (bohr) | $R_e$ (pm) | $D_e$ (eV) |
|---|---|---|---|---|
| OM, $\zeta = 1$ | 1 | 1,603 | 84,8 | 2,70 |
| OM, $\zeta$ optimal | 1,193 | 1,385 | 73,3 | 3,49 |
| Batas Hartree–Fock | — | 1,385 | 73,3 | 3,64 |
| Heitler–London | 1 | 1,643 | 86,9 | 3,16 |
| Wang (HL, $\zeta$ optimal) | 1,166 | 1,414 | 74,8 | 3,78 |
| CI / Weinbaum | 1,194 | 1,430 | 75,7 | 4,03 |
| Eksak (Kołos–Wolniewicz) | — | 1,401 | 74,14 | 4,747 |

(Semua baris kecuali batas Hartree–Fock dan nilai eksak dihitung ulang dengan integral orbital Slater untuk bab ini.)

![Gambar 11.9 Kurva energi potensial H₂ dalam basis minimal 1s ($\zeta = 1$): OM (biru), Heitler–London (hijau), dan CI (jingga), relatif terhadap dua atom H. Bintang menandai minimum eksak ($R_e = 1{,}401$ bohr, $D_e = 4{,}747$ eV). Kurva OM naik ke nilai yang salah pada jarak besar karena memuat 50% struktur ionik.](fig/c_h2.png){width=82%}

### Energi korelasi

Selisih antara energi eksak dan energi Hartree–Fock (energi terbaik yang dapat dicapai dengan satu determinan) disebut **energi korelasi**:

$$
E_\text{kor} = E_\text{eksak} - E_\text{HF} . \qquad \text{(11.30)}
$$

Untuk H₂ pada $R_e$, $E_\text{HF} = -1{,}1336$ hartree dan $E_\text{eksak} = -1{,}1745$ hartree, sehingga $E_\text{kor} = -0{,}0408$ hartree $= -1{,}11$ eV. Energi ini kecil dibandingkan energi total (3,5%), tetapi sebanding dengan energi ikat kimia, sehingga tidak boleh diabaikan dalam perhitungan termokimia. Metode-metode di Bab 17 (CI, Møller–Plesset, coupled-cluster, DFT) pada dasarnya adalah cara-cara menangkap energi korelasi.

::: {.contoh}
**Contoh 11.44 · Seberapa ionik ikatan H–H?**

Penyelesaian CI 2 × 2 pada jarak optimum ($R = 1{,}430$ bohr, $\zeta = 1{,}194$, $S = 0{,}667$) memberi koefisien $c_1 = 0{,}9933$ dan $c_2 = -0{,}1154$. Hitung $\lambda$ dalam (11.28).

**Penyelesaian.** Dengan $\sigma_g^2 \propto [\text{kov} + \text{ion}]/2(1 + S)$ dan $\sigma_u^2 \propto [\text{ion} - \text{kov}]/2(1 - S)$, koefisien bagian kovalen dan ionik sebanding dengan $c_1/(1 + S) - c_2/(1 - S)$ dan $c_1/(1 + S) + c_2/(1 - S)$:

$$
\lambda = \frac{0{,}9933/1{,}667 - 0{,}1154/0{,}333}{0{,}9933/1{,}667 + 0{,}1154/0{,}333} = \frac{0{,}596 - 0{,}347}{0{,}596 + 0{,}347} = 0{,}264 .
$$

**Memahami hasil.** Koefisien struktur ionik sekitar seperempat koefisien struktur kovalen; bila tumpang tindih diabaikan, bobotnya $\lambda^2/(1 + \lambda^2) \approx 7\%$. Bahkan ikatan antara dua atom identik mempunyai sedikit karakter "ionik", dalam arti adanya peluang kedua elektron berada di atom yang sama. Hal ini tidak membuat H₂ polar: kedua struktur ionik H⁺H⁻ dan H⁻H⁺ berbobot sama, sehingga momen dipolnya tetap nol.
:::

::: {.contoh}
**Contoh 11.45 · Kurva H₂ dengan Python**

Tuliskan program yang menghitung energi OM, Heitler–London, dan CI H₂ dalam basis 1s dengan eksponen $\zeta$, memakai rumus tertutup integral orbital Slater.

**Penyelesaian.**

```python
import numpy as np
from scipy.special import expi
g = 0.5772156649                                  # tetapan Euler
def integral(R, z):
    w = z * R; e = np.exp
    S = e(-w) * (1 + w + w*w/3); Sp = e(w) * (1 - w + w*w/3)
    Haa = z*z/2 - z - (1 - (1 + w) * e(-2*w)) / R
    Hab = -z*z*S/2 + (z*z - 2*z) * (1 + w) * e(-w)
    aaaa = 5*z/8
    aabb = z * (1/w - e(-2*w) * (1/w + 11/8 + 3*w/4 + w*w/6))
    aaab = z * (e(-w) * (w + 1/8 + 5/(16*w)) - e(-3*w) * (1/8 + 5/(16*w)))
    abab = z/5 * (-e(-2*w) * (-25/8 + 23*w/4 + 3*w*w + w**3/3)
                  + 6/w * (S*S*(g + np.log(w)) + Sp*Sp*expi(-4*w) - 2*S*Sp*expi(-2*w)))
    return S, Haa, Hab, aaaa, aabb, aaab, abab
def energi(R, z=1.0):
    S, Haa, Hab, aaaa, aabb, aaab, abab = integral(R, z)
    hg, hu = (Haa + Hab) / (1 + S), (Haa - Hab) / (1 - S)
    Jgg = (aaaa + aabb + 2*abab + 4*aaab) / (2 * (1 + S)**2)
    Juu = (aaaa + aabb + 2*abab - 4*aaab) / (2 * (1 - S)**2)
    Kgu = (aaaa - aabb) / (2 * (1 - S*S))
    OM = 2*hg + Jgg + 1/R
    HL = (2*Haa + aabb + 2*S*Hab + abab) / (1 + S*S) + 1/R
    CI = np.linalg.eigvalsh([[2*hg + Jgg, Kgu], [Kgu, 2*hu + Juu]])[0] + 1/R
    return OM, HL, CI
print(energi(1.4))          # (-1.0909, -1.1055, -1.1066)
```

**Memahami hasil.** Dengan $\zeta = 1$ pada $R = 1{,}4$ bohr: OM $-1{,}0909$, HL $-1{,}1055$, CI $-1{,}1066$ hartree, sesuai urutan yang diharapkan (CI terendah karena memuat kedua fungsi lain sebagai kasus khusus). Kopling antara kedua konfigurasi, $K_{gu} = [(aa|aa) - (aa|bb)]/2(1 - S^2)$, adalah selisih antara tolakan dua elektron di atom yang sama dan di atom berbeda: tepat besaran yang mengukur seberapa "mahal" struktur ionik. Program ini, dengan pencarian minimum, menghasilkan tabel di atas.
:::

::: {.contoh}
**Contoh 11.46 · Kapan OM cukup, kapan perlu CI?**

Bandingkan kesalahan energi OM ($\zeta = 1$) relatif terhadap CI pada $R = 1{,}4$, 2, 4, dan 6 bohr: OM $-1{,}0909$, $-1{,}0808$, $-0{,}8954$, $-0{,}7951$; CI $-1{,}1066$, $-1{,}1084$, $-1{,}0128$, $-1{,}0005$ hartree.

**Penyelesaian.** Selisih: 0,016; 0,028; 0,117; 0,205 hartree, atau 0,43; 0,75; 3,2; 5,6 eV.

**Memahami hasil.** Di sekitar jarak setimbang, satu konfigurasi sudah menangkap hampir seluruh struktur elektronik, dan bobot $(\sigma_u)^2$ kecil. Ketika ikatan diregangkan, orbital $\sigma_g$ dan $\sigma_u$ makin mendekati degenerasi (selisih energinya sebanding dengan tumpang tindih), dan kedua konfigurasi menjadi sama pentingnya. Aturan praktis kimia komputasi: metode satu determinan baik untuk molekul di sekitar geometri setimbangnya, tetapi pemutusan ikatan, diradikal, dan banyak senyawa logam transisi memerlukan fungsi gelombang **multikonfigurasi** (subbab 17.10).
:::

::: {.terapan}
**Kaitan kimia · Dua bahasa untuk ikatan yang sama**

Teori OM dan teori IV bersaing sengit pada 1930-an sampai 1950-an. Teori IV, lewat Pauling, menguasai kimia organik dan anorganik karena bahasanya dekat dengan struktur Lewis: pasangan elektron, hibridisasi, resonansi. Teori OM menang dalam spektroskopi dan, setelah komputer tersedia, dalam perhitungan, karena orbital molekul mudah diprogram. Kini keduanya dipahami sebagai titik awal berbeda menuju jawaban yang sama: perluasan penuh keduanya (CI lengkap dan IV lengkap dalam basis yang sama) memberi fungsi gelombang yang identik. Kimiawan memakai bahasa OM ketika membicarakan spektrum fotoelektron, warna, aromatisitas, dan reaksi perisiklik (Bab 13), serta bahasa IV ketika membicarakan pembentukan dan pemutusan ikatan, geometri, dan mekanisme reaksi (Bab 12).
:::

::: {.kuis}
**Kuis cepat 11.12**

\(a) Mengapa konfigurasi $(\sigma_g)^1(\sigma_u)^1$ tidak ikut dalam CI keadaan dasar H₂? (b) Nilai $\lambda$ berapa yang berhubungan dengan OM sederhana dan dengan Heitler–London? (c) Mengapa energi korelasi penting meskipun hanya 3,5% energi total?
:::
