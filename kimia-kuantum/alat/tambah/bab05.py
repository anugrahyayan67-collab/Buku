import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import sisip, soal
N = 5
sisip(N, '5.2', r'''
::: {.contoh}
**Contoh 5.t1 · Skala panjang osilator HCl**

Untuk H³⁵Cl, $\tilde\nu = 2990{,}9$ cm⁻¹ dan $\mu = 0{,}9796$ u. Hitung tetapan gaya $k$, parameter $\alpha = \mu\omega/\hbar$, dan titik balik klasik $x_\text{tb} = \sqrt{(2v + 1)/\alpha}$ untuk $v = 0$ dan $v = 1$.

**Penyelesaian.** $\omega = 2\pi c\tilde\nu = 5{,}634 \times 10^{14}$ s⁻¹ dan $\mu = 1{,}6267 \times 10^{-27}$ kg.

$$
k = \mu\omega^2 = 516\ \text{N/m}, \qquad \alpha = \frac{\mu\omega}{\hbar} = 8{,}69 \times 10^{21}\ \text{m}^{-2}.
$$

Titik balik: $v = 0$, $x_\text{tb} = 1/\sqrt\alpha = 10{,}7$ pm; $v = 1$, $x_\text{tb} = \sqrt{3/\alpha} = 18{,}6$ pm.

**Memahami hasil.** Satuan panjang alami osilator, $1/\sqrt\alpha$, hanya sekitar 11 pm, kurang dari sepersepuluh panjang ikatan HCl (127,5 pm). Getaran titik nol menggoyang ikatan sekitar ±8%. Karena itu pendekatan harmonik cukup baik untuk tingkat-tingkat rendah, dan variabel tak berdimensi $y = \sqrt\alpha\,x$ membuat persamaan berlaku untuk semua molekul sekaligus.
:::
''', 'Skala panjang osilator HCl')
sisip(N, '5.3', r'''
::: {.contoh}
**Contoh 5.t2 · Membangun $H_3$ dan $H_4$ dari rekursi**

Polinom Hermite memenuhi $H_{v+1}(y) = 2yH_v(y) - 2vH_{v-1}(y)$ dengan $H_0 = 1$ dan $H_1 = 2y$. Bangun $H_2$, $H_3$, dan $H_4$, lalu periksa paritas dan banyak akarnya.

**Penyelesaian.**

$H_2 = 2y(2y) - 2(1)(1) = 4y^2 - 2$.

$H_3 = 2y(4y^2 - 2) - 2(2)(2y) = 8y^3 - 12y$.

$H_4 = 2y(8y^3 - 12y) - 2(3)(4y^2 - 2) = 16y^4 - 48y^2 + 12$.

$H_v$ genap bila $v$ genap dan ganjil bila $v$ ganjil. $H_3$ berakar di $y = 0$, $\pm\sqrt{3/2}$ (tiga akar); $H_4$ berakar di $y^2 = (3 \pm \sqrt6)/2$, yaitu $y = \pm0{,}525$ dan $\pm1{,}651$ (empat akar).

**Memahami hasil.** Keadaan ke-$v$ mempunyai tepat $v$ simpul, seperti partikel dalam kotak, dan paritasnya bergantian. Paritas inilah yang menyebabkan aturan seleksi $\Delta v = \pm1$: momen dipol transisi $\langle v'|x|v\rangle$ hanya tidak nol bila $v$ dan $v'$ berbeda paritas, dan sifat tangga (subbab 5.6) membatasinya lebih jauh menjadi selisih tepat satu.
:::
''', 'Membangun $H_3$ dan $H_4$')
sisip(N, '5.5', r'''
::: {.contoh}
**Contoh 5.t3 · Seberapa jauh osilator menembus daerah terlarang?**

Hitung peluang osilator berada di luar titik balik klasiknya untuk $v = 0$ dan $v = 1$. Untuk $v = 0$, $P = \operatorname{erfc}(1)$; untuk $v = 1$, $P = \operatorname{erfc}(\sqrt3) + \tfrac{2\sqrt3}{\sqrt\pi}e^{-3}$.

**Penyelesaian.** $v = 0$: $P = 0{,}157$. $v = 1$: $P = 0{,}0143 + 0{,}0975 = 0{,}112$.

**Memahami hasil.** Pada keadaan dasar, hampir 16% waktu molekul berada di jarak yang secara klasik terlarang, dan peluang itu menurun perlahan dengan $v$. Penembusan seperti ini mendasari penerobosan atom hidrogen dalam reaksi transfer proton dan inversi amonia (subbab 3.12): fungsi gelombang yang "bocor" ke daerah terlarang dapat menyambung ke sumur di seberangnya.
:::
''', 'Seberapa jauh osilator menembus daerah terlarang')
sisip(N, '5.6', r'''
::: {.contoh}
**Contoh 5.t4 · Simpangan rms dengan operator tangga**

Dengan $\hat x = (\hat a + \hat a^\dagger)/\sqrt{2\alpha}$, hitung $\langle v|\hat x^2|v\rangle$ tanpa integral, lalu nilai rms simpangan HCl untuk $v = 0$ dan $v = 1$ ($\alpha = 8{,}69 \times 10^{21}$ m⁻²).

**Penyelesaian.** $\hat x^2 = (\hat a^2 + \hat a\hat a^\dagger + \hat a^\dagger\hat a + \hat a^{\dagger2})/2\alpha$. Suku $\hat a^2$ dan $\hat a^{\dagger2}$ mengubah $v$ sebesar 2 sehingga nilai harapnya nol. Dengan $\hat a^\dagger\hat a|v\rangle = v|v\rangle$ dan $\hat a\hat a^\dagger|v\rangle = (v + 1)|v\rangle$:

$$
\langle\hat x^2\rangle = \frac{2v + 1}{2\alpha} .
$$

HCl: $v = 0$, $x_\text{rms} = 1/\sqrt{2\alpha} = 7{,}6$ pm; $v = 1$, $x_\text{rms} = \sqrt{3/2\alpha} = 13{,}1$ pm.

**Memahami hasil.** Satu baris aljabar operator menggantikan integral fungsi Hermite. Simpangan rms yang membesar dengan $v$ menjelaskan mengapa panjang ikatan rata-rata naik pada tingkat getaran lebih tinggi (dengan bantuan anharmonisitas, subbab 5.9), dan mengapa difraksi elektron gas memberi panjang ikatan "efektif" yang sedikit bergantung pada suhu.
:::
''', 'Simpangan rms dengan operator tangga')
sisip(N, '5.7', r'''
::: {.contoh}
**Contoh 5.t5 · Tetapan gaya dan orde ikatan**

Hitung tetapan gaya dari bilangan gelombang getaran: CO 2170 cm⁻¹, N₂ 2359 cm⁻¹, O₂ 1580 cm⁻¹, F₂ 917 cm⁻¹, dan HF 4138 cm⁻¹ (massa atom: N 14,003; O 15,995; F 18,998; C 12,000; H 1,008 u).

**Penyelesaian.** $k = \mu(2\pi c\tilde\nu)^2$:

| Molekul | orde ikatan | $k$ (N/m) |
|---|---|---|
| N₂ | 3 | 2296 |
| CO | 3 | 1902 |
| O₂ | 2 | 1176 |
| F₂ | 1 | 471 |
| HF | 1 | 966 |

**Memahami hasil.** Tetapan gaya naik hampir sebanding dengan orde ikatan: N₂ (rangkap tiga) sekitar lima kali F₂ (tunggal). HF yang berorde satu tetap jauh lebih kaku daripada F₂ karena ikatannya pendek dan sangat polar. Bilangan gelombang HF yang tinggi (4138 cm⁻¹) terutama berasal dari massa tereduksinya yang kecil, bukan dari kekakuannya. Tabel seperti ini menjadi uji langsung bagi teori orbital molekul di Bab 11.
:::
''', 'Tetapan gaya dan orde ikatan')
sisip(N, '5.11', r'''
::: {.contoh}
**Contoh 5.t6 · Menghitung mode normal**

Berapa banyak mode getaran untuk CO₂, H₂O, CH₄, dan benzena? Untuk CO₂, mode mana yang aktif inframerah?

**Penyelesaian.** Molekul linear mempunyai $3N - 5$ mode, molekul tak linear $3N - 6$: CO₂ 4, H₂O 3, CH₄ 9, benzena 30. CO₂ mempunyai ulur simetris (1333 cm⁻¹), ulur asimetris (2349 cm⁻¹), dan dua tekuk yang berdegenerasi (667 cm⁻¹). Ulur simetris tidak mengubah momen dipol (kedua O bergerak berlawanan arah secara simetris), sehingga tidak aktif inframerah; ulur asimetris dan tekuk aktif.

**Memahami hasil.** Mode yang tidak aktif inframerah biasanya aktif Raman, dan sebaliknya untuk molekul yang mempunyai pusat inversi (aturan saling eksklusi, Bab 10). Teori grup memberi cara sistematis untuk menentukan aktivitas semua 30 mode benzena tanpa menggambar satu per satu.
:::

::: {.terapan}
**Kaitan kimia · Mode tekuk CO₂ dan efek rumah kaca**

Bumi bersuhu sekitar 288 K memancarkan radiasi inframerah dengan puncak di sekitar 10 μm (hukum Wien). Mode tekuk CO₂ pada 667 cm⁻¹ berada di 15,0 μm, di sisi kuat spektrum pancaran itu, sehingga CO₂ menyerap sebagian radiasi yang seharusnya lolos ke angkasa. N₂ dan O₂, yang jauh lebih melimpah, tidak menyerap sama sekali karena getaran molekul diatom homonuklir tidak mengubah momen dipol. Jadi efek rumah kaca adalah akibat langsung aturan seleksi inframerah yang diturunkan di bab ini.
:::
''', 'Menghitung mode normal')
soal(N, '5.2', [r'Hitung $1/\sqrt\alpha$ (pm) untuk ¹²C¹⁶O ($\tilde\nu = 2170$ cm⁻¹, $\mu = 6{,}8562$ u). ||| 4,76 pm'])
soal(N, '5.3', [r'Dengan rekursi, bangun $H_5(y)$. ||| $32y^5 - 160y^3 + 120y$'])
soal(N, '5.5', [r'Untuk keadaan dasar, berapa peluang osilator berada di dalam $|y| < 0{,}5$? ||| 0,520'])
soal(N, '5.6', [r'Dengan operator tangga, tunjukkan bahwa $\langle v|\hat p^2|v\rangle = (2v + 1)\hbar^2\alpha/2$, lalu periksa bahwa $\langle T\rangle = \langle V\rangle$. ||| $\langle T\rangle = \langle V\rangle = \tfrac12(v + \tfrac12)\hbar\omega$'])
soal(N, '5.7', [r'Hitung tetapan gaya Cl₂ ($\tilde\nu = 560$ cm⁻¹, ³⁵Cl 34,969 u) dan bandingkan dengan F₂. ||| 323 N/m; lebih lunak dari F₂ (471 N/m)'])
soal(N, '5.11', [r'Berapa mode getaran NH₃ dan C₂H₆? ||| 6; 18',
                 r'Pada panjang gelombang berapa (μm) mode ulur asimetris CO₂ (2349 cm⁻¹) menyerap? Mengapa mode ini tidak penting untuk efek rumah kaca bumi? ||| 4,26 μm; jauh dari puncak pancaran bumi (± 10 μm)'])
print('selesai')
