## 13.13 Dari molekul ke padatan: rantai Hückel tak hingga dan pita energi

### Cincin yang sangat besar

Kita sudah memiliki semua yang diperlukan untuk membicarakan padatan. Ambil cincin Hückel (13.14) dengan $N$ atom berjarak $a$, dan biarkan $N$ menjadi sangat besar. Cincin besar dan rantai panjang mempunyai tingkat-tingkat energi yang hampir sama (Kuis 13.6); bedanya hanya di ujung-ujung, yang tidak berarti bila $N \sim 10^{23}$. Syarat batas periodik ini (syarat Born–von Kármán) adalah cara baku fisika zat padat memperlakukan kristal.

Dengan $\theta = 2\pi m/N$ dan definisi **vektor gelombang** $k = \theta/a = 2\pi m/(Na)$, orbital dan energinya menjadi

$$
\psi_k = \frac{1}{\sqrt N}\sum_{n=1}^{N}e^{ikna}\,\phi_n , \qquad E(k) = \alpha + 2\beta\cos(ka) , \qquad -\frac{\pi}{a} < k \le \frac{\pi}{a} . \qquad \text{(13.24)}
$$

Persamaan pertama adalah contoh **teorema Bloch**: dalam kisi periodik, fungsi gelombang berpindah dari satu sel ke sel berikutnya hanya dengan dikalikan faktor fase $e^{ika}$. Persamaan kedua adalah **hubungan dispersi**: energi sebagai fungsi vektor gelombang. Karena $N$ sangat besar, nilai $k$ yang diizinkan hampir kontinu, dan $N$ tingkat diskret menjadi satu **pita** energi dari $\alpha + 2\beta$ (di $k = 0$, semua fase sama, orbital paling ikatan) sampai $\alpha - 2\beta$ (di $k = \pm\pi/a$, fase berselang, orbital paling antiikatan). Lebar pitanya $4|\beta|$. Selang $-\pi/a < k \le \pi/a$ disebut **zona Brillouin pertama**.

### Kecepatan, massa efektif, dan rapat keadaan

Di dekat dasar pita ($k \approx 0$), $\cos(ka) \approx 1 - \tfrac12k^2a^2$, sehingga $E \approx (\alpha + 2\beta) + |\beta|a^2k^2$. Ini berbentuk energi partikel bebas, $\hbar^2k^2/2m^*$, dengan **massa efektif**

$$
m^* = \frac{\hbar^2}{2|\beta|a^2} . \qquad \text{(13.25)}
$$

Pita yang lebar (interaksi antaratom kuat) memberi elektron yang "ringan" dan mudah bergerak; pita sempit memberi elektron yang "berat". Kecepatan grup paket gelombang adalah $v = \hbar^{-1}dE/dk$, yang nol di dasar dan puncak pita.

Banyaknya keadaan per selang energi, **rapat keadaan** $g(E)$, diperoleh dari $dk/dE$. Untuk rantai, setiap nilai $k$ menempati selang $2\pi/(Na)$, sehingga

$$
g(E) = 2\cdot\frac{Na}{2\pi}\left|\frac{dk}{dE}\right| = \frac{N}{\pi\sqrt{4\beta^2 - (E - \alpha)^2}} , \qquad \text{(13.26)}
$$

dengan faktor 2 untuk $\pm k$. Rapat keadaan menjadi tak hingga (tetapi terintegralkan) di tepi pita (Gambar 13.10(b)): ini **singularitas van Hove** untuk satu dimensi, dan bentuknya persis sama dengan rapat peluang osilator klasik di titik balik (subbab 5.1).

![Gambar 13.10 (a) Hubungan dispersi rantai Hückel tak hingga dengan ikatan seragam (biru) dan dengan ikatan berselang-seling $\beta_1 = 1{,}15\beta$, $\beta_2 = 0{,}85\beta$ (jingga, sel satuan berisi dua atom sehingga zona Brillouin menyempit menjadi $|ka| \le \pi/2$). Alternasi membuka celah di tepi zona. (b) Rapat keadaan rantai seragam; dengan satu elektron π per atom, pita terisi tepat sampai $E = \alpha$ (bagian berarsir, $x > 0$, karena $\beta < 0$).](fig/c_pita.png){width=94%}

### Poliasetilena: logam atau semikonduktor?

Poliasetilena, (CH)$_x$, adalah rantai karbon terkonjugasi dengan satu elektron π per atom. Dengan $N$ elektron dan $2N$ tempat (dua spin per orbital), pita π terisi tepat setengah: semua keadaan dengan $E < \alpha$ terisi. Tingkat terisi tertinggi, **tingkat Fermi**, berada di tengah pita, dan tepat di atasnya ada keadaan-keadaan kosong. Medan listrik sekecil apa pun dapat menggeser elektron ke keadaan dengan $k$ sedikit berbeda dan menghasilkan arus. Model Hückel dengan ikatan seragam karena itu meramalkan bahwa poliasetilena adalah **logam**.

Kenyataannya, poliasetilena trans murni adalah semikonduktor dengan celah sekitar 1,5 eV, dan ikatannya berselang-seling (sekitar 136 dan 144 pm). R. Peierls menunjukkan bahwa ini bukan kebetulan: **rantai satu dimensi dengan pita setengah terisi tidak stabil terhadap distorsi yang menggandakan sel satuan**. Dengan ikatan berselang $\beta_1$ dan $\beta_2$, sel satuan memuat dua atom, dan persamaan Hückel untuk dua sublattice memberikan

$$
E_\pm(k) = \alpha \pm |\beta_1 + \beta_2e^{2ika}| , \qquad \text{(13.27)}
$$

dengan celah $2|\beta_1 - \beta_2|$ di tepi zona baru, $k = \pi/2a$ (Gambar 13.10(a)). Keadaan-keadaan terisi di dekat tingkat Fermi turun, keadaan kosong naik, dan energi elektronik total turun lebih cepat daripada kenaikan energi regangan σ ketika distorsi kecil (Contoh 13.44). Ini versi tak hingga dari siklobutadiena yang merenggang (Contoh 13.24): sistem dengan keadaan "setengah terisi" di tingkat Fermi selalu dapat menurunkan energinya dengan distorsi.

Celah 1,5 eV memberi $|\beta_1 - \beta_2| \approx 0{,}75$ eV. Ketika poliasetilena dioksidasi dengan iodium atau direduksi dengan natrium (**doping**), elektron dikeluarkan dari pita valensi atau dimasukkan ke pita konduksi, dan konduktivitasnya naik lebih dari sepuluh orde besar, mendekati tembaga. Penemuan ini (A. J. Heeger, A. G. MacDiarmid, H. Shirakawa, Hadiah Nobel 2000) membuka bidang polimer penghantar: polipirola, politiofena, PEDOT, dan polimer untuk LED organik dan sel surya organik.

::: {.inti}
**Dari orbital ke pita.** $N$ orbital atom yang berinteraksi menghasilkan $N$ orbital molekul. Bila $N$ sangat besar, tingkat-tingkat itu membentuk pita dengan lebar sebanding dengan $|\beta|$. Sifat listrik ditentukan oleh pengisian pita: pita yang terisi sebagian menghantarkan (logam); pita yang terisi penuh dan dipisahkan oleh celah dari pita kosong berikutnya tidak menghantarkan pada 0 K (isolator atau semikonduktor). Konsep HOMO dan LUMO molekul berubah menjadi puncak pita valensi dan dasar pita konduksi.
:::

::: {.contoh}
**Contoh 13.43 · Pita dari teorema Bloch**

(a) Masukkan $\psi_k$ dari (13.24) ke persamaan Hückel $\sum_sA_{rs}c_s = xc_r$ dan turunkan $E(k)$. (b) Berapa lebar pita bila $\beta = -2{,}5$ eV? (c) Hitung massa efektif di dasar pita untuk $a = 1{,}40$ Å.

**Penyelesaian.** (a) Untuk atom $n$, $c_n = e^{ikna}/\sqrt N$. Tetangganya $n \pm 1$: $c_{n-1} + c_{n+1} = (e^{-ika} + e^{ika})c_n = 2\cos(ka)\,c_n$. Jadi $x = 2\cos(ka)$ dan $E = \alpha + 2\beta\cos(ka)$. (b) $4|\beta| = 10$ eV. (c) $m^* = \hbar^2/(2|\beta|a^2) = (1{,}0546 \times 10^{-34})^2/[2(2{,}5)(1{,}602 \times 10^{-19})(1{,}40 \times 10^{-10})^2] = 7{,}08 \times 10^{-31}$ kg $= 0{,}78\,m_e$.

**Memahami hasil.** Pita π selebar sekitar 10 eV dan massa efektif mendekati massa elektron bebas menunjukkan bahwa elektron π dalam rantai terkonjugasi panjang hampir sebebas elektron dalam logam. Model elektron bebas untuk poliena (subbab 3.8) bekerja karena itu, setidaknya untuk sistem tanpa alternasi ikatan seperti zat warna sianin.
:::

::: {.contoh}
**Contoh 13.44 · Ketidakstabilan Peierls dengan Python**

Hitung energi π per atom untuk rantai tak hingga setengah terisi dengan ikatan berselang $\beta(1 + \delta)$ dan $\beta(1 - \delta)$, dan bandingkan dengan rantai seragam, untuk $\delta$ = 0,01; 0,02; 0,05; 0,10.

**Penyelesaian.**

```python
import numpy as np
def E_per_atom(d, M=100000):              # M sel satuan (2 atom per sel)
    ka = np.pi * np.arange(M) / M         # 0 <= ka < pi meliputi zona sel ganda
    x = np.abs((1 + d) + (1 - d) * np.exp(2j * ka))   # pita bawah (terisi)
    return 2 * x.sum() / (2 * M)          # dua elektron per orbital terisi
E0 = E_per_atom(0)                        # = 4/pi = 1,2732
for d in (0.01, 0.02, 0.05, 0.10):
    g = E_per_atom(d) - E0
    print(d, round(g, 6), round(g / d**2, 3))
```

Keuntungan energi per atom (dalam $|\beta|$): 0,000350; 0,00122; 0,00618; 0,0204. Perbandingan terhadap $\delta^2$: 3,50; 3,06; 2,47; 2,04, bertambah ketika $\delta$ mengecil.

**Memahami hasil.** Energi π rantai seragam $4|\beta|/\pi$ per atom. Keuntungan dari distorsi tumbuh lebih cepat daripada $\delta^2$ ketika $\delta \to 0$ (secara analitik sebanding dengan $\delta^2\ln(1/\delta)$), sedangkan biaya regangan σ sebanding dengan $\delta^2$. Untuk $\delta$ yang cukup kecil keuntungan selalu menang: rantai seragam tidak pernah stabil. Inilah ketidakstabilan Peierls, versi satu dimensi efek Jahn–Teller.
:::

::: {.contoh}
**Contoh 13.45 · Dari annulena ke poliasetilena**

Annulena besar menunjukkan alternasi ikatan yang makin jelas ketika cincin membesar: [18]annulena hampir tanpa alternasi, sedangkan annulena di atas sekitar [30] diramalkan beralternasi. (a) Untuk cincin $4n + 2$, berapa celah HOMO–LUMO Hückel tanpa alternasi, sebagai fungsi $N$? (b) Hitung untuk $N = 18$ dan $N = 30$ dengan $|\beta| = 2{,}5$ eV. (c) Tafsirkan.

**Penyelesaian.** (a) Untuk $N = 4n + 2$, HOMO adalah $k = \pm n$ dan LUMO $k = \pm(n + 1)$, sehingga $\Delta x = 2[\cos(2\pi n/N) - \cos(2\pi(n + 1)/N)] = 4\sin(\pi/N)\sin[\pi(2n + 1)/N] = 4\sin(\pi/N)$, karena $(2n + 1)/N = \tfrac12$. (b) $N = 18$: $4\sin10° = 0{,}695$, celah 1,74 eV. $N = 30$: $4\sin6° = 0{,}418$, celah 1,05 eV.

**Memahami hasil.** Celah yang dijaga oleh aromatisitas mengecil seperti $1/N$. Ketika celah aromatik menjadi lebih kecil daripada yang dapat diperoleh dari distorsi Peierls, cincin memilih alternasi ikatan dan kehilangan aromatisitas (dan arus cincinnya). Aturan $4n + 2$ dan ketidakstabilan Peierls adalah dua ujung satu cerita.
:::

::: {.kuis}
**Kuis cepat 13.13**

Bila setiap atom dalam rantai menyumbang dua elektron ke pita π (misalnya rantai atom dengan pasangan bebas), pita terisi penuh. Logam atau isolator?
:::

## 13.14 Logam, semikonduktor, grafena

### Pengisian pita menentukan sifat listrik

Gagasan pita berlaku untuk padatan tiga dimensi. Setiap orbital atom valensi menghasilkan satu pita, dengan lebar sebanding dengan $|\beta|$ dan dengan banyaknya tetangga $z$ (untuk kisi kubus sederhana dengan model Hückel, $E = \alpha + 2\beta(\cos k_xa + \cos k_ya + \cos k_za)$, lebar pita $12|\beta| = 2z|\beta|$). Sifat listrik ditentukan oleh posisi tingkat Fermi:

* **Logam**: tingkat Fermi berada di dalam pita. Natrium mempunyai satu elektron $3s$ per atom, sehingga pita $3s$ setengah terisi. Magnesium mempunyai dua elektron $3s$; pita $3s$ akan penuh, tetapi bertumpang tindih dengan pita $3p$, sehingga Mg tetap logam.
* **Isolator**: pita valensi penuh, celah besar ke pita konduksi. Intan, dengan celah 5,5 eV, adalah isolator yang sangat baik.
* **Semikonduktor**: celah kecil (sekitar 0,1–3 eV). Pada suhu kamar sebagian kecil elektron tereksitasi termal ke pita konduksi; banyaknya pembawa muatan intrinsik sebanding dengan $e^{-E_g/2kT}$.

Untuk unsur golongan 14 dengan struktur intan, celah pitanya turun dari C (5,5 eV) ke Si (1,12 eV), Ge (0,66 eV), dan Sn abu-abu (sekitar 0,1 eV). Dengan gambaran hibrida dari Bab 12, alasan ini mudah dipahami. Setiap atom memakai empat hibrida sp³; setiap pasangan hibrida yang berhadapan membentuk orbital ikatan dan antiikatan. Dalam kristal, orbital-orbital ikatan menyebar menjadi pita valensi dan orbital antiikatan menjadi pita konduksi. Celah pita adalah sisa pemisahan ikatan–antiikatan setelah kedua pita melebar. Ikatan C–C yang kuat dan pendek memberi pemisahan besar; ikatan Si–Si, Ge–Ge, dan Sn–Sn makin lemah dan panjang, sehingga pemisahannya mengecil dan celahnya menyempit. Pada timah putih dan timbal, celah hilang sama sekali: logam.

### Grafena

Grafena adalah lembaran tunggal atom karbon sp² dalam kisi sarang lebah, "benzena tak hingga dua dimensi". Kisi sarang lebah mempunyai dua atom per sel satuan, A dan B, dan setiap atom A hanya bertetangga dengan atom B: grafena adalah **hidrokarbon alternan** tak hingga (subbab 13.9). Ambil vektor kisi $\mathbf a_1$ dan $\mathbf a_2$ (panjang $\sqrt3\,a_\text{CC}$, dengan $a_\text{CC} = 142$ pm). Dengan fungsi Bloch $\psi_A$ dan $\psi_B$ untuk kedua sublattice, persamaan Hückel menjadi matriks $2 \times 2$

$$
\begin{pmatrix}\alpha & \beta f(\mathbf k)\\ \beta f^*(\mathbf k) & \alpha\end{pmatrix} , \qquad f(\mathbf k) = 1 + e^{i\mathbf k\cdot\mathbf a_1} + e^{i\mathbf k\cdot\mathbf a_2} , \qquad \text{(13.28)}
$$

karena setiap atom A mempunyai tiga tetangga B, yang fase Bloch-nya relatif terhadap sel asal adalah $1$, $e^{i\mathbf k\cdot\mathbf a_1}$, dan $e^{i\mathbf k\cdot\mathbf a_2}$. Nilai eigennya

$$
E_\pm(\mathbf k) = \alpha \pm \beta\,|f(\mathbf k)| . \qquad \text{(13.29)}
$$

Kedua pita simetris di sekitar $\alpha$, sesuai teorema pasangan. Di titik pusat zona ($\Gamma$, $\mathbf k = 0$), $|f| = 3$: dasar pita π di $\alpha + 3\beta$ dan puncak pita π* di $\alpha - 3\beta$. Yang menakjubkan terjadi di titik sudut zona Brillouin heksagonal, titik **K**: di sana ketiga suku $f$ adalah $1$, $e^{2\pi i/3}$, dan $e^{-2\pi i/3}$, yang berjumlah nol. **Pita π dan π* bersentuhan tepat di titik K** (Gambar 13.11). Dengan satu elektron π per karbon, pita π terisi penuh dan π* kosong, dan tingkat Fermi berada tepat di titik sentuh: grafena adalah **semikonduktor bercelah nol** atau semilogam.

Di dekat K, $|f|$ naik linear terhadap jarak $q$ dari K, sehingga energinya

$$
E - \alpha = \pm\hbar v_Fq , \qquad v_F = \frac{3|\beta|a_\text{CC}}{2\hbar} . \qquad \text{(13.30)}
$$

Hubungan linear ini mirip hubungan $E = cp$ untuk partikel tak bermassa dalam teori relativitas, dengan $v_F$ menggantikan kecepatan cahaya. Daerah ini disebut **kerucut Dirac**. Dengan $|\beta| = 2{,}7$ eV (nilai yang cocok dengan data grafena), $v_F = 8{,}7 \times 10^5$ m/s, sekitar 1/340 kecepatan cahaya. Elektron di grafena berperilaku seperti fermion Dirac tak bermassa, dan inilah asal mobilitas pembawa muatan yang sangat tinggi, efek Hall kuantum pada suhu kamar, dan banyak sifat yang membuat grafena menarik (A. Geim dan K. Novoselov, Hadiah Nobel Fisika 2010).

![Gambar 13.11 (a) Pita π (bawah) dan π* (atas) grafena dalam model Hückel sepanjang lintasan Γ–K–M–Γ zona Brillouin. Kedua pita bersentuhan di titik K. (b) Rapat keadaan: nol di $E = \alpha$ (tingkat Fermi), naik linear di sekitarnya, dan mempunyai puncak van Hove di $\alpha \pm |\beta|$ (titik M).](fig/c_grafena.png){width=94%}

### Nanotabung karbon dan kimia grafit

Nanotabung karbon adalah lembaran grafena yang digulung menjadi silinder. Penggulungan memaksa syarat batas periodik di sekeliling tabung, sehingga hanya garis-garis $\mathbf k$ tertentu yang diizinkan. Bila salah satu garis itu melewati titik K, nanotabung bersifat logam; bila tidak, ia semikonduktor dengan celah sekitar $2a_\text{CC}|\beta|/d$ untuk diameter $d$. Untuk nanotabung dengan indeks penggulungan $(n, m)$, garis melewati K bila $n - m$ habis dibagi 3 (Contoh 13.48). Satu langkah geometri kecil, satu bilangan bulat, menentukan apakah sebuah molekul karbon adalah kawat logam atau semikonduktor.

Grafit, tumpukan lembaran grafena, menghantarkan listrik di sepanjang lembaran tetapi jauh lebih buruk tegak lurus lembaran; intan, dengan karbon sp³, adalah isolator. Perbedaan hibridisasi (Bab 12) langsung tampak sebagai perbedaan struktur pita.

::: {.contoh}
**Contoh 13.46 · Titik Dirac**

Ambil $\mathbf a_1 = a_\text{CC}(\tfrac32, \tfrac{\sqrt3}{2})$ dan $\mathbf a_2 = a_\text{CC}(\tfrac32, -\tfrac{\sqrt3}{2})$. (a) Hitung $f(\mathbf k)$ di $\Gamma$ dan di $\mathbf K = \tfrac{1}{a_\text{CC}}\left(\tfrac{2\pi}{3}, \tfrac{2\pi}{3\sqrt3}\right)$. (b) Berapa lebar total pita π + π*? (c) Hitung $v_F$ untuk $|\beta| = 2{,}7$ eV.

**Penyelesaian.** (a) $\Gamma$: $f = 1 + 1 + 1 = 3$. Di K: $\mathbf K\cdot\mathbf a_1 = \tfrac{2\pi}{3}\cdot\tfrac32 + \tfrac{2\pi}{3\sqrt3}\cdot\tfrac{\sqrt3}{2} = \pi + \tfrac{\pi}{3} = \tfrac{4\pi}{3}$; $\mathbf K\cdot\mathbf a_2 = \pi - \tfrac{\pi}{3} = \tfrac{2\pi}{3}$. $f = 1 + e^{4\pi i/3} + e^{2\pi i/3} = 1 + (-\tfrac12 - \tfrac{\sqrt3}{2}i) + (-\tfrac12 + \tfrac{\sqrt3}{2}i) = 0$. (b) Dari $\alpha + 3\beta$ sampai $\alpha - 3\beta$: $6|\beta| = 16{,}2$ eV. (c) $v_F = 3(2{,}7)(1{,}602 \times 10^{-19})(1{,}42 \times 10^{-10})/[2(1{,}0546 \times 10^{-34})] = 8{,}7 \times 10^5$ m/s.

**Memahami hasil.** Tiga fase yang berjumlah nol di titik K adalah akar-akar kubik satu, sama seperti tiga koefisien yang membuat orbital berdegenerasi siklopropenil (Contoh 13.22). Titik Dirac grafena dijamin oleh simetri kisi sarang lebah (kedua sublattice setara); bila simetri itu dirusak, misalnya pada boron nitrida heksagonal dengan atom B dan N yang berbeda $\alpha$-nya, celah terbuka (h-BN adalah isolator dengan celah sekitar 6 eV).
:::

::: {.contoh}
**Contoh 13.47 · Pembawa muatan dalam semikonduktor**

Pada 300 K ($kT = 0{,}02585$ eV), bandingkan faktor $e^{-E_g/2kT}$ untuk Ge (0,66 eV), Si (1,12 eV), dan intan (5,47 eV). Berapa perbandingan Si terhadap Ge, dan intan terhadap Si?

**Penyelesaian.** Ge: $e^{-12{,}77} = 2{,}9 \times 10^{-6}$. Si: $e^{-21{,}66} = 3{,}9 \times 10^{-10}$. Intan: $e^{-105{,}8} = 1{,}1 \times 10^{-46}$. Si/Ge $= 1{,}4 \times 10^{-4}$; intan/Si $= 2{,}9 \times 10^{-37}$.

**Memahami hasil.** Selisih celah 0,46 eV antara Ge dan Si mengurangi pembawa intrinsik hampir sepuluh ribu kali. Inilah salah satu alasan silikon menjadi bahan utama elektronik: arus bocor pada suhu operasi kecil, dan konduktivitas dapat diatur sepenuhnya dengan doping. Intan praktis tidak mempunyai pembawa intrinsik, sehingga ia isolator sempurna dan, sekaligus, penghantar panas terbaik di antara bahan alam (panas dibawa oleh getaran kisi, bukan elektron).
:::

::: {.contoh}
**Contoh 13.48 · Nanotabung: logam atau semikonduktor?**

Diameter nanotabung $(n, m)$ adalah $d = a\sqrt{n^2 + nm + m^2}/\pi$ dengan $a = 2{,}46$ Å. Untuk (10,10), (10,0), (9,0), (8,0), dan (12,4), tentukan apakah logam atau semikonduktor, hitung $d$, dan taksir celah untuk yang semikonduktor dengan $E_g \approx 2a_\text{CC}|\beta|/d$ ($a_\text{CC} = 1{,}42$ Å, $|\beta| = 2{,}7$ eV).

**Penyelesaian.** (10,10): $n - m = 0$, logam, $d = 13{,}6$ Å. (10,0): $n - m = 10$, semikonduktor, $d = 7{,}83$ Å, $E_g = 2(1{,}42)(2{,}7)/7{,}83 = 0{,}98$ eV. (9,0): $n - m = 9$, logam, $d = 7{,}05$ Å. (8,0): semikonduktor, $d = 6{,}26$ Å, $E_g = 1{,}22$ eV. (12,4): $n - m = 8$, semikonduktor, $d = 11{,}3$ Å, $E_g = 0{,}68$ eV.

**Memahami hasil.** Kira-kira sepertiga dari semua jenis nanotabung bersifat logam dan dua pertiga semikonduktor, dan celah semikonduktor berbanding terbalik dengan diameter. Untuk nanotabung zigzag kecil, kelengkungan kuat juga mencampur σ dan π dan sedikit mengubah aturan ini; tetapi untuk nanotabung berdiameter lebih dari sekitar 1 nm, model Hückel grafena yang digulung meramalkan sifat listriknya dengan sangat baik.
:::

::: {.kuis}
**Kuis cepat 13.14**

Mengapa model Hückel meramalkan bahwa grafena tidak mempunyai celah, sedangkan benzena (C₆H₆) mempunyai celah HOMO–LUMO $2|\beta|$? Petunjuk: titik-titik $\mathbf k$ mana yang "diizinkan" pada sebuah cincin enam atom?
:::
