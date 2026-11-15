## 15.7 Spektroskopi elektronik dan asas Franck–Condon

### Struktur getaran pita elektronik

Transisi elektronik molekul menyerap di daerah tampak dan ultraviolet. Dalam fase gas, pita elektronik molekul kecil tampak sebagai **deretan** puncak, masing-masing transisi ke tingkat getaran yang berbeda dalam keadaan elektronik atas, dan setiap puncak itu sendiri terdiri atas garis-garis rotasi. Pertanyaan utama subbab ini adalah: transisi getaran mana yang kuat dan mana yang lemah? Jawabannya, **asas Franck–Condon**, adalah salah satu gagasan paling berguna dalam seluruh spektroskopi molekul.

### Pemisahan momen dipol transisi

Dalam hampiran Born–Oppenheimer (subbab 11.1), fungsi gelombang molekul adalah hasil kali fungsi elektronik (yang bergantung secara parametrik pada koordinat inti $\mathbf R$) dan fungsi getaran: $\Psi = \psi_\text{el}(\mathbf r; \mathbf R)\chi_v(\mathbf R)$. Operator momen dipol adalah jumlah bagian elektron dan bagian inti, $\hat{\boldsymbol\mu} = -e\sum_i\mathbf r_i + e\sum_AZ_A\mathbf R_A$. Momen dipol transisi antara keadaan $(\text{el}'', v'')$ dan $(\text{el}', v')$ menjadi

$$
\boldsymbol\mu_{fi} = \int\chi_{v'}^*\left[\int\psi_\text{el}'^*\hat{\boldsymbol\mu}\,\psi_\text{el}''\,d\mathbf r\right]\chi_{v''}\,d\mathbf R . \qquad \text{(15.27)}
$$

Suku inti tidak menyumbang, karena fungsi elektronik yang berbeda ortogonal pada setiap $\mathbf R$. Integral dalam kurung adalah momen dipol transisi elektronik $\boldsymbol\mu_\text{el}(\mathbf R)$, yang biasanya berubah perlahan dengan geometri. Bila ia dianggap tetap, ia dapat dikeluarkan dari integral:

$$
\boldsymbol\mu_{fi} \approx \boldsymbol\mu_\text{el}\int\chi_{v'}^*\chi_{v''}\,d\mathbf R, \qquad I_{v'v''} \propto |\boldsymbol\mu_\text{el}|^2\,|\langle v'|v''\rangle|^2 . \qquad \text{(15.28)}
$$

Besaran $|\langle v'|v''\rangle|^2$ disebut **faktor Franck–Condon**. Karena fungsi getaran $\chi_{v'}$ untuk satu keadaan elektronik membentuk himpunan lengkap, jumlah faktor Franck–Condon atas semua $v'$ (termasuk kontinuum di atas batas disosiasi) sama dengan 1: intensitas total pita ditentukan oleh $|\boldsymbol\mu_\text{el}|^2$, dan faktor Franck–Condon hanya **membagi** intensitas itu di antara puncak-puncak getaran.

::: {.inti}
**Asas Franck–Condon**

Transisi elektronik berlangsung sangat cepat (sekitar $10^{-15}$ s) dibanding gerak inti (sekitar $10^{-13}$ s), sehingga inti praktis diam selama transisi: transisi digambarkan sebagai garis **tegak** pada diagram energi potensial. Intensitas setiap komponen getaran sebanding dengan faktor Franck–Condon $|\langle v'|v''\rangle|^2$, yaitu kuadrat tumpang tindih fungsi getaran awal dan akhir. Komponen terkuat adalah yang fungsi getaran atasnya bertumpang tindih paling banyak dengan fungsi getaran awal di daerah geometri awal.
:::

### Osilator tergeser

Bila kedua keadaan elektronik mempunyai frekuensi getaran yang sama, tetapi posisi setimbangnya tergeser sejauh $\Delta r$, faktor Franck–Condon dari $v'' = 0$ dapat dihitung secara tepat. Dengan pergeseran tak berdimensi $d = \Delta r\sqrt{\mu\omega/\hbar}$ dan **faktor Huang–Rhys** $S = d^2/2$,

$$
|\langle v'|0\rangle|^2 = e^{-S}\frac{S^{v'}}{v'!} , \qquad \text{(15.29)}
$$

yaitu distribusi Poisson dengan rata-rata $S$. Bila $S \ll 1$ (geometri hampir tidak berubah), hampir seluruh intensitas jatuh pada transisi 0–0 dan pita tampak sebagai satu puncak tajam. Bila $S$ besar, intensitas tersebar pada progresi panjang dengan puncak di sekitar $v' \approx S$, dan energi puncak itu kira-kira sama dengan energi transisi tegak dari dasar sumur bawah.

::: {.dalam}
**Penurunan distribusi Poisson**

Keadaan dasar osilator bawah, dilihat dari osilator atas yang pusatnya tergeser, adalah fungsi Gauss yang pusatnya tidak di titik setimbang. Dalam bahasa operator tangga (subbab 5.6), operator geser $\hat D = \exp[-(d/\sqrt2)(\hat a^\dagger - \hat a)]$ memindahkan pusat fungsi gelombang sejauh $d$. Dengan rumus Baker–Campbell–Hausdorff, $\hat D = e^{-d^2/4}e^{-(d/\sqrt2)\hat a^\dagger}e^{(d/\sqrt2)\hat a}$. Bekerja pada $|0\rangle$, faktor terakhir memberi 1 (karena $\hat a|0\rangle = 0$), dan

$$
\hat D|0\rangle = e^{-d^2/4}\sum_{v}\frac{(-d/\sqrt2)^v}{\sqrt{v!}}|v\rangle .
$$

Kuadrat koefisien adalah $e^{-d^2/2}(d^2/2)^v/v! = e^{-S}S^v/v!$. Keadaan seperti $\hat D|0\rangle$ disebut keadaan koheren; ia akan muncul lagi sebagai paket gelombang dalam spektroskopi resolusi waktu (subbab 15.12).
:::

::: {.contoh}
**Contoh 15.28 · Progresi Poisson**

Hitung faktor Franck–Condon $v' = 0$ sampai 6 untuk $S = 2{,}0$. Komponen mana yang terkuat?

**Penyelesaian.** $e^{-2} = 0{,}1353$. Dengan (15.29): 0,135; 0,271; 0,271; 0,180; 0,090; 0,036; 0,012.

**Memahami hasil.** Komponen $v' = 1$ dan 2 sama kuat dan menjadi puncak. Komponen 0–0 hanya 13,5% dari total. Spektrum serapan seperti ini, dengan puncak-puncak berjarak $\tilde\nu'$ (frekuensi keadaan atas) dan selubung yang naik lalu turun, khas untuk transisi yang mengubah panjang ikatan sedang, misalnya transisi π→π* yang memperpanjang ikatan C=C sekitar 5–10 pm. Mengukur perbandingan intensitas puncak memberi $S$, dan dari $S$ diperoleh besar perubahan geometri, keterangan yang sulit diperoleh dengan cara lain untuk keadaan tereksitasi yang berumur nanodetik.
:::

![Gambar 15.5 Asas Franck–Condon. (a) Kurva energi potensial keadaan dasar X dan keadaan tereksitasi B molekul I₂ (model Morse); panah tegak dari $v'' = 0$ jatuh di daerah $v' \approx 30$. (b) Faktor Franck–Condon yang dihitung untuk model Morse (batang biru) dan untuk model harmonik (batang jingga): anharmonisitas menggeser puncak ke $v'$ yang lebih tinggi.](fig/c_franck.png){width=94%}

::: {.contoh}
**Contoh 15.29 · Mengapa uap iodin ungu**

Untuk I₂: keadaan X, $\omega_e = 214{,}50$ cm⁻¹, $\omega_ex_e = 0{,}614$ cm⁻¹, $r_e = 2{,}666$ Å; keadaan B, $\omega_e = 125{,}69$ cm⁻¹, $\omega_ex_e = 0{,}764$ cm⁻¹, $r_e = 3{,}024$ Å, $T_e = 15\,769$ cm⁻¹. Hitung faktor Franck–Condon dari $v'' = 0$ dengan (a) model harmonik dan (b) model Morse, lalu tentukan komponen terkuat dan panjang gelombangnya.

**Rencana.** Bangun potensial Morse dengan $D_e = \omega_e^2/4\omega_ex_e$ dan $a = \sqrt{8\pi^2c\mu\omega_ex_e/h}$, selesaikan persamaan Schrödinger secara numerik pada kisi (matriks tridiagonal beda hingga, subbab 5.12), lalu hitung tumpang tindihnya.

**Penyelesaian.**

```python
import numpy as np
from scipy.linalg import eigh_tridiagonal
h, c, u = 6.62607015e-34, 2.99792458e10, 1.66053906660e-27
mu = 63.452                                   # massa tereduksi I2 (u)

def tingkat_morse(we, wexe, re, r, nmax=60):
    De = we**2 / (4*wexe)                                     # cm^-1
    a = np.sqrt(8*np.pi**2*c*mu*u*wexe/h) * 1e-10             # Å^-1
    T = h / (8*np.pi**2*c*mu*u) * 1e20                        # hbar^2/2mu
    dr = r[1] - r[0]
    V = De * (1 - np.exp(-a*(r - re)))**2
    E, psi = eigh_tridiagonal(2*T/dr**2 + V, -T/dr**2*np.ones(len(r) - 1),
                              select='i', select_range=(0, nmax))
    return E, psi / np.sqrt(dr)

r = np.linspace(2.2, 5.5, 6000)
EX, pX = tingkat_morse(214.50, 0.614, 2.666, r)
EB, pB = tingkat_morse(125.69, 0.764, 3.024, r)
FC = (pB.T @ pX[:, 0] * (r[1] - r[0]))**2                     # |<v'|0>|^2
v = FC.argmax()
nu = 15769.0 + EB[v] - EX[0]
print(v, FC[v], nu, 1e7/nu, FC.sum())
```

(a) Model harmonik (osilator dengan frekuensi berbeda, tumpang tindih dihitung dengan cara yang sama): puncak di $v' = 15$, sekitar 17 430 cm⁻¹ (574 nm). (b) Model Morse: puncak di $v' = 32$, 18 940 cm⁻¹ (528 nm). Jumlah faktor untuk $v' \le 60$ adalah 0,88; sisanya jatuh pada tingkat yang lebih tinggi dan kontinuum.

**Memahami hasil.** Serapan terkuat uap iodin memang berada di sekitar 520–540 nm, sehingga iodin menyerap hijau-kuning dan tampak ungu. Model harmonik meleset jauh karena transisi tegak dari $r = 2{,}666$ Å mendarat di **dinding dalam** potensial B, 0,36 Å di sebelah kiri dasarnya, tempat potensial Morse jauh lebih curam daripada parabola; energi di titik itu lebih tinggi, dan $v'$ yang bersesuaian lebih besar. Pada panjang gelombang lebih pendek dari 499 nm (batas konvergensi, energi disosiasi keadaan B), progresi berubah menjadi serapan kontinu, karena molekul yang tereksitasi langsung terurai menjadi dua atom iodin, satu di antaranya tereksitasi. Contoh ini menunjukkan mengapa spektroskopi elektronik peka terhadap bentuk potensial jauh dari titik setimbang.
:::

### Aturan seleksi elektronik

Momen dipol transisi elektronik $\boldsymbol\mu_\text{el}$ nol atau tidak ditentukan oleh kesetangkupan. Untuk molekul diatom (lambang suku subbab 11.9), aturan seleksinya adalah

$$
\Delta\Lambda = 0, \pm1; \qquad \Delta S = 0; \qquad \Sigma^+ \leftrightarrow \Sigma^+,\ \Sigma^- \leftrightarrow \Sigma^-; \qquad g \leftrightarrow u\ (\text{homonuklir}) . \qquad \text{(15.30)}
$$

Untuk molekul poliatom, transisi diizinkan bila hasil kali langsung $\Gamma(\psi_\text{el}') \otimes \Gamma(x, y, z) \otimes \Gamma(\psi_\text{el}'')$ mengandung representasi bersetangkup penuh (subbab 10.10). Transisi yang terlarang simetri masih dapat teramati lemah melalui kopling vibronik: getaran yang tidak bersetangkup penuh mencampurkan keadaan elektronik lain ke dalam keadaan atas, dan transisi meminjam intensitas (mekanisme Herzberg–Teller, yang telah kita jumpai pada transisi d–d di subbab 14.11).

::: {.contoh}
**Contoh 15.30 · Oksigen: diizinkan dan terlarang**

Keadaan dasar O₂ adalah $X\,^3\Sigma_g^-$. Keadaan tereksitasi terendahnya $a\,^1\Delta_g$ (7918 cm⁻¹), $b\,^1\Sigma_g^+$ (13 195 cm⁻¹), dan $B\,^3\Sigma_u^-$ (sekitar 49 800 cm⁻¹). Transisi mana dari X yang diizinkan dipol listrik?

**Penyelesaian.** X → a: $\Delta S \ne 0$, $\Delta\Lambda = 2$, $g \to g$: terlarang tiga kali. X → b: $\Delta S \ne 0$, $\Sigma^- \to \Sigma^+$, $g \to g$: terlarang. X → B: $\Delta S = 0$, $\Sigma^- \to \Sigma^-$, $g \to u$: diizinkan.

**Memahami hasil.** Transisi X → B adalah pita Schumann–Runge (175–200 nm) yang kuat; O₂ di atmosfer atas menyerap ultraviolet jauh di daerah ini dan terurai menjadi atom O, langkah pertama pembentukan ozon. Transisi X → b sangat lemah tetapi teramati sebagai "pita A atmosfer" di 762 nm berkat kopling spin–orbit dan dipol magnet; ia dipakai satelit untuk mengukur tekanan puncak awan. Keadaan $a\,^1\Delta_g$ adalah oksigen singlet, yang umurnya dalam gas sekitar 72 menit karena transisinya ke keadaan dasar terlarang ganda. Oksigen singlet sangat reaktif dan dibentuk dengan sengaja dalam terapi fotodinamik kanker melalui transfer energi dari molekul fotosensitizer dalam keadaan triplet (subbab 15.8).
:::

### Struktur rotasi dan kepala pita

Dalam pita elektronik molekul diatom, setiap komponen getaran mempunyai cabang P dan R (dan Q bila $\Lambda \ne 0$ pada salah satu keadaan). Berbeda dengan pita inframerah, tetapan rotasi keadaan atas $B'$ dapat sangat berbeda dari $B''$, karena ikatan dapat memanjang atau memendek banyak. Untuk cabang R, $\tilde\nu = \tilde\nu_0 + (B' + B'')(J + 1) + (B' - B'')(J + 1)^2$, sebuah parabola dalam $J$ (**diagram Fortrat**). Bila $B' < B''$ (ikatan memanjang), suku kuadrat negatif, sehingga garis-garis cabang R mula-mula bergerak ke energi lebih tinggi, berbalik pada suatu $J$, lalu bergerak kembali. Titik balik itu, tempat garis-garis menumpuk, disebut **kepala pita**, dan pitanya disebut "terdegradasi ke merah".

::: {.contoh}
**Contoh 15.31 · Letak kepala pita**

Untuk transisi dengan $B'' = 1{,}90$ cm⁻¹ dan $B' = 1{,}70$ cm⁻¹, tentukan $J$ tempat kepala pita cabang R terbentuk dan jaraknya dari pusat pita.

**Penyelesaian.** Turunan $d\tilde\nu/dJ = (B' + B'') + 2(B' - B'')(J + 1) = 0$ memberi $J + 1 = (B' + B'')/2(B'' - B') = 3{,}60/0{,}40 = 9$, jadi $J = 8$. Jaraknya $(3{,}60)(9) + (-0{,}20)(81) = 32{,}4 - 16{,}2 = 16{,}2$ cm⁻¹ di atas pusat pita.

**Memahami hasil.** Kepala pita adalah bagian pita yang paling tajam dan paling mudah diukur, sehingga dulu posisi pita elektronik dilaporkan sebagai posisi kepalanya. Arah degradasi pita langsung memberi tahu apakah ikatan memanjang ($B' < B''$, degradasi ke merah) atau memendek (degradasi ke ungu) dalam keadaan tereksitasi, bahkan sebelum garis rotasi dianalisis satu per satu.
:::

### Molekul poliatom dan benzena

Pada molekul poliatom, progresi Franck–Condon hanya muncul untuk mode yang geometri setimbangnya berubah, biasanya mode bersetangkup penuh. Dalam transisi n→π* formaldehida, misalnya, elektron dipindah ke orbital π* yang antiikatan terhadap C=O, sehingga ikatan C=O memanjang dan progresi panjang muncul dalam ulur C=O keadaan tereksitasi (sekitar 1183 cm⁻¹, dibanding 1746 cm⁻¹ pada keadaan dasar). Penurunan frekuensi ini sendiri adalah bukti bahwa elektron masuk orbital antiikatan.

Benzena memberikan contoh baku kopling vibronik. Transisi $^1A_{1g} \to {}^1B_{2u}$ (pita 254 nm) terlarang simetri, karena $B_{2u} \otimes \Gamma(x, y, z)$ tidak mengandung $A_{1g}$. Pita asal 0–0 di 38 086 cm⁻¹ hampir tidak terlihat. Spektrum yang teramati dimulai dari komponen yang melibatkan satu kuantum mode tekuk cincin $e_{2g}$ ($\nu_6$, 521 cm⁻¹ pada keadaan tereksitasi): $B_{2u} \otimes E_{2g} = E_{1u}$, yang bertransformasi seperti $(x, y)$, sehingga diizinkan. Dari komponen itu tumbuh progresi dalam mode napas cincin $a_{1g}$ (923 cm⁻¹ pada keadaan tereksitasi). Kekuatan osilator pita ini hanya sekitar 0,002 (Contoh 15.6).

::: {.contoh}
**Contoh 15.32 · Pita benzena yang "salah tempat"**

Asal pita $^1B_{2u}$ benzena di 38 086 cm⁻¹. Hitung panjang gelombang asal itu dan komponen $6_0^1$ (satu kuantum $\nu_6' = 521$ cm⁻¹ dalam keadaan atas). Komponen $6_1^0$ (dari satu kuantum $\nu_6'' = 608$ cm⁻¹ di keadaan dasar, pita panas) juga teramati. Di mana letaknya dan mengapa lemah pada suhu kamar?

**Penyelesaian.** Asal: $10^7/38\,086 = 262{,}6$ nm. $6_0^1$: $38\,086 + 521 = 38\,607$ cm⁻¹, yaitu 259,0 nm. $6_1^0$: $38\,086 - 608 = 37\,478$ cm⁻¹, yaitu 266,8 nm. Populasi $v_6'' = 1$ pada 298 K sebanding dengan $2e^{-608/207{,}2} = 0{,}11$ (faktor 2 dari degenerasi mode $e_{2g}$).

**Memahami hasil.** Spektrum benzena dengan demikian mengapit pita asal yang hilang: komponen yang diizinkan vibronik muncul $\nu_6'$ di atas dan $\nu_6''$ di bawahnya. Ketergantungan intensitas pita panas pada suhu memastikan penafsiran ini. Benzena adalah contoh pertama ketika mekanisme Herzberg–Teller dikonfirmasi secara kuantitatif, dan pola serupa muncul pada banyak molekul aromatik.
:::

::: {.kuis}
**Kuis cepat 15.7**

Jika keadaan atas dan bawah mempunyai potensial yang identik (tidak tergeser), komponen getaran apa saja yang muncul dalam spektrum serapan dari $v'' = 0$? Mengapa?
:::

## 15.8 Fluoresensi, fosforesensi, diagram Jablonski

### Nasib molekul yang tereksitasi

Molekul organik dalam keadaan dasar singlet $S_0$ yang menyerap foton naik ke keadaan singlet tereksitasi $S_1$, $S_2$, dan seterusnya, biasanya ke tingkat getaran yang tinggi. Apa yang terjadi selanjutnya digambarkan oleh **diagram Jablonski** (Gambar 15.6), yang menyusun keadaan singlet dan triplet berdampingan beserta semua jalur peluruhannya:

- **Relaksasi getaran** (sekitar $10^{-12}$ s): kelebihan energi getaran diserahkan ke pelarut melalui tumbukan, dan molekul turun ke tingkat getaran terendah keadaan elektronik yang sama.
- **Konversi internal** (IC): peralihan tanpa radiasi antara keadaan berspin sama, misalnya $S_2 \to S_1$ atau $S_1 \to S_0$.
- **Fluoresensi** (laju $k_f$): pancaran foton $S_1 \to S_0$, diizinkan spin, umur khas nanodetik.
- **Lintas antarsistem** (ISC): peralihan tanpa radiasi antara keadaan berspin berbeda, $S_1 \to T_1$, dimungkinkan oleh kopling spin–orbit.
- **Fosforesensi**: pancaran $T_1 \to S_0$, terlarang spin, umur milidetik sampai detik.

Karena konversi internal di antara keadaan tereksitasi yang lebih tinggi sangat cepat, pendaran hampir selalu berasal dari tingkat getaran terendah $S_1$ (atau $T_1$), apa pun panjang gelombang eksitasinya. Inilah **aturan Kasha**. Pengecualian terkenal adalah azulena, yang berpendar dari $S_2$ karena celah $S_2$–$S_1$-nya sangat besar.

![Gambar 15.6 Diagram Jablonski. Panah lurus: proses radiatif (serapan A, fluoresensi F, fosforesensi P); panah bergelombang: proses tanpa radiasi (relaksasi getaran RG, konversi internal KI, lintas antarsistem LAS). Skala waktu khas dicantumkan di sebelah kanan.](fig/c_jablonski.png){width=88%}

### Kinetika dan hasil kuantum

Keadaan $S_1$ dikosongkan oleh beberapa proses orde pertama yang bersaing. Bila $k_f$, $k_\text{IC}$, dan $k_\text{ISC}$ adalah tetapan lajunya,

$$
\tau_f = \frac{1}{k_f + k_\text{IC} + k_\text{ISC}}, \qquad \Phi_f = \frac{k_f}{k_f + k_\text{IC} + k_\text{ISC}} = k_f\tau_f . \qquad \text{(15.31)}
$$

**Hasil kuantum** $\Phi_f$ adalah fraksi foton terserap yang dipancarkan kembali sebagai fluoresensi; **umur fluoresensi** $\tau_f$ terukur dari peluruhan pendaran setelah pulsa laser singkat. Kedua besaran yang terukur ini memberi $k_f = \Phi_f/\tau_f$ dan $k_\text{nr} = (1 - \Phi_f)/\tau_f$. Laju radiatif $k_f$ sendiri dapat ditaksir dari spektrum serapan, karena ia adalah koefisien Einstein $A$ untuk transisi yang sama. Strickler dan Berg menurunkan versi praktis hubungan Einstein untuk pita lebar dalam larutan:

$$
k_f \approx 2{,}88 \times 10^{-9}\,n^2\tilde\nu^2\int\varepsilon\,d\tilde\nu\quad (\text{s}^{-1}) , \qquad \text{(15.32)}
$$

dengan $n$ indeks bias pelarut, $\tilde\nu$ bilangan gelombang rata-rata pita dalam cm⁻¹, dan $\varepsilon$ dalam L mol⁻¹ cm⁻¹. Faktor $\tilde\nu^2$ (bukan $\tilde\nu^3$) muncul karena integralnya atas $\varepsilon$, yang sendiri sudah memuat satu faktor frekuensi.

::: {.contoh}
**Contoh 15.33 · Fluoresein**

Fluoresein dalam NaOH 0,1 M mempunyai $\Phi_f = 0{,}93$ dan $\tau_f = 4{,}0$ ns. Pita serapannya di 490 nm dengan $\varepsilon_\text{maks} = 76\,900$ L mol⁻¹ cm⁻¹ dan lebar efektif sekitar 2000 cm⁻¹. (a) Hitung $k_f$ dan $k_\text{nr}$. (b) Taksir $k_f$ dengan (15.32) ($n = 1{,}333$).

**Penyelesaian.** (a) $k_f = 0{,}93/4{,}0 \times 10^{-9} = 2{,}3 \times 10^8$ s⁻¹; $k_\text{nr} = 0{,}07/4{,}0 \times 10^{-9} = 1{,}8 \times 10^7$ s⁻¹. (b) $\int\varepsilon\,d\tilde\nu = 1{,}0645 \times 76\,900 \times 2000 = 1{,}64 \times 10^8$. Dengan $\tilde\nu = 20\,400$ cm⁻¹: $k_f \approx 2{,}88 \times 10^{-9} \times 1{,}777 \times (20\,400)^2 \times 1{,}64 \times 10^8 = 3{,}5 \times 10^8$ s⁻¹.

**Memahami hasil.** Taksiran dari serapan sesuai dalam faktor 1,5 dengan nilai terukur, ketelitian yang biasa untuk rumus Strickler–Berg (lebar pita yang dipakai di sini hanya kira-kira). Fluoresein memancarkan 93 dari setiap 100 foton yang diserapnya: jalur tanpa radiasinya lambat karena kerangka xantena yang kaku tidak mudah mengubah energi elektronik menjadi getaran. Inilah sebabnya fluoresein dan turunannya (FITC, Alexa) dipakai di mana-mana dalam biologi, dari pewarnaan sel sampai pelacak kebocoran pipa.
:::

### Geseran Stokes dan citra cermin

Fluoresensi selalu berada pada panjang gelombang yang lebih panjang daripada serapan. Selisihnya, **geseran Stokes**, berasal dari relaksasi getaran dan penataan ulang pelarut: serapan berakhir di tingkat getaran tinggi $S_1$ dalam geometri $S_0$, sedangkan pancaran berawal dari $S_1$ yang telah relaks dan berakhir di tingkat getaran tinggi $S_0$. Karena progresi Franck–Condon serapan mencerminkan tingkat getaran $S_1$ dan progresi pancaran mencerminkan tingkat getaran $S_0$, dan kedua himpunan itu sering hampir sama, spektrum fluoresensi tampak seperti **citra cermin** spektrum serapan terhadap transisi 0–0 (Gambar 15.7). Pelanggaran aturan citra cermin menandakan bahwa geometri keadaan tereksitasi sangat berbeda atau bahwa ada proses dalam keadaan tereksitasi, seperti transfer proton atau pembentukan eksimer.

![Gambar 15.7 Spektrum serapan dan fluoresensi model untuk molekul dengan progresi getaran 1400 cm⁻¹ dan faktor Huang–Rhys $S = 1{,}0$ dalam kedua keadaan. Kedua spektrum saling bercermin terhadap transisi 0–0; geseran Stokes kecil karena relaksasi pelarut diabaikan.](fig/c_cermin.png){width=86%}

### Lintas antarsistem dan fosforesensi

Lintas antarsistem memerlukan kopling spin–orbit, yang lemah untuk unsur ringan. Laju ISC meningkat tajam dalam dua kasus. Pertama, bila molekul mengandung atom berat (Br, I, logam transisi): **efek atom berat**. Naftalena berfluoresensi dengan $\Phi_f \approx 0{,}2$, sedangkan 1-bromonaftalena hampir tidak berfluoresensi karena hampir semua $S_1$ berpindah ke $T_1$. Kedua, bila peralihan melibatkan perubahan jenis orbital: **aturan El-Sayed** menyatakan bahwa ISC antara keadaan $^1(n,\pi^*)$ dan $^3(\pi,\pi^*)$ jauh lebih cepat daripada antara dua keadaan berjenis sama, karena perubahan orbital dari n ke π memberikan perubahan momentum sudut orbital yang dapat mengimbangi perubahan spin. Benzofenona, dengan $S_1$ berjenis n,π*, menjalani ISC dalam sekitar 10 ps dengan hasil kuantum hampir 1.

Fosforesensi jarang terlihat dalam larutan pada suhu kamar, karena keadaan triplet yang berumur panjang dipadamkan oleh tumbukan, terutama dengan O₂ (yang keadaan dasarnya triplet dan menerima energi dengan membentuk oksigen singlet). Dalam kaca beku pada 77 K atau dalam padatan kaku, fosforesensi tampak jelas. Bahan "glow in the dark" dan layar OLED fosforesens (yang memakai kompleks iridium, dengan kopling spin–orbit kuat, agar triplet dapat memancar efisien) memanfaatkan proses ini.

::: {.contoh}
**Contoh 15.34 · Mengapa benzofenona tidak berfluoresensi**

Untuk benzofenona, $k_\text{ISC} \approx 10^{11}$ s⁻¹ dan $k_f \approx 10^6$ s⁻¹ (pita n→π* yang lemah). Taksir $\Phi_f$ dan $\Phi_\text{ISC}$. Mengapa benzofenona dipakai sebagai fotosensitizer triplet?

**Penyelesaian.** $\Phi_f = 10^6/(10^{11} + 10^6) = 1 \times 10^{-5}$; $\Phi_\text{ISC} \approx 1$.

**Memahami hasil.** Hampir setiap foton yang diserap benzofenona menghasilkan satu molekul dalam keadaan $T_1$, yang berumur panjang dan mempunyai energi sekitar 290 kJ/mol. Triplet ini dapat memindahkan energinya ke molekul lain yang sulit dieksitasi langsung ke keadaan tripletnya (transfer energi triplet–triplet), atau mengambil atom hidrogen dari pelarut. Kedua sifat ini menjadikan benzofenona alat standar dalam fotokimia organik dan inisiator polimerisasi yang dipakai dalam tinta dan pelapis yang dikeringkan dengan sinar UV.
:::

### Pemadaman dan transfer energi

Molekul lain (pemadam, Q) dapat mengosongkan $S_1$ melalui tumbukan dengan tetapan laju bimolekular $k_q$. Laju peluruhan total menjadi $1/\tau_0 + k_q[\text{Q}]$, dan perbandingan intensitas tanpa dan dengan pemadam mengikuti **persamaan Stern–Volmer**:

$$
\frac{I_0}{I} = \frac{\tau_0}{\tau} = 1 + k_q\tau_0[\text{Q}] = 1 + K_\text{SV}[\text{Q}] . \qquad \text{(15.33)}
$$

Untuk pemadaman yang dikendalikan difusi dalam pelarut biasa, $k_q \approx 10^{10}$ L mol⁻¹ s⁻¹.

Pemadaman juga dapat terjadi tanpa tumbukan, melalui interaksi dipol–dipol jarak jauh antara molekul donor yang tereksitasi dan molekul akseptor yang menyerap di panjang gelombang pancaran donor. Efisiensi **transfer energi resonansi Förster** (FRET) bergantung sangat tajam pada jarak $r$:

$$
E = \frac{1}{1 + (r/R_0)^6} , \qquad \text{(15.34)}
$$

dengan $R_0$ (biasanya 2–8 nm) jarak tempat efisiensinya 50%. Ketergantungan $r^{-6}$ berasal dari laju yang sebanding dengan kuadrat energi interaksi dipol–dipol ($\propto r^{-3}$), menurut aturan emas Fermi. FRET dipakai sebagai "penggaris molekul" untuk mengukur jarak di dalam protein dan asam nukleat.

::: {.contoh}
**Contoh 15.35 · Analisis Stern–Volmer**

Fluoresensi kinina sulfat ($\tau_0 = 19$ ns) dipadamkan oleh ion klorida. Data $I_0/I$ pada [Cl⁻] = 0, 2, 4, 6, 8, dan 10 mM adalah 1,000; 1,410; 1,788; 2,208; 2,594; 3,010. Tentukan $K_\text{SV}$ dan $k_q$.

**Penyelesaian.**

```python
import numpy as np
Q = np.array([0, 2, 4, 6, 8, 10]) * 1e-3          # mol/L
r = np.array([1.000, 1.410, 1.788, 2.208, 2.594, 3.010])
KSV, b = np.polyfit(Q, r, 1)
print(KSV, b, KSV / 19e-9)
```

Garis lurus memberi $K_\text{SV} = 200$ L/mol dengan perpotongan 1,000, sehingga $k_q = 200/(19 \times 10^{-9}) = 1{,}05 \times 10^{10}$ L mol⁻¹ s⁻¹.

**Memahami hasil.** Nilai $k_q$ sama dengan laju tumbukan yang dikendalikan difusi: setiap pertemuan kinina tereksitasi dengan ion klorida memadamkannya. Itulah sebabnya larutan kinina untuk baku hasil kuantum dibuat dalam asam sulfat, bukan asam klorida. Grafik Stern–Volmer yang melengkung ke atas menunjukkan adanya pemadaman statis (pembentukan kompleks di keadaan dasar) di samping pemadaman dinamis; perbedaannya dapat dipastikan dengan mengukur $\tau$, yang hanya berubah oleh pemadaman dinamis.
:::

::: {.contoh}
**Contoh 15.36 · Penggaris FRET**

Pasangan donor–akseptor dengan $R_0 = 5{,}0$ nm dipasang pada dua ujung sebuah protein. Efisiensi transfer terukur 0,25. (a) Berapa jarak keduanya? (b) Hitung efisiensi bila jaraknya 3, 5, dan 7 nm.

**Penyelesaian.** (a) Dari (15.34), $r = R_0(1/E - 1)^{1/6} = 5{,}0 \times 3^{1/6} = 6{,}0$ nm. (b) 0,96; 0,50; 0,12.

**Memahami hasil.** Efisiensi berubah dari hampir 1 ke hampir 0 dalam rentang beberapa nanometer di sekitar $R_0$, ukuran khas makromolekul biologis. Pengukuran FRET pada molekul tunggal memungkinkan peneliti melihat protein melipat dan membuka atau enzim berganti konformasi secara langsung, satu molekul pada satu waktu.
:::

::: {.kuis}
**Kuis cepat 15.8**

Mengapa fosforesensi selalu berada pada panjang gelombang yang lebih panjang daripada fluoresensi molekul yang sama? Mengapa melarutkan sampel dalam pelarut yang mengandung iodoetana mengurangi fluoresensi tetapi dapat meningkatkan fosforesensi?
:::

## 15.9 UV-Vis senyawa organik

### Kromofor dan jenis transisi

Spektrum serapan ultraviolet dan tampak senyawa organik ditentukan oleh **kromofor**, gugus atom tempat transisi elektronik terjadi. Dalam bahasa orbital molekul, jenis transisinya diberi nama menurut orbital asal dan tujuan:

| Transisi | Contoh | $\lambda_\text{maks}$ (nm) | $\varepsilon_\text{maks}$ |
|---|---|---|---|
| σ → σ* | CH₄ | < 150 | — |
| n → σ* | CH₃OH, CH₃NH₂ | 180–215 | 100–3000 |
| π → π* (terisolasi) | CH₂=CH₂ | 165 | ≈ 15 000 |
| π → π* (terkonjugasi) | CH₂=CH–CH=CH₂ | 217 | 21 000 |
| n → π* | (CH₃)₂C=O | 279 | 15 |
| π → π* aromatik | benzena | 184, 204, 254 | 60 000; 7400; 204 |

: Tabel 15.2 Transisi elektronik khas molekul organik (pelarut nonpolar).

Hanya transisi π→π* dalam sistem terkonjugasi dan n→π* yang jatuh di daerah yang mudah diukur (di atas 200 nm). Transisi n→π* lemah karena orbital n (pasangan bebas di bidang molekul) dan π* (tegak lurus bidang) hampir tidak bertumpang tindih, sehingga momen dipol transisinya kecil; dalam molekul bersetangkup ia bahkan terlarang simetri. Transisi π→π* kuat karena kedua orbital menempati daerah yang sama dan elektron berpindah sepanjang sistem terkonjugasi.

### Konjugasi

Makin panjang sistem terkonjugasi, makin kecil selisih HOMO–LUMO (subbab 13.5–13.6) dan makin panjang $\lambda_\text{maks}$. Dari etilena (165 nm) ke butadiena (217 nm), heksatriena, dan seterusnya, setiap ikatan rangkap tambahan menggeser serapan 30–40 nm ke merah, dan intensitasnya naik karena momen dipol transisi memanjang bersama molekul. β-Karotena dengan sebelas ikatan rangkap terkonjugasi menyerap di 450 nm dan berwarna jingga. Namun, penggeseran ini makin kecil untuk rantai yang sangat panjang dan mendekati batas sekitar 600 nm, bukan nol. Penyebabnya adalah selang-seling panjang ikatan (ikatan tunggal dan rangkap tidak menjadi sama panjang), yang membuka celah energi seperti pada poliasetilena (subbab 13.13).

::: {.contoh}
**Contoh 15.37 · Kegagalan model elektron bebas untuk karotena**

Model partikel dalam kotak (subbab 3.8) untuk $N$ elektron π dalam kotak sepanjang $L$ memberi $\lambda = 8m_ecL^2/h(N + 1)$. Untuk β-karotena, $N = 22$, dan ambil $L = 22 \times 1{,}40$ Å (rantai 22 atom karbon dengan panjang ikatan rata-rata, ditambah satu panjang ikatan untuk ujung-ujungnya). Bandingkan dengan 450 nm.

**Penyelesaian.** $L = 3{,}08$ nm. $\lambda = 8(9{,}109 \times 10^{-31})(2{,}998 \times 10^8)(3{,}08 \times 10^{-9})^2/[(6{,}626 \times 10^{-34})(23)] = 1{,}36 \times 10^{-6}$ m $= 1360$ nm.

**Memahami hasil.** Model elektron bebas, yang bekerja sangat baik untuk zat warna sianin (subbab 3.8) yang semua ikatannya setara, meleset tiga kali lipat untuk poliena. Pada sianin, muatan dan resonansi membuat ikatan tunggal dan rangkap sama panjang; pada poliena, ikatan berselang-seling (sekitar 1,35 dan 1,45 Å), dan potensial periodik yang ditimbulkannya membuka celah yang tidak menutup walaupun rantai sangat panjang. Model Hückel dengan dua nilai $\beta$ yang berbeda untuk ikatan tunggal dan rangkap menangkap efek ini. Perbandingan sianin dan poliena adalah contoh indah bagaimana struktur geometri menentukan warna.
:::

### Aturan Woodward–Fieser

Untuk diena dan enon terkonjugasi, Woodward (1941) dan Fieser menyusun aturan empiris yang meramalkan $\lambda_\text{maks}$ transisi π→π* dalam beberapa nanometer. Aturan untuk diena: nilai dasar 214 nm untuk diena asiklik atau heteroanular (kedua ikatan rangkap di cincin berbeda) dan 253 nm untuk diena homoanular (kedua ikatan rangkap dalam satu cincin), ditambah 30 nm untuk setiap ikatan rangkap terkonjugasi tambahan, 5 nm untuk setiap substituen alkil atau "sisa cincin" yang terikat pada atom karbon diena, dan 5 nm untuk setiap ikatan rangkap eksosiklik (yang menempel di luar suatu cincin). Untuk enon α,β-tak jenuh: nilai dasar 215 nm (asiklik atau cincin enam), ditambah 10 nm untuk substituen α, 12 nm untuk substituen β, 30 nm untuk perluasan konjugasi, dan 5 nm untuk ikatan rangkap eksosiklik.

Aturan ini bekerja karena setiap substituen alkil menaikkan HOMO sedikit melalui hiperkonjugasi, dan setiap ikatan rangkap tambahan menurunkan celah HOMO–LUMO dengan besaran yang hampir tetap untuk rantai pendek. Diena homoanular lebih merah karena geometri s-cis-nya membuat interaksi antarujung diena (yang memisahkan kombinasi orbital) berbeda dari geometri s-trans.

::: {.contoh}
**Contoh 15.38 · Meramalkan $\lambda_\text{maks}$**

Ramalkan $\lambda_\text{maks}$ untuk (a) kolesta-3,5-diena (diena heteroanular dengan tiga sisa cincin dan satu ikatan rangkap eksosiklik), (b) mesitil oksida, (CH₃)₂C=CH–CO–CH₃, dan (c) isoforon (3,5,5-trimetilsikloheks-2-enon: satu metil dan satu sisa cincin pada karbon β). Nilai teramati 235, 236, dan 235 nm.

**Penyelesaian.** (a) $214 + 3 \times 5 + 5 = 234$ nm. (b) Dua metil pada karbon β: $215 + 2 \times 12 = 239$ nm. (c) Dua substituen β: $215 + 2 \times 12 = 239$ nm.

**Memahami hasil.** Ramalan meleset 1–4 nm. Sebelum NMR tersedia, aturan Woodward–Fieser adalah alat utama untuk menentukan letak ikatan rangkap dalam steroid dan terpena: dua isomer yang berbeda letak ikatan rangkapnya sering berbeda $\lambda_\text{maks}$-nya 20–40 nm. Woodward kemudian memakai pengalaman ini dalam teori simetri orbital (subbab 13.11).
:::

### Pengaruh pelarut

Transisi n→π* bergeser ke **biru** (energi lebih tinggi) dalam pelarut polar dan protik. Pasangan elektron bebas oksigen karbonil membentuk ikatan hidrogen dengan pelarut, yang menurunkan energi orbital n; dalam keadaan tereksitasi, satu elektron n telah pindah ke π*, sehingga ikatan hidrogen melemah dan stabilisasinya hilang. Sebaliknya, transisi π→π* biasanya bergeser sedikit ke **merah** dalam pelarut polar, karena keadaan tereksitasi π,π* lebih polar daripada keadaan dasar dan distabilkan lebih banyak. Arah geseran pelarut dengan demikian membantu membedakan kedua jenis transisi.

::: {.contoh}
**Contoh 15.39 · Ikatan hidrogen dari geseran biru**

Pita n→π* aseton berada di 279 nm dalam heksana dan 265 nm dalam air. Hitung geseran energinya dalam cm⁻¹ dan kJ/mol. Apa arti fisisnya?

**Penyelesaian.** $10^7/265 - 10^7/279 = 37\,736 - 35\,842 = 1894$ cm⁻¹ $= 22{,}7$ kJ/mol.

**Memahami hasil.** Geseran 23 kJ/mol sebanding dengan energi ikatan hidrogen antara gugus karbonil dan air. Dalam tafsir sederhana, angka ini adalah stabilisasi ikatan hidrogen keadaan dasar yang hilang ketika elektron n tereksitasi. Geseran solvatokromik dengan demikian dapat dipakai untuk mengukur kekuatan interaksi zat terlarut–pelarut. Skala polaritas pelarut seperti $E_T(30)$ didasarkan pada geseran pita transfer muatan zat warna Reichardt, yang bergeser lebih dari 9000 cm⁻¹ dari pelarut nonpolar ke air.
:::

### Benzena dan senyawa aromatik

Tiga pita benzena (Tabel 15.2) berasal dari keadaan $^1B_{2u}$ (254 nm), $^1B_{1u}$ (204 nm), dan $^1E_{1u}$ (184 nm), yang semuanya berasal dari konfigurasi $e_{1g}^3e_{2u}^1$ (HOMO dan LUMO Hückel benzena yang berdegenerasi, subbab 13.7). Hanya transisi ke $^1E_{1u}$ yang diizinkan simetri; dua lainnya diamati berkat kopling vibronik dan karena itu lemah. Substituen yang merusak kesetangkupan (OH, NH₂, NO₂, C=O) memperkuat pita 254 nm dan menggesernya ke merah: fenol menyerap di sekitar 270 nm, anilina di sekitar 280 nm. Substituen pemberi elektron dan penarik elektron pada posisi para menghasilkan pita transfer muatan intramolekul yang kuat, prinsip yang dipakai untuk merancang zat warna dan indikator.

::: {.terapan}
**Indikator asam–basa**

Fenolftalein tidak berwarna dalam larutan asam: ketiga cincin aromatiknya terpisah oleh satu atom karbon sp³ yang memutus konjugasi, sehingga serapannya di ultraviolet. Dalam larutan basa (pH di atas sekitar 8,2), cincin lakton membuka, karbon pusat menjadi sp², dan ketiga cincin bergabung menjadi satu sistem π terkonjugasi bermuatan dengan pita serapan kuat di 552 nm: larutan menjadi merah muda keunguan. Prinsip yang sama, yaitu memutus atau menyambung konjugasi dengan mengubah hibridisasi satu atom, bekerja pada banyak indikator, zat warna fotokromik untuk lensa kacamata, dan sakelar molekul.
:::

::: {.kuis}
**Kuis cepat 15.9**

Ramalkan arah geseran pita n→π* benzofenona bila pelarut diganti dari sikloheksana ke etanol. Mengapa fenolftalein dalam larutan basa yang sangat pekat menjadi tidak berwarna lagi?
:::
