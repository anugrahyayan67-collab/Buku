## 10.9 Mode vibrasi, aktivitas IR dan Raman

### Dari $3N$ koordinat ke mode normal

Molekul dengan $N$ atom mempunyai $3N$ derajat kebebasan gerak inti: 3 translasi, 3 rotasi (2 untuk molekul linear), dan $3N - 6$ getaran ($3N - 5$ untuk molekul linear). Di subbab 5.11 kita melihat bahwa getaran kecil dapat diuraikan menjadi **mode normal**, gerak kolektif yang setiap modenya berperilaku sebagai osilator harmonik tersendiri dengan frekuensinya sendiri. Mode normal adalah vektor eigen matriks tetapan gaya yang diberi bobot massa, dan matriks itu tidak berubah oleh operasi simetri molekul. Akibatnya, menurut alasan yang sama dengan orbital, setiap mode normal bertransformasi menurut satu irrep grup titik, dan mode yang irrepnya berdimensi $d$ berdegenerasi $d$ kali lipat.

Simetri mode normal dapat ditemukan tanpa mengetahui tetapan gaya sama sekali. Caranya: bangun representasi $\Gamma_{3N}$ dengan basis $3N$ vektor perpindahan Kartesius (tiga panah kecil di setiap atom), reduksi, lalu kurangkan translasi dan rotasi.

### Karakter $\Gamma_{3N}$

Karakter $\Gamma_{3N}$ mudah dihitung. Bila operasi $R$ memindahkan sebuah atom ke posisi atom lain, ketiga panahnya berpindah ke atom lain dan tidak menyumbang apa pun pada unsur diagonal matriks. Hanya atom yang **tidak berpindah** yang menyumbang, dan sumbangannya adalah teras matriks 3 × 3 operasi itu (10.3). Jadi

$$
\chi_{3N}(R) = N_R \times \left(\pm1 + 2\cos\theta_R\right) , \qquad \text{(10.16)}
$$

dengan $N_R$ banyak atom yang tidak berpindah oleh $R$, tanda $+$ untuk operasi sejati dan $-$ untuk operasi tak sejati, dan $\theta_R$ sudut putarnya. Sumbangan per atom yang sering dipakai:

| Operasi | $E$ | $C_2$ | $C_3$ | $C_4$ | $C_6$ | $\sigma$ | $i$ | $S_3$ | $S_4$ | $S_6$ |
|---|---|---|---|---|---|---|---|---|---|---|
| Sumbangan per atom | 3 | $-1$ | 0 | 1 | 2 | 1 | $-3$ | $-2$ | $-1$ | 0 |

Setelah $\Gamma_{3N}$ direduksi, kurangkan irrep translasi (irrep $x$, $y$, $z$ dalam tabel karakter) dan rotasi (irrep $R_x$, $R_y$, $R_z$):

$$
\Gamma_\text{vib} = \Gamma_{3N} - \Gamma_\text{trans} - \Gamma_\text{rot} . \qquad \text{(10.17)}
$$

Untuk molekul linear, hanya dua rotasi yang dikurangkan (rotasi terhadap sumbu molekul tidak memindahkan inti).

### Aturan seleksi IR dan Raman

Transisi getaran fundamental membawa molekul dari keadaan dasar $v = 0$ semua mode ke $v = 1$ pada satu mode $k$. Fungsi gelombang keadaan dasar adalah hasil kali fungsi Gauss $e^{-\alpha_kQ_k^2/2}$ untuk semua mode; setiap faktor tidak berubah oleh operasi apa pun (operasi hanya dapat mengubah tanda $Q_k$ atau mencampur mode berdegenerasi tanpa mengubah jumlah kuadratnya), sehingga keadaan dasar bersimetri total. Keadaan $v_k = 1$ sebanding dengan $Q_ke^{-\alpha Q^2/2}$ (polinom Hermite derajat satu, subbab 5.3), sehingga bertransformasi seperti $Q_k$ sendiri, yaitu menurut $\Gamma_k$. Momen dipol transisi $\langle 1_k|\hat\mu_q|0\rangle$ tidak nol hanya bila $\Gamma_k \times \Gamma_q \times A_1$ memuat $A_1$, yaitu bila $\Gamma_k = \Gamma_q$:

::: {.inti}
**Aturan seleksi getaran fundamental**

- **Aktif IR**: mode yang irrepnya sama dengan irrep salah satu dari $x$, $y$, atau $z$. Mode itu mengubah momen dipol ke arah yang bersesuaian. $\qquad \text{(10.18)}$
- **Aktif Raman**: mode yang irrepnya sama dengan irrep salah satu fungsi kuadrat ($x^2$, $y^2$, $z^2$, $xy$, $xz$, $yz$ atau kombinasinya), karena komponen tensor polarisabilitas $\alpha_{qq'}$ bertransformasi seperti hasil kali $qq'$. $\qquad \text{(10.19)}$
- **Aturan saling meniadakan**: pada molekul yang mempunyai pusat inversi, $x$, $y$, $z$ semuanya $u$ dan fungsi kuadrat semuanya $g$. Tidak ada mode yang sekaligus aktif IR dan Raman.
- Mode yang tidak aktif keduanya disebut **mode bisu** (*silent*); mode itu hanya tampak sebagai bagian pita kombinasi atau melalui hamburan neutron.
:::

Aturan Raman memberi satu alat tambahan. Hanya mode bersimetri total yang menghasilkan garis Raman **terpolarisasi** (rasio depolarisasi kurang dari 3/4), karena hanya mode itu yang mengubah bagian isotropik polarisabilitas, $\alpha_{xx} + \alpha_{yy} + \alpha_{zz}$. Mengukur polarisasi garis Raman adalah cara langsung mengenali mode $A_1$.

::: {.contoh}
**Contoh 10.41 · Getaran air**

Tentukan simetri, aktivitas IR, dan aktivitas Raman ketiga getaran H₂O. Frekuensi terukurnya 3657, 1595, dan 3756 cm⁻¹.

**Penyelesaian.** Dari Contoh 10.27, $\Gamma_{3N} = 3A_1 + A_2 + 2B_1 + 3B_2$. Translasi: $A_1 + B_1 + B_2$ ($z$, $x$, $y$); rotasi: $A_2 + B_1 + B_2$ ($R_z$, $R_y$, $R_x$). Maka $\Gamma_\text{vib} = 2A_1 + B_2$. Dari tabel $C_{2v}$, $A_1$ memuat $z$ dan $x^2$, $y^2$, $z^2$; $B_2$ memuat $y$ dan $yz$. Ketiga mode aktif IR dan aktif Raman. Kedua mode $A_1$ adalah ulur simetris (3657 cm⁻¹) dan tekuk (1595 cm⁻¹), dengan dipol berubah sepanjang $z$; mode $B_2$ adalah ulur asimetris (3756 cm⁻¹), dengan dipol berubah sepanjang $y$ (Gambar 10.7).

**Memahami hasil.** Analisis simetri tidak memberi frekuensi, tetapi memberi bentuk umum mode: mode $A_1$ mempertahankan semua unsur simetri (kedua ikatan meregang bersama, atau sudut membuka dan menutup), sedangkan mode $B_2$ merusak sumbu $C_2$ (satu ikatan memanjang ketika yang lain memendek). Dalam spektrum Raman air cair, pita ulur 3400 cm⁻¹ yang lebar memperlihatkan komponen terpolarisasi kuat, sesuai dengan sumbangan mode ulur simetris $A_1$.
:::

![Gambar 10.7 Tiga mode normal H₂O, dihitung dari medan gaya valensi sederhana. Panah menunjukkan arah dan besar relatif perpindahan atom H; atom O ikut bergerak sedikit ke arah yang menjaga pusat massa tetap, tetapi perpindahannya terlalu kecil untuk digambar karena O jauh lebih berat. Dua mode pertama bersimetri $A_1$; mode ketiga $B_2$ merusak sumbu $C_2$.](fig/c_mode_h2o.png){width=92%}

::: {.contoh}
**Contoh 10.42 · Amonia: enam mode, empat frekuensi**

Tentukan $\Gamma_\text{vib}$ NH₃ dan banyak pita IR serta Raman.

**Penyelesaian.** Atom tak berpindah: $E$: 4; $C_3$: 1 (N); $\sigma_v$: 2 (N dan satu H). Karakter dengan (10.16): $\chi = (12, 0, 2)$. Reduksi dalam $C_{3v}$: $n(A_1) = \tfrac16(12 + 0 + 6) = 3$, $n(A_2) = \tfrac16(12 + 0 - 6) = 1$, $n(E) = \tfrac16(24 + 0 + 0) = 4$. $\Gamma_{3N} = 3A_1 + A_2 + 4E$. Kurangkan translasi $A_1 + E$ dan rotasi $A_2 + E$: $\Gamma_\text{vib} = 2A_1 + 2E$. Periksa: $2 + 2 \times 2 = 6 = 3N - 6$. Karena $A_1$ memuat $z$ dan $E$ memuat $(x, y)$, keempat frekuensi aktif IR; karena $A_1$ dan $E$ juga memuat fungsi kuadrat, keempatnya aktif Raman.

**Memahami hasil.** Frekuensi terukur: $\nu_1(A_1) = 3337$ cm⁻¹ (ulur simetris), $\nu_2(A_1) = 950$ cm⁻¹ (tekuk "payung"), $\nu_3(E) = 3444$ cm⁻¹ (ulur asimetris, berdegenerasi), dan $\nu_4(E) = 1627$ cm⁻¹ (tekuk asimetris). Pita payung terbelah menjadi dua komponen, 932 dan 968 cm⁻¹, akibat penerobosan inversi amonia (subbab 3.12): mode inilah yang membawa molekul melewati bentuk datar.
:::

::: {.contoh}
**Contoh 10.43 · Metana dan koordinat internal**

(a) Tentukan $\Gamma_\text{vib}$ CH₄. (b) Dengan basis empat vektor ulur C–H, tentukan mode mana yang terutama ulur dan mana yang tekuk. (c) Ramalkan banyak pita IR dan Raman.

**Penyelesaian.** (a) Atom tak berpindah: $E$: 5; $C_3$: 2; $C_2$: 1; $S_4$: 1; $\sigma_d$: 3. Karakter: $(15, 0, -1, -1, 3)$. Reduksi dalam $T_d$ memberi $\Gamma_{3N} = A_1 + E + T_1 + 3T_2$. Translasi $T_2$, rotasi $T_1$: $\Gamma_\text{vib} = A_1 + E + 2T_2$ ($1 + 2 + 6 = 9$ mode).

\(b) Empat vektor ulur bertransformasi seperti empat orbital H: $\Gamma_\text{ulur} = A_1 + T_2$ (Contoh 10.26). Sisanya, $E + T_2$, adalah tekuk.

\(c) IR: hanya $T_2$ (memuat $x$, $y$, $z$): dua pita, ulur $\nu_3$ dan tekuk $\nu_4$. Raman: $A_1$, $E$, dan $T_2$ semuanya memuat fungsi kuadrat: empat pita.

**Memahami hasil.** Spektrum IR metana memang hanya memperlihatkan dua pita fundamental, di 3019 cm⁻¹ ($\nu_3$) dan 1306 cm⁻¹ ($\nu_4$). Ulur simetris $\nu_1$ (2917 cm⁻¹) dan tekuk $\nu_2$ (1534 cm⁻¹) hanya tampak di Raman. Pita $\nu_4$ di 7,7 µm terletak di tepi jendela atmosfer, dan itulah yang membuat metana menjadi gas rumah kaca yang kuat.
:::

::: {.contoh}
**Contoh 10.44 · Karbon dioksida dan molekul linear**

Grup $D_{\infty h}$ mempunyai tak hingga banyak operasi, sehingga rumus reduksi tidak dapat dipakai langsung. Kerjakan analisis CO₂ dalam subgrup $D_{2h}$, lalu terjemahkan hasilnya.

**Penyelesaian.** Ambil sumbu molekul sebagai $z$. Atom tak berpindah: $E$: 3; $C_2(z)$: 3; $C_2(y)$: 1; $C_2(x)$: 1; $i$: 1; $\sigma(xy)$: 1; $\sigma(xz)$: 3; $\sigma(yz)$: 3. Dengan sumbangan $3, -1, -1, -1, -3, 1, 1, 1$ diperoleh $\chi = (9, -3, -1, -1, -3, 1, 3, 3)$. Reduksi dalam $D_{2h}$: $\Gamma_{3N} = A_g + B_{2g} + B_{3g} + 2B_{1u} + 2B_{2u} + 2B_{3u}$. Kurangkan translasi ($B_{1u} + B_{2u} + B_{3u}$) dan hanya dua rotasi ($R_x$: $B_{3g}$, $R_y$: $B_{2g}$): $\Gamma_\text{vib} = A_g + B_{1u} + B_{2u} + B_{3u}$. Dalam bahasa $D_{\infty h}$: $A_g$ menjadi $\Sigma_g^+$ (ulur simetris), $B_{1u}$ menjadi $\Sigma_u^+$ (ulur asimetris), dan pasangan $B_{2u} + B_{3u}$ menyatu menjadi $\Pi_u$ (tekuk berdegenerasi dua).

**Memahami hasil.** Aktif IR: $\Sigma_u^+$ (2349 cm⁻¹) dan $\Pi_u$ (667 cm⁻¹). Aktif Raman: hanya $\Sigma_g^+$ (sekitar 1333 cm⁻¹, tampak sebagai pasangan 1285/1388 cm⁻¹ karena resonansi Fermi dengan nada atas tekuk). CO₂ sentrosimetris sehingga mematuhi aturan saling meniadakan, sebagaimana sudah dicatat di subbab 5.8. Pita tekuk 667 cm⁻¹, yaitu 15,0 µm, jatuh tepat di puncak pancaran termal Bumi: itulah pita yang membuat CO₂ menjadi gas rumah kaca utama.
:::

::: {.contoh}
**Contoh 10.45 · SF₆: aturan saling meniadakan dan mode bisu**

Tentukan $\Gamma_\text{vib}$ SF₆ ($O_h$) dan klasifikasikan aktivitasnya.

**Penyelesaian.** Atom tak berpindah: $E$: 7; $C_3$: 1; $C_2$: 1; $C_4$: 3; $C_4^2$: 3; $i$: 1; $S_4$: 1; $S_6$: 1; $\sigma_h$: 5; $\sigma_d$: 3. Dengan sumbangan per atom, $\chi = (21, 0, -1, 3, -3, -3, -1, 0, 5, 3)$. Reduksi dalam $O_h$: $\Gamma_{3N} = A_{1g} + E_g + T_{1g} + T_{2g} + 3T_{1u} + T_{2u}$. Kurangkan $T_{1u}$ (translasi) dan $T_{1g}$ (rotasi):

$$
\Gamma_\text{vib} = A_{1g} + E_g + T_{2g} + 2T_{1u} + T_{2u} .
$$

Periksa: $1 + 2 + 3 + 6 + 3 = 15 = 3(7) - 6$. Aktif IR: $2T_{1u}$ (dua pita). Aktif Raman: $A_{1g}$, $E_g$, $T_{2g}$ (tiga pita, dengan $A_{1g}$ terpolarisasi). Bisu: $T_{2u}$.

**Memahami hasil.** Frekuensi terukur: IR $\nu_3 = 948$ dan $\nu_4 = 615$ cm⁻¹; Raman $\nu_1 = 775$, $\nu_2 = 643$, dan $\nu_5 = 525$ cm⁻¹; mode bisu $\nu_6 \approx 348$ cm⁻¹, yang diketahui dari pita kombinasi (Gambar 10.8). Tidak satu pun frekuensi muncul di kedua spektrum. Pita $\nu_3$ yang sangat kuat di 10,5 µm terletak di tengah jendela atmosfer (8–13 µm) yang hampir tidak diserap gas lain. Ditambah umurnya di atmosfer yang ribuan tahun, hal ini membuat SF₆ menjadi gas rumah kaca terkuat yang dikenal per molekul, lebih dari 20 000 kali CO₂ per satuan massa dalam rentang seratus tahun.
:::

![Gambar 10.8 Spektrum getaran SF₆ secara skematis: atas IR, bawah Raman. Tidak ada frekuensi yang muncul di keduanya (aturan saling meniadakan untuk molekul sentrosimetris). Garis putus-putus di 348 cm⁻¹ menandai mode bisu $T_{2u}$. Intensitas hanya kualitatif.](fig/c_sf6.png){width=85%}

::: {.contoh}
**Contoh 10.46 · Membedakan isomer kompleks karbonil**

Kompleks M(CO)₄L₂ oktahedral dapat berbentuk *cis* ($C_{2v}$) atau *trans* ($D_{4h}$), dan M(CO)₃L₃ dapat berbentuk *fac* ($C_{3v}$) atau *mer* ($C_{2v}$). Ramalkan banyak pita ulur C≡O di spektrum IR masing-masing. Anggap getaran C≡O hanya bercampur dengan sesamanya.

**Penyelesaian.** Gunakan basis vektor ulur C≡O; karakternya adalah banyak gugus CO yang tidak berpindah.

- *cis*-M(CO)₄L₂, $C_{2v}$: $\chi = (4, 0, 2, 2)$, tereduksi menjadi $2A_1 + B_1 + B_2$. Semuanya aktif IR: **empat** pita.
- *trans*-M(CO)₄L₂, $D_{4h}$ (keempat CO di bidang $xy$): $\chi(E) = 4$, $\chi(C_2') = 2$, $\chi(\sigma_h) = 4$, $\chi(\sigma_v) = 2$, lainnya 0. Tereduksi menjadi $A_{1g} + B_{1g} + E_u$. Aktif IR hanya $E_u$: **satu** pita (dan dua pita Raman).
- *fac*-M(CO)₃L₃, $C_{3v}$: $\chi = (3, 0, 1)$, tereduksi menjadi $A_1 + E$: **dua** pita IR.
- *mer*-M(CO)₃L₃, $C_{2v}$: $\chi = (3, 1, 1, 3)$ (dengan sumbu $C_2$ sepanjang CO yang berseberangan dengan L), tereduksi menjadi $2A_1 + B_2$: **tiga** pita IR.

**Memahami hasil.** Ahli kimia organologam memakai hitungan ini setiap hari. Pita C≡O sangat kuat dan terletak di daerah yang bersih (1850–2150 cm⁻¹), sehingga banyaknya pita langsung mengungkap geometri. Misalnya, spektrum IR yang hanya memperlihatkan satu pita C≡O kuat untuk Mo(CO)₄(PR₃)₂ menunjukkan isomer *trans*. Untuk Cr(CO)₆ ($O_h$), basis enam CO tereduksi menjadi $A_{1g} + E_g + T_{1u}$, sehingga hanya satu pita IR, di sekitar 2000 cm⁻¹.
:::

::: {.contoh}
**Contoh 10.47 · Datar atau piramida?**

Molekul AX₃ dapat datar ($D_{3h}$, seperti SO₃ atau BF₃) atau piramida ($C_{3v}$, seperti NH₃ atau XeO₃). Bagaimana spektrum IR dan Raman membedakan keduanya?

**Penyelesaian.** *Datar*: atom tak berpindah $E$: 4; $C_3$: 1; $C_2$: 2; $\sigma_h$: 4; $S_3$: 1; $\sigma_v$: 2. Karakter $(12, 0, -2, 4, -2, 2)$, tereduksi menjadi $\Gamma_{3N} = A_1' + A_2' + 3E' + 2A_2'' + E''$. Kurangkan translasi ($E' + A_2''$) dan rotasi ($A_2' + E''$): $\Gamma_\text{vib} = A_1' + A_2'' + 2E'$. IR: $A_2''$ dan $2E'$, tiga pita. Raman: $A_1'$ dan $2E'$, tiga pita. Dua frekuensi ($E'$) muncul di keduanya, satu ($A_1'$) hanya di Raman, satu ($A_2''$) hanya di IR.

*Piramida*: $\Gamma_\text{vib} = 2A_1 + 2E$ (Contoh 10.42); keempat frekuensi muncul di IR dan di Raman.

**Memahami hasil.** Untuk BF₃: $\nu_1(A_1') = 888$ cm⁻¹ hanya Raman; $\nu_2(A_2'') = 691$ cm⁻¹ (tekuk keluar bidang) hanya IR; $\nu_3(E') = 1454$ dan $\nu_4(E') = 480$ cm⁻¹ di keduanya. Pola "tiga dan tiga, dua bersamaan" adalah tanda geometri datar. Analisis seperti ini dipakai untuk menentukan bentuk molekul baru sebelum kristalografi atau difraksi elektron tersedia. Perhatikan bahwa BF₃ tidak sentrosimetris, sehingga aturan saling meniadakan tidak berlaku, tetapi simetri tetap memisahkan mode $A_1'$ dan $A_2''$.
:::

::: {.contoh}
**Contoh 10.48 · Jawaban teka-teki C₆₀**

Untuk C₆₀ ($I_h$), operasi apa pun selain $E$ dan $\sigma$ memindahkan semua atom, sedangkan setiap bidang cermin memuat empat atom. (a) Tunjukkan bahwa banyaknya irrep $\Gamma_i$ dalam $\Gamma_{3N}$ adalah $n_i = \tfrac12(3d_i + \chi_i(\sigma))$. (b) Pakai tabel karakter $I_h$ (untuk irrep $g$, $\chi(\sigma) = \chi(C_2)$; untuk $u$, $\chi(\sigma) = -\chi(C_2)$; dengan $\chi(C_2) = 1, -1, -1, 0, 1$ untuk $A$, $T_1$, $T_2$, $G$, $H$) untuk menentukan $\Gamma_\text{vib}$, lalu hitung banyak pita IR dan Raman.

**Penyelesaian.** (a) Hanya dua kelas yang karakternya tidak nol: $\chi(E) = 3 \times 60 = 180$ dan $\chi(\sigma) = 4 \times 1 = 4$ untuk 15 bidang. Dengan $h = 120$: $n_i = \tfrac1{120}[180d_i + 15 \cdot 4\,\chi_i(\sigma)] = \tfrac12(3d_i + \chi_i(\sigma))$.

\(b) Misalnya $T_{1u}$: $d = 3$, $\chi(\sigma) = -(-1) = 1$, sehingga $n = \tfrac12(9 + 1) = 5$; $A_g$: $n = \tfrac12(3 + 1) = 2$; $H_g$: $n = \tfrac12(15 + 1) = 8$. Semua irrep:

$$
\Gamma_{3N} = 2A_g + A_u + 4T_{1g} + 5T_{1u} + 4T_{2g} + 5T_{2u} + 6G_g + 6G_u + 8H_g + 7H_u .
$$

Kurangkan translasi $T_{1u}$ dan rotasi $T_{1g}$:

$$
\Gamma_\text{vib} = 2A_g + A_u + 3T_{1g} + 4T_{1u} + 4T_{2g} + 5T_{2u} + 6G_g + 6G_u + 8H_g + 7H_u .
$$

Periksa: $2 + 1 + 9 + 12 + 12 + 15 + 24 + 24 + 40 + 35 = 174$. Banyak frekuensi berbeda: $2 + 1 + 3 + 4 + 4 + 5 + 6 + 6 + 8 + 7 = 46$. Aktif IR: $T_{1u}$ (memuat $x$, $y$, $z$), jadi 4 pita. Aktif Raman: $A_g$ dan $H_g$ (fungsi kuadrat dalam $I_h$): $2 + 8 = 10$. Sisanya, 32 frekuensi, bisu.

**Memahami hasil.** Inilah jawaban teka-teki pembuka bab: empat pita IR yang diamati Krätschmer dan Huffman (527, 577, 1183, 1429 cm⁻¹) cocok tepat dengan $4T_{1u}$, dan spektrum Raman memperlihatkan sepuluh pita, dua di antaranya terpolarisasi ($A_g$, termasuk mode "napas" di 496 cm⁻¹ dan mode "jepit segi lima" di 1469 cm⁻¹). Molekul dengan simetri lebih rendah akan memperlihatkan jauh lebih banyak pita. Kesesuaian ini menjadi salah satu bukti terkuat bahwa C₆₀ benar-benar berbentuk bola sepak, dan diperoleh tanpa satu pun tetapan gaya.
:::

::: {.terapan}
**Kaitan kimia · Mengapa N₂ dan O₂ bukan gas rumah kaca**

Molekul diatom homonuklir mempunyai satu getaran, bersimetri $\Sigma_g^+$ dalam $D_{\infty h}$. Mode itu tidak bertransformasi seperti $x$, $y$, atau $z$, sehingga tidak aktif IR; ia hanya aktif Raman. Karena itu 99% atmosfer (N₂, O₂, Ar) transparan terhadap radiasi inframerah termal Bumi. Efek rumah kaca seluruhnya berasal dari komponen kecil yang mempunyai mode aktif IR di daerah 5–50 µm: H₂O, CO₂, CH₄, N₂O, O₃, dan gas buatan seperti SF₆ dan freon. Satu baris tabel karakter menjelaskan mengapa sekitar 0,04% CO₂ lebih penting bagi iklim daripada 78% nitrogen.
:::

### Pita nada atas dan kombinasi

Aturan (10.18) dan (10.19) berlaku untuk transisi fundamental. Pita **nada atas** ($v_k = 0 \to 2$) dan **kombinasi** ($v_k = 0 \to 1$ dan $v_l = 0 \to 1$ sekaligus) jauh lebih lemah, karena dalam pendekatan harmonik keduanya terlarang, tetapi menjadi lemah teramati karena anharmonisitas (subbab 5.9). Simetri keadaan akhir pita kombinasi adalah $\Gamma_k \times \Gamma_l$; pita itu aktif IR bila hasil kali langsung itu memuat irrep $x$, $y$, atau $z$. Untuk nada atas pertama mode tak berdegenerasi, simetrinya $\Gamma_k \times \Gamma_k = A_1$, sehingga selalu aktif Raman tetapi aktif IR hanya bila $A_1$ memuat $z$. Dengan cara ini, mode bisu seperti $\nu_6$ SF₆ dapat diketahui frekuensinya dari pita kombinasi $\nu_6 + \nu_k$ yang aktif IR.

::: {.kuis}
**Kuis cepat 10.9**

\(a) Berapa mode getaran yang dimiliki etilena (C₂H₄, $D_{2h}$), dan berapa yang aktif IR jika $\Gamma_\text{vib} = 3A_g + B_{2g} + 2B_{3g} + A_u + 2B_{1u} + 2B_{2u} + B_{3u}$ (dengan sumbu $z$ sepanjang C=C dan $x$ tegak lurus bidang molekul)? (b) Mengapa pita ulur C–H simetris metana tidak tampak di IR? (c) Bila sebuah molekul AX₃ memperlihatkan empat pita IR dan empat pita Raman yang frekuensinya sama, apa bentuknya?
:::
