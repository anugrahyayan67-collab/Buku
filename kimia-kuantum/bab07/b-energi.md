## 7.4 Tingkat energi dan degenerasi

### Tangga Coulomb

Menurut (7.10), tingkat energi atom hidrogen ($Z = 1$) adalah $-\tfrac12$, $-\tfrac18$, $-\tfrac1{18}$, ... hartree, atau $-13{,}6$; $-3{,}40$; $-1{,}51$; ... eV. Berbeda dengan osilator (berjarak sama) dan rotor (makin renggang), tingkat Coulomb makin **rapat** ke atas dan berkumpul di $E = 0$, batas ionisasi. Di atas batas itu, elektron tidak terikat dan energinya malar.

Dengan massa tereduksi, energi dikalikan $\mu/m_e$:

$$
E_n = -\frac{\mu}{m_e}\,\frac{Z^2}{2n^2}\,E_h . \qquad \text{(7.11)}
$$

Untuk hidrogen, $\mu/m_e = 0{,}999\,456$, sehingga energi ionisasi adalah $13{,}598$ eV, bukan $13{,}606$ eV.

### Degenerasi dan simetri tersembunyi

Untuk $n$ tertentu, $\ell$ dapat bernilai $0, 1, \ldots, n - 1$, dan untuk setiap $\ell$ ada $2\ell + 1$ nilai $m$. Banyaknya orbital berenergi sama adalah

$$
g_n = \sum_{\ell=0}^{n-1}(2\ell + 1) = n^2 . \qquad \text{(7.12)}
$$

Degenerasi terhadap $m$ dimiliki setiap potensial sentral (simetri bola). Tetapi degenerasi terhadap $\ell$, yang membuat 2s dan 2p berenergi sama, adalah khas potensial $1/r$. Persamaan radial (7.6) memang bergantung pada $\ell$; bahwa energinya tidak bergantung pada $\ell$ adalah "kebetulan" yang ternyata bersumber dari simetri tersembunyi: dalam masalah Kepler klasik, selain momentum sudut, ada vektor Runge–Lenz yang juga kekal (itulah sebabnya orbit planet berbentuk elips tertutup yang tidak berpresesi). Versi kuantum vektor ini komut dengan $\hat H$ dan menghubungkan keadaan dengan $\ell$ berbeda.

Simetri ini rapuh. Begitu potensial menyimpang dari $1/r$ murni, degenerasi $\ell$ pecah. Dalam atom berelektron banyak, elektron lain menyaring muatan inti sehingga potensial efektif tidak lagi $1/r$, dan orbital yang lebih "menembus" ke dekat inti (s) lebih rendah daripada yang kurang menembus (p, d). Di atom hidrogen sendiri, efek relativistik (struktur halus) dan elektrodinamika kuantum (pergeseran Lamb) memecah degenerasi itu sedikit sekali.

::: {.contoh}
**Contoh 7.10 · Garis-garis utama hidrogen**

Dengan $R_H = 109\,677{,}6$ cm⁻¹ ($= R_\infty\mu/m_e$), hitung panjang gelombang vakum garis Lyman-α ($2 \to 1$), Lyman-β ($3 \to 1$), H$_\alpha$ ($3 \to 2$), H$_\beta$ ($4 \to 2$), dan Paschen-α ($4 \to 3$).

**Penyelesaian.** $1/\lambda = R_H(1/n_1^2 - 1/n_2^2)$. Lyman-α: $1/[R_H(3/4)] = 121{,}57$ nm. Lyman-β: 102,57 nm. H$_\alpha$: $1/[R_H(5/36)] = 656{,}47$ nm. H$_\beta$: 486,27 nm. Paschen-α: 1875,6 nm.

**Memahami hasil.** Garis-garis Balmer (Gambar 7.4) yang tampak dalam foto nebula diukur di udara, yang indeks biasnya membuat panjang gelombang sedikit lebih pendek: H$_\alpha$ = 656,28 nm di udara. Perbedaan 0,19 nm ini sebesar pergeseran isotop deuterium (Contoh 6.27): spektroskopis harus selalu menyebut apakah panjang gelombangnya vakum atau udara.
:::

::: {.contoh}
**Contoh 7.11 · Atom Rydberg**

Untuk hidrogen dengan $n = 100$, hitung jarak rata-rata elektron ($\langle r\rangle \approx \tfrac32n^2a_0$), energi ikatnya, dan frekuensi transisi $100 \to 99$.

**Penyelesaian.** $\langle r\rangle = 1{,}5 \times 10^4\,a_0 = 0{,}79$ µm. Energi ikat $13{,}6/10^4 = 1{,}36$ meV. Transisi: $\Delta E = \tfrac12\left(\tfrac{1}{99^2} - \tfrac{1}{100^2}\right)E_h(\mu/m_e)$, frekuensi 6,68 GHz.

**Memahami hasil.** Atom Rydberg hampir sebesar bakteri, terikat sangat lemah, dan memancarkan gelombang radio. Di awan gas terionisasi di sekitar bintang muda, elektron yang bergabung kembali dengan proton menuruni tangga Rydberg dan memancarkan **garis rekombinasi radio**, misalnya H109α ($110 \to 109$) di 5,009 GHz, yang dipakai untuk memetakan daerah pembentukan bintang. Dalam laboratorium, atom Rydberg dengan dipol raksasanya dipakai sebagai sensor medan listrik dan sebagai qubit.
:::

::: {.contoh}
**Contoh 7.12 · Seberapa tepat degenerasi 2s–2p?**

Pada atom hidrogen sungguhan, tingkat $2p_{3/2}$ berada 10,97 GHz di atas $2p_{1/2}$ (struktur halus), dan $2s_{1/2}$ berada 1057,8 MHz di atas $2p_{1/2}$ (pergeseran Lamb). Nyatakan keduanya dalam cm⁻¹ dan eV, dan bandingkan dengan energi tingkat $n = 2$.

**Penyelesaian.** Struktur halus: $10{,}97 \times 10^9/2{,}998 \times 10^{10} = 0{,}366$ cm⁻¹ $= 4{,}5 \times 10^{-5}$ eV. Pergeseran Lamb: 0,0353 cm⁻¹ $= 4{,}37 \times 10^{-6}$ eV. Dibandingkan dengan 3,40 eV, keduanya berorde $10^{-5}$ dan $10^{-6}$.

**Memahami hasil.** Degenerasi $\ell$ benar sampai satu bagian dalam seratus ribu. Struktur halus (sebanding dengan $\alpha^2 = 5{,}3 \times 10^{-5}$) adalah efek relativistik dan spin–orbit (Bab 9). Pergeseran Lamb, yang diukur tahun 1947, tidak dapat dijelaskan oleh persamaan Dirac sekalipun dan memicu lahirnya elektrodinamika kuantum. Untuk kimia, energi (7.10) lebih dari cukup; untuk unsur berat, efek relativistik menjadi besar (Bab 9).
:::

::: {.contoh}
**Contoh 7.13 · Batas Balmer dan lompatan Balmer bintang**

Hitung panjang gelombang terpanjang yang dapat mengionisasi atom hidrogen dari $n = 2$. Mengapa spektrum bintang panas memperlihatkan penurunan intensitas yang tajam di bawah panjang gelombang ini?

**Penyelesaian.** $E = R_Hhc/4$, $\lambda = 4/R_H = 4/(109\,677{,}6\ \text{cm}^{-1}) = 364{,}7$ nm.

**Memahami hasil.** Di atmosfer bintang bersuhu sekitar 10 000 K, banyak atom hidrogen berada di $n = 2$. Foton dengan $\lambda < 364{,}7$ nm dapat mengionisasi atom-atom itu dan diserap kuat (serapan malar, bukan garis), sehingga spektrum bintang "melompat" turun di batas ini. Besarnya **lompatan Balmer** bergantung pada populasi $n = 2$ dan karena itu pada suhu dan tekanan atmosfer bintang; astronom memakainya untuk mengklasifikasi bintang.
:::

::: {.kuis}
**Kuis cepat 7.4**

Berapa degenerasi tingkat $n = 4$ (tanpa spin)? Berapa energi yang diperlukan untuk mengionisasi atom hidrogen dari $n = 3$?
:::

## 7.5 Fungsi radial dan simpul

### Menghitung simpul

Fungsi radial $R_{n\ell}$ mempunyai $n - \ell - 1$ **simpul radial**, yaitu akar polinom Laguerre berderajat $n - \ell - 1$. Harmonik bola $Y_\ell^m$ mempunyai $\ell$ **simpul sudut** (bidang atau kerucut, subbab 6.5). Jumlah semua simpul $n - 1$, seperti partikel dalam kotak (kotak satu dimensi: $n - 1$ simpul). Energi naik dengan jumlah simpul, karena setiap simpul tambahan menambah kelengkungan fungsi gelombang dan dengan itu energi kinetiknya.

| Orbital | 1s | 2s | 2p | 3s | 3p | 3d | 4s | 4p | 4d | 4f |
|---|---|---|---|---|---|---|---|---|---|---|
| simpul radial | 0 | 1 | 0 | 2 | 1 | 0 | 3 | 2 | 1 | 0 |
| simpul sudut | 0 | 0 | 1 | 0 | 1 | 2 | 0 | 1 | 2 | 3 |

Untuk $\ell$ tertentu, orbital dengan $n$ terendah ($n = \ell + 1$: 1s, 2p, 3d, 4f) tidak mempunyai simpul radial; fungsi radialnya sederhana, $R \propto r^{n-1}e^{-Zr/n}$.

### Nilai di inti

Dari Contoh 7.5, hanya orbital s yang tidak nol di inti. Dari tabel fungsi radial, $R_{n0}(0)$ memberi

$$
|\psi_{n00}(0)|^2 = \frac{Z^3}{\pi n^3} . \qquad \text{(7.13)}
$$

Rapat elektron di inti menurun cepat dengan $n$ dan naik sangat cepat dengan $Z$. Besaran ini menentukan interaksi hiperhalus, pergeseran isotop karena ukuran inti, dan laju penangkapan elektron.

![Gambar 7.2 Atas: fungsi radial $R_{n\ell}$ untuk $n = 1$, 2, 3 (satuan atom, $Z = 1$). Bawah: fungsi distribusi radial $r^2R_{n\ell}^2$; garis titik-titik menandai $\langle r\rangle$. Orbital 2s dan 3s mempunyai puncak kecil di dekat inti yang tidak dimiliki 2p dan 3d: inilah penembusan.](fig/c_radial.png){width=95%}

::: {.contoh}
**Contoh 7.14 · Letak simpul 3s**

Tentukan simpul radial orbital 3s hidrogen dalam bohr dan pm.

**Penyelesaian.** $27 - 18r + 2r^2 = 0$ memberi $r = \tfrac{18 \pm \sqrt{324 - 216}}{4} = \tfrac{9 \pm 3\sqrt3}{2}$: $r = 1{,}902$ dan $7{,}098$ bohr, yaitu 100,6 pm dan 375,6 pm.

**Memahami hasil.** Elektron 3s menempati tiga kulit konsentris yang dipisahkan dua permukaan bola tempat peluangnya nol. Simpul tidak menghalangi elektron "pindah" antarkulit, karena elektron tidak bergerak di sepanjang lintasan; fungsi gelombang adalah gelombang berdiri yang meliputi semua kulit sekaligus, seperti tali bergetar dengan simpul tidak "memisahkan" bagian-bagiannya.
:::

::: {.contoh}
**Contoh 7.15 · Normalisasi $R_{21}$**

Periksa bahwa $R_{21} = \tfrac{1}{2\sqrt6}re^{-r/2}$ ternormalisasi, dengan (2.8).

**Penyelesaian.** $\int_0^\infty R_{21}^2r^2dr = \tfrac{1}{24}\int_0^\infty r^4e^{-r}dr = \tfrac{1}{24}\cdot4! = 1$.

**Memahami hasil.** Hampir semua integral atom hidrogen bermuara pada $\int_0^\infty r^ne^{-ar}dr = n!/a^{n+1}$. Inilah alasan praktis mengapa orbital jenis Slater ($r^{n-1}e^{-\zeta r}$) begitu mudah diintegrasikan untuk satu pusat, meskipun integral antara dua pusat atom menjadi sulit, sehingga kimia komputasi beralih ke fungsi Gauss (Bab 17).
:::

::: {.contoh}
**Contoh 7.16 · Elektron di dalam proton**

Proton berjari-jari sekitar 0,84 fm. Hitung peluang elektron 1s hidrogen berada di dalam proton, dengan menganggap $|\psi|^2$ tetap bernilai $|\psi(0)|^2$ di dalam bola sekecil itu.

**Penyelesaian.** $|\psi_{1s}(0)|^2 = 1/\pi a_0^3$. Volume proton $\tfrac43\pi r_p^3$. Peluang $\tfrac43(r_p/a_0)^3 = \tfrac43(0{,}84 \times 10^{-15}/5{,}29 \times 10^{-11})^3 = 5{,}3 \times 10^{-15}$.

**Memahami hasil.** Peluangnya sangat kecil tetapi tidak nol. Karena elektron s "masuk" ke dalam inti, energi tingkat s sedikit bergantung pada ukuran inti; pergeseran ini, bersama spin inti, menghasilkan struktur hiperhalus, termasuk transisi garis 21 cm hidrogen yang memetakan gas hidrogen netral di seluruh galaksi. Pada atom berat ($Z$ besar), rapat elektron 1s di inti $Z^3$ kali lebih besar, dan inti dapat menangkap elektron 1s (peluruhan penangkapan elektron, misalnya ⁴⁰K → ⁴⁰Ar).
:::

::: {.kuis}
**Kuis cepat 7.5**

Berapa simpul radial dan sudut orbital 5d? Mengapa orbital 2p tidak mempunyai simpul radial meskipun $R_{21}(0) = 0$?
:::

## 7.6 Fungsi distribusi radial

### Peluang pada jarak tertentu

Peluang menemukan elektron dalam kulit bola berjari-jari $r$ dan tebal $dr$ adalah

$$
P(r)\,dr = \left[\int|\psi|^2r^2\sin\theta\,d\theta\,d\phi\right]dr = R_{n\ell}^2(r)\,r^2\,dr = u^2(r)\,dr , \qquad \text{(7.14)}
$$

karena harmonik bola ternormalisasi. $P(r)$ adalah **fungsi distribusi radial** (subbab 2.5). Ia nol di inti (kulit berjari-jari nol tidak bervolume) bahkan untuk orbital s, dan menuju nol jauh dari inti. Puncaknya adalah **jari-jari paling mungkin** $r_\text{mp}$. Untuk orbital tanpa simpul radial ($\ell = n - 1$), $P \propto r^{2n}e^{-2Zr/n}$, dan $dP/dr = 0$ memberi

$$
r_\text{mp} = \frac{n^2}{Z}\,a_0 \qquad (\ell = n - 1) . \qquad \text{(7.15)}
$$

Ini tepat jari-jari orbit Bohr. Model Bohr ternyata menyimpan sepotong kebenaran: jari-jari orbitnya adalah jarak paling mungkin untuk orbital "paling melingkar" 1s, 2p, 3d, 4f.

### Penembusan

Gambar 7.2 (bawah) memperlihatkan bahwa 2s mempunyai puncak kecil di dekat inti ($r < 2$) yang tidak dimiliki 2p, meskipun $\langle r\rangle$ 2s (6 bohr) lebih besar daripada 2p (5 bohr). Dengan kata lain, elektron 2s lebih sering **menembus** daerah dekat inti. Dalam atom hidrogen, ini tidak berpengaruh pada energi (degenerasi $\ell$). Dalam atom berelektron banyak, elektron dalam (1s²) menyaring muatan inti; elektron yang menembus ke dalam awan 1s merasakan muatan inti yang lebih besar dan terikat lebih kuat. Urutan penembusan s > p > d > f adalah urutan energi s < p < d < f dalam atom berelektron banyak, dan dengan itu, struktur tabel periodik (Bab 9).

::: {.contoh}
**Contoh 7.17 · Jari-jari paling mungkin 2p**

Turunkan $r_\text{mp}$ untuk 2p hidrogen.

**Penyelesaian.** $P(r) = r^2R_{21}^2 \propto r^4e^{-r}$. $dP/dr \propto (4r^3 - r^4)e^{-r} = 0$ memberi $r = 4$ bohr $= 211{,}7$ pm.

**Memahami hasil.** Sama dengan jari-jari orbit Bohr $n = 2$ ($n^2a_0$). Untuk 2s, puncak terbesar berada di 5,24 bohr dan ada puncak kecil di 0,76 bohr. Perhatikan bahwa $r_\text{mp}$, $\langle r\rangle$, dan "jari-jari atom" adalah tiga besaran berbeda; jari-jari atom yang diukur secara kimia (kovalen, van der Waals) tidak dapat diturunkan dari satu orbital saja.
:::

::: {.contoh}
**Contoh 7.18 · Seberapa besar atom hidrogen?**

Hitung peluang elektron 1s berada di dalam bola berjari-jari $a_0$, dan jari-jari bola yang memuat 90% dan 99% peluang.

**Penyelesaian.** $\int_0^R4r^2e^{-2r}dr = 1 - e^{-2R}(1 + 2R + 2R^2)$. Untuk $R = 1$: $1 - 5e^{-2} = 0{,}323$. Untuk 90% dan 99%, selesaikan secara numerik: $R = 2{,}66$ dan $4{,}20$ bohr (141 dan 222 pm).

**Memahami hasil.** Atom tidak mempunyai batas yang tajam; ukurannya bergantung pada definisi. Gambar "permukaan batas" orbital biasanya digambar pada kontur yang memuat 90% peluang. Jari-jari van der Waals hidrogen (sekitar 110–120 pm) dan jari-jari kovalennya (31–37 pm) masing-masing mencerminkan sisi berbeda dari awan elektron yang sama.
:::

::: {.contoh}
**Contoh 7.19 · Mengukur penembusan**

Hitung peluang elektron berada dalam jarak 1 bohr dari inti untuk 2s, 2p, 3s, 3p, dan 3d hidrogen.

**Penyelesaian.** Dengan integrasi $\int_0^1r^2R^2dr$: 2s 0,0343; 2p 0,00366; 3s 0,00987; 3p 0,00126; 3d $6{,}5 \times 10^{-6}$.

**Memahami hasil.** Pada $n = 2$, elektron s sembilan kali lebih sering berada dekat inti daripada elektron p. Pada $n = 3$, perbandingan s : p : d sekitar 1500 : 190 : 1. Dalam atom natrium, dengan teras 1s²2s²2p⁶ berjari-jari sekitar 1 bohr, elektron 3s menembus teras jauh lebih sering daripada 3p, dan 3p jauh lebih sering daripada 3d. Inilah sebabnya garis kuning natrium (3p → 3s) ada di 589 nm, sedangkan dalam hidrogen 3s dan 3p berenergi sama (subbab 7.13).
:::

::: {.contoh}
**Contoh 7.20 · Lobus dalam 2s**

Berapa peluang elektron 2s berada di dalam simpulnya ($r < 2$ bohr)? Bandingkan $\langle r\rangle$ dan $r_\text{mp}$ 2s.

**Penyelesaian.** $\int_0^2\tfrac18(2 - r)^2r^2e^{-r}dr = 0{,}053$. $\langle r\rangle_{2s} = 6$ bohr (subbab 7.9), sedangkan $r_\text{mp} = 3 + \sqrt5 = 5{,}24$ bohr (akar terbesar $dP/dr = 0$).

**Memahami hasil.** Hanya 5% peluang 2s berada di lobus dalam, tetapi itu cukup untuk membuat 2s terikat lebih kuat daripada 2p dalam litium: energi ionisasi Li (2s) 5,39 eV, sedangkan elektron 2p tereksitasi hanya terikat 3,54 eV. Sebagian kecil fungsi gelombang di daerah penting dapat menentukan sifat kimia.
:::

::: {.kuis}
**Kuis cepat 7.6**

Di mana $r_\text{mp}$ orbital 3d hidrogen? Orbital 4s atau 3d yang lebih menembus?
:::
