## 8.10 Efek Stark dan polarisabilitas

### Atom dan molekul dalam medan listrik

Letakkan atom atau molekul dalam medan listrik seragam $\mathbf F$ sepanjang sumbu $z$. Muatan $q_i$ di posisi $\mathbf r_i$ mempunyai energi potensial $-q_iFz_i$, sehingga perturbasinya

$$
\hat H' = -F\sum_iq_iz_i = -\hat\mu_zF , \qquad \hat\mu_z = \sum_iq_iz_i , \qquad \text{(8.45)}
$$

dengan $\hat\mu_z$ operator momen dipol. Untuk satu elektron dalam satuan atom ($q = -1$), $\hat H' = Fz$. Medan laboratorium sangat lemah dibandingkan medan dalam atom (Contoh 8.3), sehingga teori perturbasi orde rendah sangat tepat. Pergeseran tingkat energi akibat medan listrik disebut **efek Stark**, dari nama Johannes Stark yang mengamatinya pada garis Balmer hidrogen tahun 1913.

Uraikan energi suatu keadaan sebagai deret pangkat kuat medan:

$$
E(F) = E^{(0)} - \mu_0F - \tfrac12\alpha F^2 - \cdots \qquad \text{(8.46)}
$$

Koefisien suku linear, $\mu_0 = -dE/dF$ di $F = 0$, adalah **momen dipol permanen** keadaan itu, dan koefisien suku kuadrat, $\alpha = -d^2E/dF^2$, adalah **polarisabilitas** (dalam arah $z$). Membandingkan dengan deret perturbasi memberi rumus untuk keduanya.

### Orde pertama: momen dipol permanen

$E^{(1)} = \langle n|\hat H'|n\rangle = -F\langle n|\hat\mu_z|n\rangle$, sehingga $\mu_0 = \langle n|\hat\mu_z|n\rangle$: momen dipol permanen adalah nilai rata-rata operator dipol. Untuk atom dalam keadaan tak terdegenerasi, fungsi gelombangnya mempunyai paritas tertentu (genap atau ganjil terhadap inversi, subbab 4.11), sehingga $|\psi|^2$ genap dan $z|\psi|^2$ ganjil, dan integralnya nol. **Atom dalam keadaan tak terdegenerasi tidak mempunyai momen dipol permanen**, dan tidak menunjukkan efek Stark linear. Molekul polar seperti HCl, yang tidak mempunyai pusat inversi, mempunyai $\mu_0 \ne 0$ dalam kerangka molekul; tetapi molekul yang berotasi bebas dalam keadaan rotasi tertentu juga tidak mempunyai dipol rata-rata dalam kerangka laboratorium, dan efek Starknya biasanya kuadratik (Contoh 8.49).

### Orde kedua: polarisabilitas

Dengan (8.35) dan $\hat H' = -\hat\mu_zF$,

$$
E_n^{(2)} = F^2\sum_{m\ne n}\frac{|\langle m|\hat\mu_z|n\rangle|^2}{E_n - E_m} \equiv -\tfrac12\alpha F^2 ,
$$

sehingga polarisabilitas keadaan dasar adalah

$$
\alpha = 2\sum_{m\ne1}\frac{|\langle m|\hat\mu_z|1\rangle|^2}{E_m - E_1} . \qquad \text{(8.47)}
$$

Rumus **jumlah atas keadaan** ini mengatakan bahwa polarisabilitas besar bila (1) ada keadaan tereksitasi yang terhubung kuat dengan keadaan dasar melalui operator dipol (momen dipol transisi besar, subbab 8.12), dan (2) keadaan itu dekat dalam energi. Molekul berwarna, yang mempunyai transisi kuat pada energi rendah, karena itu lebih mudah dipolarisasi daripada molekul tak berwarna yang hanya menyerap di ultraungu jauh.

Fungsi gelombang orde pertama (8.34) mencampurkan keadaan-keadaan $m$ yang terhubung oleh $\hat\mu_z$, sehingga awan elektron bergeser ke arah yang menurunkan energi. Momen dipol terinduksi $\mu_\text{ind} = -dE/dF = \alpha F$ (untuk atom) adalah hasil langsung pergeseran itu.

Satuan polarisabilitas dalam SI adalah C² m² J⁻¹ (atau C m² V⁻¹). Yang lebih lazim dalam kimia adalah **volume polarisabilitas** $\alpha' = \alpha/4\pi\varepsilon_0$, dalam Å³. Dalam satuan atom, $\alpha$ dinyatakan dalam $a_0^3$, dan $1\ a_0^3 = 0{,}148\,18$ Å³.

::: {.inti}
**Efek Stark**

$$
E(F) = E^{(0)} - \mu_0F - \tfrac12\alpha F^2 , \qquad \mu_0 = \langle n|\hat\mu_z|n\rangle , \qquad \alpha = 2\sum_{m\ne1}\frac{|\langle m|\hat\mu_z|1\rangle|^2}{E_m - E_1} .
$$

Atom dalam keadaan tak terdegenerasi hanya menunjukkan efek Stark kuadratik. Efek linear muncul bila ada degenerasi antara keadaan berparitas berlawanan.
:::

::: {.dalam}
**Lebih dalam: polarisabilitas hidrogen yang eksak (metode Dalgarno–Lewis)**

Jumlah (8.47) untuk hidrogen melibatkan semua keadaan $np$ dan kontinu, dan tidak mudah dijumlahkan langsung. Dalgarno dan Lewis (1955) menunjukkan cara lain: cari fungsi $\psi^{(1)}$ langsung dari persamaan orde pertama (8.31), $(\hat H^{(0)} - E^{(0)})\psi^{(1)} = -(\hat H' - E^{(1)})\psi^{(0)}$. Untuk 1s dengan $\hat H' = Fz = Fr\cos\theta$ dan $E^{(1)} = 0$, coba $\psi^{(1)} = Ff(r)\cos\theta\,\psi_{1s}$. Substitusi ke persamaan dan penyederhanaan (Laplasian dalam koordinat bola, subbab 6.2) memberi persamaan diferensial biasa untuk $f$ yang dipenuhi oleh

$$
f(r) = -\left(r + \tfrac12r^2\right) .
$$

(Pembaca dapat memeriksa langsung bahwa $(-\tfrac12\nabla^2 - 1/r + \tfrac12)[f\cos\theta\,e^{-r}] = -r\cos\theta\,e^{-r}$.) Maka

$$
E^{(2)} = \langle\psi_{1s}|\hat H'|\psi^{(1)}\rangle = -F^2\left\langle\left(r^2 + \tfrac12r^3\right)\cos^2\theta\right\rangle = -\frac{F^2}{3}\left(\langle r^2\rangle + \tfrac12\langle r^3\rangle\right) = -\frac{F^2}{3}\left(3 + \frac{15}{4}\right) = -\frac94F^2 ,
$$

memakai $\langle r^2\rangle = 3$, $\langle r^3\rangle = \tfrac{15}{2}$ untuk 1s dan $\langle\cos^2\theta\rangle = \tfrac13$. Jadi $\alpha = \tfrac92\ a_0^3$ **tepat**. Fungsi $\psi^{(1)}$ ini memuat sumbangan semua keadaan $np$ dan kontinu sekaligus. Bentuknya juga memberi gambaran fisika yang jelas: $\psi_{1s} + \psi^{(1)}$ adalah orbital 1s yang dicampur dengan "orbital p" bergeser $\propto(r + r^2/2)\cos\theta\,e^{-r}$, sejenis hibrida sp.
:::

::: {.contoh}
**Contoh 8.46 · Polarisabilitas hidrogen dari jumlah atas keadaan**

Unsur matriks dipol 1s–$n$p untuk hidrogen adalah $|\langle np_0|z|1s\rangle|^2 = 2^8n^7(n - 1)^{2n-5}/[3(n + 1)^{2n+5}]$, dan $E_n - E_1 = \tfrac12(1 - 1/n^2)$. (a) Hitung sumbangan $n = 2$ dan jumlah kumulatif keadaan terikat. (b) Berapa bagian $\alpha = 4{,}5$ yang berasal dari kontinu? (c) Bandingkan dengan taksiran Unsöld (8.37).

**Penyelesaian.** (a) Untuk $n = 2$: $|z|^2 = 2^8\cdot2^7/(3\cdot3^9) = 0{,}5549$, jadi $|\langle 2p_0|z|1s\rangle| = 0{,}7449$, dan sumbangannya $2(0{,}5549)/0{,}375 = 2{,}960$. Jumlah kumulatif (dengan Python):

| Sampai $n$ | 2 | 3 | 4 | 5 | 10 | $\infty$ |
|---|---|---|---|---|---|---|
| $\alpha$ kumulatif | 2,960 | 3,360 | 3,492 | 3,553 | 3,634 | 3,663 |

(b) Keadaan terikat menyumbang 3,663, atau 81%. Kontinu (keadaan tak terikat, ionisasi) menyumbang $4{,}5 - 3{,}663 = 0{,}837$, atau 19%.

(c) Dengan $\langle z^2\rangle = \tfrac13\langle r^2\rangle = 1$: bila $\Delta E$ diambil energi ionisasi 0,5, $\alpha \approx 2(1)/0{,}5 = 4{,}0$ (11% terlalu rendah); bila diambil $E_2 - E_1 = 0{,}375$, $\alpha \le 5{,}33$, batas atas yang terjamin.

**Memahami hasil.** Dua pertiga polarisabilitas berasal dari satu keadaan, 2p: keadaan tereksitasi terendah yang terhubung kuat. Tetapi kontinu tidak dapat diabaikan, sebuah peringatan bagi perhitungan yang hanya memakai beberapa keadaan tereksitasi. Volume polarisabilitas hidrogen $4{,}5 \times 0{,}148\,18 = 0{,}667$ Å³. Teknik Dalgarno–Lewis, yang menghindari jumlah atas keadaan, adalah cikal bakal metode modern "respons linear" yang dipakai program kimia komputasi untuk menghitung polarisabilitas, spektrum, dan sifat NMR.
:::

### Efek Stark linear: hidrogen $n = 2$

Bila keadaan terdegenerasi mempunyai paritas berlawanan, efek Stark linear muncul. Contoh klasiknya adalah tingkat $n = 2$ hidrogen, dengan empat fungsi 2s, 2p$_0$, 2p$_{+1}$, 2p$_{-1}$ yang terdegenerasi (bila struktur halus diabaikan). Operator $z$ ganjil dan, sebagai komponen $z$ suatu vektor, tidak mengubah $m$ (subbab 6.5). Jadi satu-satunya unsur tak nol adalah $\langle 2s|z|2p_0\rangle$, yang dihitung dengan fungsi gelombang hidrogen:

$$
\langle 2s|z|2p_0\rangle = -3\ a_0 .
$$

Matriks perturbasi 4 × 4 terpecah menjadi blok 2 × 2 untuk $\{2s, 2p_0\}$, dan dua blok 1 × 1 nol untuk $2p_{\pm1}$:

$$
\begin{pmatrix} 0 & -3F\\ -3F & 0\end{pmatrix} \quad\Longrightarrow\quad E^{(1)} = \pm3F , \qquad \psi_\pm = \frac{1}{\sqrt2}\left(2s \mp 2p_0\right) . \qquad \text{(8.48)}
$$

Kedua fungsi orde nol yang benar adalah **hibrida sp**: kombinasi 2s dan 2p$_0$ yang awannya bergeser ke satu sisi inti. Keduanya mempunyai momen dipol permanen sebesar $3ea_0$ yang menunjuk berlawanan, dan medan memilih orientasinya. Inilah contoh paling sederhana bagaimana pencampuran s dan p menghasilkan orbital berarah, gagasan yang menjadi inti hibridisasi (Bab 12).

::: {.dalam}
**Lebih dalam: menghitung $\langle 2s|z|2p_0\rangle$**

Fungsi hidrogen ternormalisasi (satuan atom): $\psi_{2s} = (32\pi)^{-1/2}(2 - r)e^{-r/2}$ dan $\psi_{2p_0} = (32\pi)^{-1/2}r\cos\theta\,e^{-r/2}$. Dengan $z = r\cos\theta$,

$$
\langle 2s|z|2p_0\rangle = \frac{1}{32\pi}\int_0^{2\pi}\!\!\int_0^\pi\cos^2\theta\sin\theta\,d\theta\,d\phi\int_0^\infty(2 - r)\,r^4e^{-r}\,dr = \frac{1}{32\pi}\cdot\frac{4\pi}{3}\left(2\cdot4! - 5!\right) = \frac{48 - 120}{24} = -3 .
$$

Tandanya bergantung pada pilihan fase fungsi gelombang dan tidak bermakna fisika; yang bermakna adalah besarnya, $3a_0$, yang sangat besar dibandingkan $\langle 1s|z|2p_0\rangle = 0{,}745\ a_0$ karena kedua orbital $n = 2$ sama-sama luas.
:::

::: {.contoh}
**Contoh 8.47 · Efek Stark linear dan kuadratik hidrogen**

(a) Hitung pemecahan tingkat $n = 2$ hidrogen dalam medan $1{,}0 \times 10^7$ V/m, dalam cm⁻¹. (b) Hitung pergeseran keadaan dasar dalam medan yang sama. (c) Bandingkan.

**Penyelesaian.** (a) $F = 1{,}0 \times 10^7/5{,}142 \times 10^{11} = 1{,}945 \times 10^{-5}$ satuan atom. $3F = 5{,}83 \times 10^{-5}\ E_h = 12{,}8$ cm⁻¹. Tingkat $n = 2$ pecah menjadi tiga: $+12{,}8$, 0 (dua keadaan), dan $-12{,}8$ cm⁻¹; selisih ujung ke ujung 25,6 cm⁻¹.

(b) $-\tfrac94F^2 = -\tfrac94(1{,}945 \times 10^{-5})^2 = -8{,}51 \times 10^{-10}\ E_h = -1{,}87 \times 10^{-4}$ cm⁻¹.

(c) Efek linear $n = 2$ hampir $7 \times 10^4$ kali lebih besar daripada efek kuadratik 1s.

**Memahami hasil.** Degenerasi membuat atom "sangat lunak": keadaan tereksitasi hidrogen dapat dipolarisasi tanpa biaya energi, karena 2s dan 2p sudah sama energinya. Garis Balmer, yang berasal dari $n \ge 3$, pecah menjadi banyak komponen dalam medan listrik; dari pemecahan itu fisikawan plasma mengukur medan listrik di dalam lucutan gas dan plasma fusi. Pada atom lain, degenerasi $\ell$ sudah pecah (Contoh 8.45), sehingga efek Starknya kuadratik kecuali pada medan sangat kuat.
:::

::: {.contoh}
**Contoh 8.48 · Polarisabilitas elektron dalam kotak dan rantai terkonjugasi**

Di Contoh 4.52 kita menghitung dengan diagonalisasi bahwa elektron dalam kotak 1,00 nm mempunyai polarisabilitas $9{,}23 \times 10^{-39}$ C m²/V. (a) Hitung $\alpha$ dengan (8.47), memakai $\langle 1|x|n\rangle = -8Ln/[\pi^2(n^2 - 1)^2]$ untuk $n$ genap. (b) Berapa sumbangan keadaan $n = 2$? (c) Bagaimana $\alpha$ bergantung pada $L$?

**Penyelesaian.** (a) Penjumlahan dengan Python sampai $n = 400$ memberi $\alpha = 9{,}228 \times 10^{-39}$ C m²/V, atau volume $\alpha' = 82{,}9$ Å³, sesuai hasil diagonalisasi.

(b) Suku $n = 2$ saja: 99,87% dari jumlah. Rumus Unsöld dengan $\Delta E = E_2 - E_1$ dan $\langle x^2\rangle - \langle x\rangle^2 = L^2(\tfrac{1}{12} - \tfrac{1}{2\pi^2})$ memberi nilai hanya 0,6% di atasnya.

(c) Unsur matriks $\langle 1|x|n\rangle \propto L$ dan selisih energi $\propto 1/L^2$, sehingga $\alpha \propto L^2/L^{-2} = L^4$. Hasilnya dapat ditulis $\alpha = 0{,}004\,39\,e^2m_eL^4/\hbar^2$.

**Memahami hasil.** Polarisabilitas satu elektron dalam kotak tumbuh dengan pangkat empat panjangnya. Untuk rantai poliena nyata, jumlah elektron π juga bertambah dengan panjang rantai, tetapi celah HOMO–LUMO tidak menutup sepenuhnya (subbab 3.8), sehingga kenaikannya lebih lambat; meskipun begitu, polarisabilitas per satuan panjang naik tajam dengan panjang konjugasi. Sifat ini, dan lebih lagi hiperpolarisabilitas (suku $F^3$ dan $F^4$ di (8.46)), dimanfaatkan untuk bahan optik nonlinear: molekul terkonjugasi panjang dengan gugus pendorong dan penarik elektron di ujung-ujungnya mengubah frekuensi cahaya laser.
:::

::: {.contoh}
**Contoh 8.49 · Efek Stark rotasi dan pengukuran momen dipol**

Molekul linear polar dengan momen dipol $\mu$ dan tetapan rotasi $B$ (dalam satuan energi) berada dalam keadaan rotasi $J = 0$. (a) Tunjukkan bahwa $E^{(1)} = 0$ dan $E^{(2)} = -\mu^2F^2/6B$. Gunakan $\langle 1, 0|\cos\theta|0, 0\rangle = 1/\sqrt3$. (b) Hitung pergeseran untuk HCl ($\mu = 1{,}109$ D, $B = 10{,}44$ cm⁻¹) dalam medan $1{,}0 \times 10^7$ V/m, dan untuk OCS ($\mu = 0{,}7152$ D, $B = 6081{,}49$ MHz) dalam medan $1{,}0 \times 10^5$ V/m.

**Penyelesaian.** (a) $\hat H' = -\mu F\cos\theta$, dengan $\theta$ sudut antara sumbu molekul dan medan. $\langle 0, 0|\cos\theta|0, 0\rangle = 0$ (harmonik bola $Y_0^0$ tetap, $\cos\theta$ ganjil). $\cos\theta$ hanya menghubungkan $J = 0$ dengan $J = 1$, $M = 0$, dan $E_1 - E_0 = 2B$. Jadi $E^{(2)} = -\mu^2F^2(1/3)/2B = -\mu^2F^2/6B$.

(b) HCl: $\mu F = (1{,}109 \times 3{,}336 \times 10^{-30})(10^7) = 3{,}70 \times 10^{-23}$ J $= 1{,}862$ cm⁻¹. $E^{(2)} = -(1{,}862)^2/(6 \times 10{,}44) = -0{,}0554$ cm⁻¹ $= -1{,}66$ GHz. OCS: $\mu F/h = 360$ MHz, $E^{(2)}/h = -(360)^2/(6 \times 6081) = -3{,}55$ MHz.

**Memahami hasil.** Walaupun HCl mempunyai dipol permanen, molekul yang berputar dalam keadaan $J = 0$ menunjuk ke segala arah dengan peluang sama, sehingga dipol rata-ratanya nol dan efek Starknya kuadratik. Medan "mencampurkan" sedikit $J = 1$ dan sedikit mengarahkan molekul. Pergeseran beberapa MHz mudah diukur dengan spektroskopi gelombang mikro, yang ketelitian frekuensinya sampai kHz; karena $\mu^2$ muncul langsung dalam rumus, efek Stark rotasi adalah cara paling teliti untuk mengukur momen dipol molekul. Momen dipol OCS sering dipakai sebagai standar kalibrasi medan.
:::

### Gaya dispersi London

Mengapa dua atom argon saling tarik? Keduanya netral, bersimetri bola, dan tanpa momen dipol permanen, sehingga interaksi elektrostatik klasiknya nol pada jarak jauh. Jawabannya adalah efek orde kedua. Untuk dua atom A dan B yang berjarak $R$ (jauh lebih besar daripada ukuran atom), interaksi elektrostatik antara keduanya dapat diuraikan; suku pertama yang tidak nol adalah interaksi dipol–dipol

$$
\hat H' = \frac{1}{R^3}\left(\hat\mu_{xA}\hat\mu_{xB} + \hat\mu_{yA}\hat\mu_{yB} - 2\hat\mu_{zA}\hat\mu_{zB}\right) , \qquad \text{(8.49)}
$$

dengan $z$ searah sumbu antaratom. Keadaan tak terganggu adalah $|0_A0_B\rangle$, kedua atom dalam keadaan dasar. Orde pertama nol, karena $\langle 0_A|\hat\mu_A|0_A\rangle = 0$. Orde kedua memerlukan keadaan $|m_An_B\rangle$ dengan **kedua** atom tereksitasi:

$$
E^{(2)} = -\sum_{m,n\ne0}\frac{|\langle m_An_B|\hat H'|0_A0_B\rangle|^2}{(E_m^A - E_0^A) + (E_n^B - E_0^B)} = -\frac{C_6}{R^6} .
$$

Faktor $1/R^3$ di $\hat H'$ menjadi $1/R^6$ setelah dikuadratkan. Tafsiran fisikanya: fluktuasi kuantum awan elektron A menghasilkan dipol sesaat; dipol itu menginduksi dipol pada B; keduanya berkorelasi sehingga selalu saling tarik. London (1930) menaksir jumlah itu dengan pendekatan Unsöld, mengganti semua energi eksitasi dengan energi ionisasi $I$, dan memperoleh

$$
C_6 \approx \frac32\,\frac{I_AI_B}{I_A + I_B}\,\alpha_A\alpha_B , \qquad\text{untuk atom sejenis}\quad C_6 \approx \tfrac34I\alpha^2 . \qquad \text{(8.50)}
$$

Gaya dispersi sebanding dengan **kuadrat polarisabilitas**: atom dan molekul yang besar dan "lunak" saling tarik lebih kuat.

::: {.contoh}
**Contoh 8.50 · Gas mulia: dispersi dan titik didih**

Data: polarisabilitas (dalam $a_0^3$) dan energi ionisasi (eV): He 1,383 dan 24,59; Ne 2,670 dan 21,56; Ar 11,08 dan 15,76; Kr 16,77 dan 14,00; Xe 27,16 dan 12,13. Nilai $C_6$ yang teliti (satuan atom): 1,46; 6,38; 64,3; 130; 286. Titik didih: 4,2; 27,1; 87,3; 119,9; 165,1 K. (a) Hitung $C_6$ London. (b) Bandingkan dengan nilai teliti. (c) Kaitkan dengan titik didih.

**Penyelesaian.** (a) Dengan $I$ dalam $E_h$, $C_6 = \tfrac34I\alpha^2$:

| Atom | $\alpha'$ (Å³) | $C_6$ London | $C_6$ teliti | London/teliti | $T_\text{d}$ (K) |
|---|---|---|---|---|---|
| He | 0,205 | 1,30 | 1,46 | 0,89 | 4,2 |
| Ne | 0,396 | 4,24 | 6,38 | 0,66 | 27,1 |
| Ar | 1,64 | 53,3 | 64,3 | 0,83 | 87,3 |
| Kr | 2,49 | 109 | 130 | 0,84 | 119,9 |
| Xe | 4,02 | 247 | 286 | 0,86 | 165,1 |

(b) Rumus London terlalu rendah 11–34%, karena energi ionisasi lebih besar daripada energi eksitasi rata-rata yang sebenarnya.

(c) $C_6$ naik hampir 200 kali dari He ke Xe, dan titik didih naik hampir 40 kali.

**Memahami hasil.** Tanpa gaya dispersi, gas mulia tidak akan pernah mencair. Gaya ini juga yang membuat titik didih alkana naik dengan panjang rantai, yang membuat cicak dapat menempel di langit-langit, dan yang menstabilkan tumpukan pasangan basa dalam DNA. Gaya dispersi adalah efek **korelasi elektron** murni: metode Hartree–Fock, yang memperlakukan setiap elektron dalam medan rata-rata, sama sekali tidak menangkapnya, sedangkan MP2 (teori perturbasi orde kedua) menangkapnya secara alami. Untuk He₂, suku $-C_6/R^6$ pada $R = 5{,}6\ a_0$ (3,0 Å) sebesar $-10$ cm⁻¹; setelah tolakan pada jarak itu diperhitungkan, sumur potensial He₂ hanya sedalam sekitar 11 K (7,6 cm⁻¹), sehingga dimer helium adalah molekul paling lemah yang dikenal.
:::

![Gambar 8.8 Kiri: efek Stark linear tingkat $n = 2$ hidrogen. Dua keadaan hibrida $(2s \mp 2p_0)/\sqrt2$ bergeser $\pm3F$, dan dua keadaan $2p_{\pm1}$ tetap. Inset: bentuk kedua hibrida, yang awannya bergeser ke sisi berlawanan. Kanan: titik didih gas mulia terhadap tetapan dispersi $C_6$ (skala logaritma); kenaikan $C_6$ sebanding dengan kuadrat polarisabilitas.](fig/c_stark.png){width=95%}

::: {.terapan}
**Polarisabilitas, indeks bias, dan warna langit**

Polarisabilitas menghubungkan dunia molekul dengan sifat optik makroskopik. Persamaan Lorentz–Lorenz mengaitkan indeks bias $n$ dengan polarisabilitas pada frekuensi cahaya: $(n^2 - 1)/(n^2 + 2) = N\alpha/3\varepsilon_0$, dengan $N$ kerapatan molekul. Refraksi molar senyawa organik dapat dihitung dengan menjumlahkan sumbangan ikatan, karena polarisabilitas kira-kira aditif. Hamburan Rayleigh cahaya oleh molekul udara sebanding dengan $\alpha^2\omega^4$, sehingga cahaya biru dihamburkan jauh lebih kuat daripada merah: inilah sebabnya langit biru dan matahari terbenam merah. Ketika frekuensi cahaya mendekati frekuensi serapan, penyebut di (8.47) mengecil, polarisabilitas dinamis membesar, dan muncul dispersi anomali serta hamburan resonansi.
:::

::: {.contoh}
**Contoh 8.51 · Indeks bias gas dari polarisabilitas**

Untuk gas, $n$ dekat 1 sehingga persamaan Lorentz–Lorenz dapat ditulis $n - 1 \approx 2\pi N\alpha'$, dengan $\alpha'$ volume polarisabilitas dan $N$ jumlah molekul per satuan volume. Hitung $n - 1$ untuk metana ($\alpha' = 2{,}59$ Å³) dan nitrogen ($\alpha' = 1{,}74$ Å³) pada 0 °C dan 1 atm. Nilai terukur: 0,000 44 dan 0,000 30.

**Penyelesaian.** $N = p/k_BT = 101\,325/(1{,}381 \times 10^{-23} \times 273{,}15) = 2{,}687 \times 10^{25}$ m⁻³. Metana: $2\pi(2{,}687 \times 10^{25})(2{,}59 \times 10^{-30}) = 4{,}37 \times 10^{-4}$. Nitrogen: $2{,}94 \times 10^{-4}$.

**Memahami hasil.** Sifat satu molekul yang dihitung dengan teori perturbasi orde kedua meramalkan sifat optik gas dengan galat hanya beberapa persen (selisih kecil berasal dari perbedaan polarisabilitas statis dan polarisabilitas pada frekuensi cahaya). Arah sebaliknya juga dipakai: pengukuran indeks bias atau tetapan dielektrik gas adalah cara klasik untuk menentukan polarisabilitas molekul. Pada cairan, $N$ seribu kali lebih besar dan $n - 1$ menjadi berorde 0,3–0,5; refraktometer Abbe di laboratorium kimia organik pada dasarnya mengukur polarisabilitas molekul.
:::

::: {.kuis}
**Kuis cepat 8.10**

(a) Mengapa atom He dalam keadaan dasar tidak mempunyai efek Stark linear, sedangkan atom H dalam keadaan $n = 2$ mempunyai? (b) Bila polarisabilitas suatu atom dilipatduakan, bagaimana $C_6$ berubah? (c) Molekul mana yang diharapkan lebih mudah dipolarisasi: heksana (tak berwarna) atau β-karotena (jingga)? Mengapa?
:::

