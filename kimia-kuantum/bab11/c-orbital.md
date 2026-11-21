## 11.5 Orbital ikatan dan antiikatan

### Interferensi dua orbital atom

Dua fungsi LCAO (11.12) adalah **orbital molekul** (OM) pertama yang kita temui. Kerapatan peluangnya

$$
|\psi_\pm|^2 = \frac{1s_A^2 + 1s_B^2 \pm 2\,1s_A1s_B}{2(1 \pm S)} \qquad \text{(11.17)}
$$

terdiri atas dua bagian: kerapatan atom-atom yang dijumlahkan, dan suku interferensi $\pm 2\,1s_A1s_B$, yang hanya besar di daerah tempat kedua orbital tumpang tindih, yaitu di antara inti. Pada $\psi_+$ suku itu ditambahkan: kerapatan elektron menumpuk di antara inti, tempat elektron ditarik kedua proton sekaligus. Pada $\psi_-$ suku itu dikurangkan: muncul bidang simpul di tengah-tengah, dan kerapatan terdorong ke luar, ke belakang masing-masing inti. Karena itu $\psi_+$ disebut **orbital ikatan** dan $\psi_-$ **orbital antiikatan** (Gambar 11.5).

![Gambar 11.5 Orbital ikatan dan antiikatan H₂⁺ (LCAO, $R = 2$ bohr) pada bidang yang memuat sumbu molekul. Kiri: $\psi_+ = 1\sigma_g$. Tengah: $\psi_- = 1\sigma_u$, dengan bidang simpul di tengah. Kanan: kerapatan selisih $|\psi_+|^2 - \tfrac12(1s_A^2 + 1s_B^2)$; biru menandai penumpukan elektron, jingga pengurangan. Titik hitam adalah inti.](fig/c_orbital_h2p.png){width=95%}

Faktor normalisasi $1/2(1 \pm S)$ juga penting. Integrasi (11.17) di seluruh ruang memberi $[1 + 1 \pm 2S]/[2(1 \pm S)] = 1$: muatan yang ditambahkan ke daerah tumpang tindih pada $\psi_+$ diambil dari daerah dekat inti dan daerah luar, sehingga jumlah total tetap satu elektron. Ikatan bukan "elektron tambahan" di antara inti, melainkan **penataan ulang** kerapatan.

### Label orbital

Kedua orbital bersimetri σ ($m = 0$). Terhadap inversi, $\psi_+$ tidak berubah ($1s_A \leftrightarrow 1s_B$) dan $\psi_-$ berubah tanda. Labelnya, dalam dua notasi yang sama-sama dipakai:

| Orbital | Notasi atom terpisah | Notasi urutan | Notasi atom bersatu |
|---|---|---|---|
| $\psi_+$ | $\sigma_g1s$ | $1\sigma_g$ | $1s\sigma_g$ |
| $\psi_-$ | $\sigma_u^*1s$ | $1\sigma_u$ | $2p\sigma_u$ |

Tanda bintang menandai antiikatan. Notasi urutan ($1\sigma_g$, $2\sigma_g$, ...) memberi nomor menurut energi di antara orbital berlabel simetri sama, seperti $1a_1$, $2a_1$ di Bab 10; notasi inilah yang dipakai dalam spektroskopi dan program kimia kuantum. Notasi atom bersatu menyebut orbital atom He⁺ yang menjadi tujuan OM bila $R \to 0$ (subbab 11.6): orbital antiikatan, dengan bidang simpul tegak lurus sumbu, berubah menjadi orbital $2p_z$.

### Diagram energi orbital

Hasil (11.15) biasanya digambar sebagai diagram tingkat energi: dua orbital atom di kiri dan kanan, dua OM di tengah, ikatan di bawah dan antiikatan di atas. Dengan menulis $\alpha = H_{AA}$ dan $\beta = H_{AB}$, energinya

$$
E_\pm = \frac{\alpha \pm \beta}{1 \pm S} .
$$

Karena $\beta < 0$, $E_+$ di bawah $\alpha$ dan $E_-$ di atas $\alpha$. Dengan tumpang tindih, kenaikan orbital antiikatan lebih besar daripada penurunan orbital ikatan (Contoh 11.15). Jika $S$ diabaikan, kedua pergeseran sama besar, $\pm\beta$: inilah metode Hückel (Bab 13), yang cukup baik untuk membandingkan molekul-molekul serupa.

::: {.inti}
**Aturan pengisian orbital molekul**

1. Orbital molekul diisi dari energi terendah, paling banyak dua elektron per orbital dengan spin berlawanan (asas Pauli, subbab 9.5).
2. Orbital berdegenerasi diisi satu-satu dahulu dengan spin sejajar (aturan Hund).
3. **Orde ikatan** $= \tfrac12$(elektron ikatan $-$ elektron antiikatan). Orde ikatan nol berarti tidak ada ikatan kovalen yang mantap.
:::

::: {.contoh}
**Contoh 11.21 · Penumpukan elektron di titik tengah**

Untuk $\psi_+$ LCAO pada $R = 2$ bohr ($S = 0{,}5865$), hitung kerapatan elektron di titik tengah antarinti dan bandingkan dengan rata-rata kerapatan dua atom H, $\tfrac12(1s_A^2 + 1s_B^2)$, di titik yang sama.

**Penyelesaian.** Di titik tengah $r_A = r_B = 1$: $1s_A = 1s_B = e^{-1}/\sqrt\pi = 0{,}2076$. Maka $\psi_+ = 2(0{,}2076)/\sqrt{2(1{,}5865)} = 0{,}2331$ dan $|\psi_+|^2 = 0{,}0543$ bohr⁻³. Rata-rata atom: $\tfrac12(0{,}0431 + 0{,}0431) = 0{,}0431$ bohr⁻³. Perbandingannya 1,26.

**Memahami hasil.** Orbital ikatan menumpuk 26% lebih banyak kerapatan di titik tengah daripada "atom yang diletakkan berdampingan". Untuk $\psi_-$ kerapatan di titik tengah tepat nol. Peta kerapatan selisih seperti Gambar 11.5 kanan kini dapat diukur dengan difraksi sinar-X resolusi tinggi pada kristal, dan memperlihatkan penumpukan elektron ikatan yang serupa di antara atom-atom yang berikatan kovalen.
:::

::: {.contoh}
**Contoh 11.22 · Populasi tumpang tindih**

Elektron dalam $\psi_\pm$ dapat dibagi menjadi bagian "di atom $A$", "di atom $B$", dan "di daerah tumpang tindih" dengan mengintegrasikan setiap suku (11.17) secara terpisah. Hitung bagian tumpang tindih untuk $\psi_+$ dan $\psi_-$ pada $R = 2$ bohr.

**Penyelesaian.** Integral suku interferensi: $\pm2S/[2(1 \pm S)] = \pm S/(1 \pm S)$. Untuk $\psi_+$: $0{,}5865/1{,}5865 = +0{,}370$ elektron. Untuk $\psi_-$: $-0{,}5865/0{,}4135 = -1{,}418$ elektron. Bagian atom masing-masing: $\psi_+$: $1/(2 \times 1{,}5865) = 0{,}315$ di setiap atom; $\psi_-$: $1/(2 \times 0{,}4135) = 1{,}209$ di setiap atom.

**Memahami hasil.** Besaran ini disebut **populasi tumpang tindih Mulliken**: positif untuk interaksi ikatan, negatif untuk antiikatan (subbab 17.7). Untuk $\psi_-$ bagian "atom" melebihi satu dan bagian tumpang tindih negatif besar: elektron didorong keluar dari daerah antarinti. Ukuran ini kasar karena bergantung pada cara membagi, tetapi tandanya dapat dipercaya, dan dalam bentuk diagram (kurva COOP atau COHP) dipakai luas dalam kimia padatan untuk mengenali ikatan dan antiikatan.
:::

::: {.contoh}
**Contoh 11.23 · Orde ikatan molekul satu dan dua atom H/He**

Dengan dua orbital $1\sigma_g$ dan $1\sigma_u$, tentukan konfigurasi dan orde ikatan H₂⁺, H₂, He₂⁺, dan He₂. Data: $D_0$ H₂⁺ 2,65 eV, H₂ 4,48 eV, He₂⁺ 2,4 eV; He₂ hanya terikat gaya van der Waals dengan $D_e$ sekitar 0,001 eV.

**Penyelesaian.** H₂⁺: $(1\sigma_g)^1$, orde $\tfrac12$. H₂: $(1\sigma_g)^2$, orde 1. He₂⁺: $(1\sigma_g)^2(1\sigma_u)^1$, orde $\tfrac12$. He₂: $(1\sigma_g)^2(1\sigma_u)^2$, orde 0.

**Memahami hasil.** Orde ikatan meramalkan urutan kekuatan dengan benar, dan He₂ dengan orde nol tidak membentuk ikatan kovalen. Karena orbital antiikatan lebih menolak daripada orbital ikatan mengikat, $(1\sigma_g)^2(1\sigma_u)^2$ bahkan menolak bersih. Molekul He₂ hanya ada sebagai pasangan van der Waals yang sangat lemah, yang baru terdeteksi pada 1993 dalam berkas helium dingin, dengan jarak rata-rata antaratom lebih dari 5 nm. Ion He₂⁺ yang terikat kuat terbentuk dalam lucutan helium dan bertanggung jawab atas sebagian spektrum lampu helium.
:::

::: {.contoh}
**Contoh 11.24 · Energi kinetik di orbital ikatan LCAO**

Energi kinetik elektron dalam $\psi_\pm$ adalah $T_\pm = (T_{AA} \pm T_{AB})/(1 \pm S)$, dengan $T_{AA} = \tfrac12$ hartree (atom H) dan $T_{AB} = \langle 1s_A|-\tfrac12\nabla^2|1s_B\rangle = -\tfrac12S + (1 + R)e^{-R}$. Hitung $T_+$ dan $T_-$ pada $R = 2$ bohr.

**Penyelesaian.** $T_{AB} = -\tfrac12(0{,}5865) + 3(0{,}13534) = -0{,}2933 + 0{,}4060 = 0{,}1128$ hartree. $T_+ = (0{,}5 + 0{,}1128)/1{,}5865 = 0{,}386$ hartree; $T_- = (0{,}5 - 0{,}1128)/0{,}4135 = 0{,}936$ hartree.

**Memahami hasil.** Dalam orbital ikatan LCAO dengan $\zeta = 1$, energi kinetik elektron **turun** dari 0,500 ke 0,386 hartree: elektron yang dapat menyebar ke dua atom mempunyai panjang gelombang efektif lebih panjang, seperti partikel dalam kotak yang lebih lebar. Dalam orbital antiikatan, simpul tambahan memaksa fungsi gelombang melengkung tajam, dan energi kinetiknya naik hampir dua kali. Penurunan energi kinetik oleh delokalisasi ternyata adalah salah satu kunci ikatan kimia, tetapi ceritanya belum selesai: di jarak setimbang, teorema virial menuntut energi kinetik total *naik*. Kita kembali ke teka-teki ini di subbab 11.15.
:::

::: {.kuis}
**Kuis cepat 11.5**

\(a) Berapa elektron total yang terkandung dalam (11.17) setelah diintegrasikan, dan mengapa? (b) Apa orde ikatan H₂⁻? (c) Mengapa kerapatan $\psi_-$ di titik tengah tepat nol?
:::

## 11.6 Keadaan tereksitasi H₂⁺ dan bentuk orbital σ, π, δ

### Spektrum keadaan eksak

Program di Contoh 11.12 dapat mencari keadaan-keadaan H₂⁺ lain dengan memilih $m$, paritas fungsi $M(\mu)$, dan banyak simpul. Energi elektroniknya pada $R = 2$ bohr:

| Keadaan | $E_\text{el}$ (hartree) | Keadaan | $E_\text{el}$ (hartree) |
|---|---|---|---|
| $1s\sigma_g$ | $-1{,}1026$ | $3p\sigma_u$ | $-0{,}2554$ |
| $2p\sigma_u$ | $-0{,}6675$ | $3d\sigma_g$ | $-0{,}2358$ |
| $2p\pi_u$ | $-0{,}4288$ | $3d\pi_g$ | $-0{,}2267$ |
| $2s\sigma_g$ | $-0{,}3609$ | $3d\delta_g$ | $-0{,}2127$ |

Setiap keadaan diberi nama menurut orbital atom bersatu (He⁺) yang menjadi tujuannya bila $R \to 0$, ditambah label σ, π, δ dan $g$, $u$. Perhatikan bahwa urutannya tidak sama dengan urutan atom H maupun He⁺: misalnya $2p\pi_u$ lebih rendah daripada $2s\sigma_g$.

### Diagram korelasi

Bagaimana keadaan atom bersatu ($R = 0$) dihubungkan dengan keadaan atom terpisah ($R = \infty$)? Dua aturan menentukan hubungannya. Pertama, simetri ($\lambda$ dan $g/u$) dipertahankan sepanjang $R$, karena simetri silinder dan inversi ada untuk setiap $R$. Kedua, kurva-kurva yang simetrinya sama tidak bersilangan (aturan tak bersilangan, subbab 11.1). Dengan dua aturan ini, keadaan terendah setiap simetri di satu ujung dihubungkan dengan keadaan terendah simetri yang sama di ujung lain, yang kedua dengan yang kedua, dan seterusnya. Hasilnya adalah **diagram korelasi** (Gambar 11.6).

![Gambar 11.6 Diagram korelasi H₂⁺. Kiri: tingkat atom bersatu He⁺ ($R = 0$). Tengah: energi elektronik eksak pada $R = 2$ bohr. Kanan: atom terpisah H + H⁺ ($R = \infty$). Garis menghubungkan keadaan yang simetrinya sama; σ biru, π hijau. Label kanan memakai notasi atom terpisah.](fig/c_korelasi.png){width=88%}

Diagram korelasi menjelaskan sesuatu yang tidak tampak dari LCAO: orbital $\sigma_u^*1s$ (antiikatan) berasal dari orbital $2p$ atom bersatu, dan orbital $\sigma_g2p$ dari atom terpisah berasal dari $3d\sigma_g$. Molekul nyata berada di antara kedua batas; makin pendek ikatannya, makin mirip urutan orbitalnya dengan atom bersatu. Inilah dasar kualitatif urutan OM diatom periode 2 (subbab 11.8).

### Orbital molekul dari orbital 2s dan 2p

Untuk molekul periode 2, orbital valensinya dibangun dari orbital $2s$ dan $2p$ kedua atom. Pilih sumbu $z$ sepanjang ikatan, dengan sumbu $z$ setiap atom menunjuk ke atom yang lain. Kombinasi yang diizinkan simetri adalah:

- **Dari 2s**: $\sigma_g2s = 2s_A + 2s_B$ dan $\sigma_u^*2s = 2s_A - 2s_B$, mirip dengan 1s.
- **Dari $2p_z$** (menunjuk sepanjang sumbu): bila kedua cuping positif menunjuk satu sama lain, tumpang tindihnya positif dan menghasilkan $\sigma_g2p$ (ikatan); kombinasi yang berlawanan menghasilkan $\sigma_u^*2p$. Keduanya bersimetri σ karena $2p_z$ tidak berubah oleh putaran terhadap sumbu.
- **Dari $2p_x$ dan $2p_y$** (tegak lurus sumbu): $2p_{xA} + 2p_{xB}$ bertumpang tindih ke samping, membentuk ikatan π dengan bidang simpul yang memuat sumbu. Pasangan $2p_x$ dan $2p_y$ memberi dua orbital π berdegenerasi, $\pi_u2p$ (ikatan) dan $\pi_g^*2p$ (antiikatan).

Satu hal yang sering membingungkan: untuk orbital π, kombinasi *jumlah* bersifat $u$ dan kombinasi *selisih* bersifat $g$, kebalikan dari σ. Inversi membawa cuping atas $p_x$ di $A$ ke cuping bawah di $B$, yang bertanda berlawanan. Maka $p_{xA} \to -p_{xB}$, sehingga $p_{xA} + p_{xB} \to -(p_{xA} + p_{xB})$: ungerade. Label $g/u$ tidak sama dengan "ikatan/antiikatan"; hanya untuk σ keduanya kebetulan sejalan.

![Gambar 11.7 Bentuk orbital molekul valensi diatom homonuklir, digambar dari kombinasi orbital Slater pada bidang $xz$ (sumbu molekul mendatar). Atas: $\sigma_g2s$, $\sigma_u^*2s$, $\sigma_g2p$, $\sigma_u^*2p$. Bawah: $\pi_u2p$, $\pi_g^*2p$, serta $\delta_g$ dan $\delta_u^*$ dari orbital $d_{xy}$, digambar pada bidang yang memuat sumbu molekul dan garis $x = y$. Biru positif, jingga negatif.](fig/c_sigmapi.png){width=98%}

### σ, π, δ: berapa bidang simpul yang memuat sumbu

Huruf σ, π, δ menyatakan $\lambda = |m|$, komponen momentum sudut elektron sepanjang sumbu. Secara geometri, $\lambda$ sama dengan banyaknya **bidang simpul yang memuat sumbu molekul**: σ tidak mempunyai bidang simpul seperti itu, π mempunyai satu, dan δ dua. Orbital antiikatan mempunyai tambahan satu bidang simpul tegak lurus sumbu, di antara kedua inti. Ikatan δ terbentuk dari orbital $d_{xy}$ atau $d_{x^2-y^2}$ kedua atom yang bertumpang tindih "muka ke muka"; ikatan ini dijumpai pada senyawa logam transisi dengan ikatan logam–logam rangkap.

::: {.contoh}
**Contoh 11.25 · Keadaan mana yang terikat?**

Dengan tabel energi eksak pada $R = 2$ bohr, hitung energi total ($E_\text{el} + 1/R$) keadaan $1s\sigma_g$, $2p\sigma_u$, dan $2p\pi_u$, lalu bandingkan dengan batas atom terpisahnya: H(1s) + H⁺ untuk dua keadaan pertama ($-0{,}5$ hartree) dan H($n = 2$) + H⁺ untuk yang ketiga ($-0{,}125$ hartree).

**Penyelesaian.** $1s\sigma_g$: $-1{,}1026 + 0{,}5 = -0{,}6026$, lebih rendah 0,103 hartree dari batasnya. $2p\sigma_u$: $-0{,}6675 + 0{,}5 = -0{,}1675$, lebih tinggi 0,333 hartree. $2p\pi_u$: $-0{,}4288 + 0{,}5 = +0{,}0712$, lebih tinggi 0,196 hartree dari $-0{,}125$.

**Memahami hasil.** Pada $R = 2$ hanya keadaan dasar yang terikat. Keadaan $2p\pi_u$ menolak di jarak itu, tetapi perhitungan untuk banyak $R$ menunjukkan bahwa ia mempunyai sumur dangkal pada jarak sekitar 8 bohr: orbital π yang dibangun dari $2p$ mengikat lemah di jarak yang sesuai dengan ukuran orbital $2p$ yang besar. Hal yang sama berlaku untuk molekul nyata: setiap jenis ikatan mempunyai jarak optimum yang ditentukan oleh ukuran orbital penyusunnya.
:::

::: {.contoh}
**Contoh 11.26 · Tumpang tindih σ dan π dalam N₂ dan F₂**

Dengan orbital $2p$ Slater ($\zeta = 1{,}95$ untuk N dan 2,60 untuk F), integrasi numerik dalam koordinat eliptik pada jarak setimbang (N₂: 109,8 pm; F₂: 141,2 pm) memberi tumpang tindih berikut. N₂: $S_\sigma = 0{,}321$, $S_\pi = 0{,}280$. F₂: $S_\sigma = 0{,}176$, $S_\pi = 0{,}048$. Apa artinya bagi kekuatan ikatan π?

**Penyelesaian.** Pada N₂, tumpang tindih π hampir sebesar tumpang tindih σ, sehingga kedua ikatan π memberi sumbangan besar pada ikatan rangkap tiga. Pada F₂, ikatannya jauh lebih panjang dan orbital $2p$ fluorin lebih kecil ($\zeta$ besar), sehingga tumpang tindih π hampir lenyap: sisi-sisi cuping $p$ hampir tidak bersentuhan.

**Memahami hasil.** Tumpang tindih π meluruh lebih cepat daripada tumpang tindih σ ketika jarak bertambah, karena cuping π bertemu "dari samping". Inilah alasan ikatan π penting terutama untuk unsur periode 2 yang kecil (C, N, O), sedangkan untuk unsur periode 3 dan seterusnya, dengan ikatan yang lebih panjang, ikatan rangkap jauh lebih lemah. Silikon jarang membentuk Si=Si yang mantap, sedangkan karbon membentuk C=C dengan mudah ("aturan ikatan rangkap").
:::

::: {.contoh}
**Contoh 11.27 · Paritas orbital π dan δ**

Tentukan label $g$ atau $u$ untuk (a) $p_{yA} - p_{yB}$, (b) $d_{xyA} + d_{xyB}$, dan (c) $d_{xyA} - d_{xyB}$, dengan sumbu $z$ setiap atom sejajar (bukan saling menunjuk).

**Penyelesaian.** Inversi melalui titik tengah memindahkan atom $A$ ke $B$ dan membalik semua koordinat relatif terhadap atom: $p_y \to -p_y$ dan $d_{xy} \to +d_{xy}$ (karena $(-x)(-y) = xy$). (a) $p_{yA} - p_{yB} \to -p_{yB} + p_{yA}$: tidak berubah, $g$ (yaitu $\pi_g^*$). (b) $d_{xyA} + d_{xyB} \to d_{xyB} + d_{xyA}$: $g$ ($\delta_g$, ikatan). (c) $u$ ($\delta_u^*$, antiikatan).

**Memahami hasil.** Orbital d mempunyai paritas atom genap, sehingga, seperti s, kombinasi jumlahnya $g$. Orbital p berparitas ganjil, sehingga kombinasi jumlahnya $u$. Aturan umum: paritas OM = paritas orbital atom × (+1 untuk jumlah, $-1$ untuk selisih), bila sumbu lokal kedua atom sejajar.
:::

::: {.contoh}
**Contoh 11.28 · Ikatan rangkap empat dalam [Re₂Cl₈]²⁻**

Dalam ion [Re₂Cl₈]²⁻, dua atom Re ($d^4$ setelah memperhitungkan muatan ligan) terikat dengan jarak hanya 224 pm, dan kedua gugus ReCl₄ berada dalam konformasi **tindih** (*eclipsed*), meskipun konformasi bersilang mengurangi tolakan antarligan. Delapan elektron d menempati $\sigma^2\pi^4\delta^2$. Jelaskan orde ikatan dan konformasinya.

**Penyelesaian.** Orbital ikatan σ ($d_{z^2}$), π ($d_{xz}$, $d_{yz}$), dan δ ($d_{xy}$) terisi semuanya, tanpa elektron antiikatan: orde ikatan $\tfrac12(8 - 0) = 4$. Tumpang tindih δ antara $d_{xy}$ kedua atom maksimum bila keempat cupingnya sejajar (konformasi tindih) dan nol bila satu atom diputar 45° (cuping positif $A$ berhadapan sama banyak dengan cuping positif dan negatif $B$).

**Memahami hasil.** Konformasi tindih adalah bukti eksperimen ikatan δ: tanpa ikatan δ tidak ada alasan memilih konformasi yang lebih berdesakan. Penemuan ikatan rangkap empat oleh F. A. Cotton pada 1964 memperluas konsep orde ikatan jauh melampaui ikatan rangkap tiga yang dikenal dalam kimia organik. Ikatan δ lemah karena tumpang tindihnya kecil, dan transisi $\delta \to \delta^*$ memberi warna biru kompleks ini.
:::

::: {.contoh}
**Contoh 11.29 · Fotodisosiasi H₂⁺**

Pada $R = 2$ bohr, energi total eksak H₂⁺ adalah $-0{,}60263$ ($1s\sigma_g$), $-0{,}16753$ ($2p\sigma_u$), dan $+0{,}07123$ hartree ($2p\pi_u$). (a) Hitung energi foton untuk transisi vertikal dari keadaan dasar ke kedua keadaan itu, beserta panjang gelombangnya. (b) Apakah kedua transisi diizinkan, dan bagaimana polarisasinya? (c) Setelah menyerap foton ke $2p\sigma_u$, ion terurai menjadi H + H⁺. Berapa energi kinetik total kedua fragmen?

**Penyelesaian.** (a) $\sigma_g \to \sigma_u$: $0{,}43510$ hartree $= 11{,}84$ eV, $\lambda = 1239{,}8/11{,}84 = 104{,}7$ nm. $\sigma_g \to \pi_u$: $0{,}67386$ hartree $= 18{,}34$ eV, $\lambda = 67{,}6$ nm. (b) Keduanya $g \to u$ dan $\Delta\Lambda = 0$ atau 1, jadi diizinkan. Transisi Σ → Σ dirangsang oleh komponen medan sepanjang sumbu molekul (polarisasi sejajar); Σ → Π oleh komponen tegak lurus. (c) Keadaan $2p\sigma_u$ pada $R = 2$ berada $-0{,}16753 - (-0{,}5) = 0{,}33247$ hartree $= 9{,}05$ eV di atas H + H⁺. Karena kurvanya menolak murni, seluruh energi itu menjadi energi kinetik fragmen, masing-masing sekitar 4,5 eV (massanya hampir sama).

**Memahami hasil.** Keadaan $2p\sigma_u$ adalah contoh **kurva menolak**: penyerapan ke kurva seperti ini selalu berakhir dengan disosiasi, dalam waktu yang sebanding dengan satu periode getaran. Polarisasi sejajar berarti molekul yang sumbunya sejajar medan listrik cahaya yang paling banyak terurai, sehingga fragmen-fragmen terlempar terutama sepanjang arah polarisasi. Pengukuran sebaran sudut fragmen dalam percobaan fotodisosiasi memakai gejala ini untuk mengenali simetri keadaan tereksitasi.
:::

::: {.kuis}
**Kuis cepat 11.6**

\(a) Berapa bidang simpul yang memuat sumbu pada orbital $\pi_g^*$? Berapa bidang simpul tegak lurus sumbu? (b) Mengapa $2p\pi_u$ dan $2p\sigma_u$ berdegenerasi pada $R = 0$ tetapi tidak pada $R = 2$? (c) Mengapa $p_{xA}$ tidak dapat bergabung dengan $s_B$ untuk membentuk OM?
:::
