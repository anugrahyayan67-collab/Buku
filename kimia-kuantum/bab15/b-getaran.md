## 15.4 Spektroskopi rotasi lanjut

### Apa yang sudah kita ketahui

Bab 6 membahas rotor tegar diatom: tingkat energi $F(J) = BJ(J + 1)$, aturan seleksi $\Delta J = \pm1$ yang hanya berlaku bila molekul berdipol permanen, garis berjarak $2B$, populasi Boltzmann, distorsi sentrifugal, dan statistik spin inti. Subbab ini memperluasnya ke tiga arah yang penting dalam praktik: molekul poliatom (rotor simetris dan tak simetris), pengaruh medan listrik (efek Stark) yang dipakai untuk mengukur momen dipol, dan spektroskopi Raman rotasi yang membuka spektrum rotasi molekul tanpa dipol seperti N₂, O₂, dan CO₂.

### Rotor simetris

Molekul seperti NH₃, CH₃F, CH₃CN, dan C₆H₆ mempunyai sumbu simetri berlipat tiga atau lebih, sehingga dua dari tiga momen inersia utamanya sama. Hamiltonian rotor tegar klasik $E = \sum_i L_i^2/2I_i$ menjadi, dengan $I_b = I_c \ne I_a$ (lonjong) atau $I_a = I_b \ne I_c$ (pipih),

$$
\hat H = \frac{\hat L^2}{2I_b} + \left(\frac{1}{2I_a} - \frac{1}{2I_b}\right)\hat L_a^2 , \qquad \text{(15.13)}
$$

dengan $\hat L_a$ komponen momentum sudut sepanjang sumbu simetri molekul. Karena $\hat L^2$ dan $\hat L_a$ saling komut, keduanya mempunyai fungsi eigen bersama, dengan bilangan kuantum $J$ dan $K$ ($K = -J, \ldots, J$, proyeksi pada sumbu molekul). Selain itu ada proyeksi $M$ pada sumbu ruang, sehingga setiap tingkat dengan $K \ne 0$ berdegenerasi $2(2J + 1)$:

$$
F(J, K) = BJ(J + 1) + (A - B)K^2 \quad (\text{lonjong}), \qquad F(J, K) = BJ(J + 1) + (C - B)K^2 \quad (\text{pipih}) . \qquad \text{(15.14)}
$$

Momen dipol molekul simetris terletak sepanjang sumbu simetri, sehingga radiasi tidak dapat memberikan momen putar terhadap sumbu itu. Aturan seleksinya $\Delta J = \pm1$, $\Delta K = 0$. Akibatnya garis serapan tetap di $2B(J + 1)$, sama dengan molekul linear, dan $A$ tidak dapat dibaca dari spektrum gelombang mikro murni. Distorsi sentrifugal menambah suku $-D_JJ^2(J + 1)^2 - D_{JK}J(J + 1)K^2 - D_KK^4$, sehingga garis $J + 1 \leftarrow J$ terpecah sedikit menurut $K$:

$$
\nu = 2B(J + 1) - 4D_J(J + 1)^3 - 2D_{JK}(J + 1)K^2 . \qquad \text{(15.15)}
$$

::: {.contoh}
**Contoh 15.15 · Struktur $K$ asetonitril**

Untuk CH₃CN, $B = 9198{,}9$ MHz, $D_J = 3{,}8$ kHz, dan $D_{JK} = 17{,}74$ kHz. Hitung frekuensi komponen $K = 0$ sampai 4 garis $J = 5 \leftarrow 4$.

**Penyelesaian.** Dengan (15.15) dan $J + 1 = 5$: $2B(5) = 91\,989{,}0$ MHz, $4D_J(125) = 1{,}90$ MHz, dan $2D_{JK}(5)K^2 = 0{,}1774K^2$ MHz. Hasilnya: $K = 0$: 91 987,10; $K = 1$: 91 986,92; $K = 2$: 91 986,39; $K = 3$: 91 985,50; $K = 4$: 91 984,26 MHz.

**Memahami hasil.** Kelima komponen terpisah dalam rentang 3 MHz, mudah diukur dengan spektrometer gelombang mikro modern yang ketelitiannya beberapa kilohertz. Karena komponen dengan $K$ berbeda hanya dapat saling berpindah melalui tumbukan (radiasi tidak mengubah $K$), perbandingan intensitasnya mengukur suhu gas secara langsung. Asetonitril dipakai astronom sebagai termometer awan pembentuk bintang yang panas dan rapat, melengkapi CO untuk awan yang dingin.
:::

### Rotor tak simetris

Kebanyakan molekul, termasuk H₂O, H₂CO, dan hampir semua molekul organik, mempunyai tiga momen inersia yang berbeda. Tidak ada bilangan kuantum $K$ yang baik, dan tingkat energinya diperoleh dengan mendiagonalkan Hamiltonian rotasi dalam basis fungsi rotor simetris (subbab 8.5). Tingkatnya diberi label $J_{K_aK_c}$, yaitu nilai $|K|$ yang akan diperoleh bila molekul didistorsi ke batas lonjong ($K_a$) dan ke batas pipih ($K_c$). Derajat ketaksimetrisan diukur dengan parameter Ray

$$
\kappa = \frac{2B - A - C}{A - C} , \qquad \text{(15.16)}
$$

yang bernilai −1 untuk rotor lonjong dan +1 untuk rotor pipih. Air ($A = 27{,}88$, $B = 14{,}51$, $C = 9{,}28$ cm⁻¹) mempunyai $\kappa = -0{,}44$: sangat tak simetris. Spektrum rotasinya yang kaya garis, dari gelombang mikro sampai inframerah jauh, membuat uap air menjadi penyerap utama radiasi termal di atmosfer.

::: {.awas}
**Oven gelombang mikro tidak bekerja pada resonansi air**

Garis rotasi air yang terkenal di 22,235 GHz (transisi $6_{16} \leftarrow 5_{23}$) sering dikira sebagai prinsip kerja oven gelombang mikro. Oven bekerja pada 2,45 GHz, jauh dari garis rotasi mana pun, dan yang dipanaskan adalah air **cair**, yang tidak mempunyai spektrum rotasi bergaris karena molekulnya tidak dapat berputar bebas. Pemanasan terjadi karena dipol-dipol air yang terikat ikatan hidrogen berusaha mengikuti medan listrik yang berosilasi dan kehilangan energi melalui gesekan dengan tetangganya (relaksasi dielektrik). Frekuensi 2,45 GHz dipilih karena berada di pita frekuensi yang diizinkan dan cukup menembus makanan, bukan karena resonansi.
:::

### Menentukan struktur dari momen inersia

Satu molekul linear triatom mempunyai dua panjang ikatan tetapi hanya satu momen inersia. Kuncinya adalah **substitusi isotop**: dalam hampiran Born–Oppenheimer (subbab 11.1), panjang ikatan tidak berubah ketika satu atom diganti isotopnya, sedangkan momen inersia berubah. Dua isotopolog memberi dua persamaan untuk dua tak diketahui.

::: {.contoh}
**Contoh 15.16 · Panjang ikatan OCS**

Tetapan rotasi ¹⁶O¹²C³²S dan ¹⁶O¹²C³⁴S masing-masing 6081,492 MHz dan 5932,834 MHz. Tentukan panjang ikatan C=O dan C=S.

**Rencana.** Hitung $I = h/8\pi^2B$ untuk keduanya. Untuk molekul linear dengan atom pada posisi $0$, $r_1$, $r_1 + r_2$, momen inersia terhadap pusat massa adalah $I = \sum m_iz_i^2 - (\sum m_iz_i)^2/\sum m_i$. Selesaikan dua persamaan taklinear secara numerik.

**Penyelesaian.**

```python
import numpy as np
from scipy.optimize import fsolve
h, u = 6.62607015e-34, 1.66053906660e-27
I_dari_B = lambda B: h / (8*np.pi**2*B) / (u*1e-20)        # dalam u Å^2
def I_linear(m, r1, r2):
    z = np.array([0, r1, r1 + r2]); m = np.array(m)
    return (m*z**2).sum() - (m*z).sum()**2 / m.sum()
mO, mC, mS32, mS34 = 15.99491, 12.0, 31.97207, 33.96787
I1, I2 = I_dari_B(6081.492e6), I_dari_B(5932.834e6)
r = fsolve(lambda p: [I_linear([mO, mC, mS32], *p) - I1,
                      I_linear([mO, mC, mS34], *p) - I2], [1.2, 1.6])
print(I1, I2, r)
```

Hasilnya $I_1 = 83{,}101$ dan $I_2 = 85{,}183$ u Å², serta $r(\text{C=O}) = 1{,}163$ Å dan $r(\text{C=S}) = 1{,}560$ Å.

**Memahami hasil.** Panjang ikatan dari spektroskopi gelombang mikro mempunyai ketelitian beberapa perseribu angstrom, jauh lebih teliti daripada difraksi sinar-X untuk molekul kecil. Nilai yang diperoleh dengan tetapan $B_0$ disebut struktur $r_0$; ia sedikit berbeda dari struktur kesetimbangan $r_e$ karena getaran titik nol (subbab 6.12), dan karena itu dua isotopolog dapat memberi jawaban yang sedikit berbeda dari dua isotopolog lain. Metode substitusi Kraitchman, yang memakai banyak isotopolog, mengurangi galat ini.
:::

### Efek Stark dan pengukuran momen dipol

Medan listrik statis $\mathcal E$ berinteraksi dengan momen dipol molekul, $\hat H' = -\mu\mathcal E\cos\theta$. Untuk molekul linear, perturbasi ini tidak mempunyai unsur diagonal dalam basis $|J, M\rangle$ (orientasi rata-rata molekul yang berputar tidak mempunyai arah), sehingga efeknya baru muncul pada orde kedua (subbab 8.7):

$$
E^{(2)}(J, M) = \frac{\mu^2\mathcal E^2}{2hB}\,\frac{J(J + 1) - 3M^2}{J(J + 1)(2J - 1)(2J + 3)}\quad (J \ge 1), \qquad E^{(2)}(0, 0) = -\frac{\mu^2\mathcal E^2}{6hB} , \qquad \text{(15.17)}
$$

dengan $B$ dalam hertz. Medan memecah degenerasi $M$ (tetapi $+M$ dan $-M$ tetap sama), dan geseran sebanding dengan $\mu^2\mathcal E^2$. Mengukur geseran dalam medan yang diketahui adalah cara paling teliti menentukan momen dipol molekul dalam fase gas, bebas dari pengaruh pelarut.

::: {.contoh}
**Contoh 15.17 · Momen dipol OCS dari efek Stark**

Untuk OCS ($B = 6081{,}49$ MHz, $\mu = 0{,}7152$ D), hitung geseran komponen $M = 0 \to 0$ garis $J = 1 \leftarrow 0$ dalam medan 1000 V/cm.

**Penyelesaian.** $\mu\mathcal E/h = (0{,}7152 \times 3{,}3356 \times 10^{-30})(10^5)/6{,}626 \times 10^{-34} = 360{,}0$ MHz. Maka $(\mu\mathcal E)^2/h^2B = 360{,}0^2/6081{,}49 = 21{,}31$ MHz. Dari (15.17): $J = 1$, $M = 0$ naik $\tfrac{2}{2 \cdot 2 \cdot 1 \cdot 5} = \tfrac1{10}$ satuan; $J = 0$ turun $\tfrac16$ satuan. Geseran transisi $21{,}31 \times (\tfrac1{10} + \tfrac16) = 5{,}68$ MHz.

**Memahami hasil.** Geseran 5,7 MHz pada garis 12,163 GHz mudah diukur. Karena hubungan kuadratnya, kesalahan 1% pada geseran hanya memberi 0,5% kesalahan pada $\mu$. Momen dipol OCS yang diukur dengan cara ini begitu teliti sehingga dipakai sebagai baku untuk mengkalibrasi medan listrik dalam spektrometer Stark. Program kimia kuantum diuji dengan membandingkan momen dipol hasil hitungan dengan nilai-nilai Stark seperti ini.
:::

### Spektroskopi Raman rotasi

Molekul tanpa momen dipol permanen tidak mempunyai spektrum rotasi serapan, tetapi polarisabilitasnya biasanya **anisotrop**: molekul diatom lebih mudah dipolarisasi sepanjang ikatan daripada tegak lurus. Ketika molekul berputar, polarisabilitas yang "dilihat" medan listrik cahaya berubah dua kali setiap putaran (keadaan molekul setelah berputar 180° sama dengan semula). Akibatnya cahaya terhambur dengan frekuensi bergeser, dan aturan seleksinya

$$
\Delta J = 0, \pm2 \qquad (\text{molekul linear}) . \qquad \text{(15.18)}
$$

$\Delta J = 0$ memberikan hamburan Rayleigh; $\Delta J = +2$ memberikan cabang **S** (Stokes) dan $\Delta J = -2$ cabang **O** (anti-Stokes). Geseran garis cabang S dari frekuensi laser adalah

$$
\Delta\tilde\nu = F(J + 2) - F(J) = B(4J + 6) = 4B\left(J + \tfrac32\right) , \qquad J = 0, 1, 2, \ldots \qquad \text{(15.19)}
$$

Garis pertama berada di $6B$ dan garis-garis berikutnya berjarak $4B$. Statistik spin inti (subbab 6.11) tampak jelas: untuk ¹⁴N₂ ($I = 1$), tingkat $J$ genap berbobot 6 dan $J$ ganjil berbobot 3, sehingga intensitas garis berselang-seling 2 : 1. Untuk ¹⁶O¹²C¹⁶O (inti ¹⁶O, $I = 0$), hanya $J$ genap yang ada, sehingga garis berjarak $8B$.

![Gambar 15.2 Spektrum Raman rotasi N₂ pada 298 K yang dihitung dari (15.19) dengan $B = 1{,}9896$ cm⁻¹, populasi Boltzmann, dan bobot spin inti 6 : 3. Cabang S (geseran positif, Stokes) dan cabang O (anti-Stokes) mengapit garis Rayleigh yang jauh lebih kuat (dipotong). Selang-seling intensitas 2 : 1 berasal dari spin inti ¹⁴N.](fig/c_ramanrot.png){width=90%}

::: {.contoh}
**Contoh 15.18 · Spektrum Raman rotasi N₂**

Untuk N₂, $B_0 = 1{,}9896$ cm⁻¹. (a) Hitung geseran empat garis S pertama. (b) Garis mana yang paling kuat pada 298 K? (c) Mengapa N₂ di atmosfer dapat diukur dengan lidar Raman rotasi padahal tidak menyerap gelombang mikro?

**Penyelesaian.** (a) $4B(J + \tfrac32)$: 11,94; 19,90; 27,85; 35,81 cm⁻¹ untuk $J = 0$–3. (b) Intensitas sebanding dengan $g_J(2J + 1)e^{-BJ(J+1)hc/kT}$. Dengan $kT/hc = 207{,}2$ cm⁻¹, nilai relatifnya untuk $J = 0$–8 adalah 6,0; 8,8; 28,3; 18,7; 44,6; 24,7; 52,1; 26,3; 51,1. Garis terkuat adalah $J = 6$ (geseran 59,7 cm⁻¹), dengan $J = 8$ hampir sama. (c) Hamburan Raman hanya memerlukan perubahan polarisabilitas, bukan dipol permanen.

**Memahami hasil.** Tanpa bobot spin inti, puncak distribusi akan berada di $J \approx \sqrt{kT/2hcB} - \tfrac12 = 6{,}7$; selang-seling 2 : 1 membuat garis genap menonjol. Selang-seling ini juga bukti bahwa inti ¹⁴N adalah boson: seandainya fermion, pola intensitasnya akan berbeda. Lidar Raman rotasi mengukur suhu atmosfer dari perbandingan intensitas garis $J$ rendah dan tinggi, termometer yang tidak memerlukan kalibrasi.
:::

::: {.contoh}
**Contoh 15.19 · Hidrogen orto dan para**

Untuk H₂, $B = 60{,}85$ cm⁻¹. (a) Hitung geseran garis S(0) dan S(1) menurut rotor tegar. Nilai teramati 354,4 dan 587,0 cm⁻¹. (b) Pada suhu kamar perbandingan orto (J ganjil, bobot 3) dan para (J genap, bobot 1) sekitar 3 : 1. Garis mana yang lebih kuat?

**Penyelesaian.** (a) S(0) $= 6B = 365{,}1$ cm⁻¹; S(1) $= 10B = 608{,}5$ cm⁻¹. Nilai teramati 3% lebih rendah karena distorsi sentrifugal yang besar pada H₂ dan karena $B_0 < B_e$. (b) S(1), karena berasal dari $J = 1$ (orto) yang berbobot 3 dan juga berpopulasi besar.

**Memahami hasil.** Spektrum Raman rotasi adalah cara paling langsung mengukur perbandingan orto/para hidrogen. Hidrogen cair yang baru dibuat masih mengandung 75% orto dan perlahan berubah ke para, melepaskan panas yang cukup untuk menguapkan sebagian besar cairan; karena itu pabrik hidrogen cair memakai katalis paramagnetik untuk mempercepat konversi sebelum penyimpanan. Pengukuran Raman inilah yang dipakai untuk memantau prosesnya.
:::

::: {.kuis}
**Kuis cepat 15.4**

Mengapa CH₄ (rotor bola) tidak mempunyai spektrum gelombang mikro maupun spektrum Raman rotasi murni? Mengapa garis Raman rotasi CO₂ berjarak $8B$, bukan $4B$?
:::

## 15.5 Spektroskopi getaran IR

### Mode normal dan aktivitas IR

Molekul taklinear dengan $N$ atom mempunyai $3N - 6$ mode normal (subbab 5.11); molekul linear $3N - 5$. Menurut subbab 5.8, mode normal $Q_k$ aktif inframerah bila momen dipol berubah selama getaran, $(\partial\boldsymbol\mu/\partial Q_k)_0 \ne 0$, dengan aturan seleksi harmonik $\Delta v_k = \pm1$. Teori grup memberikan uji yang cepat (subbab 10.9): momen dipol transisi $\langle 1|\hat{\boldsymbol\mu}|0\rangle$ tidak nol bila kesetangkupan mode sama dengan kesetangkupan salah satu komponen $x$, $y$, atau $z$, karena keadaan dasar getaran bersetangkup penuh dan keadaan $v_k = 1$ mempunyai kesetangkupan mode itu sendiri.

| Molekul | Grup | Mode (cm⁻¹, kesetangkupan) | Aktif IR |
|---|---|---|---|
| H₂O | $C_{2v}$ | 3657 ($a_1$), 1595 ($a_1$), 3756 ($b_2$) | semua |
| CO₂ | $D_{\infty h}$ | 1333 ($\sigma_g^+$), 667 ($\pi_u$), 2349 ($\sigma_u^+$) | 667, 2349 |
| CH₄ | $T_d$ | 2917 ($a_1$), 1534 ($e$), 3019 ($t_2$), 1306 ($t_2$) | 3019, 1306 |
| SF₆ | $O_h$ | 775 ($a_{1g}$), 643 ($e_g$), 948 ($t_{1u}$), 615 ($t_{1u}$), 525 ($t_{2g}$), 346 ($t_{2u}$) | 948, 615 |

: Tabel 15.1 Mode normal beberapa molekul dan aktivitas inframerahnya.

Untuk molekul dengan kesetangkupan tinggi, hanya sebagian kecil mode yang tampak dalam spektrum IR. SF₆ mempunyai 15 mode (enam frekuensi berbeda), tetapi spektrum IR-nya hanya memperlihatkan dua pita dasar. Benzena, dengan 30 mode dan 20 frekuensi berbeda, hanya memperlihatkan empat pita dasar.

### Kontur pita: sejajar dan tegak lurus

Dalam fase gas, setiap pita getaran disertai struktur rotasi. Untuk molekul linear ada dua jenis pita. **Pita sejajar** berasal dari getaran yang momen dipol transisinya sepanjang sumbu molekul ($\Sigma \leftarrow \Sigma$, misalnya ulur asimetris CO₂ di 2349 cm⁻¹). Aturan seleksinya $\Delta J = \pm1$, sama dengan diatom: cabang P dan R dengan celah di tengah. **Pita tegak lurus** berasal dari getaran yang momen dipol transisinya tegak lurus sumbu ($\Pi \leftarrow \Sigma$, misalnya tekuk CO₂ di 667 cm⁻¹). Getaran tekuk yang berdegenerasi membawa momentum sudut terhadap sumbu molekul, dan aturan seleksinya menjadi $\Delta J = 0, \pm1$: selain P dan R muncul **cabang Q** yang tajam di tengah, karena semua transisi $\Delta J = 0$ jatuh hampir pada frekuensi yang sama.

![Gambar 15.3 Kontur pita CO₂ pada 298 K yang dihitung dari tingkat rotasi molekul linear ($B = 0{,}390$ cm⁻¹, hanya $J$ genap pada keadaan dasar) dengan lebar garis 0,6 cm⁻¹. (a) Pita sejajar $\nu_3$: cabang P dan R tanpa cabang Q. (b) Pita tegak lurus $\nu_2$: cabang Q yang tajam di tengah.](fig/c_pita.png){width=92%}

Bentuk pita dengan demikian memberi tahu arah momen dipol transisi relatif terhadap sumbu molekul, keterangan yang sangat membantu untuk mengenali getaran pada molekul yang belum dikenal.

::: {.contoh}
**Contoh 15.20 · Jarak puncak P dan R**

Untuk pita sejajar, jarak antara puncak cabang P dan R kira-kira $\Delta\tilde\nu_{PR} \approx \sqrt{8BkT/hc}$. Hitung untuk CO₂ ($B = 0{,}390$ cm⁻¹) dan HCl ($B = 10{,}4$ cm⁻¹) pada 298 K. Bagaimana rumus ini dipakai bila garis-garis rotasi tidak terpisah?

**Penyelesaian.** $kT/hc = 207{,}2$ cm⁻¹. CO₂: $\sqrt{8 \times 0{,}390 \times 207{,}2} = 25{,}4$ cm⁻¹. HCl: $\sqrt{8 \times 10{,}4 \times 207{,}2} = 131$ cm⁻¹.

**Memahami hasil.** Untuk molekul besar, garis rotasi individual tidak terpisah dalam spektrometer biasa, tetapi jarak antarpuncak kontur masih terukur, sehingga $B$, dan dengan demikian ukuran molekul, dapat ditaksir dari bentuk pita saja. Rumus ini diturunkan dengan mencari $J$ yang memaksimumkan populasi (subbab 6.11) lalu menghitung jarak garis R($J_\text{maks}$) dan P($J_\text{maks}$), yaitu $4B(J_\text{maks} + \tfrac12)$.
:::

### Nada atas, pita gabungan, dan pita panas

Anharmonisitas (subbab 5.9) melonggarkan aturan $\Delta v = \pm1$. Untuk molekul poliatom, energi getaran dengan suku anharmonik orde terendah adalah

$$
G(v_1, v_2, \ldots) = \sum_k\omega_k\left(v_k + \tfrac{d_k}{2}\right) + \sum_{k \le l}x_{kl}\left(v_k + \tfrac{d_k}{2}\right)\left(v_l + \tfrac{d_l}{2}\right) , \qquad \text{(15.20)}
$$

dengan $d_k$ degenerasi mode $k$ dan $x_{kl}$ tetapan anharmonisitas (biasanya negatif). Selain pita dasar ($v_k = 0 \to 1$), muncul **nada atas** ($0 \to 2$, di sekitar $2\tilde\nu_k$), **pita gabungan** ($v_k$ dan $v_l$ masing-masing naik satu, di sekitar $\tilde\nu_k + \tilde\nu_l$), dan **pita panas** (dari tingkat yang sudah tereksitasi termal, misalnya $v_k = 1 \to 2$). Intensitasnya biasanya sepuluh sampai seratus kali lebih lemah daripada pita dasar. Kesetangkupan nada atas dan pita gabungan adalah hasil kali langsung kesetangkupan mode-modenya, sehingga pita gabungan dua mode yang tidak aktif IR dapat menjadi aktif IR.

::: {.contoh}
**Contoh 15.21 · Nada atas dan pita gabungan air**

Pita dasar H₂O dalam gas: $\nu_1 = 3657{,}1$, $\nu_2 = 1594{,}7$, $\nu_3 = 3755{,}9$ cm⁻¹. Nada atas $2\nu_2$ teramati di 3151,6 cm⁻¹ dan pita gabungan $\nu_2 + \nu_3$ di 5331,3 cm⁻¹. (a) Hitung selisih terhadap ramalan harmonik. (b) Tentukan kesetangkupan $\nu_2 + \nu_3$ dan apakah ia aktif IR.

**Penyelesaian.** (a) $2\nu_2$: ramalan $3189{,}4$, selisih 37,8 cm⁻¹. Dari (15.20), $G(0, 2, 0) - G(0, 0, 0) = 2\omega_2 + 6x_{22} + \ldots$ dan $G(0, 1, 0) - G(0, 0, 0) = \omega_2 + 2x_{22} + \ldots$, sehingga selisihnya $2x_{22} = -37{,}8$ cm⁻¹ dan $x_{22} = -18{,}9$ cm⁻¹. $\nu_2 + \nu_3$: ramalan 5350,6, selisih $x_{23} = -19{,}3$ cm⁻¹. (b) $a_1 \otimes b_2 = b_2$, yang bertransformasi seperti $y$: aktif IR.

**Memahami hasil.** Pita-pita air di inframerah dekat (sekitar 5300 dan 7250 cm⁻¹) adalah pita gabungan dan nada atas. Walaupun lemah, mereka menyerap kuat bila lintasan cahayanya panjang: itulah sebabnya air dalam jumlah besar tampak sedikit biru (nada atas ulur O–H yang tinggi menyerap sedikit cahaya merah) dan sebabnya spektroskopi inframerah dekat dipakai untuk mengukur kadar air dalam biji-bijian dan obat-obatan tanpa merusak sampel.
:::

### Resonansi Fermi

Bila nada atas atau pita gabungan kebetulan hampir berdegenerasi dengan pita dasar yang berkesetangkupan sama, keduanya bercampur melalui suku anharmonik kubik potensial. Inilah **resonansi Fermi**, yang ditemukan Fermi pada 1931 untuk menjelaskan spektrum Raman CO₂. Dua keadaan yang semula $E_a$ dan $E_b$ dengan unsur kopling $W$ menjadi

$$
E_\pm = \tfrac12(E_a + E_b) \pm \tfrac12\sqrt{(E_a - E_b)^2 + 4W^2} . \qquad \text{(15.21)}
$$

Keduanya saling menjauh, dan intensitas pita dasar yang kuat terbagi di antara keduanya. Pada CO₂, $\nu_1$ (sekitar 1333 cm⁻¹) dan $2\nu_2$ (sekitar $2 \times 667 = 1334$ cm⁻¹) bercampur dan menghasilkan dua pita Raman kuat di 1285 dan 1388 cm⁻¹. Bila perbandingan intensitas kedua pita diketahui, komposisi campuran, dan dengan demikian energi tanpa gangguan, dapat dihitung.

::: {.contoh}
**Contoh 15.22 · Membongkar resonansi Fermi**

Dua pita yang saling beresonansi Fermi berada di 1285 dan 1388 cm⁻¹, dengan perbandingan intensitas $I(1388)/I(1285) = 1{,}4$. Anggap hanya keadaan pita dasar $|a\rangle$ yang membawa intensitas, sehingga $I_\pm \propto |\langle a|\pm\rangle|^2$. Tentukan $E_a$, $E_b$, dan $W$.

**Penyelesaian.** Tulis $|+\rangle = \cos\theta|a\rangle + \sin\theta|b\rangle$ dan $|-\rangle = -\sin\theta|a\rangle + \cos\theta|b\rangle$. Maka $I_+/I_- = \cot^2\theta = 1{,}4$, sehingga $\cos^2\theta = 1{,}4/2{,}4 = 0{,}583$. Untuk masalah dua tingkat, $E_a = \bar E + \tfrac12\Delta_\text{obs}(2\cos^2\theta - 1)$ dan $W = \tfrac12\Delta_\text{obs}\sin2\theta$, dengan $\bar E = 1336{,}5$ dan $\Delta_\text{obs} = 103$ cm⁻¹. Jadi $E_a = 1336{,}5 + 51{,}5(0{,}167) = 1345{,}1$, $E_b = 1327{,}9$ cm⁻¹, dan $W = 51{,}5\sin(2 \times 40{,}2°) = 50{,}8$ cm⁻¹.

**Memahami hasil.** Selisih energi tanpa gangguan hanya 17 cm⁻¹, jauh lebih kecil daripada kopling 51 cm⁻¹: kedua keadaan tercampur hampir separuh-separuh, dan pita "nada atas" yang semestinya lemah menjadi hampir sekuat pita dasar. Resonansi Fermi harus selalu dicurigai bila dua pita kuat muncul di tempat yang hanya diharapkan satu, misalnya pita karbonil ganda pada beberapa aldehida dan pita C–H aldehida di sekitar 2720 dan 2820 cm⁻¹.
:::

### Pergeseran oleh lingkungan dan ikatan hidrogen

Frekuensi getaran peka terhadap lingkungan. Ikatan hidrogen O–H···O melemahkan ikatan O–H (sebagian rapat elektron berpindah ke orbital antiikatan σ*(O–H)), sehingga pita ulur O–H bergeser dari sekitar 3650 cm⁻¹ (O–H bebas dalam gas atau larutan sangat encer) ke 3200–3400 cm⁻¹ dan melebar hingga ratusan cm⁻¹, karena setiap molekul mempunyai geometri ikatan hidrogen yang sedikit berbeda (pelebaran tak homogen). Dalam asam karboksilat dimer, pita ulur O–H melebar dari 2500 sampai 3300 cm⁻¹. Besarnya pergeseran berkorelasi dengan kekuatan ikatan hidrogen (hubungan Badger–Bauer), sehingga spektrum IR dipakai untuk mengukur kekuatan interaksi antarmolekul.

### Spektrometer FTIR

Spektrometer inframerah modern hampir semuanya **spektrometer transformasi Fourier** (FTIR). Cahaya dari sumber dibagi dua oleh pembagi berkas dalam interferometer Michelson; satu berkas memantul pada cermin diam, yang lain pada cermin bergerak, lalu keduanya digabungkan kembali. Detektor mencatat intensitas sebagai fungsi beda lintasan optis $\delta$, yang disebut **interferogram**:

$$
I(\delta) = \int_0^\infty S(\tilde\nu)\left[1 + \cos(2\pi\tilde\nu\delta)\right]d\tilde\nu . \qquad \text{(15.22)}
$$

Spektrum $S(\tilde\nu)$ diperoleh dengan transformasi Fourier balik. Resolusinya ditentukan oleh beda lintasan maksimum: $\Delta\tilde\nu \approx 1/\delta_\text{maks}$. Dibanding spektrometer dispersif, FTIR mengukur semua panjang gelombang sekaligus (keunggulan Fellgett) dan tidak memerlukan celah sempit (keunggulan Jacquinot), sehingga jauh lebih cepat dan peka.

::: {.contoh}
**Contoh 15.23 · Resolusi FTIR dan garis rotasi**

(a) Berapa beda lintasan maksimum yang diperlukan untuk resolusi 0,5 cm⁻¹? (b) Dapatkah spektrometer ini memisahkan garis-garis rotasi pita $\nu_3$ CO₂ dalam fase gas? (c) Bagaimana dengan HCl?

**Penyelesaian.** (a) $\delta_\text{maks} = 1/0{,}5 = 2$ cm, cermin bergerak 1 cm. (b) Garis-garis CO₂ berjarak sekitar $4B = 1{,}56$ cm⁻¹ (hanya $J$ genap pada keadaan dasar), tiga kali resolusi: terpisah. (c) Garis HCl berjarak sekitar $2B = 21$ cm⁻¹: terpisah sangat jelas, bahkan garis isotop ³⁵Cl dan ³⁷Cl (berselisih sekitar 2 cm⁻¹) terpisah.

**Memahami hasil.** Spektrometer FTIR laboratorium biasa beresolusi 0,5–4 cm⁻¹, cukup untuk gas sederhana. Spektrometer riset dengan cermin bergerak beberapa meter mencapai 0,001 cm⁻¹, mendekati lebar Doppler. Untuk sampel cair dan padat, resolusi 4 cm⁻¹ sudah cukup karena pita-pitanya sendiri selebar puluhan cm⁻¹.
:::

::: {.contoh}
**Contoh 15.24 · Mengapa tekuk CO₂ penting bagi iklim**

Hitung bilangan gelombang puncak radiasi benda hitam Bumi bersuhu 288 K, memakai hukum Wien dalam bilangan gelombang $\tilde\nu_\text{maks} = 2{,}821\,kT/hc$. Bandingkan dengan pita tekuk CO₂.

**Penyelesaian.** $kT/hc = 0{,}6950 \times 288 = 200{,}2$ cm⁻¹, sehingga $\tilde\nu_\text{maks} = 565$ cm⁻¹ (17,7 µm). Pita tekuk CO₂ di 667 cm⁻¹ (15,0 µm) terletak di dekat puncak.

**Memahami hasil.** Pita tekuk CO₂ yang aktif IR (karena momen dipolnya berubah tegak lurus sumbu) menyerap tepat di daerah tempat Bumi paling banyak memancarkan energi. Pita ini sudah jenuh di pusatnya; penambahan CO₂ memperkuat serapan di sayap-sayap pita (cabang P dan R yang jauh serta pita panas dan pita isotop), sehingga pemanasannya naik secara logaritmik terhadap konsentrasi. Ulur simetris CO₂ yang tidak aktif IR tidak berperan sama sekali. Aturan seleksi mekanika kuantum menentukan gas mana yang menjadi gas rumah kaca.
:::

::: {.kuis}
**Kuis cepat 15.5**

Berapa banyak pita dasar yang diharapkan dalam spektrum IR CH₄ dan NH₃? Mengapa pita panas CO₂ ($01^10 \to 02^20$) cukup kuat pada suhu kamar, sedangkan pita panas HCl hampir tidak terlihat?
:::

## 15.6 Spektroskopi Raman

### Asal klasik hamburan Raman

Cahaya dengan medan listrik $\mathcal E = \mathcal E_0\cos\omega_0t$ menginduksi momen dipol $\mu_\text{ind} = \alpha\mathcal E$ dalam molekul. Bila molekul bergetar dengan koordinat normal $Q = Q_0\cos\omega_vt$, polarisabilitasnya ikut berubah:

$$
\alpha = \alpha_0 + \left(\frac{\partial\alpha}{\partial Q}\right)_0Q_0\cos\omega_vt . \qquad \text{(15.23)}
$$

Dengan identitas $\cos a\cos b = \tfrac12[\cos(a - b) + \cos(a + b)]$:

$$
\mu_\text{ind} = \alpha_0\mathcal E_0\cos\omega_0t + \tfrac12\left(\frac{\partial\alpha}{\partial Q}\right)_0Q_0\mathcal E_0\left[\cos(\omega_0 - \omega_v)t + \cos(\omega_0 + \omega_v)t\right] . \qquad \text{(15.24)}
$$

Dipol yang berosilasi memancarkan cahaya pada frekuensinya sendiri. Suku pertama adalah hamburan **Rayleigh** pada frekuensi laser. Suku kedua menghasilkan cahaya bergeser ke $\omega_0 - \omega_v$ (**Stokes**) dan $\omega_0 + \omega_v$ (**anti-Stokes**), asalkan $(\partial\alpha/\partial Q)_0 \ne 0$. Gambaran klasik ini memberikan aturan seleksi kasar dengan benar, tetapi meramalkan intensitas Stokes dan anti-Stokes yang sama, yang keliru. Mekanika kuantum memperbaikinya: garis anti-Stokes berasal dari molekul yang sudah berada di tingkat getaran tereksitasi, yang populasinya kecil.

### Gambaran kuantum

Dalam bahasa kuantum, hamburan Raman adalah proses dua foton: molekul menyerap foton laser dan sekaligus memancarkan foton terhambur, melalui **keadaan maya** yang bukan keadaan stasioner molekul. Intensitas hamburan sebanding dengan pangkat empat frekuensi cahaya terhambur dan dengan populasi tingkat awal, sehingga

$$
\frac{I_\text{anti-Stokes}}{I_\text{Stokes}} = \left(\frac{\tilde\nu_0 + \tilde\nu_v}{\tilde\nu_0 - \tilde\nu_v}\right)^4e^{-hc\tilde\nu_v/kT} . \qquad \text{(15.25)}
$$

Hamburan Raman sangat lemah: sekitar satu dari $10^6$–$10^8$ foton terhambur, dan hanya sebagian kecil dari yang terhambur yang bergeser frekuensinya. Karena itu spektroskopi Raman baru menjadi teknik rutin setelah laser tersedia.

![Gambar 15.4 (a) Diagram tingkat energi untuk serapan IR, hamburan Rayleigh, Stokes, dan anti-Stokes; garis putus-putus adalah keadaan maya. (b) Spektrum Raman CCl₄ yang dihitung untuk eksitasi 532 nm pada 298 K, dengan sisi anti-Stokes yang makin lemah untuk geseran besar. Intensitas relatif garis Stokes mengikuti pengamatan.](fig/c_raman.png){width=94%}

### Aturan seleksi dan larangan bersama

Polarisabilitas sebenarnya adalah tensor: dipol induksi tidak selalu sejajar medan. Komponen tensor $\alpha_{ij}$ bertransformasi seperti hasil kali koordinat $x^2$, $y^2$, $z^2$, $xy$, $xz$, $yz$. Akibatnya aturan seleksi Raman: **mode aktif Raman bila kesetangkupannya sama dengan salah satu fungsi kuadrat**, yang biasanya tercantum di kolom kanan tabel karakter (subbab 10.9). Untuk molekul berpusat inversi, fungsi kuadrat semuanya genap ($g$), sedangkan $x$, $y$, $z$ semuanya ganjil ($u$). Maka berlaku **aturan larangan bersama**:

> Dalam molekul berpusat inversi, tidak ada mode yang aktif IR dan aktif Raman sekaligus.

CO₂ adalah contoh baku: ulur simetris ($\sigma_g^+$) hanya aktif Raman, tekuk ($\pi_u$) dan ulur asimetris ($\sigma_u^+$) hanya aktif IR. Untuk SF₆ (Tabel 15.1), dua mode aktif IR ($t_{1u}$), tiga mode aktif Raman ($a_{1g}$, $e_g$, $t_{2g}$), dan satu mode ($t_{2u}$) tidak aktif sama sekali. Bila suatu molekul memperlihatkan pita yang sama di IR dan Raman, molekul itu pasti tidak berpusat inversi. Uji sederhana ini dipakai untuk membedakan, misalnya, isomer trans (berpusat inversi) dan cis kompleks atau alkena.

### Rasio depolarisasi

Bila laser terpolarisasi linear, cahaya Raman terhambur sebagian terpolarisasi sejajar dan sebagian tegak lurus polarisasi laser. **Rasio depolarisasi** $\rho = I_\perp/I_\parallel$ dinyatakan dengan dua invarian tensor turunan polarisabilitas, rata-ratanya $a$ dan anisotropinya $\gamma$:

$$
\rho = \frac{3\gamma^2}{45a^2 + 4\gamma^2} . \qquad \text{(15.26)}
$$

Untuk mode yang tidak bersetangkup penuh, $a = 0$ karena kesetangkupan, sehingga $\rho = \tfrac34$ (**terdepolarisasi**). Untuk mode bersetangkup penuh, $a \ne 0$ dan $0 \le \rho < \tfrac34$ (**terpolarisasi**); untuk mode yang sangat setangkup seperti ulur napas CCl₄, $\rho$ mendekati nol. Rasio depolarisasi dengan demikian mengenali mode bersetangkup penuh tanpa perhitungan apa pun.

::: {.contoh}
**Contoh 15.25 · Spektrum Raman CCl₄**

CCl₄ ($T_d$) mempunyai mode di 218 ($e$), 314 ($t_2$), 459 ($a_1$), dan sekitar 776 cm⁻¹ ($t_2$, pasangan resonansi Fermi 762/790). Dengan laser 532 nm pada 298 K: (a) hitung panjang gelombang garis Stokes dan anti-Stokes 459 cm⁻¹; (b) hitung perbandingan anti-Stokes/Stokes untuk keempat mode; (c) ramalkan rasio depolarisasi.

**Penyelesaian.** (a) $\tilde\nu_0 = 18\,797$ cm⁻¹. Stokes $18\,338$ cm⁻¹ = 545,3 nm; anti-Stokes $19\,256$ cm⁻¹ = 519,3 nm. (b) Dengan (15.25): 218 cm⁻¹: 0,38; 314: 0,25; 459: 0,13; 776: 0,033. (c) Mode 459 ($a_1$) terpolarisasi, $\rho \approx 0$; mode lain terdepolarisasi, $\rho = 0{,}75$.

**Memahami hasil.** Semua mode CCl₄ aktif Raman (fungsi kuadrat dalam $T_d$ bertransformasi sebagai $a_1$, $e$, dan $t_2$), dan hanya dua mode $t_2$ yang juga aktif IR: CCl₄ tidak berpusat inversi, sehingga larangan bersama tidak berlaku. Garis 459 cm⁻¹ yang kuat dan terpolarisasi sempurna adalah mode "napas" ketika keempat atom klorin bergerak serentak menjauhi karbon. CCl₄ dipakai sebagai sampel kalibrasi spektrometer Raman, dan perbandingan anti-Stokes/Stokes-nya dipakai sebagai termometer lokal di mikroskop Raman.
:::

::: {.contoh}
**Contoh 15.26 · Larangan bersama dan struktur**

Senyawa X₂Y₂ dapat berbentuk trans planar ($C_{2h}$) atau cis planar ($C_{2v}$). Spektrum IR dan Ramannya masing-masing memperlihatkan tiga pita yang semuanya pada frekuensi berbeda. Struktur mana yang lebih mungkin?

**Penyelesaian.** Struktur trans ($C_{2h}$) mempunyai pusat inversi; modenya terbagi menjadi $a_g$ dan $b_g$ (hanya Raman) serta $a_u$ dan $b_u$ (hanya IR). Struktur cis ($C_{2v}$) tidak mempunyai pusat inversi; mode $a_1$, $b_1$, dan $b_2$ aktif di keduanya. Karena tidak ada pita yang berimpit, struktur trans lebih mungkin.

**Memahami hasil.** Molekul N₂F₂, misalnya, ada dalam kedua bentuk dan dapat dibedakan dengan cara ini. Larangan bersama hanya mengizinkan kesimpulan satu arah: adanya pita yang berimpit membuktikan tidak ada pusat inversi; tidak adanya pita yang berimpit hanya menyarankan adanya pusat inversi, karena pita yang lemah atau tumpang tindih dapat terlewat.
:::

### Raman resonansi dan SERS

Bila frekuensi laser mendekati serapan elektronik molekul, keadaan maya digantikan keadaan elektronik nyata, dan intensitas mode yang "berkaitan" dengan transisi elektronik itu meningkat $10^3$–$10^6$ kali. Inilah **Raman resonansi**. Mode yang diperkuat adalah mode yang menggeser geometri molekul ke arah geometri keadaan tereksitasi, sehingga spektrumnya selektif: dalam protein hem, hanya mode porfirin yang terlihat, tanpa gangguan ribuan mode protein lainnya. Pada β-karotena, pita ulur C=C (sekitar 1520 cm⁻¹) dan C–C (sekitar 1157 cm⁻¹) sangat kuat dengan eksitasi biru-hijau.

Molekul yang teradsorpsi pada permukaan perak atau emas berstruktur nano memberikan **hamburan Raman yang diperkuat permukaan** (SERS), dengan penguatan $10^6$–$10^{10}$. Penyebab utamanya adalah resonansi plasmon permukaan logam: medan listrik lokal di celah antarpartikel nano dapat seratus kali lebih kuat daripada medan laser, dan karena hamburan Raman melibatkan medan dua kali (eksitasi dan pancaran), penguatannya kira-kira pangkat empat medan lokal: $100^4 = 10^8$. Dengan SERS, spektrum Raman satu molekul tunggal dapat diamati.

::: {.contoh}
**Contoh 15.27 · Air: lemah di Raman, kuat di IR**

Air adalah pelarut yang sangat buruk untuk spektroskopi IR (serapannya menutupi sebagian besar spektrum), tetapi pelarut yang baik untuk Raman. Jelaskan dengan perubahan momen dipol dan polarisabilitas.

**Penyelesaian.** Air sangat polar dan getaran O–H mengubah momen dipol besar-besaran, sehingga $(\partial\mu/\partial Q)$ besar dan serapan IR-nya sangat kuat. Polarisabilitas air kecil (molekul kecil dengan elektron yang terikat kuat oleh oksigen) dan berubah sedikit selama getaran, sehingga $(\partial\alpha/\partial Q)$ kecil dan hamburan Ramannya lemah.

**Memahami hasil.** Sebaliknya, molekul dengan elektron yang mudah terpolarisasi dan ikatan rangkap atau cincin aromatik (C=C, C≡C, S–S, cincin benzena) memberikan pita Raman kuat. Karena itu spektroskopi Raman ideal untuk sampel biologis berair, untuk membedakan polimorf obat dalam tablet, dan untuk bahan karbon: grafena dikenali dari pita G (sekitar 1580 cm⁻¹) dan 2D (sekitar 2700 cm⁻¹), yang bentuk dan perbandingannya menunjukkan berapa lapisan grafena yang ada. IR dan Raman saling melengkapi; keduanya bersama-sama memberi gambaran getaran yang utuh.
:::

::: {.kuis}
**Kuis cepat 15.6**

Mode mana dari SF₆ yang tidak dapat diamati baik dengan IR maupun Raman? Bagaimana frekuensinya dapat ditentukan?
:::
