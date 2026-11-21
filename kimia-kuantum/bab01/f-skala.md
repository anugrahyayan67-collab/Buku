## 1.10 Skala energi dalam kimia: eV, cm⁻¹, kJ/mol, hartree

Bab ini telah memakai setidaknya tujuh satuan energi: joule, elektronvolt, kJ/mol, kcal/mol, cm⁻¹, kelvin, dan hartree. Ini bukan kekacauan; setiap satuan lahir dari cara pengukuran tertentu. Kimiawan termodinamika mengukur kalor reaksi tiap mol (kJ/mol). Spektroskopiwan mengukur panjang gelombang, sehingga bilangan gelombang (cm⁻¹) paling alami. Fisikawan mempercepat elektron dengan tegangan, sehingga memakai eV. Kimiawan teori menghitung dengan satuan atom (hartree). Ahli NMR membaca frekuensi (MHz). Kimiawan kuantum yang baik harus dapat berpindah di antara semuanya tanpa berpikir panjang.

### Hubungan dasar

Semua satuan itu dihubungkan oleh beberapa tetapan dasar. Untuk energi $E$ satu partikel (satu molekul, satu foton):

$$
E = h\nu = hc\tilde\nu = kT_E = \frac{E_\text{mol}}{N_A} . \qquad \text{(1.37)}
$$

Di sini $\nu$ frekuensi foton yang energinya $E$, $\tilde\nu = 1/\lambda$ bilangan gelombangnya, $T_E$ "suhu setara", yaitu suhu yang $kT$-nya sama dengan $E$, dan $E_\text{mol}$ energi satu mol. Satuan eV didefinisikan sebagai energi yang diperoleh muatan $e$ yang dipercepat melalui beda potensial 1 V: 1 eV $= 1{,}602\,176\,634 \times 10^{-19}$ J.

Hubungan antara eV dan kJ/mol patut diperhatikan:

$$
1\ \text{eV} \times N_A = (1{,}602 \times 10^{-19}\ \text{J})(6{,}022 \times 10^{23}\ \text{mol}^{-1}) = 96{,}485\ \text{kJ/mol} ,
$$

dan $eN_A = F = 96\,485$ C/mol adalah **tetapan Faraday**. Inilah sebabnya persamaan elektrokimia $\Delta G = -nFE$ mengubah potensial sel dalam volt langsung menjadi energi bebas dalam kJ/mol: reaksi yang memindahkan satu elektron melalui 1 V membebaskan 96,5 kJ/mol.

### Bilangan gelombang sebagai satuan energi

Spektroskopiwan menulis "energi 2000 cm⁻¹" sebagai singkatan untuk "energi $hc \times 2000$ cm⁻¹". Satuan ini praktis karena (i) berbanding lurus dengan energi, tidak seperti panjang gelombang; (ii) angkanya enak untuk spektroskopi getaran (ratusan sampai ribuan); dan (iii) berhubungan langsung dengan panjang gelombang:

$$
\tilde\nu\ (\text{cm}^{-1}) = \frac{10^7}{\lambda\ (\text{nm})} . \qquad \text{(1.38)}
$$

Cahaya 500 nm adalah 20 000 cm⁻¹; inframerah 10 µm adalah 1000 cm⁻¹. Dalam satuan ini, energi termal pada 298 K adalah $kT/hc = 207$ cm⁻¹, angka yang patut dihafal.

### Populasi Boltzmann

Perbandingan energi dengan $kT$ menentukan populasi tingkat-tingkat energi pada keseimbangan termal. Jika tingkat $j$ dan $i$ mempunyai energi $E_j > E_i$ dan **degenerasi** (banyaknya keadaan dengan energi yang sama) $g_j$ dan $g_i$, maka

$$
\boxed{\ \frac{N_j}{N_i} = \frac{g_j}{g_i}\,e^{-(E_j - E_i)/kT}\ } \qquad \text{(1.39)}
$$

Untuk perhitungan dengan bilangan gelombang, pakai **tetapan radiasi kedua** $c_2 = hc/k = 1{,}4388$ cm·K, sehingga

$$
\frac{\Delta E}{kT} = \frac{1{,}4388\,\Delta\tilde\nu\ (\text{cm}^{-1})}{T\ (\text{K})} .
$$

### Satuan atom

Mulai Bab 7, perhitungan atom dan molekul memakai **satuan atom**: massa elektron $m_e$, muatan elementer $e$, $\hbar$, dan $4\pi\varepsilon_0$ semuanya diberi nilai 1. Satuan panjangnya jari-jari Bohr, 1 bohr $= a_0 = 52{,}918$ pm, dan satuan energinya **hartree**,

$$
1\ E_h = \frac{e^2}{4\pi\varepsilon_0a_0} = \frac{\hbar^2}{m_ea_0^2} = 27{,}211\ \text{eV} = 2625{,}5\ \text{kJ/mol} = 219\,475\ \text{cm}^{-1} . \qquad \text{(1.40)}
$$

Energi atom hidrogen pada keadaan dasar tepat $-\tfrac12E_h$ (dalam pendekatan inti tak hingga berat). Satuan atom menghilangkan tetapan-tetapan yang merepotkan dari persamaan, dan hasil perhitungan program kimia kuantum hampir selalu dicetak dalam hartree. Kimiawan komputasi berbicara tentang **ketelitian kimia** sebesar 1 kcal/mol, sekitar 1,6 m$E_h$: ketelitian yang diperlukan untuk meramalkan tetapan kesetimbangan dan laju reaksi dengan berguna.

::: {.inti}
**Tabel konversi energi.** Baris menyatakan satuan asal; kalikan dengan angka di kolom untuk memperoleh satuan tujuan.
:::

| 1 satuan = | eV | kJ/mol | kcal/mol | cm⁻¹ | K | $E_h$ |
|---|---|---|---|---|---|---|
| 1 eV | 1 | 96,485 | 23,061 | 8065,54 | 11 604,5 | 0,036 749 |
| 1 kJ/mol | 0,010 364 | 1 | 0,239 01 | 83,593 | 120,27 | 3,8088 × 10⁻⁴ |
| 1 kcal/mol | 0,043 364 | 4,184 | 1 | 349,76 | 503,22 | 1,5936 × 10⁻³ |
| 1 cm⁻¹ | 1,2398 × 10⁻⁴ | 0,011 963 | 2,8591 × 10⁻³ | 1 | 1,4388 | 4,5563 × 10⁻⁶ |
| 1 $E_h$ | 27,2114 | 2625,50 | 627,51 | 219 474,6 | 315 775 | 1 |

| Ingat | Nilai |
|---|---|
| $kT$ pada 298,15 K | 0,025 69 eV = 2,479 kJ/mol = 0,5925 kcal/mol = 207,2 cm⁻¹ |
| foton 500 nm | 2,480 eV = 239,3 kJ/mol = 20 000 cm⁻¹ |
| $hc$ | 1239,84 eV·nm |
| 1 MHz (NMR) | $3{,}336 \times 10^{-5}$ cm⁻¹ = $4{,}136 \times 10^{-9}$ eV |

::: {.contoh}
**Contoh 1.49 · Satu serapan, enam satuan**

HCl menyerap inframerah dengan kuat pada 2886 cm⁻¹ (getaran ulur H–Cl). Nyatakan energi kuantum ini sebagai panjang gelombang (µm), frekuensi (THz), energi tiap molekul (J dan eV), dan energi tiap mol (kJ/mol). Berapa perbandingan populasi tingkat getaran pertama terhadap tingkat dasar pada 298 K (degenerasi keduanya satu)?

**Penyelesaian.** 

- Panjang gelombang: $\lambda = 1/\tilde\nu = 1/(2886\ \text{cm}^{-1}) = 3{,}465 \times 10^{-4}$ cm $= 3{,}465$ µm.
- Frekuensi: $\nu = c\tilde\nu = (2{,}998 \times 10^{10}\ \text{cm/s})(2886\ \text{cm}^{-1}) = 8{,}652 \times 10^{13}$ Hz $= 86{,}52$ THz.
- Energi tiap molekul: $E = hc\tilde\nu = 5{,}733 \times 10^{-20}$ J $= 0{,}3578$ eV.
- Energi tiap mol: $(2886)(0{,}011\,963) = 34{,}52$ kJ/mol.
- Populasi: $\Delta E/kT = 1{,}4388(2886)/298{,}15 = 13{,}93$, sehingga $N_1/N_0 = e^{-13{,}93} = 8{,}9 \times 10^{-7}$.

**Memahami hasil.** Pada suhu kamar hampir sejuta molekul berada pada tingkat dasar untuk setiap satu molekul yang tereksitasi. Serapan inframerah karena itu hampir seluruhnya berasal dari tingkat $v = 0$. Ini menyederhanakan spektrum, dan merupakan lagi akibat dari kuantum getaran yang besar dibandingkan $kT$.
:::

::: {.contoh}
**Contoh 1.50 · Rotasi: banyak tingkat yang terisi**

Selang antara dua tingkat rotasi terendah CO adalah $2B = 3{,}845$ cm⁻¹, dengan degenerasi $g_0 = 1$ dan $g_1 = 3$. Hitung $N_1/N_0$ pada 298 K.

**Penyelesaian.** $\Delta E/kT = 1{,}4388(3{,}845)/298{,}15 = 0{,}018\,55$. Maka $N_1/N_0 = 3e^{-0{,}018\,55} = 2{,}94$.

**Memahami hasil.** Tingkat $J = 1$ lebih padat daripada tingkat dasar, karena degenerasinya tiga dan selang energinya kecil sekali dibandingkan $kT$. Pada suhu kamar puluhan tingkat rotasi CO terisi; yang terpadat adalah sekitar $J = 7$ (Bab 6). Inilah sebabnya spektrum rotasi dan pita rotasi–getaran memperlihatkan banyak garis, sedangkan spektrum getaran hanya satu pita dasar.
:::

::: {.contoh}
**Contoh 1.51 · Ikatan hidrogen dalam berbagai satuan**

Energi ikatan hidrogen O–H···O sekitar 20 kJ/mol. Nyatakan dalam eV, cm⁻¹, kcal/mol, dan kelipatan $kT$ pada 298 K.

**Penyelesaian.** $20 \times 0{,}010\,364 = 0{,}207$ eV; $20 \times 83{,}593 = 1672$ cm⁻¹; $20 \times 0{,}239\,01 = 4{,}78$ kcal/mol; $20/2{,}479 = 8{,}1\,kT$.

**Memahami hasil.** Delapan kali $kT$ berarti faktor Boltzmann $e^{-8{,}1} \approx 3 \times 10^{-4}$. Satu ikatan hidrogen terputus secara termal sangat sering pada skala waktu molekul (dalam air cair, umurnya beberapa pikodetik), tetapi pada setiap saat sebagian besar ikatan utuh. Energi sebesar inilah yang membuat struktur protein dan DNA cukup mantap untuk berfungsi, tetapi cukup lentur untuk berubah bentuk.
:::

::: {.contoh}
**Contoh 1.52 · Energi disosiasi H₂ dan ketelitian kimia**

Energi disosiasi H₂ (dari tingkat titik nol) adalah 4,478 eV. (a) Nyatakan dalam kJ/mol, cm⁻¹, dan hartree. (b) Program kimia kuantum menghitungnya dengan galat 1,0 m$E_h$. Berapa galat itu dalam kJ/mol dan kcal/mol?

**Penyelesaian.** (a) $4{,}478 \times 96{,}485 = 432{,}1$ kJ/mol; $4{,}478 \times 8065{,}54 = 36\,118$ cm⁻¹; $4{,}478 \times 0{,}036\,749 = 0{,}1646\ E_h$.

\(b) $1{,}0 \times 10^{-3} \times 2625{,}5 = 2{,}6$ kJ/mol $= 0{,}63$ kcal/mol.

**Memahami hasil.** Galat 1 m$E_h$ hanya 0,6% dari energi ikatan H₂, dan masih di dalam ketelitian kimia. Tetapi energi total elektron molekul air sekitar $-76{,}4\ E_h$, sehingga ketelitian 1 m$E_h$ berarti ketelitian relatif $10^{-5}$ pada energi total. Kimia hidup dalam selisih kecil antara bilangan-bilangan besar; inilah salah satu alasan kimia kuantum komputasi itu sulit (Bab 17).
:::

::: {.contoh}
**Contoh 1.53 · Mengapa NMR kurang peka**

Spektrometer NMR 400 MHz mendeteksi transisi proton antara dua tingkat spin yang berselisih energi $h\nu$ dengan $\nu = 400$ MHz. (a) Nyatakan selisih energi itu dalam J, cm⁻¹, dan kJ/mol. (b) Hitung selisih populasi relatif $(N_\alpha - N_\beta)/(N_\alpha + N_\beta)$ pada 298 K. Gunakan $e^{-x} \approx 1 - x$.

**Penyelesaian.** (a) $\Delta E = (6{,}626 \times 10^{-34})(4{,}00 \times 10^8) = 2{,}65 \times 10^{-25}$ J $= 0{,}013\,34$ cm⁻¹ $= 1{,}60 \times 10^{-4}$ kJ/mol.

\(b) $x = \Delta E/kT = 2{,}65 \times 10^{-25}/4{,}116 \times 10^{-21} = 6{,}44 \times 10^{-5}$. Dengan $N_\beta/N_\alpha = e^{-x} \approx 1 - x$:

$$
\frac{N_\alpha - N_\beta}{N_\alpha + N_\beta} = \frac{1 - (1 - x)}{1 + (1 - x)} \approx \frac{x}{2} = 3{,}2 \times 10^{-5} .
$$

**Memahami hasil.** Hanya sekitar 3 dari 100 000 proton yang "berlebih" di tingkat bawah; sinyal NMR berasal dari kelebihan kecil itu, karena serapan dan pancaran terstimulasi dari kedua tingkat saling meniadakan. Itulah sebabnya NMR memerlukan sampel miligram, sedangkan spektroskopi UV-Vis cukup dengan mikrogram, dan mengapa magnet yang makin kuat (900 MHz, 1,2 GHz) begitu berharga (Bab 16).
:::

::: {.contoh}
**Contoh 1.54 · Kembali ke garam dalam nyala**

Kini kita dapat menjawab sebagian teka-teki pembuka bab. Dalam nyala bersuhu 2500 K, berapa fraksi atom natrium yang berada dalam keadaan tereksitasi 3p (589,0 nm di atas keadaan dasar 3s)? Degenerasi keadaan 3s adalah 2 dan keadaan 3p adalah 6.

**Penyelesaian.** $\tilde\nu = 10^7/589{,}0 = 16\,978$ cm⁻¹. $\Delta E/kT = 1{,}4388(16\,978)/2500 = 9{,}771$. Dengan (1.39):

$$
\frac{N_{3p}}{N_{3s}} = \frac{6}{2}\,e^{-9{,}771} = 3(5{,}71 \times 10^{-5}) = 1{,}7 \times 10^{-4} .
$$

**Memahami hasil.** Hanya sekitar dua atom dari sepuluh ribu yang tereksitasi pada setiap saat, tetapi setiap atom tereksitasi memancarkan foton dalam belasan nanodetik lalu dieksitasi ulang oleh tumbukan, sehingga nyala tampak kuning terang. Warnanya tajam karena energi 3p − 3s terkuantisasi, sama untuk setiap atom natrium di mana pun; dan pada suhu kamar ($\Delta E/kT = 82$) tidak ada satu pun atom yang tereksitasi. Fotometri nyala dan spektroskopi emisi atom memanfaatkan fakta ini untuk menentukan kadar natrium dan kalium dalam darah, tanah, dan air. Mengapa selisih energi 3p − 3s natrium tepat 2,10 eV, dan bukan 10,2 eV seperti pada hidrogen, akan dijawab di Bab 9 dengan konsep perisai dan muatan inti efektif.
:::

::: {.awas}
**Awas · Tiap molekul atau tiap mol?**

Kesalahan paling umum dalam soal kimia kuantum adalah mencampur energi tiap molekul dengan energi tiap mol. Rumus $E = h\nu$, $\Delta E/kT$, dan $hc/\lambda$ memberikan energi **tiap partikel**. Faktor Boltzmann dapat ditulis $e^{-\Delta E/kT}$ (tiap partikel) atau $e^{-\Delta E_\text{mol}/RT}$ (tiap mol), tetapi tidak pernah $e^{-\Delta E_\text{mol}/kT}$. Periksa selalu: jika $\Delta E/kT$ bernilai sekitar $10^{23}$, satuannya tercampur.
:::

::: {.kuis}
**Kuis cepat 1.10**

Tanpa kalkulator: (a) berapa kira-kira cm⁻¹ setara dengan 1 eV? (b) Kira-kira berapa kJ/mol energi satu foton 400 nm? (c) Pada suhu berapa $kT$ sama dengan 1 eV?
:::

### Menuju bab berikutnya

Bab ini menunjukkan bahwa alam memaksa kita menerima kuantum. Untuk mengolahnya secara kuantitatif kita memerlukan bahasa matematikanya: bilangan kompleks, persamaan diferensial, dan matriks. Itulah isi Bab 2.
