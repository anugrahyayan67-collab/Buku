## 9.13 Kopling spin–orbit dan struktur halus

### Asal kopling spin–orbit

Bayangkan diri kita menumpang pada elektron yang mengorbit inti. Dari sudut pandang elektron, intilah yang berputar mengelilinginya, dan muatan yang bergerak membangkitkan medan magnet. Medan ini sebanding dengan momentum sudut orbital $\mathbf L$, dan ia berinteraksi dengan momen magnet spin elektron, yang sebanding dengan $\mathbf S$. Hasilnya adalah energi yang bergantung pada orientasi relatif spin dan orbit:

$$
\hat H_\text{SO} = \xi(r)\,\hat{\mathbf L}\cdot\hat{\mathbf S} , \qquad \xi(r) = \frac{1}{2m_e^2c^2}\,\frac1r\frac{dV}{dr} . \qquad \text{(9.40)}
$$

(Perhitungan yang naif dalam kerangka elektron memberi dua kali nilai ini; faktor $\tfrac12$, **faktor Thomas**, berasal dari efek relativistik kerangka yang berputar, dan muncul otomatis dari persamaan Dirac.) Untuk atom mirip hidrogen, $V = -Ze^2/4\pi\varepsilon_0r$ dan $\xi \propto Z/r^3$. Karena $\langle r^{-3}\rangle \propto Z^3/n^3$, besar kopling tumbuh kira-kira seperti $Z^4$: inilah alasan efek spin–orbit kecil pada atom ringan dan sangat besar pada atom berat. Dalam atom berelektron banyak, elektron valensi terperisai, sehingga pertumbuhan efektifnya lebih lambat (kira-kira $Z^2$ untuk elektron valensi dalam satu golongan), tetapi tetap dramatis.

### Satu elektron

Untuk satu elektron dengan $\ell$ dan $s = \tfrac12$, $\hat{\mathbf L}\cdot\hat{\mathbf S}$ tidak komut dengan $\hat L_z$ maupun $\hat S_z$, tetapi komut dengan $\hat L^2$, $\hat S^2$, $\hat J^2$, dan $\hat J_z$. Fungsi eigen yang benar adalah fungsi terkopel $|\ell s; jm_j\rangle$ (Contoh 9.39), dengan $j = \ell \pm \tfrac12$. Dari $\hat J^2 = \hat L^2 + \hat S^2 + 2\hat{\mathbf L}\cdot\hat{\mathbf S}$:

$$
E_\text{SO} = \frac{\zeta_{n\ell}}{2}\left[j(j + 1) - \ell(\ell + 1) - s(s + 1)\right] , \qquad \zeta_{n\ell} = \hbar^2\langle\xi(r)\rangle_{n\ell} . \qquad \text{(9.41)}
$$

Untuk $j = \ell + \tfrac12$, $E_\text{SO} = \tfrac12\ell\zeta$; untuk $j = \ell - \tfrac12$, $E_\text{SO} = -\tfrac12(\ell + 1)\zeta$. Pemecahannya $(\ell + \tfrac12)\zeta$, dan pusat beratnya (rata-rata berbobot $2j + 1$) tidak bergeser. Untuk atom mirip hidrogen, $\zeta_{n\ell} = \alpha_\text{f}^2Z^4E_h/[2n^3\ell(\ell + \tfrac12)(\ell + 1)]$. Elektron s tidak mempunyai momentum sudut orbital dan tidak mengalami pemecahan.

### Banyak elektron: konstanta kopling suku dan aturan selang Landé

Dalam kopling LS, di dalam satu suku $^{2S+1}L$ kopling spin–orbit dapat ditulis sebagai $A\,\hat{\mathbf L}\cdot\hat{\mathbf S}$, dengan $A$ konstanta kopling suku. Energi tingkat $J$:

$$
E(J) = \frac A2\left[J(J + 1) - L(L + 1) - S(S + 1)\right] , \qquad E(J) - E(J - 1) = AJ . \qquad \text{(9.42)}
$$

Rumus kedua adalah **aturan selang Landé**: jarak antara tingkat-tingkat berurutan sebanding dengan $J$ yang lebih besar. Untuk subkulit kurang dari setengah penuh, $A > 0$ dan tingkat $J$ terkecil paling rendah (multiplet **normal**); untuk subkulit lebih dari setengah penuh, $A < 0$ (multiplet **terbalik**), karena "lubang" berperilaku seperti elektron bermuatan berlawanan. Inilah dasar aturan Hund ketiga. Penyimpangan dari aturan selang adalah ukuran seberapa jauh kopling LS sudah tidak berlaku.

### Kopling spin–orbit dalam kimia

Kopling spin–orbit melonggarkan aturan seleksi $\Delta S = 0$ (subbab 8.12), karena ia mencampurkan sedikit karakter singlet ke dalam keadaan triplet dan sebaliknya. Akibatnya terlihat di banyak tempat: fosforesensi dan perpindahan antarsistem dalam fotokimia (Bab 15), **efek atom berat** (pelarut beriodium mempercepat perpindahan singlet → triplet), kompleks iridium dan platina yang memancarkan cahaya triplet secara efisien dalam layar OLED, serta faktor $g$ ion logam transisi yang menyimpang dari 2 (Contoh 9.6). Pada unsur sangat berat, kopling spin–orbit ikut menentukan panjang ikatan, energi ikatan, dan bahkan keadaan oksidasi yang stabil.

::: {.inti}
**Kopling spin–orbit**

$\hat H_\text{SO} = \xi(r)\hat{\mathbf L}\cdot\hat{\mathbf S}$; untuk satu elektron $E = \tfrac12\zeta[j(j + 1) - \ell(\ell + 1) - \tfrac34]$, pemecahan $(\ell + \tfrac12)\zeta$. Dalam satu suku: $E(J) - E(J - 1) = AJ$; $A > 0$ untuk subkulit kurang dari setengah penuh, $A < 0$ untuk lebih dari setengah. Besarnya naik tajam dengan $Z$.
:::

::: {.contoh}
**Contoh 9.45 · Garis D natrium dan hidrogen 2p**

(a) Garis D₂ ($3\,^2P_{3/2} \to 3\,^2S_{1/2}$) dan D₁ ($3\,^2P_{1/2} \to 3\,^2S_{1/2}$) natrium berada di 589,00 dan 589,59 nm. Hitung pemecahan dalam cm⁻¹ dan $\zeta_{3p}$. (b) Hitung pemecahan 2p hidrogen dengan rumus hidrogen dan bandingkan.

**Penyelesaian.** (a) $10^7/589{,}00 - 10^7/589{,}59 = 17{,}2$ cm⁻¹. Untuk $\ell = 1$, pemecahan $\tfrac32\zeta$, jadi $\zeta_{3p} = 11{,}5$ cm⁻¹.

(b) $\zeta_{2p}(\text{H}) = \alpha_\text{f}^2E_h/[2(8)(1)(1{,}5)(2)] = \alpha_\text{f}^2E_h/48$. Pemecahan $\tfrac32\zeta = \alpha_\text{f}^2E_h/32 = 0{,}365$ cm⁻¹ (10,9 GHz).

**Memahami hasil.** Elektron 3p natrium mengalami kopling spin–orbit hampir lima puluh kali lebih besar daripada elektron 2p hidrogen, walaupun keduanya elektron valensi tunggal. Penyebabnya penetrasi: di dekat inti natrium, yang muatannya 11, elektron 3p merasakan gradien potensial yang jauh lebih curam daripada di dekat proton, dan $\xi(r) \propto r^{-1}dV/dr$ sangat peka terhadap daerah itu. Pemecahan D natrium cukup besar untuk dilihat dengan spektroskop sederhana, dan cukup kecil untuk menjadi uji klasik daya pisah spektrometer.
:::

::: {.contoh}
**Contoh 9.46 · Logam alkali dan halogen: kenaikan dengan Z**

Pemecahan $^2P_{3/2}$–$^2P_{1/2}$ keadaan $np$ tereksitasi pertama logam alkali (cm⁻¹): Li 0,34; Na 17,2; K 57,7; Rb 237,6; Cs 554,0. Pemecahan keadaan dasar $^2P$ halogen: F 404; Cl 882; Br 3685; I 7603. (a) Berapa kali pemecahan naik dari Na ke Cs? (b) Untuk halogen ($p^5$), tingkat mana yang lebih rendah? (c) Berapa fraksi atom F dan I dalam keadaan $^2P_{1/2}$ pada 298 K?

**Penyelesaian.** (a) $554{,}0/17{,}2 = 32$ kali, sedangkan $Z$ naik dari 11 ke 55 (lima kali); kira-kira sebanding dengan $Z^2$ untuk elektron valensi.

(b) $p^5$ lebih dari setengah penuh, sehingga $J$ terbesar terendah: $^2P_{3/2}$ adalah keadaan dasar.

(c) Bobot $2J + 1$: 4 untuk $J = \tfrac32$, 2 untuk $J = \tfrac12$. F: $\tfrac24e^{-404/207} = 0{,}071$, fraksi $0{,}071/1{,}071 = 6{,}6$%. I: $\tfrac24e^{-7603/207} = 6 \times 10^{-17}$, praktis nol.

**Memahami hasil.** Atom iodium dalam keadaan $^2P_{1/2}$ (I*) berada 0,94 eV di atas keadaan dasar dan meluruh sangat lambat (transisi dipol magnet). Laser kimia oksigen–iodium memanfaatkannya: oksigen singlet memindahkan energi ke iodium, menciptakan inversi populasi, dan laser memancar di 1315 nm. Dalam reaksi atom halogen, kedua tingkat spin–orbit sering bereaksi dengan laju berbeda, sehingga untuk atom berat "satu atom" sebenarnya adalah dua spesies kimia.
:::

![Gambar 9.7 Pemecahan spin–orbit terhadap nomor atom (skala logaritma): keadaan $np$ tereksitasi pertama logam alkali dan keadaan dasar $^2$P halogen. Garis tipis menunjukkan kemiringan $Z^2$. Dari Li ke Cs pemecahan naik lebih dari seribu kali, sehingga efek yang hanya terlihat dengan spektroskopi resolusi tinggi pada atom ringan menjadi faktor kimia penting pada atom berat.](fig/c_spinorbit.png){width=72%}

::: {.contoh}
**Contoh 9.47 · Aturan selang Landé dan runtuhnya kopling LS**

Tingkat $^3P_1$ dan $^3P_2$ (relatif terhadap $^3P_0$, cm⁻¹) untuk golongan 14: C 16,4 dan 43,4; Si 77,1 dan 223,2; Ge 557,1 dan 1410,0; Sn 1691,8 dan 3427,7; Pb 7819,3 dan 10 650,3. Menurut (9.42), $[E(2) - E(1)]/[E(1) - E(0)] = 2$. Hitung perbandingan ini dan tafsirkan.

**Penyelesaian.** C: $27{,}0/16{,}4 = 1{,}65$. Si: 1,89. Ge: 1,53. Sn: 1,03. Pb: 0,36.

**Memahami hasil.** Untuk Si dan C, perbandingannya dekat 2: kopling LS baik. Mulai Ge, dan terutama Sn dan Pb, aturan selang runtuh total. Pada timbal, kopling spin–orbit (ribuan cm⁻¹) sudah sebanding dengan pemecahan antarsuku, sehingga $L$ dan $S$ tidak lagi bilangan kuantum yang baik; label $^3$P hanya nama. Lebih tepat menggambarkan Pb dengan kopling jj: dua elektron 6p menempati orbital $6p_{1/2}$ (lebih rendah) yang bersimetri bola. Kestabilan pasangan $6s^2$ dan $6p_{1/2}^2$ ini ikut menjelaskan mengapa timbal lebih menyukai keadaan oksidasi +2 daripada +4, kebalikan dari karbon.
:::

::: {.contoh}
**Contoh 9.48 · Faktor $g$ dan efek Zeeman anomal**

Dalam medan magnet lemah, tingkat $J$ pecah menjadi $2J + 1$ subtingkat dengan energi $g_J\mu_BBM_J$, dengan faktor Landé $g_J = 1 + [J(J + 1) + S(S + 1) - L(L + 1)]/2J(J + 1)$ (dengan $g_e \approx 2$). (a) Hitung $g_J$ untuk $^2S_{1/2}$, $^2P_{1/2}$, dan $^2P_{3/2}$. (b) Berapa komponen garis D₁ dalam medan magnet?

**Penyelesaian.** (a) $^2S_{1/2}$: $1 + (\tfrac34 + \tfrac34 - 0)/(2 \cdot \tfrac34) = 2$. $^2P_{1/2}$: $1 + (\tfrac34 + \tfrac34 - 2)/\tfrac32 = \tfrac23$. $^2P_{3/2}$: $1 + (\tfrac{15}{4} + \tfrac34 - 2)/\tfrac{15}{2} = \tfrac43$.

(b) D₁: $^2P_{1/2}$ ($M_J = \pm\tfrac12$, pemecahan $\tfrac23\mu_BB$) ke $^2S_{1/2}$ ($M_J = \pm\tfrac12$, pemecahan $2\mu_BB$). Dengan $\Delta M_J = 0, \pm1$, ada empat komponen. Energi setiap komponen adalah $(g_\text{atas}M_\text{atas} - g_\text{bawah}M_\text{bawah})\mu_BB$, yaitu $\pm\tfrac23\mu_BB$ (untuk $\Delta M_J = 0$) dan $\pm\tfrac43\mu_BB$ (untuk $\Delta M_J = \pm1$) relatif terhadap pusat garis.

**Memahami hasil.** Seandainya spin tidak ada (atau $g_e = 1$), semua tingkat akan pecah dengan jarak sama dan setiap garis menjadi tiga komponen (efek Zeeman "normal" untuk singlet). Garis-garis alkali pecah menjadi empat atau enam komponen, efek Zeeman "anomal" yang membingungkan fisikawan sebelum 1925 dan ikut mendorong hipotesis spin. Faktor $g$ yang sama menentukan posisi sinyal ESR ion dan radikal (subbab 16.11).
:::

::: {.kuis}
**Kuis cepat 9.13**

(a) Mengapa orbital s tidak mengalami pemecahan spin–orbit? (b) Ramalkan urutan tingkat $J$ dalam suku dasar $^3$P oksigen dan bandingkan dengan Contoh 9.44. (c) Mengapa efek atom berat mempercepat fosforesensi?
:::

## 9.14 Aturan Condon–Slater

### Unsur matriks antara determinan

Hampir setiap perhitungan atom dan molekul memerlukan integral seperti $\langle D|\hat H|D'\rangle$, dengan $D$ dan $D'$ determinan Slater. Menguraikan determinan secara langsung tidak mungkin untuk lebih dari beberapa elektron ($N!$ suku). Untungnya, ortonormalitas spin-orbital membuat hampir semua suku nol, dan hasil akhirnya hanya bergantung pada **berapa banyak spin-orbital yang berbeda** di antara kedua determinan. Aturan-aturannya diturunkan oleh Slater (1929) dan Condon (1930).

Tulis Hamiltonian elektronik sebagai jumlah operator satu elektron dan dua elektron:

$$
\hat H = \sum_i\hat h(i) + \sum_{i<j}\frac{1}{r_{ij}} ,
$$

dan definisikan integral dua elektron atas spin-orbital

$$
\langle ab|cd\rangle = \int\!\!\int\chi_a^*(1)\chi_b^*(2)\frac{1}{r_{12}}\chi_c(1)\chi_d(2)\,d\tau_1d\tau_2 , \qquad \langle ab\|cd\rangle = \langle ab|cd\rangle - \langle ab|dc\rangle . \qquad \text{(9.43)}
$$

Dengan notasi ini, $J_{ab} = \langle ab|ab\rangle$ dan $K_{ab} = \langle ab|ba\rangle$. Integral atas spin membuat $K_{ab} = 0$ bila $\chi_a$ dan $\chi_b$ berspin berlawanan.

### Empat aturan

Susun kolom-kolom kedua determinan agar sebanyak mungkin spin-orbital berada di posisi yang sama (**koinsidensi maksimum**); setiap pertukaran kolom yang diperlukan mengubah tanda.

::: {.inti}
**Aturan Condon–Slater**

1. **Determinan sama**, $D = |\cdots\chi_m\chi_n\cdots|$:
$$\langle D|\hat H|D\rangle = \sum_mh_{mm} + \tfrac12\sum_m\sum_n\langle mn\|mn\rangle .$$
2. **Berbeda satu spin-orbital**, $\chi_m \to \chi_p$:
$$\langle D|\hat H|D_m^p\rangle = h_{mp} + \sum_n\langle mn\|pn\rangle .$$
3. **Berbeda dua spin-orbital**, $\chi_m\chi_n \to \chi_p\chi_q$:
$$\langle D|\hat H|D_{mn}^{pq}\rangle = \langle mn\|pq\rangle .$$
4. **Berbeda tiga atau lebih**: $\langle D|\hat H|D'\rangle = 0$.
:::

Aturan 4 mencerminkan fakta bahwa $\hat H$ paling banyak memuat operator dua elektron: satu suku $1/r_{ij}$ hanya dapat "memindahkan" dua elektron sekaligus. Aturan 1 adalah rumus energi satu determinan (9.25) yang kita pakai di subbab 9.8.

::: {.dalam}
**Lebih dalam: aturan 1 untuk dua elektron**

Ambil $D = \tfrac{1}{\sqrt2}[\chi_a(1)\chi_b(2) - \chi_b(1)\chi_a(2)]$. Bagian satu elektron: $\langle D|\hat h(1) + \hat h(2)|D\rangle$. Uraikan menjadi empat suku. Suku $\tfrac12\langle\chi_a(1)\chi_b(2)|\hat h(1)|\chi_a(1)\chi_b(2)\rangle = \tfrac12h_{aa}\langle\chi_b|\chi_b\rangle = \tfrac12h_{aa}$; suku silang $-\tfrac12\langle\chi_a(1)\chi_b(2)|\hat h(1)|\chi_b(1)\chi_a(2)\rangle = -\tfrac12h_{ab}\langle\chi_b|\chi_a\rangle = 0$. Menjumlahkan semuanya untuk $\hat h(1)$ dan $\hat h(2)$ memberi $h_{aa} + h_{bb}$. Bagian dua elektron:

$$
\langle D|\frac{1}{r_{12}}|D\rangle = \tfrac12\left[\langle ab|ab\rangle - \langle ab|ba\rangle - \langle ba|ab\rangle + \langle ba|ba\rangle\right] = \langle ab|ab\rangle - \langle ab|ba\rangle = J_{ab} - K_{ab} ,
$$

karena $\langle ba|ba\rangle = \langle ab|ab\rangle$ (mengganti nama variabel integrasi) dan kedua integral pertukaran sama. Suku pertukaran muncul dari suku silang yang tidak hilang karena operator $1/r_{12}$ melibatkan kedua elektron sekaligus. Perluasan ke $N$ elektron mengikuti pola yang sama: dari $N!$ suku, hanya suku-suku yang permutasinya sama atau berbeda satu transposisi yang bertahan.
:::

::: {.contoh}
**Contoh 9.49 · Energi helium dan litium dari aturan 1**

(a) Terapkan aturan 1 pada $|1s\alpha\,1s\beta|$. (b) Terapkan pada $|1s\alpha\,1s\beta\,2s\alpha|$ dan peroleh (9.24).

**Penyelesaian.** (a) Bagian satu elektron: $h_{1s} + h_{1s}$. Bagian dua elektron: satu pasangan $(1s\alpha, 1s\beta)$; $J = J_{1s1s}$ dan $K = 0$ (spin berlawanan). Jadi $E = 2h_{1s} + J_{1s1s}$, sesuai subbab 8.3 dan 9.8.

(b) Satu elektron: $2h_{1s} + h_{2s}$. Pasangan: $(1s\alpha, 1s\beta)$: $J_{1s1s}$; $(1s\alpha, 2s\alpha)$: $J_{1s2s} - K_{1s2s}$; $(1s\beta, 2s\alpha)$: $J_{1s2s}$. Jumlah: $E = 2h_{1s} + h_{2s} + J_{1s1s} + 2J_{1s2s} - K_{1s2s}$.

**Memahami hasil.** Aturan 1 mengubah penghitungan energi determinan menjadi akuntansi sederhana: setiap elektron menyumbang $h$, setiap pasangan menyumbang $J$, dan setiap pasangan **berspin sama** dikurangi $K$. Akuntansi inilah yang dipakai di Contoh 9.31 untuk membandingkan konfigurasi kromium.
:::

::: {.contoh}
**Contoh 9.50 · Interaksi konfigurasi helium: $1s^2$ dan $2s^2$**

Dengan orbital He⁺ ($Z = 2$), energi determinan $|1s\alpha\,1s\beta|$ adalah $-2{,}75\ E_h$ dan determinan $|2s\alpha\,2s\beta|$ adalah $2(-\tfrac12) + J_{2s2s}$, dengan $J_{2s2s} = 77Z/512$. (a) Hitung unsur matriks kopling dengan aturan 3. (b) Selesaikan masalah 2 × 2 dan bandingkan penurunan energinya dengan energi korelasi helium.

**Penyelesaian.** (a) Kedua determinan berbeda dua spin-orbital ($1s\alpha \to 2s\alpha$, $1s\beta \to 2s\beta$). Aturan 3: $\langle 1s\alpha\,1s\beta\|2s\alpha\,2s\beta\rangle = \langle 1s\alpha\,1s\beta|2s\alpha\,2s\beta\rangle - \langle 1s\alpha\,1s\beta|2s\beta\,2s\alpha\rangle$. Suku kedua nol (spin), suku pertama $\int\!\!\int 1s(1)2s(1)\,r_{12}^{-1}\,1s(2)2s(2) = K_{1s2s} = 16Z/729 = 0{,}0439\ E_h$.

(b) $E(2s^2) = -1 + 0{,}3008 = -0{,}6992\ E_h$. Matriks $\begin{pmatrix}-2{,}7500 & 0{,}0439\\ 0{,}0439 & -0{,}6992\end{pmatrix}$ memberi akar terendah $-2{,}75094\ E_h$: penurunan $0{,}00094\ E_h$, sesuai pendekatan orde kedua $-K^2/\Delta E = -0{,}0439^2/2{,}051$.

**Memahami hasil.** Satu konfigurasi tereksitasi ganda hanya memberi kurang dari 1 m$E_h$, sekitar 2% energi korelasi helium. Korelasi tersebar atas sangat banyak konfigurasi ($ns^2$, $np^2$, $nd^2$, ... dan kontinu), masing-masing dengan sumbangan kecil; itulah sifat korelasi dinamis. Program CI modern menangani jutaan sampai miliaran determinan dengan aturan Condon–Slater, yang membuat sebagian besar unsur matriks nol (aturan 4) sehingga matriksnya sangat jarang.
:::

::: {.contoh}
**Contoh 9.51 · Energi suku $p^2$ dari determinan**

Untuk dua elektron p, integral Coulomb dan pertukaran antara orbital $m_\ell$ dapat ditulis dengan dua parameter Slater–Condon $F_0$ dan $F_2$: $J(1, 1) = J(1, -1) = F_0 + F_2$, $J(1, 0) = F_0 - 2F_2$, $J(0, 0) = F_0 + 4F_2$, $K(1, 0) = 3F_2$, $K(1, -1) = 6F_2$. (a) Hitung energi $^3$P dari determinan $|p_1\alpha\,p_0\alpha|$ dan energi $^1$D dari $|p_1\alpha\,p_1\beta|$ (bagian tolakan saja). (b) Pakai **aturan jumlah diagonal** (jumlah energi determinan dengan $M_L = 0$, $M_S = 0$ sama dengan jumlah energi suku-suku yang mempunyai komponen itu) untuk memperoleh $E(^1S)$. (c) Ramalkan $[E(^1S) - E(^1D)]/[E(^1D) - E(^3P)]$ dan bandingkan dengan karbon (1,13) dan oksigen (1,14).

**Penyelesaian.** (a) $|p_1\alpha\,p_0\alpha|$ ($M_L = 1$, $M_S = 1$) hanya milik $^3$P: $E = J(1, 0) - K(1, 0) = F_0 - 5F_2$. $|p_1\alpha\,p_1\beta|$ ($M_L = 2$) hanya milik $^1$D: $E = J(1, 1) = F_0 + F_2$.

(b) Determinan dengan $M_L = 0$, $M_S = 0$: $|p_1\alpha\,p_{-1}\beta|$ dan $|p_1\beta\,p_{-1}\alpha|$ (masing-masing $J(1, -1) = F_0 + F_2$) serta $|p_0\alpha\,p_0\beta|$ ($J(0, 0) = F_0 + 4F_2$). Jumlahnya $3F_0 + 6F_2 = E(^1D) + E(^3P) + E(^1S)$, sehingga $E(^1S) = 3F_0 + 6F_2 - (F_0 + F_2) - (F_0 - 5F_2) = F_0 + 10F_2$.

(c) $E(^1D) - E(^3P) = 6F_2$ dan $E(^1S) - E(^1D) = 9F_2$: perbandingannya 1,50. Karbon dan oksigen memberi sekitar 1,13.

**Memahami hasil.** Aturan Condon–Slater dan aturan jumlah diagonal meramalkan urutan suku ($^3$P < $^1$D < $^1$S, sesuai aturan Hund) dari satu parameter saja; dari jarak $^3$P–$^1$D karbon, $F_2 = 1694$ cm⁻¹. Perbandingan terukur yang lebih kecil daripada 1,5 menunjukkan batas pendekatan satu konfigurasi: suku $^1$S bercampur dengan konfigurasi lain ($2s^02p^4$) yang mempunyai suku $^1$S juga dan didorong turun oleh tolakan tingkat (subbab 8.7). Parameter seperti $F_2$ (atau parameter Racah $B$ dan $C$ untuk elektron d) adalah bahasa yang dipakai spektroskopis untuk menyusun diagram Tanabe–Sugano (subbab 14.10).
:::

::: {.contoh}
**Contoh 9.52 · Teorema Brillouin**

Tunjukkan dengan aturan 2 bahwa, bila orbital-orbitalnya adalah orbital Hartree–Fock, unsur matriks antara determinan HF $\Phi_0$ dan determinan tereksitasi tunggal $\Phi_m^p$ (spin-orbital terisi $m$ diganti spin-orbital kosong $p$) adalah nol.

**Penyelesaian.** Aturan 2: $\langle\Phi_0|\hat H|\Phi_m^p\rangle = h_{mp} + \sum_n\langle mn\|pn\rangle$, dengan $n$ menjalani semua spin-orbital terisi. Ini tepat unsur matriks operator Fock antara $\chi_m$ dan $\chi_p$: $\langle\chi_m|\hat F|\chi_p\rangle$. Orbital HF adalah fungsi eigen $\hat F$, sehingga $\langle\chi_m|\hat F|\chi_p\rangle = \varepsilon_p\langle\chi_m|\chi_p\rangle = 0$.

**Memahami hasil.** Determinan HF tidak bercampur langsung dengan determinan tereksitasi tunggal (**teorema Brillouin**); sebenarnya syarat ini setara dengan persamaan HF itu sendiri. Akibatnya, dalam interaksi konfigurasi dan teori perturbasi, koreksi korelasi pertama datang dari eksitasi **ganda** (aturan 3), sesuai gambaran "pasangan elektron yang bersama-sama menghindar". Eksitasi tunggal tetap penting untuk sifat-sifat seperti momen dipol dan untuk keadaan tereksitasi (metode CIS), tetapi tidak untuk energi korelasi keadaan dasar pada orde terendah.
:::

::: {.kuis}
**Kuis cepat 9.14**

(a) Berapa unsur matriks $\hat H$ antara $|1s\alpha\,1s\beta\,2s\alpha|$ dan $|2p\alpha\,2p\beta\,3d\alpha|$? (b) Mengapa aturan 3 tidak memuat integral satu elektron? (c) Untuk determinan $|1s\alpha\,2s\alpha\,2p\alpha|$, berapa integral pertukaran yang muncul dalam energinya?
:::

