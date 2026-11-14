## 10.10 Aturan seleksi elektronik

### Simetri keadaan elektronik

Transisi elektronik membawa molekul dari keadaan $\Psi_i$ ke $\Psi_f$ dengan menyerap foton. Dalam pendekatan dipol listrik, intensitasnya sebanding dengan kuadrat momen dipol transisi $\boldsymbol\mu_{fi} = \langle\Psi_f|\hat{\boldsymbol\mu}|\Psi_i\rangle$ (subbab 5.8; penurunan lengkapnya di subbab 8.12). Komponen $\hat\mu_x$, $\hat\mu_y$, $\hat\mu_z$ bertransformasi seperti $x$, $y$, $z$. Teorema integral lenyap (10.12) langsung memberikan aturan seleksi:

::: {.inti}
**Aturan seleksi simetri untuk transisi elektronik**

Transisi $\Psi_i \to \Psi_f$ diizinkan secara dipol listrik bila, untuk sedikitnya satu komponen $q = x, y, z$,

$$
\Gamma_f \times \Gamma_q \times \Gamma_i \ \text{memuat}\ A_1 . \qquad \text{(10.20)}
$$

Komponen $q$ yang memenuhi syarat ini adalah arah **polarisasi** transisi: cahaya yang medan listriknya sejajar $q$ yang diserap. Bila keadaan awal bersimetri total (seperti keadaan dasar hampir semua molekul stabil), syaratnya menjadi $\Gamma_f = \Gamma_q$.
:::

Untuk memakai aturan ini, kita perlu simetri keadaan, bukan hanya simetri orbital. Fungsi gelombang banyak elektron (determinan Slater, subbab 9.6) bertransformasi seperti hasil kali orbital-orbital yang terisi. Tiga aturan praktis:

1. **Kulit tertutup bersimetri total.** Orbital tak berdegenerasi yang terisi dua elektron menyumbang $\Gamma \times \Gamma = A_1$. Kelompok orbital berdegenerasi yang terisi penuh juga menyumbang $A_1$. Karena itu keadaan dasar molekul berkulit tertutup selalu $^1A_1$ (atau $^1A_{1g}$, $^1\Sigma_g^+$, dan seterusnya).
2. **Eksitasi satu elektron.** Bila satu elektron dipindahkan dari orbital terisi $\phi_a$ ke orbital kosong $\phi_b$, simetri ruang keadaan tereksitasi adalah $\Gamma_a \times \Gamma_b$. Spinnya dapat singlet atau triplet.
3. **Orbital berdegenerasi terisi sebagian** menghasilkan beberapa keadaan, seperti $E \times E = A_1 + A_2 + E$ di Contoh 10.29. Untuk konfigurasi lubang–partikel antara dua kelompok berdegenerasi, hasil kali langsungnya dapat memuat beberapa irrep, dan masing-masing menjadi keadaan tersendiri dengan energi berbeda.

Selain aturan simetri ruang, ada **aturan spin**: operator dipol tidak bekerja pada spin, sehingga transisi hanya diizinkan bila $\Delta S = 0$. Transisi singlet–triplet terlarang spin; ia menjadi lemah teramati hanya karena kopling spin–orbit (subbab 9.13), yang makin kuat untuk atom berat. Fosforesensi adalah contohnya (Bab 15).

### Aturan Laporte

Untuk molekul sentrosimetris, $x$, $y$, $z$ semuanya berlabel $u$. Hasil kali (10.20) memuat $A_{1g}$ hanya bila $\Gamma_f \times \Gamma_i$ berlabel $u$, yaitu bila paritas kedua keadaan berlawanan:

$$
g \leftrightarrow u \ \text{diizinkan}; \qquad g \leftrightarrow g \ \text{dan} \ u \leftrightarrow u \ \text{terlarang} .
$$

Inilah **aturan Laporte** yang sudah diturunkan dari paritas di subbab 4.11, kini sebagai kasus khusus teori grup. Akibat kimia yang paling terkenal: transisi d–d dalam kompleks oktahedral, yang menghubungkan dua keadaan berpusat di orbital d ($g$), terlarang.

### Kopling vibronik

Mengapa kompleks oktahedral tetap berwarna, dan mengapa pita benzena yang terlarang tetap tampak? Karena molekul bergetar. Fungsi gelombang yang lebih lengkap adalah hasil kali bagian elektronik dan bagian getaran (pendekatan Born–Oppenheimer, subbab 11.1), dan aturan seleksinya menjadi

$$
\Gamma_f^\text{el} \times \Gamma_f^\text{vib} \times \Gamma_q \times \Gamma_i^\text{el} \times \Gamma_i^\text{vib} \ \text{memuat}\ A_1 . \qquad \text{(10.21)}
$$

Bila molekul berangkat dari $v = 0$ (bersimetri total) dan berakhir dengan satu kuantum mode getaran $\Gamma_k$, transisi elektronik yang terlarang dapat diizinkan **secara vibronik** asalkan $\Gamma_k$ tepat "menutup kekurangan" simetrinya. Secara fisis, getaran yang tidak simetris sesaat merusak simetri molekul (misalnya menghilangkan pusat inversi), sehingga keadaan elektronik bercampur sedikit dengan keadaan lain yang transisinya diizinkan, dan "meminjam" intensitasnya. Intensitas pinjaman itu biasanya 10 sampai 1000 kali lebih lemah daripada transisi yang diizinkan penuh.

::: {.contoh}
**Contoh 10.49 · Formaldehida: transisi $n \to \pi^*$ yang gelap**

Dalam formaldehida ($C_{2v}$; molekul di bidang $yz$, ikatan C=O sepanjang $z$), pasangan elektron bebas oksigen yang paling tinggi ($n$) adalah orbital $2p_y$ O di bidang molekul ($b_2$), orbital π ikatan C=O adalah $b_1$, dan orbital π* juga $b_1$. Tentukan simetri keadaan $n\pi^*$ dan $\pi\pi^*$, dan apakah transisi dari keadaan dasar diizinkan.

**Penyelesaian.** Keadaan dasar: $^1A_1$. *n → π\**: $B_2 \times B_1 = A_2$, keadaan $^1A_2$. Dalam $C_{2v}$, $z$ adalah $A_1$, $x$ adalah $B_1$, $y$ adalah $B_2$; tidak ada yang $A_2$. Transisi $^1A_1 \to {}^1A_2$ **terlarang**. *π → π\**: $B_1 \times B_1 = A_1$, keadaan $^1A_1$; diizinkan dengan polarisasi $z$ (sepanjang ikatan C=O).

**Memahami hasil.** Pita $n \to \pi^*$ aldehida dan keton memang sangat lemah: untuk formaldehida sekitar 300 nm dan untuk aseton sekitar 275 nm, dengan koefisien ekstingsi molar hanya 10–20 L mol⁻¹ cm⁻¹, dibandingkan $10^4$ atau lebih untuk transisi yang diizinkan penuh. Pita itu muncul karena kopling vibronik dengan mode tekuk keluar bidang ($B_1$ atau $B_2$), dan juga karena geometri keadaan $n\pi^*$ formaldehida sendiri berbentuk piramida. Pita π → π* jauh lebih kuat dan berada jauh di ultraviolet vakum, di bawah sekitar 170 nm. Kelemahan pita $n \to \pi^*$ adalah alasan kromofor karbonil sederhana tampak tidak berwarna.
:::

::: {.contoh}
**Contoh 10.50 · Etilena: arah polarisasi**

Untuk etilena ($D_{2h}$; molekul di bidang $yz$, C=C sepanjang $z$, sumbu $x$ tegak lurus bidang), orbital π adalah $b_{3u}$ dan π* adalah $b_{2g}$. Tentukan simetri keadaan $\pi\pi^*$ dan polarisasi transisinya.

**Penyelesaian.** $B_{3u} \times B_{2g}$: kalikan karakter $(1, -1, -1, 1, -1, 1, 1, -1)$ dan $(1, -1, 1, -1, 1, -1, 1, -1)$ unsur demi unsur, hasilnya $(1, 1, -1, -1, -1, -1, 1, 1)$, yaitu $B_{1u}$. Dari tabel $D_{2h}$, $z$ bertransformasi sebagai $B_{1u}$. Transisi $^1A_g \to {}^1B_{1u}$ diizinkan dengan polarisasi $z$, sejajar ikatan C=C.

**Memahami hasil.** Pita π → π* etilena di sekitar 165 nm sangat kuat, dan percobaan dengan molekul yang terorientasi (dalam kristal atau film yang diregangkan) memastikan bahwa polarisasinya sepanjang ikatan rangkap. Secara intuitif: elektron berpindah dari orbital yang sefase di kedua C ke orbital yang berlawanan fase, sehingga selama transisi muatan berosilasi bolak-balik di sepanjang ikatan. Aturan polarisasi yang sama dipakai dalam spektroskopi dikroisme linear untuk menentukan orientasi zat warna dalam membran dan serat.
:::

::: {.contoh}
**Contoh 10.51 · Tiga pita benzena**

Konfigurasi dasar benzena ($D_{6h}$) adalah $(a_{2u})^2(e_{1g})^4$, dan orbital kosong terendah adalah $e_{2u}$ (Contoh 10.39). Eksitasi satu elektron $e_{1g} \to e_{2u}$ menghasilkan keadaan dengan simetri $E_{1g} \times E_{2u} = B_{1u} + B_{2u} + E_{1u}$. Dalam $D_{6h}$, $(x, y)$ adalah $E_{1u}$ dan $z$ adalah $A_{2u}$. Mana yang diizinkan? Hubungkan dengan pita serapan benzena di 255 nm ($\varepsilon \approx 200$), 204 nm ($\varepsilon \approx 7400$), dan 184 nm ($\varepsilon \approx 60\,000$).

**Penyelesaian.** Dari keadaan dasar $^1A_{1g}$, hanya keadaan yang irrepnya $E_{1u}$ atau $A_{2u}$ yang dapat dicapai. Dari tiga keadaan singlet, hanya $^1E_{1u}$ yang diizinkan, dengan polarisasi di bidang cincin. Keadaan $^1B_{2u}$ dan $^1B_{1u}$ terlarang simetri.

**Memahami hasil.** Pita terkuat, 184 nm, adalah $^1A_{1g} \to {}^1E_{1u}$. Pita 255 nm yang lemah dengan struktur getaran yang indah adalah $^1A_{1g} \to {}^1B_{2u}$, yang dipinjami intensitas oleh mode getaran $e_{2g}$: menurut (10.21), $B_{2u} \times E_{2g} \times E_{1u}$ memuat $A_{1g}$ karena $B_{2u} \times E_{1u} = E_{2g}$. Deret puncaknya memang berjarak sekitar 920 cm⁻¹ (mode napas $a_{1g}$ di keadaan tereksitasi) dan dimulai bukan dari titik 0–0 melainkan dari satu kuantum mode $e_{2g}$, tanda pasti kopling vibronik. Pita 204 nm ($^1B_{1u}$) juga terlarang dan meminjam intensitas. Teori orbital Hückel yang hanya memberi satu energi eksitasi $e_{1g} \to e_{2u}$ tidak dapat menjelaskan tiga pita ini; teori grup dan interaksi antarelektron diperlukan.
:::

::: {.contoh}
**Contoh 10.52 · Merah muda pucat dan biru pekat**

Larutan [Co(H₂O)₆]²⁺ (oktahedral) berwarna merah muda pucat dengan pita d–d utama $\varepsilon \approx 5$ L mol⁻¹ cm⁻¹ di sekitar 510 nm. Larutan [CoCl₄]²⁻ (tetrahedral) berwarna biru pekat dengan pita d–d $\varepsilon \approx 600$ di sekitar 690 nm. Jelaskan perbedaan intensitas sekitar 120 kali itu dengan simetri.

**Penyelesaian.** Dalam $O_h$, orbital d adalah $e_g + t_{2g}$ dan semua keadaan yang berasal dari konfigurasi $d^n$ berlabel $g$. Transisi antara keadaan $g$ terlarang Laporte. Intensitas kecil berasal dari kopling vibronik dengan getaran $u$ yang sesaat menghilangkan pusat inversi. Dalam $T_d$ tidak ada pusat inversi, sehingga aturan Laporte tidak berlaku. Lebih lagi, dalam $T_d$ orbital $d_{xy}$, $d_{xz}$, $d_{yz}$ ($t_2$) berirrep sama dengan orbital $4p$ ($t_2$), sehingga keduanya bercampur, dan transisi "d–d" memperoleh sebagian karakter d → p yang diizinkan.

**Memahami hasil.** Pola ini umum: kompleks tetrahedral biasanya berwarna jauh lebih pekat daripada kompleks oktahedral logam yang sama. Perubahan warna kertas indikator silika gel berkobalt (biru saat kering, merah muda saat lembap) berasal dari perubahan geometri di sekitar Co²⁺ dari tetrahedral menjadi oktahedral ketika air terikat. Kompleks Mn²⁺ oktahedral spin tinggi ($d^5$) hampir tidak berwarna, karena transisi d–d-nya terlarang Laporte **dan** terlarang spin sekaligus, dengan $\varepsilon$ di bawah 0,1. Warna intens seperti ungu permanganat berasal dari transisi transfer muatan yang diizinkan (Bab 14).
:::

::: {.contoh}
**Contoh 10.53 · Serapan pertama air**

Transisi elektronik pertama H₂O memindahkan elektron dari HOMO $1b_1$ ke orbital kosong terendah $4a_1$. Tentukan simetri keadaan tereksitasi dan polarisasi transisinya.

**Penyelesaian.** $B_1 \times A_1 = B_1$, keadaan $^1B_1$. Dalam $C_{2v}$, $x$ bertransformasi sebagai $B_1$, sehingga transisi diizinkan dengan polarisasi $x$, tegak lurus bidang molekul.

**Memahami hasil.** Air mulai menyerap kuat di bawah sekitar 190 nm, dengan pita pertama berpuncak sekitar 167 nm (7,4 eV). Pita itu lebar dan tanpa struktur, karena orbital $4a_1$ bersifat antiikatan O–H: keadaan tereksitasinya disosiatif dan segera terurai menjadi H + OH. Inilah sebabnya air transparan di seluruh daerah tampak dan ultraviolet dekat (sehingga kehidupan di laut dangkal mendapat cahaya), tetapi mengalami fotolisis di atmosfer atas oleh ultraviolet vakum matahari.
:::

::: {.kuis}
**Kuis cepat 10.10**

\(a) Dalam kompleks oktahedral, apakah transisi $t_{2g} \to e_g$ diizinkan? (b) Dalam $C_{2v}$, apakah transisi $^1A_1 \to {}^1B_2$ diizinkan, dan ke arah mana polarisasinya? (c) Mengapa transisi singlet–triplet pada molekul organik ringan sangat lemah?
:::

## 10.11 Kiralitas dan aktivitas optik

### Syarat simetri kiralitas

Molekul disebut **kiral** bila tidak dapat ditumpangkan tepat pada bayangan cerminnya, seperti tangan kiri dan tangan kanan. Kedua bentuk itu disebut **enantiomer**. Pertanyaan geometri "dapatkah ditumpangkan?" ternyata mempunyai jawaban teori grup yang sangat sederhana:

::: {.inti}
**Kriteria kiralitas**

Sebuah molekul kiral **jika dan hanya jika** ia tidak mempunyai sumbu putar tak sejati $S_n$ untuk $n$ berapa pun. Karena $S_1 = \sigma$ dan $S_2 = i$, molekul dengan bidang cermin atau pusat inversi pasti tidak kiral. Molekul kiral hanya dapat termasuk grup yang semua operasinya putaran sejati: $C_1$, $C_n$, $D_n$, $T$, $O$, dan $I$.
:::

Alasannya sebagai berikut. Bayangan cermin molekul $M$ dapat dibuat dengan pencerminan pada bidang apa pun; pilih bidang $\sigma$ yang tegak lurus sebuah sumbu $C_n$ melalui pusat molekul. Bila molekul mempunyai operasi $S_n = \sigma C_n$, maka $\sigma C_nM = M$, sehingga bayangan cerminnya $\sigma M = C_n^{-1}M$: bayangan itu tidak lain adalah molekul semula yang diputar. Putaran adalah gerak fisis yang dapat dilakukan, sehingga bayangan dapat ditumpangkan. Sebaliknya, bila tidak ada operasi tak sejati sama sekali, tidak ada putaran yang dapat mengubah $M$ menjadi bayangannya.

Kriteria ini lebih umum daripada aturan "atom karbon asimetris" dalam kimia organik. Molekul tanpa atom karbon asimetris dapat kiral (alena tersubstitusi, heliksena, bifenil terpuntir, kompleks logam), dan molekul dengan dua atom karbon asimetris dapat tidak kiral (senyawa meso). Yang menentukan selalu ada atau tidaknya sumbu tak sejati.

::: {.contoh}
**Contoh 10.54 · Kiral atau tidak?**

Tentukan grup titik dan kiralitas: (a) CHFClBr; (b) H₂O₂; (c) [Co(en)₃]³⁺ (en = etilenadiamina, ligan bidentat); (d) 1,3-dikloroalena; (e) *trans*- dan *cis*-1,2-dimetilsiklopropana; (f) 1,3,5,7-tetrametilsiklooktatetraena.

**Penyelesaian.** (a) $C_1$: kiral. (b) $C_2$: kiral, tetapi kedua enantiomer saling berubah sangat cepat melalui rotasi di sekitar ikatan O–O (penghalang hanya sekitar 4 kJ/mol), sehingga tidak dapat dipisahkan. (c) $D_3$: tiga cincin kelat tersusun seperti baling-baling; kiral, dengan enantiomer Δ dan Λ. (d) $C_2$: kiral, meskipun tidak ada atom karbon asimetris. (e) *trans*: $C_2$, kiral; *cis*: $C_s$ (bidang cermin membagi dua cincin), tidak kiral, meskipun mempunyai dua pusat stereogenik (meso). (f) $S_4$: tidak kiral, meskipun tidak mempunyai bidang cermin maupun pusat inversi.

**Memahami hasil.** Kasus (f) adalah contoh paling meyakinkan bahwa yang menentukan adalah sumbu $S_n$, bukan bidang cermin. Kasus (c) bersejarah: Alfred Werner pada 1911 memisahkan enantiomer kompleks kobalt etilenadiamina, sehingga membuktikan bahwa kiralitas adalah sifat geometri ruang, bukan sifat khusus atom karbon, dan sekaligus menguatkan teorinya tentang struktur oktahedral kompleks.
:::

### Aktivitas optik

Larutan molekul kiral memutar bidang polarisasi cahaya terpolarisasi linear. Cahaya terpolarisasi linear dapat dipandang sebagai jumlah dua gelombang terpolarisasi melingkar, kiri dan kanan, dengan amplitudo sama (*Fisika Umum*, Bab 14). Molekul kiral berinteraksi berbeda dengan keduanya: indeks biasnya berbeda ($n_L \ne n_R$), sehingga kedua komponen merambat dengan laju berbeda dan bidang polarisasi resultannya berputar. Gejala ini disebut **rotasi optik**. Di dekat pita serapan, kedua komponen juga diserap berbeda ($\varepsilon_L \ne \varepsilon_R$), dan gejala ini disebut **dikroisme melingkar** (*circular dichroism*, CD).

Mekanika kuantum menunjukkan bahwa kekuatan CD sebuah transisi $0 \to n$ ditentukan oleh **kekuatan rotasi**

$$
R_{0n} = \mathrm{Im}\left(\boldsymbol\mu_{0n} \cdot \mathbf m_{n0}\right) , \qquad \text{(10.22)}
$$

dengan $\boldsymbol\mu_{0n}$ momen dipol listrik transisi dan $\mathbf m_{n0}$ momen dipol magnet transisi. Momen dipol magnet berasal dari operator momentum sudut ($\hat{\mathbf m} \propto \hat{\mathbf L}$, subbab 6.1), sehingga komponennya bertransformasi seperti rotasi $R_x$, $R_y$, $R_z$, bukan seperti $x$, $y$, $z$. Vektor seperti ini disebut **vektor aksial**: ia tidak berubah oleh inversi, sedangkan vektor polar seperti $\boldsymbol\mu$ berbalik.

Akibatnya, hasil kali skalar $\boldsymbol\mu \cdot \mathbf m$ adalah **pseudoskalar**: tidak berubah oleh putaran, tetapi berubah tanda oleh setiap operasi tak sejati (pencerminan, inversi, $S_n$). Larutan berisi molekul yang berorientasi acak hanya merasakan besaran yang tidak bergantung pada orientasi, yaitu skalar atau pseudoskalar seperti $R_{0n}$. Bila molekul mempunyai operasi tak sejati $S$, maka $R_{0n}$ harus sama dengan dirinya sendiri (karena $S$ adalah simetri molekul) dan sekaligus sama dengan negatifnya (karena $R_{0n}$ pseudoskalar). Satu-satunya kemungkinan: $R_{0n} = 0$. Dalam bahasa tabel karakter, pseudoskalar bertransformasi menurut irrep yang karakternya $+1$ untuk putaran dan $-1$ untuk operasi tak sejati; irrep itu bersimetri total hanya dalam grup tanpa operasi tak sejati.

::: {.inti}
**Aktivitas optik dan simetri**

Molekul yang berorientasi acak (larutan, gas, cairan) aktif optik **jika dan hanya jika** ia kiral. Kekuatan rotasi $R_{0n}$ adalah pseudoskalar; ia lenyap untuk setiap molekul yang mempunyai sumbu $S_n$. Enantiomer mempunyai spektrum serapan biasa yang identik, tetapi kekuatan rotasi dan sudut rotasi optik yang sama besar dan berlawanan tanda.
:::

::: {.contoh}
**Contoh 10.55 · Pseudoskalar dalam $C_{2v}$ dan $C_2$**

Pakai tabel karakter untuk menunjukkan bahwa molekul $C_{2v}$ (seperti H₂O) tidak dapat aktif optik, sedangkan molekul $C_2$ (seperti H₂O₂) dapat.

**Penyelesaian.** Dalam $C_{2v}$: $\mu_x$ ($B_1$) dan $m_x$ ($R_x$: $B_2$) memberi $B_1 \times B_2 = A_2$; $\mu_y$ ($B_2$) dan $m_y$ ($R_y$: $B_1$) memberi $A_2$; $\mu_z$ ($A_1$) dan $m_z$ ($R_z$: $A_2$) memberi $A_2$. Ketiga suku $\boldsymbol\mu \cdot \mathbf m$ bertransformasi sebagai $A_2$, bukan $A_1$, sehingga integral orientasi rata-ratanya nol. (Periksa: $A_2$ berkarakter $+1$ untuk $E$ dan $C_2$, $-1$ untuk kedua cermin, sesuai definisi pseudoskalar.) Dalam $C_2$ (irrep $A$ dan $B$): $z$ dan $R_z$ keduanya $A$; $x$, $y$, $R_x$, $R_y$ semuanya $B$. Hasil kali $\mu_zm_z$ adalah $A \times A = A$, dan $\mu_xm_x$ adalah $B \times B = A$: bersimetri total, sehingga $R_{0n}$ boleh tidak nol.

**Memahami hasil.** Perhatikan bahwa dalam $C_{2v}$, $x$ dan $R_y$ kebetulan berada di irrep yang sama ($B_1$). Itu tidak cukup untuk aktivitas optik; yang diperlukan adalah komponen sejajar, $\mu_x$ dengan $m_x$, dan hasil kalinya selalu $A_2$. Pernyataan yang bersih adalah: pseudoskalar harus bersimetri total, dan itu terjadi tepat dalam grup kiral.
:::

### Rotasi jenis dan kelebihan enantiomer

Sudut putar $\alpha$ yang terukur dalam polarimeter sebanding dengan panjang lintasan $l$ dan konsentrasi $c$. Sifat zatnya dinyatakan dengan **rotasi jenis**

$$
[\alpha]_\lambda^T = \frac{\alpha}{l\,c} , \qquad \text{(10.23)}
$$

dengan $l$ dalam desimeter dan $c$ dalam g/mL (satuannya biasanya tidak ditulis, cukup "derajat"). Panjang gelombang yang lazim adalah garis D natrium (589 nm). Campuran enantiomer berputar sebanding dengan selisih jumlahnya, sehingga **kelebihan enantiomer** (*enantiomeric excess*, ee) dapat dihitung dari rotasi:

$$
\text{ee} = \frac{[R] - [S]}{[R] + [S]} = \frac{[\alpha]_\text{sampel}}{[\alpha]_\text{murni}} . \qquad \text{(10.24)}
$$

Campuran rasemat (50 : 50) mempunyai ee nol dan tidak memutar cahaya, meskipun setiap molekulnya kiral.

::: {.contoh}
**Contoh 10.56 · Rotasi larutan sukrosa**

Rotasi jenis sukrosa $[\alpha]_D^{20} = +66{,}5°$. Berapa sudut putar larutan 10,0 g sukrosa dalam 100 mL air dalam tabung polarimeter sepanjang 20,0 cm?

**Penyelesaian.** $c = 10{,}0/100 = 0{,}100$ g/mL, $l = 2{,}00$ dm. Dengan (10.23): $\alpha = [\alpha]lc = 66{,}5 \times 2{,}00 \times 0{,}100 = +13{,}3°$.

**Memahami hasil.** Tanda positif berarti searah jarum jam bila dilihat oleh pengamat yang menghadap sumber cahaya (dekstrorotatori). Industri gula memakai polarimeter ("sakarimeter") untuk menentukan kadar gula secara cepat. Ketika sukrosa dihidrolisis menjadi campuran glukosa ($+52{,}7°$) dan fruktosa ($-92°$), rotasinya berubah tanda menjadi negatif; karena itu campuran hasil hidrolisis disebut gula *invert*.
:::

::: {.contoh}
**Contoh 10.57 · Kelebihan enantiomer dari polarimetri**

Senyawa kiral X murni mempunyai $[\alpha]_D = +40{,}0°$. Hasil sintesis asimetris memberikan $[\alpha]_D = +28{,}0°$ pada kondisi yang sama. Hitung ee dan perbandingan kedua enantiomer.

**Penyelesaian.** ee $= 28{,}0/40{,}0 = 0{,}700 = 70{,}0\%$. Bila fraksi enantiomer (+) adalah $f$, maka $f - (1 - f) = 0{,}700$, sehingga $f = 0{,}850$: perbandingan 85 : 15.

**Memahami hasil.** Polarimetri cepat tetapi kasar: hasilnya peka terhadap pengotor yang memutar cahaya dan terhadap suhu serta pelarut. Industri farmasi kini memakai kromatografi dengan fase diam kiral untuk mengukur ee secara langsung. Namun prinsipnya sama: enantiomer hanya dapat dibedakan oleh sesuatu yang juga kiral, entah cahaya terpolarisasi melingkar atau fase diam kiral.
:::

::: {.contoh}
**Contoh 10.58 · Heliks yang memutar cahaya sangat kuat**

Heksaheliksena, enam cincin benzena yang terkondensasi *orto* membentuk heliks ($C_2$), mempunyai $[\alpha]_D$ sekitar $3600°$, kira-kira 54 kali rotasi jenis sukrosa. Mengapa molekul heliks memberikan rotasi optik yang begitu besar?

**Penyelesaian.** Menurut (10.22), rotasi optik besar memerlukan transisi yang sekaligus mempunyai momen dipol listrik dan momen dipol magnet yang besar dan sejajar. Pada heliks, elektron π yang berpindah sepanjang rangka heliks bergerak maju (komponen sepanjang sumbu heliks, menghasilkan $\boldsymbol\mu$) sambil berputar (menghasilkan $\mathbf m$ sepanjang sumbu yang sama), seperti arus dalam kumparan pegas. Kedua momen itu otomatis sejajar atau antisejajar, dan keduanya besar karena sistem π-nya terdelokalisasi luas. Pada sukrosa, kiralitas hanya berupa susunan atom tunggal di sekitar pusat stereogenik, dan transisi-transisinya berada di ultraviolet jauh.

**Memahami hasil.** Arah putaran heliks (tangan kiri atau kanan) menentukan tanda $R_{0n}$. Hubungan ini dipakai terbalik dalam spektroskopi CD protein: heliks α (tangan kanan) memberikan pita CD negatif khas di 222 dan 208 nm dan pita positif di sekitar 192 nm, sedangkan lembaran β memberikan pola lain (Gambar 10.9). Dari spektrum CD, persentase heliks dan lembaran dalam protein dapat diperkirakan dalam beberapa menit.
:::

![Gambar 10.9 Spektrum dikroisme melingkar skematis untuk protein dengan struktur sekunder heliks α (biru), lembaran β (hijau), dan acak (jingga). Bentuk kurva digambar sebagai jumlah pita Gauss dan hanya kualitatif; posisi pita khas heliks α di 192, 208, dan 222 nm.](fig/c_cd.png){width=78%}

::: {.terapan}
**Kaitan kimia · Obat kiral**

Reseptor dan enzim dalam tubuh tersusun dari asam amino L dan gula D, sehingga bersifat kiral, dan dapat membedakan enantiomer obat seperti tangan kanan membedakan sarung tangan kiri dan kanan. Kedua enantiomer sebuah obat mempunyai energi, titik lebur, dan spektrum IR yang identik, karena Hamiltonian molekul tidak berubah oleh pencerminan, tetapi efek biologisnya bisa sangat berbeda. Enantiomer (S) ibuprofen adalah bentuk yang aktif sebagai antiradang; (R)-karvon berbau daun mint sedangkan (S)-karvon berbau jintan. Contoh yang paling tragis adalah talidomida pada 1950-an, dengan satu enantiomer yang bersifat teratogenik; kasus ini rumit karena kedua enantiomernya saling berubah di dalam tubuh. Sejak itu, badan pengawas obat menuntut agar sifat setiap enantiomer obat kiral diuji tersendiri, dan sintesis asimetris menjadi salah satu bidang terpenting kimia organik.
:::

::: {.kuis}
**Kuis cepat 10.11**

\(a) Apakah molekul $D_{2d}$ dapat kiral? (b) Mengapa campuran rasemat tidak memutar bidang polarisasi? (c) Momen dipol magnet transisi bertransformasi seperti apa dalam tabel karakter?
:::
