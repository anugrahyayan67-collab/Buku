# Bab 9 Spin Elektron dan Atom Berelektron Banyak

Neon dan natrium bertetangga di tabel periodik. Inti natrium hanya mempunyai satu proton lebih banyak, dan atomnya hanya satu elektron lebih banyak. Namun neon adalah gas yang hampir tidak mau bereaksi dengan apa pun, sedangkan natrium adalah logam lunak yang terbakar di udara dan meledak dalam air. Energi untuk mencabut satu elektron dari neon 21,6 eV; dari natrium hanya 5,1 eV. Mengapa elektron kesebelas begitu berbeda dari sepuluh elektron sebelumnya? Mengapa ia tidak ikut menempati orbital 1s yang paling rendah energinya, seperti yang akan dilakukan bola yang menggelinding ke dasar lembah? Dan mengapa pola yang sama, gas mulia yang lembam lalu logam alkali yang reaktif, berulang setelah 2, 8, 8, 18, 18, dan 32 unsur?

Jawabannya bertumpu pada dua fakta yang tidak dapat ditebak dari persamaan Schrödinger yang telah kita pelajari sejauh ini. Pertama, elektron mempunyai **spin**: momentum sudut intrinsik sebesar $\tfrac12\hbar$ yang tidak berasal dari gerak apa pun di ruang. Kedua, elektron adalah partikel yang **identik** dalam arti yang jauh lebih kuat daripada dua kelereng yang sama persis: fungsi gelombang sekumpulan elektron harus berubah tanda bila dua elektron mana pun dipertukarkan. Dari kedua fakta ini lahir asas larangan Pauli, determinan Slater, struktur kulit atom, dan tabel periodik.

Bab ini menyatukan spin dengan metode pendekatan dari Bab 8 untuk membangun teori atom berelektron banyak. Kita akan menghitung energi atom litium, mengenal metode Hartree–Fock yang menjadi fondasi kimia komputasi, memahami mengapa 4s terisi sebelum 3d, dan mempelajari bahasa lambang suku yang dipakai spektroskopis dan kimiawan anorganik untuk menamai keadaan elektronik atom dan ion. Pada akhirnya kita akan dapat menjawab mengapa oksigen di atmosfer atas memancarkan cahaya hijau aurora, mengapa garis D natrium kembar, dan mengapa ion Fe²⁺ bersifat paramagnet dengan empat elektron tak berpasangan.

::: {.strategi}
**Pertanyaan pembuka**

1. Bagaimana percobaan dengan berkas atom perak membuktikan bahwa elektron mempunyai momentum sudut yang bukan bilangan bulat kali $\hbar$?
2. Mengapa fungsi gelombang dua elektron harus berubah tanda bila kedua elektron dipertukarkan, dan apa akibatnya yang dapat diukur?
3. Mengapa setiap orbital hanya dapat diisi dua elektron, dan mengapa keduanya harus berspin berlawanan?
4. Mengapa orbital 4s terisi sebelum 3d pada kalium dan kalsium, tetapi elektron 4s yang lebih dulu lepas ketika besi menjadi Fe²⁺?
5. Apa arti lambang seperti ³P₂ atau ²S₁/₂, dan bagaimana aturan Hund menentukan keadaan dasar atom?
:::

::: {.tujuan}
**Tujuan belajar**

Setelah mempelajari bab ini, kamu mampu:

1. Menjelaskan percobaan Stern–Gerlach dan menghitung simpangan berkas serta frekuensi resonansi spin elektron.
2. Bekerja dengan operator spin, matriks Pauli, dan keadaan spin sembarang, termasuk presesi dalam medan magnet.
3. Menuliskan fungsi gelombang simetris dan antisimetris untuk partikel identik dan menjelaskan teorema spin–statistik.
4. Menyusun fungsi spin dua elektron (singlet dan triplet) dan menggabungkannya dengan fungsi ruang helium.
5. Menurunkan asas larangan Pauli dari antisimetri dan menerapkannya pada struktur kulit dan gas elektron.
6. Menuliskan dan menguraikan determinan Slater untuk atom berelektron sedikit.
7. Menghitung energi variasi atom litium dan menjelaskan mengapa konfigurasinya 1s²2s.
8. Menurunkan persamaan Hartree–Fock, menafsirkan energi orbital, dan memakai teorema Koopmans.
9. Menjelaskan urutan pengisian orbital, muatan inti efektif, dan kecenderungan periodik.
10. Mendefinisikan energi korelasi elektron dan membedakan korelasi dinamis dan statis.
11. Menjumlahkan momentum sudut dan menentukan lambang suku konfigurasi atom, termasuk elektron ekuivalen.
12. Menerapkan aturan Hund dan menghitung pemecahan spin–orbit serta struktur halus.
13. Menghitung unsur matriks Hamiltonian antara determinan Slater dengan aturan Condon–Slater.
:::

::: {.mat}
**Prasyarat**

Dari Bab 2: matriks dan determinan (subbab 2.7) dan nilai eigen matriks (subbab 2.8). Dari Bab 4: operator Hermitian, komutator, pengukuran, dan notasi Dirac (subbab 4.8, 4.10, 4.12, dan 4.14). Dari Bab 6: aljabar momentum sudut dan operator tangga (subbab 6.2, 6.6, dan 6.7). Dari Bab 7: orbital atom hidrogen dan atom mirip hidrogen (subbab 7.4–7.10). Dari Bab 8: metode variasi, muatan inti efektif helium, perturbasi terdegenerasi, dan integral Coulomb serta pertukaran (subbab 8.2, 8.3, 8.8, dan 8.9). Satuan atom dipakai sepanjang bab.
:::

## 9.1 Percobaan Stern–Gerlach dan spin

### Momen magnet dalam medan tak seragam

Di subbab 6.1 kita melihat bahwa partikel bermuatan yang mempunyai momentum sudut juga mempunyai momen magnet. Untuk elektron yang mengorbit, $\boldsymbol\mu = -(e/2m_e)\mathbf L$, sehingga komponen $z$-nya terkuantisasi dalam satuan magneton Bohr: $\mu_z = -m_\ell\mu_B$, dengan $\mu_B = e\hbar/2m_e = 9{,}274 \times 10^{-24}$ J/T.

Dalam medan magnet **seragam**, momen magnet hanya mengalami torsi dan berpresesi; tidak ada gaya bersih. Dalam medan yang **tidak seragam**, misalnya medan yang makin kuat ke arah $z$, energi $U = -\boldsymbol\mu\cdot\mathbf B$ bergantung pada posisi, dan ada gaya

$$
F_z = -\frac{\partial U}{\partial z} = \mu_z\frac{\partial B_z}{\partial z} . \qquad \text{(9.1)}
$$

Atom yang $\mu_z$-nya positif didorong ke arah medan kuat, yang negatif ke arah medan lemah. Seberkas atom yang melewati magnet semacam ini karena itu dipilah menurut $\mu_z$.

### Percobaan 1922

Otto Stern dan Walther Gerlach (1922) menguapkan perak dalam tungku, membentuk berkas atom yang sempit dengan celah-celah, melewatkannya di antara kutub magnet yang dibentuk sedemikian sehingga medannya sangat tak seragam, lalu menangkap atom-atom itu pada pelat kaca. Menurut fisika klasik, momen magnet atom-atom dalam tungku mengarah acak, sehingga $\mu_z$ dapat bernilai berapa pun antara $-\mu$ dan $+\mu$, dan jejak di pelat seharusnya berupa pita malar. Menurut teori kuantum lama (model Bohr–Sommerfeld), $\mu_z = -m_\ell\mu_B$ dengan $m_\ell = -\ell, \ldots, +\ell$, sehingga jejaknya seharusnya terdiri atas $2\ell + 1$ titik, bilangan **ganjil**, termasuk satu titik tak terbelokkan di tengah ($m_\ell = 0$).

Yang teramati adalah **dua** jejak, satu di atas dan satu di bawah, tanpa apa pun di tengah. Ini mengejutkan dari dua sisi. Kuantisasi ruang ternyata nyata (bukan pita malar), tetapi jumlah komponennya genap, yang tidak mungkin untuk momentum sudut orbital. Dari besar simpangannya, $\mu_z$ ternyata sama dengan $\pm\mu_B$ (dalam batas ketelitian).

![Gambar 9.1 Percobaan Stern–Gerlach. Kiri: skema; atom perak dari tungku dibentuk menjadi berkas sempit, melewati medan magnet yang sangat tak seragam, lalu mengenai pelat. Kanan: sebaran jejak di pelat sepanjang $z$. Fisika klasik meramalkan pita malar (garis putus-putus); yang teramati adalah dua jejak terpisah, tanpa atom di tengah.](fig/c_sterngerlach.png){width=92%}

Atom perak mempunyai 47 elektron. Empat puluh enam di antaranya membentuk kulit-kulit penuh dengan momentum sudut total nol; elektron ke-47 menempati orbital 5s, dengan $\ell = 0$. Jadi atom perak **tidak** mempunyai momentum sudut orbital, dan seharusnya tidak dibelokkan sama sekali. Percobaan yang sama dengan atom hidrogen dalam keadaan dasar (Phipps dan Taylor, 1927), yang elektronnya pasti di 1s, juga menghasilkan dua jejak.

### Hipotesis spin

Pada tahun 1925, Uhlenbeck dan Goudsmit, untuk menjelaskan struktur kembar garis-garis spektrum logam alkali (subbab 9.13), mengusulkan bahwa elektron mempunyai momentum sudut intrinsik, **spin**, dengan bilangan kuantum $s = \tfrac12$. Menurut aljabar momentum sudut umum (subbab 6.7), nilai setengah bulat diizinkan bila momentum sudut tidak berasal dari fungsi ruang yang bernilai tunggal. Untuk $s = \tfrac12$:

$$
|\mathbf S| = \sqrt{s(s + 1)}\,\hbar = \frac{\sqrt3}{2}\hbar , \qquad S_z = m_s\hbar , \quad m_s = \pm\tfrac12 . \qquad \text{(9.2)}
$$

Hanya ada $2s + 1 = 2$ orientasi: inilah dua jejak Stern–Gerlach. Keadaan $m_s = +\tfrac12$ disebut "spin ke atas" (lambang $\alpha$ atau $\uparrow$) dan $m_s = -\tfrac12$ "spin ke bawah" ($\beta$ atau $\downarrow$).

Momen magnet spin ternyata **dua kali** lebih besar daripada yang diharapkan dari perbandingan $e/2m_e$ untuk momentum sudut orbital:

$$
\boldsymbol\mu_s = -g_e\frac{e}{2m_e}\mathbf S = -g_e\mu_B\frac{\mathbf S}{\hbar} , \qquad g_e = 2{,}002\,319 . \qquad \text{(9.3)}
$$

Faktor $g_e \approx 2$ muncul secara alami dari persamaan Dirac (1928), versi relativistik persamaan Schrödinger untuk elektron, yang juga menghasilkan spin $\tfrac12$ tanpa perlu dipostulatkan. Selisih kecil dari 2 berasal dari elektrodinamika kuantum dan termasuk besaran yang paling teliti diukur dan dihitung dalam seluruh fisika. Dengan $g_e \approx 2$ dan $S_z = \pm\tfrac12\hbar$, $\mu_z = \mp\mu_B$, sesuai pengamatan Stern dan Gerlach.

::: {.awas}
**Spin bukan elektron yang berputar**

Gambaran elektron sebagai bola kecil yang berputar pada porosnya menarik, tetapi tidak dapat dipertahankan. Bila elektron dianggap bola berjari-jari sekitar $10^{-15}$ m (jari-jari elektron klasik), permukaannya harus berputar jauh lebih cepat daripada cahaya untuk menghasilkan momentum sudut $\tfrac12\hbar$. Pengukuran hamburan juga tidak menemukan ukuran elektron sampai $10^{-18}$ m. Spin adalah sifat intrinsik, seperti massa dan muatan, yang tidak mempunyai padanan klasik. Ia berperilaku **seperti** momentum sudut (memenuhi aljabar yang sama dan bergabung dengan momentum sudut orbital), tetapi tidak berasal dari gerak di ruang. Karena itu fungsi gelombang spin bukan fungsi koordinat $x$, $y$, $z$.
:::

### Koordinat spin

Untuk menggambarkan elektron secara lengkap, kita menambahkan satu "koordinat" lagi pada tiga koordinat ruang: **koordinat spin** $\omega$ (atau langsung $m_s$), yang hanya dapat bernilai $+\tfrac12$ atau $-\tfrac12$. Fungsi spin $\alpha$ dan $\beta$ didefinisikan oleh

$$
\alpha(+\tfrac12) = 1, \quad \alpha(-\tfrac12) = 0, \qquad \beta(+\tfrac12) = 0, \quad \beta(-\tfrac12) = 1 .
$$

"Integral" atas koordinat spin adalah penjumlahan atas kedua nilainya, sehingga $\langle\alpha|\alpha\rangle = \langle\beta|\beta\rangle = 1$ dan $\langle\alpha|\beta\rangle = 0$. Bila Hamiltonian tidak memuat spin (pendekatan yang sangat baik untuk atom ringan), fungsi gelombang satu elektron dapat ditulis sebagai hasil kali fungsi ruang dan fungsi spin,

$$
\chi(\mathbf r, \omega) = \psi(\mathbf r)\,\sigma(\omega) , \qquad \sigma = \alpha\ \text{atau}\ \beta , \qquad \text{(9.4)}
$$

yang disebut **spin-orbital**. Setiap orbital ruang $\psi$ melahirkan dua spin-orbital, $\psi\alpha$ dan $\psi\beta$. Inilah sebabnya jumlah keadaan atom hidrogen pada kulit $n$ adalah $2n^2$, bukan $n^2$.

::: {.inti}
**Spin elektron**

$s = \tfrac12$, $|\mathbf S| = \tfrac{\sqrt3}{2}\hbar$, $S_z = \pm\tfrac12\hbar$. Momen magnet spin $\boldsymbol\mu_s = -g_e\mu_B\mathbf S/\hbar$ dengan $g_e = 2{,}0023$. Fungsi gelombang lengkap satu elektron adalah spin-orbital $\psi(\mathbf r)\sigma(\omega)$, dengan $\sigma = \alpha$ ($m_s = +\tfrac12$) atau $\beta$ ($m_s = -\tfrac12$).
:::

::: {.contoh}
**Contoh 9.1 · Simpangan berkas perak**

Atom perak ($M = 107{,}87$ g/mol) keluar dari tungku dengan kelajuan khas 550 m/s dan melewati magnet sepanjang 3,5 cm dengan gradien medan $1{,}0 \times 10^3$ T/m. Hitung percepatan atom dengan $\mu_z = \pm\mu_B$ dan simpangannya di ujung magnet.

**Penyelesaian.** Massa atom $m = 107{,}87 \times 1{,}661 \times 10^{-27} = 1{,}791 \times 10^{-25}$ kg. Gaya $F = \mu_B(\partial B/\partial z) = 9{,}27 \times 10^{-21}$ N, percepatan $a = F/m = 5{,}18 \times 10^4$ m/s². Waktu di dalam magnet $t = 0{,}035/550 = 6{,}36 \times 10^{-5}$ s. Simpangan $z = \tfrac12at^2 = 0{,}105$ mm ke atas atau ke bawah.

**Memahami hasil.** Pemisahan total sekitar 0,2 mm di ujung magnet (dan sedikit lebih besar di pelat penangkap) cukup untuk dilihat dengan mikroskop, walaupun Stern dan Gerlach mula-mula hanya mendapat lapisan perak yang sangat tipis; jejaknya baru tampak jelas setelah mereka (menurut cerita) bernapas di atasnya dengan asap cerutu murah yang mengandung belerang, sehingga perak berubah menjadi perak sulfida yang hitam. Atom bergerak dengan sebaran kelajuan, sehingga setiap jejak agak melebar; tetapi tidak ada atom di tengah.
:::

::: {.contoh}
**Contoh 9.2 · Sudut vektor spin**

(a) Hitung besar momentum sudut spin dalam satuan $\hbar$. (b) Dalam model vektor (subbab 6.6), berapa sudut antara $\mathbf S$ dan sumbu $z$ untuk $m_s = +\tfrac12$? (c) Berapa $\langle S_x^2\rangle$ dalam keadaan $\alpha$?

**Penyelesaian.** (a) $\sqrt{\tfrac12\cdot\tfrac32} = \sqrt3/2 = 0{,}866$. (b) $\cos\theta = \tfrac12/0{,}866 = 0{,}577$, $\theta = 54{,}7°$. (c) $\langle S_x^2 + S_y^2\rangle = \langle S^2\rangle - \langle S_z^2\rangle = \tfrac34\hbar^2 - \tfrac14\hbar^2 = \tfrac12\hbar^2$, dan karena simetri $\langle S_x^2\rangle = \tfrac14\hbar^2$.

**Memahami hasil.** Vektor spin tidak pernah sejajar sumbu $z$; ia selalu membentuk sudut 54,7° (sudut yang sama dengan "sudut ajaib" dalam NMR padatan, $\cos^2\theta = \tfrac13$). Komponen $x$ dan $y$-nya tidak tajam: setiap pengukuran $S_x$ memberi $\pm\tfrac12\hbar$, sehingga $S_x^2 = \tfrac14\hbar^2$ selalu, tetapi tandanya acak. Untuk spin $\tfrac12$, kuadrat setiap komponen selalu tepat $\tfrac14\hbar^2$, sifat yang akan terlihat dari matriks Pauli di subbab 9.2.
:::

::: {.contoh}
**Contoh 9.3 · Resonansi spin elektron**

Dalam medan $B$, dua orientasi spin elektron bebas mempunyai energi $\pm\tfrac12g_e\mu_BB$. (a) Hitung frekuensi foton yang menyebabkan transisi untuk $B = 0{,}35$ T (spektrometer ESR pita X) dan 1,0 T. (b) Pada 298 K dan 1,0 T, berapa perbandingan populasi kedua tingkat?

**Penyelesaian.** (a) $\nu = g_e\mu_BB/h$. Untuk 0,35 T: $2{,}0023(9{,}274 \times 10^{-24})(0{,}35)/(6{,}626 \times 10^{-34}) = 9{,}81$ GHz; untuk 1,0 T: 28,0 GHz.

(b) $\Delta E/k_BT = g_e\mu_B(1{,}0)/(1{,}381 \times 10^{-23} \times 298{,}15) = 4{,}51 \times 10^{-3}$. $N_\text{atas}/N_\text{bawah} = e^{-0{,}00451} = 0{,}9955$.

**Memahami hasil.** Spektroskopi resonansi spin elektron (ESR atau EPR) bekerja pada daerah gelombang mikro dan mendeteksi radikal bebas, ion logam transisi, dan cacat dalam padatan. Hanya molekul yang mempunyai elektron tak berpasangan yang memberi sinyal; elektron berpasangan saling meniadakan momen magnetnya (subbab 9.5). Selisih populasi hanya sekitar 0,2%, tetapi karena momen magnet elektron sekitar 660 kali momen magnet proton, ESR jauh lebih peka daripada NMR untuk jumlah spin yang sama. Penyimpangan faktor $g$ suatu radikal dari 2,0023 dan pemecahan hiperhalus oleh inti di sekitarnya memberi informasi struktur (subbab 16.11).
:::

::: {.kuis}
**Kuis cepat 9.1**

(a) Seandainya elektron tidak mempunyai spin dan perak mempunyai satu elektron p di luar kulit penuh, berapa jejak yang akan teramati? (b) Mengapa percobaan Stern–Gerlach tidak dilakukan dengan berkas elektron bebas? (Petunjuk: gaya Lorentz.) (c) Berapa banyak spin-orbital pada kulit $n = 3$ atom hidrogen?
:::

## 9.2 Operator spin dan matriks Pauli

### Postulat momentum sudut untuk spin

Spin tidak mempunyai fungsi ruang, sehingga operatornya tidak dapat ditulis sebagai turunan seperti $\hat L_z = -i\hbar\,\partial/\partial\phi$. Sebagai gantinya, kita **mempostulatkan** bahwa operator spin $\hat S_x$, $\hat S_y$, $\hat S_z$ adalah operator Hermitian yang memenuhi komutator momentum sudut yang sama dengan $\hat L$ (subbab 6.2):

$$
[\hat S_x, \hat S_y] = i\hbar\hat S_z , \qquad [\hat S_y, \hat S_z] = i\hbar\hat S_x , \qquad [\hat S_z, \hat S_x] = i\hbar\hat S_y . \qquad \text{(9.5)}
$$

Semua hasil aljabar operator tangga di subbab 6.7 kemudian berlaku tanpa perubahan: $\hat S^2$ komut dengan setiap komponen, nilai eigen $\hat S^2$ adalah $s(s + 1)\hbar^2$, nilai eigen $\hat S_z$ adalah $m_s\hbar$, dan operator tangga $\hat S_\pm = \hat S_x \pm i\hat S_y$ menaikkan atau menurunkan $m_s$ satu satuan. Untuk elektron, $s = \tfrac12$:

$$
\hat S^2\alpha = \tfrac34\hbar^2\alpha , \quad \hat S_z\alpha = \tfrac12\hbar\alpha , \qquad \hat S^2\beta = \tfrac34\hbar^2\beta , \quad \hat S_z\beta = -\tfrac12\hbar\beta , \qquad \text{(9.6)}
$$

dan dari rumus $\hat S_\pm|s, m\rangle = \hbar\sqrt{s(s + 1) - m(m \pm 1)}\,|s, m \pm 1\rangle$:

$$
\hat S_+\beta = \hbar\alpha , \quad \hat S_+\alpha = 0 , \qquad \hat S_-\alpha = \hbar\beta , \quad \hat S_-\beta = 0 . \qquad \text{(9.7)}
$$

### Matriks Pauli

Karena hanya ada dua keadaan, setiap operator spin dapat dinyatakan sebagai matriks 2 × 2 dalam basis $\{\alpha, \beta\}$ (subbab 4.14). Tulislah $\alpha = \begin{pmatrix}1\\0\end{pmatrix}$ dan $\beta = \begin{pmatrix}0\\1\end{pmatrix}$. Dari (9.6), $\hat S_z$ diagonal dengan unsur $\pm\tfrac12\hbar$. Dari (9.7), $\hat S_+$ hanya mempunyai unsur $\langle\alpha|\hat S_+|\beta\rangle = \hbar$, dan $\hat S_-$ hanya $\langle\beta|\hat S_-|\alpha\rangle = \hbar$. Dengan $\hat S_x = \tfrac12(\hat S_+ + \hat S_-)$ dan $\hat S_y = \tfrac{1}{2i}(\hat S_+ - \hat S_-)$:

$$
\hat S_x = \frac\hbar2\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix} , \qquad \hat S_y = \frac\hbar2\begin{pmatrix}0 & -i\\ i & 0\end{pmatrix} , \qquad \hat S_z = \frac\hbar2\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix} . \qquad \text{(9.8)}
$$

Matriks-matriks tanpa faktor $\hbar/2$ disebut **matriks Pauli** $\sigma_x$, $\sigma_y$, $\sigma_z$, sehingga $\hat{\mathbf S} = \tfrac\hbar2\boldsymbol\sigma$. Kita sudah bertemu dengan mereka di Contoh 2.30. Sifat-sifat pentingnya, yang dapat diperiksa dengan perkalian langsung:

$$
\sigma_x^2 = \sigma_y^2 = \sigma_z^2 = \mathbf 1 , \qquad \sigma_x\sigma_y = i\sigma_z \ (\text{dan siklis}) , \qquad \sigma_x\sigma_y + \sigma_y\sigma_x = 0 . \qquad \text{(9.9)}
$$

Sifat pertama berarti setiap komponen spin, bila diukur, hanya dapat memberi $\pm\tfrac12\hbar$, dan kuadratnya selalu $\tfrac14\hbar^2$. Dari sifat itu pula $\hat S^2 = \tfrac{\hbar^2}{4}(\sigma_x^2 + \sigma_y^2 + \sigma_z^2) = \tfrac34\hbar^2\mathbf 1$, sesuai (9.6).

### Keadaan spin sembarang

Keadaan spin paling umum adalah superposisi $\chi = c_1\alpha + c_2\beta$ dengan $|c_1|^2 + |c_2|^2 = 1$. Pengukuran $S_z$ memberi $+\tfrac12\hbar$ dengan peluang $|c_1|^2$ dan $-\tfrac12\hbar$ dengan peluang $|c_2|^2$. Setiap keadaan seperti itu ternyata adalah keadaan "spin ke atas" sepanjang suatu arah tertentu. Bila arah itu ditandai sudut kutub $\theta$ dan sudut azimut $\phi$, vektor eigen operator $\hat S_n = \hat{\mathbf S}\cdot\mathbf n$ dengan nilai eigen $+\tfrac12\hbar$ adalah

$$
\chi_{\mathbf n} = \cos\frac\theta2\,\alpha + e^{i\phi}\sin\frac\theta2\,\beta . \qquad \text{(9.10)}
$$

Perhatikan munculnya **setengah** sudut. Untuk $\theta = 0$, $\chi = \alpha$; untuk $\theta = \pi$ (arah $-z$), $\chi = e^{i\phi}\beta$; untuk $\theta = \pi/2$, $\phi = 0$ (arah $+x$), $\chi = (\alpha + \beta)/\sqrt2$. Setiap keadaan spin $\tfrac12$ dapat digambarkan sebagai satu titik pada bola satuan (**bola Bloch**), dan sebaliknya.

### Spin dalam medan magnet: presesi Larmor

Dalam medan $\mathbf B = B\hat{\mathbf z}$, Hamiltonian spin elektron adalah

$$
\hat H = -\hat{\boldsymbol\mu}_s\cdot\mathbf B = \frac{g_e\mu_BB}{\hbar}\hat S_z = \frac{\hbar\omega_L}{2}\sigma_z , \qquad \omega_L = \frac{g_e\mu_BB}{\hbar} . \qquad \text{(9.11)}
$$

Bila spin mula-mula mengarah ke $+x$, $\chi(0) = (\alpha + \beta)/\sqrt2$, setiap komponen berevolusi dengan faktor fasenya sendiri: $\chi(t) = (e^{-i\omega_Lt/2}\alpha + e^{i\omega_Lt/2}\beta)/\sqrt2$. Sampai faktor fase global, ini adalah (9.10) dengan $\theta = \pi/2$ dan $\phi = \omega_Lt$: arah spin berputar mengelilingi medan dengan frekuensi sudut $\omega_L$, **presesi Larmor**, persis seperti gasing yang miring dalam medan gravitasi. Nilai harap $\langle S_x\rangle = \tfrac12\hbar\cos\omega_Lt$ berosilasi. Presesi ini adalah dasar NMR dan ESR: momen magnet yang berpresesi menginduksi arus berosilasi dalam kumparan detektor (Bab 16).

::: {.dalam}
**Lebih dalam: rotasi 360° mengubah tanda**

Setelah satu putaran penuh presesi, $\omega_Lt = 2\pi$, fungsi spin menjadi $\chi(2\pi/\omega_L) = (e^{-i\pi}\alpha + e^{i\pi}\beta)/\sqrt2 = -\chi(0)$. Spin $\tfrac12$ yang diputar 360° tidak kembali ke dirinya sendiri, melainkan ke negatifnya; baru setelah 720° ia kembali utuh. Hal ini juga terlihat dari setengah sudut di (9.10). Tanda minus ini tidak teramati bila hanya satu keadaan yang ada (fase global tidak bermakna), tetapi dapat teramati dalam interferensi. Pada tahun 1975 percobaan dengan interferometer neutron (neutron juga berspin $\tfrac12$) membuktikannya: berkas neutron yang spinnya diputar 360° dalam satu lengan interferometer berinterferensi destruktif dengan berkas di lengan lain. Inilah alasan matematis mengapa momentum sudut setengah bulat tidak dapat berasal dari fungsi ruang bernilai tunggal seperti $e^{im\phi}$ (subbab 6.7).
:::

::: {.contoh}
**Contoh 9.4 · Vektor eigen $\hat S_x$ dan pengukuran berurutan**

(a) Cari nilai eigen dan vektor eigen $\hat S_x$. (b) Elektron dalam keadaan $\alpha$. Berapa peluang pengukuran $S_x$ memberi $+\tfrac12\hbar$? (c) Setelah hasil itu diperoleh, $S_z$ diukur lagi. Berapa peluang memperoleh $-\tfrac12\hbar$?

**Penyelesaian.** (a) $\det\begin{pmatrix}-\lambda & 1\\ 1 & -\lambda\end{pmatrix} = \lambda^2 - 1 = 0$, jadi $\lambda = \pm1$ (dalam satuan $\hbar/2$). Vektor eigen: $\chi_{+x} = (\alpha + \beta)/\sqrt2$ dan $\chi_{-x} = (\alpha - \beta)/\sqrt2$.

(b) $|\langle\chi_{+x}|\alpha\rangle|^2 = |1/\sqrt2|^2 = \tfrac12$.

(c) Setelah pengukuran, keadaannya $\chi_{+x}$; $|\langle\beta|\chi_{+x}\rangle|^2 = \tfrac12$.

**Memahami hasil.** Spin yang mula-mula pasti "ke atas" sepanjang $z$, setelah diukur sepanjang $x$, kehilangan seluruh informasi tentang $z$: pengukuran $S_z$ berikutnya memberi hasil 50 : 50. Dalam percobaan Stern–Gerlach berurutan (magnet $z$, lalu $x$, lalu $z$ lagi), berkas yang dipilih "ke atas" oleh magnet pertama pecah lagi menjadi dua oleh magnet ketiga. Inilah ilustrasi paling bersih dari pengukuran kuantum dan komponen yang tidak komut (Contoh 4.42 dan subbab 4.12). Gagasan yang sama mendasari kriptografi kuantum dengan foton terpolarisasi.
:::

::: {.contoh}
**Contoh 9.5 · Nilai harap spin dalam arah sembarang**

Elektron berada dalam keadaan $\chi = \tfrac35\alpha + \tfrac45\beta$. (a) Hitung $\langle S_x\rangle$, $\langle S_y\rangle$, $\langle S_z\rangle$. (b) Ke arah mana spin "menunjuk"? (c) Tunjukkan bahwa panjang vektor nilai harap itu $\tfrac12\hbar$.

**Penyelesaian.** (a) Dengan $\chi = (0{,}6;\ 0{,}8)$: $\langle\sigma_z\rangle = 0{,}36 - 0{,}64 = -0{,}28$; $\langle\sigma_x\rangle = 2(0{,}6)(0{,}8) = 0{,}96$; $\langle\sigma_y\rangle = 0$ (koefisien riil). Dikali $\hbar/2$: $\langle S_x\rangle = 0{,}48\hbar$, $\langle S_y\rangle = 0$, $\langle S_z\rangle = -0{,}14\hbar$.

(b) Dari (9.10), $\cos(\theta/2) = 0{,}6$, sehingga $\theta = 2\arccos0{,}6 = 106{,}3°$ dan $\phi = 0$: di bidang $xz$, sedikit di bawah sumbu $x$.

(c) $\sqrt{0{,}48^2 + 0{,}14^2} = 0{,}50$.

**Memahami hasil.** Vektor nilai harap $\langle\hat{\mathbf S}\rangle$ selalu mempunyai panjang $\tfrac12\hbar$ untuk keadaan murni, dan menunjuk ke arah $\mathbf n$ di (9.10). Panjang ini lebih kecil daripada $|\mathbf S| = 0{,}866\hbar$: komponen tegak lurus terhadap $\mathbf n$ tetap berfluktuasi. Dalam NMR, magnetisasi sampel adalah jumlah vektor-vektor seperti ini dari sangat banyak inti, dan pulsa frekuensi radio memutarnya pada bola Bloch (Contoh 8.54).
:::

::: {.contoh}
**Contoh 9.6 · Presesi Larmor elektron dan proton**

(a) Hitung frekuensi Larmor elektron bebas dan proton (rasio giromagnet proton $\gamma_p/2\pi = 42{,}58$ MHz/T) dalam medan 1,0 T. (b) Berapa lama spin elektron berpresesi satu putaran? (c) Bila radikal organik dalam larutan berpresesi pada 9,81 GHz di medan 0,35 T, berapa faktor $g$-nya?

**Penyelesaian.** (a) Elektron: $\nu_L = g_e\mu_BB/h = 28{,}0$ GHz. Proton: 42,6 MHz. Perbandingannya 658.

(b) $1/(28{,}0 \times 10^9) = 3{,}57 \times 10^{-11}$ s, sekitar 36 ps.

(c) $g = h\nu/\mu_BB = (6{,}626 \times 10^{-34})(9{,}81 \times 10^9)/[(9{,}274 \times 10^{-24})(0{,}35)] = 2{,}003$.

**Memahami hasil.** Elektron berpresesi hampir tujuh ratus kali lebih cepat daripada proton dalam medan yang sama, sebanding dengan perbandingan momen magnetnya. Itulah sebabnya NMR proton pada magnet 9,4 T bekerja di 400 MHz (gelombang radio), sedangkan ESR pada 0,35 T sudah berada di gelombang mikro. Faktor $g$ radikal organik sangat dekat dengan 2,0023 karena momentum sudut orbitalnya hampir seluruhnya padam; ion logam transisi, yang kopling spin–orbitnya kuat (subbab 9.13), mempunyai $g$ yang menyimpang jauh, dari sekitar 1,9 sampai di atas 4.
:::

::: {.kuis}
**Kuis cepat 9.2**

(a) Berapa nilai eigen $\sigma_y$? (b) Mengapa $\hat S_x\hat S_y \ne \hat S_y\hat S_x$, padahal keduanya adalah komponen dari vektor yang sama? (c) Keadaan $(\alpha + i\beta)/\sqrt2$ menunjuk ke arah mana?
:::

