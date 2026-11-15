## 9.6 Determinan Slater

### Membuat fungsi yang antisimetris

Untuk dua elektron, kita dapat menulis kombinasi antisimetris dengan tangan. Untuk tiga elektron atau lebih, diperlukan cara yang sistematis. Misalkan $N$ elektron menempati $N$ spin-orbital ortonormal $\chi_1, \chi_2, \ldots, \chi_N$. Hasil kali sederhana $\chi_1(1)\chi_2(2)\cdots\chi_N(N)$ (disebut **hasil kali Hartree**) tidak antisimetris: menukar elektron 1 dan 2 menghasilkan fungsi yang berbeda. Agar antisimetris, kita harus menjumlahkan semua $N!$ cara menugaskan elektron ke spin-orbital, masing-masing dengan tanda $+$ untuk permutasi genap dan $-$ untuk permutasi ganjil. Jumlah bertanda semacam itu tidak lain adalah sebuah **determinan** (subbab 2.7). Slater (1929) menuliskannya:

$$
\Psi(1, 2, \ldots, N) = \frac{1}{\sqrt{N!}}\begin{vmatrix} \chi_1(1) & \chi_2(1) & \cdots & \chi_N(1)\\ \chi_1(2) & \chi_2(2) & \cdots & \chi_N(2)\\ \vdots & \vdots & \ddots & \vdots\\ \chi_1(N) & \chi_2(N) & \cdots & \chi_N(N)\end{vmatrix} . \qquad \text{(9.22)}
$$

Setiap **baris** berisi satu elektron, setiap **kolom** berisi satu spin-orbital. Faktor $1/\sqrt{N!}$ menormalisasi fungsi bila spin-orbitalnya ortonormal: dari $N!$ suku, setiap suku ternormalisasi dan semua suku saling ortogonal.

Sifat-sifat determinan yang sudah kita kenal langsung menjadi sifat fisika:

1. **Antisimetri.** Menukar dua elektron berarti menukar dua baris, dan determinan berubah tanda.
2. **Asas Pauli.** Bila dua spin-orbital sama, dua kolom sama, dan determinan nol.
3. **Kebebasan memilih orbital.** Menambahkan kelipatan satu kolom ke kolom lain tidak mengubah determinan. Akibatnya, setiap transformasi linear (uniter) di antara spin-orbital yang terisi menghasilkan fungsi gelombang yang sama (paling banyak berbeda faktor fase). Orbital-orbital yang terisi tidak unik; yang unik hanyalah ruang yang dibentuknya. Inilah alasan matematis mengapa orbital molekul terdelokalisasi dan orbital ikatan terlokalisasi (atau hibrida) memberikan fungsi gelombang total yang sama (subbab 12.13 dan 17.8).

Notasi ringkas determinan hanya mencantumkan diagonalnya: $|\chi_1\chi_2\cdots\chi_N|$, misalnya $|1s\alpha\,1s\beta\,2s\alpha|$ untuk litium. Kadang-kadang garis di atas lambang menandai spin $\beta$: $|1s\,\overline{1s}\,2s|$.

### Helium sebagai determinan

Untuk keadaan dasar helium:

$$
|1s\alpha\,1s\beta| = \frac{1}{\sqrt2}\begin{vmatrix} 1s(1)\alpha(1) & 1s(1)\beta(1)\\ 1s(2)\alpha(2) & 1s(2)\beta(2)\end{vmatrix} = 1s(1)1s(2)\cdot\frac{1}{\sqrt2}\left[\alpha(1)\beta(2) - \beta(1)\alpha(2)\right] ,
$$

tepat fungsi (9.18). Secara umum, determinan untuk **kulit tertutup** (setiap orbital ruang terisi $\alpha$ dan $\beta$) otomatis merupakan singlet murni dengan $S = 0$. Untuk kulit terbuka, satu determinan belum tentu fungsi eigen $\hat S^2$, dan kombinasi beberapa determinan diperlukan (Contoh 9.18).

### Determinan dalam praktik

Determinan $N \times N$ mempunyai $N!$ suku: 6 untuk litium, 720 untuk karbon, lebih dari tiga juta untuk neon, dan sekitar $4 \times 10^{26}$ untuk besi. Tidak ada yang menguraikannya. Semua perhitungan dengan determinan Slater memakai aturan-aturan umum untuk unsur matriks antara determinan (aturan Condon–Slater, subbab 9.14), yang mereduksi integral $3N$ dimensi menjadi jumlah integral satu dan dua elektron.

::: {.inti}
**Determinan Slater**

$$
\Psi = \frac{1}{\sqrt{N!}}\det\left[\chi_j(i)\right] = |\chi_1\chi_2\cdots\chi_N| .
$$

Baris = elektron, kolom = spin-orbital. Pertukaran dua elektron mengubah tanda; spin-orbital ganda membuat determinan nol; pencampuran orbital terisi di antara mereka sendiri tidak mengubah fungsi gelombang.
:::

::: {.contoh}
**Contoh 9.16 · Menguraikan determinan litium**

(a) Uraikan $|1s\alpha\,1s\beta\,2s\alpha|$ menjadi enam suku. Tulis $a = 1s\alpha$, $b = 1s\beta$, $c = 2s\alpha$. (b) Tunjukkan bahwa menukar elektron 1 dan 3 mengubah tandanya.

**Penyelesaian.** (a) Ekspansi kofaktor sepanjang baris pertama (subbab 2.7):

$$
\sqrt6\,\Psi = a(1)[b(2)c(3) - c(2)b(3)] - b(1)[a(2)c(3) - c(2)a(3)] + c(1)[a(2)b(3) - b(2)a(3)] .
$$

Enam suku: tiga bertanda $+$ ($a_1b_2c_3$, $b_1c_2a_3$, $c_1a_2b_3$, permutasi siklis) dan tiga bertanda $-$.

(b) Menukar label 1 dan 3 mengubah setiap suku $+$ menjadi suku $-$ dan sebaliknya; misalnya $a_1b_2c_3 \to a_3b_2c_1$, yang ada di daftar dengan tanda $-$. Jadi $\Psi(3, 2, 1) = -\Psi(1, 2, 3)$.

**Memahami hasil.** Setiap elektron muncul di setiap spin-orbital dalam sebagian suku: tidak ada yang dapat mengatakan bahwa "elektron 3 adalah elektron 2s". Yang bermakna hanyalah pernyataan bahwa salah satu elektron menempati 2s$\alpha$. Inilah bahasa yang benar untuk konfigurasi elektron $1s^22s^1$.
:::

::: {.contoh}
**Contoh 9.17 · Mencoba $1s^3$**

Tuliskan determinan untuk "konfigurasi" $1s^3$ litium dan tunjukkan bahwa ia nol.

**Penyelesaian.** Hanya ada dua spin-orbital 1s: $1s\alpha$ dan $1s\beta$. Elektron ketiga harus mengulang salah satunya, misalnya $|1s\alpha\,1s\beta\,1s\alpha|$. Kolom pertama dan ketiga sama, sehingga determinannya nol.

**Memahami hasil.** Determinan menegakkan asas Pauli secara otomatis: kita tidak perlu mengingat aturan apa pun, karena keadaan terlarang tidak ada sebagai fungsi. Elektron ketiga litium harus menempati orbital dengan $n = 2$, jauh lebih tinggi energinya. Itulah sebabnya litium, tidak seperti helium, mudah melepaskan satu elektron dan bersifat logam.
:::

::: {.contoh}
**Contoh 9.18 · Singlet dan triplet dari determinan**

Untuk konfigurasi 1s2s ($M_S = 0$) ada dua determinan, $D_1 = |1s\alpha\,2s\beta|$ dan $D_2 = |1s\beta\,2s\alpha|$. (a) Uraikan $D_1 - D_2$ dan $D_1 + D_2$. (b) Kombinasi mana yang singlet dan mana triplet?

**Penyelesaian.** (a) Tulis $a = 1s$, $b = 2s$ (fungsi ruang). $\sqrt2D_1 = a_1b_2\alpha_1\beta_2 - b_1a_2\beta_1\alpha_2$ dan $\sqrt2D_2 = a_1b_2\beta_1\alpha_2 - b_1a_2\alpha_1\beta_2$. Maka

$$
\sqrt2(D_1 - D_2) = (a_1b_2 + b_1a_2)(\alpha_1\beta_2 - \beta_1\alpha_2) , \qquad \sqrt2(D_1 + D_2) = (a_1b_2 - b_1a_2)(\alpha_1\beta_2 + \beta_1\alpha_2) .
$$

(b) $(D_1 - D_2)/\sqrt2$ = (ruang simetris) × (spin singlet): suku $^1$S. $(D_1 + D_2)/\sqrt2$ = (ruang antisimetris) × (triplet $M_S = 0$): komponen ketiga suku $^3$S, bersama $|1s\alpha\,2s\alpha|$ ($M_S = +1$) dan $|1s\beta\,2s\beta|$ ($M_S = -1$).

**Memahami hasil.** Satu determinan dengan spin berlawanan, $|1s\alpha\,2s\beta|$, adalah campuran 50 : 50 singlet dan triplet; ia bukan keadaan stasioner yang benar. Perhitungan Hartree–Fock "tak terbatas" (UHF) yang memakai satu determinan untuk radikal dan keadaan tereksitasi menderita **kontaminasi spin** semacam ini, yang harus diperiksa dengan menghitung $\langle S^2\rangle$. Program kimia komputasi selalu melaporkan nilai ini; untuk singlet murni seharusnya 0, untuk doblet 0,75, untuk triplet 2.
:::

::: {.contoh}
**Contoh 9.19 · Orbital terisi dapat dicampur**

Untuk berilium $|1s\alpha\,1s\beta\,2s\alpha\,2s\beta|$, ganti 1s dan 2s dengan $h_\pm = (1s \pm 2s)/\sqrt2$. Tunjukkan bahwa determinan baru sama dengan determinan lama (sampai tanda).

**Penyelesaian.** Kolom-kolom spin $\alpha$ berubah dari $(1s\alpha, 2s\alpha)$ menjadi $(h_+\alpha, h_-\alpha) = (1s\alpha, 2s\alpha)\,\mathbf U$, dengan $\mathbf U = \tfrac{1}{\sqrt2}\begin{pmatrix}1 & 1\\ 1 & -1\end{pmatrix}$; hal yang sama untuk kolom $\beta$. Determinan hasil kali sama dengan hasil kali determinan (subbab 2.7), dan $\det\mathbf U = -1$. Jadi determinan baru $= (-1)(-1)$ × determinan lama = determinan lama.

**Memahami hasil.** Orbital $h_\pm$ tampak sangat berbeda dari 1s dan 2s (yang satu besar di dalam dan di luar, yang lain mempunyai bentuk lain), tetapi kerapatan elektron, energi, dan setiap sifat lain atom berilium tidak berubah sedikit pun. Dalam molekul, kebebasan yang sama memungkinkan kita memilih orbital molekul kanonik (terdelokalisasi, energinya terdefinisi) atau orbital ikatan terlokalisasi (sesuai gambar Lewis). Keduanya sah; pertanyaannya hanya mana yang lebih berguna untuk sifat tertentu.
:::

::: {.contoh}
**Contoh 9.20 · Kontaminasi spin satu determinan**

(a) Dengan hasil Contoh 9.18, hitung $\langle S^2\rangle$ untuk determinan $D_1 = |1s\alpha\,2s\beta|$. (b) Perhitungan HF tak terbatas (UHF) untuk radikal metil, yang seharusnya doblet murni, melaporkan $\langle S^2\rangle = 0{,}762\hbar^2$. Berapa nilai idealnya, dan apa artinya selisih itu?

**Penyelesaian.** (a) Dari Contoh 9.18, $D_1 = (\Psi_\text{triplet} + \Psi_\text{singlet})/\sqrt2$. Karena $\hat S^2$ bernilai $2\hbar^2$ pada triplet dan 0 pada singlet, dan keduanya ortogonal, $\langle S^2\rangle = \tfrac12(2\hbar^2) + \tfrac12(0) = 1\hbar^2$.

(b) Doblet murni: $S(S + 1) = \tfrac12\cdot\tfrac32 = 0{,}75\hbar^2$. Selisih $0{,}012\hbar^2$ menunjukkan campuran kecil keadaan kuartet ($S = \tfrac32$, $S(S+1) = 3{,}75\hbar^2$), sekitar $0{,}012/3 = 0{,}4$%.

**Memahami hasil.** Nilai $\langle S^2\rangle$ adalah "termometer" kemurnian spin sebuah fungsi gelombang. Nilai 1 untuk $D_1$ berarti campuran 50 : 50, sangat tercemar. Untuk radikal organik yang stabil, UHF biasanya memberi kontaminasi kecil seperti di (b) dan hasilnya masih dapat dipercaya; untuk diradikal, logam transisi, dan keadaan transisi pemutusan ikatan, kontaminasinya bisa besar dan energinya tidak dapat dipercaya tanpa koreksi. Kebiasaan memeriksa $\langle S^2\rangle$ di setiap keluaran program adalah salah satu kebiasaan baik pertama yang dipelajari kimiawan komputasi.
:::

::: {.kuis}
**Kuis cepat 9.6**

(a) Berapa suku dalam determinan Slater atom boron? (b) Apakah $|1s\alpha\,1s\beta\,2s\alpha\,2s\beta|$ fungsi eigen $\hat S^2$? Berapa $S$-nya? (c) Mengapa determinan berubah tanda bila dua kolomnya ditukar, dan apakah ini mengubah sifat fisika?
:::

## 9.7 Atom litium

### Konfigurasi 1s²2s

Litium ($Z = 3$) adalah atom pertama yang memerlukan asas Pauli. Dua elektron menempati 1s dengan spin berlawanan, dan elektron ketiga harus pergi ke kulit $n = 2$. Dalam ion mirip hidrogen, 2s dan 2p terdegenerasi; dalam litium, elektron ketiga melihat inti yang diperisai oleh dua elektron 1s, dan seperti pada helium tereksitasi (Contoh 8.45), orbital 2s, yang **menembus** awan 1s, lebih stabil daripada 2p. Keadaan dasar litium karena itu $1s^22s$, dengan fungsi gelombang (pendekatan satu determinan)

$$
\Psi(\text{Li}) = |1s\alpha\,1s\beta\,2s\alpha| . \qquad \text{(9.23)}
$$

Keadaan dengan $2s\beta$ di kolom ketiga mempunyai energi sama; bersama-sama keduanya membentuk doblet $^2$S ($S = \tfrac12$).

### Energi determinan

Hamiltonian litium (inti diam, satuan atom) adalah

$$
\hat H = \sum_{i=1}^3\left(-\tfrac12\nabla_i^2 - \frac{3}{r_i}\right) + \frac{1}{r_{12}} + \frac{1}{r_{13}} + \frac{1}{r_{23}} = \sum_i\hat h(i) + \sum_{i<j}\frac{1}{r_{ij}} .
$$

Nilai harapnya dalam determinan (9.23), dengan orbital ruang 1s dan 2s yang ortonormal, dapat dihitung dengan aturan Condon–Slater (subbab 9.14), atau dengan menguraikan determinan seperti Contoh 9.16 dan memakai ortonormalitas. Hasilnya:

$$
E = 2h_{1s} + h_{2s} + J_{1s1s} + 2J_{1s2s} - K_{1s2s} , \qquad \text{(9.24)}
$$

dengan $h_i = \langle i|\hat h|i\rangle$, $J$ integral Coulomb, dan $K$ integral pertukaran (subbab 8.9). Setiap pasangan elektron menyumbang satu integral Coulomb: pasangan (1s$\alpha$, 1s$\beta$) memberi $J_{1s1s}$, pasangan (1s$\alpha$, 2s$\alpha$) dan (1s$\beta$, 2s$\alpha$) masing-masing $J_{1s2s}$. Integral pertukaran hanya muncul untuk pasangan dengan spin **sama**, yaitu (1s$\alpha$, 2s$\alpha$), karena integral pertukaran antara spin berlawanan memuat $\langle\alpha|\beta\rangle = 0$. Aturan ini berlaku umum: **pertukaran hanya terjadi antara elektron berspin sejajar**, dan ia selalu menurunkan energi. Inilah sumber aturan Hund pertama (subbab 9.12).

### Fungsi uji dan hasilnya

Fungsi uji yang sederhana tetapi baik adalah orbital Slater dengan eksponen berbeda: $1s \propto e^{-\zeta_1r}$ dan $2s \propto re^{-\zeta_2r}$, dengan 2s diortogonalkan pada 1s (Gram–Schmidt). Integral-integralnya dapat dihitung analitis atau numerik; Contoh 9.21 melakukannya dengan Python. Hasil minimisasi:

$$
\zeta_1 = 2{,}686 , \qquad \zeta_2 = 0{,}637 , \qquad E = -7{,}4179\ E_h = -201{,}85\ \text{eV} .
$$

Nilai Hartree–Fock (orbital terbaik yang mungkin dalam satu determinan) adalah $-7{,}4327\ E_h$, dan energi eksak (nonrelativistik) $-7{,}4781\ E_h$. Dua parameter sudah mencapai $0{,}015\ E_h$ dari batas Hartree–Fock.

Eksponen 1s, 2,686, hampir sama dengan $3 - \tfrac{5}{16} = 2{,}6875$ untuk ion Li⁺ (subbab 8.3): elektron 2s yang jauh hampir tidak memengaruhi kulit dalam. Eksponen 2s, 0,637, berarti orbital Slater $re^{-0{,}637r}$; padanan muatan efektifnya ($\zeta = Z_\text{ef}/n$) adalah $Z_\text{ef} \approx 1{,}27$. Dari luar, inti +3 tampak terperisai hampir penuh oleh dua elektron 1s.

::: {.contoh}
**Contoh 9.21 · Energi litium dengan Python**

Hitung (9.24) untuk fungsi uji di atas dengan integrasi numerik pada kisi radial, lalu minimumkan terhadap $\zeta_1$ dan $\zeta_2$. Untuk orbital s, tulis $u(r) = rR(r)$; energi kinetik $\tfrac12\int u'^2dr$, dan integral dua elektron dihitung dari potensial awan muatan bersimetri bola seperti di subbab 8.3.

**Penyelesaian.**

```python
import numpy as np
from scipy.integrate import cumulative_trapezoid as kum
from scipy.optimize import minimize

r = np.linspace(1e-7, 40, 200001)          # kisi radial (bohr)
I = lambda f: np.trapezoid(f, r)
norm = lambda u: u/np.sqrt(I(u*u))          # u = r R(r)

def h(u, Z=3):                              # <-1/2 lap - Z/r>
    du = np.gradient(u, r)
    return 0.5*I(du*du) - Z*I(u*u/r)

def J(ui, uj, uk, ul):                      # (ij|kl), orbital s
    rho = uk*ul
    q = kum(rho, r, initial=0)              # muatan di dalam r
    t = kum(rho/r, r, initial=0)
    return I(ui*uj*(q/r + t[-1] - t))

def energi(p):
    z1, z2 = p
    a = norm(r*np.exp(-z1*r))               # 1s
    f = norm(r*r*np.exp(-z2*r))             # 2s Slater
    b = norm(f - I(a*f)*a)                  # ortogonal pada 1s
    return (2*h(a) + h(b) + J(a, a, a, a)
            + 2*J(a, a, b, b) - J(a, b, a, b))

hasil = minimize(energi, [2.7, 0.65], method='Nelder-Mead')
print(hasil.x.round(3), round(hasil.fun, 5))
# keluaran: [2.686 0.637] -7.41793
```

Di titik optimum: $h_{1s} = -4{,}4508$, $h_{2s} = -0{,}8188$, $J_{1s1s} = 1{,}6790$, $J_{1s2s} = 0{,}3180$, $K_{1s2s} = 0{,}0125\ E_h$.

**Memahami hasil.** Pemeriksaan ketelitian: $J_{1s1s}$ harus tepat $5\zeta_1/8 = 1{,}6790$, dan memang demikian. Integral pertukaran $K_{1s2s}$ kecil (0,34 eV), karena orbital 1s dan 2s menempati daerah yang sangat berbeda ($\langle r\rangle = 0{,}56$ dan $3{,}98\ a_0$) sehingga kerapatan tumpang tindihnya kecil. Tolakan antara elektron 2s dan kulit dalam, $2J_{1s2s} = 0{,}636\ E_h$, hampir menghapus tarikan inti tambahan yang dirasakan elektron 2s; itulah perisai dalam bahasa integral. Metode yang sama, dengan lebih banyak fungsi dan iterasi swakonsisten, adalah metode Hartree–Fock untuk atom (subbab 9.8).
:::

::: {.contoh}
**Contoh 9.22 · Energi ionisasi litium**

(a) Energi orbital 2s dalam determinan adalah $\varepsilon_{2s} = h_{2s} + 2J_{1s2s} - K_{1s2s}$. Hitung dari data Contoh 9.21 dan bandingkan $-\varepsilon_{2s}$ dengan energi ionisasi terukur 5,392 eV. (b) Hitung muatan inti efektif $Z_\text{ef}$ yang memberi energi mirip hidrogen $-Z_\text{ef}^2/8$ yang sama. (c) Bandingkan dengan aturan Slater ($\sigma = 2 \times 0{,}85$ untuk elektron $n = 2$ yang diperisai dua elektron 1s).

**Penyelesaian.** (a) $\varepsilon_{2s} = -0{,}8188 + 0{,}6361 - 0{,}0125 = -0{,}1953\ E_h$; $-\varepsilon_{2s} = 5{,}31$ eV, galat 1,5%.

(b) $Z_\text{ef} = \sqrt{8 \times 0{,}1953} = 1{,}25$.

(c) Slater: $Z_\text{ef} = 3 - 1{,}70 = 1{,}30$, energi $-1{,}30^2/8 = -0{,}211\ E_h$, energi ionisasi 5,75 eV (terlalu tinggi 7%).

**Memahami hasil.** Mengambil $-\varepsilon$ sebagai energi ionisasi adalah **teorema Koopmans** (subbab 9.8): bila elektron dicabut tanpa orbital lain sempat menyesuaikan diri, energi yang diperlukan sama dengan minus energi orbitalnya. Untuk litium, muatan inti efektif sekitar 1,25 berarti elektron valensi hampir seperti elektron atom hidrogen di kulit $n = 2$ (yang energi ionisasinya hanya 3,4 eV), sedikit lebih terikat karena menembus kulit dalam. Energi ionisasi rendah inilah yang membuat litium dan logam alkali lain menjadi reduktor kuat dan pembentuk kation $M^+$.
:::

::: {.contoh}
**Contoh 9.23 · Nyala merah litium dan cacat kuantum**

Garam litium mewarnai nyala menjadi merah tua karena garis 670,8 nm (2p → 2s). Energi ionisasi litium 5,392 eV. Energi elektron valensi atom alkali sering ditulis $E = -1/2(n - \delta_\ell)^2$ (satuan atom), dengan $\delta_\ell$ **cacat kuantum** yang hanya bergantung pada $\ell$. (a) Hitung $\delta_s$ dan $\delta_p$ litium. (b) Tafsirkan.

**Penyelesaian.** (a) 2s: $E = -5{,}392\ \text{eV} = -0{,}1981\ E_h$, $n - \delta_s = 1/\sqrt{2 \times 0{,}1981} = 1{,}589$, jadi $\delta_s = 0{,}411$. 2p: energi foton 670,8 nm = 1,848 eV, sehingga $E_{2p} = -3{,}544\ \text{eV} = -0{,}1302\ E_h$, $n - \delta_p = 1{,}959$, dan $\delta_p = 0{,}041$.

(b) Elektron 2p hampir seperti elektron hidrogen ($\delta \approx 0$), karena orbital p hampir tidak menembus kulit 1s. Elektron 2s menembus jauh lebih dalam dan merasakan muatan inti yang kurang terperisai, sehingga energinya lebih rendah.

**Memahami hasil.** Pemecahan 2s–2p sebesar 1,85 eV, yang dalam hidrogen nol, adalah sidik jari penetrasi. Cacat kuantum hampir tetap sepanjang deret Rydberg ($ns$, $np$ dengan $n$ besar), sehingga spektrum alkali dapat diramalkan dengan dua atau tiga bilangan. Uji nyala di laboratorium kimia analitik (Li merah, Na kuning, K ungu) adalah pengamatan langsung pemecahan $\ell$ oleh elektron kulit dalam; warna masing-masing ditentukan oleh cacat kuantum $\delta_s - \delta_p$ dan bilangan kuantum $n$ elektron valensi.
:::

::: {.kuis}
**Kuis cepat 9.7**

(a) Mengapa (9.24) memuat $K_{1s2s}$ hanya sekali, padahal ada dua elektron 1s? (b) Untuk keadaan tereksitasi $1s^22p$, apakah energi ionisasinya lebih besar atau lebih kecil daripada keadaan dasar, dan berapa (dalam eV)? (c) Mengapa eksponen 1s litium hampir sama dengan eksponen ion Li⁺?
:::

