## 13.4 Metode Hückel

### Memisahkan elektron π

Dalam molekul datar seperti etilena, butadiena, atau benzena, bidang molekul adalah bidang cermin. Setiap orbital molekul bersifat simetris (σ) atau antisimetris (π) terhadap pencerminan itu, dan kedua jenis orbital tidak bercampur (subbab 12.4). Orbital π dibentuk hanya dari orbital $2p_z$ (tegak lurus bidang) atom-atom karbon dan heteroatom. Karena elektron π adalah elektron yang paling tinggi energinya, paling mudah tereksitasi, dan paling reaktif, banyak sifat kimia molekul terkonjugasi ditentukan oleh elektron π saja. E. Hückel (1931) memanfaatkan pemisahan ini: elektron σ dan inti dianggap sebagai "inti" tetap yang menghasilkan medan efektif, dan hanya elektron π yang diperlakukan secara eksplisit.

### Empat metode Hückel

Untuk sistem π dengan $N$ atom karbon, setiap atom menyumbang satu orbital $2p_z$, $\phi_r$, dan OM π ditulis $\psi_k = \sum_rc_{rk}\phi_r$. Persamaan sekuler (13.2) disederhanakan secara drastis:

1. **Tumpang tindih diabaikan**: $S_{rs} = \delta_{rs}$.
2. **Integral Coulomb sama**: $H_{rr} = \alpha$ untuk setiap atom karbon. $\alpha$ adalah energi elektron dalam orbital $2p_z$ karbon di dalam molekul, kira-kira negatif energi ionisasi orbital itu.
3. **Integral resonansi hanya antartetangga**: $H_{rs} = \beta$ bila atom $r$ dan $s$ terikat langsung, dan nol bila tidak. $\beta$ bernilai negatif.
4. **Semua ikatan sama**: $\beta$ sama untuk setiap pasangan tetangga, berapa pun panjang ikatannya.

Dengan pendekatan ini, matriks Hamiltonian π dapat ditulis

$$
\mathbf H = \alpha\,\mathbf I + \beta\,\mathbf A , \qquad \text{(13.4)}
$$

dengan $\mathbf A$ **matriks keterhubungan** (matriks topologi) molekul: $A_{rs} = 1$ bila $r$ dan $s$ terikat, nol bila tidak. Karena $\mathbf I$ dan $\mathbf A$ berkomutasi, vektor eigen $\mathbf H$ sama dengan vektor eigen $\mathbf A$, dan nilai eigennya

$$
E_k = \alpha + x_k\,\beta , \qquad \mathbf A\mathbf c_k = x_k\,\mathbf c_k . \qquad \text{(13.5)}
$$

Seluruh teori Hückel untuk hidrokarbon direduksi menjadi **masalah nilai eigen matriks keterhubungan**: geometri molekul tidak masuk sama sekali, hanya topologinya (siapa terikat dengan siapa). Karena $\beta < 0$, nilai $x_k$ yang **positif** memberi energi **di bawah** $\alpha$ (orbital ikatan) dan $x_k$ negatif memberi orbital antiikatan. Orbital dengan $x_k = 0$ adalah **nonikatan**.

Buku ini selalu memakai konvensi (13.5): $E = \alpha + x\beta$, dengan $x$ nilai eigen $\mathbf A$. Setelah dibagi $\beta$, determinan sekulernya menjadi

$$
\det(\mathbf A - x\,\mathbf I) = 0 . \qquad \text{(13.6)}
$$

### Besaran yang dihitung

Dari koefisien dan bilangan okupasi $n_k$ (0, 1, atau 2) kita menghitung:

$$
E_\pi = \sum_kn_kE_k , \qquad q_r = \sum_kn_kc_{rk}^2 , \qquad p_{rs} = \sum_kn_kc_{rk}c_{sk} , \qquad \text{(13.7)}
$$

yaitu **energi π total**, **kerapatan elektron π** pada atom $r$, dan **orde ikatan π** (Coulson) antara atom $r$ dan $s$. Muatan π atom $r$ adalah $1 - q_r$ untuk karbon yang menyumbang satu elektron. Ketiga besaran ini adalah inti subbab 13.9.

### Arti α dan β

Parameter $\alpha$ hanya menggeser semua energi; ia tidak mempengaruhi koefisien, muatan, atau selisih energi. Yang penting adalah $\beta$, yang mengukur kekuatan interaksi π antara dua karbon tetangga. Masalahnya, $\beta$ tidak mempunyai satu nilai "benar":

* Dari energi resonansi termokimia benzena ($2|\beta| \approx 150$ kJ/mol, subbab 13.7): $\beta \approx -75$ kJ/mol $\approx -0{,}8$ eV.
* Dari energi eksitasi π → π*: $\beta$ sekitar $-2{,}4$ sampai $-3{,}8$ eV, bergantung pada molekul yang dipakai (Contoh 13.14).

Perbedaan faktor tiga sampai lima ini bukan kesalahan pengukuran, melainkan tanda bahwa model Hückel memasukkan banyak efek (tolakan elektron, perubahan kerangka σ, korelasi) ke dalam satu parameter. Dalam setiap pemakaian, $\beta$ harus dikalibrasi untuk sifat yang dibicarakan.

::: {.awas}
**Awas · Tanda β dan x**

Karena $\beta < 0$, orbital dengan $x = +2$ adalah yang **paling rendah** energinya. Banyak buku menulis determinan sekuler dengan $x = (\alpha - E)/\beta$, sehingga akarnya berlawanan tanda dengan akar dalam buku ini. Kedua konvensi benar asalkan konsisten. Periksa selalu: orbital tanpa simpul (semua koefisien bertanda sama) harus menjadi orbital terendah.
:::

::: {.contoh}
**Contoh 13.11 · Etilena dengan tangan**

Tuliskan determinan sekuler Hückel untuk etilena, selesaikan untuk energi dan koefisien, lalu hitung $E_\pi$, $q_1$, dan $p_{12}$.

**Penyelesaian.** $\mathbf A = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$; $\det(\mathbf A - x\mathbf I) = x^2 - 1 = 0$, jadi $x = \pm1$: $E_1 = \alpha + \beta$, $E_2 = \alpha - \beta$. Untuk $x = 1$: $-c_1 + c_2 = 0$, dengan normalisasi $c_1 = c_2 = 1/\sqrt2$. Untuk $x = -1$: $c_1 = -c_2 = 1/\sqrt2$. Dua elektron di $\psi_1$: $E_\pi = 2\alpha + 2\beta$; $q_1 = 2(\tfrac12) = 1$; $p_{12} = 2(\tfrac12) = 1$.

**Memahami hasil.** Satu ikatan π penuh berorde 1, dan energi ikatan π dalam model ini $2\beta$. Eksitasi π → π* memerlukan $2|\beta|$. Etilena menyerap di sekitar 162 nm (7,65 eV), sehingga $|\beta|_\text{spek} = 3{,}8$ eV menurut etilena saja.
:::

::: {.contoh}
**Contoh 13.12 · Rutin Hückel dengan Python**

Tulis fungsi Python yang menerima banyaknya atom, daftar ikatan, dan banyaknya elektron π, lalu mengembalikan $x_k$, koefisien, $E_\pi$ (dalam satuan $\beta$, di luar $\alpha$), muatan, dan orde ikatan. Uji dengan butadiena.

**Penyelesaian.**

```python
import numpy as np
def huckel(n, ikatan, nel=None):
    A = np.zeros((n, n))
    for i, j in ikatan: A[i, j] = A[j, i] = 1
    x, C = np.linalg.eigh(A)
    x, C = x[::-1], C[:, ::-1]               # urutkan: x terbesar = energi terendah
    nel = n if nel is None else nel
    occ = np.array([min(2, max(0, nel - 2*k)) for k in range(n)])
    P = (C * occ) @ C.T                       # matriks kerapatan dan orde ikatan
    return x, C, (occ * x).sum(), 1 - np.diag(P), P

x, C, Epi, q, P = huckel(4, [(0, 1), (1, 2), (2, 3)])
print(x.round(4), Epi.round(4), q.round(3), P[0, 1].round(4), P[1, 2].round(4))
```

Keluaran: $x$ = 1,618; 0,618; $-0{,}618$; $-1{,}618$; $E_\pi = 4\alpha + 4{,}472\beta$; muatan semua nol; $p_{12} = 0{,}894$, $p_{23} = 0{,}447$.

**Memahami hasil.** Sepuluh baris kode menyelesaikan teori Hückel untuk hidrokarbon apa pun; perlu hanya daftar ikatan. Fungsi `eigh` untuk matriks simetris riil menjamin vektor eigen ortonormal. Heteroatom (subbab 13.8) cukup ditambahkan sebagai unsur diagonal dan unsur ikatan yang berbeda.
:::

::: {.contoh}
**Contoh 13.13 · Mengapa geometri tidak penting**

(a) Apakah teori Hückel membedakan butadiena *s-trans* dan *s-cis*? (b) Apakah ia membedakan benzena dari prisman (C₆H₆ berbentuk prisma) atau dari heksatriena siklik terpuntir? (c) Apa artinya bagi daya ramal model ini?

**Penyelesaian.** (a) Tidak: keduanya mempunyai matriks keterhubungan yang sama (rantai empat atom). (b) Prisman bukan sistem π (karbonnya sp³), jadi di luar jangkauan model. Untuk cincin enam yang terpuntir, matriks keterhubungannya sama dengan benzena, sehingga Hückel memberi energi yang sama, padahal puntiran mengurangi tumpang tindih $p_z$. (c) Model Hückel hanya dapat dipakai untuk sistem yang kurang lebih datar dengan ikatan-ikatan yang sebanding.

**Memahami hasil.** Ketidakpekaan terhadap geometri adalah kelemahan sekaligus kekuatan. Kekuatannya: kesimpulan tentang aromatisitas, simetri orbital, dan pola muatan murni topologis, sehingga sangat umum. Kelemahannya: perbedaan konformasi dan regangan harus ditangani dengan cara lain, misalnya dengan membuat $\beta$ bergantung pada sudut puntir, $\beta(\theta) = \beta_0\cos\theta$, seperti tumpang tindih π di subbab 12.4.
:::

::: {.kuis}
**Kuis cepat 13.4**

Untuk molekul dengan matriks keterhubungan $\mathbf A$, mengapa jumlah semua nilai eigen $x_k$ selalu nol? Apa artinya bagi rata-rata energi semua OM π?
:::

## 13.5 Etilena, alil, butadiena

### Sistem alil

Gugus alil, CH₂=CH–CH₂, mempunyai tiga atom karbon terkonjugasi. Ia dapat berupa kation (2 elektron π), radikal (3), atau anion (4). Determinan sekulernya

$$
\begin{vmatrix}-x & 1 & 0\\ 1 & -x & 1\\ 0 & 1 & -x\end{vmatrix} = -x^3 + 2x = 0 , \qquad x = \sqrt2,\ 0,\ -\sqrt2 . \qquad \text{(13.8)}
$$

Orbital-orbitalnya sama bentuknya dengan sistem tiga pusat F–Xe–F di subbab 12.8 (Gambar 12.7):

$$
\psi_1 = \tfrac12\phi_1 + \tfrac{1}{\sqrt2}\phi_2 + \tfrac12\phi_3 , \quad \psi_2 = \tfrac{1}{\sqrt2}(\phi_1 - \phi_3) , \quad \psi_3 = \tfrac12\phi_1 - \tfrac{1}{\sqrt2}\phi_2 + \tfrac12\phi_3 . \qquad \text{(13.9)}
$$

Orbital nonikatan $\psi_2$ hanya berada pada kedua karbon ujung, dengan simpul tepat di karbon tengah. Akibatnya:

* **Kation alil** ($\psi_1^2$): muatan positif $+\tfrac12$ pada C1 dan C3, nol pada C2. Nukleofil menyerang di ujung.
* **Radikal alil** ($\psi_1^2\psi_2^1$): kerapatan spin $\tfrac12$ pada C1 dan C3. Spektrum ESR menunjukkan kopling hiperhalus besar dengan H ujung.
* **Anion alil** ($\psi_1^2\psi_2^2$): muatan negatif $-\tfrac12$ pada C1 dan C3.

Energi π ketiganya, dari elektron di $\psi_1$, adalah $2\alpha + 2\sqrt2\beta$, ditambah $n_2\alpha$ untuk elektron di $\psi_2$. Dibandingkan dengan satu ikatan π terlokalisasi (etilena, $2\alpha + 2\beta$) ditambah satu orbital $p$ terpisah, delokalisasi menurunkan energi sebesar $(2\sqrt2 - 2)|\beta| = 0{,}828|\beta|$ untuk **ketiga** spesies. Inilah dasar kuantum **kestabilan alilik**: kation, radikal, dan anion alil semuanya distabilkan resonansi, dan ikatan C–H alilik lebih lemah daripada C–H alkana biasa (Contoh 13.16).

### Butadiena

Untuk butadiena, $\det(\mathbf A - x\mathbf I) = x^4 - 3x^2 + 1 = 0$, sehingga $x^2 = (3 \pm \sqrt5)/2$ dan

$$
x = \pm1{,}618 ,\ \pm0{,}618 . \qquad \text{(13.10)}
$$

Bilangan 1,618 dan 0,618 adalah perbandingan emas dan kebalikannya: $\tfrac12(1 + \sqrt5)$ dan $\tfrac12(\sqrt5 - 1)$. Koefisien-koefisiennya (Gambar 13.3):

| OM | $x$ | $c_1$ | $c_2$ | $c_3$ | $c_4$ | simpul |
|---|---|---|---|---|---|---|
| $\psi_1$ | 1,618 | 0,372 | 0,602 | 0,602 | 0,372 | 0 |
| $\psi_2$ (HOMO) | 0,618 | 0,602 | 0,372 | $-0{,}372$ | $-0{,}602$ | 1 |
| $\psi_3$ (LUMO) | $-0{,}618$ | 0,602 | $-0{,}372$ | $-0{,}372$ | 0,602 | 2 |
| $\psi_4$ | $-1{,}618$ | 0,372 | $-0{,}602$ | 0,602 | $-0{,}372$ | 3 |

![Gambar 13.3 Tingkat energi Hückel dan koefisien OM π etilena, radikal alil, dan butadiena. Lingkaran: koefisien $2p_z$ setiap karbon (ukuran sebanding dengan besar koefisien; biru positif, jingga negatif). Banyaknya simpul bertambah satu dari satu orbital ke orbital berikutnya.](fig/c_huckel.png){width=94%}

Pola simpulnya umum: OM ke-$k$ mempunyai $k - 1$ simpul, persis seperti fungsi gelombang partikel dalam kotak (subbab 3.6). Empat elektron π mengisi $\psi_1$ dan $\psi_2$:

$$
E_\pi = 2(\alpha + 1{,}618\beta) + 2(\alpha + 0{,}618\beta) = 4\alpha + 4{,}472\beta .
$$

Dua ikatan rangkap terlokalisasi memberi $4\alpha + 4\beta$; selisihnya, $0{,}472\beta$, adalah **energi delokalisasi** butadiena. Orde ikatan π: $p_{12} = p_{34} = 0{,}894$, $p_{23} = 0{,}447$. Ikatan tengah mempunyai sifat rangkap yang nyata, sehingga butadiena lebih suka datar (*s-trans*), dan rotasi di sekitar C2–C3 terhalang beberapa puluh kJ/mol.

Celah HOMO–LUMO butadiena adalah $1{,}236|\beta|$, lebih kecil daripada etilena ($2|\beta|$). Inilah sebabnya butadiena menyerap pada panjang gelombang lebih panjang (217 nm) daripada etilena (162 nm). Tetapi bila $|\beta|$ dihitung dari kedua spektrum, hasilnya berbeda (Contoh 13.14): model Hückel menangkap arah perubahan, bukan besarnya.

::: {.contoh}
**Contoh 13.14 · β dari spektrum: sebuah inkonsistensi**

Hitung $|\beta|$ dari energi eksitasi π → π* pertama: etilena 162 nm, butadiena 217 nm, heksatriena 258 nm (celah Hückel 2; 1,236; 0,890 dalam satuan $|\beta|$). Apa kesimpulannya?

**Penyelesaian.** Energi foton: 7,65; 5,71; 4,81 eV. $|\beta| = E/\text{celah}$: 3,83; 4,62; 5,40 eV.

**Memahami hasil.** Nilai $|\beta|$ "spektroskopik" bertambah dengan panjang rantai. Model Hückel menganggap energi eksitasi sama dengan selisih energi orbital, padahal keadaan tereksitasi juga dipengaruhi oleh tolakan dan korelasi elektron, dan panjang ikatan dalam poliena berselang-seling. Bila data dipaskan dengan garis lurus yang mempunyai titik potong, $E = a + b\cdot\text{celah}$, kecocokannya jauh lebih baik (subbab 13.6). Metode PPP di subbab 13.12 menjelaskan asal titik potong itu.
:::

::: {.contoh}
**Contoh 13.15 · Alil dengan tangan**

(a) Turunkan koefisien $\psi_1$ alil dari persamaan linear untuk $x = \sqrt2$. (b) Hitung muatan π pada setiap karbon kation alil. (c) Hitung orde ikatan $p_{12}$ untuk kation, radikal, dan anion.

**Penyelesaian.** (a) Baris pertama $(\mathbf A - x\mathbf I)\mathbf c = 0$: $-\sqrt2c_1 + c_2 = 0$, jadi $c_2 = \sqrt2c_1$. Baris ketiga: $c_2 = \sqrt2c_3$, jadi $c_3 = c_1$. Normalisasi: $c_1^2 + 2c_1^2 + c_1^2 = 1$, $c_1 = \tfrac12$. Jadi $\psi_1 = \tfrac12\phi_1 + \tfrac{1}{\sqrt2}\phi_2 + \tfrac12\phi_3$.

\(b) $q_1 = 2(\tfrac14) = \tfrac12$, $q_2 = 2(\tfrac12) = 1$. Muatan: C1 dan C3 $+\tfrac12$, C2 0.

\(c) Sumbangan $\psi_1$: $2(\tfrac12)(\tfrac{1}{\sqrt2}) = 0{,}707$. Sumbangan $\psi_2$: $c_2 = 0$, sehingga nol. Jadi $p_{12} = 0{,}707$ untuk ketiga spesies.

**Memahami hasil.** Karena orbital nonikatan alil bersimpul di C2, mengisinya tidak mengubah orde ikatan; yang berubah hanya muatan (kation, anion) atau spin (radikal) di C1 dan C3. Hal yang sama dijumpai pada ikatan 3c-4e (subbab 12.8): orbital nonikatan menampung muatan tanpa mengubah ikatan. Kedua ikatan C–C alil setara dengan orde $1 + 0{,}707$, sesuai dengan dua struktur resonansi setara.
:::

::: {.contoh}
**Contoh 13.16 · Kestabilan radikal alil**

Energi disosiasi C–H alilik pada propena (CH₂=CH–CH₂–H) adalah 88,8 kkal/mol, sedangkan C–H primer pada etana 101,1 kkal/mol. (a) Hitung selisihnya dalam kJ/mol. (b) Bandingkan dengan energi delokalisasi radikal alil, $0{,}828|\beta|$, dengan $|\beta| = 75$ kJ/mol. (c) Model McConnell menghubungkan kopling hiperhalus proton dengan kerapatan spin, $a_\text{H} = Q\rho$ dengan $Q \approx 2{,}3$ mT. Ramalkan $a_\text{H}$ untuk H ujung dan H tengah, dan bandingkan dengan nilai teramati (sekitar 1,4 dan 0,41 mT).

**Penyelesaian.** (a) $(101{,}1 - 88{,}8) \times 4{,}184 = 51{,}5$ kJ/mol. (b) $0{,}828 \times 75 = 62$ kJ/mol. (c) Ujung: $\rho = \tfrac12$, $a = 1{,}15$ mT. Tengah: $\rho = 0$, $a = 0$.

**Memahami hasil.** Ikatan C–H alilik sekitar 50 kJ/mol lebih lemah karena radikal yang terbentuk distabilkan oleh delokalisasi; Hückel menaksirnya dengan wajar. Ramalan ESR untuk H ujung juga wajar, tetapi untuk H tengah Hückel meramalkan nol, padahal teramati 0,41 mT. Kopling di tengah berasal dari **polarisasi spin**: elektron tak berpasangan di C1 dan C3 sedikit menyelaraskan spin elektron-elektron lain, sehingga muncul kerapatan spin **negatif** kecil di C2. Efek ini memerlukan tolakan elektron eksplisit, yang tidak ada dalam model Hückel.
:::

::: {.contoh}
**Contoh 13.17 · Energi konjugasi butadiena**

Entalpi hidrogenasi but-1-ena menjadi butana $-126{,}8$ kJ/mol, dan buta-1,3-diena menjadi butana $-236{,}7$ kJ/mol. (a) Hitung energi konjugasi termokimia. (b) Bandingkan dengan energi delokalisasi Hückel $0{,}472|\beta|$ ($|\beta| = 75$ kJ/mol). (c) Mengapa model Hückel memberi nilai terlalu besar?

**Penyelesaian.** (a) $2(126{,}8) - 236{,}7 = 16{,}9$ kJ/mol. (b) $0{,}472 \times 75 = 35$ kJ/mol. (c) Dengan $|\beta|$ yang dikalibrasi pada benzena, Hückel melebih-lebihkan stabilisasi butadiena. Sebagian "energi konjugasi" yang tersisa pun bukan delokalisasi π: ikatan tengah butadiena adalah ikatan sp²–sp², yang lebih kuat daripada ikatan sp³–sp² pada butena (subbab 12.7).

**Memahami hasil.** Delokalisasi π pada poliena linear lemah dibanding pada benzena. Perbandingan $0{,}472/2 = 0{,}24$ dari model Hückel mengatakan hal yang sama secara kualitatif: energi delokalisasi per elektron π benzena jauh lebih besar daripada butadiena. Perbedaan kualitatif inilah, bukan nilai mutlaknya, yang membuat aromatisitas istimewa.
:::

::: {.kuis}
**Kuis cepat 13.5**

Pada anion pentadienil (lima karbon, enam elektron π), di karbon mana muatan negatif terkumpul? (Petunjuk: orbital nonikatan rantai lima atom mempunyai koefisien $\tfrac{1}{\sqrt3}(1, 0, -1, 0, 1)$.)
:::

## 13.6 Poliena linear dan siklik: rumus umum

### Rantai linear

Untuk rantai $N$ atom karbon, persamaan $\mathbf A\mathbf c = x\mathbf c$ berbunyi, untuk atom ke-$r$ di dalam rantai,

$$
c_{r-1} + c_{r+1} = x\,c_r , \qquad r = 1, \ldots, N , \qquad \text{(13.11)}
$$

dengan syarat batas $c_0 = c_{N+1} = 0$ (tidak ada atom di luar ujung). Ini adalah persamaan beda orde dua, analog diskret dari $\psi'' = -k^2\psi$ untuk partikel dalam kotak. Coba $c_r = \sin(r\theta)$: dengan identitas $\sin[(r - 1)\theta] + \sin[(r + 1)\theta] = 2\cos\theta\sin(r\theta)$, persamaan terpenuhi bila $x = 2\cos\theta$. Syarat $c_0 = 0$ sudah dipenuhi oleh sinus; syarat $c_{N+1} = \sin[(N + 1)\theta] = 0$ menuntut $\theta = k\pi/(N + 1)$. Jadi

$$
\boxed{\ E_k = \alpha + 2\beta\cos\frac{k\pi}{N + 1} , \qquad c_{rk} = \left(\frac{2}{N + 1}\right)^{1/2}\sin\frac{rk\pi}{N + 1} , \qquad k = 1, \ldots, N\ } \qquad \text{(13.12)}
$$

Faktor normalisasi berasal dari $\sum_{r=1}^N\sin^2[rk\pi/(N + 1)] = (N + 1)/2$. Semua energi terletak di antara $\alpha + 2\beta$ dan $\alpha - 2\beta$, dan ketika $N$ bertambah, tingkat-tingkatnya makin rapat mengisi pita selebar $4|\beta|$ (Gambar 13.4(a)). Hasil ini akan menjadi pita energi di subbab 13.13.

Untuk poliena dengan $N$ genap dan $N$ elektron π, HOMO adalah $k = N/2$ dan LUMO $k = N/2 + 1$. Celahnya

$$
\Delta x = 2\left[\cos\frac{N\pi}{2(N + 1)} - \cos\frac{(N + 2)\pi}{2(N + 1)}\right] = 4\sin\frac{\pi}{2(N + 1)} \approx \frac{2\pi}{N + 1} . \qquad \text{(13.13)}
$$

Celah mengecil kira-kira sebanding dengan $1/N$, seperti pada model elektron bebas (subbab 3.8). Inilah sebabnya poliena panjang berwarna: β-karotena, dengan 11 ikatan rangkap terkonjugasi, menyerap cahaya biru dan tampak jingga.

![Gambar 13.4 (a) Tingkat energi π poliena linear dengan $N$ atom karbon menurut (13.12); biru: orbital ikatan ($x > 0$), jingga: antiikatan. Tingkat-tingkat mengisi pita antara $x = -2$ dan $x = +2$. (b) Energi serapan UV terkuat poliena (C₂ etilena sampai C₁₀ dekapentaena) terhadap celah HOMO–LUMO Hückel, dengan garis lurus terbaik.](fig/c_poliena.png){width=94%}

### Cincin

Untuk cincin $N$ atom, syarat batasnya periodik: $c_{N+1} = c_1$ dan $c_0 = c_N$. Coba $c_r = e^{ir\theta}$: persamaan (13.11) memberi $x = e^{-i\theta} + e^{i\theta} = 2\cos\theta$, dan periodisitas $e^{iN\theta} = 1$ menuntut $\theta = 2\pi k/N$. Jadi

$$
\boxed{\ E_k = \alpha + 2\beta\cos\frac{2\pi k}{N} , \qquad c_{rk} = \frac{1}{\sqrt N}e^{2\pi irk/N} , \qquad k = 0, \pm1, \pm2, \ldots\ } \qquad \text{(13.14)}
$$

dengan $k$ berjalan dari $-\lfloor(N - 1)/2\rfloor$ sampai $\lfloor N/2\rfloor$. Tingkat terendah ($k = 0$) selalu $\alpha + 2\beta$ dan tunggal. Karena $\cos(-\theta) = \cos\theta$, orbital $k$ dan $-k$ **berdegenerasi**; kombinasi riilnya adalah kosinus dan sinus. Untuk $N$ genap, tingkat tertinggi ($k = N/2$, $\alpha - 2\beta$) juga tunggal.

Ada cara mengingat yang elegan: **lingkaran Frost** (A. A. Frost dan B. Musulin, 1953). Gambar lingkaran berjari-jari $2|\beta|$ dengan pusat di $\alpha$, lalu lukis segi-$N$ beraturan di dalamnya dengan satu titik sudut di bawah. Ketinggian setiap titik sudut adalah satu tingkat energi (Gambar 13.5). Benzena: $\alpha + 2\beta$, $\alpha + \beta$ (dua), $\alpha - \beta$ (dua), $\alpha - 2\beta$.

![Gambar 13.5 Lingkaran Frost untuk cincin beranggota 3 sampai 8, dengan elektron π diisikan dari bawah. Ketinggian setiap titik sudut segi banyak adalah energi satu OM π; garis mendatar tipis menandai $\alpha$. Pada C₄H₄ dan C₈H₈ datar, dua elektron terakhir masing-masing menempati satu orbital nonikatan yang berdegenerasi (aturan Hund).](fig/c_frost.png){width=96%}

### Membandingkan rantai dan cincin

Menutup rantai menjadi cincin mengubah pola tingkat energi secara mendasar. Pada rantai, semua tingkat tunggal dan simetris di sekitar $\alpha$. Pada cincin, tingkat-tingkat berpasangan (berdegenerasi), kecuali yang terendah (dan yang tertinggi bila $N$ genap). Konsekuensinya bagi pengisian elektron:

* Orbital terendah (tunggal) memuat 2 elektron; setiap pasangan berdegenerasi berikutnya memuat 4 elektron.
* Kulit tertutup (semua orbital ikatan terisi penuh, tidak ada orbital berdegenerasi yang setengah terisi) tercapai pada $2, 6, 10, 14, \ldots = 4n + 2$ elektron.

Inilah asal **aturan Hückel** $4n + 2$, yang dibahas di subbab 13.7.

::: {.contoh}
**Contoh 13.18 · Memeriksa rumus rantai**

Pakai (13.12) untuk heksatriena ($N = 6$): hitung keenam nilai $x_k$, koefisien HOMO, dan celah HOMO–LUMO. Bandingkan dengan diagonalisasi numerik.

**Penyelesaian.** $x_k = 2\cos(k\pi/7)$: 1,802; 1,247; 0,445; $-0{,}445$; $-1{,}247$; $-1{,}802$. HOMO ($k = 3$): $c_{r3} = \sqrt{2/7}\sin(3r\pi/7)$ = 0,521; 0,232; $-0{,}418$; $-0{,}418$; 0,232; 0,521 (dengan tanda keseluruhan bebas). Celah $2(0{,}445) = 0{,}890$; rumus (13.13): $4\sin(\pi/14) = 0{,}890$. Diagonalisasi numerik memberikan nilai yang sama sampai angka terakhir.

**Memahami hasil.** HOMO heksatriena mempunyai dua simpul dan koefisien terbesar di kedua ujung. Pola ini menentukan stereokimia penutupan cincin heksatriena (subbab 13.11): yang penting adalah tanda koefisien di C1 dan C6, yang di sini sama.
:::

::: {.contoh}
**Contoh 13.19 · Kalibrasi serapan poliena**

Energi serapan π → π* terkuat: etilena 7,65 eV, butadiena 5,71 eV, heksatriena 4,81 eV, oktatetraena sekitar 4,28 eV, dekapentaena sekitar 3,71 eV. (a) Paskan $E = a + b\,\Delta x$ dengan $\Delta x$ dari (13.13). (b) Ramalkan λ untuk β-karotena ($N = 22$) dan bandingkan dengan nilai teramati sekitar 450 nm.

**Penyelesaian.** (a) $\Delta x$ = 2,000; 1,236; 0,890; 0,695; 0,569. Kuadrat terkecil: $a = 2{,}34$ eV, $b = 2{,}68$ eV; ramalan 7,70; 5,66; 4,73; 4,20; 3,87 eV. (b) $\Delta x = 4\sin(\pi/46) = 0{,}273$; $E = 2{,}34 + 2{,}68(0{,}273) = 3{,}07$ eV; $\lambda = 1239{,}8/3{,}07 = 403$ nm.

**Memahami hasil.** Garis dengan titik potong 2,34 eV jauh lebih baik daripada garis melalui titik asal (Contoh 13.14). Ramalan untuk β-karotena (403 nm) masih terlalu pendek dibanding 450 nm: rantai yang panjang membawa sifat-sifat baru (energi eksitasi yang mendatar, efek gugus ujung) yang memerlukan model lebih baik. Titik potong positif menyatakan bahwa celah energi **tidak** menuju nol untuk rantai tak hingga; subbab 13.13 menjelaskannya dengan alternasi ikatan.
:::

::: {.contoh}
**Contoh 13.20 · Benzena dari rumus cincin**

Dengan (13.14) untuk $N = 6$, tentukan energi dan bentuk riil keenam OM benzena. Hitung $E_\pi$ untuk enam elektron.

**Penyelesaian.** $k = 0$: $x = 2$, $\psi_0 = \tfrac{1}{\sqrt6}(1, 1, 1, 1, 1, 1)$. $k = \pm1$: $x = 1$; kombinasi riil $\tfrac{1}{\sqrt{12}}(2, 1, -1, -2, -1, 1)$ dan $\tfrac12(0, 1, 1, 0, -1, -1)$. $k = \pm2$: $x = -1$; $\tfrac{1}{\sqrt{12}}(2, -1, -1, 2, -1, -1)$ dan $\tfrac12(0, 1, -1, 0, 1, -1)$. $k = 3$: $x = -2$, $\tfrac{1}{\sqrt6}(1, -1, 1, -1, 1, -1)$. Enam elektron mengisi $k = 0, \pm1$: $E_\pi = 2(\alpha + 2\beta) + 4(\alpha + \beta) = 6\alpha + 8\beta$.

**Memahami hasil.** Tiga ikatan rangkap terlokalisasi memberi $6\alpha + 6\beta$, sehingga energi delokalisasi benzena $2\beta$, lebih dari empat kali butadiena ($0{,}472\beta$). Pasangan orbital berdegenerasi $e_{1g}$ (HOMO) dan $e_{2u}$ (LUMO) dalam notasi $D_{6h}$ adalah ciri benzena; eksitasi dari pasangan HOMO ke pasangan LUMO menghasilkan empat keadaan tereksitasi yang dalam model Hückel berdegenerasi (subbab 13.12).
:::

::: {.contoh}
**Contoh 13.21 · Rantai panjang dengan Python**

Bandingkan nilai eigen numerik matriks keterhubungan rantai $N = 10$ dengan (13.12), dan periksa rumus normalisasi koefisien.

**Penyelesaian.**

```python
import numpy as np
N = 10
A = np.diag(np.ones(N - 1), 1); A = A + A.T
x = np.sort(np.linalg.eigvalsh(A))[::-1]
k = np.arange(1, N + 1)
print(np.allclose(x, 2*np.cos(k*np.pi/(N + 1))))           # True
r = np.arange(1, N + 1)
c = np.sqrt(2/(N + 1))*np.sin(np.outer(r, k)*np.pi/(N + 1))  # kolom = OM
print(np.allclose(c.T @ c, np.eye(N)), np.allclose(A @ c, c*x))   # True True
```

Celah HOMO–LUMO: $4\sin(\pi/22) = 0{,}569$.

**Memahami hasil.** Rumus analitik dan diagonalisasi numerik sama persis. Dalam praktik, untuk molekul tanpa simetri sederhana kita selalu memakai diagonalisasi numerik; rumus analitik berguna untuk memahami tren (celah $\propto 1/N$, pita selebar $4|\beta|$) dan untuk limit $N \to \infty$.
:::

::: {.kuis}
**Kuis cepat 13.6**

Berapa energi orbital terendah rantai linear yang sangat panjang, dan berapa energi orbital terendah cincin beranggota berapa pun? Mengapa keduanya hampir sama untuk $N$ besar?
:::
