## 5.10 Efek isotop

### Satu permukaan potensial, banyak massa

Kini kita dapat menjawab teka-teki pembuka bab. Menurut aproksimasi Born–Oppenheimer (Bab 11), kurva energi potensial sebuah ikatan ditentukan oleh elektron dan muatan inti, bukan oleh massa inti. H₂, HD, dan D₂ mempunyai kurva potensial yang **sama persis**: $D_e$, $r_e$, dan tetapan gaya $k$ yang sama. Yang berbeda hanyalah massa tereduksi, sehingga

$$
\frac{\omega(\text{berat})}{\omega(\text{ringan})} = \sqrt{\frac{\mu_\text{ringan}}{\mu_\text{berat}}}, \qquad \frac{\omega_ex_e(\text{berat})}{\omega_ex_e(\text{ringan})} = \frac{\mu_\text{ringan}}{\mu_\text{berat}} . \qquad \text{(5.29)}
$$

Hubungan kedua mengikuti dari (5.27): $\omega_ex_e = \omega_e^2/4D_e$ dengan $D_e$ tetap. Untuk ikatan X–H dengan X berat, $\mu$ hampir dua kali lipat bila H diganti D, sehingga frekuensinya turun dengan faktor hampir $\sqrt2$.

### Energi titik nol dan energi ikatan

Karena frekuensinya lebih rendah, energi titik nol isotopolog berat lebih kecil. Molekul berat duduk lebih dalam di sumur yang sama, sehingga energi disosiasinya **lebih besar**:

$$
D_0(\text{berat}) - D_0(\text{ringan}) = E_0(\text{ringan}) - E_0(\text{berat}) > 0 . \qquad \text{(5.30)}
$$

Inilah akar hampir semua efek isotop kimia. Ikatan O–D lebih sulit diputus daripada O–H bukan karena gayanya berbeda, tetapi karena O–D "memulai" dari titik yang lebih rendah di sumur.

### Efek isotop kinetik

Dalam reaksi yang langkah penentu lajunya memutus ikatan C–H, getaran ulur C–H berubah menjadi gerak sepanjang koordinat reaksi di keadaan transisi. Dalam model paling sederhana, energi titik nol ulur ini hilang di keadaan transisi, sedangkan energi titik nol lainnya tidak berubah. Maka energi aktivasi C–D lebih besar daripada C–H sebesar selisih energi titik nol ulurnya, dan perbandingan laju

$$
\frac{k_H}{k_D} \approx \exp\left[\frac{\tfrac12hc(\tilde\nu_\text{CH} - \tilde\nu_\text{CD})}{kT}\right] . \qquad \text{(5.31)}
$$

Nilai klasik maksimum sekitar 7 pada suhu kamar ini disebut **efek isotop kinetik primer**. Pengukurannya adalah alat utama ahli kimia organik dan biokimia untuk mengetahui apakah ikatan C–H diputus pada langkah penentu laju. Nilai yang jauh lebih besar daripada 7 (sampai 50 atau lebih pada beberapa enzim) menandakan **penerobosan** hidrogen melalui penghalang (Contoh 3.43).

::: {.contoh}
**Contoh 5.40 · Ramalan spektrum D₂ dan HD**

Dari data H₂ ($\omega_e = 4401{,}21$, $\omega_ex_e = 121{,}34$ cm⁻¹, $D_e = 4{,}7472$ eV), ramalkan $\omega_e$, energi titik nol, dan $D_0$ untuk HD dan D₂.

**Penyelesaian.** Massa tereduksi: H₂ 0,50391 u; HD 0,67171 u; D₂ 1,00705 u. Dengan (5.29) dan $G(0) = \tfrac12\omega_e - \tfrac14\omega_ex_e$:

| | H₂ | HD | D₂ |
|---|---|---|---|
| $\omega_e$ (cm⁻¹) | 4401,2 | 3812,0 | 3113,3 |
| $G(0)$ (cm⁻¹) | 2170,3 | 1883,3 | 1541,5 |
| $D_0$ ramalan (eV) | 4,4781 | 4,5137 | 4,5561 |
| $D_0$ terukur (eV) | 4,4781 | 4,5137 | 4,5562 |

**Memahami hasil.** Ramalan dari data H₂ saja cocok dengan percobaan sampai 0,0001 eV. Ini adalah salah satu pengujian paling tajam aproksimasi Born–Oppenheimer: satu kurva potensial, tiga massa, tiga spektrum. Ikatan D–D 0,078 eV (7,5 kJ/mol) lebih kuat daripada H–H, seluruhnya karena energi titik nol.
:::

::: {.contoh}
**Contoh 5.41 · Pita O–H dan O–D**

Pita ulur simetris H₂O gas berada di 3657 cm⁻¹. Ramalkan pita O–D yang bersesuaian, anggap getaran ini sebagai osilator O–H diatom.

**Penyelesaian.** $\mu(\text{OH}) = 0{,}9481$ u, $\mu(\text{OD}) = 1{,}7889$ u. $\tilde\nu(\text{OD}) = 3657\sqrt{0{,}9481/1{,}7889} = 2662$ cm⁻¹. Nilai terukur untuk D₂O adalah 2671 cm⁻¹.

**Memahami hasil.** Model diatom sederhana meleset hanya 0,3%. Perbandingan $\tilde\nu_\text{OH}/\tilde\nu_\text{OD} = 1{,}37$, sedikit di bawah $\sqrt2 = 1{,}414$, karena atom O tidak tak hingga berat. Dalam spektroskopi IR protein, pertukaran H/D dengan pelarut D₂O dipakai untuk membedakan gugus N–H yang terpapar pelarut dari yang tersembunyi di dalam struktur.
:::

::: {.contoh}
**Contoh 5.42 · Efek isotop kinetik C–H/C–D**

Ulur C–H khas berada di 2900 cm⁻¹. Hitung $\tilde\nu(\text{C–D})$, selisih energi titik nol, dan $k_H/k_D$ maksimum menurut (5.31) pada 25 °C dan 100 °C.

**Penyelesaian.** $\mu(\text{CH}) = 0{,}9297$ u, $\mu(\text{CD}) = 1{,}7246$ u; $\tilde\nu(\text{CD}) = 2900/1{,}362 = 2129$ cm⁻¹. Selisih energi titik nol $\tfrac12(2900 - 2129) = 385$ cm⁻¹ $= 4{,}61$ kJ/mol. Pada 298 K, $hc(385)/kT = 1{,}86$, jadi $k_H/k_D = e^{1{,}86} = 6{,}4$; pada 373 K, $4{,}4$.

**Memahami hasil.** Efek isotop menurun bila suhu naik, karena selisih energi yang tetap menjadi kecil dibandingkan $kT$. Pengukuran $k_H/k_D \approx 6$ dalam oksidasi alkohol oleh kromat (Westheimer, 1950-an) menunjukkan bahwa ikatan C–H diputus pada langkah penentu laju. Untuk tritium ($\tilde\nu_\text{CT} = 1801$ cm⁻¹), rumus yang sama memberi $k_H/k_T = 14$.
:::

::: {.contoh}
**Contoh 5.43 · Kesetimbangan pertukaran isotop**

Untuk reaksi H₂ + D₂ ⇌ 2HD, hitung perubahan energi titik nol dengan data Contoh 5.40. Pada suhu tinggi, tetapan kesetimbangan mendekati 4 (faktor statistik: HD tidak simetris). Seberapa besar energi titik nol menggeser nilai itu pada 298 K?

**Penyelesaian.** $\Delta E_0 = 2(1883{,}3) - 2170{,}3 - 1541{,}5 = 54{,}8$ cm⁻¹ $= 0{,}66$ kJ/mol. Faktor Boltzmann $e^{-54{,}8 \times 1{,}4388/298{,}15} = 0{,}768$, jadi $K \approx 4 \times 0{,}768 = 3{,}1$.

**Memahami hasil.** Nilai terukur $K$ pada 298 K adalah sekitar 3,3; selisihnya berasal dari fungsi partisi rotasi dan translasi yang juga bergantung massa. Energi titik nol, meski hanya 0,7 kJ/mol bedanya, menggeser kesetimbangan sebesar 20%. Efek seperti ini yang memisahkan isotop secara alamiah: air laut dan air hujan mempunyai perbandingan D/H dan ¹⁸O/¹⁶O yang berbeda, dan perbedaan itu dipakai sebagai termometer iklim masa lampau dalam inti es.
:::

::: {.terapan}
**Obat terdeuterasi**

Banyak obat diuraikan di hati oleh enzim sitokrom P450 melalui pemutusan ikatan C–H. Mengganti H pada posisi itu dengan D memperlambat penguraian (efek isotop kinetik), sehingga obat bertahan lebih lama dalam tubuh dan dosisnya dapat diturunkan. Deutetrabenazin, obat terdeuterasi pertama yang disetujui di Amerika Serikat (2017), memanfaatkan prinsip ini. Satu neutron per atom hidrogen, melalui energi titik nol $\tfrac12h\nu$, mengubah farmakologi sebuah molekul.
:::

::: {.contoh}
**Contoh 5.44 · Energi disosiasi DCl**

Dari data HCl ($\omega_e = 2990{,}95$, $\omega_ex_e = 52{,}82$ cm⁻¹, $D_0 = 4{,}434$ eV), ramalkan $D_0$ untuk DCl.

**Penyelesaian.** $\mu(\text{HCl})/\mu(\text{DCl}) = 0{,}51438$. Dengan (5.29): $\omega_e(\text{DCl}) = 2145{,}1$ cm⁻¹ dan $\omega_ex_e = 27{,}17$ cm⁻¹. $G(0)$: HCl 1482,3; DCl 1065,8 cm⁻¹. Selisih 416,5 cm⁻¹ $= 0{,}052$ eV. $D_0(\text{DCl}) = 4{,}434 + 0{,}052 = 4{,}486$ eV.

**Memahami hasil.** Ikatan D–Cl 5,0 kJ/mol lebih kuat daripada H–Cl. Untuk efek isotop yang melibatkan pemutusan atau pembentukan ikatan dengan H, selisih semacam ini, yang tampak kecil, cukup untuk mengubah tetapan kesetimbangan dan laju dengan faktor beberapa kali pada suhu kamar.
:::

::: {.kuis}
**Kuis cepat 5.10**

Ikatan mana yang lebih kuat: O–H atau O–D? Mengapa titik leleh dan titik didih D₂O sedikit lebih tinggi daripada H₂O?
:::

## 5.11 Mode normal molekul poliatom

### Menghitung derajat kebebasan

Molekul dengan $N$ atom mempunyai $3N$ koordinat. Tiga di antaranya menggambarkan translasi pusat massa dan tiga lagi rotasi (dua untuk molekul linear, karena rotasi terhadap sumbu molekul tidak memindahkan inti). Sisanya adalah getaran:

$$
\text{banyak mode getaran} = 3N - 6 \ (\text{tak linear}), \qquad 3N - 5 \ (\text{linear}) . \qquad \text{(5.32)}
$$

### Mode normal

Di dekat geometri setimbang, energi potensial molekul poliatom adalah fungsi kuadrat dari semua simpangan: $V = \tfrac12\sum_{ij}k_{ij}q_iq_j$, dengan suku silang $k_{ij}$ yang menggandengkan gerak atom-atom. Persamaan geraknya terlihat rumit, tetapi seperti halnya matriks simetris dapat didiagonalkan (subbab 2.8), selalu ada kombinasi linear koordinat, $Q_1, Q_2, \ldots$, yang membuat energi menjadi jumlah suku-suku tak bergandeng:

$$
H = \sum_{k=1}^{3N-6}\left(\tfrac12\dot Q_k^2 + \tfrac12\omega_k^2Q_k^2\right) . \qquad \text{(5.33)}
$$

Koordinat $Q_k$ disebut **koordinat normal**, dan gerak sepanjang masing-masing disebut **mode normal**: semua atom bergerak dengan frekuensi yang sama dan fase yang sama (atau berlawanan), mencapai titik balik bersamaan. Karena Hamiltonian (5.33) adalah jumlah osilator yang terpisah, secara kuantum fungsi gelombangnya adalah hasil kali fungsi osilator dan energinya adalah jumlah:

$$
E = \sum_k\left(v_k + \tfrac12\right)\hbar\omega_k , \qquad E_0 = \tfrac12\sum_k\hbar\omega_k . \qquad \text{(5.34)}
$$

Setiap mode adalah osilator harmonik bab ini, dengan aturan seleksi $\Delta v_k = \pm1$ untuk satu mode (pita dasar), dan aturan seleksi kasar bahwa momen dipol harus berubah sepanjang $Q_k$.

![Gambar 5.5 Mode normal CO₂ (kiri) dan H₂O (kanan). Pada CO₂, ulur simetris tidak mengubah momen dipol (tidak aktif IR, tetapi aktif Raman), tekuk (dua mode berdegenerasi, dalam bidang gambar dan tegak lurus padanya) dan ulur asimetris aktif IR. Ketiga mode H₂O aktif IR.](fig/c_mode.png){width=95%}

### Frekuensi gugus

Dalam molekul organik besar, mode normal pada prinsipnya melibatkan semua atom, tetapi beberapa getaran praktis terlokalisasi pada satu gugus: ulur X–H (karena H ringan; Contoh 5.28), ulur C=O (tetapan gaya besar, sekitar 1700 cm⁻¹), ulur C≡N dan C≡C (sekitar 2100–2250 cm⁻¹). Frekuensinya hanya sedikit dipengaruhi sisa molekul, sehingga menjadi **frekuensi gugus** yang dipakai untuk mengenali gugus fungsi dalam spektrum IR. Getaran kerangka di bawah 1500 cm⁻¹ bergandeng kuat dan khas untuk tiap molekul: daerah **sidik jari**.

::: {.contoh}
**Contoh 5.45 · Menghitung mode**

Berapa banyak mode getaran untuk H₂O, CO₂, NH₃, CH₄, HC≡CH, C₆H₆, SF₆, dan C₆₀?

**Penyelesaian.** H₂O $3(3) - 6 = 3$; CO₂ (linear) $9 - 5 = 4$; NH₃ $12 - 6 = 6$; CH₄ $15 - 6 = 9$; HC≡CH (linear) $12 - 5 = 7$; C₆H₆ $36 - 6 = 30$; SF₆ $21 - 6 = 15$; C₆₀ $180 - 6 = 174$.

**Memahami hasil.** Banyak mode tumbuh sebanding dengan banyak atom, tetapi banyak pita IR yang teramati jauh lebih sedikit. Untuk C₆₀ yang sangat simetris, dari 174 mode hanya **empat** pita IR yang teramati, karena sebagian besar mode berdegenerasi atau tidak aktif IR. Teori grup (Bab 10) memberi cara menghitung banyak pita yang aktif tanpa menggambar satu mode pun.
:::

::: {.contoh}
**Contoh 5.46 · Energi titik nol air dan air berat**

Mode normal H₂O gas: 3657, 1595, 3756 cm⁻¹; D₂O: 2671, 1178, 2788 cm⁻¹. Hitung energi titik nol harmonik keduanya dan selisihnya.

**Penyelesaian.** $E_0(\text{H}_2\text{O}) = \tfrac12(3657 + 1595 + 3756) = 4504$ cm⁻¹ $= 53{,}9$ kJ/mol. $E_0(\text{D}_2\text{O}) = \tfrac12(2671 + 1178 + 2788) = 3319$ cm⁻¹ $= 39{,}7$ kJ/mol. Selisih 1186 cm⁻¹ $= 14{,}2$ kJ/mol.

**Memahami hasil.** Untuk memutus kedua ikatan O–H, molekul H₂O memerlukan 14 kJ/mol lebih sedikit daripada D₂O. Dalam cairan, ikatan hidrogen O–D···O juga sedikit lebih kuat karena alasan yang sama, sehingga D₂O mendidih 1,4 °C lebih tinggi. Teka-teki pembuka bab terjawab: satu neutron tambahan tidak mengubah gaya, tetapi mengubah energi titik nol.
:::

::: {.contoh}
**Contoh 5.47 · Pita kombinasi dan resonansi Fermi**

Pada CO₂, ulur simetris (1333 cm⁻¹, tidak aktif IR) hampir tepat dua kali tekuk (667 cm⁻¹). Apa yang terjadi pada tingkat $v_1 = 1$ dan tingkat $v_2 = 2$?

**Penyelesaian.** $E(v_1 = 1) \approx 1333$ cm⁻¹ dan $E(v_2 = 2) \approx 2 \times 667 = 1334$ cm⁻¹. Dua tingkat dengan energi hampir sama dan simetri sama digandengkan oleh suku anharmonik potensial. Seperti dua tingkat dalam masalah 2×2 (Contoh 2.35), keduanya bercampur dan saling menolak; dalam spektrum Raman CO₂ teramati dua pita di 1285 dan 1388 cm⁻¹, bukan satu pita di 1333.

**Memahami hasil.** Gejala ini disebut **resonansi Fermi**. Ia menunjukkan batas model osilator yang terpisah sempurna: bila dua tingkat hampir berdegenerasi, sedikit anharmonisitas cukup untuk mencampurnya. Pita kombinasi dan nada atas juga memberi pita lemah tambahan dalam spektrum IR, misalnya pasangan pita CO₂ di 3716 dan 3609 cm⁻¹ (ulur asimetris digabung dengan masing-masing anggota pasangan resonansi Fermi, $2349 + 1388$ dan $2349 + 1285$, dikurangi koreksi anharmonik), yang ikut menentukan serapan atmosfer.
:::

::: {.contoh}
**Contoh 5.48 · Memperkirakan pita karbonil**

Tetapan gaya C=O dalam keton sekitar 1200 N/m, dan ikatan tunggal C–O sekitar 500 N/m. Dengan model diatom C–O ($\mu = 6{,}856$ u), perkirakan bilangan gelombang ulurnya. Bagaimana konjugasi dengan ikatan rangkap C=C ($k$ turun menjadi sekitar 1150 N/m) mengubah pita C=O?

**Penyelesaian.** $\tilde\nu = \sqrt{k/\mu}/2\pi c$. Untuk $k = 1200$ N/m: 1724 cm⁻¹; $k = 500$ N/m: 1113 cm⁻¹; $k = 1150$ N/m: 1687 cm⁻¹.

**Memahami hasil.** Model diatom sederhana menempatkan pita karbonil di 1720 cm⁻¹, tepat di daerah tempat keton alifatik menyerap (1715 cm⁻¹), dan menjelaskan mengapa keton terkonjugasi menyerap sekitar 30–40 cm⁻¹ lebih rendah. Pita C=O kuat (dipol berubah besar) dan terletak di daerah yang kosong, sehingga menjadi pita paling berguna dalam spektroskopi IR organik.
:::

::: {.contoh}
**Contoh 5.49 · Menghitung mode normal**

Berapa banyak mode getaran untuk CO₂, H₂O, CH₄, dan benzena? Untuk CO₂, mode mana yang aktif inframerah?

**Penyelesaian.** Molekul linear mempunyai $3N - 5$ mode, molekul tak linear $3N - 6$: CO₂ 4, H₂O 3, CH₄ 9, benzena 30. CO₂ mempunyai ulur simetris (1333 cm⁻¹), ulur asimetris (2349 cm⁻¹), dan dua tekuk yang berdegenerasi (667 cm⁻¹). Ulur simetris tidak mengubah momen dipol (kedua O bergerak berlawanan arah secara simetris), sehingga tidak aktif inframerah; ulur asimetris dan tekuk aktif.

**Memahami hasil.** Mode yang tidak aktif inframerah biasanya aktif Raman, dan sebaliknya untuk molekul yang mempunyai pusat inversi (aturan saling eksklusi, Bab 10). Teori grup memberi cara sistematis untuk menentukan aktivitas semua 30 mode benzena tanpa menggambar satu per satu.
:::

::: {.terapan}
**Kaitan kimia · Mode tekuk CO₂ dan efek rumah kaca**

Bumi bersuhu sekitar 288 K memancarkan radiasi inframerah dengan puncak di sekitar 10 μm (hukum Wien). Mode tekuk CO₂ pada 667 cm⁻¹ berada di 15,0 μm, di sisi kuat spektrum pancaran itu, sehingga CO₂ menyerap sebagian radiasi yang seharusnya lolos ke angkasa. N₂ dan O₂, yang jauh lebih melimpah, tidak menyerap sama sekali karena getaran molekul diatom homonuklir tidak mengubah momen dipol. Jadi efek rumah kaca adalah akibat langsung aturan seleksi inframerah yang diturunkan di bab ini.
:::

::: {.kuis}
**Kuis cepat 5.11**

Berapa banyak mode getaran etana (C₂H₆) dan glisin (C₂H₅NO₂)? Mengapa molekul linear mempunyai satu mode lebih banyak daripada molekul tak linear dengan jumlah atom yang sama?
:::

## 5.12 Penyelesaian numerik: metode Numerov

### Mengapa numerik

Osilator harmonik dan potensial Morse termasuk sedikit potensial yang dapat diselesaikan eksak. Untuk kurva potensial sungguhan (dari perhitungan kuantum atau dari data spektroskopi), persamaan Schrödinger satu dimensi diselesaikan secara numerik. Metode yang paling banyak dipakai untuk persamaan berbentuk

$$
\psi''(x) = g(x)\,\psi(x), \qquad g(x) = \frac{2\mu}{\hbar^2}\left[V(x) - E\right] \qquad \text{(5.35)}
$$

adalah metode **Numerov** (1924), yang sederhana tetapi sangat teliti.

### Penurunan

Bagi sumbu $x$ menjadi titik-titik berjarak $h$: $x_i = x_0 + ih$, $\psi_i = \psi(x_i)$. Uraian Taylor ke depan dan ke belakang:

$$
\psi_{i\pm1} = \psi_i \pm h\psi_i' + \frac{h^2}{2}\psi_i'' \pm \frac{h^3}{6}\psi_i''' + \frac{h^4}{24}\psi_i^{(4)} \pm \cdots
$$

Jumlahkan; suku ganjil hilang:

$$
\psi_{i+1} + \psi_{i-1} - 2\psi_i = h^2\psi_i'' + \frac{h^4}{12}\psi_i^{(4)} + O(h^6) .
$$

Rumus beda hingga biasa membuang suku $h^4$, dengan galat $O(h^4)$ per langkah. Numerov justru mempertahankannya. Karena $\psi'' = g\psi$, turunan keempat adalah $\psi^{(4)} = (g\psi)''$, yang dapat didekati dengan beda hingga juga: $(g\psi)''_i \approx [(g\psi)_{i+1} + (g\psi)_{i-1} - 2(g\psi)_i]/h^2$. Masukkan, kumpulkan suku-suku, dan definisikan $f_i = 1 - \tfrac{h^2}{12}g_i$:

$$
\psi_{i+1} = \frac{(12 - 10f_i)\,\psi_i - f_{i-1}\,\psi_{i-1}}{f_{i+1}} . \qquad \text{(5.36)}
$$

Galatnya $O(h^6)$ per langkah, sehingga energi yang dihasilkan mempunyai galat sebanding dengan $h^4$: mengecilkan langkah dua kali memperkecil galat 16 kali.

### Metode tembak

Rumus (5.36) menghasilkan $\psi$ dari kiri ke kanan bila dua nilai awal diketahui. Di tepi kiri, jauh di daerah terlarang, ambil $\psi_0 = 0$ dan $\psi_1$ sembarang kecil (normalisasi diurus belakangan). Untuk energi $E$ sembarang, fungsi hasil integrasi akan meledak ke $+\infty$ atau $-\infty$ di tepi kanan (Gambar 5.6). Hanya pada nilai eigen, $\psi$ meluruh ke nol. Tandanya di tepi kanan berganti ketika $E$ melewati nilai eigen, sehingga nilai eigen dapat dicari dengan **metode bagi dua**: persempit selang $[E_1, E_2]$ sampai tanda $\psi$ di tepi kanan berganti di dalam selang yang sangat sempit.

![Gambar 5.6 Metode tembak untuk osilator harmonik (satuan $\hbar = \mu = \omega = 1$). Untuk $E = 0{,}45$ dan $E = 0{,}55$, fungsi hasil integrasi Numerov meledak ke arah berlawanan di sebelah kanan; hanya untuk nilai eigen $E = 0{,}50$ ia meluruh. Pergantian arah ledakan menandai adanya nilai eigen di antaranya.](fig/c_numerov.png){width=78%}

Program Python berikut melaksanakan semua itu dalam dua puluh baris (satuan $\hbar = \mu = 1$):

```python
import numpy as np

def numerov(E, x, V):
    """Integrasi psi'' = 2(V - E) psi dari kiri ke kanan."""
    h = x[1] - x[0]
    f = 1 + h**2 / 12 * 2 * (E - V)          # faktor Numerov
    psi = np.zeros_like(x)
    psi[1] = 1e-6                             # psi[0] = 0 di tepi kiri
    for i in range(1, len(x) - 1):
        psi[i+1] = ((12 - 10*f[i]) * psi[i] - f[i-1] * psi[i-1]) / f[i+1]
    return psi

def cari_energi(E1, E2, x, V, tol=1e-10):
    """Bagi dua: cari E di antara E1 dan E2 sehingga psi di tepi kanan = 0."""
    p1 = numerov(E1, x, V)[-1]
    while E2 - E1 > tol:
        Em = 0.5 * (E1 + E2)
        pm = numerov(Em, x, V)[-1]
        if p1 * pm < 0:
            E2 = Em
        else:
            E1, p1 = Em, pm
    return 0.5 * (E1 + E2)

x = np.linspace(-6, 6, 1201)                  # osilator harmonik
V = 0.5 * x**2
for E1 in [0.3, 1.3, 2.3, 3.3]:
    print(round(cari_energi(E1, E1 + 0.4, x, V), 6))
```

Keluarannya adalah 0,5; 1,5; 2,5; 3,5, tepat $v + \tfrac12$. (Di sini $g = 2(V - E)$, sehingga $f = 1 - \tfrac{h^2}{12}g = 1 + \tfrac{h^2}{12}\cdot2(E - V)$.)

::: {.contoh}
**Contoh 5.50 · Galat terhadap ukuran langkah**

Dengan program di atas, energi keadaan dasar dan keadaan $v = 2$ osilator harmonik dihitung pada selang $[-6, 6]$ dengan langkah $h$ yang berbeda. Hasil galatnya ($E_\text{numerik} - E_\text{eksak}$):

| $h$ | 0,2 | 0,1 | 0,05 | 0,01 |
|---|---|---|---|---|
| galat $v = 0$ | $-6{,}3 \times 10^{-6}$ | $-3{,}9 \times 10^{-7}$ | $-2{,}4 \times 10^{-8}$ | $-4{,}7 \times 10^{-11}$ |
| galat $v = 2$ | $-1{,}6 \times 10^{-4}$ | $-9{,}8 \times 10^{-6}$ | $-6{,}1 \times 10^{-7}$ | $-9{,}8 \times 10^{-10}$ |

Periksa bahwa galat sebanding dengan $h^4$.

**Penyelesaian.** Perbandingan galat dari $h = 0{,}2$ ke $0{,}1$: $6{,}3 \times 10^{-6}/3{,}9 \times 10^{-7} = 16{,}1$ dan $1{,}6 \times 10^{-4}/9{,}8 \times 10^{-6} = 16{,}1$. Dari $0{,}1$ ke $0{,}05$: 16,0. Untuk $h^4$ diharapkan $2^4 = 16$.

**Memahami hasil.** Dengan hanya 61 titik ($h = 0{,}2$), energi keadaan dasar sudah benar sampai lima angka. Galat lebih besar untuk $v$ yang lebih tinggi, karena fungsi gelombangnya berosilasi lebih cepat dan memerlukan titik lebih rapat per panjang gelombang. Aturan praktis: paling sedikit sekitar 10 titik per panjang gelombang de Broglie lokal.
:::

::: {.contoh}
**Contoh 5.51 · Tingkat getaran Morse H₂ secara numerik**

Program yang sama, dengan $V$ diganti potensial Morse H₂ (Contoh 5.37) dalam satuan atom ($\mu = 918{,}6\,m_e$, 4000 titik dari 0,4 sampai 6 bohr), memberikan tingkat-tingkat berikut. Bandingkan dengan rumus eksak Morse $G(v) = \omega_e(v + \tfrac12) - \omega_ex_e(v + \tfrac12)^2$ dengan $\omega_e = 4401{,}21$ dan $\omega_ex_e = 126{,}48$ cm⁻¹.

| $v$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Numerov (cm⁻¹) | 2168,98 | 6317,24 | 10212,53 | 13854,88 | 17244,26 |
| rumus Morse (cm⁻¹) | 2168,98 | 6317,24 | 10212,53 | 13854,88 | 17244,26 |

**Penyelesaian.** Kedua baris sama sampai 0,01 cm⁻¹. Pita dasar Morse $G(1) - G(0) = 4148{,}25$ cm⁻¹, dibandingkan dengan 4161,2 cm⁻¹ terukur untuk H₂.

**Memahami hasil.** Metode numerik mereproduksi penyelesaian eksak, sehingga kita dapat percaya padanya untuk potensial yang **tidak** mempunyai penyelesaian eksak. Selisih 13 cm⁻¹ terhadap percobaan bukan galat numerik, tetapi galat model Morse. Dengan kurva potensial H₂ dari perhitungan kuantum yang sangat teliti, prosedur yang sama mereproduksi seluruh 15 tingkat getaran H₂ sampai ketelitian spektroskopi; inilah cara spektroskopis modern menguji perhitungan kimia kuantum.
:::

::: {.contoh}
**Contoh 5.52 · Sumur ganda: inversi amonia**

Gerak "payung" amonia dapat dimodelkan dengan potensial sumur ganda $V(x) = V_0(x^2 - a^2)^2/a^4$, dengan penghalang setinggi $V_0$ di $x = 0$ (subbab 3.12). Apa yang akan diperlihatkan metode Numerov untuk tingkat-tingkat terendahnya?

**Penyelesaian.** Bila penghalang tinggi dan lebar, setiap sumur berperilaku seperti osilator harmonik terpisah, dan setiap tingkat osilator muncul **dua kali** dengan energi hampir sama: satu kombinasi simetris (lebih rendah) dan satu antisimetris (lebih tinggi). Selisih energi pasangan itu, **pemisahan inversi**, bergantung secara eksponensial pada tinggi dan lebar penghalang, karena berasal dari penerobosan. Untuk NH₃, pasangan terendah terpisah 0,79 cm⁻¹ (frekuensi 23,8 GHz, dasar maser amonia pertama); untuk ND₃, yang massanya lebih besar, hanya 0,053 cm⁻¹.

**Memahami hasil.** Metode numerik menyatukan tiga topik: getaran (osilator), penerobosan (Bab 3), dan efek isotop (subbab 5.10). Dalam soal di akhir bab kamu diminta menjalankan program ini untuk sumur ganda dan mengamati bagaimana pemisahan berubah bila $V_0$ dinaikkan.
:::

::: {.contoh}
**Contoh 5.53 · Teorema virial sebagai uji hasil numerik**

Dengan fungsi gelombang keadaan dasar dari program Numerov (dinormalisasi secara numerik dengan aturan Simpson), nilai harap untuk dua potensial ($\hbar = \mu = 1$) adalah:

| Potensial | $E_0$ | $\langle T\rangle$ | $\langle V\rangle$ |
|---|---|---|---|
| $\tfrac12x^2$ | 0,5000 | 0,2501 | 0,2499 |
| $x^4$ | 0,6680 | 0,4453 | 0,2227 |

Periksa teorema virial $2\langle T\rangle = n\langle V\rangle$ untuk $V \propto x^n$.

**Penyelesaian.** Harmonik ($n = 2$): $\langle T\rangle = \langle V\rangle$, cocok sampai 0,0002. Kuartik ($n = 4$): $2\langle T\rangle = 0{,}8906$ dan $4\langle V\rangle = 0{,}8907$. Juga $\langle T\rangle + \langle V\rangle = 0{,}6680 = E_0$.

**Memahami hasil.** Teorema virial adalah uji mandiri yang murah untuk hasil numerik: ia tidak memerlukan penyelesaian eksak. Untuk potensial kuartik, $E_0 = 3\langle V\rangle$, sehingga $\langle x^4\rangle = E_0/3$. Program kimia komputasi melaporkan perbandingan $-\langle V\rangle/\langle T\rangle$ (seharusnya 2 untuk molekul pada geometri setimbang) sebagai pemeriksaan kualitas perhitungan.
:::

::: {.kuis}
**Kuis cepat 5.12**

Mengapa metode tembak memerlukan dua nilai awal, $\psi_0$ dan $\psi_1$? Mengapa nilai $\psi_1$ yang tepat tidak penting?
:::

### Menuju bab berikutnya

Molekul tidak hanya bergetar tetapi juga berputar. Bab 6 membahas momentum sudut dan rotor tegar, sekaligus menyiapkan harmonik bola yang menjadi bagian sudut orbital atom.
