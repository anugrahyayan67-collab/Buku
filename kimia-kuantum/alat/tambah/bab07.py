import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import sisip, soal
N = 7
sisip(N, '7.1', r'''
### Massa tereduksi: hidrogen, deuterium, positronium, hidrogen muonik

Dalam satuan atom kita menganggap inti tak bermassa hingga, sehingga massa tereduksi $\mu$ sama dengan massa elektron. Kenyataannya $\mu = m_eM/(m_e + M)$, dan semua energi serta jari-jari ikut berskala: energi sebanding dengan $\mu$, jari-jari sebanding dengan $1/\mu$. Koreksi ini kecil untuk hidrogen biasa (sekitar 0,05%), tetapi teramati dengan jelas dalam spektroskopi, dan menjadi besar untuk "atom" yang intinya ringan atau partikel pengorbitnya berat.

::: {.contoh}
**Contoh 7.t1 · Empat atom mirip hidrogen**

Hitung energi ionisasi (eV) untuk (a) hidrogen, (b) deuterium, (c) positronium (elektron yang mengorbit positron, $M = m_e$), dan (d) hidrogen muonik (muon bermassa $206{,}77\,m_e$ yang mengorbit proton). Untuk (d) hitung juga jari-jari Bohr-nya. Pakai $E_\infty = 13{,}6057$ eV dan $a_0 = 52{,}918$ pm untuk inti tak hingga berat.

**Penyelesaian.** Energi ionisasi $= E_\infty\,\mu/m_e$ dan jari-jari $= a_0\,m_e/\mu$.

(a) $\mu/m_e = 1/(1 + 1/1836{,}15) = 0{,}999\,456$, sehingga $E_i = 13{,}598$ eV.

(b) Deuteron $3670{,}5\,m_e$: $\mu/m_e = 0{,}999\,728$, $E_i = 13{,}602$ eV.

(c) $\mu = m_e/2$: $E_i = 6{,}80$ eV, dan jari-jarinya dua kali jari-jari Bohr.

(d) $\mu/m_e = 206{,}77 \times 1836{,}15/(206{,}77 + 1836{,}15) = 185{,}84$: $E_i = 2{,}53$ keV dan jari-jari $52{,}918\ \text{pm}/185{,}84 = 0{,}285$ pm $= 285$ fm.

**Memahami hasil.** Selisih H dan D hanya 0,004 eV, tetapi pada spektrometer resolusi tinggi selisih ini memisahkan garis-garis spektrum keduanya; dari situlah deuterium ditemukan pada tahun 1932. Positronium berukuran dua kali hidrogen dan terikat setengah lebih lemah. Hidrogen muonik 186 kali lebih kecil: muonnya mengorbit begitu dekat sehingga merasakan ukuran proton (0,84 fm), dan pengukuran spektrumnya pada tahun 2010 justru memberi jari-jari proton yang paling teliti.
:::
''', 'Empat atom mirip hidrogen')
sisip(N, '7.4', r'''
::: {.contoh}
**Contoh 7.t2 · Penemuan deuterium dari geseran isotop**

Konstanta Rydberg untuk inti bermassa $M$ adalah $R_M = R_\infty\,\mu/m_e$, dengan $R_\infty = 109\,737{,}3$ cm⁻¹. Hitung panjang gelombang (dalam vakum) garis H$_\alpha$ ($n = 3 \to 2$) untuk hidrogen dan deuterium, serta selisihnya.

**Penyelesaian.** $R_\text{H} = 109\,677{,}6$ cm⁻¹ dan $R_\text{D} = 109\,707{,}4$ cm⁻¹. Untuk H$_\alpha$, $\tilde\nu = R_M(\tfrac14 - \tfrac19) = \tfrac{5}{36}R_M$:

$$
\lambda_\text{H} = \frac{36}{5R_\text{H}} = 656{,}470\ \text{nm}, \qquad \lambda_\text{D} = \frac{36}{5R_\text{D}} = 656{,}291\ \text{nm}.
$$

Selisihnya 0,179 nm.

**Memahami hasil.** Harold Urey mencari garis lemah yang bergeser sekitar 0,18 nm ke arah biru dari H$_\alpha$ pada contoh hidrogen yang dipekatkan dengan penguapan, dan menemukannya. Geseran sebesar ini mudah dipisahkan oleh spektrograf kisi, sehingga satu rumus massa tereduksi menghasilkan Hadiah Nobel Kimia 1934. Prinsip yang sama dipakai sekarang untuk mengukur perbandingan isotop dalam air dan senyawa organik.
:::
''', 'Penemuan deuterium dari geseran isotop')
sisip(N, '7.5', r'''
::: {.terapan}
**Kaitan kimia · Mengapa nilai di inti penting**

Hanya orbital s yang tidak nol di inti. Besaran $|\psi(0)|^2$ muncul langsung dalam beberapa pengukuran kimia. **Kopling hiperhalus kontak Fermi** dalam ESR dan **kopling spin–spin** dalam NMR sebanding dengan rapat elektron s di inti; itulah sebabnya karakter s suatu ikatan (subbab 12.7) terbaca dari tetapan kopling ¹³C–H. **Geseran isomer Mössbauer** pada besi mengukur rapat elektron s di inti besi, dan dipakai untuk membedakan Fe(II) dari Fe(III). Garis 21 cm hidrogen antarbintang (1420 MHz), yang dipakai astronom untuk memetakan galaksi, juga berasal dari interaksi kontak elektron 1s dengan proton.
:::
''', 'Mengapa nilai di inti penting')
sisip(N, '7.6', r'''
::: {.contoh}
**Contoh 7.t3 · Seberapa sering elektron 1s berada di dalam inti?**

Peluang menemukan elektron 1s di dalam bola berjari-jari $r_0$ adalah $P(r_0) = 1 - e^{-x}(1 + x + x^2/2)$ dengan $x = 2r_0/a_0$. Hitung peluang itu untuk (a) $r_0 = a_0$, (b) $r_0 = 2a_0$, dan (c) $r_0$ = jari-jari proton, 0,84 fm.

**Penyelesaian.**

(a) $x = 2$: $P = 1 - e^{-2}(1 + 2 + 2) = 0{,}323$.

(b) $x = 4$: $P = 1 - e^{-4}(1 + 4 + 8) = 0{,}762$.

(c) $x = 2(0{,}84 \times 10^{-15})/(5{,}29 \times 10^{-11}) = 3{,}2 \times 10^{-5}$. Untuk $x$ kecil, $P \approx x^3/6 = \tfrac43(r_0/a_0)^3 = 5{,}3 \times 10^{-15}$.

**Memahami hasil.** Walaupun jari-jari paling mungkin adalah $a_0$, hanya sepertiga waktu elektron berada di dalam $a_0$; lebih dari 20% waktunya berada di luar $2a_0$. Peluang di dalam proton hanya $5 \times 10^{-15}$, tetapi tidak nol. Peluang kecil inilah yang memungkinkan **tangkapan elektron**: inti yang kaya proton, seperti ⁷Be atau ⁴⁰K, menangkap elektron 1s-nya sendiri dan berubah menjadi unsur lain.
:::
''', 'Seberapa sering elektron 1s berada di dalam inti')
sisip(N, '7.8', r'''
::: {.contoh}
**Contoh 7.t4 · Kerucut simpul orbital $d_{z^2}$**

Bagian sudut orbital $3d_{z^2}$ sebanding dengan $3\cos^2\theta - 1$. Pada sudut berapa terdapat bidang simpul (berbentuk kerucut)? Mengapa bentuk ini penting dalam senyawa kompleks oktahedral?

**Penyelesaian.** Simpul terjadi bila $3\cos^2\theta - 1 = 0$, yaitu $\cos\theta = \pm1/\sqrt3$, $\theta = 54{,}74°$ dan $125{,}26°$. Dua kerucut simpul memisahkan dua cuping di sumbu $z$ (bertanda positif) dari "cincin" di bidang $xy$ (bertanda negatif).

**Memahami hasil.** Sudut 54,74° adalah separuh sudut tetrahedral (109,47°), dan disebut juga "sudut ajaib" dalam NMR padatan, karena kopling dipol antarinti sebanding dengan faktor $3\cos^2\theta - 1$ yang sama. Dalam kompleks oktahedral, cuping $d_{z^2}$ mengarah tepat ke dua ligan di sumbu $z$, sehingga orbital ini (bersama $d_{x^2 - y^2}$) naik energinya oleh tolakan ligan (Bab 14).
:::
''', 'Kerucut simpul orbital')
sisip(N, '7.9', r'''
::: {.contoh}
**Contoh 7.t5 · Ukuran dan sebaran orbital kulit $n = 2$ dan $n = 3$**

Dengan $\langle r\rangle = \tfrac12[3n^2 - \ell(\ell + 1)]$ dan $\langle r^2\rangle = \tfrac12n^2[5n^2 + 1 - 3\ell(\ell + 1)]$ (satuan bohr), hitung $\langle r\rangle$ dan sebaran $\Delta r = \sqrt{\langle r^2\rangle - \langle r\rangle^2}$ untuk 2s, 2p, 3s, 3p, dan 3d.

**Penyelesaian.**

| Orbital | $\langle r\rangle$ | $\langle r^2\rangle$ | $\Delta r$ |
|---|---|---|---|
| 2s | 6,0 | 42 | 2,45 |
| 2p | 5,0 | 30 | 2,24 |
| 3s | 13,5 | 207 | 4,97 |
| 3p | 12,5 | 180 | 4,87 |
| 3d | 10,5 | 126 | 3,97 |

**Memahami hasil.** Dalam satu kulit, orbital dengan $\ell$ lebih besar rata-rata **lebih dekat** ke inti dan lebih sempit sebarannya, walaupun energinya sama dalam hidrogen. Orbital s menyebar paling luas karena punya simpul-simpul radial dan cuping kecil di dekat inti. Dalam atom berelektron banyak, cuping dalam itulah yang menembus kulit dalam (subbab 7.6) dan menurunkan energi orbital s di bawah p dan d.
:::
''', 'Ukuran dan sebaran orbital kulit')
sisip(N, '7.10', r'''
::: {.contoh}
**Contoh 7.t6 · Deret Pickering: ion helium yang menyamar sebagai hidrogen**

Pada tahun 1896 Edward Pickering menemukan dalam spektrum bintang panas deret garis yang mirip deret Balmer, tetapi dengan garis tambahan di antaranya. Garis itu berasal dari He⁺ ($Z = 2$) untuk transisi $n \to 4$. Dengan $R_\text{He} = 109\,722{,}3$ cm⁻¹, hitung panjang gelombang transisi $6 \to 4$, $8 \to 4$, dan $5 \to 4$, lalu bandingkan dengan garis Balmer hidrogen (656,47; 486,27; dan 434,17 nm dalam vakum).

**Penyelesaian.** $\tilde\nu = Z^2R_\text{He}(\tfrac1{16} - \tfrac1{n^2}) = 4R_\text{He}(\tfrac1{16} - \tfrac1{n^2})$.

$6 \to 4$: 656,20 nm. $8 \to 4$: 486,08 nm. $5 \to 4$: 1012,7 nm.

**Memahami hasil.** Untuk $n$ genap, $4(\tfrac1{16} - \tfrac1{(2m)^2}) = \tfrac14 - \tfrac1{m^2}$, persis rumus Balmer; garis He⁺ hanya berbeda sedikit karena massa tereduksinya lebih besar, dan karena itu bergeser sekitar 0,27 nm ke arah biru. Untuk $n$ ganjil muncul garis yang tidak ada pada hidrogen. Mula-mula Pickering mengira menemukan bentuk hidrogen baru; Bohr pada 1913 menunjukkan bahwa garis itu milik He⁺, dan ramalan geseran kecil ini menjadi salah satu kemenangan pertama teorinya.
:::

::: {.terapan}
**Kaitan kimia · Atom Rydberg**

Atom yang elektronnya tereksitasi ke $n$ sangat besar disebut **atom Rydberg**. Untuk $n = 100$, jari-jari orbitnya $n^2a_0 \approx 0{,}53$ μm, sebesar bakteri kecil, dan energi ikatnya hanya 1,4 meV, jauh di bawah energi termal pada suhu kamar (26 meV). Atom seperti ini sangat peka terhadap medan listrik dan saling berinteraksi dari jarak mikrometer; kini atom Rydberg dari rubidium dan cesium dipakai sebagai qubit dalam komputer kuantum dan sebagai sensor medan listrik gelombang mikro.
:::
''', 'Deret Pickering')
sisip(N, '7.11', r'''
::: {.contoh}
**Contoh 7.t7 · Batas deret dan garis inframerah**

Dengan $R_\text{H} = 109\,677{,}6$ cm⁻¹, hitung (a) batas deret Lyman dan deret Balmer, (b) panjang gelombang garis pertama deret Paschen ($4 \to 3$). Di daerah spektrum mana masing-masing berada?

**Penyelesaian.**

(a) Batas Lyman: $\lambda = 1/R_\text{H} = 91{,}18$ nm (ultraviolet jauh). Batas Balmer: $\lambda = 4/R_\text{H} = 364{,}7$ nm (ultraviolet dekat).

(b) Paschen α: $\tilde\nu = R_\text{H}(\tfrac19 - \tfrac1{16}) = 5331{,}6$ cm⁻¹, $\lambda = 1{,}876$ μm (inframerah dekat).

**Memahami hasil.** Foton yang lebih pendek dari 91,2 nm dapat mengionkan hidrogen dari keadaan dasar; karena itu ruang antarbintang di sekitar bintang panas dipenuhi hidrogen terionisasi, dan cahaya ultraviolet jauh dari galaksi jauh hampir seluruhnya terserap. Di bawah batas Balmer, spektrum bintang menunjukkan lompatan serapan (lompatan Balmer) yang dipakai astronom untuk mengukur suhu bintang.
:::
''', 'Batas deret dan garis inframerah')
sisip(N, '7.12', r'''
::: {.contoh}
**Contoh 7.t8 · Seberapa besar pemecahan Zeeman?**

Dalam efek Zeeman normal, tingkat $m_\ell$ terpisah sebesar $\mu_BB$. Hitung pemecahan itu untuk $B = 1{,}0$ T dalam cm⁻¹ dan GHz, dan geseran panjang gelombang garis H$_\alpha$ (656,3 nm) yang bersesuaian.

**Penyelesaian.** $\mu_BB = 9{,}274 \times 10^{-24}$ J. Dalam bilangan gelombang: $\mu_BB/hc = 0{,}467$ cm⁻¹; dalam frekuensi: 14,0 GHz. Geseran panjang gelombang:

$$
\Delta\lambda = \frac{\lambda^2\,\Delta E}{hc} = \frac{(656{,}3 \times 10^{-9})^2(9{,}274 \times 10^{-24})}{(6{,}626 \times 10^{-34})(2{,}998 \times 10^8)} = 2{,}0 \times 10^{-11}\ \text{m} = 0{,}020\ \text{nm}.
$$

**Memahami hasil.** Medan 1 T, sekuat magnet laboratorium yang besar, menggeser garis tampak hanya 0,02 nm, sepersepuluh geseran isotop H/D. Karena itu efek Zeeman memerlukan spektrograf beresolusi tinggi. Sebaliknya, pemecahan 14 GHz ini persis berada di daerah gelombang mikro, dan itulah dasar spektroskopi ESR (Bab 16): alih-alih mengukur geseran garis optik yang kecil, ESR mengukur langsung transisi antartingkat Zeeman.
:::
''', 'Seberapa besar pemecahan Zeeman')
soal(N, '7.1', [r'Hitung energi ionisasi (eV) dan jari-jari Bohr (pm) atom "muonium", yaitu elektron yang mengorbit muon positif ($m_\mu = 206{,}77\,m_e$). ||| 13,54 eV; 53,17 pm'])
soal(N, '7.4', [r'Hitung panjang gelombang (vakum) garis Lyman α ($2 \to 1$) untuk H dan D. Berapa selisihnya? ||| 121,568 nm; 121,535 nm; 0,033 nm',
                r'Tritium mempunyai inti bermassa $5496{,}9\,m_e$. Hitung konstanta Rydberg-nya dan panjang gelombang H$_\alpha$-nya (vakum). ||| 109 717,4 cm⁻¹; 656,231 nm'])
soal(N, '7.6', [r'Hitung peluang elektron 1s berada di luar $3a_0$. ||| 0,062',
                r'Hitung peluang elektron 2p berada di dalam $a_0$, dengan $P(r < r_0) = 1 - e^{-x}(1 + x + x^2/2 + x^3/6 + x^4/24)$ dan $x = r_0/a_0$. ||| 0,0037'])
soal(N, '7.8', [r'Pada sudut $\theta$ berapa bagian sudut orbital $f_{z^3} \propto 5\cos^3\theta - 3\cos\theta$ bernilai nol? ||| 39,2°; 90°; 140,8°'])
soal(N, '7.9', [r'Hitung $\langle r\rangle$ dan $\Delta r$ untuk orbital 4f. Bandingkan $\langle r\rangle$ dengan 4s. ||| 18; 6,0; 4s: 24'])
soal(N, '7.10', [r'Berapa energi ionisasi Li²⁺ (eV), termasuk koreksi massa tereduksi ($M = 12\,786\,m_e$)? ||| 122,44 eV',
                 r'Hitung jari-jari orbit (μm) dan energi ikat (meV) atom Rydberg hidrogen dengan $n = 50$. ||| 0,132 μm; 5,44 meV'])
soal(N, '7.11', [r'Hitung batas deret Paschen dan panjang gelombang garis Brackett α ($5 \to 4$). ||| 820,6 nm; 4,05 μm'])
soal(N, '7.12', [r'Berapa medan magnet yang diperlukan agar pemecahan Zeeman normal sama dengan $k_BT$ pada 4 K? ||| 5,95 T',
                 r'Spektrometer ESR pita X bekerja pada 9,5 GHz. Berapa medan resonansi untuk elektron bebas ($g = 2{,}0023$, $\Delta E = g\mu_BB$)? ||| 0,339 T'])
print('selesai')
