## 14.7 Teori medan ligan: OM kompleks oktahedral

### Mengapa model ionik tidak cukup

Teori medan kristal menjelaskan pola pemecahan dan banyak sifat termodinamika, tetapi beberapa fakta tidak dapat ia tampung:

1. **Deret spektrokimia** tidak mengikuti muatan ligan (subbab 14.2).
2. **Efek nefelauksetik**: parameter tolakan antarelektron d dalam kompleks selalu lebih kecil daripada dalam ion bebas, seolah-olah awan elektron d "mengembang" (Yunani *nephele* = awan, *kelos* = pengembang). Model ionik tidak mempunyai mekanisme untuk itu.
3. **Bukti langsung kovalensi.** Spektrum resonansi spin elektron [IrCl₆]²⁻ memperlihatkan pemecahan hiperhalus oleh inti ³⁵Cl dan ³⁷Cl: elektron tak berpasangan, yang menurut TMK murni berada di orbital $t_{2g}$ iridium, ternyata menghabiskan sekitar 5% waktunya pada setiap atom klorin.
4. **Pita transfer muatan** yang intens (subbab 14.12) menuntut orbital ligan dan logam sebagai bagian dari satu sistem elektronik.

Semua ini mengarah ke satu kesimpulan: orbital d logam bercampur dengan orbital ligan, dan pemecahan $\Delta_o$ sebagian besar merupakan selisih energi antara orbital molekul yang tak berikatan dan yang antiikatan. Teori yang memperlakukan kompleks dengan metode orbital molekul (Bab 11 dan 13), sambil tetap memakai bahasa dan parameter TMK, disebut **teori medan ligan** (TML).

### Orbital basis dan kesetangkupannya

Untuk kompleks oktahedral ML₆ logam periode 4 dengan ligan donor σ saja (misalnya NH₃), basis valensinya adalah sembilan orbital logam (lima 3d, satu 4s, tiga 4p) dan enam orbital σ ligan, yaitu pasangan elektron bebas yang menunjuk ke logam. Beri nomor ligan: 1 di $+x$, 2 di $+y$, 3 di $-x$, 4 di $-y$, 5 di $+z$, 6 di $-z$, dan sebut orbital σ-nya $\sigma_1, \ldots, \sigma_6$.

Kesetangkupan orbital logam dibaca langsung dari tabel karakter $O_h$: 4s bertransformasi sebagai $a_{1g}$, ketiga orbital 4p sebagai $t_{1u}$, dan orbital 3d sebagai $e_g + t_{2g}$. Untuk keenam orbital σ, karakter representasi tereduksinya adalah banyaknya orbital yang tidak berpindah tempat di bawah setiap operasi (subbab 10.7). Dalam urutan kelas $E$, $8C_3$, $6C_2'$, $6C_4$, $3C_2$, $i$, $6S_4$, $8S_6$, $3\sigma_h$, $6\sigma_d$, diperoleh

$$
\Gamma_\sigma:\ 6,\ 0,\ 0,\ 2,\ 2,\ 0,\ 0,\ 0,\ 4,\ 2 \quad\Longrightarrow\quad \Gamma_\sigma = A_{1g} + E_g + T_{1u} . \qquad \text{(14.el1)}
$$

Tidak ada komponen $T_{2g}$. Inilah hasil terpenting teori medan ligan: **orbital $t_{2g}$ logam tidak mempunyai pasangan σ pada ligan**, sehingga dalam kompleks donor σ murni ketiganya tetap orbital d murni yang tak berikatan.

::: {.contoh}
**Contoh 14.l1 · SALC σ oktahedral**

(a) Periksa reduksi (14.el1) untuk $A_{1g}$ dan $T_{1u}$. (b) Tuliskan kombinasi linear teradaptasi simetri (SALC) yang cocok dengan 4s, $4p_x$, $3d_{z^2}$, dan $3d_{x^2-y^2}$, lalu periksa normalisasinya dengan mengabaikan tumpang tindih antarligan.

**Penyelesaian.** (a) Rumus reduksi dengan $h = 48$. $A_{1g}$ (semua karakter 1): $\tfrac{1}{48}[6 + 6 \cdot 2 + 3 \cdot 2 + 3 \cdot 4 + 6 \cdot 2] = \tfrac{48}{48} = 1$. $T_{1u}$ (karakter 3, 0, −1, 1, −1, −3, −1, 0, 1, 1): $\tfrac{1}{48}[18 + 6(2)(1) + 3(2)(-1) + 3(4)(1) + 6(2)(1)] = \tfrac{1}{48}[18 + 12 - 6 + 12 + 12] = 1$.

(b) SALC dibangun agar tandanya mengikuti tanda orbital logam di arah setiap ligan:

$$
\begin{aligned}
a_{1g}:&\ \tfrac{1}{\sqrt6}(\sigma_1 + \sigma_2 + \sigma_3 + \sigma_4 + \sigma_5 + \sigma_6), \qquad t_{1u}(x):\ \tfrac{1}{\sqrt2}(\sigma_1 - \sigma_3),\\
e_g(z^2):&\ \tfrac{1}{\sqrt{12}}(2\sigma_5 + 2\sigma_6 - \sigma_1 - \sigma_2 - \sigma_3 - \sigma_4), \qquad e_g(x^2 - y^2):\ \tfrac12(\sigma_1 - \sigma_2 + \sigma_3 - \sigma_4) .
\end{aligned}
$$

Normalisasinya: $\tfrac16 \cdot 6 = 1$; $\tfrac12 \cdot 2 = 1$; $\tfrac{1}{12}(4 + 4 + 1 + 1 + 1 + 1) = 1$; $\tfrac14 \cdot 4 = 1$.

**Memahami hasil.** Pola koefisien SALC $e_g(z^2)$, yaitu $2, 2, -1, -1, -1, -1$, meniru nilai fungsi $d_{z^2}$ di keenam arah (Contoh 14.a1): positif dua kali lipat di sumbu $z$, negatif setengahnya di ekuator. Pola $e_g(x^2 - y^2)$ meniru $d_{x^2-y^2}$: positif di $\pm x$, negatif di $\pm y$. Begitulah SALC "memotret" orbital logam pada ligan, dan begitulah teori grup memastikan bahwa setiap SALC hanya berinteraksi dengan orbital logam yang sejenis.
:::

### Tumpang tindih grup

Interaksi antara orbital logam dan SALC sebanding dengan tumpang tindihnya, yang disebut **tumpang tindih grup** $G$. Misalkan $S_\sigma$ tumpang tindih $d_{z^2}$ dengan satu orbital σ ligan di sumbu $z$. Untuk ligan di ekuator, fungsi sudut $d_{z^2}$ bernilai $-\tfrac12$ kali nilainya di sumbu, sehingga tumpang tindihnya $-\tfrac12S_\sigma$. Maka

$$
G(e_g) = \langle d_{z^2}|e_g(z^2)\rangle = \tfrac{1}{\sqrt{12}}\left[2S_\sigma + 2S_\sigma - 4\left(-\tfrac12S_\sigma\right)\right] = \tfrac{6}{\sqrt{12}}S_\sigma = \sqrt3\,S_\sigma . \qquad \text{(14.el2)}
$$

Hasil yang sama diperoleh untuk $d_{x^2-y^2}$: nilai sudutnya di keempat ligan ekuator $\pm\tfrac{\sqrt3}{2}$ kali nilai $d_{z^2}$ di sumbunya, sehingga $G = \tfrac12 \cdot 4 \cdot \tfrac{\sqrt3}{2}S_\sigma = \sqrt3\,S_\sigma$. Dengan cara yang sama, $G(a_{1g}) = \sqrt6\,S_s$ dan $G(t_{1u}) = \sqrt2\,S_p$, dengan $S_s$ dan $S_p$ tumpang tindih 4s dan 4p dengan satu orbital ligan. Untuk $t_{2g}$, $G = 0$.

### Persamaan sekuler per simetri

Karena orbital dengan kesetangkupan berbeda tidak bercampur, matriks Hamiltonian 15 × 15 terpecah menjadi blok-blok kecil. Untuk $e_g$, setiap komponen memberi masalah dua tingkat: orbital logam dengan energi $\alpha_M$ dan SALC dengan energi $\alpha_L$ (lebih rendah, karena pasangan elektron bebas ligan lebih stabil daripada orbital d logam), dengan unsur matriks $\beta_{e_g}$. Dengan mengabaikan tumpang tindih dalam penyebut, persamaan sekulernya (subbab 11.4)

$$
\begin{vmatrix}\alpha_M - E & \beta_{e_g}\\ \beta_{e_g} & \alpha_L - E\end{vmatrix} = 0
\quad\Longrightarrow\quad
E_\pm = \frac{\alpha_M + \alpha_L}{2} \pm \sqrt{\left(\frac{\alpha_M - \alpha_L}{2}\right)^2 + \beta_{e_g}^2} . \qquad \text{(14.el3)}
$$

Akar bawah adalah orbital ikatan $e_g$ (sebagian besar ligan), akar atas orbital antiikatan $e_g^*$ (sebagian besar logam). Bila $|\beta| \ll \alpha_M - \alpha_L$, uraian akar memberi

$$
E(e_g^*) \approx \alpha_M + \frac{\beta_{e_g}^2}{\alpha_M - \alpha_L} . \qquad \text{(14.el4)}
$$

Orbital $t_{2g}$ tetap di $\alpha_M$. Dengan demikian

$$
\Delta_o = E(e_g^*) - E(t_{2g}) \approx \frac{\beta_{e_g}^2}{\alpha_M - \alpha_L} = 3\,\frac{\beta_\sigma^2}{\alpha_M - \alpha_L} \equiv 3e_\sigma , \qquad \text{(14.el5)}
$$

dengan $\beta_{e_g} = \sqrt3\,\beta_\sigma$, karena unsur matriks Hamiltonian kira-kira sebanding dengan tumpang tindih (hampiran Wolfsberg–Helmholz). Faktor 3 adalah kuadrat faktor tumpang tindih grup $\sqrt3$. Inilah dasar model tumpang tindih sudut (14.ea14): parameter $e_\sigma$ adalah destabilisasi orbital d oleh satu ligan, dan sudut masuk melalui kuadrat tumpang tindih.

Dalam tafsir orbital molekul, $\Delta_o$ **bukan** hasil tolakan elektrostatik, melainkan ukuran sifat antiikatan $e_g^*$. Ligan yang merupakan donor σ lebih kuat (energi $\alpha_L$ lebih tinggi, lebih dekat ke $\alpha_M$; atau tumpang tindih lebih besar) memberi $\Delta_o$ lebih besar. Logam 4d dan 5d dengan orbital lebih luas memberi tumpang tindih lebih besar dan $\Delta_o$ lebih besar. Muatan logam yang lebih tinggi memendekkan ikatan dan menaikkan tumpang tindih. Semua kecenderungan subbab 14.2 muncul kembali, kini dengan penjelasan yang benar.

![Gambar 14.g5 Diagram orbital molekul kompleks oktahedral ML₆ dengan ligan donor σ saja, dihitung dari model Contoh 14.l3. Orbital ikatan $a_{1g}$, $t_{1u}$, dan $e_g$ (sebagian besar ligan) menampung 12 elektron ligan. Orbital $t_{2g}$ tak berikatan dan $e_g^*$ antiikatan menampung elektron d; selisih keduanya adalah $\Delta_o$.](fig/c_om.png){width=88%}

### Diagram orbital molekul dan pengisian elektron

Gambar 14.g5 memperlihatkan diagram lengkapnya. Dari bawah ke atas: enam orbital ikatan ($a_{1g}$, $t_{1u}$, $e_g$), yang sebagian besar berkarakter ligan; tiga orbital $t_{2g}$ tak berikatan, murni d; dua orbital $e_g^*$ antiikatan, sebagian besar d; lalu $a_{1g}^*$ dan $t_{1u}^*$ yang jauh di atas, sebagian besar 4s dan 4p.

Keenam ligan menyumbang 12 elektron yang mengisi enam orbital ikatan. Elektron d logam masuk ke $t_{2g}$ dan $e_g^*$: **persis** seperti dalam teori medan kristal. Itu sebabnya semua penghitungan ESMK, keadaan spin, dan momen magnet di subbab 14.4–14.6 tetap berlaku; yang berubah hanyalah pemahaman bahwa elektron $e_g^*$ menempati orbital antiikatan. Mengisi $e_g^*$ **melemahkan** ikatan logam–ligan. Inilah alasan mendalam mengapa ion spin tinggi lebih besar, mengapa kompleks d⁸ dan d⁹ melemahkan atau memanjangkan sebagian ikatannya, dan mengapa kompleks dengan $e_g^*$ kosong (Cr³⁺, Co³⁺ spin rendah) begitu stabil.

::: {.contoh}
**Contoh 14.l2 · Menghitung elektron dalam diagram OM**

Untuk [Co(NH₃)₆]³⁺, [Cr(H₂O)₆]³⁺, [Ni(H₂O)₆]²⁺, dan [Cu(NH₃)₄(H₂O)₂]²⁺, hitung banyaknya elektron valensi total dalam diagram OM dan banyaknya elektron di orbital antiikatan $e_g^*$.

**Penyelesaian.** Elektron ligan selalu 12 (enam pasangan σ). Elektron d: Co³⁺ 6, Cr³⁺ 3, Ni²⁺ 8, Cu²⁺ 9. Totalnya 18, 15, 20, dan 21. Elektron di $e_g^*$: [Co(NH₃)₆]³⁺ spin rendah $t_{2g}^6$: 0; [Cr(H₂O)₆]³⁺ $t_{2g}^3$: 0; [Ni(H₂O)₆]²⁺ $t_{2g}^6e_g^{*2}$: 2; Cu²⁺ $t_{2g}^6e_g^{*3}$: 3.

**Memahami hasil.** [Co(NH₃)₆]³⁺ mengisi tepat semua orbital ikatan dan tak berikatan, 18 elektron, dan $e_g^*$ kosong: kompleks yang sangat stabil dan lembam. Kompleks Ni²⁺ dan Cu²⁺ menempatkan dua dan tiga elektron di orbital antiikatan; ikatannya lebih lemah dan lebih labil. Untuk Cu²⁺, ketiga elektron $e_g^*$ yang tidak seragam adalah asal efek Jahn–Teller, kini dalam bahasa orbital molekul: elektron antiikatan yang lebih banyak di $d_{z^2}$ melemahkan ikatan aksial. Bilangan 18 akan muncul lagi sebagai aturan 18 elektron (subbab 14.13).
:::

::: {.contoh}
**Contoh 14.l3 · Model OM numerik**

Pakai energi Coulomb (eV) $\alpha(3d) = -11{,}0$, $\alpha(4s) = -7{,}0$, $\alpha(4p) = -3{,}5$, $\alpha_L = -15{,}0$, dan unsur matriks resonansi $\beta(a_{1g}) = 4{,}0$, $\beta(t_{1u}) = 2{,}5$, $\beta(e_g) = 2{,}8$ eV. Hitung energi orbital molekul, $\Delta_o$, dan persen karakter logam setiap orbital. Bandingkan $\Delta_o$ dengan hampiran (14.el4).

**Penyelesaian.**

```python
import numpy as np
aL = -15.0
blok = {'a1g': (-7.0, 4.0), 't1u': (-3.5, 2.5), 'eg': (-11.0, 2.8)}
for nama, (aM, b) in blok.items():
    E, C = np.linalg.eigh([[aM, b], [b, aL]])
    print(nama, 'E =', E.round(3),
          '%logam ikatan/antiikatan =', round(100*C[0,0]**2, 1), round(100*C[0,1]**2, 1))
Eeg = np.linalg.eigvalsh([[-11.0, 2.8], [2.8, aL]])[1]
print('Delta_o =', Eeg - (-11.0), 'eV;  hampiran:', 2.8**2/4.0)
```

Hasilnya:

| Simetri | Ikatan (eV) | % logam | Antiikatan (eV) | % logam |
|---|---|---|---|---|
| $a_{1g}$ | −16,66 | 14,6 | −5,34 | 85,4 |
| $e_g$ | −16,44 | 20,9 | −9,56 | 79,1 |
| $t_{1u}$ | −15,52 | 4,1 | −2,98 | 95,9 |
| $t_{2g}$ | — | — | −11,00 (tak berikatan) | 100 |

$\Delta_o = -9{,}559 - (-11{,}000) = 1{,}441$ eV $= 11\,600$ cm⁻¹. Hampiran (14.el4) memberi $2{,}8^2/4{,}0 = 1{,}96$ eV, 36% terlalu besar.

**Memahami hasil.** Orbital $e_g^*$ hanya 79% d; 21% sisanya tersebar pada keenam ligan. Elektron di $e_g^*$ karena itu menempati ruang yang lebih besar daripada orbital 3d ion bebas: inilah efek nefelauksetik dalam bentuk paling sederhana. Hampiran perturbasi (14.el4) kurang tepat di sini karena $\beta$ tidak jauh lebih kecil daripada $\alpha_M - \alpha_L$; ikatan logam–ligan cukup kovalen. Model ini tentu kasar (parameternya dipilih, bukan dihitung), tetapi seluruh perhitungan ab initio modern menghasilkan gambaran kualitatif yang sama.
:::

### Efek nefelauksetik

Dalam ion bebas, tolakan antarelektron d dinyatakan dengan parameter Racah $B$ dan $C$ (subbab 14.9). Dalam kompleks, nilai $B$ yang diperoleh dari spektrum (subbab 14.10) selalu lebih kecil. Perbandingannya,

$$
\beta = \frac{B_\text{kompleks}}{B_\text{ion bebas}} < 1 , \qquad \text{(14.el6)}
$$

disebut **rasio nefelauksetik**. Ada dua penyebab yang keduanya bersumber dari kovalensi: orbital $e_g^*$ dan $t_{2g}$ (bila ada ikatan π) sebagian berada pada ligan sehingga rata-rata jarak antarelektron d membesar, dan muatan efektif logam berkurang karena ligan menyumbangkan rapat elektron sehingga orbital d mengembang. Jørgensen menemukan bahwa, seperti $\Delta_o$, pengaruh ligan dan logam dapat dipisahkan:

$$
1 - \beta \approx h(\text{ligan}) \times k(\text{logam}) , \qquad \text{(14.el7)}
$$

dengan $h$: F⁻ 0,8; H₂O 1,0; NH₃ 1,4; en 1,5; Cl⁻ 2,0; CN⁻ 2,0; Br⁻ 2,3; I⁻ 2,7, dan $k$: Mn²⁺ 0,07; Ni²⁺ 0,12; Cr³⁺ 0,20; Fe³⁺ 0,24; Rh³⁺ 0,28; Co³⁺ 0,33. **Deret nefelauksetik** ligan, F⁻ < H₂O < NH₃ < en < Cl⁻ ≈ CN⁻ < Br⁻ < I⁻, berbeda dari deret spektrokimia. Ia mengurutkan ligan menurut kovalensinya: ligan yang lunak dan mudah terpolarisasi (I⁻, Br⁻) paling banyak "berbagi" elektron dengan logam, walaupun $\Delta_o$-nya kecil.

::: {.contoh}
**Contoh 14.l4 · Memeriksa rumus nefelauksetik**

Dari analisis spektrum (subbab 14.10), $B$ untuk [Cr(H₂O)₆]³⁺ adalah 729 cm⁻¹ dan untuk [Cr(NH₃)₆]³⁺ 657 cm⁻¹; $B$ ion bebas Cr³⁺ 918 cm⁻¹. Hitung $\beta$ teramati dan bandingkan dengan (14.el7).

**Penyelesaian.** Teramati: $\beta(\text{H}_2\text{O}) = 729/918 = 0{,}79$; $\beta(\text{NH}_3) = 657/918 = 0{,}72$. Ramalan: $1 - (1{,}0)(0{,}20) = 0{,}80$ dan $1 - (1{,}4)(0{,}20) = 0{,}72$.

**Memahami hasil.** Kecocokannya hampir sempurna. Dalam [Cr(NH₃)₆]³⁺, tolakan antarelektron d hanya 72% nilai ion bebas: elektron d menghabiskan cukup banyak waktu di luar logam. Hasil ini juga menjelaskan Contoh 14.b8: karena energi pemasangan sebanding dengan $B$ dan $C$, energi pemasangan dalam kompleks berkurang dengan faktor yang sama, dan kompleks dengan $\Delta_o$ di dekat perbatasan dapat jatuh ke spin rendah.
:::

::: {.awas}
**Dua deret, dua makna**

Deret spektrokimia mengurutkan **besar pemecahan** $\Delta_o$; deret nefelauksetik mengurutkan **besar kovalensi**. Keduanya sering tertukar. Iodida adalah ligan medan paling lemah tetapi paling kovalen. Fluorida adalah ligan medan lemah dan paling ionik. Sianida berada di ujung kuat kedua deret. Tidak ada satu "kekuatan ligan" yang dapat menggambarkan semua sifat sekaligus; itulah sebabnya diperlukan teori, bukan sekadar urutan.
:::

::: {.kuis}
**Kuis cepat 14.7**

Dalam diagram OM kompleks oktahedral donor σ murni, berapa banyak orbital ikatan, tak berikatan, dan antiikatan yang terbentuk dari 15 orbital basis? Mengapa orbital $t_{2g}$ tidak berikatan?
:::

## 14.8 Ikatan π dan deret spektrokimia

### Orbital π ligan

Banyak ligan mempunyai orbital yang dapat berinteraksi dengan logam secara π, yaitu dengan simpul pada sumbu logam–ligan. Halida, OH⁻, dan O²⁻ mempunyai orbital p terisi yang tegak lurus sumbu ikatan. CO, CN⁻, NO⁺, dan N₂ mempunyai orbital π* kosong. Fosfina mempunyai orbital σ*(P–C) kosong yang berperilaku seperti π. Piridina, bipiridina, dan fenantrolina mempunyai orbital π dan π* aromatik.

Setiap ligan menyumbang dua orbital π, tegak lurus satu sama lain dan tegak lurus sumbu ikatan, sehingga oktahedron mempunyai 12 orbital π. Karakter representasinya (kotak di bawah) memberi

$$
\Gamma_\pi = T_{1g} + T_{2g} + T_{1u} + T_{2u} . \qquad \text{(14.el8)}
$$

Komponen $T_{2g}$ adalah pasangan bagi orbital $t_{2g}$ logam yang tidak mempunyai pasangan σ. Komponen $T_{1u}$ dapat bercampur sedikit dengan 4p (yang sudah sibuk dengan ikatan σ), sedangkan $T_{1g}$ dan $T_{2u}$ tidak mempunyai pasangan di logam dan tetap orbital ligan murni. Jadi ikatan π mengubah satu hal yang paling penting: orbital $t_{2g}$ **tidak lagi tak berikatan**.

::: {.dalam}
**Karakter $\Gamma_\pi$**

Sebuah vektor π yang tidak berpindah tempat di bawah suatu operasi menyumbang $+1$ ke karakter bila arahnya tetap, $-1$ bila arahnya terbalik, dan nol bila diputar 90°. Untuk $E$: 12. Untuk $C_3$, $C_2'$, $i$, $S_6$: semua ligan berpindah, 0. Untuk $C_4$ (di sekitar $z$): ligan 5 dan 6 tidak berpindah, tetapi vektor π-nya diputar 90°, sumbangan 0. Untuk $C_2 = C_4^2$: ligan 5 dan 6 tetap dan keempat vektor π-nya terbalik, $-4$. Untuk $S_4$: tidak ada ligan yang tetap (5 dan 6 bertukar), 0. Untuk $\sigma_h$ (bidang $xy$): ligan 1–4 tetap; dari masing-masing dua vektor π, satu di bidang (tetap) dan satu sejajar $z$ (terbalik), jumlah 0. Untuk $\sigma_d$: dua ligan tetap; masing-masing satu vektor tetap dan satu terbalik, 0. Jadi $\Gamma_\pi$ = 12, 0, 0, 0, −4, 0, 0, 0, 0, 0, dan rumus reduksi memberi $T_{1g} + T_{2g} + T_{1u} + T_{2u}$, masing-masing satu kali.
:::

### Donor π: $\Delta_o$ mengecil

Bila ligan mempunyai orbital π **terisi** yang energinya di bawah orbital d (halida, OH⁻, O²⁻), interaksi $t_{2g}$–$t_{2g}(\pi_L)$ membentuk pasangan ikatan–antiikatan. Kombinasi ikatan, sebagian besar ligan, terisi oleh elektron ligan. Kombinasi antiikatan, sebagian besar logam, menjadi "$t_{2g}$" baru yang terangkat ke atas. Orbital $e_g^*$ tidak berubah. Akibatnya $\Delta_o$ **mengecil**. Inilah sebabnya halida berada di ujung lemah deret spektrokimia: mereka donor σ yang cukup baik, tetapi donor π yang kuat juga, dan sumbangan π itu mengurangi pemecahan.

### Akseptor π: $\Delta_o$ membesar

Bila ligan mempunyai orbital π **kosong** di atas orbital d (CO, CN⁻, bipiridina, fosfina), kombinasi ikatan adalah "$t_{2g}$" baru yang terdorong ke bawah, sebagian besar logam tetapi kini sedikit tersebar ke ligan. $\Delta_o$ **membesar**. Elektron $t_{2g}$ yang menempati orbital ikatan ini memperkuat ikatan logam–ligan dengan memindahkan rapat elektron dari logam ke orbital π* ligan. Gejala ini disebut **ikatan balik** (*back-bonding*). Ikatan σ dari ligan ke logam dan ikatan balik π dari logam ke ligan saling memperkuat: makin banyak rapat elektron yang diterima logam melalui σ, makin mudah logam mengembalikannya melalui π. Kerja sama ini, yang disebut **sinergi**, menjelaskan mengapa CO, ligan yang hampir tidak bersifat basa terhadap proton, membentuk ikatan sangat kuat dengan logam bervalensi rendah.

![Gambar 14.g6 Pengaruh ikatan π pada $\Delta_o$. Kiri: ligan donor σ saja, $t_{2g}$ tak berikatan. Tengah: ligan donor π (orbital π terisi di bawah d) mendorong $t_{2g}$ naik, $\Delta_o$ mengecil. Kanan: ligan akseptor π (orbital π* kosong di atas d) menarik $t_{2g}$ turun, $\Delta_o$ membesar. Energi dihitung dengan model Contoh 14.l5.](fig/c_pi.png){width=92%}

Dengan ini deret spektrokimia (14.ea10) mendapat tafsirnya:

$$
\underbrace{\text{I}^- < \text{Br}^- < \text{Cl}^- < \text{F}^- < \text{OH}^-}_{\text{donor }\pi} < \underbrace{\text{H}_2\text{O}}_{\pi\text{ lemah}} < \underbrace{\text{NH}_3 < \text{en}}_{\sigma\text{ saja}} < \underbrace{\text{bpy} < \text{phen} < \text{PR}_3 < \text{CN}^- < \text{CO}}_{\text{akseptor }\pi} .
$$

Dalam model tumpang tindih sudut, interaksi π ditambahkan dengan parameter $e_\pi$ (positif untuk donor, negatif untuk akseptor). Setiap orbital $t_{2g}$ berinteraksi π dengan empat ligan, sehingga $E(t_{2g}) = 4e_\pi$, dan orbital $e_g$ tidak berinteraksi π sama sekali:

$$
\Delta_o = 3e_\sigma - 4e_\pi . \qquad \text{(14.el9)}
$$

::: {.contoh}
**Contoh 14.l5 · Model OM dengan ikatan π**

Lanjutkan Contoh 14.l3. Tambahkan (a) orbital π ligan terisi pada $-16{,}0$ eV dengan $\beta(t_{2g}) = 1{,}0$ eV (donor π), atau (b) orbital π* ligan kosong pada $-7{,}0$ eV dengan $\beta(t_{2g}) = 1{,}0$ eV (akseptor π). Hitung pergeseran $t_{2g}$ dan $\Delta_o$ baru.

**Penyelesaian.** Blok $t_{2g}$ kini matriks 2 × 2.

```python
import numpy as np
ad, Eeg = -11.0, -9.559           # energi d dan e_g* dari Contoh 14.l3
for nama, api in [('donor', -16.0), ('akseptor', -7.0)]:
    E, C = np.linalg.eigh([[ad, 1.0], [1.0, api]])
    t2g = E[1] if api < ad else E[0]      # orbital yang sebagian besar d
    print(nama, 't2g =', round(t2g, 3), 'Delta_o =', round(Eeg - t2g, 3), 'eV')
```

(a) Donor: $t_{2g}$ naik dari $-11{,}000$ ke $-10{,}807$ eV (+0,193 eV); $\Delta_o$ turun dari 1,441 ke 1,248 eV, berkurang 1550 cm⁻¹. (b) Akseptor: $t_{2g}$ turun ke $-11{,}236$ eV (−0,236 eV); $\Delta_o$ naik ke 1,677 eV, bertambah 1900 cm⁻¹.

**Memahami hasil.** Interaksi π yang unsur matriksnya hanya sepertiga interaksi σ sudah menggeser $\Delta_o$ sekitar 15%. Pada kasus akseptor, orbital $t_{2g}$ terisi kini 5% berkarakter π* ligan: setiap elektron $t_{2g}$ menyumbang sedikit rapat elektron ke ligan. Untuk ion bermuatan rendah dengan banyak elektron $t_{2g}$ dan energi d tinggi (Cr(0), Fe(II), Ru(II)), selisih $\alpha_\pi - \alpha_d$ lebih kecil dan ikatan balik jauh lebih kuat.
:::

::: {.contoh}
**Contoh 14.l6 · Memisahkan σ dan π**

(a) Untuk [Cr(NH₃)₆]³⁺, NH₃ tidak mempunyai orbital π yang cocok ($e_\pi = 0$) dan $\Delta_o = 21\,550$ cm⁻¹. Hitung $e_\sigma(\text{NH}_3)$. (b) Untuk [CrF₆]³⁻, $\Delta_o = 15\,060$ cm⁻¹. Jika $e_\pi(\text{F}^-) \approx 2000$ cm⁻¹ (diperoleh dari spektrum kompleks campuran trans-[CrF₂L₄]⁺), hitung $e_\sigma(\text{F}^-)$. (c) Untuk [Cr(CN)₆]³⁻, $\Delta_o = 26\,600$ cm⁻¹. Jika $e_\sigma(\text{CN}^-) \approx 7500$ cm⁻¹, hitung $e_\pi(\text{CN}^-)$.

**Penyelesaian.** Dari (14.el9). (a) $e_\sigma = 21\,550/3 = 7180$ cm⁻¹. (b) $e_\sigma = (15\,060 + 4 \times 2000)/3 = 7690$ cm⁻¹. (c) $e_\pi = (3 \times 7500 - 26\,600)/4 = -1030$ cm⁻¹.

**Memahami hasil.** Sebagai donor σ, F⁻ sebenarnya **lebih kuat** daripada NH₃ ($e_\sigma$ 7690 terhadap 7180), sesuai dengan muatannya. Kedudukannya yang rendah di deret spektrokimia sepenuhnya akibat donasi π. Sebaliknya, sianida memperoleh hampir 15% $\Delta_o$-nya dari ikatan balik ($-4e_\pi = 4100$ cm⁻¹). Parameter AOM yang terpisah ini dapat dipindahkan dari satu kompleks ke kompleks lain dengan logam yang sama, sehingga memungkinkan ramalan spektrum kompleks campuran.
:::

### Karbonil logam dan frekuensi ulur CO

Bukti paling jelas ikatan balik datang dari spektroskopi inframerah. Orbital π* CO bersifat antiikatan terhadap ikatan C≡O. Setiap elektron yang didonasikan logam ke π* melemahkan ikatan C–O dan menurunkan frekuensi ulurnya. CO bebas menyerap di 2143 cm⁻¹. Dalam deret isoelektronik heksakarbonil, makin negatif muatan kompleks, makin tinggi energi orbital d logam, makin kuat ikatan balik, dan makin rendah $\tilde\nu(\text{CO})$:

| Kompleks | [Ti(CO)₆]²⁻ | [V(CO)₆]⁻ | Cr(CO)₆ | [Mn(CO)₆]⁺ | [Fe(CO)₆]²⁺ | CO bebas |
|---|---|---|---|---|---|---|
| $\tilde\nu(\text{CO})$ (cm⁻¹) | 1748 | 1859 | 2000 | 2090 | 2204 | 2143 |

: Tabel 14.6 Frekuensi ulur CO (mode aktif IR) dalam heksakarbonil isoelektronik.

Pengaruhnya terhadap ikatan C≡O dapat dikuantitatifkan dengan tetapan gaya $k = \mu(2\pi c\tilde\nu)^2$ (subbab 5.7), dengan $\mu(^{12}\text{C}^{16}\text{O}) = 6{,}856$ u.

::: {.contoh}
**Contoh 14.l7 · Tetapan gaya CO dalam karbonil**

Hitung tetapan gaya C–O untuk CO bebas, [Ti(CO)₆]²⁻, Cr(CO)₆, dan [Fe(CO)₆]²⁺ dari Tabel 14.6. Mengapa CO dalam [Fe(CO)₆]²⁺ bergetar lebih cepat daripada CO bebas?

**Penyelesaian.** $\mu = 6{,}856 \times 1{,}6605 \times 10^{-27} = 1{,}1385 \times 10^{-26}$ kg. Untuk CO bebas, $2\pi c\tilde\nu = 2\pi(2{,}998 \times 10^{10})(2143) = 4{,}037 \times 10^{14}$ s⁻¹, sehingga $k = 1{,}1385 \times 10^{-26} \times (4{,}037 \times 10^{14})^2 = 1855$ N/m. Dengan cara sama: [Ti(CO)₆]²⁻ 1234 N/m; Cr(CO)₆ 1616 N/m; [Fe(CO)₆]²⁺ 1962 N/m.

**Memahami hasil.** Dari Fe(II) ke Ti(−II), tetapan gaya C–O turun 37%, sebanding dengan perbedaan antara ikatan rangkap tiga dan rangkap dua: ikatan balik dalam [Ti(CO)₆]²⁻ hampir menghapus satu ikatan π CO. Pada [Fe(CO)₆]²⁺, logam bermuatan +2 hampir tidak mendonasikan apa pun, sedangkan donasi σ dari orbital 5σ CO (yang sedikit antiikatan terhadap C–O) ke logam **menguatkan** ikatan C–O. Itulah sebabnya $\tilde\nu$ naik di atas CO bebas, seperti juga pada CO⁺ (2184 cm⁻¹), yang kehilangan elektron 5σ. Frekuensi ulur CO dengan demikian menjadi "pengukur" rapat elektron pada logam, dan dipakai sehari-hari untuk membandingkan sifat donor ligan lain dalam kompleks karbonil campuran (parameter elektronik Tolman untuk fosfina diukur dengan cara ini pada Ni(CO)₃L).
:::

### Model Dewar–Chatt–Duncanson

Gagasan σ + π balik berlaku pula untuk ligan alkena. Dalam garam Zeise, K[PtCl₃(C₂H₄)], ikatan Pt–etilena terbentuk dari donasi orbital π C=C yang terisi ke orbital σ kosong platina, ditambah ikatan balik dari orbital d terisi platina ke orbital π* C=C yang kosong. Kedua interaksi melemahkan ikatan C=C: frekuensi ulurnya turun dari 1623 cm⁻¹ pada etilena bebas ke sekitar 1516 cm⁻¹, dan atom-atom hidrogen sedikit membengkok menjauhi logam. Bila ikatan balik sangat kuat (logam kaya elektron, alkena dengan substituen penarik elektron), ikatan C=C hampir menjadi tunggal, dan kompleks lebih tepat digambarkan sebagai metalasiklopropana. Model yang sama menjelaskan aktivasi molekul kecil oleh katalis logam: ikatan balik ke orbital antiikatan substrat melemahkan ikatannya.

::: {.contoh}
**Contoh 14.l8 · Melemahnya ikatan C=C dalam garam Zeise**

Dengan menganggap massa tereduksi efektif getaran C=C tidak berubah, berapa persen tetapan gaya C=C berkurang ketika etilena terikat pada Pt(II)?

**Penyelesaian.** $k \propto \tilde\nu^2$, sehingga $k_\text{kompleks}/k_\text{bebas} = (1516/1623)^2 = 0{,}934^2 = 0{,}872$. Tetapan gaya berkurang sekitar 13%.

**Memahami hasil.** Penurunan 13% jauh lebih kecil daripada pada karbonil kaya elektron, karena Pt(II) bermuatan positif dan ikatan baliknya sedang. Getaran C=C dalam kompleks juga bercampur dengan getaran tekuk CH₂, sehingga anggapan massa tereduksi tetap hanyalah hampiran. Namun, arah dan besarnya sesuai dengan ikatan C=C yang memanjang beberapa pikometer. Penurunan frekuensi semacam ini dipakai untuk mengikuti aktivasi alkena dalam reaksi katalitik seperti hidrogenasi dan polimerisasi.
:::

::: {.contoh}
**Contoh 14.l9 · Ramalan urutan $\Delta_o$**

Tanpa tabel, urutkan $\Delta_o$ untuk [CrCl₆]³⁻, [Cr(H₂O)₆]³⁺, [Cr(NH₃)₆]³⁺, [Cr(bpy)₃]³⁺, dan [Cr(CN)₆]³⁻, dan sebutkan jenis interaksi yang menentukan setiap langkah.

**Penyelesaian.** [CrCl₆]³⁻ < [Cr(H₂O)₆]³⁺ < [Cr(NH₃)₆]³⁺ < [Cr(bpy)₃]³⁺ < [Cr(CN)₆]³⁻. Cl⁻: donor σ lemah (orbital 3p tinggi tetapi tumpang tindih dengan d kecil pada jarak Cr–Cl yang panjang) dan donor π kuat. H₂O: donor σ sedang, donor π lemah. NH₃: donor σ saja. bpy: donor σ ditambah akseptor π lemah. CN⁻: donor σ kuat dan akseptor π.

**Memahami hasil.** Nilai teramati (cm⁻¹) kira-kira 13 000; 17 400; 21 550; 23 000; dan 26 600, sesuai urutan. Dengan Cr³⁺ (muatan tinggi, $t_{2g}^3$), ikatan balik ke CN⁻ dan bpy masih sedang. Untuk logam bermuatan rendah, akseptor π jauh lebih kuat; itulah sebabnya faktor $f(\text{CN}^-)$ Jørgensen lebih cocok untuk Fe(II) daripada untuk Cr(III) (Contoh 14.a6).
:::

::: {.terapan}
**Mengaktifkan nitrogen**

N₂ adalah molekul yang sangat lembam: ikatan rangkap tiganya 945 kJ/mol dan HOMO-nya jauh di bawah, LUMO-nya jauh di atas. Industri mengubahnya menjadi amonia dengan proses Haber–Bosch pada 400–500 °C dan 150–300 atm dengan katalis besi. Enzim nitrogenase melakukannya pada suhu kamar dengan kofaktor besi–molibdenum. Dalam kedua kasus, langkah kuncinya adalah ikatan balik π dari logam yang kaya elektron ke orbital π* N₂. Dalam kompleks dinitrogen sederhana seperti [Ru(NH₃)₅(N₂)]²⁺, frekuensi ulur N–N turun dari 2331 cm⁻¹ (N₂ bebas) ke sekitar 2100–2200 cm⁻¹; dalam kompleks dengan logam lebih kaya elektron penurunannya jauh lebih besar. Merancang kompleks yang melemahkan N₂ cukup untuk direduksi pada kondisi lunak adalah salah satu tantangan besar kimia koordinasi, dan bahasa yang dipakai untuk merancangnya adalah bahasa orbital $t_{2g}$ dan π* dalam subbab ini.
:::

::: {.kuis}
**Kuis cepat 14.8**

Dalam AOM, mengapa interaksi π sama sekali tidak memengaruhi orbital $e_g$ kompleks oktahedral? Ke arah mana $\Delta_o$ bergeser bila satu ligan NH₃ dalam [Co(NH₃)₆]³⁺ diganti Cl⁻?
:::
