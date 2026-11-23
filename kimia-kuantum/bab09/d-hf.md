## 9.8 Metode Hartree–Fock untuk atom

### Gagasan medan swakonsisten

Untuk helium (subbab 8.3) dan litium (subbab 9.7), kita memilih bentuk orbital lebih dulu (eksponensial dengan satu parameter) lalu mengoptimumkan parameternya. Pertanyaan yang lebih ambisius: **bentuk orbital apa** yang memberi energi terendah untuk satu determinan Slater? Jawabannya adalah orbital **Hartree–Fock** (HF), dan energi yang diperolehnya, batas Hartree–Fock, adalah yang terbaik yang dapat dicapai dengan gambaran "setiap elektron menempati orbitalnya sendiri".

Hartree (1928) memulai dengan gagasan fisika yang sederhana. Setiap elektron bergerak dalam medan inti ditambah medan **rata-rata** semua elektron lain, yang dihitung dari kerapatan muatan orbital-orbital mereka. Tetapi orbital-orbital itu sendiri bergantung pada medan yang belum diketahui. Jalan keluarnya adalah iterasi: tebak orbital, hitung medan, selesaikan persamaan satu elektron untuk memperoleh orbital baru, hitung medan baru, dan ulangi sampai orbital yang keluar sama dengan orbital yang masuk. Keadaan akhir ini disebut **medan swakonsisten** (*self-consistent field*, SCF). Fock dan Slater (1930) menyempurnakan metode Hartree dengan memakai determinan Slater, sehingga antisimetri, dan karena itu pertukaran, ikut diperhitungkan.

### Energi satu determinan

Untuk determinan dengan spin-orbital ortonormal $\chi_1, \ldots, \chi_N$, aturan Condon–Slater (subbab 9.14) memberi

$$
E = \sum_{i=1}^Nh_i + \frac12\sum_{i=1}^N\sum_{j=1}^N\left(J_{ij} - K_{ij}\right) , \qquad \text{(9.25)}
$$

dengan $h_i = \langle\chi_i|\hat h|\chi_i\rangle$, $J_{ij}$ integral Coulomb antara kerapatan $|\chi_i|^2$ dan $|\chi_j|^2$, dan $K_{ij}$ integral pertukaran, yang nol bila $\chi_i$ dan $\chi_j$ berspin berlawanan. Faktor $\tfrac12$ mencegah setiap pasangan dihitung dua kali. Suku $i = j$ boleh dimasukkan karena $J_{ii} = K_{ii}$: tolakan elektron dengan dirinya sendiri dihapus tepat oleh pertukaran dengan dirinya sendiri. Untuk sistem **kulit tertutup** dengan $N/2$ orbital ruang $\phi_i$ yang masing-masing terisi dua elektron, (9.25) menjadi

$$
E = 2\sum_{i=1}^{N/2}h_i + \sum_{i=1}^{N/2}\sum_{j=1}^{N/2}\left(2J_{ij} - K_{ij}\right) . \qquad \text{(9.26)}
$$

Untuk helium ($N/2 = 1$), $E = 2h_{1s} + J_{1s1s}$; untuk berilium, $E = 2h_{1s} + 2h_{2s} + J_{1s1s} + J_{2s2s} + 4J_{1s2s} - 2K_{1s2s}$.

### Persamaan Hartree–Fock

Minimumkan (9.26) terhadap bentuk orbital, dengan syarat orbital tetap ortonormal (syarat ini dimasukkan dengan pengali Lagrange). Penurunan lengkapnya panjang tetapi tidak sulit; hasilnya adalah persamaan nilai eigen satu elektron untuk setiap orbital terisi:

$$
\hat F\phi_i = \varepsilon_i\phi_i , \qquad \hat F = \hat h + \sum_{j=1}^{N/2}\left(2\hat J_j - \hat K_j\right) . \qquad \text{(9.27)}
$$

$\hat F$ adalah **operator Fock**. Operator Coulomb dan pertukaran didefinisikan oleh aksinya pada sembarang fungsi $f$:

$$
\hat J_j f(1) = \left[\int\frac{|\phi_j(2)|^2}{r_{12}}\,d\tau_2\right]f(1) , \qquad \hat K_jf(1) = \left[\int\frac{\phi_j^*(2)f(2)}{r_{12}}\,d\tau_2\right]\phi_j(1) . \qquad \text{(9.28)}
$$

$\hat J_j$ hanya mengalikan dengan potensial listrik awan elektron $j$: inilah medan rata-rata Hartree. $\hat K_j$ jauh lebih aneh: ia "menukar" fungsi $f$ ke dalam integral dan mengembalikan $\phi_j$. Operator ini **tak lokal** (nilainya di titik 1 bergantung pada $f$ di seluruh ruang) dan tidak mempunyai padanan klasik. Ia muncul semata-mata dari antisimetri, dan efeknya menurunkan energi elektron dengan menjauhkannya dari elektron lain berspin sama (lubang Fermi).

Karena $\hat F$ bergantung pada orbital-orbital yang ingin dicari, (9.27) harus diselesaikan secara iteratif seperti diuraikan di atas. Untuk atom, orbital HF berbentuk $R_{n\ell}(r)Y_\ell^m(\theta, \phi)$, dan persamaan radialnya dapat diselesaikan numerik pada kisi (program HF numerik atom telah ada sejak 1930-an dengan kalkulator mekanik). Untuk molekul, orbital diuraikan dalam basis dan persamaan HF menjadi persamaan matriks Roothaan $\mathbf{FC} = \mathbf{SC\varepsilon}$ (subbab 17.3), persis bentuk masalah nilai eigen umum (8.25).

::: {.dalam}
**Lebih dalam: menurunkan persamaan Hartree–Fock**

Ambil orbital riil dan kulit tertutup. Kita ingin meminimumkan $E$ di (9.26) dengan syarat $\langle\phi_i|\phi_j\rangle = \delta_{ij}$. Syarat-syarat ini dimasukkan dengan pengali Lagrange $\varepsilon_{ji}$ (simetris), sehingga fungsi yang distasionerkan adalah

$$
\mathcal L = E - 2\sum_{i,j}\varepsilon_{ji}\left(\langle\phi_i|\phi_j\rangle - \delta_{ij}\right) .
$$

Ubah satu orbital sedikit, $\phi_k \to \phi_k + \delta\phi_k$, dan kumpulkan suku-suku orde pertama dalam $\delta\phi_k$.

*Bagian satu elektron.* $\phi_k$ muncul dua kali dalam $h_k = \langle\phi_k|\hat h|\phi_k\rangle$, dan $\hat h$ Hermitian, sehingga $\delta(2h_k) = 4\langle\delta\phi_k|\hat h|\phi_k\rangle$.

*Bagian dua elektron.* Dalam $\sum_{ij}2J_{ij}$, orbital $\phi_k$ muncul pada suku-suku dengan $i = k$ dan dengan $j = k$; dalam setiap $J_{kj}$ ia muncul dua kali (dalam $|\phi_k|^2$). Menjumlahkan semuanya memberi $8\sum_j\langle\delta\phi_k|\hat J_j|\phi_k\rangle$. Dengan cara yang sama, $\delta\sum_{ij}K_{ij} = 4\sum_j\langle\delta\phi_k|\hat K_j|\phi_k\rangle$, dengan operator $\hat J_j$ dan $\hat K_j$ dari (9.28). Jadi

$$
\delta E = 4\left\langle\delta\phi_k\left|\hat h + \sum_j\left(2\hat J_j - \hat K_j\right)\right|\phi_k\right\rangle = 4\langle\delta\phi_k|\hat F|\phi_k\rangle .
$$

*Bagian syarat.* $\delta\left(2\sum_{ij}\varepsilon_{ji}\langle\phi_i|\phi_j\rangle\right) = 4\sum_j\varepsilon_{jk}\langle\delta\phi_k|\phi_j\rangle$.

Syarat $\delta\mathcal L = 0$ untuk **setiap** $\delta\phi_k$ berarti fungsi di sebelah kanan $\langle\delta\phi_k|$ harus nol:

$$
\hat F\phi_k = \sum_j\varepsilon_{jk}\phi_j .
$$

Matriks $\varepsilon_{jk}$ simetris, sehingga dapat didiagonalkan dengan transformasi ortogonal di antara orbital-orbital terisi. Menurut subbab 9.6, transformasi seperti itu tidak mengubah determinan, dan karena itu juga tidak mengubah $\hat F$ (yang hanya bergantung pada kerapatan total). Dalam basis orbital yang mendiagonalkan $\varepsilon$, yaitu orbital **kanonik**, persamaannya menjadi persamaan nilai eigen (9.27), dan pengali Lagrange $\varepsilon_k$ ternyata adalah energi orbital. Orbital terlokalisasi (subbab 17.8) adalah pilihan lain dari transformasi yang sama, yang tidak mendiagonalkan $\varepsilon$ tetapi memberi orbital yang lebih dekat dengan gambar ikatan kimia.
:::

### Energi orbital dan energi total

Kalikan (9.27) dengan $\phi_i^*$ dan integralkan:

$$
\varepsilon_i = h_i + \sum_{j=1}^{N/2}\left(2J_{ij} - K_{ij}\right) . \qquad \text{(9.29)}
$$

Energi orbital adalah energi satu elektron di orbital $i$: energi kinetik dan tarikan inti, ditambah tolakan dengan **semua** elektron lain. Menjumlahkan $2\varepsilon_i$ atas semua orbital terisi menghitung setiap tolakan antarelektron **dua kali** (sekali dari sisi masing-masing elektron). Membandingkan dengan (9.26),

$$
E = \sum_{i=1}^{N/2}\left(\varepsilon_i + h_i\right) \ne 2\sum_{i=1}^{N/2}\varepsilon_i . \qquad \text{(9.30)}
$$

Energi total **bukan** jumlah energi orbital. Kesalahan ini mudah dibuat, dan penting diingat ketika membaca diagram tingkat energi orbital molekul: jumlah energi orbital terisi bukan energi molekul.

### Teorema Koopmans

Apa makna fisika $\varepsilon_i$? Bayangkan satu elektron dicabut dari orbital $i$, sedangkan semua orbital lain tidak berubah bentuk (pendekatan "orbital beku"). Dengan (9.25), selisih energi ion dan atom tepat sama dengan $-\varepsilon_i$:

$$
I_i \approx -\varepsilon_i . \qquad \text{(9.31)}
$$

Inilah **teorema Koopmans** (1934). Ia tidak eksak karena dua alasan yang arahnya berlawanan. Dalam ion yang sebenarnya, orbital-orbital lain mengerut karena perisai berkurang (**relaksasi**), yang menurunkan energi ion dan membuat $-\varepsilon_i$ terlalu besar. Di sisi lain, atom netral mempunyai lebih banyak elektron dan karena itu energi korelasi yang lebih besar daripada ion (subbab 9.10), yang membuat $-\varepsilon_i$ terlalu kecil. Untuk elektron valensi kedua galat itu sebagian saling menghapus, dan teorema Koopmans memberi energi ionisasi dengan galat sekitar 1–2 eV. Untuk elektron kulit dalam, relaksasi mendominasi dan galatnya puluhan eV. Teorema Koopmans adalah jembatan utama antara orbital teori dan spektrum fotoelektron (subbab 15.11).

::: {.inti}
**Metode Hartree–Fock**

- Orbital terbaik untuk satu determinan memenuhi $\hat F\phi_i = \varepsilon_i\phi_i$, dengan $\hat F = \hat h + \sum_j(2\hat J_j - \hat K_j)$, diselesaikan secara iteratif sampai swakonsisten.
- Energi orbital $\varepsilon_i = h_i + \sum_j(2J_{ij} - K_{ij})$; energi total $E = \sum_i(\varepsilon_i + h_i)$, bukan $\sum 2\varepsilon_i$.
- Teorema Koopmans: $I_i \approx -\varepsilon_i$ (orbital beku).
:::

::: {.contoh}
**Contoh 9.24 · SCF helium dengan Python**

Hitung energi Hartree–Fock helium dengan basis dua fungsi 1s, $e^{-\zeta r}$ dengan $\zeta = 1{,}45363$ dan $2{,}91093$. Untuk kulit tertutup dalam basis, matriks Fock adalah $F_{pq} = h_{pq} + \sum_{rs}P_{rs}\left[(pq|rs) - \tfrac12(pr|qs)\right]$, dengan $P_{rs} = 2c_rc_s$ matriks kerapatan dan $(pq|rs)$ integral tolakan dua elektron. Energinya $E = \tfrac12\sum_{pq}P_{pq}(h_{pq} + F_{pq})$.

**Penyelesaian.**

```python
import numpy as np
from scipy.linalg import eigh

z = np.array([1.45363, 2.91093])        # eksponen dua fungsi 1s
N = np.sqrt(z**3/np.pi)                 # normalisasi
NN = np.outer(N, N); a = z[:, None] + z[None, :]
S = NN*8*np.pi/a**3                     # tumpang tindih
T = NN*0.5*np.outer(z, z)*8*np.pi/a**3  # energi kinetik
V = -2*NN*4*np.pi/a**2                  # tarikan inti, Z = 2
h = T + V
J = lambda p, q: (32*np.pi**2*(p*p + 3*p*q + q*q)
                  /(p*p*q*q*(p + q)**3))
n = len(z); G = np.zeros((n, n, n, n))  # (pq|rs)
for p, q, r, s in np.ndindex(n, n, n, n):
    G[p, q, r, s] = N[p]*N[q]*N[r]*N[s]*J(z[p] + z[q],
                                          z[r] + z[s])

eps, C = eigh(h, S)                     # tebakan: tanpa tolakan
for it in range(1, 6):
    c = C[:, 0]; P = 2*np.outer(c, c)   # matriks kerapatan
    Jm = np.einsum('rs,pqrs->pq', P, G)
    Km = np.einsum('rs,prqs->pq', P, G)
    F = h + Jm - 0.5*Km                 # matriks Fock
    E = 0.5*np.sum(P*(h + F))
    eps, C = eigh(F, S)
    print(it, round(E, 7), round(eps[0], 5))
```

| Iterasi | $E$ ($E_h$) | $\varepsilon_{1s}$ ($E_h$) |
|---|---|---|
| 1 | $-2{,}776\,626$ | $-0{,}837\,69$ |
| 2 | $-2{,}861\,501$ | $-0{,}914\,70$ |
| 3 | $-2{,}861\,672$ | $-0{,}917\,78$ |
| 4 | $-2{,}861\,673$ | $-0{,}917\,93$ |
| 5 | $-2{,}861\,673$ | $-0{,}917\,94$ |

**Memahami hasil.** Dalam empat iterasi energi stabil sampai tujuh angka penting. Energinya $-2{,}861\,673\ E_h$, hanya $7 \times 10^{-6}\ E_h$ di atas batas Hartree–Fock yang eksak ($-2{,}861\,680$): dua fungsi basis yang dipilih baik sudah hampir sempurna untuk orbital 1s. Bandingkan dengan fungsi satu eksponen ($-2{,}8477$): fleksibilitas tambahan memberi $0{,}014\ E_h$, tetapi selisih $0{,}042\ E_h$ ke energi eksak tetap tidak tersentuh, karena itulah batas satu determinan. Tebakan awal (orbital tanpa tolakan) memberi energi iterasi pertama yang jauh terlalu tinggi; inilah sebabnya program kimia komputasi memakai tebakan awal yang lebih cerdas dan teknik percepatan konvergensi.
:::

::: {.contoh}
**Contoh 9.25 · Memeriksa hubungan energi orbital dan energi total**

Dari Contoh 9.24, $E = -2{,}86167\ E_h$ dan $\varepsilon_{1s} = -0{,}91794\ E_h$. (a) Hitung $h_{1s}$ dan $J_{1s1s}$ dengan (9.26) dan (9.29). (b) Hitung energi ionisasi menurut Koopmans dan bandingkan dengan 24,59 eV. (c) Apa yang terjadi bila energi helium "dihitung" sebagai $2\varepsilon_{1s}$?

**Penyelesaian.** (a) Untuk helium, $E = 2h + J$ dan $\varepsilon = h + J$, sehingga $h = E - \varepsilon = -1{,}94373\ E_h$ dan $J = \varepsilon - h = 1{,}02579\ E_h$.

(b) $-\varepsilon = 0{,}91794\ E_h = 24{,}98$ eV, terlalu tinggi 0,39 eV (1,6%).

(c) $2\varepsilon = -1{,}836\ E_h$, meleset lebih dari $1\ E_h$: tolakan $J$ dihitung dua kali.

**Memahami hasil.** Tolakan rata-rata $\langle 1/r_{12}\rangle_\text{HF} = 1{,}026\ E_h$ lebih kecil daripada pada orbital He⁺ ($1{,}25$) dan pada fungsi satu eksponen ($1{,}055$), karena orbital HF lebih menyebar; fungsi gelombang eksak menurunkannya lagi menjadi 0,946, karena korelasi membuat elektron saling menghindar (subbab 9.10). Galat Koopmans 0,39 eV adalah selisih dua galat yang lebih besar. Bila orbital ion dibiarkan menyesuaikan diri, energi ionisasinya $E(\text{He}^+) - E_\text{HF}(\text{He}) = -2 + 2{,}86167 = 0{,}86167\ E_h = 23{,}45$ eV: relaksasi menurunkan 1,53 eV. Energi korelasi atom netral ($0{,}042\ E_h = 1{,}14$ eV, sedangkan He⁺ yang berelektron satu tidak mempunyai korelasi) menaikkannya kembali ke nilai eksak 24,59 eV. Kedua galat saling menghapus sebagian, $1{,}53 - 1{,}14 = 0{,}39$ eV, dan itulah sebabnya teorema Koopmans bekerja cukup baik untuk elektron valensi.
:::

::: {.contoh}
**Contoh 9.26 · Neon: energi orbital dan spektrum fotoelektron**

Energi orbital Hartree–Fock neon adalah $\varepsilon_{1s} = -32{,}772$, $\varepsilon_{2s} = -1{,}930$, $\varepsilon_{2p} = -0{,}850\ E_h$. Energi ionisasi terukur (spektroskopi fotoelektron sinar-X dan UV): 870,3; 48,5; 21,6 eV. (a) Bandingkan menurut teorema Koopmans. (b) Hitung $2\sum\varepsilon_i$ dan bandingkan dengan energi HF total $-128{,}547\ E_h$.

**Penyelesaian.** (a)

| Orbital | $-\varepsilon$ (eV) | terukur (eV) | selisih (eV) |
|---|---|---|---|
| 1s | 891,8 | 870,3 | 21,5 |
| 2s | 52,5 | 48,5 | 4,1 |
| 2p | 23,1 | 21,6 | 1,6 |

(b) $2(-32{,}772) + 2(-1{,}930) + 6(-0{,}850) = -74{,}51\ E_h$, jauh di atas $-128{,}55\ E_h$.

**Memahami hasil.** Teorema Koopmans menghasilkan urutan dan orde besaran yang benar untuk ketiga kulit, sehingga spektrum fotoelektron neon dapat dipahami sebagai "peta" energi orbitalnya. Galatnya terbesar untuk 1s: ketika elektron 1s dicabut, kedelapan elektron kulit L tiba-tiba merasakan inti yang hampir satu muatan lebih besar dan mengerut dengan kuat, melepaskan sekitar 20 eV energi relaksasi. Dalam spektroskopi fotoelektron sinar-X (XPS), energi ikat elektron kulit dalam bergeser beberapa eV menurut lingkungan kimia atom (misalnya C 1s pada C–H, C–O, dan C=O), dan pergeseran itulah yang dipakai untuk analisis permukaan; perhitungan yang baik untuk pergeseran ini harus menyertakan relaksasi.
:::

::: {.contoh}
**Contoh 9.27 · Pemecahan multiplet pada ionisasi kulit dalam**

Dalam determinan litium $|1s\alpha\,1s\beta\,2s\alpha|$, kedua elektron 1s tidak setara: hanya $1s\alpha$ yang berinteraksi pertukaran dengan elektron $2s\alpha$. Dengan integral Contoh 9.21 ($h_{1s} = -4{,}4508$, $J_{1s1s} = 1{,}6790$, $J_{1s2s} = 0{,}3180$, $K_{1s2s} = 0{,}0125\ E_h$): (a) hitung energi orbital $1s\beta$ dan $1s\alpha$; (b) jelaskan mengapa spektrum fotoelektron 1s litium memperlihatkan dua puncak.

**Penyelesaian.** (a) $\varepsilon_{1s\beta} = h_{1s} + J_{1s1s} + J_{1s2s} = -2{,}4538\ E_h$; $\varepsilon_{1s\alpha} = \varepsilon_{1s\beta} - K_{1s2s} = -2{,}4663\ E_h$. Selisihnya 0,34 eV.

(b) Setelah satu elektron 1s dicabut, ion Li⁺ mempunyai konfigurasi 1s2s, yang dapat berupa $^3$S atau $^1$S (subbab 9.4). Kedua keadaan ion itu berbeda energi $2K_{1s2s}$ (dengan orbital beku), sehingga energi ikat 1s yang teramati juga terpecah menjadi dua, dengan perbandingan intensitas kira-kira 3 : 1 sesuai bobot spin.

**Memahami hasil.** Pada atom dan molekul berkulit terbuka, ionisasi elektron kulit dalam menghasilkan **pemecahan multiplet** dalam spektrum XPS. Molekul O₂, yang paramagnetik dengan dua elektron tak berpasangan, memperlihatkan dua puncak O 1s yang terpisah sekitar 1,1 eV dengan perbandingan intensitas 2 : 1, sedangkan N₂ yang berkulit tertutup hanya satu. Pemecahan semacam ini adalah tanda khas elektron tak berpasangan, dan dipakai untuk mengenali ion logam transisi paramagnetik dalam spektrum XPS bahan.
:::

::: {.kuis}
**Kuis cepat 9.8**

(a) Mengapa operator pertukaran tidak muncul dalam metode Hartree yang asli? (b) Mengapa energi total tidak sama dengan jumlah energi orbital terisi? (c) Untuk elektron kulit dalam, apakah teorema Koopmans cenderung melebih-lebihkan atau mengurangi energi ionisasi, dan mengapa?
:::

## 9.9 Orbital dan tabel periodik

### Pendekatan medan sentral

Potensial yang dirasakan satu elektron dalam atom HF tidak tepat bersimetri bola untuk kulit terbuka, tetapi rata-rata bolanya adalah pendekatan yang sangat baik. Dalam **pendekatan medan sentral**, setiap elektron bergerak dalam potensial $V(r)$ yang hanya bergantung pada jarak dari inti. Momentum sudut tetap kekal (subbab 6.1), sehingga orbital-orbital tetap berbentuk $R_{n\ell}(r)Y_\ell^m$ dengan label $n\ell$ yang sama seperti hidrogen. Bedanya, $V(r)$ bukan $-Z/r$: di dekat inti elektron merasakan $-Z/r$ penuh, di jauh hanya $-1/r$ (inti dikurangi $Z - 1$ elektron lain). Potensial seperti ini memecah degenerasi $\ell$ yang khas atom hidrogen.

Orbital dengan $\ell$ kecil mempunyai lebih banyak simpul radial dan lebih banyak kerapatan di dekat inti: orbital ns mempunyai puncak-puncak kecil di dalam kulit-kulit dalam (Gambar 9.3). Di sana, perisainya lemah dan tarikan inti kuat. Karena itu, untuk $n$ yang sama,

$$
\varepsilon_{ns} < \varepsilon_{np} < \varepsilon_{nd} < \varepsilon_{nf} . \qquad \text{(9.32)}
$$

Efek penetrasi bisa begitu besar sehingga orbital dengan $n$ lebih besar tetapi $\ell$ lebih kecil turun di bawah orbital dengan $n$ lebih kecil dan $\ell$ lebih besar: 4s di bawah 3d pada kalium, 5s di bawah 4d pada rubidium, 6s dan bahkan 5d di bawah 4f pada sesium dan barium.

![Gambar 9.3 Fungsi distribusi radial $r^2R^2$ orbital 3s, 3p, dan 3d atom hidrogen. Ketiganya mempunyai energi sama dalam hidrogen, tetapi 3s mempunyai dua puncak kecil di dekat inti dan 3p satu, sedangkan 3d tidak mempunyai. Arsiran menandai daerah kira-kira tempat kulit dalam ($n = 1$ dan 2) sebuah atom berelektron banyak; elektron yang menembus daerah ini kurang terperisai dan lebih terikat.](fig/c_penetrasi.png){width=78%}

### Prinsip Aufbau dan urutan pengisian

Konfigurasi keadaan dasar atom diperoleh dengan mengisi orbital dari energi terendah, dua elektron per orbital (asas Pauli). Urutan empirisnya, yang sesuai dengan sebagian besar unsur, mengikuti **aturan Madelung**: urutkan menurut $n + \ell$ naik, dan untuk $n + \ell$ yang sama, menurut $n$ naik:

$$
1s < 2s < 2p < 3s < 3p < 4s < 3d < 4p < 5s < 4d < 5p < 6s < 4f < 5d < 6p < 7s < 5f < 6d < 7p .
$$

Dari urutan ini dan kapasitas subkulit (9.20), panjang periode langsung terbaca: periode 1 (1s) 2 unsur; periode 2 (2s, 2p) dan periode 3 (3s, 3p) masing-masing 8; periode 4 (4s, 3d, 4p) dan periode 5 (5s, 4d, 5p) masing-masing 18; periode 6 (6s, 4f, 5d, 6p) dan 7 masing-masing 32. Jawaban atas teka-teki "2, 8, 8, 18, 18, 32" adalah: asas Pauli menentukan kapasitas, penetrasi menentukan urutan.

### Logam transisi: 4s lebih dulu masuk, lebih dulu keluar

Pada kalium dan kalsium, 4s jelas lebih rendah daripada 3d (Contoh 9.28). Tetapi energi orbital 3d turun jauh lebih cepat daripada 4s ketika $Z$ bertambah, karena elektron 3d kurang terperisai oleh elektron 4s yang lebih luar. Sejak skandium, energi orbital 3d sebenarnya sudah di bawah 4s. Mengapa unsur-unsur itu tetap mempunyai konfigurasi $3d^n4s^2$, bukan $3d^{n+2}$? Karena yang menentukan konfigurasi adalah energi **total**, termasuk tolakan antarelektron: orbital 3d kompak, sehingga menambahkan elektron ke sana menaikkan tolakan jauh lebih banyak daripada menambahkannya ke 4s yang luas. Ketika atom diionisasi, muatan bersih memperkuat tarikan inti dan memperkecil peran tolakan, sehingga 3d menjadi jelas lebih stabil. Akibatnya, ion logam transisi kehilangan elektron 4s lebih dulu: Fe ($[\text{Ar}]3d^6 4s^2$) menjadi Fe²⁺ ($[\text{Ar}]3d^6$), bukan $[\text{Ar}]3d^4 4s^2$. Seluruh kimia koordinasi (Bab 14) bekerja dengan konfigurasi $d^n$ ion seperti ini.

Beberapa pengecualian aturan Madelung, misalnya Cr ($3d^5 4s^1$) dan Cu ($3d^{10}4s^1$), muncul karena selisih energi konfigurasi sangat kecil, dan stabilisasi pertukaran subkulit setengah penuh atau penuh (Contoh 9.31) cukup untuk membalik urutan.

### Muatan inti efektif dan aturan Slater

Slater (1930) merumuskan aturan sederhana untuk menaksir tetapan perisai $\sigma$, sehingga $Z_\text{ef} = Z - \sigma$ untuk elektron di orbital tertentu. Kelompokkan orbital: (1s), (2s, 2p), (3s, 3p), (3d), (4s, 4p), (4d), .... Untuk elektron s atau p:

- elektron dalam kelompok yang sama menyumbang 0,35 masing-masing (0,30 untuk 1s);
- elektron di kulit $n - 1$ menyumbang 0,85 masing-masing;
- elektron di kulit $n - 2$ dan lebih dalam menyumbang 1,00 masing-masing.

Untuk elektron d atau f, kelompok sendiri 0,35 dan semua elektron di sebelah kiri 1,00. Aturan ini kasar, tetapi menangkap kecenderungan utama: sepanjang periode 2, $Z_\text{ef}$ elektron valensi naik dari 1,30 (Li) ke 1,95, 2,60, 3,25, 3,90, 4,55, 5,20, dan 5,85 (Ne), sehingga jari-jari atom mengecil dan energi ionisasi naik. Pada awal periode baru, $Z_\text{ef}$ anjlok kembali, dan energi ionisasi pun anjlok (Gambar 9.4).

![Gambar 9.4 Energi ionisasi pertama unsur $Z = 1$ sampai 36. Puncak pada gas mulia dan lembah pada logam alkali menandai kulit-kulit; lekukan kecil pada B, O, Al, S, dan Ga dijelaskan oleh penetrasi (B, Al, Ga: elektron p pertama) dan oleh tolakan pasangan elektron (O, S: elektron p keempat). Di deret logam transisi energi ionisasi hampir datar, karena elektron yang dilepas adalah 4s, yang terperisai hampir sempurna oleh elektron 3d yang bertambah.](fig/c_ionisasi.png){width=92%}

::: {.contoh}
**Contoh 9.28 · Mengapa kalium mengisi 4s, bukan 3d**

Dengan aturan Slater, hitung $Z_\text{ef}$ untuk elektron valensi kalium ($Z = 19$) bila ia berada di 4s dan bila di 3d. Taksir energinya dengan $-\tfrac12(Z_\text{ef}/n^*)^2$, memakai bilangan kuantum efektif Slater $n^* = 3{,}7$ untuk $n = 4$. Bandingkan dengan data: energi ionisasi K 4,34 eV, dan keadaan $3d$ kalium berada 2,67 eV di atas keadaan dasar.

**Penyelesaian.** 4s: elektron $n = 3$ (8 elektron) masing-masing 0,85, elektron $n \le 2$ (10 elektron) masing-masing 1,00. $\sigma = 6{,}80 + 10{,}00 = 16{,}80$, $Z_\text{ef} = 2{,}20$, energi $-\tfrac12(2{,}20/3{,}7)^2 = -0{,}177\ E_h = -4{,}81$ eV. 3d: semua 18 elektron teras menyumbang 1,00, $Z_\text{ef} = 1{,}00$, energi $-\tfrac12(1/3)^2 = -0{,}056\ E_h = -1{,}51$ eV. Data: 4s terikat 4,34 eV, 3d terikat $4{,}34 - 2{,}67 = 1{,}67$ eV.

**Memahami hasil.** Elektron 3d kalium sama sekali tidak menembus teras argon dan merasakan muatan +1 saja, seperti elektron hidrogen di $n = 3$ (1,51 eV). Elektron 4s menembus jauh ke dalam teras dan merasakan muatan efektif lebih dari dua. Aturan Slater, walaupun kasar, menangkap selisih ini dengan baik. Sepuluh unsur kemudian, pada seng, muatan inti 30 dan elektron 3d sudah menjadi bagian teras yang kompak.
:::

::: {.contoh}
**Contoh 9.29 · Garis D natrium: menjawab janji Bab 1**

Di subbab 1.10 kita bertanya mengapa selisih 3p − 3s natrium 2,10 eV, bukan 10,2 eV seperti 2p − 1s hidrogen dan bukan nol seperti 3p − 3s hidrogen. Energi ionisasi natrium 5,139 eV dan garis D rata-rata 589,3 nm. (a) Hitung cacat kuantum $\delta_s$ dan $\delta_p$. (b) Tafsirkan dengan penetrasi.

**Penyelesaian.** (a) 3s: $E = -5{,}139\ \text{eV} = -0{,}18886\ E_h$, $n^* = 1/\sqrt{2(0{,}18886)} = 1{,}627$, $\delta_s = 3 - 1{,}627 = 1{,}373$. Foton D: $1239{,}84/589{,}3 = 2{,}104$ eV, sehingga $E_{3p} = -3{,}035\ \text{eV} = -0{,}11154\ E_h$, $n^* = 2{,}117$, $\delta_p = 0{,}883$.

(b) Tanpa penetrasi, elektron valensi natrium akan seperti elektron hidrogen di $n = 3$, dengan energi $-1{,}51$ eV untuk 3s dan 3p. Elektron 3s, yang mempunyai dua puncak kecil di dalam teras neon, terikat lebih dari tiga kali lebih kuat (5,14 eV). Elektron 3p menembus lebih sedikit (3,04 eV). Selisihnya, 2,10 eV, adalah ukuran perbedaan penetrasi s dan p.

**Memahami hasil.** Warna kuning lampu jalan natrium dan nyala natrium dengan demikian adalah "warna penetrasi". Cacat kuantum natrium (1,37 dan 0,88) jauh lebih besar daripada litium (0,41 dan 0,04, Contoh 9.23), karena teras natrium lebih besar dan berisi elektron p yang ikut ditembus. Garis D sendiri kembar (589,0 dan 589,6 nm) karena kopling spin–orbit pada keadaan 3p (subbab 9.13).
:::

::: {.contoh}
**Contoh 9.30 · Lekukan energi ionisasi: Be → B dan N → O**

Energi ionisasi pertama: Be 9,32; B 8,30; C 11,26; N 14,53; O 13,62 eV. Jelaskan kedua penurunan, padahal $Z_\text{ef}$ terus naik sepanjang periode.

**Penyelesaian.** **Be → B**: elektron yang dilepas berilium berasal dari 2s; boron melepas elektron 2p yang pertama. Orbital 2p menembus lebih sedikit daripada 2s, sehingga lebih mudah dilepas walaupun $Z$ lebih besar.

**N → O**: nitrogen ($2p^3$) mempunyai tiga elektron p di tiga orbital berbeda dengan spin sejajar (aturan Hund). Oksigen ($2p^4$) harus menempatkan elektron keempat di orbital yang sudah terisi, dengan spin berlawanan. Elektron itu (i) mengalami tolakan Coulomb yang besar dari pasangannya di orbital yang sama, dan (ii) tidak memperoleh stabilisasi pertukaran dengan tiga elektron lain, karena spinnya berlawanan. Melepaskannya mudah. Sebaliknya, melepaskan satu elektron dari nitrogen menghilangkan dua pasangan pertukaran sejajar.

**Memahami hasil.** Pola yang sama muncul di periode 3 (Mg → Al dan P → S) dan periode 4 (Zn → Ga dan As → Se), sehingga ia bukan kebetulan melainkan sifat kulit s dan p. Kedua efek ini, penetrasi dan pertukaran, juga menjelaskan mengapa afinitas elektron nitrogen hampir nol sedangkan karbon dan oksigen jelas positif: elektron tambahan pada nitrogen harus berpasangan.
:::

::: {.contoh}
**Contoh 9.31 · Kromium dan stabilisasi pertukaran**

Bandingkan konfigurasi $3d^4 4s^2$ dan $3d^5 4s^1$ kromium. (a) Dalam masing-masing, berapa elektron yang berspin sejajar (aturan Hund) dan berapa pasangan pertukaran sejajar $\binom{n}{2}$ di antara mereka? (b) Mengapa hal ini dapat membalik urutan energi?

**Penyelesaian.** (a) $3d^4 4s^2$: empat elektron d sejajar ditambah satu elektron 4s searah (yang lain berlawanan): 5 elektron sejajar, $\binom52 = 10$ pasangan. $3d^5 4s^1$: lima elektron d dan satu 4s semuanya sejajar: 6 elektron, $\binom62 = 15$ pasangan.

(b) Setiap pasangan sejajar menyumbang $-K$ (integral pertukaran, beberapa puluh kJ/mol untuk orbital 3d). Lima pasangan tambahan, ditambah berkurangnya tolakan pasangan di 4s, cukup untuk mengalahkan selisih kecil energi orbital 3d dan 4s.

**Memahami hasil.** Penjelasan "subkulit setengah penuh itu stabil" sebenarnya adalah penjelasan pertukaran: elektron berspin sejajar saling menghindar karena antisimetri, dan tolakan yang dihindari itu muncul sebagai integral $K$. Untuk Cu ($3d^{10}4s^1$ lawan $3d^9 4s^2$), alasannya serupa, ditambah kontraksi kuat orbital 3d menjelang akhir deret. Pengecualian Aufbau di deret 4d dan 5d (misalnya Pd $4d^{10}5s^0$, Pt $5d^9 6s^1$) menunjukkan bahwa ketika selisih energi konfigurasi hanya puluhan kJ/mol, setiap efek kecil, termasuk relativitas, dapat menentukan pemenangnya.
:::

::: {.contoh}
**Contoh 9.32 · Kontraksi lantanida**

Jari-jari logam zirkonium ($Z = 40$, periode 5) adalah 160 pm, dan hafnium ($Z = 72$, periode 6) 159 pm, hampir sama, padahal hafnium mempunyai satu kulit elektron lebih banyak. Jari-jari ion La³⁺ 103 pm dan Lu³⁺ 86 pm (bilangan koordinasi 6). Jelaskan.

**Penyelesaian.** Di antara La dan Hf, empat belas elektron mengisi subkulit 4f. Orbital 4f kompak dan berbentuk sedemikian sehingga memerisai elektron 5s, 5p, 6s, dan 5d di luarnya dengan buruk (jauh lebih buruk daripada asumsi 1,00 aturan Slater). Setiap kali $Z$ naik satu, muatan inti efektif yang dirasakan elektron luar bertambah hampir satu, sehingga sepanjang deret lantanida ion-ionnya mengerut sekitar 17 pm. Ketika deret 5d dimulai pada Hf, kontraksi ini hampir tepat menghapus pertambahan ukuran karena kulit baru. Efek relativistik (subbab 9.13 dan Contoh 8.31) menyumbang sebagian kecil tambahan.

**Memahami hasil.** Kontraksi lantanida membuat unsur-unsur 5d sangat mirip dengan pasangan 4d-nya: Zr dan Hf hampir tidak dapat dipisahkan secara kimia (keduanya selalu ditemukan bersama dalam mineral), dan pasangan Nb–Ta, Mo–W juga sangat mirip. Pengerutan bertahap ion Ln³⁺ sepanjang deret juga dimanfaatkan untuk memisahkan unsur-unsur tanah jarang dengan kromatografi penukar ion, karena kekuatan ikatan dengan ligan bergantung pada ukuran ion.
:::

::: {.kuis}
**Kuis cepat 9.9**

(a) Tuliskan konfigurasi Fe³⁺ dan hitung jumlah elektron tak berpasangan. (b) Mengapa unsur periode 4 berjumlah 18, bukan 8 atau 32? (c) Dengan aturan Slater, berapa $Z_\text{ef}$ elektron 2p fluor?
:::

