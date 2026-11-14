## 12.3 Hibrida sp: BeH₂ dan asetilena; penurunan sudut 180°

### Berilium hidrida

Dalam fase gas, BeH₂ dan BeCl₂ berupa molekul linear (Be–H 133 pm, Be–Cl sekitar 180 pm). Atom berilium dalam keadaan dasar ($2s^2$, $^1S$) tidak mempunyai elektron tak berpasangan; untuk membentuk dua ikatan, satu elektron dipromosikan ke $2p$ ($2s2p$, $^3P$, 2,72 eV). Karena hanya dua orbital yang dipakai, kita membentuk dua hibrida dari $s$ dan satu orbital $p$, misalnya $p_z$.

### Penurunan langkah demi langkah

Tulis kedua hibrida sebagai

$$
h_1 = a\,s + b\,p_z , \qquad h_2 = c\,s + d\,p_z ,
$$

dengan koefisien riil yang belum diketahui. Kita menuntut empat syarat:

1. **Normalisasi:** $a^2 + b^2 = 1$ dan $c^2 + d^2 = 1$.
2. **Kesetaraan:** kedua hibrida mempunyai karakter $s$ yang sama, $a^2 = c^2$.
3. **Kekekalan orbital:** orbital $s$ dibagi habis, $a^2 + c^2 = 1$.
4. **Ortogonalitas:** $\langle h_1|h_2\rangle = ac + bd = 0$.

Dari syarat 2 dan 3, $a^2 = c^2 = \tfrac12$. Pilih $a = c = 1/\sqrt2$ (tanda keseluruhan sebuah orbital bebas dipilih). Dari syarat 1, $b^2 = d^2 = \tfrac12$. Syarat 4 menjadi $\tfrac12 + bd = 0$, sehingga $bd = -\tfrac12$: $b$ dan $d$ berlawanan tanda. Dengan $b = 1/\sqrt2$:

$$
h_1 = \frac{s + p_z}{\sqrt2} , \qquad h_2 = \frac{s - p_z}{\sqrt2} . \qquad \text{(12.18)}
$$

Bagian $p$ dari $h_1$ adalah $+p_z$, yang cuping positifnya menunjuk ke $+z$; bagian $p$ dari $h_2$ adalah $-p_z$, yang cuping positifnya menunjuk ke $-z$. **Kedua hibrida menunjuk ke arah berlawanan: sudutnya 180°.** Hasil yang sama keluar dari (12.17) dengan $\alpha = \tfrac12$: $\cos\theta = -1$.

Dalam bentuk matriks, transformasinya

$$
\begin{pmatrix}h_1\\ h_2\end{pmatrix} = \frac{1}{\sqrt2}\begin{pmatrix}1 & 1\\ 1 & -1\end{pmatrix}\begin{pmatrix}s\\ p_z\end{pmatrix} , \qquad \text{(12.19)}
$$

dan matriks ini ortogonal: $\mathbf U\mathbf U^\text{T} = \mathbf I$. Baris-barisnya ternormalisasi dan saling tegak lurus (hibrida ortonormal), dan kolom-kolomnya juga (setiap orbital atom terbagi habis). Transformasi baliknya adalah transposnya: $s = (h_1 + h_2)/\sqrt2$, $p_z = (h_1 - h_2)/\sqrt2$.

Mengapa tidak memilih hibrida yang tidak setara? Untuk BeH₂, kedua ikatan sejenis, dan argumen tumpang tindih total di subbab 12.2 memberi pembagian rata. Untuk molekul seperti HBeCl, karakter $s$ dapat dibagi tidak rata, tetapi kedua hibrida **tetap** harus berlawanan arah: dengan $\alpha_1 + \alpha_2 = 1$, (12.16) memberikan $\cos\theta = -\sqrt{\alpha_1\alpha_2/(\alpha_2\alpha_1)} = -1$. Setiap pasangan hibrida yang dibentuk dari satu $s$ dan satu $p$ selalu linear.

### Orbital p yang tersisa

Hibridisasi sp hanya memakai $p_z$. Orbital $p_x$ dan $p_y$ tetap murni dan, pada BeH₂, kosong. Orbital kosong ini menjelaskan mengapa BeH₂ dan BeCl₂ adalah asam Lewis yang kuat: dalam fase padat keduanya membentuk rantai dengan jembatan Be–H–Be atau Be–Cl–Be (subbab 12.9), dan dengan eter BeCl₂ membentuk aduk tetrahedral BeCl₂(OEt₂)₂, tempat Be memakai hibrida sp³.

### Asetilena: ikatan rangkap tiga

Pada H–C≡C–H, setiap karbon membentuk ikatan dengan dua atom yang segaris, sehingga ia memakai dua hibrida sp. Satu hibrida bertumpang tindih dengan $1s$ hidrogen (ikatan σ C–H), yang lain dengan hibrida sp karbon tetangga (ikatan σ C–C). Dua elektron karbon yang tersisa berada di $p_x$ dan $p_y$, dan keduanya berpasangan dengan elektron di $p_x$ dan $p_y$ karbon tetangga, membentuk **dua ikatan π** yang saling tegak lurus. Ikatan rangkap tiga adalah satu σ dan dua π.

Data percobaan menegaskan gambaran ini: C≡C 120,3 pm (bandingkan C=C 133,9 pm dan C–C 153,5 pm), C–H 106,1 pm (lebih pendek daripada C–H metana, 108,7 pm), dan molekulnya linear.

Pertanyaan yang wajar: apakah sepasang ikatan π yang tegak lurus membuat asetilena "bersudut", misalnya dengan kerapatan elektron yang lebih besar di bidang $xz$ dan $yz$ daripada di antara keduanya? Jawabannya tidak: kerapatan dua ikatan π yang terisi penuh **simetris silinder** di sekitar sumbu molekul (Contoh 12.10). Akibatnya, rangkap tiga tidak mempunyai arah istimewa di sekeliling sumbunya, dan substituen di ujung-ujung asetilena tidak mempunyai isomer rotasi.

### Molekul linear lainnya

Gambaran sp + dua π berlaku untuk HCN (C≡N 115,3 pm), nitril R–C≡N, dan ion sianida. Pada CO₂, karbon pusat memakai dua hibrida sp untuk ikatan σ dengan kedua O, sementara $p_x$-nya membentuk π dengan satu O dan $p_y$-nya dengan O yang lain. Kedua ikatan π CO₂ terletak di bidang yang saling tegak lurus. Susunan yang sama pada **alena**, H₂C=C=CH₂, membawa akibat stereokimia yang menarik: atom karbon tengah memakai sp, dan kedua ikatan π-nya tegak lurus, sehingga kedua gugus CH₂ ujung terletak pada bidang yang saling tegak lurus. Alena dengan dua substituen berbeda di setiap ujung bersifat **kiral** walaupun tidak mempunyai atom karbon kiral (Contoh 12.11).

::: {.contoh}
**Contoh 12.9 · Memeriksa hibrida sp**

(a) Tunjukkan bahwa $h_{1,2} = (s \pm p_z)/\sqrt2$ ortonormal. (b) Hitung bagian sudut $h_1$ ke arah $+z$ dan $-z$ (dalam satuan $1/\sqrt{4\pi}$), dan perbandingannya. (c) Bila sebuah elektron menempati $h_1$, berapa peluang bahwa pengukuran "jenis orbital" menemukan $s$?

**Penyelesaian.** (a) $\langle h_1|h_1\rangle = \tfrac12(1 + 1) = 1$; $\langle h_1|h_2\rangle = \tfrac12(\langle s|s\rangle - \langle p_z|p_z\rangle) = \tfrac12(1 - 1) = 0$; suku silang $\langle s|p_z\rangle = 0$.

\(b) Bagian sudut $s$ adalah 1 dan bagian sudut $p_z$ adalah $\sqrt3\cos\theta$. Ke arah $+z$: $(1 + \sqrt3)/\sqrt2 = 1{,}932$; ke arah $-z$: $|1 - \sqrt3|/\sqrt2 = 0{,}518$. Perbandingan 3,73.

\(c) $|\langle s|h_1\rangle|^2 = \tfrac12$.

**Memahami hasil.** Karakter $s$ 50% berarti, secara harfiah, peluang 50% menemukan elektron "dalam orbital $s$" bila kita menguraikan hibrida ke basis orbital atom. Cuping depan hibrida sp hampir empat kali cuping belakangnya, sehingga hampir seluruh kerapatannya mengarah ke satu sisi.
:::

::: {.contoh}
**Contoh 12.10 · Rangkap tiga simetris silinder**

Ikatan π$_x$ dan π$_y$ asetilena masing-masing berisi dua elektron. Dengan $p_x = x\,f(r)$ dan $p_y = y\,f(r)$ pada setiap karbon, tunjukkan bahwa kerapatan total kedua ikatan π tidak bergantung pada sudut azimut $\phi$ di sekitar sumbu $z$.

**Penyelesaian.** Dalam pendekatan paling sederhana, orbital π$_x$ adalah $N(p_{xA} + p_{xB}) = N\,x\,[f(r_A) + f(r_B)] \equiv N\,x\,g(\rho, z)$, dengan $\rho = \sqrt{x^2 + y^2}$ jarak dari sumbu; begitu pula π$_y = N\,y\,g(\rho, z)$, dengan $g$ yang sama. Kerapatan total dua pasang elektron:

$$
\rho_\pi = 2|\pi_x|^2 + 2|\pi_y|^2 = 2N^2(x^2 + y^2)\,g^2 = 2N^2\rho^2g(\rho, z)^2 .
$$

Karena $x = \rho\cos\phi$ dan $y = \rho\sin\phi$, $x^2 + y^2 = \rho^2$ tidak bergantung pada $\phi$.

**Memahami hasil.** Dua π yang terisi penuh membentuk "selubung" berbentuk silinder di sekitar sumbu C≡C, seperti cincin donat yang memanjang. Hasil yang sama berlaku untuk pasangan orbital $p_x$, $p_y$ pada atom bebas: kulit $p^6$ (dan juga $p^2$ dengan $m_\ell = \pm1$) bersimetri silinder atau bola. Asetilena dan N₂ tidak mempunyai "sudut" di sekeliling sumbunya.
:::

::: {.contoh}
**Contoh 12.11 · Alena kiral dan butatriena**

(a) Tentukan hibridisasi setiap karbon pada penta-2,3-diena, CH₃–CH=C=CH–CH₃, dan jelaskan mengapa molekul ini mempunyai dua enansiomer. (b) Pada butatriena, H₂C=C=C=CH₂, apakah kedua gugus CH₂ ujung sebidang atau tegak lurus? Apakah 1,4-diklorobutatriena mempunyai isomer cis–trans atau enansiomer?

**Penyelesaian.** (a) C1 dan C5 (metil): sp³. C2 dan C4: sp². C3 (tengah): sp. Ikatan π C2=C3 memakai, misalnya, $p_x$ dari C3, sehingga C2 dan substituennya (H dan CH₃) terletak di bidang $yz$. Ikatan π C3=C4 memakai $p_y$ dari C3, sehingga C4 dan substituennya terletak di bidang $xz$. Kedua bidang substituen tegak lurus. Karena setiap ujung membawa dua substituen yang berbeda (H dan CH₃), bayangan cermin molekul tidak dapat ditumpangkan pada molekul semula: ada sepasang enansiomer dengan sumbu kiral.

\(b) Pada butatriena, C1 sp², C2 dan C3 sp, C4 sp². Ikatan π C1=C2 memakai, misalnya, $p_x$ di C2; π C2=C3 memakai $p_y$ di C2 dan C3; π C3=C4 memakai $p_x$ di C3. Ikatan π pertama dan ketiga sejajar (keduanya dari $p_x$), sehingga keempat substituen ujung **sebidang**. 1,4-Diklorobutatriena mempunyai isomer cis dan trans, bukan enansiomer.

**Memahami hasil.** Aturannya: kumulena dengan banyaknya ikatan rangkap genap (alena: 2) mempunyai ujung-ujung yang tegak lurus dan dapat kiral; kumulena dengan banyaknya ikatan rangkap ganjil (butatriena: 3) mempunyai ujung-ujung yang sebidang dan dapat menunjukkan isomer geometri. Seluruh stereokimia ini mengikuti dari satu fakta: dua orbital $p$ pada karbon sp saling tegak lurus.
:::

::: {.kuis}
**Kuis cepat 12.3**

Pada HC≡C–C≡CH (butadiuna), berapa banyak ikatan σ dan π? Mengapa molekul ini lurus?
:::

## 12.4 Hibrida sp²: BF₃ dan etilena; ikatan σ dan π

### Boron trifluorida

BF₃ berbentuk segitiga datar dengan sudut F–B–F 120° dan B–F 130,7 pm. Boron ($2s^22p$) dipromosikan ke $2s2p^2$ (3,57 eV) dan membentuk tiga hibrida dari $s$, $p_x$, dan $p_y$. Orbital $p_z$, tegak lurus bidang molekul, tetap murni dan kosong.

### Penurunan tiga hibrida setara

Kita mencari tiga hibrida setara di bidang $xy$. Langkahnya:

1. **Karakter $s$.** Kekekalan orbital dan kesetaraan memberi $3\alpha = 1$, jadi $\alpha = \tfrac13$ dan koefisien $s$ setiap hibrida $1/\sqrt3$.
2. **Hibrida pertama.** Pilih arah $h_1$ sepanjang $+x$: $h_1 = \tfrac{1}{\sqrt3}s + b\,p_x$, dengan $\tfrac13 + b^2 = 1$, jadi $b = \sqrt{2/3}$.
3. **Hibrida kedua.** Tulis $h_2 = \tfrac{1}{\sqrt3}s + c\,p_x + d\,p_y$. Ortogonal terhadap $h_1$: $\tfrac13 + \sqrt{\tfrac23}\,c = 0$, sehingga $c = -\tfrac{1}{\sqrt6}$. Normalisasi: $\tfrac13 + \tfrac16 + d^2 = 1$, sehingga $d = \pm\tfrac{1}{\sqrt2}$.
4. **Hibrida ketiga.** Pilih tanda $+$ untuk $h_2$; $h_3$ mendapat tanda $-$. Periksa: $\langle h_2|h_3\rangle = \tfrac13 + \tfrac16 - \tfrac12 = 0$.

Hasilnya:

$$
\begin{aligned}
h_1 &= \tfrac{1}{\sqrt3}\,s + \sqrt{\tfrac23}\,p_x ,\\
h_2 &= \tfrac{1}{\sqrt3}\,s - \tfrac{1}{\sqrt6}\,p_x + \tfrac{1}{\sqrt2}\,p_y ,\\
h_3 &= \tfrac{1}{\sqrt3}\,s - \tfrac{1}{\sqrt6}\,p_x - \tfrac{1}{\sqrt2}\,p_y .
\end{aligned} \qquad \text{(12.20)}
$$

Arah bagian $p$ dari $h_2$ sebanding dengan $(-\tfrac{1}{\sqrt6}, \tfrac{1}{\sqrt2}) \propto (-\tfrac12, \tfrac{\sqrt3}{2})$, yaitu 120° dari sumbu $+x$; $h_3$ menunjuk ke 240°. **Tiga hibrida setara di satu bidang membentuk sudut 120°**, sesuai dengan (12.17) untuk $\alpha = \tfrac13$: $\cos\theta = -\tfrac12$. Matriks transformasi $3 \times 3$ yang baris-barisnya adalah koefisien (12.20) bersifat ortogonal (Contoh 12.12).

Orbital $p_z$ yang kosong menjadikan BF₃ asam Lewis. Ketika NH₃ menyumbangkan pasangan bebasnya, boron berubah menjadi tetrahedral (sp³), dan ikatan B–F memanjang dari 130,7 pm menjadi sekitar 138 pm. Sebagian dari "kependekan" B–F pada BF₃ bebas berasal dari sumbangan elektron $p$ fluor ke $p_z$ boron yang kosong, semacam ikatan π parsial yang hilang ketika $p_z$ diisi oleh NH₃.

### Etilena: kerangka σ dan ikatan π

Etilena, H₂C=CH₂, adalah molekul datar dengan semua sudut di sekitar setiap karbon mendekati 120°. Setiap karbon memakai tiga hibrida sp² di bidang molekul: dua untuk ikatan σ dengan H dan satu untuk ikatan σ dengan karbon tetangga. Elektron keempat setiap karbon berada di $p_z$, dan kedua orbital $p_z$ yang sejajar bertumpang tindih secara menyamping membentuk **ikatan π**. Ikatan rangkap dua adalah satu σ dan satu π.

Pemisahan σ dan π bukan sekadar cara memandang; ia dijamin oleh simetri. Bidang molekul adalah bidang cermin. Orbital-orbital σ (hibrida sp² dan $1s$ hidrogen) simetris terhadap pencerminan itu, sedangkan $p_z$ antisimetris (berganti tanda di bawah bidang). Unsur matriks Hamiltonian antara fungsi simetris dan antisimetris terhadap operasi simetri molekul selalu nol (subbab 10.8), sehingga σ dan π tidak bercampur.

### Mengapa ikatan π lebih lemah dan lebih reaktif

Tumpang tindih menyamping dua orbital $p$ jauh lebih kecil daripada tumpang tindih ujung ke ujung dua hibrida. Dengan orbital Slater karbon pada 133,9 pm, tumpang tindih π antara kedua $p_z$ adalah 0,270, sedangkan tumpang tindih σ antara dua hibrida sp² adalah 0,771. Elektron π juga lebih jauh dari sumbu antarinti dan kurang terlindung, sehingga energinya lebih tinggi. Inilah sebabnya:

* elektron π adalah elektron yang paling mudah dilepas (energi ionisasi etilena 10,5 eV, jauh di bawah etana 11,5 eV);
* alkena bereaksi dengan elektrofil (H⁺, Br₂) melalui awan π-nya;
* serapan UV pertama alkena berasal dari eksitasi π → π*.

Ikatan π juga menentukan geometri. Tumpang tindih kedua $p_z$ maksimum bila sumbu-sumbunya sejajar, yaitu bila kedua gugus CH₂ sebidang. Bila satu ujung diputar dengan sudut $\theta$ terhadap sumbu C=C, sumbu $p_z$ ujung itu ikut berputar, dan dengan (12.8) tumpang tindihnya menjadi

$$
S_\pi(\theta) = S_\pi(0)\cos\theta . \qquad \text{(12.21)}
$$

Pada $\theta = 90°$ tumpang tindih π hilang sama sekali: ikatan π putus. Itulah sebabnya rotasi di sekitar ikatan rangkap dua terhalang, dan isomer cis dan trans alkena dapat dipisahkan. Penghalang isomerisasi cis–trans etilena terdeuterasi sekitar 272 kJ/mol, ukuran yang baik untuk kekuatan ikatan π.

### Kerangka σ etilena yang sebenarnya

Sudut H–C–H etilena yang terukur adalah 117,4°, bukan tepat 120°. Dengan (12.17), kedua hibrida C–H mempunyai karakter $s$ $\alpha_\text{H} = 0{,}460/1{,}460 = 0{,}315$, dan hibrida σ C–C mendapat sisanya, $\alpha_\text{CC} = 1 - 2(0{,}315) = 0{,}370$, yaitu sp$^{1{,}7}$. Ikatan σ C–C mendapat karakter $s$ lebih banyak daripada ikatan C–H. Mengapa? Gambar 12.2 memberi petunjuk: makin pendek ikatan C–C, makin besar karakter $s$ yang memaksimumkan tumpang tindihnya (0,51 pada 154 pm, 0,56 pada 134 pm, 0,61 pada 120 pm). Ikatan σ C=C yang pendek "lebih menghargai" orbital $s$ daripada ikatan C–H.

::: {.contoh}
**Contoh 12.12 · Matriks hibrida sp² dengan Python**

Susun matriks transformasi $\mathbf U$ dari $\{s, p_x, p_y\}$ ke $\{h_1, h_2, h_3\}$ menurut (12.20), periksa ortogonalitasnya, dan hitung sudut antara bagian-bagian $p$.

**Penyelesaian.**

```python
import numpy as np
r2, r3, r6 = np.sqrt(2), np.sqrt(3), np.sqrt(6)
U = np.array([[1/r3,  2/r6,  0   ],     # baris = hibrida; kolom = s, px, py
              [1/r3, -1/r6,  1/r2],
              [1/r3, -1/r6, -1/r2]])
print(np.allclose(U @ U.T, np.eye(3)))   # True: hibrida ortonormal
print(np.allclose(U.T @ U, np.eye(3)))   # True: tiap orbital atom terbagi habis
n = U[:, 1:] / np.linalg.norm(U[:, 1:], axis=1)[:, None]   # arah bagian p
print(np.degrees(np.arccos(n @ n.T)).round(2))
```

Keluarannya `True`, `True`, dan matriks sudut dengan 120° di luar diagonal ($\sqrt{2/3} = 2/\sqrt6$).

**Memahami hasil.** $\mathbf U\mathbf U^\text{T} = \mathbf I$ adalah ortonormalitas hibrida; $\mathbf U^\text{T}\mathbf U = \mathbf I$ adalah kekekalan orbital (kolom $s$ memberi $\sum\alpha_i = 1$). Untuk matriks persegi, satu syarat menjamin yang lain. Cara ini berguna untuk memeriksa set hibrida yang lebih rumit, misalnya hibrida $d^2sp^3$ di subbab 12.14.
:::

::: {.contoh}
**Contoh 12.13 · Karakter s pada etilena dan formaldehida**

(a) Dari sudut H–C–H etilena, 117,4°, hitung karakter $s$ hibrida C–H dan hibrida σ C=C, lalu ramalkan sudut H–C–C. (b) Ulangi untuk formaldehida, H₂C=O, dengan sudut H–C–H 116,5°.

**Penyelesaian.** (a) $\cos117{,}4° = -0{,}4602$, $\alpha_\text{H} = 0{,}4602/1{,}4602 = 0{,}315$. $\alpha_\text{CC} = 1 - 0{,}630 = 0{,}370$, $\lambda^2 = 0{,}630/0{,}370 = 1{,}71$. Dengan (12.16): $\cos\theta_\text{HCC} = -\sqrt{(0{,}315)(0{,}370)/[(0{,}685)(0{,}630)]} = -0{,}520$, $\theta = 121{,}3°$.

\(b) $\cos116{,}5° = -0{,}4462$, $\alpha_\text{H} = 0{,}309$, $\alpha_\text{CO} = 0{,}383$. Sudut H–C–O $= 121{,}75°$.

**Memahami hasil.** Pada kedua molekul, $2 \times 121{,}3° + 117{,}4° = 360°$ (dan $2 \times 121{,}75° + 116{,}5° = 360°$): hasil ini bukan kebetulan. Untuk tiga hibrida sebidang yang memakai seluruh $s$, $p_x$, dan $p_y$, ortogonalitas dan kekekalan orbital memaksa sudut-sudutnya berjumlah 360°. Yang kita peroleh adalah pembagian karakter $s$: ikatan σ ganda menerima 37–38% $s$, ikatan C–H 31%.
:::

::: {.contoh}
**Contoh 12.14 · Memuntir etilena**

Anggap energi ikatan π sebanding dengan tumpang tindih π, dan bahwa memuntir etilena sejauh 90° memerlukan 272 kJ/mol. (a) Tulis energi sebagai fungsi sudut puntir. (b) Berapa energi yang diperlukan untuk memuntir 30° dan 45°? (c) Apa artinya bagi isomerisasi cis–trans pada suhu kamar?

**Penyelesaian.** (a) Dengan (12.21), $E(\theta) = E_\pi(1 - \cos\theta)$ dengan $E_\pi = 272$ kJ/mol. (b) $\theta = 30°$: $272(1 - 0{,}866) = 36{,}4$ kJ/mol. $\theta = 45°$: $272(1 - 0{,}707) = 79{,}7$ kJ/mol. (c) Pada 298 K, $RT = 2{,}48$ kJ/mol, sehingga faktor Boltzmann untuk 272 kJ/mol sekitar $e^{-110} \approx 10^{-48}$: isomerisasi termal praktis tidak terjadi.

**Memahami hasil.** Puntiran kecil murah (puntiran 10° hanya memerlukan sekitar 4 kJ/mol menurut model ini), sehingga alkena yang padat substituen dapat sedikit terpuntir. Isomerisasi penuh memerlukan pemutusan π, yang dapat dilakukan dengan cahaya: eksitasi π → π* menaruh satu elektron di orbital antiikatan, sehingga bentuk terpuntir 90° menjadi minimum pada keadaan tereksitasi. Isomerisasi cis–trans retinal dalam rodopsin, langkah pertama penglihatan, bekerja dengan cara ini.
:::

::: {.contoh}
**Contoh 12.15 · σ dan π pada tumpang tindih**

Dengan orbital Slater karbon pada jarak 133,9 pm, $S_{ss} = 0{,}437$, $S_{sp} = 0{,}433$, $S_{p\sigma p\sigma} = 0{,}325$, dan $S_{p\pi p\pi} = 0{,}270$. Hitung tumpang tindih σ antara dua hibrida sp² yang saling berhadapan, dan bandingkan dengan tumpang tindih π.

**Penyelesaian.** Untuk dua hibrida $\sqrt\alpha\,s + \sqrt{1 - \alpha}\,p_\sigma$ yang saling berhadapan,

$$
S_\sigma = \alpha S_{ss} + 2\sqrt{\alpha(1 - \alpha)}\,S_{sp} + (1 - \alpha)S_{p\sigma p\sigma} .
$$

Dengan $\alpha = \tfrac13$: $\tfrac13(0{,}437) + 2(0{,}4714)(0{,}433) + \tfrac23(0{,}325) = 0{,}146 + 0{,}408 + 0{,}217 = 0{,}771$. Tumpang tindih π 0,270, sekitar sepertiga σ.

**Memahami hasil.** Suku silang $s$–$p$ menyumbang lebih dari setengah tumpang tindih σ: tanpa hibridisasi ($\alpha = 0$), σ hanya 0,325, tidak jauh di atas π. Tumpang tindih π yang kecil konsisten dengan kekuatan ikatan π (sekitar 270 kJ/mol) yang lebih kecil daripada ikatan σ C–C (sekitar 350–380 kJ/mol), meskipun kekuatan ikatan tidak sebanding sederhana dengan tumpang tindih.
:::

::: {.kuis}
**Kuis cepat 12.4**

Kation metil, CH₃⁺, datar. Orbital apa yang kosong, dan bagaimana sebuah nukleofil sebaiknya mendekat?
:::

## 12.5 Hibrida sp³: metana; penurunan 109,47° dari ortogonalitas

### Penurunan dari ortogonalitas

Karbon dalam metana memakai keempat orbital valensinya. Kita mencari empat hibrida setara $h_i = \sqrt\alpha\,s + \sqrt{1 - \alpha}\,p_{\mathbf n_i}$, $i = 1, \ldots, 4$, dan menurunkan arah-arahnya tanpa menggambar apa pun.

**Langkah 1: karakter $s$.** Kekekalan orbital (12.14): $4\alpha = 1$, jadi $\alpha = \tfrac14$. Setiap hibrida adalah $h_i = \tfrac12 s + \tfrac{\sqrt3}{2}p_{\mathbf n_i}$.

**Langkah 2: sudut.** Ortogonalitas setiap pasangan (12.15): $\tfrac14 + \tfrac34\,\mathbf n_i\cdot\mathbf n_j = 0$, jadi

$$
\mathbf n_i\cdot\mathbf n_j = -\frac13 , \qquad \theta = \arccos\left(-\frac13\right) = 109{,}4712° \qquad (i \ne j) . \qquad \text{(12.22)}
$$

**Langkah 3: jumlah arah.** Hitung panjang kuadrat jumlah keempat vektor satuan:

$$
\Big|\sum_i\mathbf n_i\Big|^2 = \sum_i\mathbf n_i\cdot\mathbf n_i + \sum_{i \ne j}\mathbf n_i\cdot\mathbf n_j = 4 + 12\left(-\frac13\right) = 0 .
$$

Jadi $\sum_i\mathbf n_i = \mathbf 0$: keempat arah saling "meniadakan", seperti yang dituntut agar ikatan-ikatan setara mengelilingi atom secara seimbang.

**Langkah 4: bentuknya.** Empat titik pada bola satuan yang jarak antarpasangannya sama ($|\mathbf n_i - \mathbf n_j|^2 = 2 - 2(-\tfrac13) = \tfrac83$ untuk setiap pasangan) adalah titik-titik sudut **tetrahedron beraturan**. Bentuk tetrahedral metana dengan demikian adalah satu-satunya susunan empat hibrida $s$–$p$ setara yang saling ortogonal.

### Bentuk eksplisit: sudut-sudut kubus

Tetrahedron beraturan dapat diletakkan dalam kubus dengan titik-titik sudutnya pada empat sudut kubus yang berselang-seling (Gambar 12.4(a)): $(1, 1, 1)$, $(1, -1, -1)$, $(-1, 1, -1)$, $(-1, -1, 1)$, masing-masing dibagi $\sqrt3$. Dengan (12.7), bagian $p$ dari hibrida pertama adalah $\tfrac{\sqrt3}{2}\cdot\tfrac{1}{\sqrt3}(p_x + p_y + p_z) = \tfrac12(p_x + p_y + p_z)$. Hasil lengkapnya:

$$
\begin{aligned}
h_1 &= \tfrac12\,(s + p_x + p_y + p_z) , & h_2 &= \tfrac12\,(s + p_x - p_y - p_z) ,\\
h_3 &= \tfrac12\,(s - p_x + p_y - p_z) , & h_4 &= \tfrac12\,(s - p_x - p_y + p_z) .
\end{aligned} \qquad \text{(12.23)}
$$

Setiap pasangan memberikan $\tfrac14(1 + 1 - 1 - 1) = 0$ atau sejenisnya: ortogonal. Transformasi baliknya sama sederhana:

$$
s = \tfrac12(h_1 + h_2 + h_3 + h_4) , \qquad p_x = \tfrac12(h_1 + h_2 - h_3 - h_4) , \quad \ldots \qquad \text{(12.24)}
$$

Orbital $s$ adalah jumlah keempat hibrida dengan bobot sama; orbital $p_x$ adalah selisih antara dua hibrida "di sisi $+x$" dan dua "di sisi $-x$". Kita akan memakai pasangan transformasi ini lagi di subbab 12.13: ia juga menghubungkan orbital molekul kanonik metana dengan orbital ikatan terlokalisasinya.

![Gambar 12.4 (a) Arah keempat hibrida sp³ metana ke empat sudut kubus yang berselang-seling. (b) Ikatan bengkok pada siklopropana: sudut antarinti 60°, tetapi hibrida-hibrida karbon (panah) tidak dapat membentuk sudut kurang dari 90° dan membentuk sudut sekitar 105°, sehingga masing-masing menyimpang sekitar 22° ke luar dari garis antarinti.](fig/c_metana.png){width=84%}

### Metana, etana, intan

Metana adalah contoh sempurna: empat ikatan C–H setara (108,7 pm), sudut 109,47°. Pada etana, setiap karbon memakai tiga hibrida untuk C–H dan satu untuk C–C (153,5 pm). Hibridisasi tidak menghalangi rotasi di sekitar ikatan tunggal, karena ikatan σ simetris silinder; penghalang rotasi etana yang kecil (12 kJ/mol, dengan konformasi goyang lebih stabil daripada konformasi gerhana) berasal dari interaksi antara ikatan-ikatan C–H pada kedua ujung, bukan dari ikatan σ C–C itu sendiri.

Intan adalah "molekul" sp³ raksasa: setiap atom karbon terikat pada empat karbon lain secara tetrahedral (C–C 154,4 pm), membentuk jaringan tiga dimensi dari ikatan σ yang kuat dan terarah. Kekerasan intan, konduktivitas termalnya yang luar biasa, dan celah pita lebarnya (5,5 eV) adalah sifat jaringan ikatan sp³. Silikon dan germanium mempunyai struktur yang sama. Ion-ion NH₄⁺, BH₄⁻, dan tetrahedron SiO₄ dalam silikat adalah contoh lain hibridisasi sp³ pada atom pusat yang isoelektronik dengan karbon.

### Ikatan bengkok: siklopropana

Siklopropana menguji teori dengan keras. Sudut C–C–C antarinti dalam cincin segitiga adalah 60°. Menurut (12.16), hibrida $s$–$p$ tidak pernah membentuk sudut kurang dari 90°. Jadi hibrida-hibrida karbon **tidak dapat** menunjuk langsung ke atom-atom karbon tetangga; ikatan C–C siklopropana harus "bengkok", dengan tumpang tindih maksimum terletak di luar garis antarinti (Gambar 12.4(b)). Gambaran ini diusulkan oleh C. A. Coulson dan W. E. Moffitt (1949).

Kita dapat menghitung susunannya dari data. Sudut H–C–H siklopropana sekitar 115°, sehingga hibrida C–H mempunyai $\alpha_\text{H} = 0{,}297$. Sisanya, $1 - 2(0{,}297) = 0{,}406$, dibagi dua hibrida cincin: $\alpha_\text{r} = 0{,}203$ (sp$^{3{,}9}$). Sudut antara kedua hibrida cincin, dengan (12.17), adalah 104,7°. Karena garis antarinti membentuk 60°, setiap hibrida menyimpang $(104{,}7° - 60°)/2 = 22{,}4°$ ke luar cincin.

Akibat kimianya banyak dan dapat diukur:

* **Tegangan cincin.** Tumpang tindih ikatan bengkok lebih kecil daripada ikatan lurus (Contoh 12.18), dan siklopropana menyimpan energi tegangan sekitar 115 kJ/mol.
* **Ikatan C–H yang "lebih sp²".** Karakter $s$ C–H (30%) mendekati alkena, sehingga ikatan C–H siklopropana lebih pendek, lebih asam, dan mempunyai kopling $^1J(^{13}\text{C–H}) = 161$ Hz, hampir sama dengan etilena (subbab 12.7).
* **Kereaktifan mirip alkena.** Kerapatan elektron ikatan bengkok berada di luar cincin dan mudah dijangkau elektrofil; siklopropana bereaksi dengan HBr dan Br₂ membuka cincin, dan gugus siklopropil dapat berkonjugasi dengan ikatan rangkap atau pusat kation di sebelahnya.

::: {.contoh}
**Contoh 12.16 · Hibrida sp³ dengan Python**

Bangun matriks $\mathbf U$ untuk (12.23), periksa ortogonalitasnya, hitung semua sudut antarhibrida, dan periksa $\sum_i\tfrac34\mathbf n_i\mathbf n_i^\text{T}$.

**Penyelesaian.**

```python
import numpy as np
U = 0.5 * np.array([[1,  1,  1,  1],    # kolom: s, px, py, pz
                    [1,  1, -1, -1],
                    [1, -1,  1, -1],
                    [1, -1, -1,  1]])
print(np.allclose(U @ U.T, np.eye(4)))        # True
n = U[:, 1:] / np.linalg.norm(U[:, 1:], axis=1)[:, None]
print(np.degrees(np.arccos(np.clip(n @ n.T, -1, 1))).round(4))
print(0.75 * n.T @ n)                         # matriks identitas 3x3
print(np.linalg.det(U))                       # -1
```

Semua sudut di luar diagonal 109,4712°; $\tfrac34\sum_i\mathbf n_i\mathbf n_i^\text{T} = \mathbf I_3$; determinan $\mathbf U$ adalah $-1$.

**Memahami hasil.** $\tfrac34\sum_i\mathbf n_i\mathbf n_i^\text{T} = \mathbf I$ menyatakan bahwa ketiga orbital $p$ terbagi habis ke keempat hibrida dan tidak ada arah ruang yang diistimewakan: jumlah kerapatan keempat hibrida yang terisi sama dengan kerapatan kulit $s^2p^6$ yang simetris bola. Determinan $\pm1$ menunjukkan bahwa transformasi ini adalah rotasi (atau rotasi dengan pencerminan) dalam ruang empat dimensi orbital: ia mengubah cara kita membagi kerapatan, bukan kerapatannya sendiri.
:::

::: {.contoh}
**Contoh 12.17 · Dari hibrida kembali ke orbital atom**

(a) Dengan (12.24), nyatakan $p_z$ dalam hibrida. (b) Bila keempat hibrida masing-masing berisi satu elektron (keadaan valensi karbon), berapa banyak elektron "di dalam" orbital $s$ dan di dalam setiap orbital $p$? (c) Bandingkan dengan konfigurasi $2s2p^3$.

**Penyelesaian.** (a) Dari koefisien $p_z$ dalam (12.23) (kolom keempat $\mathbf U$): $p_z = \tfrac12(h_1 - h_2 - h_3 + h_4)$. (b) Populasi orbital $s$ adalah $\sum_i|\langle s|h_i\rangle|^2\cdot1 = 4 \times \tfrac14 = 1$; populasi setiap orbital $p$ juga $4 \times \tfrac14 = 1$. (c) Tepat $2s^12p^3$.

**Memahami hasil.** Empat elektron dalam empat hibrida sp³ memberi populasi orbital atom yang sama dengan konfigurasi promosi $2s2p^3$. Hibridisasi tidak mengubah konfigurasi; ia hanya memilih kombinasi orbital yang paling cocok untuk memasangkan elektron-elektron itu dengan atom-atom hidrogen di arah tetrahedral.
:::

::: {.contoh}
**Contoh 12.18 · Seberapa lemah ikatan bengkok?**

Untuk siklopropana (C–C 151,0 pm, H–C–H 115,0°), orbital Slater karbon memberi $S_{ss} = 0{,}354$, $S_{sp} = 0{,}376$, $S_{p\sigma p\sigma} = 0{,}331$, $S_{p\pi p\pi} = 0{,}202$. (a) Hitung karakter $s$ hibrida cincin dan penyimpangannya dari garis antarinti. (b) Hitung tumpang tindih kedua hibrida cincin yang bengkok, dan bandingkan dengan tumpang tindih dua hibrida sp³ lurus pada jarak yang sama.

**Penyelesaian.** (a) $\cos115{,}0° = -0{,}4226$, $\alpha_\text{H} = 0{,}4226/1{,}4226 = 0{,}297$, $\alpha_\text{r} = 0{,}5 - 0{,}297 = 0{,}203$. Sudut antarhibrida cincin $\arccos(-0{,}203/0{,}797) = 104{,}7°$; penyimpangan $\delta = (104{,}7° - 60°)/2 = 22{,}4°$.

\(b) Bagian $p$ setiap hibrida adalah $\cos\delta\,p_\sigma + \sin\delta\,p_\pi$, dengan kedua hibrida condong ke sisi luar yang sama. Tumpang tindihnya

$$
S = \alpha S_{ss} + 2\sqrt{\alpha(1 - \alpha)}\cos\delta\,S_{sp} + (1 - \alpha)\left(\cos^2\delta\,S_{p\sigma p\sigma} + \sin^2\delta\,S_{p\pi p\pi}\right) .
$$

Dengan $\alpha = 0{,}203$ dan $\delta = 22{,}4°$: $S = 0{,}600$. Dua hibrida sp³ lurus pada 151 pm: $S = 0{,}662$. Ikatan bengkok kehilangan sekitar 9% tumpang tindih.

**Memahami hasil.** Penurunan tumpang tindih ini, ditambah tolakan antar-ikatan C–H yang gerhana, adalah sumber tegangan cincin siklopropana (sekitar 115 kJ/mol untuk tiga ikatan). Tumpang tindih yang "hilang" tidak sepenuhnya hilang: sebagian kerapatan ikatan berpindah ke luar cincin, tempat ia dapat diserang elektrofil. Teori lain (model Walsh) melukiskan siklopropana dengan orbital sp² dan orbital $p$ yang menunjuk ke pusat cincin; kedua gambaran itu adalah dua cara membagi kerapatan yang sama.
:::

::: {.kuis}
**Kuis cepat 12.5**

Mengapa (12.22) tidak bergantung pada pilihan sumbu koordinat? Mengapa sikloheksana bentuk kursi tidak memerlukan ikatan bengkok?
:::
