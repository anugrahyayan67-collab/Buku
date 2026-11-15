## 17.3 Persamaan Roothaan dan prosedur SCF

### Dari persamaan diferensial ke persamaan matriks

Untuk atom, persamaan Hartree–Fock dapat diselesaikan secara numerik pada kisi radial (subbab 9.8). Untuk molekul, yang tidak mempunyai simetri bola, cara itu tidak praktis. Clemens Roothaan dan George Hall secara terpisah (1951) mengusulkan jalan yang sama dengan LCAO (subbab 11.4): uraikan setiap orbital ruang atas $K$ **fungsi basis** $\phi_\mu$ yang diketahui,

$$
\psi_i(\mathbf r) = \sum_{\mu=1}^K C_{\mu i}\,\phi_\mu(\mathbf r) . \qquad \text{(17.9)}
$$

Masukkan ke persamaan Hartree–Fock kulit tertutup $\hat f\psi_i = \varepsilon_i\psi_i$, kalikan dari kiri dengan $\phi_\mu^*$, dan integrasikan:

$$
\sum_\nu C_{\nu i}\int\phi_\mu^*\hat f\phi_\nu\,d\mathbf r = \varepsilon_i\sum_\nu C_{\nu i}\int\phi_\mu^*\phi_\nu\,d\mathbf r .
$$

Dengan **matriks Fock** $F_{\mu\nu} = \langle\phi_\mu|\hat f|\phi_\nu\rangle$ dan **matriks tumpang tindih** $S_{\mu\nu} = \langle\phi_\mu|\phi_\nu\rangle$, ini adalah **persamaan Roothaan**:

$$
\mathbf F\mathbf C = \mathbf S\mathbf C\boldsymbol\varepsilon . \qquad \text{(17.10)}
$$

Persamaan diferensial integro yang rumit telah menjadi persamaan nilai eigen matriks yang diperumum, persis seperti persamaan sekuler metode variasi linear (subbab 8.4). Kolom-kolom $\mathbf C$ adalah koefisien orbital molekul, dan $\boldsymbol\varepsilon$ matriks diagonal energi orbital. Dengan $K$ fungsi basis diperoleh $K$ orbital: $N/2$ orbital terendah diisi dua elektron (**orbital terisi**), sisanya kosong (**orbital virtual**). Orbital terisi tertinggi disebut HOMO, orbital kosong terendah LUMO.

### Matriks kerapatan dan matriks Fock

Rapat elektron kulit tertutup adalah $\rho(\mathbf r) = 2\sum_a|\psi_a|^2 = \sum_{\mu\nu}P_{\mu\nu}\phi_\mu(\mathbf r)\phi_\nu^*(\mathbf r)$, dengan **matriks kerapatan**

$$
P_{\mu\nu} = 2\sum_{a=1}^{N/2}C_{\mu a}C_{\nu a}^* . \qquad \text{(17.11)}
$$

Matriks kerapatan memuat seluruh informasi tentang fungsi gelombang HF. Matriks Fock dapat ditulis dengannya:

$$
F_{\mu\nu} = H^\text{inti}_{\mu\nu} + \sum_{\lambda\sigma}P_{\lambda\sigma}\left[(\mu\nu|\sigma\lambda) - \tfrac12(\mu\lambda|\sigma\nu)\right] , \qquad \text{(17.12)}
$$

dengan $H^\text{inti}_{\mu\nu} = T_{\mu\nu} + V_{\mu\nu}$ (energi kinetik dan tarikan semua inti) dan **integral tolakan dua elektron** dalam notasi kimiawan

$$
(\mu\nu|\lambda\sigma) = \iint\frac{\phi_\mu^*(\mathbf r_1)\phi_\nu(\mathbf r_1)\,\phi_\lambda^*(\mathbf r_2)\phi_\sigma(\mathbf r_2)}{r_{12}}\,d\mathbf r_1d\mathbf r_2 . \qquad \text{(17.13)}
$$

Suku pertama dalam kurung siku (17.12) adalah sumbangan Coulomb, suku kedua sumbangan pertukaran. Energi elektronik, dari (17.8), menjadi

$$
E_\text{el} = \tfrac12\sum_{\mu\nu}P_{\nu\mu}\left(H^\text{inti}_{\mu\nu} + F_{\mu\nu}\right) . \qquad \text{(17.14)}
$$

Untuk fungsi riil, integral (17.13) tidak berubah bila $\mu \leftrightarrow \nu$, $\lambda \leftrightarrow \sigma$, atau pasangan $(\mu\nu) \leftrightarrow (\lambda\sigma)$ ditukar: ada delapan kesetaraan, sehingga banyaknya integral berbeda sekitar $K^4/8$. Untuk 100 fungsi basis itu sekitar 13 juta integral; untuk 1000 fungsi, sekitar $10^{11}$ integral atau satu terabita. Program modern karena itu tidak menyimpan integral, melainkan menghitung ulang yang diperlukan pada setiap siklus (**SCF langsung**), dan membuang integral yang dapat dipastikan sangat kecil (penyaringan Schwarz).

### Prosedur SCF

Matriks Fock bergantung pada $\mathbf P$, yang bergantung pada $\mathbf C$, yang diperoleh dari $\mathbf F$. Lingkaran ini diputus secara iteratif:

1. Tentukan geometri, himpunan basis, dan banyaknya elektron. Hitung $\mathbf S$, $\mathbf H^\text{inti}$, dan integral dua elektron.
2. Bentuk matriks ortogonalisasi $\mathbf X = \mathbf S^{-1/2}$ (ortogonalisasi simetris atau Löwdin), sehingga $\mathbf X^\dagger\mathbf S\mathbf X = \mathbf 1$.
3. Tebak matriks kerapatan awal (misalnya dari diagonalisasi $\mathbf H^\text{inti}$ saja, atau dari superposisi kerapatan atom).
4. Bentuk $\mathbf F$ dari (17.12).
5. Ubah ke basis ortonormal, $\mathbf F' = \mathbf X^\dagger\mathbf F\mathbf X$, lalu diagonalkan: $\mathbf F'\mathbf C' = \mathbf C'\boldsymbol\varepsilon$. Kembalikan, $\mathbf C = \mathbf X\mathbf C'$.
6. Bentuk $\mathbf P$ baru dari $N/2$ kolom terendah $\mathbf C$.
7. Bila $\mathbf P$ (dan energi) tidak berubah lagi dalam batas toleransi, berhenti; bila belum, kembali ke langkah 4.

Langkah 5 adalah trik matriks dari subbab 2.8: persamaan nilai eigen diperumum $\mathbf F\mathbf C = \mathbf S\mathbf C\boldsymbol\varepsilon$ diubah menjadi persamaan nilai eigen biasa dengan matriks simetris. Iterasi sederhana sering berosilasi atau lambat. Hampir semua program memakai **DIIS** (*direct inversion in the iterative subspace*, Péter Pulay, 1980): matriks Fock baru disusun sebagai kombinasi linear matriks-matriks Fock sebelumnya, dengan koefisien yang meminimumkan vektor galat $\mathbf F\mathbf P\mathbf S - \mathbf S\mathbf P\mathbf F$. Vektor galat ini nol tepat pada penyelesaian, karena pada swakonsistensi $\mathbf F$ dan $\mathbf P$ "komut" dalam metrik $\mathbf S$.

![Gambar 17.3 Konvergensi SCF untuk H₂O dengan basis STO-3G (geometri percobaan), dimulai dari tebakan Hcore. Sumbu tegak: selisih energi terhadap energi akhir, skala logaritmik. Iterasi biasa (lingkaran) memerlukan 15 siklus untuk mencapai 10⁻¹⁰ hartree; DIIS (segitiga) memerlukan 7 siklus.](fig/c_scf.png){width=74%}

### Menghitung integral dengan fungsi Gauss

Semua bahan (17.12) adalah integral atas fungsi basis. Seperti akan kita bahas di subbab 17.5, fungsi basis praktis adalah kombinasi fungsi Gauss, karena hasil kali dua fungsi Gauss yang berpusat di titik berbeda adalah satu fungsi Gauss di titik di antaranya (subbab 2.2). Untuk dua fungsi Gauss $s$ tak ternormalisasi $e^{-a|\mathbf r - \mathbf A|^2}$ dan $e^{-b|\mathbf r - \mathbf B|^2}$, dengan $p = a + b$ dan $\mathbf P = (a\mathbf A + b\mathbf B)/p$, semua integral dapat ditulis tertutup:

$$
S = \left(\frac\pi p\right)^{3/2}e^{-\frac{ab}{p}|\mathbf A - \mathbf B|^2}, \qquad T = \frac{ab}{p}\left(3 - \frac{2ab}{p}|\mathbf A - \mathbf B|^2\right)S , \qquad \text{(17.15)}
$$

$$
V_C = -\frac{2\pi Z_C}{p}\,e^{-\frac{ab}{p}|\mathbf A - \mathbf B|^2}F_0\!\left(p|\mathbf P - \mathbf C|^2\right) , \qquad \text{(17.16)}
$$

dan, untuk pasangan kedua dengan $q = c + d$ dan pusat $\mathbf Q$,

$$
(ab|cd) = \frac{2\pi^{5/2}}{pq\sqrt{p + q}}\,e^{-\frac{ab}{p}|\mathbf A - \mathbf B|^2 - \frac{cd}{q}|\mathbf C - \mathbf D|^2}F_0\!\left(\frac{pq}{p + q}|\mathbf P - \mathbf Q|^2\right) , \qquad \text{(17.17)}
$$

dengan **fungsi Boys** orde nol $F_0(t) = \int_0^1e^{-tu^2}du = \tfrac12\sqrt{\pi/t}\,\operatorname{erf}(\sqrt t)$ dan $F_0(0) = 1$. Fungsi Boys muncul dari integral $1/r$ setelah fungsi Gauss digabung. Untuk fungsi Gauss dengan momentum sudut lebih tinggi (fungsi p, d, f), integral diperoleh dengan rumus rekursi yang memakai fungsi Boys orde lebih tinggi; skema yang paling banyak dipakai adalah McMurchie–Davidson dan Obara–Saika.

::: {.dalam}
**Dari hasil kali Gauss ke fungsi Boys**

Untuk dua fungsi Gauss $s$ berpusat di $\mathbf A$ dan $\mathbf B$, lengkapkan kuadrat dalam eksponen:

$$
a|\mathbf r - \mathbf A|^2 + b|\mathbf r - \mathbf B|^2 = p|\mathbf r - \mathbf P|^2 + \frac{ab}{p}|\mathbf A - \mathbf B|^2, \qquad p = a + b, \quad \mathbf P = \frac{a\mathbf A + b\mathbf B}{p} .
$$

Jadi hasil kalinya adalah tetapan $K_{AB} = e^{-ab|\mathbf A - \mathbf B|^2/p}$ dikali satu fungsi Gauss di $\mathbf P$. Integral tumpang tindih langsung mengikuti dari $\int e^{-p|\mathbf r - \mathbf P|^2}d\mathbf r = (\pi/p)^{3/2}$ (subbab 2.2). Untuk tarikan inti, kesulitannya adalah $1/|\mathbf r - \mathbf C|$. Tuliskan dengan identitas

$$
\frac{1}{|\mathbf r - \mathbf C|} = \frac{2}{\sqrt\pi}\int_0^\infty e^{-t^2|\mathbf r - \mathbf C|^2}dt ,
$$

yang mengubah $1/r$ menjadi "fungsi Gauss yang dirata-ratakan atas eksponen". Sekarang integral atas $\mathbf r$ adalah integral hasil kali dua fungsi Gauss (di $\mathbf P$ dan $\mathbf C$), yang dengan teorema yang sama memberi $(\pi/(p + t^2))^{3/2}e^{-pt^2|\mathbf P - \mathbf C|^2/(p + t^2)}$. Substitusi $u^2 = t^2/(p + t^2)$, dengan $dt = \sqrt p\,du/(1 - u^2)^{3/2}$, mengubah sisa integral menjadi

$$
\int\frac{e^{-p|\mathbf r - \mathbf P|^2}}{|\mathbf r - \mathbf C|}d\mathbf r = \frac{2\pi}{p}\int_0^1e^{-p|\mathbf P - \mathbf C|^2u^2}du = \frac{2\pi}{p}F_0\!\left(p|\mathbf P - \mathbf C|^2\right) ,
$$

yang setelah dikali $K_{AB}$ dan $-Z_C$ adalah (17.16). Integral dua elektron (17.17) diperoleh dengan cara yang sama: kedua pasangan digabung menjadi fungsi Gauss di $\mathbf P$ dan $\mathbf Q$, lalu $1/r_{12}$ diganti dengan identitas di atas. Seluruh mesin integral kimia kuantum adalah variasi gagasan ini.
:::

### Program SCF pertama

Program berikut, sekitar lima puluh baris, menghitung semua integral untuk molekul diatom dengan satu fungsi STO-3G 1s pada setiap atom memakai (17.15)–(17.17), lalu menjalankan prosedur SCF. Ia dipakai di Contoh 17.10.

```python
import numpy as np
from scipy.special import erf

# STO-3G untuk 1s dengan zeta = 1; eksponen dipersekalakan dengan zeta**2
d0 = np.array([0.444635, 0.535328, 0.154329])
a0 = np.array([0.109818, 0.405771, 2.227660])

def F0(t):                       # fungsi Boys orde nol
    return 1.0 if t < 1e-10 else 0.5 * np.sqrt(np.pi / t) * erf(np.sqrt(t))

def scf(Z, zeta, R, nel=2, siklus=30):
    X = np.array([0.0, R])       # posisi inti pada sumbu z
    # primitif tiap atom: (eksponen, koefisien ternormalisasi)
    prim = [[(z**2 * a0[k], d0[k] * (2 * z**2 * a0[k] / np.pi)**0.75)
             for k in range(3)] for z in zeta]
    n = len(X)
    S, T, V = np.zeros((n, n)), np.zeros((n, n)), np.zeros((n, n))
    G = np.zeros((n, n, n, n))
    for i in range(n):
        for j in range(n):
            for a, ca in prim[i]:
                for b, cb in prim[j]:
                    p = a + b; P = (a * X[i] + b * X[j]) / p
                    K = ca * cb * np.exp(-a * b / p * (X[i] - X[j])**2)
                    S[i, j] += K * (np.pi / p)**1.5
                    T[i, j] += K * (np.pi / p)**1.5 * a * b / p \
                               * (3 - 2 * a * b / p * (X[i] - X[j])**2)
                    for C in range(n):
                        V[i, j] -= K * 2 * np.pi / p * Z[C] * F0(p * (P - X[C])**2)
                    for k in range(n):
                        for l in range(n):
                            for c, cc in prim[k]:
                                for d, cd in prim[l]:
                                    q = c + d; Q = (c * X[k] + d * X[l]) / q
                                    L = cc * cd * np.exp(-c * d / q * (X[k] - X[l])**2)
                                    G[i, j, k, l] += (K * L * 2 * np.pi**2.5
                                        / (p * q * np.sqrt(p + q))
                                        * F0(p * q / (p + q) * (P - Q)**2))
    H = T + V
    s, U = np.linalg.eigh(S)
    Xm = U @ np.diag(s**-0.5) @ U.T          # ortogonalisasi simetris
    P = np.zeros((n, n))                      # tebakan awal: Hcore
    for it in range(siklus):
        F = H + np.einsum('kl,ijkl->ij', P, G) - 0.5 * np.einsum('kl,ilkj->ij', P, G)
        e, Cp = np.linalg.eigh(Xm.T @ F @ Xm); C = Xm @ Cp
        Pbaru = 2 * C[:, :nel // 2] @ C[:, :nel // 2].T
        if np.abs(Pbaru - P).max() < 1e-8: break
        P = Pbaru
    Eel = 0.5 * np.sum(P * (H + F))
    return Eel + Z[0] * Z[1] / R, e, C, S, P

for nama, Z, zeta, R in [('H2', [1, 1], [1.24, 1.24], 1.4),
                         ('HeH+', [2, 1], [1.69, 1.24], 1.4632)]:
    E, e, C, S, P = scf(Z, zeta, R)
    print(f'{nama}: E = {E:.6f} hartree, energi orbital = {np.round(e, 4)}')
```

Keluarannya:

```
H2: E = -1.116714 hartree, energi orbital = [-0.5782  0.6703]
HeH+: E = -2.841837 hartree, energi orbital = [-1.6328 -0.1725]
```

Tebakan awal $\mathbf P = 0$ berarti matriks Fock pertama sama dengan $\mathbf H^\text{inti}$. Nilai $\zeta = 1{,}24$ untuk H dan $1{,}69$ untuk He adalah faktor skala baku basis STO-3G. Program untuk molekul sembarang dengan fungsi p dan d (program pendamping `kq.py` di folder kode bab ini) memakai prosedur yang sama persis; yang bertambah hanya rumus integralnya.


::: {.contoh}
**Contoh 17.8 · H₂ dengan tangan**

Untuk H₂ dalam basis STO-3G pada $R = 1{,}4$ bohr, integral basis atom adalah $S_{12} = 0{,}6593$, $H^\text{inti}_{11} = -1{,}1204$, $H^\text{inti}_{12} = -0{,}9584$, $(11|11) = 0{,}7746$, $(11|22) = 0{,}5697$, $(12|12) = 0{,}2970$, $(11|12) = 0{,}4441$ (dalam $E_h$). Simetri menetapkan $\sigma_g = (\phi_1 + \phi_2)/\sqrt{2(1 + S_{12})}$ tanpa perlu iterasi. Hitung koefisien, matriks kerapatan, matriks Fock, dan energi orbital.

**Penyelesaian.** $C_{11} = C_{21} = 1/\sqrt{2(1{,}6593)} = 0{,}5489$. $P_{\mu\nu} = 2C_{\mu1}C_{\nu1} = 0{,}6027$ untuk semua $\mu, \nu$. Dari (17.12), dengan memakai kesetaraan integral:

$$
F_{11} = H_{11} + P_{11}\left[\tfrac12(11|11)\right] + P_{22}\left[(11|22) - \tfrac12(12|12)\right] + 2P_{12}\left[\tfrac12(11|12)\right] = -0{,}3655 ,
$$

$$
F_{12} = H_{12} + P_{12}\left[\tfrac32(12|12) - \tfrac12(11|22)\right] + (P_{11} + P_{22})\left[\tfrac12(11|12)\right] = -0{,}5939 .
$$

Untuk orbital simetri, $\varepsilon_{1,2} = (F_{11} \pm F_{12})/(1 \pm S_{12})$: $\varepsilon_1 = -0{,}9594/1{,}6593 = -0{,}5782$ dan $\varepsilon_2 = 0{,}2284/0{,}3407 = 0{,}6703\ E_h$.

**Memahami hasil.** Hasilnya sama dengan keluaran program. Unsur di luar diagonal $F_{12}$ negatif dan besar, hasil tumpang tindih yang besar: inilah "integral resonansi" yang menurunkan orbital ikatan dan menaikkan orbital antiikatan, versi swakonsisten dari $\beta$ dalam teori Hückel. Orbital antiikatan naik lebih banyak (+0,67) daripada orbital ikatan turun, karena penyebut $1 - S_{12}$ kecil.
:::

::: {.contoh}
**Contoh 17.9 · Berapa banyak integral?**

Hitung banyaknya integral dua elektron yang berbeda untuk $K = 7$ (H₂O/STO-3G), 25 (H₂O/6-31G**), 100, dan 1000 fungsi basis. Berapa memori yang diperlukan untuk menyimpan integral $K = 1000$ dalam presisi ganda (8 bita per angka)?

**Penyelesaian.** Banyaknya pasangan $(\mu\nu)$ dengan $\mu \geq \nu$ adalah $M = K(K + 1)/2$, dan banyaknya integral berbeda $M(M + 1)/2$. $K = 7$: $M = 28$, 406 integral. $K = 25$: 52 975. $K = 100$: $1{,}28 \times 10^7$. $K = 1000$: $1{,}25 \times 10^{11}$, yaitu sekitar 1,0 terabita.

**Memahami hasil.** Molekul obat berukuran sedang dengan basis yang baik mudah mencapai 1000 fungsi basis. Menyimpan semua integral tidak praktis, sehingga program menghitungnya ulang tiap siklus dan memanfaatkan kenyataan bahwa integral antara fungsi yang berjauhan sangat kecil. Untuk molekul besar, banyaknya integral yang berarti hanya tumbuh sekitar $K^2$, dan itulah mengapa HF dan DFT dapat dipakai untuk ratusan atom.
:::

::: {.contoh}
**Contoh 17.10 · Ion HeH⁺**

Program di atas memberi, untuk HeH⁺ ($R = 1{,}4632$ bohr), $E = -2{,}8418\ E_h$, orbital terisi $\psi_1 = 0{,}8766\,\phi_\text{He} + 0{,}2025\,\phi_\text{H}$, dan $S_{12} = 0{,}5368$. Hitung banyaknya elektron yang "dimiliki" He dan H menurut pembagian Mulliken (subbab 17.7), yaitu $N_\text{He} = P_{11} + P_{12}S_{12}$, dan muatan atomnya.

**Penyelesaian.** $P_{11} = 2(0{,}8766)^2 = 1{,}5369$, $P_{12} = 2(0{,}8766)(0{,}2025) = 0{,}3550$, $P_{22} = 2(0{,}2025)^2 = 0{,}0820$. $N_\text{He} = 1{,}5369 + 0{,}3550(0{,}5368) = 1{,}7275$; $N_\text{H} = 0{,}0820 + 0{,}1906 = 0{,}2725$. Muatan: He $+0{,}27$, H $+0{,}73$.

**Memahami hasil.** Muatan positif ion sebagian besar berada pada hidrogen: kedua elektron lebih suka mengelilingi inti helium yang bermuatan +2. Dari sudut pandang kimia, HeH⁺ adalah ion He yang mengikat proton, dan memang molekul ini, yang dianggap molekul pertama yang terbentuk di alam semesta, berdisosiasi menjadi He + H⁺, bukan He⁺ + H. Molekul ini akhirnya terdeteksi di ruang antarbintang pada tahun 2019, di nebula planeter NGC 7027.
:::

::: {.contoh}
**Contoh 17.11 · Jalannya iterasi SCF**

Untuk H₂O dengan basis STO-3G pada geometri percobaan ($r = 0{,}9572$ Å, $\angle = 104{,}52°$), energi total pada beberapa siklus pertama, dimulai dari tebakan Hcore, adalah $-73{,}232479$; $-74{,}945898$; $-74{,}962080$; $-74{,}962813$; …; energi akhir $-74{,}962928\ E_h$. Mengapa tebakan pertama begitu jauh? Berapa siklus diperlukan sampai energi berubah kurang dari $10^{-10}\ E_h$ dengan dan tanpa DIIS?

**Penyelesaian.** Tebakan Hcore mengabaikan seluruh tolakan antarelektron dalam pemilihan orbital, sehingga orbitalnya terlalu tertarik ke inti oksigen; energi pertama 1,73 $E_h$ terlalu tinggi. Satu siklus sudah memperbaiki sebagian besar galat (sisa 0,017 $E_h$), dan galat terus mengecil kira-kira dengan faktor tetap tiap siklus. Program pendamping memerlukan 15 siklus tanpa DIIS dan 7 siklus dengan DIIS untuk mencapai perubahan energi di bawah $10^{-10}\ E_h$ (Gambar 17.3); satu siklus tambahan diperlukan agar vektor galat $\mathbf F\mathbf P\mathbf S - \mathbf S\mathbf P\mathbf F$ juga di bawah $10^{-6}$.

**Memahami hasil.** Konvergensi linear (galat berkurang dengan faktor tetap) adalah ciri iterasi titik tetap. DIIS mempercepatnya hampir dua kali lipat untuk molekul kecil, dan sering menentukan konvergen tidaknya perhitungan untuk molekul dengan HOMO–LUMO yang berdekatan, misalnya kompleks logam transisi. Bila SCF tidak konvergen, kiat yang lazim adalah tebakan awal yang lebih baik, peredaman, atau penggeseran tingkat (*level shifting*).
:::

::: {.kuis}
**Kuis cepat 17.3**

Mengapa persamaan Roothaan memerlukan matriks $\mathbf S$, sedangkan persamaan Hückel sederhana tidak? Apa yang terjadi pada banyaknya orbital molekul bila himpunan basis diperbesar dari 7 ke 25 fungsi?
:::

## 17.4 Teorema Koopmans dan energi ionisasi

### Energi orbital sebagai energi ionisasi

Apa arti fisis energi orbital $\varepsilon_i$? Tjalling Koopmans (1934), yang kemudian menerima Hadiah Nobel Ekonomi, memberi jawabannya: bila elektron dikeluarkan dari orbital $\chi_i$ dan semua orbital lain dianggap **tidak berubah**, energi yang diperlukan adalah $-\varepsilon_i$:

$$
\text{EI}_i \approx -\varepsilon_i, \qquad \text{AE}_a \approx -\varepsilon_a , \qquad \text{(17.18)}
$$

dengan EI energi ionisasi dan AE afinitas elektron (penambahan elektron ke orbital virtual $\chi_a$).

::: {.dalam}
**Menurunkan teorema Koopmans**

Misalkan $^{N-1}\Psi_i$ adalah determinan yang diperoleh dari $\Psi_0$ dengan menghapus kolom $\chi_i$, tanpa mengubah orbital lain. Dari (17.3):

$$
E_0 = \sum_jh_{jj} + \tfrac12\sum_{j,k}(J_{jk} - K_{jk}), \qquad {}^{N-1}E_i = \sum_{j \neq i}h_{jj} + \tfrac12\sum_{j \neq i}\sum_{k \neq i}(J_{jk} - K_{jk}) .
$$

Selisihnya hanya memuat suku yang mengandung indeks $i$: $E_0 - {}^{N-1}E_i = h_{ii} + \tfrac12\sum_k(J_{ik} - K_{ik}) + \tfrac12\sum_j(J_{ji} - K_{ji}) = h_{ii} + \sum_k(J_{ik} - K_{ik}) = \varepsilon_i$ menurut (17.7). Jadi ${}^{N-1}E_i - E_0 = -\varepsilon_i$. Hasil ini memerlukan orbital kanonik; orbital terlokalisasi (subbab 17.8) tidak memenuhinya.
:::

### Dua galat yang saling meniadakan

Pendekatan "orbital beku" mengandung dua galat yang berlawanan arah:

1. **Relaksasi orbital**. Setelah ionisasi, elektron yang tersisa merasakan tolakan yang lebih kecil dan menyusut ke arah inti, sehingga energi kation turun. Akibatnya energi ionisasi sebenarnya lebih **kecil** daripada $-\varepsilon_i$.
2. **Korelasi**. Molekul netral mempunyai lebih banyak pasangan elektron dan karena itu lebih banyak energi korelasi daripada kation. HF tidak memuat korelasi, sehingga energi netral terlalu tinggi relatif terhadap kation, dan energi ionisasi sebenarnya lebih **besar**.

Untuk elektron valensi, kedua galat sebanding besarnya dan sebagian besar saling meniadakan, sehingga teorema Koopmans sering memberi energi ionisasi valensi dengan galat sekitar 1 eV. Untuk elektron inti (misalnya O 1s), relaksasi jauh lebih besar karena lubang di kulit dalam sangat mengubah perisai elektron valensi, dan $-\varepsilon$ terlalu besar sekitar 20 eV. Untuk afinitas elektron, kedua galat **searah**, dan energi orbital virtual juga sangat bergantung pada basis; teorema Koopmans praktis tidak berguna untuk AE.

Cara yang lebih baik adalah menghitung energi kation secara terpisah dengan orbitalnya sendiri, lalu mengambil selisih: metode **ΔSCF**. Ia memasukkan relaksasi tetapi tidak korelasi, sehingga cenderung memberi energi ionisasi yang terlalu kecil. Metode modern (ΔCCSD(T), teori fungsi Green, EOM-IP-CCSD) memasukkan keduanya dan mencapai ketelitian sekitar 0,1–0,2 eV.

### Orbital kanonik dan spektrum fotoelektron

Teorema Koopmans memberi arti fisis kepada orbital **kanonik**: setiap orbital kanonik terisi bersesuaian dengan satu pita dalam spektrum fotoelektron (subbab 15.11). Inilah bukti percobaan paling langsung bahwa gambaran orbital molekul delokalisasi bukan sekadar alat hitung. Metana mempunyai empat ikatan C–H yang setara, tetapi spektrum fotoelektronnya menunjukkan **dua** pita valensi, di sekitar 14 eV (berasal dari tiga orbital $t_2$ yang terdegenerasi) dan 23 eV (orbital $a_1$), bukan satu pita (subbab 12.13). Perhitungan HF/6-31G* memberi $-\varepsilon$ = 14,8 dan 25,7 eV. Gambaran empat ikatan lokal tetap sah untuk energi total dan rapat elektron (subbab 17.8); yang tidak sah adalah anggapan bahwa ionisasi mengeluarkan elektron dari satu ikatan tertentu.

::: {.contoh}
**Contoh 17.12 · Spektrum fotoelektron air**

Energi orbital H₂O dengan basis 6-31G** pada geometri percobaan adalah: $1a_1$ $-20{,}561$; $2a_1$ $-1{,}340$; $1b_2$ $-0{,}704$; $3a_1$ $-0{,}569$; $1b_1$ $-0{,}497\ E_h$. Energi ionisasi vertikal terukur: 539,9; 32,2; 18,5; 14,7; 12,6 eV. Bandingkan.

**Penyelesaian.** Kalikan dengan $-27{,}211$ eV/$E_h$:

| Orbital | $-\varepsilon$ (eV) | EI terukur (eV) | Selisih (eV) |
|---|---|---|---|
| $1b_1$ | 13,53 | 12,6 | +0,9 |
| $3a_1$ | 15,48 | 14,7 | +0,7 |
| $1b_2$ | 19,14 | 18,5 | +0,6 |
| $2a_1$ | 36,47 | 32,2 | +4,3 |
| $1a_1$ | 559,48 | 539,9 | +19,6 |

**Memahami hasil.** Urutan dan pola pita valensi diramalkan dengan benar, dengan galat kurang dari 1 eV. HOMO $1b_1$ adalah orbital p oksigen yang tegak lurus bidang molekul, praktis pasangan elektron bebas; galat terbesar ada pada elektron 1s oksigen, tempat relaksasi paling kuat. Pada pita $2a_1$, ionisasi juga memicu proses banyak elektron yang memecah pita, sehingga gambaran satu elektron mulai runtuh.
:::

::: {.contoh}
**Contoh 17.13 · Koopmans dibandingkan ΔSCF**

Dengan basis 6-31G**, energi H₂O adalah $-76{,}02316\ E_h$, dan energi UHF kation H₂O⁺ pada geometri yang sama $-75{,}62539\ E_h$ ($\langle\hat S^2\rangle = 0{,}756$). Hitung energi ionisasi pertama dengan ΔSCF dan bandingkan dengan Koopmans (13,53 eV) dan percobaan (12,62 eV).

**Penyelesaian.** $\Delta E = -75{,}62539 - (-76{,}02316) = 0{,}39777\ E_h = 10{,}82$ eV.

**Memahami hasil.** Koopmans terlalu besar 0,9 eV, ΔSCF terlalu kecil 1,8 eV. Selisih Koopmans–ΔSCF, 2,7 eV, adalah energi relaksasi; selisih ΔSCF–percobaan, 1,8 eV, adalah perbedaan energi korelasi antara molekul netral dan kation. Bahwa Koopmans "lebih baik" daripada ΔSCF adalah kebetulan yang menguntungkan dari peniadaan galat, bukan tanda bahwa pendekatannya lebih unggul.
:::

::: {.contoh}
**Contoh 17.14 · Ketika Koopmans salah urutan: N₂**

HF/6-31G* untuk N₂ ($r = 1{,}098$ Å) memberi energi orbital valensi $3\sigma_g$ $-0{,}630$, $1\pi_u$ $-0{,}612$, $2\sigma_u$ $-0{,}776\ E_h$. Spektrum fotoelektron menunjukkan pita pertama pada 15,58 eV (ion $X\,^2\Sigma_g^+$, lubang di $3\sigma_g$), kedua pada 16,93 eV ($A\,^2\Pi_u$), dan ketiga pada 18,75 eV ($B\,^2\Sigma_u^+$). Bandingkan.

**Penyelesaian.** Menurut Koopmans: $1\pi_u$ 16,65 eV, $3\sigma_g$ 17,14 eV, $2\sigma_u$ 21,12 eV. Koopmans meramalkan bahwa ionisasi pertama berasal dari orbital π, padahal percobaan menunjukkan σ.

**Memahami hasil.** Selisih energi kedua orbital teratas hanya 0,5 eV, lebih kecil daripada galat relaksasi dan korelasi yang berbeda untuk kedua lubang. Lubang di orbital $3\sigma_g$, yang terkonsentrasi di ujung-ujung molekul, mengalami relaksasi dan korelasi yang berbeda dari lubang di orbital π. Perhitungan ΔCCSD(T) memulihkan urutan yang benar. Urutan orbital $3\sigma_g$ dan $1\pi_u$ dalam N₂ terkait dengan pencampuran s–p (subbab 11.8), dan kasus ini mengingatkan bahwa urutan energi orbital HF tidak selalu sama dengan urutan keadaan ion.
:::

::: {.contoh}
**Contoh 17.15 · Helium: memisahkan relaksasi dan korelasi**

Untuk He, batas HF memberi $\varepsilon_{1s} = -0{,}91796$ dan $E_\text{HF} = -2{,}86168\ E_h$; ion He⁺ adalah sistem satu elektron dengan energi tepat $-2{,}00000\ E_h$; energi tepat He $-2{,}90372\ E_h$. Hitung energi ionisasi menurut Koopmans, ΔSCF, dan nilai tepat, lalu pisahkan sumbangan relaksasi dan korelasi.

**Penyelesaian.** Koopmans: $0{,}91796\ E_h = 24{,}98$ eV. ΔSCF: $-2{,}00000 - (-2{,}86168) = 0{,}86168\ E_h = 23{,}45$ eV. Tepat: $0{,}90372\ E_h = 24{,}59$ eV. Relaksasi = Koopmans − ΔSCF = 1,53 eV; korelasi = tepat − ΔSCF = 1,14 eV.

**Memahami hasil.** Helium adalah kasus bersih karena kation tidak mempunyai korelasi sama sekali dan HF-nya tepat. Relaksasi (1,53 eV) sedikit lebih besar daripada korelasi (1,14 eV), sehingga Koopmans hanya meleset 0,39 eV. Peniadaan galat ini, yang kebetulan tetapi sistematis untuk elektron valensi, adalah alasan teorema Koopmans tetap dipakai dalam penafsiran spektrum fotoelektron selama lebih dari delapan puluh tahun.
:::

::: {.kuis}
**Kuis cepat 17.4**

Mengapa teorema Koopmans memberi energi ionisasi inti yang terlalu besar sekitar 20 eV, sedangkan untuk elektron valensi galatnya hanya sekitar 1 eV? Mengapa teorema itu tidak berlaku untuk orbital terlokalisasi?
:::
