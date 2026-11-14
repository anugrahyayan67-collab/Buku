## 6.9 Rotor tegar diatom

### Model

Dalam molekul diatom, gerak relatif (6.25) terdiri atas getaran (perubahan $r$) dan rotasi (perubahan $\theta$, $\phi$). Bila panjang ikatan dianggap tetap pada $r_e$, molekul adalah **rotor tegar**: partikel bermassa $\mu$ pada bola berjari-jari $r_e$, dengan momen inersia $I = \mu r_e^2$. Hasil subbab 6.4 langsung berlaku, dengan bilangan kuantum rotasi yang secara tradisional ditulis $J$ (dan $M$ untuk komponen $z$):

$$
E_J = \frac{\hbar^2}{2I}J(J + 1), \qquad \psi_{JM} = Y_J^M(\theta, \phi), \qquad J = 0, 1, 2, \ldots, \quad M = -J, \ldots, J . \qquad \text{(6.27)}
$$

Dalam spektroskopi, energi rotasi ditulis sebagai **suku rotasi** dalam cm⁻¹:

$$
F(J) = \frac{E_J}{hc} = BJ(J + 1), \qquad B = \frac{h}{8\pi^2cI} = \frac{\hbar}{4\pi cI} . \qquad \text{(6.28)}
$$

$B$ adalah **tetapan rotasi**. Bila $I$ dalam kg m² dan $c$ dalam cm/s, $B$ dalam cm⁻¹; dalam spektroskopi gelombang mikro, $B$ sering dinyatakan dalam frekuensi ($Bc$, dalam MHz atau GHz). Tingkat-tingkatnya 0, $2B$, $6B$, $12B$, $20B$, ..., masing-masing berdegenerasi $2J + 1$ (Gambar 6.4).

### Skala energi rotasi

| Molekul | $r_e$ (pm) | $B$ (cm⁻¹) | $\theta_\text{rot} = hcB/k$ (K) |
|---|---|---|---|
| H₂ | 74,14 | 60,85 | 87,6 |
| HF | 91,68 | 20,96 | 30,2 |
| HCl | 127,46 | 10,59 | 15,2 |
| N₂ | 109,77 | 2,00 | 2,88 |
| CO | 112,83 | 1,931 | 2,78 |
| O₂ | 120,75 | 1,446 | 2,08 |
| NaCl | 236,08 | 0,218 | 0,31 |
| I₂ | 266,6 | 0,0374 | 0,054 |

Untuk semua molekul kecuali H₂, $\theta_\text{rot}$ jauh di bawah suhu kamar: banyak tingkat rotasi terisi dan rotasi hampir "klasik" secara termodinamika (berbeda dengan getaran, subbab 5.4). Urutan skala energi dalam molekul adalah elektronik (puluhan ribu cm⁻¹) ≫ getaran (ribuan) ≫ rotasi (puluhan sampai sepersepuluh cm⁻¹). Pemisahan skala inilah yang membenarkan perlakuan terpisah ketiga gerak.

::: {.contoh}
**Contoh 6.30 · Tetapan rotasi HCl**

Dari $r_e = 127{,}46$ pm dan $\mu = 0{,}97959$ u, hitung $I$, $B$ (dalam cm⁻¹ dan GHz), dan empat tingkat rotasi terendah.

**Penyelesaian.** $I = (0{,}97959)(1{,}66054 \times 10^{-27})(1{,}2746 \times 10^{-10})^2 = 2{,}643 \times 10^{-47}$ kg m². $B = h/(8\pi^2cI) = 6{,}626 \times 10^{-34}/[8\pi^2(2{,}998 \times 10^{10})(2{,}643 \times 10^{-47})] = 10{,}593$ cm⁻¹ $= 317{,}6$ GHz. Tingkat: $F(0) = 0$, $F(1) = 21{,}19$, $F(2) = 63{,}56$, $F(3) = 127{,}12$ cm⁻¹.

**Memahami hasil.** Selisih tingkat terendah, 21 cm⁻¹, berada di daerah inframerah jauh (sekitar 0,5 mm), sepuluh kali lebih kecil daripada $kT$ pada suhu kamar. Untuk molekul yang lebih berat (CO, $B = 1{,}93$ cm⁻¹), transisi rotasi jatuh di daerah gelombang mikro (beberapa milimeter).
:::

::: {.contoh}
**Contoh 6.31 · Efek isotop pada rotasi**

Ramalkan $B$ untuk DCl dan H³⁷Cl dari $B(\text{H}^{35}\text{Cl}) = 10{,}593$ cm⁻¹. Bandingkan efek isotop pada rotasi dan getaran.

**Penyelesaian.** Panjang ikatan sama (aproksimasi Born–Oppenheimer), sehingga $B \propto 1/\mu$. $\mu(\text{DCl}) = 1{,}9044$ u; $\mu(\text{H}^{37}\text{Cl}) = 0{,}98105$ u. $B(\text{DCl}) = 10{,}593 \times 0{,}97959/1{,}9044 = 5{,}449$ cm⁻¹; $B(\text{H}^{37}\text{Cl}) = 10{,}577$ cm⁻¹.

**Memahami hasil.** Rotasi berskala $1/\mu$, getaran berskala $1/\sqrt\mu$ (subbab 5.10). Penggantian H dengan D menurunkan $B$ hampir dua kali, tetapi frekuensi getaran hanya $\sqrt2$ kali. Dengan mengukur $B$ untuk beberapa isotopolog, panjang ikatan dalam molekul poliatom dapat ditentukan satu per satu (metode substitusi Kraitchman).
:::

::: {.contoh}
**Contoh 6.32 · Frekuensi transisi dan frekuensi putaran klasik**

Untuk CO ($B = 1{,}9225$ cm⁻¹), bandingkan frekuensi transisi $J = 7 \to 8$ dengan frekuensi putaran klasik molekul yang momentum sudutnya $\sqrt{J(J+1)}\hbar$ untuk $J = 7$ dan $J = 8$.

**Penyelesaian.** Frekuensi transisi $\nu = [F(8) - F(7)]c = 16Bc = 922{,}2$ GHz. Frekuensi putaran klasik $f = \omega/2\pi = L/(2\pi I) = \sqrt{J(J+1)}\,\hbar/(2\pi I) = 2Bc\sqrt{J(J+1)}$, karena $\hbar/(2\pi I) = h/(4\pi^2I) = 2Bc$: $J = 7$: 862,6 GHz; $J = 8$: 978,1 GHz.

**Memahami hasil.** Frekuensi foton yang diserap atau dipancarkan terletak di antara frekuensi putaran klasik kedua keadaan, seperti dalam model Bohr untuk atom (subbab 1.6). Untuk $J$ besar, perbedaan keduanya mengecil: molekul yang berputar cepat memancarkan pada frekuensi putarannya sendiri, sesuai elektrodinamika klasik. Inilah asas korespondensi untuk rotasi.
:::

### Molekul poliatom (sekilas)

Molekul poliatom mempunyai tiga momen inersia utama $I_a \le I_b \le I_c$ terhadap tiga sumbu yang saling tegak lurus. Molekul linear (CO₂, HCN, OCS) mempunyai satu momen inersia dan tingkat energi seperti diatom. **Rotor simetris** mempunyai dua momen inersia yang sama: lonjong (*prolate*, misalnya CH₃F, $I_a < I_b = I_c$) atau pipih (*oblate*, misalnya NH₃ dan C₆H₆, $I_a = I_b < I_c$). Energinya bergantung pada $J$ dan bilangan kuantum $K$, proyeksi momentum sudut pada sumbu simetri molekul:

$$
F(J, K) = BJ(J + 1) + (A - B)K^2, \qquad K = -J, \ldots, J ,
$$

dengan $A$ dan $B$ tetapan rotasi untuk sumbu simetri dan sumbu tegak lurusnya. Aturan seleksinya $\Delta J = \pm1$, $\Delta K = 0$, sehingga garis-garis gelombang mikro tetap di $2B(J + 1)$, hanya sedikit terpecah menurut $K$ oleh distorsi sentrifugal. Rotor bola (CH₄, SF₆) tidak berdipol. Rotor asimetris (H₂O, sebagian besar molekul organik) tidak mempunyai rumus tertutup; tingkatnya diperoleh dengan mendiagonalkan matriks Hamiltonian rotasi dalam basis rotor simetris.

::: {.contoh}
**Contoh 6.33 · Rotor simetris CH₃F**

Garis $J = 1 \leftarrow 0$ CH₃F terukur di 51,072 GHz. Tentukan $B$ (dalam MHz dan cm⁻¹) dan momen inersia tegak lurus sumbu C–F. Berapa garis $J = 2 \leftarrow 1$?

**Penyelesaian.** $2B = 51\,072$ MHz, jadi $B = 25\,536$ MHz $= 0{,}8518$ cm⁻¹. $I_b = h/(8\pi^2B) = 6{,}626 \times 10^{-34}/[8\pi^2(2{,}5536 \times 10^{10}\ \text{s}^{-1})] = 3{,}29 \times 10^{-46}$ kg m². Garis $J = 2 \leftarrow 1$ di $4B = 102{,}14$ GHz.

**Memahami hasil.** Satu garis memberi satu momen inersia, tetapi CH₃F mempunyai tiga parameter geometri (C–H, C–F, sudut HCH). Diperlukan isotopolog tambahan (¹³CH₃F, CD₃F), seperti soal OCS di akhir bab. Tetapan $A$ tidak muncul di spektrum gelombang mikro karena $\Delta K = 0$; ia diperoleh dari spektrum rotasi–getaran.
:::

::: {.contoh}
**Contoh 6.34 · Berapa tingkat rotasi di bawah anak tangga getaran?**

Untuk H₂ ($B = 60{,}85$ cm⁻¹, pita dasar 4161 cm⁻¹), berapa tingkat rotasi pada $v = 0$ yang berenergi lebih rendah daripada $v = 1$, $J = 0$? Bandingkan dengan CO ($B = 1{,}93$, pita dasar 2143 cm⁻¹).

**Penyelesaian.** H₂: $J(J+1)(60{,}85) < 4161$ memberi $J(J+1) < 68{,}4$, jadi $J \le 7$ ($F(7) = 3408$, $F(8) = 4381$ cm⁻¹). CO: $J(J+1) < 1110$, jadi $J \le 32$.

**Memahami hasil.** Untuk H₂, skala rotasi dan getaran hanya berbeda 70 kali, sehingga kopling rotasi–getaran besar dan $B$ berubah cukup banyak dengan $v$. Untuk molekul berat, ratusan tingkat rotasi muat dalam satu anak tangga getaran, dan pemisahan rotasi–getaran sangat baik.
:::

::: {.kuis}
**Kuis cepat 6.9**

Berapa degenerasi tingkat $J = 4$? Berapa energinya dalam satuan $B$? Jika panjang ikatan dilipatduakan, bagaimana $B$ berubah?
:::

## 6.10 Spektrum rotasi gelombang mikro

### Aturan seleksi

Transisi rotasi dipicu oleh medan listrik gelombang elektromagnetik yang memberi torsi pada dipol molekul. Bila momen dipol permanen $\mu_0$ terletak sepanjang sumbu molekul, komponen $z$-nya dalam kerangka laboratorium adalah $\mu_0\cos\theta$. Momen dipol transisi antara keadaan rotasi (cahaya terpolarisasi $z$):

$$
\langle J'M'|\hat\mu_z|JM\rangle = \mu_0\int Y_{J'}^{M'*}\cos\theta\,Y_J^M\,\sin\theta\,d\theta\,d\phi . \qquad \text{(6.29)}
$$

Ada dua syarat agar integral ini tidak nol:

* **Aturan seleksi kasar:** $\mu_0 \ne 0$. Hanya molekul dengan **momen dipol permanen** yang mempunyai spektrum rotasi murni. N₂, O₂, H₂, Cl₂, CO₂, CH₄, dan SF₆ tidak; HCl, CO, H₂O, NH₃, dan OCS punya.
* **Aturan seleksi spesifik:** $\Delta J = \pm1$, $\Delta M = 0$ (atau $\pm1$ untuk polarisasi $x$, $y$). Ini mengikuti dari rumus rekursi harmonik bola: $\cos\theta\,Y_J^M$ adalah kombinasi $Y_{J+1}^M$ dan $Y_{J-1}^M$ saja, sehingga ortogonalitas (6.16) menghapus semua suku lain. Secara fisis: foton membawa momentum sudut $\hbar$, dan kekekalan momentum sudut mengizinkan $J$ berubah satu.

### Spektrum: garis berjarak sama

Untuk serapan $J \to J + 1$:

$$
\tilde\nu = F(J + 1) - F(J) = 2B(J + 1), \qquad J = 0, 1, 2, \ldots \qquad \text{(6.30)}
$$

Garis-garisnya terletak di $2B$, $4B$, $6B$, ..., berjarak sama $2B$ (Gambar 6.4). Jarak antargaris memberi $B$, lalu $I$, lalu panjang ikatan. Dengan spektrometer gelombang mikro, frekuensi garis dapat diukur sampai ketelitian 1 bagian dalam $10^7$ atau lebih baik, sehingga panjang ikatan diperoleh sampai seperseribu pikometer (dengan catatan subbab 6.12 tentang getaran titik nol).

![Gambar 6.4 Kiri: tingkat energi rotor tegar dan transisi serapan $\Delta J = +1$. Kanan: spektrum serapan rotasi CO pada 298 K yang dihitung; garis berjarak sama $2B = 3{,}85$ cm⁻¹. Intensitas mula-mula naik (populasi dan faktor $\tilde\nu$ naik) lalu turun (populasi tingkat tinggi menurun).](fig/c_rotor.png){width=95%}

::: {.contoh}
**Contoh 6.35 · Panjang ikatan CO dari satu frekuensi**

Garis rotasi $J = 1 \leftarrow 0$ ¹²C¹⁶O berada di 115,271 202 GHz. Hitung $B_0$, $I$, dan panjang ikatan $r_0$.

**Penyelesaian.** $\nu = 2Bc$, jadi $Bc = 57\,635{,}6$ MHz dan $B_0 = 57\,635{,}6 \times 10^6/2{,}997\,92 \times 10^{10} = 1{,}922\,52$ cm⁻¹. $I = h/(8\pi^2cB_0) = 1{,}4560 \times 10^{-46}$ kg m². Dengan $\mu = 6{,}8562$ u $= 1{,}138\,51 \times 10^{-26}$ kg: $r_0 = \sqrt{I/\mu} = 113{,}09$ pm.

**Memahami hasil.** Panjang ikatan kesetimbangan CO adalah $r_e = 112{,}83$ pm; nilai $r_0$ sedikit lebih besar karena $B_0$ adalah rata-rata $\langle 1/r^2\rangle$ dalam keadaan dasar getaran, dan getaran titik nol yang anharmonik memanjangkan ikatan rata-rata (subbab 6.12). Inilah garis yang dipakai astronom untuk memetakan awan molekul di galaksi kita dan galaksi lain.
:::

::: {.contoh}
**Contoh 6.36 · Garis isotopolog CO**

Ramalkan frekuensi $J = 1 \leftarrow 0$ untuk ¹³C¹⁶O dan ¹²C¹⁸O dari garis ¹²C¹⁶O (115,2712 GHz). Nilai terukurnya 110,2014 dan 109,7822 GHz.

**Penyelesaian.** $\nu \propto 1/\mu$. $\mu(^{13}\text{C}^{16}\text{O}) = 7{,}1724$ u; $\mu(^{12}\text{C}^{18}\text{O}) = 7{,}1998$ u. $\nu = 115{,}2712 \times 6{,}8562/7{,}1724 = 110{,}189$ GHz dan $115{,}2712 \times 6{,}8562/7{,}1998 = 109{,}769$ GHz.

**Memahami hasil.** Ramalan meleset 0,01%, karena $B_0$ bukan hanya $1/\mu r_e^2$ tetapi juga bergantung pada getaran titik nol, yang berbeda untuk tiap isotopolog. Selisih kecil semacam ini yang dipakai untuk menentukan $r_e$ dari $r_0$ beberapa isotopolog. Dalam astronomi, garis ¹³CO dan C¹⁸O yang lebih lemah dipakai untuk mengukur kolom gas yang terlalu tebal bagi ¹²CO, dan perbandingan isotopnya memberi petunjuk sejarah nukleosintesis bintang.
:::

::: {.contoh}
**Contoh 6.37 · Spektrum rotasi HCl di inframerah jauh**

Dengan $B_0 = 10{,}440$ cm⁻¹, hitung empat garis serapan rotasi pertama HCl dan panjang gelombang garis pertama.

**Penyelesaian.** $\tilde\nu = 2B_0(J + 1)$: 20,88; 41,76; 62,64; 83,52 cm⁻¹. Garis pertama di $\lambda = 1/20{,}88$ cm $= 479$ µm.

**Memahami hasil.** Spektrum rotasi hidrida jatuh di inframerah jauh (terahertz), bukan gelombang mikro. Garis-garis HCl yang lebar jaraknya ini adalah salah satu spektrum pertama yang diukur (Czerny, 1925) dan langsung memberi panjang ikatan HCl. Molekul H₂O di atmosfer mempunyai banyak garis rotasi di daerah ini, sehingga astronomi terahertz harus dilakukan dari tempat yang sangat kering dan tinggi, atau dari luar angkasa.
:::

::: {.contoh}
**Contoh 6.38 · Siapa yang mempunyai spektrum rotasi murni?**

Manakah yang menunjukkan spektrum rotasi gelombang mikro: N₂, HCl, CO₂, OCS, CH₄, CH₃Cl, H₂O, C₆H₆?

**Penyelesaian.** Yang mempunyai momen dipol permanen: HCl, OCS (linear tetapi tidak simetris), CH₃Cl, H₂O. Tidak: N₂ dan CO₂ (simetris, dipol nol), CH₄ (tetrahedral), C₆H₆ (heksagonal).

**Memahami hasil.** Molekul tanpa dipol dapat diamati rotasinya dengan spektroskopi **Raman rotasi** ($\Delta J = 0, \pm2$, karena polarisabilitas anisotrop berubah dua kali dalam satu putaran) atau dari struktur rotasi pita getaran yang aktif IR (subbab 6.12). OCS, dengan garis $J = 1 \leftarrow 0$ di 12,163 GHz, adalah molekul uji klasik spektrometer gelombang mikro.
:::

::: {.awas}
**Oven gelombang mikro tidak "menala" rotasi air**

Oven gelombang mikro bekerja pada 2,45 GHz (12,2 cm). Ini bukan frekuensi transisi rotasi molekul air; garis rotasi uap air yang terendah dan terkenal ada di 22,235 GHz, dan dalam cairan, ikatan hidrogen menghalangi rotasi bebas sehingga tidak ada garis tajam sama sekali. Air cair menyerap gelombang mikro secara lebar karena dipol-dipolnya berusaha mengikuti medan yang berubah arah dan "bergesekan" dengan tetangganya (relaksasi dielektrik). Frekuensi 2,45 GHz dipilih karena alasan regulasi dan karena serapannya tidak terlalu kuat, sehingga gelombang dapat menembus beberapa sentimeter ke dalam makanan.
:::

::: {.terapan}
**Molekul di ruang antarbintang**

Hampir semua molekul antarbintang ditemukan melalui garis rotasinya. Awan molekul bersuhu 10–100 K, sehingga hanya tingkat rotasi rendah yang terisi, dan transisinya jatuh di daerah gelombang milimeter dan submilimeter, tempat atmosfer Bumi cukup transparan. Teleskop radio seperti ALMA di gurun Atacama mencatat ribuan garis dan mencocokkannya dengan frekuensi laboratorium yang terukur sampai beberapa kHz. H₂, komponen utama awan, tidak mempunyai dipol dan tidak teramati langsung; CO dipakai sebagai pelacaknya. Daftarnya mencakup HCN, rantai sianopoliuna sampai HC₉N, metanol, etanol, dan asetonitril; molekul sebesar fulerena C₆₀ juga ditemukan, tetapi melalui pita getarannya di inframerah.
:::

::: {.contoh}
**Contoh 6.39 · Spektrum Raman rotasi N₂**

N₂ tidak berdipol, tetapi polarisabilitasnya anisotrop, sehingga aktif Raman rotasi dengan $\Delta J = \pm2$. Hitung pergeseran garis Stokes $J + 2 \leftarrow J$ untuk $J = 0$ sampai 3 ($B = 1{,}99$ cm⁻¹).

**Penyelesaian.** $\Delta F = B[(J+2)(J+3) - J(J+1)] = B(4J + 6)$: 11,94; 19,90; 27,86; 35,82 cm⁻¹.

**Memahami hasil.** Garis pertama di $6B$ dan selanjutnya berjarak $4B$, dua kali jarak garis gelombang mikro. Polarisabilitas kembali ke nilai semula setelah setengah putaran, sehingga foton hamburan melihat "frekuensi ganda" rotasi; inilah asal $\Delta J = \pm2$. Pada ¹⁴N₂, intensitas garis bergantian 2 : 1 karena statistik spin inti (soal subbab 6.11).
:::

::: {.kuis}
**Kuis cepat 6.10**

Mengapa spektrum rotasi murni H₂ tidak teramati dengan serapan gelombang mikro? Jika jarak antargaris suatu molekul 3,0 cm⁻¹, berapa $B$-nya?
:::
