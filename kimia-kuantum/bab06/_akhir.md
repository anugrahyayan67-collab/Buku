# Ringkasan Bab 6

| Gagasan | Rumus | Subbab |
|---|---|---|
| Momentum sudut klasik | $\mathbf L = \mathbf r \times \mathbf p$; $\ E_\text{rot} = L^2/2I$; $\ \boldsymbol\mu = -(e/2m_e)\mathbf L$ | 6.1 |
| Komutator | $[\hat L_x, \hat L_y] = i\hbar\hat L_z$ (siklis); $\ [\hat L^2, \hat L_i] = 0$ | 6.2 |
| Bentuk bola | $\hat L_z = -i\hbar\partial_\phi$; $\ \nabla^2 = \tfrac{1}{r^2}\partial_r(r^2\partial_r) - \hat L^2/\hbar^2r^2$ | 6.2 |
| Partikel pada cincin | $\psi_m = e^{im\phi}/\sqrt{2\pi}$; $\ E_m = m^2\hbar^2/2I$; $\ m = 0, \pm1, \ldots$ | 6.3 |
| Partikel pada bola | $E_\ell = \ell(\ell + 1)\hbar^2/2I$; degenerasi $2\ell + 1$ | 6.4 |
| Legendre terasosiasi | $P_\ell^{|m|}(x) = (1 - x^2)^{|m|/2}\,d^{|m|}P_\ell/dx^{|m|}$; $\ |m| \le \ell$ | 6.4 |
| Harmonik bola | $Y_\ell^m = N_{\ell m}P_\ell^{|m|}(\cos\theta)e^{im\phi}$; paritas $(-1)^\ell$; $\ \sum_m|Y_\ell^m|^2 = (2\ell + 1)/4\pi$ | 6.5 |
| Model vektor | $\cos\theta_m = m/\sqrt{\ell(\ell+1)}$; $\ \langle L_x^2\rangle = \tfrac12[\ell(\ell+1) - m^2]\hbar^2$ | 6.6 |
| Operator tangga | $\hat L_\pm|\ell, m\rangle = \hbar\sqrt{\ell(\ell+1) - m(m \pm 1)}\,|\ell, m \pm 1\rangle$; $\ \ell = 0, \tfrac12, 1, \ldots$ | 6.7 |
| Dua benda | $\hat H = -\tfrac{\hbar^2}{2M}\nabla_R^2 - \tfrac{\hbar^2}{2\mu}\nabla_r^2 + V(r)$; $\ V_\text{ef} = V + \ell(\ell+1)\hbar^2/2\mu r^2$ | 6.8 |
| Rotor tegar | $F(J) = BJ(J + 1)$; $\ B = h/8\pi^2cI$; $\ I = \mu r^2$ | 6.9 |
| Spektrum rotasi | $\mu_0 \ne 0$; $\ \Delta J = \pm1$; $\ \tilde\nu = 2B(J + 1)$ | 6.10 |
| Populasi | $N_J/N_0 = (2J+1)e^{-hcBJ(J+1)/kT}$; $\ J_\text{maks} \approx \sqrt{kT/2hcB} - \tfrac12$; $\ q = kT/\sigma hcB$ | 6.11 |
| Distorsi sentrifugal | $F = BJ(J+1) - DJ^2(J+1)^2$; $\ D = 4B^3/\tilde\omega^2$ | 6.12 |
| Rotasi–getaran | $B_v = B_e - \alpha_e(v + \tfrac12)$; $\ R(J-1) - P(J+1) = 4B_0(J + \tfrac12)$ | 6.12 |

**Jawaban kuis cepat.** **6.1** Dalam atom hidrogen gaya pada elektron sentral terhadap inti; dalam H₂⁺ elektron ditarik dua inti, sehingga gayanya tidak sentral terhadap salah satu inti (yang kekal hanya komponen sepanjang sumbu molekul). **6.2** Tidak (kecuali $\ell = 0$); ya; karena $\hat L^2$ hanya memutar fungsi, dan rotasi tidak mengubah jarak dari titik asal. **6.3** Tidak ada daerah terbatas yang memaksa fungsi gelombang melengkung; keadaan $m = 0$ yang tetap diizinkan karena posisi sudutnya sama sekali tidak tentu; 14 elektron. **6.4** Tujuh ($\ell = 3$); karena turunan ke-$|m|$ polinom berderajat $\ell$ nol bila $|m| > \ell$. **6.5** Satu bidang simpul ($|m| = 1$) dan dua kerucut ($\ell - |m| = 2$); ganjil. **6.6** Tujuh; $\tfrac12(12 - 9)\hbar^2 = \tfrac32\hbar^2$. **6.7** Nol; $2\hbar|2, 1\rangle$; karena $e^{i\phi/2}$ berubah tanda setelah satu putaran, sehingga fungsi gelombang tidak bernilai tunggal. **6.8** Massa tereduksi He⁺ lebih dekat ke $m_e$ daripada H, sehingga tetapan Rydberg-nya sedikit lebih besar dan frekuensinya sedikit lebih dari empat kali (pergeseran ke biru). **6.9** Sembilan; $20B$; $B$ menjadi seperempatnya. **6.10** H₂ tidak mempunyai momen dipol permanen; $B = 1{,}5$ cm⁻¹. **6.11** DCl, karena $B$-nya lebih kecil; karena inti ¹⁶O berspin nol, sehingga tingkat $J$ genap O₂ sama sekali tidak ada. **6.12** Karena gaya sentrifugal selalu meregangkan ikatan, memperbesar $I$, dan menurunkan energi; tingkat atas yang sama ($v = 1$, $J$).

# Pertanyaan

1. Mengapa momentum sudut menjadi besaran yang "baik" (kekal) dalam atom, dan apa akibatnya bagi pelabelan orbital?
2. Mengapa tidak ada keadaan dengan $L_x$, $L_y$, dan $L_z$ semuanya tajam, kecuali $\mathbf L = 0$?
3. Bandingkan asal kuantisasi pada partikel dalam kotak dan partikel pada cincin.
4. Mengapa partikel pada cincin tidak mempunyai energi titik nol, sedangkan osilator harmonik mempunyai?
5. Bagaimana model elektron pada cincin menjelaskan aturan $4n + 2$? Apa keterbatasannya?
6. Mengapa deret Legendre harus berhenti, dan bagaimana syarat itu menghasilkan bilangan kuantum $\ell$?
7. Mengapa energi partikel pada bola tidak bergantung pada $m$? Kapan degenerasi ini pecah?
8. Apa hubungan antara harmonik bola dan nama orbital $p_x$, $d_{xy}$, $d_{z^2}$?
9. Mengapa orbital riil dan orbital kompleks sama-sama sah? Kapan masing-masing lebih berguna?
10. Mengapa subkulit penuh berbentuk bola, padahal setiap orbitalnya berarah?
11. Apa arti kuantisasi ruang? Mengapa vektor momentum sudut tidak pernah sejajar sumbu $z$?
12. Bagaimana operator tangga menunjukkan bahwa nilai setengah bulat diizinkan? Mengapa momentum sudut orbital tetap bulat?
13. Bagaimana pemisahan masalah dua benda memungkinkan kita memakai hasil partikel pada bola untuk molekul diatom?
14. Apa peran potensial efektif sentrifugal dalam atom dan molekul?
15. Mengapa jarak antargaris rotasi molekul diatom hampir sama? Apa yang membuatnya tidak tepat sama?
16. Mengapa hanya molekul polar yang mempunyai spektrum rotasi murni, tetapi semua molekul (kecuali yang bersimetri bola) mempunyai spektrum Raman rotasi?
17. Bagaimana suhu gas antarbintang ditentukan dari garis rotasi?
18. Mengapa hidrogen mempunyai bentuk orto dan para, dan mengapa konversinya penting bagi penyimpanan hidrogen cair?
19. Apa perbedaan $r_0$ dan $r_e$? Mana yang harus dibandingkan dengan perhitungan kuantum?
20. Bagaimana spektrum rotasi–getaran memberi tetapan rotasi dua tingkat getaran sekaligus?
21. Bagaimana teka-teki pembuka bab (panjang ikatan CO dari satu frekuensi radio) terjawab oleh teori bab ini?

# Soal

%%SOAL%%

# Jawaban

%%JAWABAN%%

# Pembahasan soal terpilih

**Soal {{bumi}}.** $I = 0{,}331(5{,}97 \times 10^{24})(6{,}371 \times 10^6)^2 = 8{,}02 \times 10^{37}$ kg m², $\omega = 2\pi/86\,164 = 7{,}29 \times 10^{-5}$ rad/s, $L = I\omega = 5{,}85 \times 10^{33}$ J s $= 5{,}5 \times 10^{67}\,\hbar$. Untuk $\ell$ sebesar ini, sudut terkecil memenuhi $\cos\theta = \ell/\sqrt{\ell(\ell+1)} \approx 1 - 1/2\ell$, sehingga $\theta \approx 1/\sqrt\ell \approx 10^{-34}$ rad.

*Cara berpikir:* kuantisasi ruang tetap berlaku untuk Bumi, tetapi celah antarorientasi sekitar $10^{-34}$ rad tidak mungkin diamati. Sifat kuantum momentum sudut hanya tampak bila $\ell$ kecil, yaitu bila momentum sudut hanya beberapa kali $\hbar$: elektron dalam atom dan molekul yang berputar lambat.

**Soal {{cincin}}.** Koefisien dalam basis $\psi_m = e^{im\phi}/\sqrt{2\pi}$: $c_1 = 1/\sqrt5$, $c_2 = 2/\sqrt5$, karena $\psi = (\psi_1 + 2\psi_2)\sqrt{2\pi}/\sqrt{10\pi}$. Peluang $\tfrac15$ dan $\tfrac45$. $\langle L_z\rangle = \tfrac15\hbar + \tfrac45(2\hbar) = \tfrac95\hbar$. $\langle E\rangle = \left[\tfrac15(1) + \tfrac45(4)\right]\tfrac{\hbar^2}{2I} = \tfrac{17}{5}\cdot\tfrac{\hbar^2}{2I}$.

*Cara berpikir:* rapat peluangnya $|\psi|^2 = [5 + 4\cos\phi]/10\pi$, tidak seragam, dan berputar terhadap waktu karena kedua komponen berenergi berbeda (frekuensi Bohr $3\hbar/2I$). Paket gelombang pada cincin berputar, persis seperti paket osilator berayun (subbab 5.5).

**Soal {{legendre}}.** Dengan $x = \cos\theta$: $\tfrac{d}{d\theta} = \tfrac{dx}{d\theta}\tfrac{d}{dx} = -\sin\theta\tfrac{d}{dx}$. Maka $\sin\theta\tfrac{d\Theta}{d\theta} = -\sin^2\theta\tfrac{d\Theta}{dx} = -(1 - x^2)\Theta'$, dan $\tfrac{1}{\sin\theta}\tfrac{d}{d\theta}[\cdots] = \tfrac{1}{\sin\theta}(-\sin\theta)\tfrac{d}{dx}[-(1 - x^2)\Theta'] = \tfrac{d}{dx}[(1 - x^2)\Theta'] = (1 - x^2)\Theta'' - 2x\Theta'$. Suku $m^2/\sin^2\theta$ menjadi $m^2/(1 - x^2)$. Hasilnya (6.13).

*Cara berpikir:* substitusi $x = \cos\theta$ mengubah sudut menjadi selang $[-1, 1]$ dan elemen $\sin\theta\,d\theta$ menjadi $-dx$. Titik $x = \pm1$ (kutub) adalah titik singular persamaan; perilaku di sana yang memaksa kuantisasi.

**Soal {{unsold}}.** Dengan $c = \cos\theta$, $s = \sin\theta$: $|Y_2^0|^2 = \tfrac{5}{16\pi}(3c^2 - 1)^2$; $|Y_2^1|^2 + |Y_2^{-1}|^2 = 2\cdot\tfrac{15}{8\pi}s^2c^2$; $|Y_2^2|^2 + |Y_2^{-2}|^2 = 2\cdot\tfrac{15}{32\pi}s^4$. Kalikan semuanya dengan $16\pi/5$: $(3c^2 - 1)^2 + 12s^2c^2 + 3s^4$. Dengan $s^2 = 1 - c^2$: $9c^4 - 6c^2 + 1 + 12c^2 - 12c^4 + 3 - 6c^2 + 3c^4 = 4$. Jadi jumlahnya $4 \cdot 5/16\pi = 5/4\pi$.

*Cara berpikir:* subkulit d¹⁰ (misalnya dalam Zn²⁺ atau Cu⁺) bersimetri bola. Ion logam transisi dengan subkulit d sebagian terisi tidak bersimetri bola, dan anisotropi itulah yang menjadi pokok teori medan kristal (Bab 14).

**Soal {{tangga1}}.** $\hat L_-\cos\theta = \hbar e^{-i\phi}(-\partial_\theta\cos\theta + 0) = \hbar e^{-i\phi}\sin\theta$. Jadi $\hat L_-Y_1^0 = \sqrt{\tfrac{3}{4\pi}}\hbar\sin\theta\,e^{-i\phi} = \sqrt2\,\hbar\sqrt{\tfrac{3}{8\pi}}\sin\theta\,e^{-i\phi} = \sqrt2\,\hbar Y_1^{-1}$.

*Cara berpikir:* faktor $\sqrt2 = \sqrt{1\cdot2 - 0\cdot(-1)}$ cocok dengan (6.23), dan $Y_1^{-1}$ bertanda positif dalam konvensi Condon–Shortley, sedangkan $Y_1^1$ bertanda negatif. Konvensi fase ini penting ketika momentum sudut digabungkan (koefisien Clebsch–Gordan, Bab 9).

**Soal {{muon}}.** $\mu = m_\mu m_p/(m_\mu + m_p)$ dengan $m_p = 1836{,}15\,m_e$: $\mu = 185{,}84\,m_e$. Energi sebanding dengan $\mu$: $E_1 = -\tfrac12(185{,}84)(27{,}211\ \text{eV}) = -2{,}53$ keV. Jari-jari berbanding terbalik dengan $\mu$: $a = a_0/185{,}84 = 285$ fm.

*Cara berpikir:* muon mengorbit 186 kali lebih dekat ke proton daripada elektron, cukup dekat untuk "merasakan" ukuran proton (sekitar 0,84 fm). Pengukuran spektrum hidrogen muonik tahun 2010 memberi jari-jari proton yang 4% lebih kecil daripada nilai sebelumnya, memicu "teka-teki jari-jari proton" yang kemudian diselesaikan dengan pengukuran hidrogen biasa yang lebih teliti.

**Soal {{ocs}}.** Momen inersia: $I = h/(8\pi^2B)$ dengan $B$ dalam Hz. $I_{32} = 1{,}3800 \times 10^{-45}$ dan $I_{34} = 1{,}4146 \times 10^{-45}$ kg m². Untuk molekul linear O–C–S dengan jarak $r_1 = r(\text{CO})$ dan $r_2 = r(\text{CS})$, $I = \sum m_ix_i^2 - (\sum m_ix_i)^2/M$ dengan $x_O = -r_1$, $x_C = 0$, $x_S = r_2$. Dua persamaan dengan dua bilangan tak diketahui diselesaikan secara numerik: $r_1 = 116{,}3$ pm, $r_2 = 156{,}0$ pm.

*Cara berpikir:* satu tetapan rotasi hanya memberi satu momen inersia; untuk molekul dengan $n$ panjang ikatan tak diketahui diperlukan $n$ isotopolog. Karena $r_0$ setiap isotopolog sedikit berbeda (getaran titik nol), hasilnya tidak tepat sama dengan $r_e$; metode substitusi Kraitchman memakai selisih momen inersia untuk mengurangi galat ini.

**Soal {{orto}}.** Deuteron adalah boson (spin 1), sehingga fungsi gelombang total harus simetris terhadap pertukaran. Dua spin 1 menghasilkan $3 \times 3 = 9$ keadaan: 6 simetris dan 3 antisimetris. $J$ genap (rotasi simetris) berpasangan dengan 6 keadaan spin simetris (orto-D₂); $J$ ganjil berpasangan dengan 3 keadaan antisimetris (para-D₂). Pada suhu tinggi orto : para = 6 : 3 = 2 : 1.

*Cara berpikir:* untuk H₂ (fermion) perbandingan dan pasangan $J$-nya terbalik: orto (berbobot 3) dengan $J$ ganjil. Pada suhu sangat rendah, D₂ dalam kesetimbangan semuanya orto ($J = 0$), sedangkan H₂ semuanya para ($J = 0$). Nama "orto" selalu menunjuk bentuk dengan bobot spin lebih besar.

**Soal {{kombinasi}}.** Dengan (6.38) untuk $J = 1$: $R(0) - P(2) = 2147{,}08 - 2135{,}55 = 11{,}535 = 4B_0(1{,}5)$, jadi $B_0 = 1{,}9225$ cm⁻¹; $R(1) - P(1) = 2150{,}86 - 2139{,}43 = 11{,}43 = 4B_1(1{,}5)$, jadi $B_1 = 1{,}905$ cm⁻¹.

*Cara berpikir:* kedua tetapan kembali tepat, karena (6.38) eksak untuk rumus (6.37). Dengan data sungguhan, selisih kombinasi untuk banyak $J$ dicocokkan bersama, dan distorsi sentrifugal ditambahkan sebagai suku $-8D(J + \tfrac12)^3$.

**Soal {{kratzer}}.** Molekul berputar dengan momentum sudut $L$; energi totalnya $E(r) = L^2/2\mu r^2 + \tfrac12k(r - r_e)^2$. Kesetimbangan baru: $dE/dr = -L^2/\mu r^3 + k(r - r_e) = 0$, sehingga $\delta r = r - r_e \approx L^2/\mu r_e^3k$. Masukkan ke $E$ dengan $1/r^2 \approx (1 - 2\delta r/r_e)/r_e^2$:

$$
E \approx \frac{L^2}{2\mu r_e^2} - \frac{L^2\delta r}{\mu r_e^3} + \tfrac12k\delta r^2 = \frac{L^2}{2I} - \frac{L^4}{2\mu^2r_e^6k} .
$$

Dengan $L^2 = J(J+1)\hbar^2$, $\mu^2r_e^6 = I^2r_e^2$ dan $k = \mu\omega^2$, koreksinya $-\hbar^4J^2(J+1)^2/(2I^3\omega^2)$. Dalam cm⁻¹, memakai $\hbar/I = 4\pi cB$ dan $\omega = 2\pi c\tilde\omega$: $D = \hbar(4\pi cB)^3/(2hc(2\pi c\tilde\omega)^2) = 4B^3/\tilde\omega^2$.

*Cara berpikir:* distorsi sentrifugal adalah kopling antara rotasi dan getaran: rotasi meregangkan pegas getaran. Karena $D$ hanya bergantung pada $B$ dan $\tilde\omega$, pengukuran $D$ dari spektrum gelombang mikro memberi frekuensi getaran tanpa spektroskopi IR, dan sebaliknya memberi uji konsistensi data.

# Bacaan lanjut

1. I. N. Levine, *Quantum Chemistry*, edisi ke-7 (Pearson, 2014), Bab 5 dan 6. Momentum sudut, harmonik bola, rotor tegar, dan pemisahan masalah dua benda.
2. D. A. McQuarrie, *Quantum Chemistry*, edisi ke-2 (University Science Books, 2008), Bab 6. Rotor tegar dan spektroskopi rotasi dengan banyak data numerik.
3. P. Atkins dan R. Friedman, *Molecular Quantum Mechanics*, edisi ke-5 (Oxford University Press, 2011), Bab 4. Momentum sudut dengan pendekatan operator dan model vektor.
4. R. N. Zare, *Angular Momentum* (Wiley, 1988). Rujukan lengkap tentang aljabar momentum sudut dan penerapannya dalam kimia dan spektroskopi.
5. W. Gordy dan R. L. Cook, *Microwave Molecular Spectra*, edisi ke-3 (Wiley, 1984). Spektroskopi gelombang mikro, penentuan struktur, dan distorsi sentrifugal.
6. P. F. Bernath, *Spectra of Atoms and Molecules*, edisi ke-3 (Oxford University Press, 2016), Bab 6 dan 7. Spektroskopi rotasi dan rotasi–getaran dengan contoh dari astronomi dan atmosfer.
