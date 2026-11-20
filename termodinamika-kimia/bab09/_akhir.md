# Ringkasan Bab 9

| Gagasan | Rumus atau hasil | Subbab |
|---|---|---|
| Besaran molar parsial | $X_\text{J} = (\partial X/\partial n_\text{J})_{T,p,n'}$; $X = \sum n_\text{J}X_\text{J}$ | 9.1 |
| Volume tidak aditif | $V = n_\text{A}V_\text{A} + n_\text{B}V_\text{B}$ dengan $V_\text{J} \ne V^*_\text{m,J}$ untuk campuran nyata | 9.1 |
| Mengukur $V_\text{J}$ | metode garis singgung ($\partial V/\partial n_\text{J}$) dan metode titik potong | 9.2 |
| Potensial kimia | $\mu_\text{J} = (\partial G/\partial n_\text{J})_{T,p,n'}$; $G = \sum n_\text{J}\mu_\text{J}$ | 9.3 |
| Persamaan fundamental | $dG = -S\,dT + V\,dp + \sum\mu_\text{J}\,dn_\text{J}$ | 9.3 |
| Arah perpindahan | zat berpindah dari μ tinggi ke μ rendah; setimbang bila μ sama | 9.3 |
| Turunan μ | $(\partial\mu_\text{J}/\partial p)_T = V_\text{J}$; $(\partial\mu_\text{J}/\partial T)_p = -S_\text{J}$ | 9.3 |
| Gibbs–Duhem | $\sum n_\text{J}\,d\mu_\text{J} = 0$; juga $\sum n_\text{J}\,dV_\text{J} = 0$ | 9.4 |
| Gas ideal | $\mu_\text{J} = \mu_\text{J}^\circ + RT\ln(p_\text{J}/p^\circ)$ | 9.5 |
| Pencampuran gas ideal | $\Delta_\text{mix}G = nRT\sum x_\text{J}\ln x_\text{J}$; $\Delta_\text{mix}H = 0$ | 9.5 |
| Fugasitas | $\mu = \mu^\circ + RT\ln(f/p^\circ)$, $f = \varphi p$; $\ln\varphi = \int_0^p (Z - 1)\,dp/p \approx Bp/RT$ | 9.5 |

**Jawaban kuis cepat.** **9.1** Lebih kecil, karena etanol menyumbang volume lebih sedikit per mol daripada ketika murni. **9.2** Di dekat $x_\text{etanol} = 0$, campuran hampir air murni, sehingga volume molar parsial air sama dengan volume molar air murni dan selisihnya nol. **9.3** Oksigen mengalir dari A ke B, nitrogen dari B ke A; setiap gas mengikuti potensial kimianya sendiri. **9.4** Tidak mungkin. Menurut Gibbs–Duhem, $n_\text{A}\,dV_\text{A} + n_\text{B}\,dV_\text{B} = 0$, sehingga keduanya harus berubah berlawanan arah (atau keduanya tetap). **9.5** Pada tekanan rendah molekul-molekul jarang bertemu, sehingga semua gas berperilaku ideal dan *Z* → 1. Di bawah suhu Boyle, tarikan dominan pada tekanan sedang, sehingga φ < 1.

# Pertanyaan

## Subbab 9.1: Besaran molar parsial

1. Mengapa 50 mL etanol dan 50 mL air menghasilkan kurang dari 100 mL larutan?
2. Apa perbedaan volume molar parsial dan volume molar?
3. Mengapa syarat "campuran yang sangat besar" diperlukan dalam arti fisis besaran molar parsial?

## Subbab 9.2: Volume molar parsial

4. Jelaskan elektrostriksi dan akibatnya bagi volume molar parsial garam.
5. Mengapa kadar alkohol dalam persen volume didefinisikan terhadap volume larutan akhir?

## Subbab 9.3: Potensial kimia

6. Apa arti fisis potensial kimia? Mengapa ia disebut "potensial"?
7. Bandingkan potensial kimia dengan suhu dan potensial listrik sebagai pendorong aliran.
8. Mengapa konsentrasi iodin dalam air dan CCl₄ tidak sama pada kesetimbangan, padahal potensial kimianya sama?
9. Bagaimana tekanan dapat menghentikan aliran osmosis?

## Subbab 9.4: Persamaan Gibbs–Duhem

10. Apa yang dikatakan persamaan Gibbs–Duhem tentang campuran dua zat?

## Subbab 9.5: Potensial kimia gas ideal dan gas nyata

11. Mengapa potensial kimia zat menuju −∞ bila tekanan parsialnya menuju nol? Apa akibatnya bagi pemurnian?
12. Mengapa pencampuran gas ideal spontan walaupun tidak ada kalor yang dilepaskan?
13. Mengapa menangkap CO₂ dari udara lebih mahal daripada dari gas buang cerobong?
14. Apa keadaan standar untuk gas nyata, dan mengapa disebut hipotetis?
15. Mengapa koefisien fugasitas H₂ lebih besar dari 1 pada suhu kamar, sedangkan CH₄ lebih kecil?

# Soal

%%SOAL%%

# Jawaban

%%JAWABAN%%

# Pembahasan soal terpilih

**Soal {{potong}}.** Volume molar campuran adalah $V_\text{m} = x_\text{A}V_\text{A} + x_\text{B}V_\text{B}$, dengan $x_\text{A} = 1 - x_\text{B}$. Turunkan terhadap $x_\text{B}$:
$$
\frac{dV_\text{m}}{dx_\text{B}} = V_\text{B} - V_\text{A} + \left(x_\text{A}\frac{dV_\text{A}}{dx_\text{B}} + x_\text{B}\frac{dV_\text{B}}{dx_\text{B}}\right) = V_\text{B} - V_\text{A} ,
$$
karena suku dalam kurung nol menurut Gibbs–Duhem (9.9). Garis singgung di titik $x_\text{B}^0$ adalah $V_\text{m}(x_\text{B}^0) + (V_\text{B} - V_\text{A})(x_\text{B} - x_\text{B}^0)$. Di $x_\text{B} = 0$ nilainya $x_\text{A}^0V_\text{A} + x_\text{B}^0V_\text{B} - x_\text{B}^0(V_\text{B} - V_\text{A}) = V_\text{A}$; di $x_\text{B} = 1$ nilainya $V_\text{B}$ dengan cara yang sama.

*Cara berpikir:* garis singgung adalah garis lurus $x_\text{A}V_\text{A} + x_\text{B}V_\text{B}$ yang dibuat dengan "membekukan" kedua volume molar parsial pada nilainya di titik singgung. Kedua ujung garis itu adalah campuran yang hanya berisi A atau hanya B, tetapi dengan volume molar parsial yang dibekukan, sehingga yang terbaca adalah $V_\text{A}$ dan $V_\text{B}$ itu sendiri. Metode ini berlaku untuk setiap besaran molar parsial, termasuk entalpi dan potensial kimia.

**Soal {{gd}}.** Dari $G = \sum n_\text{J}\mu_\text{J}$, diferensial totalnya (aturan perkalian) adalah $dG = \sum\mu_\text{J}\,dn_\text{J} + \sum n_\text{J}\,d\mu_\text{J}$. Persamaan fundamental (9.5) pada *T* dan *p* tetap memberi $dG = \sum\mu_\text{J}\,dn_\text{J}$. Kurangkan: $\sum n_\text{J}\,d\mu_\text{J} = 0$.

*Cara berpikir:* kedua ungkapan menghitung perubahan yang sama dengan dua cara. Yang pertama memandang *G* sebagai jumlah sumbangan, yang kedua memandangnya sebagai fungsi keadaan dengan turunan parsial. Agar keduanya cocok, perubahan potensial kimia harus saling meniadakan bila dibobot dengan banyaknya mol. Ini bukan sifat khusus *G*: setiap besaran ekstensif mempunyai hubungan Gibbs–Duhem-nya sendiri.

**Soal {{margules}}.** (a) Dari (9.9) dibagi *n* total, $dV_\text{B} = -(x_\text{A}/x_\text{B})\,dV_\text{A}$. Dengan $dV_\text{A} = 2a\,x_\text{B}\,dx_\text{B}$:
$$
dV_\text{B} = -\frac{x_\text{A}}{x_\text{B}}\,2a\,x_\text{B}\,dx_\text{B} = -2a\,x_\text{A}\,dx_\text{B} = 2a\,x_\text{A}\,dx_\text{A} ,
$$
karena $dx_\text{B} = -dx_\text{A}$. Integralnya $V_\text{B} = \text{tetapan} + a\,x_\text{A}^2$. Untuk B murni ($x_\text{A} = 0$), $V_\text{B} = V^*_\text{m,B}$, sehingga $V_\text{B} = V^*_\text{m,B} + a\,x_\text{A}^2$. Bentuknya sama dengan $V_\text{A}$, dengan peran A dan B ditukar: Gibbs–Duhem tidak mengizinkan bentuk lain.

Untuk (b): $\Delta_\text{mix}V_\text{m} = x_\text{A}(V_\text{A} - V^*_\text{m,A}) + x_\text{B}(V_\text{B} - V^*_\text{m,B}) = a\,x_\text{A}x_\text{B}^2 + a\,x_\text{B}x_\text{A}^2 = a\,x_\text{A}x_\text{B}(x_\text{A} + x_\text{B}) = a\,x_\text{A}x_\text{B}$.

Untuk (c): $x_\text{A}x_\text{B} = x(1 - x)$ paling besar di $x = 0{,}5$, sehingga penyusutan terbesar $a/4 = -0{,}75$ cm³ mol⁻¹. Model sederhana ini memberi kurva yang simetris. Kurva etanol–air pada Gambar 9.1 tidak simetris, sehingga untuk campuran itu diperlukan suku tambahan. Bentuk yang sama akan muncul lagi untuk energi Gibbs di subbab 10.7, sebagai model larutan reguler.

**Soal {{campur}}.** Per mol campuran, $\Delta_\text{mix}G_\text{m} = RT[x\ln x + (1 - x)\ln(1 - x)]$. Turunannya terhadap *x*:
$$
\frac{d\Delta_\text{mix}G_\text{m}}{dx} = RT\left[\ln x + 1 - \ln(1 - x) - 1\right] = RT\ln\frac{x}{1 - x} ,
$$
nol bila $x = 1 - x$, yaitu $x = 0{,}5$. Nilainya: $RT\ln0{,}5 = (2479)(-0{,}693) = -1{,}72$ kJ mol⁻¹.

*Cara berpikir:* kurva $\Delta_\text{mix}G_\text{m}$ simetris dan paling dalam di tengah, tempat ketidakteraturan campuran paling besar. Di kedua ujung, kemiringannya menuju −∞ dan +∞: menambahkan sedikit pertama zat lain ke dalam zat murni selalu sangat menguntungkan. Inilah alasan termodinamika mengapa setiap zat murni cenderung tercemar oleh zat lain, dan mengapa pemurnian sempurna tidak mungkin.

# Bacaan lanjut

1. P. Atkins, J. de Paula, dan J. Keeler, *Atkins' Physical Chemistry*, edisi ke-12 (Oxford University Press, 2023), Topik 3E dan 5A. Fugasitas, besaran molar parsial, dan potensial kimia.
2. I. N. Levine, *Physical Chemistry*, edisi ke-6 (McGraw-Hill, 2009), Bab 4 dan 9. Potensial kimia dan besaran molar parsial, dengan metode pengukuran yang rinci.
3. K. Denbigh, *The Principles of Chemical Equilibrium*, edisi ke-4 (Cambridge University Press, 1981), Bab 2 dan 4. Penurunan yang sangat cermat tentang potensial kimia dan fugasitas.
4. G. N. Lewis dan M. Randall, *Thermodynamics*, edisi revisi oleh K. S. Pitzer dan L. Brewer (McGraw-Hill, 1961). Sumber asli konsep fugasitas dan aktivitas.
