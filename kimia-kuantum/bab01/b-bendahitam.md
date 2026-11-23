## 1.3 Radiasi benda hitam: Rayleigh–Jeans dan penurunan rumus Planck

Setiap benda bersuhu di atas nol mutlak memancarkan radiasi elektromagnetik, karena muatan-muatan di dalamnya bergetar secara termal. Pada suhu kamar radiasi itu hampir seluruhnya inframerah dan tidak terlihat. Kawat kompor listrik yang dipanaskan mula-mula membara merah tua (sekitar 900 K), lalu jingga, kuning, dan akhirnya putih (filamen lampu pijar, sekitar 2800 K). Warna benda panas memberi tahu suhunya. Tukang besi dan pembuat keramik memanfaatkan hal ini selama berabad-abad.

### Benda hitam dan rongga

Benda yang menyerap seluruh radiasi yang jatuh padanya disebut **benda hitam**. Kirchhoff (1859) membuktikan dari termodinamika bahwa benda hitam juga pemancar terbaik, dan bahwa spektrum pancarannya hanya bergantung pada suhu, bukan pada bahan atau bentuknya. Wujud nyata benda hitam yang paling baik adalah **rongga** berdinding buram dengan lubang kecil. Radiasi yang masuk lewat lubang terpantul berkali-kali di dalam dan hampir pasti terserap sebelum sempat keluar lagi. Jika dinding rongga dijaga pada suhu $T$, radiasi di dalamnya mencapai keseimbangan dengan dinding, dan yang bocor keluar lewat lubang adalah contoh radiasi benda hitam.

Spektrum radiasi itu dinyatakan dengan **kerapatan energi spektral** $\rho(\nu, T)$: energi radiasi tiap satuan volume rongga dalam selang frekuensi $\nu$ sampai $\nu + d\nu$ adalah $\rho(\nu, T)\,d\nu$. Satuannya J m⁻³ Hz⁻¹. Daya yang keluar tiap satuan luas lubang, disebut **eksitansi** $M$, berbanding lurus dengan kerapatan energi total $u = \int_0^\infty \rho\,d\nu$:

$$
M = \tfrac14 c\,u . \qquad \text{(1.4)}
$$

Faktor ¼ berasal dari arah radiasi yang acak (penurunannya ada di kotak "Lebih dalam" sesudah rumus Planck).

Pengukuran yang teliti pada akhir abad ke-19 (Lummer dan Pringsheim di Berlin) menghasilkan kurva seperti Gambar 1.2, dengan dua sifat empiris:

$$
M = \sigma T^4, \qquad \sigma = 5{,}670 \times 10^{-8}\ \text{W m}^{-2}\text{K}^{-4}, \qquad \text{(1.5)}
$$

$$
\lambda_\text{maks}\,T = b, \qquad b = 2{,}898 \times 10^{-3}\ \text{m·K} . \qquad \text{(1.6)}
$$

Persamaan (1.5) adalah **hukum Stefan–Boltzmann**; (1.6) adalah **hukum pergeseran Wien**. Menaikkan suhu dua kali lipat menaikkan daya pancar 16 kali dan menggeser puncak ke panjang gelombang setengahnya.

![Gambar 1.2 Spektrum benda hitam pada empat suhu. Titik menandai puncak; garis titik-titik menunjukkan pergeseran Wien. Kurva putus-putus adalah ramalan klasik Rayleigh–Jeans untuk 5000 K, yang cocok hanya pada panjang gelombang panjang dan naik tanpa batas ke arah ultraviolet.](fig/c_bendahitam.png){width=80%}

### Penurunan klasik: rumus Rayleigh–Jeans

Lord Rayleigh (1900) dan James Jeans (1905) menghitung $\rho(\nu, T)$ dengan fisika klasik yang paling baik. Penalarannya bersih dan hampir seluruhnya tetap benar dalam teori kuantum. Hanya satu langkahnya yang keliru. Karena itu penurunannya perlu diikuti dengan teliti. Gagasan pokoknya: radiasi dalam rongga adalah kumpulan **gelombang berdiri**, dan setiap gelombang berdiri berperilaku seperti satu osilator harmonik. Energi rongga sama dengan banyaknya osilator dikalikan energi rata-rata tiap osilator.

**Langkah 1: gelombang berdiri dalam satu dimensi.** Bayangkan dulu rongga satu dimensi sepanjang $L$ dengan dinding logam di $x = 0$ dan $x = L$. Medan listrik sejajar permukaan logam harus nol di dinding, sama seperti tali gitar yang terikat di kedua ujungnya (Gambar 1.3 kiri). Gelombang yang memenuhi syarat itu adalah $E(x, t) = E_0\sin(kx)\cos(\omega t)$ dengan $\sin(kL) = 0$, yaitu

$$
k = \frac{n\pi}{L}, \qquad n = 1, 2, 3, \ldots
$$

Setiap nilai $n$ adalah satu **mode** rongga.

**Langkah 2: tiga dimensi.** Dalam kubus bersisi $L$ syarat batas berlaku pada ketiga pasang dinding, sehingga komponen-komponen vektor gelombang harus

$$
k_x = \frac{n_x\pi}{L}, \quad k_y = \frac{n_y\pi}{L}, \quad k_z = \frac{n_z\pi}{L}, \qquad n_x, n_y, n_z = 1, 2, 3, \ldots
$$

Frekuensi mode berhubungan dengan besar vektor gelombang lewat $\nu = ck/2\pi$. Karena $k^2 = k_x^2 + k_y^2 + k_z^2$,

$$
\nu = \frac{c}{2L}\sqrt{n_x^2 + n_y^2 + n_z^2} = \frac{c\,n}{2L}, \qquad n \equiv \sqrt{n_x^2 + n_y^2 + n_z^2} . \qquad \text{(1.7)}
$$

**Langkah 3: menghitung mode.** Setiap mode adalah satu titik $(n_x, n_y, n_z)$ dengan koordinat bilangan bulat positif dalam "ruang $n$" (Gambar 1.3 kanan menunjukkan irisan dua dimensinya). Titik-titik itu membentuk kisi kubus bersisi satu, jadi setiap titik "menempati" volume satu. Mode yang frekuensinya paling tinggi $\nu$ adalah titik-titik di dalam bola berjari-jari $n = 2L\nu/c$, tetapi hanya pada oktan positif (seperdelapan bola). Untuk rongga yang besar dibandingkan panjang gelombang, $n$ sangat besar, dan banyaknya titik sama dengan volume oktan itu. Gelombang elektromagnetik transversal mempunyai **dua arah polarisasi** yang bebas untuk setiap vektor gelombang, sehingga banyaknya mode dikalikan dua:

$$
N(\nu) = 2 \times \frac18 \times \frac{4\pi}{3}n^3 = \frac{\pi}{3}\left(\frac{2L\nu}{c}\right)^3 = \frac{8\pi L^3\nu^3}{3c^3} .
$$

**Langkah 4: kerapatan mode.** Banyaknya mode dalam selang $\nu$ sampai $\nu + d\nu$ adalah $dN = (dN/d\nu)\,d\nu = (8\pi L^3\nu^2/c^3)\,d\nu$. Bagi dengan volume $V = L^3$:

$$
\boxed{\ g(\nu)\,d\nu = \frac{8\pi\nu^2}{c^3}\,d\nu\ } \qquad \text{(1.8)}
$$

adalah banyaknya mode tiap satuan volume. Hasil ini tidak bergantung pada bentuk rongga, asalkan rongga jauh lebih besar daripada panjang gelombang. Perhatikan faktor $\nu^2$: makin tinggi frekuensi, makin rapat mode-modenya, tanpa batas atas.

![Gambar 1.3 Kiri: mode-mode gelombang berdiri dalam rongga satu dimensi; medan listrik nol di dinding logam. Kanan: dalam ruang $n$ setiap mode adalah satu titik kisi. Mode yang frekuensinya kurang dari $\nu$ terletak di dalam seperempat lingkaran (dalam tiga dimensi: seperdelapan bola) berjari-jari $n = 2L\nu/c$.](fig/c_mode.png){width=84%}

**Langkah 5: energi rata-rata tiap mode.** Setiap mode adalah osilator harmonik: medan listrik dan medan magnetnya berayun sinusoidal, dan energinya terdiri atas dua suku kuadrat (energi medan listrik $\propto E^2$ dan energi medan magnet $\propto B^2$), persis seperti energi kinetik dan potensial pegas. Dalam keseimbangan termal dengan dinding pada suhu $T$, asas ekuipartisi memberikan setiap suku kuadrat rata-rata $\tfrac12kT$, sehingga

$$
\langle E \rangle_\text{klasik} = kT \qquad \text{(setiap mode, berapa pun frekuensinya).}
$$

**Langkah 6: rumus Rayleigh–Jeans.** Kalikan kerapatan mode dengan energi rata-rata tiap mode:

$$
\boxed{\ \rho_\text{RJ}(\nu, T) = \frac{8\pi\nu^2}{c^3}\,kT\ } \qquad \text{(1.9)}
$$

### Bencana ultraviolet

Rumus (1.9) cocok dengan percobaan pada frekuensi rendah (inframerah jauh). Tetapi ia naik sebanding $\nu^2$ tanpa batas, sedangkan kurva percobaan mencapai puncak lalu turun ke nol (Gambar 1.2). Lebih parah lagi, energi total rongga

$$
u = \int_0^\infty \rho_\text{RJ}\,d\nu = \frac{8\pi kT}{c^3}\int_0^\infty \nu^2\,d\nu = \infty .
$$

Rongga apa pun pada suhu apa pun berisi energi tak hingga, dan setiap benda panas seharusnya memancarkan ultraviolet dan sinar-X tanpa batas. Paul Ehrenfest kelak menyebut hal ini **bencana ultraviolet**. Langkah 1 sampai 4 hanyalah geometri gelombang dan tidak dapat disalahkan. Langkah 6 hanyalah perkalian. Kesalahannya harus ada di Langkah 5: **mode berfrekuensi tinggi tidak boleh mendapat jatah energi $kT$ penuh**.

### Penurunan Planck: energi osilator terkuantisasi

Pada bulan Oktober 1900 Max Planck menemukan rumus yang cocok dengan semua data. Dua bulan kemudian, pada 14 Desember 1900, ia menyajikan penurunannya, yang ia sendiri sebut "tindakan putus asa". Planck mengandaikan bahwa osilator berfrekuensi $\nu$ hanya boleh mempunyai energi kelipatan bulat sebuah kuantum $h\nu$:

$$
\boxed{\ E_n = nh\nu, \qquad n = 0, 1, 2, \ldots\ } \qquad \text{(1.10)}
$$

dengan $h$ tetapan baru, kini disebut **tetapan Planck**. Dalam tafsir modern, $n$ adalah banyaknya foton dalam mode itu (subbab 1.4).

Sekarang kita ulangi Langkah 5 dengan aturan baru. Mekanika statistik Boltzmann tetap berlaku: peluang osilator berada pada tingkat $E_n$ sebanding dengan **faktor Boltzmann** $e^{-E_n/kT}$. Energi rata-ratanya adalah rata-rata tertimbang

$$
\langle E \rangle = \frac{\sum_{n=0}^{\infty} E_n\,e^{-E_n/kT}}{\sum_{n=0}^{\infty} e^{-E_n/kT}} .
$$

**Penyebut.** Tulis $x = h\nu/kT$ dan $q = e^{-x}$, sehingga $e^{-E_n/kT} = q^n$. Penyebut adalah deret geometri dengan $0 < q < 1$:

$$
Z = \sum_{n=0}^\infty q^n = 1 + q + q^2 + \cdots = \frac{1}{1 - q} .
$$

Besaran $Z$ disebut **fungsi partisi** osilator; ia akan sering muncul dalam termodinamika statistik.

**Pembilang.** $\sum E_n q^n = h\nu\sum n\,q^n$. Deret $\sum nq^n$ diperoleh dengan menurunkan deret geometri terhadap $q$ lalu mengalikan dengan $q$:

$$
\sum_{n=0}^\infty n\,q^n = q\frac{d}{dq}\sum_{n=0}^\infty q^n = q\frac{d}{dq}\left(\frac{1}{1 - q}\right) = \frac{q}{(1 - q)^2} .
$$

**Hasil bagi.** 

$$
\langle E \rangle = h\nu\,\frac{q/(1 - q)^2}{1/(1 - q)} = h\nu\,\frac{q}{1 - q} = \frac{h\nu}{q^{-1} - 1},
$$

yaitu

$$
\boxed{\ \langle E \rangle = \frac{h\nu}{e^{h\nu/kT} - 1}\ } \qquad \text{(1.11)}
$$

Banyaknya kuanta rata-rata dalam mode itu, $\bar n = \langle E\rangle/h\nu = 1/(e^{h\nu/kT} - 1)$, adalah bentuk yang kelak dikenal sebagai **distribusi Bose–Einstein** untuk foton.

**Pemeriksaan limit.** Untuk frekuensi rendah, $x = h\nu/kT \ll 1$, deret Taylor $e^x \approx 1 + x + \tfrac12x^2$ memberikan

$$
\langle E \rangle \approx \frac{h\nu}{x + \tfrac12x^2} = \frac{kT}{1 + \tfrac12x} \approx kT\left(1 - \frac{x}{2}\right) \;\longrightarrow\; kT .
$$

Hasil klasik muncul kembali, sesuai asas korespondensi. Untuk frekuensi tinggi, $x \gg 1$, $\langle E\rangle \approx h\nu\,e^{-h\nu/kT}$, yang menuju nol secara eksponensial. Gambar 1.4 (kiri) memperlihatkan keduanya.

**Langkah 6 yang baru: rumus Planck.** Kalikan kerapatan mode (1.8) dengan (1.11):

$$
\boxed{\ \rho(\nu, T) = \frac{8\pi h\nu^3}{c^3}\,\frac{1}{e^{h\nu/kT} - 1}\ } \qquad \text{(1.12)}
$$

Dengan $h = 6{,}626 \times 10^{-34}$ J·s, rumus ini cocok dengan semua pengukuran pada semua suhu dan panjang gelombang.

![Gambar 1.4 Kiri: energi rata-rata satu mode (osilator) terhadap $h\nu/kT$. Fisika klasik memberi $kT$ untuk semua mode; menurut Planck, mode yang kuantumnya jauh lebih besar dari $kT$ hampir tidak mendapat energi. Kanan: kapasitas kalor molar padatan menurut model Einstein (subbab ini, bagian akhir); intan pada suhu kamar berada jauh di bawah nilai klasik.](fig/c_osilator.png){width=92%}

### Mengapa kuantisasi menghentikan bencana

Mengapa mode berfrekuensi tinggi "membeku"? Bayangkan mode dengan $h\nu = 10kT$. Mode itu hanya dapat menerima energi dalam paket $h\nu$. Peluang paket semacam itu tersedia dari gerak termal dinding sebanding dengan $e^{-10} \approx 4{,}5 \times 10^{-5}$. Hampir sepanjang waktu mode itu berada pada $n = 0$ dan tidak menyimpan energi sama sekali. Dalam teori klasik, mode yang sama dapat menerima energi dalam porsi sekecil apa pun, sehingga selalu mendapat jatah rata-rata $kT$. Kuantisasi tidak mengubah banyaknya mode; ia mengubah **cara energi dibagikan** kepada mode-mode itu. Gagasan inilah yang juga menjelaskan getaran N₂ yang membeku dan kapasitas kalor intan yang kecil.

### Bentuk panjang gelombang

Spektrometer biasanya mengukur terhadap panjang gelombang. Energi dalam selang $d\lambda$ harus sama dengan energi dalam selang $d\nu$ yang bersesuaian: $\rho_\lambda\,|d\lambda| = \rho_\nu\,|d\nu|$. Dari $\nu = c/\lambda$, $|d\nu/d\lambda| = c/\lambda^2$. Jadi

$$
\rho_\lambda(\lambda, T) = \rho_\nu\,\frac{c}{\lambda^2} = \frac{8\pi h(c/\lambda)^3}{c^3}\cdot\frac{c}{\lambda^2}\cdot\frac{1}{e^{hc/\lambda kT} - 1} = \frac{8\pi hc}{\lambda^5}\,\frac{1}{e^{hc/\lambda kT} - 1} . \qquad \text{(1.13)}
$$

Eksitansi spektral yang diplot dalam Gambar 1.2 adalah $M_\lambda = \tfrac14c\,\rho_\lambda = (2\pi hc^2/\lambda^5)/(e^{hc/\lambda kT} - 1)$.

::: {.inti}
**Rumus Planck dan dua limitnya.** Dengan $x = h\nu/kT = hc/\lambda kT$:

- $x \ll 1$ (panjang gelombang panjang): $\rho \approx 8\pi\nu^2kT/c^3$, rumus Rayleigh–Jeans; $h$ lenyap dari rumus.
- $x \gg 1$ (panjang gelombang pendek): $\rho \approx (8\pi h\nu^3/c^3)\,e^{-h\nu/kT}$, rumus Wien; mode membeku.
- Tetapan $h$ hanya berperan bila kuantum $h\nu$ sebanding dengan atau lebih besar daripada $kT$.
:::

::: {.dalam}
**Lebih dalam · Hukum Stefan–Boltzmann dan pergeseran Wien dari rumus Planck**

*Faktor ¼ dalam (1.4).* Radiasi dalam rongga bergerak dengan laju $c$ ke segala arah dengan sama rata. Ambil sebidang luas kecil pada dinding. Fraksi radiasi yang arahnya membentuk sudut $\theta$ sampai $\theta + d\theta$ dengan garis normal adalah $\tfrac12\sin\theta\,d\theta$ (luas pita pada bola satuan dibagi $4\pi$, setelah diintegralkan atas sudut azimut). Komponen kecepatannya menuju bidang $c\cos\theta$. Fluks energi yang menembus bidang dari satu sisi:

$$
M = u\int_0^{\pi/2} c\cos\theta\cdot\tfrac12\sin\theta\,d\theta = \frac{cu}{2}\left[\frac{\sin^2\theta}{2}\right]_0^{\pi/2} = \frac{cu}{4} .
$$

*Hukum Stefan–Boltzmann.* Integralkan (1.12) atas semua frekuensi dengan substitusi $x = h\nu/kT$, $d\nu = (kT/h)\,dx$:

$$
u = \frac{8\pi h}{c^3}\left(\frac{kT}{h}\right)^4\int_0^\infty\frac{x^3\,dx}{e^x - 1} .
$$

Integral itu dihitung dengan menulis $1/(e^x - 1) = e^{-x}/(1 - e^{-x}) = \sum_{m=1}^\infty e^{-mx}$ lalu mengintegralkan suku demi suku. Dengan $\int_0^\infty x^3 e^{-mx}\,dx = 6/m^4$:

$$
\int_0^\infty\frac{x^3\,dx}{e^x - 1} = 6\sum_{m=1}^\infty\frac{1}{m^4} = 6\cdot\frac{\pi^4}{90} = \frac{\pi^4}{15} = 6{,}4939 .
$$

Jadi $u = (8\pi^5k^4/15h^3c^3)\,T^4$, dan dengan $M = cu/4$:

$$
M = \sigma T^4, \qquad \sigma = \frac{2\pi^5k^4}{15h^3c^2} = 5{,}670 \times 10^{-8}\ \text{W m}^{-2}\text{K}^{-4} .
$$

Hukum empiris Stefan (1879) kini mempunyai tetapan yang dihitung dari $h$, $k$, dan $c$.

*Hukum pergeseran Wien.* Puncak $\rho_\lambda$ terjadi ketika $d\rho_\lambda/d\lambda = 0$. Tulis $x = hc/\lambda kT$, sehingga $dx/d\lambda = -x/\lambda$. Turunan $\lambda^{-5}(e^x - 1)^{-1}$:

$$
\frac{d}{d\lambda}\left[\frac{\lambda^{-5}}{e^x - 1}\right] = \frac{-5\lambda^{-6}}{e^x - 1} + \frac{\lambda^{-5}\,e^x\,(x/\lambda)}{(e^x - 1)^2} .
$$

Samakan dengan nol dan kalikan dengan $\lambda^6(e^x - 1)^2$: $-5(e^x - 1) + xe^x = 0$, atau

$$
x = 5\left(1 - e^{-x}\right) .
$$

Persamaan transenden ini diselesaikan dengan iterasi: mulai dari $x = 5$, ruas kanan memberi 4,9663, lalu 4,9652, lalu 4,9651, dan seterusnya menuju $x = 4{,}965\,114$. Maka

$$
\lambda_\text{maks}T = \frac{hc}{4{,}9651\,k} = 2{,}898 \times 10^{-3}\ \text{m·K} .
$$
:::

::: {.awas}
**Awas · Puncak terhadap λ tidak sama dengan puncak terhadap ν**

Jika spektrum yang sama diplot terhadap frekuensi, puncaknya terletak pada $h\nu_\text{maks}/kT = 2{,}821$, bukan 4,965. Untuk Matahari (5772 K), puncak terhadap panjang gelombang ada di 502 nm (hijau-biru), sedangkan puncak terhadap frekuensi ada di $3{,}39 \times 10^{14}$ Hz, yang bersesuaian dengan 884 nm (inframerah dekat). Keduanya benar; "letak puncak" bergantung pada variabel yang dipakai, karena $d\lambda$ dan $d\nu$ tidak sebanding. Jadi $\lambda_\text{maks}\nu_\text{maks} \ne c$.
:::

::: {.contoh}
**Contoh 1.7 · Suhu permukaan Matahari**

Spektrum Matahari di luar atmosfer berpuncak di sekitar 502 nm. Jari-jari Matahari $6{,}957 \times 10^8$ m. Anggap Matahari benda hitam. (a) Berapa suhu permukaannya? (b) Berapa daya pancar totalnya?

**Penyelesaian.** (a) Dari hukum Wien,

$$
T = \frac{b}{\lambda_\text{maks}} = \frac{2{,}898 \times 10^{-3}\text{ m·K}}{502 \times 10^{-9}\text{ m}} = 5770\text{ K}.
$$

\(b) Luas permukaan $4\pi R^2$, jadi

$$
P = 4\pi R^2\sigma T^4 = 4\pi(6{,}957 \times 10^8)^2(5{,}670 \times 10^{-8})(5772)^4 = 3{,}83 \times 10^{26}\ \text{W}.
$$

**Memahami hasil.** Nilai resmi suhu efektif Matahari 5772 K dan luminositasnya $3{,}828 \times 10^{26}$ W. Mata manusia paling peka di sekitar 555 nm, dekat puncak spektrum Matahari. Ini bukan kebetulan: penglihatan berevolusi di bawah cahaya Matahari. Fotosintesis pun memanfaatkan rentang yang sama.
:::

::: {.contoh}
**Contoh 1.8 · Berapa banyak mode dalam satu liter?**

Berapa banyak mode elektromagnetik dalam rongga bervolume 1,00 L yang panjang gelombangnya antara 500 nm dan 501 nm?

**Rencana.** Ubah kerapatan mode (1.8) ke panjang gelombang: dengan $\nu = c/\lambda$ dan $|d\nu| = c\,|d\lambda|/\lambda^2$, banyaknya mode tiap volume adalah $(8\pi/\lambda^4)\,d\lambda$.

**Penyelesaian.**

$$
dN = V\,\frac{8\pi}{\lambda^4}\,d\lambda = (1{,}00 \times 10^{-3})\,\frac{8\pi}{(500 \times 10^{-9})^4}\,(1{,}0 \times 10^{-9}) = 4{,}0 \times 10^{14} .
$$

**Memahami hasil.** Empat ratus triliun mode dalam selang selebar 1 nm saja! Inilah sebabnya penghitungan mode boleh memakai volume bola alih-alih menghitung titik satu per satu. Dan karena $dN \propto \lambda^{-4}$, banyaknya mode meledak ke arah panjang gelombang pendek. Dengan jatah $kT$ untuk setiap mode, bencana ultraviolet tidak terelakkan.
:::

::: {.contoh}
**Contoh 1.9 · Seberapa jauh Rayleigh–Jeans meleset?**

Hitung perbandingan $\rho_\text{RJ}/\rho_\text{Planck}$ untuk benda hitam 5000 K pada (a) 500 nm dan (b) 10 µm.

**Penyelesaian.** Dari (1.9) dan (1.12), $\rho_\text{RJ}/\rho_\text{Planck} = (e^x - 1)/x$ dengan $x = hc/\lambda kT$. Gunakan $hc/k = 1{,}4388 \times 10^{-2}$ m·K.

\(a) $x = 1{,}4388 \times 10^{-2}/(500 \times 10^{-9} \times 5000) = 5{,}755$; perbandingan $(e^{5{,}755} - 1)/5{,}755 = 54{,}7$.

\(b) $x = 0{,}2878$; perbandingan $(e^{0{,}2878} - 1)/0{,}2878 = 1{,}16$.

**Memahami hasil.** Dalam inframerah jauh teori klasik hanya meleset 16%, tetapi pada cahaya tampak meleset 55 kali, dan makin parah ke arah ultraviolet. Rayleigh dan Jeans sebenarnya membandingkan rumus mereka dengan data inframerah, dan di sana rumus itu tampak baik.
:::

::: {.contoh}
**Contoh 1.10 · Mengapa benda pada suhu kamar tidak berpendar**

Hitung banyaknya foton rata-rata $\bar n = 1/(e^{h\nu/kT} - 1)$ dalam satu mode cahaya hijau 500 nm pada (a) 300 K dan (b) 5000 K. Bandingkan dengan nilai klasik $kT/h\nu$.

**Penyelesaian.** Dengan $x = 1{,}4388 \times 10^{-2}/(\lambda T)$:

\(a) $x = 95{,}9$; $\bar n = e^{-95{,}9} = 2{,}2 \times 10^{-42}$. Klasik: $1/x = 0{,}010$.

\(b) $x = 5{,}755$; $\bar n = 1/(316{,}1 - 1) = 3{,}2 \times 10^{-3}$. Klasik: $1/x = 0{,}17$.

**Memahami hasil.** Pada suhu kamar mode cahaya tampak praktis kosong sama sekali: kemungkinannya $10^{-42}$, padahal fisika klasik memberinya sepersepuluh kuantum. Itulah sebabnya benda pada suhu kamar tampak gelap dan hanya terlihat karena memantulkan cahaya. Pada 5000 K pun satu mode hijau rata-rata hanya berisi tiga per seribu foton. Banyaknya mode yang luar biasa (Contoh 1.8) itulah yang membuat cahaya Matahari terang.
:::

::: {.contoh}
**Contoh 1.11 · Efisiensi lampu pijar**

Berapa persen daya pancar benda hitam yang jatuh dalam rentang tampak 400–700 nm pada (a) 2800 K, suhu filamen tungsten lampu pijar, dan (b) 5772 K, suhu Matahari?

**Rencana.** Fraksinya $F = \int_{400}^{700}M_\lambda\,d\lambda \big/ \int_0^\infty M_\lambda\,d\lambda$. Penyebut sama dengan $\sigma T^4$. Pembilang tidak mempunyai bentuk tertutup, jadi dihitung secara numerik (misalnya dengan `scipy.integrate.quad`).

**Penyelesaian.** Integrasi numerik memberikan (a) $F = 0{,}060$, yaitu 6,0%; (b) $F = 0{,}37$, yaitu 37%.

**Memahami hasil.** Puncak spektrum 2800 K berada di $b/T = 1035$ nm, dalam inframerah, sehingga sekitar 94% daya lampu pijar menjadi kalor, bukan cahaya. Lampu LED tidak bekerja sebagai benda hitam; ia memancarkan foton dari transisi elektron antarpita dalam semikonduktor, pada panjang gelombang yang dipilih. Itulah sebabnya LED beberapa kali lebih hemat.
:::

::: {.contoh}
**Contoh 1.12 · Planck mengukur tetapan Boltzmann dan bilangan Avogadro**

Dari data radiasi, Planck menentukan $h$ dan $k$ sekaligus. Ulangi penalarannya: dari $\sigma = 5{,}670 \times 10^{-8}$ W m⁻²K⁻⁴ dan $b = 2{,}898 \times 10^{-3}$ m·K, tentukan $h$ dan $k$, lalu $N_A = R/k$ dengan $R = 8{,}314$ J mol⁻¹K⁻¹.

**Rencana.** Ada dua persamaan: $b = hc/(4{,}9651\,k)$ dan $\sigma = 2\pi^5k^4/(15h^3c^2)$. Persamaan pertama memberikan perbandingan $a \equiv h/k$; masukkan ke persamaan kedua.

**Penyelesaian.** Dari hukum Wien,

$$
a = \frac{h}{k} = \frac{4{,}9651\,b}{c} = \frac{(4{,}9651)(2{,}898 \times 10^{-3})}{2{,}998 \times 10^8} = 4{,}799 \times 10^{-11}\ \text{K·s}.
$$

Ganti $h = ak$ dalam rumus $\sigma$: $\sigma = 2\pi^5k^4/(15a^3k^3c^2) = 2\pi^5k/(15a^3c^2)$, sehingga

$$
k = \frac{15\,\sigma\,a^3c^2}{2\pi^5} = \frac{15(5{,}670 \times 10^{-8})(4{,}799 \times 10^{-11})^3(2{,}998 \times 10^8)^2}{2\pi^5} = 1{,}381 \times 10^{-23}\ \text{J/K}.
$$

Lalu $h = ak = 6{,}626 \times 10^{-34}$ J·s, dan $N_A = R/k = 8{,}314/(1{,}381 \times 10^{-23}) = 6{,}02 \times 10^{23}$ mol⁻¹.

**Memahami hasil.** Pada tahun 1900 Planck memperoleh $k = 1{,}346 \times 10^{-23}$ J/K dan $N_A = 6{,}175 \times 10^{23}$ mol⁻¹ dari data yang tersedia saat itu, nilai bilangan Avogadro yang paling teliti pada zamannya, lebih baik daripada hasil teori kinetik gas. Dari $N_A$ dan tetapan Faraday ia juga menghitung muatan elementer. Teori kuantum lahir sekaligus sebagai alat pengukur atom.
:::

### Kuantisasi getaran molekul dan kapasitas kalor

Pada tahun 1907 Albert Einstein menyadari bahwa argumen Planck tidak khusus untuk cahaya. Setiap osilator, termasuk atom yang bergetar dalam kristal atau ikatan yang bergetar dalam molekul, seharusnya mempunyai energi yang terkuantisasi. Ia memodelkan padatan sebagai $3N_A$ osilator (tiap mol) yang semuanya bergetar dengan satu frekuensi $\nu_E$. Energi termal molar menurut (1.11) adalah

$$
U_m = 3N_A\,\frac{h\nu_E}{e^{h\nu_E/kT} - 1} .
$$

Turunkan terhadap $T$. Dengan $x = h\nu_E/kT$, $dx/dT = -x/T$:

$$
C_{V,m} = \frac{dU_m}{dT} = 3N_A h\nu_E\,\frac{e^x}{(e^x - 1)^2}\cdot\frac{x}{T} = 3N_Ak\,\frac{x^2e^x}{(e^x - 1)^2} .
$$

Dengan **suhu Einstein** $\theta_E \equiv h\nu_E/k$, sehingga $x = \theta_E/T$:

$$
\boxed{\ C_{V,m} = 3R\left(\frac{\theta_E}{T}\right)^2\frac{e^{\theta_E/T}}{\left(e^{\theta_E/T} - 1\right)^2}\ } \qquad \text{(1.14)}
$$

Untuk $T \gg \theta_E$ hasil ini menuju $3R$ (Dulong–Petit); untuk $T \ll \theta_E$ ia menuju nol (Gambar 1.4 kanan). Model Einstein menjelaskan secara kualitatif mengapa intan, dengan atom ringan dan ikatan kaku, menyimpang dari Dulong–Petit pada suhu kamar, sedangkan timbal dan tembaga tidak. Pada suhu sangat rendah model ini terlalu cepat menuju nol; Peter Debye (1912) memperbaikinya dengan memperhitungkan bahwa kristal mempunyai banyak frekuensi getaran, dan memperoleh hukum $C_V \propto T^3$ yang cocok dengan percobaan.

Penalaran yang sama berlaku untuk getaran satu ikatan dalam molekul gas. Sumbangan getaran pada $C_{V,m}$ adalah $R\,x^2e^x/(e^x - 1)^2$ dengan $x = h\nu/kT$, satu osilator untuk setiap mode getaran.

::: {.contoh}
**Contoh 1.13 · Kapasitas kalor intan menurut Einstein**

Einstein mencocokkan data intan dengan $\theta_E = 1320$ K. Hitung $C_{V,m}$ intan pada (a) 298 K, (b) 1000 K. (c) Berapa bilangan gelombang getaran yang bersesuaian dengan $\theta_E$?

**Penyelesaian.** (a) $x = 1320/298{,}15 = 4{,}427$; $e^x = 83{,}7$.

$$
C_{V,m} = 3R\,\frac{(4{,}427)^2(83{,}7)}{(82{,}7)^2} = (24{,}94)(0{,}240) = 5{,}98\ \text{J mol}^{-1}\text{K}^{-1}.
$$

\(b) $x = 1{,}320$; dengan cara yang sama $C_{V,m} = 21{,}6$ J mol⁻¹K⁻¹.

\(c) $\tilde\nu = k\theta_E/hc = (0{,}6950\ \text{cm}^{-1}/\text{K})(1320\ \text{K}) = 917$ cm⁻¹.

**Memahami hasil.** Nilai percobaan pada 298 K adalah 6,11 J mol⁻¹K⁻¹: model satu parameter ini sudah sangat baik. Bilangan gelombang 917 cm⁻¹ sebanding dengan getaran ulur ikatan C–C tunggal dalam molekul organik (sekitar 800–1200 cm⁻¹). Kapasitas kalor intan yang kecil dan getaran ikatan C–C dalam etana adalah gejala yang sama: kuantum getarannya besar dibandingkan $kT$.
:::

::: {.contoh}
**Contoh 1.14 · Getaran yang membeku dan yang tidak**

Bilangan gelombang getaran N₂, Cl₂, dan I₂ berturut-turut 2359, 560, dan 214,5 cm⁻¹. Hitung sumbangan getaran pada $C_{V,m}$ masing-masing pada 298 K, lalu $C_{V,m}$ total (translasi dan rotasi menyumbang $\tfrac52R = 20{,}79$ J mol⁻¹K⁻¹).

**Penyelesaian.** $x = \tilde\nu/(207{,}2\ \text{cm}^{-1})$, lalu $C_\text{vib} = R\,x^2e^x/(e^x - 1)^2$.

| Molekul | $x$ | $C_\text{vib}/R$ | $C_\text{vib}$ (J mol⁻¹K⁻¹) | $C_{V,m}$ total |
|---|---|---|---|---|
| N₂ | 11,38 | 0,0015 | 0,012 | 20,8 |
| Cl₂ | 2,70 | 0,563 | 4,68 | 25,5 |
| I₂ | 1,035 | 0,915 | 7,61 | 28,4 |

**Memahami hasil.** Molekul dengan ikatan lemah dan atom berat (I₂) bergetar lambat, kuantumnya kecil, dan getarannya hampir sepenuhnya aktif; nilainya mendekati ramalan klasik $\tfrac72R = 29{,}1$. N₂, dengan ikatan rangkap tiga yang kaku dan atom ringan, praktis tidak menyerap kalor lewat getaran. "Keganjilan terbesar teori molekul" abad ke-19 selesai dengan satu gagasan: energi getaran terkuantisasi.
:::

::: {.contoh}
**Contoh 1.15 · Tubuh manusia sebagai pemancar inframerah**

Kulit manusia bersuhu sekitar 310 K, berperilaku hampir sebagai benda hitam di inframerah (emisivitas 0,98), dan luas permukaan tubuh sekitar 1,8 m². (a) Di mana puncak pancarannya? (b) Berapa daya pancarnya, dan berapa daya bersih yang hilang bila dinding ruangan bersuhu 293 K?

**Penyelesaian.** (a) $\lambda_\text{maks} = 2{,}898 \times 10^{-3}/310 = 9{,}35 \times 10^{-6}$ m $= 9{,}3$ µm.

\(b) $P = \varepsilon\sigma AT^4 = (0{,}98)(5{,}670 \times 10^{-8})(1{,}8)(310)^4 = 924$ W. Tubuh juga menyerap dari dinding $\varepsilon\sigma A(293)^4 = 737$ W, sehingga kehilangan bersihnya 187 W.

**Memahami hasil.** Daya bersih ini sebanding dengan laju metabolisme orang yang beristirahat (sekitar 100 W) ditambah sedikit; itulah sebabnya orang tanpa pakaian merasa kedinginan dalam ruangan 20 °C. Kamera termal dan termometer dahi bekerja di sekitar 8–14 µm, tepat di puncak pancaran tubuh dan di "jendela" atmosfer tempat uap air dan CO₂ tidak banyak menyerap.
:::

::: {.terapan}
**Kaitan kimia · Efek rumah kaca dari dua kurva benda hitam**

Matahari memancar seperti benda hitam 5772 K dengan puncak di cahaya tampak; Bumi memancar seperti benda hitam sekitar 255–288 K dengan puncak di sekitar 10–11 µm. Kedua spektrum hampir tidak bertumpang tindih. Atmosfer meneruskan sebagian besar cahaya Matahari, tetapi molekul CO₂, H₂O, dan CH₄ menyerap kuat di inframerah tempat Bumi memancar. Molekul-molekul itu menyerap karena getarannya (misalnya tekukan CO₂ di 667 cm⁻¹, atau 15 µm) mengubah momen dipolnya, suatu aturan seleksi yang akan diturunkan di Bab 5 dan 9. N₂ dan O₂, yang membentuk 99% atmosfer, tidak menyerap inframerah karena getaran molekul diatomik homonuklir tidak mengubah momen dipol.
:::

::: {.kuis}
**Kuis cepat 1.3**

\(a) Jika suhu benda hitam dinaikkan dari 300 K menjadi 600 K, berapa kali lipat daya pancar totalnya, dan ke mana puncaknya bergeser? (b) Dalam penurunan Rayleigh–Jeans, langkah mana yang diubah oleh Planck: penghitungan mode atau energi rata-rata tiap mode?
:::
