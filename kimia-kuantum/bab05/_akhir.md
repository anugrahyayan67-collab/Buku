# Ringkasan Bab 5

| Gagasan | Rumus | Subbab |
|---|---|---|
| Osilator klasik | $\omega = \sqrt{k/\mu}$; $\ E = \tfrac12kA^2$; $\ P(x) = 1/\pi\sqrt{A^2 - x^2}$ | 5.1 |
| Massa tereduksi | $\mu = m_Am_B/(m_A + m_B)$ | 5.1, 5.7 |
| Persamaan Schrödinger | $-\tfrac{\hbar^2}{2\mu}\psi'' + \tfrac12\mu\omega^2x^2\psi = E\psi$; $\ \xi = \sqrt\alpha\,x$, $\ \alpha = \mu\omega/\hbar$ | 5.2 |
| Tingkat energi | $E_v = (v + \tfrac12)\hbar\omega$, $\ v = 0, 1, 2, \ldots$ | 5.3 |
| Fungsi gelombang | $\psi_v = N_vH_v(\xi)e^{-\xi^2/2}$; $\ v$ simpul; paritas $(-1)^v$ | 5.3 |
| Rekursi Hermite | $H_{n+1} = 2\xi H_n - 2nH_{n-1}$; $\ H_n' = 2nH_{n-1}$ | 5.3 |
| Energi titik nol | $E_0 = \tfrac12\hbar\omega$; $\ D_0 = D_e - E_0$ | 5.4 |
| Fungsi partisi getaran | $q = 1/(1 - e^{-\hbar\omega/kT})$ | 5.4 |
| Nilai harap | $\langle x^2\rangle = \tfrac{\hbar}{\mu\omega}(v + \tfrac12)$; $\ \langle T\rangle = \langle V\rangle = \tfrac12E_v$ | 5.5 |
| Operator tangga | $\hat H = \hbar\omega(\hat a^\dagger\hat a + \tfrac12)$; $\ [\hat a, \hat a^\dagger] = 1$; $\ \hat a^\dagger|v\rangle = \sqrt{v + 1}|v + 1\rangle$ | 5.6 |
| Unsur matriks posisi | $\langle v'|x|v\rangle = \sqrt{\tfrac{\hbar}{2\mu\omega}}(\sqrt v\,\delta_{v',v-1} + \sqrt{v + 1}\,\delta_{v',v+1})$ | 5.6 |
| Tetapan gaya | $k = \mu(2\pi c\tilde\nu)^2$ | 5.7 |
| Aturan seleksi IR | $d\mu/dx \ne 0$; $\ \Delta v = \pm1$ (harmonik) | 5.8 |
| Anharmonisitas | $G(v) = \omega_e(v + \tfrac12) - \omega_ex_e(v + \tfrac12)^2$; $\ \Delta G_{v+1/2} = \omega_e - 2\omega_ex_e(v + 1)$ | 5.9 |
| Morse; Birge–Sponer | $V = D_e[1 - e^{-a(r - r_e)}]^2$; $\ k = 2D_ea^2$; $\ D_e = \omega_e^2/4\omega_ex_e$ | 5.9 |
| Efek isotop | $\omega \propto \mu^{-1/2}$; $\ \omega_ex_e \propto \mu^{-1}$; $\ k_H/k_D \approx e^{\Delta E_0/kT}$ | 5.10 |
| Mode normal | $3N - 6$ (tak linear), $3N - 5$ (linear); $\ E_0 = \tfrac12\sum_k\hbar\omega_k$ | 5.11 |
| Numerov | $\psi_{i+1} = [(12 - 10f_i)\psi_i - f_{i-1}\psi_{i-1}]/f_{i+1}$, $\ f = 1 - \tfrac{h^2}{12}g$ | 5.12 |

**Jawaban kuis cepat.** **5.1** Frekuensi turun dengan faktor $\sqrt2$, karena massa tereduksi berlipat dua. **5.2** Karena $e^{+\xi^2/2}$ tumbuh tanpa batas dan tidak dapat dinormalisasi. **5.3** Tujuh simpul; ganjil. **5.4** Sama: semua selisih bernilai $\hbar\omega$. **5.5** Di $\xi = 0$. Rapat klasik sebanding dengan waktu yang dihabiskan di setiap titik, dan partikel klasik melewati setiap titik di dalam daerah gerak dengan kecepatan berhingga, sehingga waktunya tidak pernah nol. **5.6** Nol; $3\psi_3$; karena nilai eigennya adalah bilangan kuanta $v$. **5.7** Setengah; H₂. **5.8** Ya, tetapi sangat lemah: intensitas sebanding dengan kuadrat turunan dipol, yang pada HD sekitar $10^{-5}$ sampai $10^{-6}$ kali HCl. **5.9** Lebih kecil, karena anharmonisitas menurunkan semua tingkat; nada atas hanya muncul melalui anharmonisitas dan suku tak linear dipol, yang kecil. **5.10** O–D, karena energi titik nolnya lebih rendah; ikatan hidrogen O–D···O sedikit lebih kuat karena alasan yang sama. **5.11** 18 dan 24; karena rotasi terhadap sumbu molekul linear bukan derajat kebebasan yang memindahkan inti, sehingga satu koordinat lagi menjadi getaran. **5.12** Persamaannya orde dua sehingga memerlukan dua syarat awal; persamaan linear, sehingga mengalikan $\psi_1$ dengan tetapan hanya mengalikan seluruh fungsi dengan tetapan yang sama, yang dihilangkan oleh normalisasi.

# Pertanyaan

## Subbab 5.1: Osilator klasik

1. Mengapa hampir setiap potensial di dekat minimumnya dapat didekati dengan parabola? Kapan pendekatan ini gagal?
2. Apa arti fisis massa tereduksi? Mengapa untuk HI ia hampir sama dengan massa atom H?

## Subbab 5.3: Penyelesaian deret dan polinom Hermite

3. Mengapa syarat kenormalan menghasilkan kuantisasi energi osilator? Bandingkan dengan syarat batas pada partikel dalam kotak.

## Subbab 5.4: Tingkat energi dan energi titik nol

4. Mengapa tingkat energi osilator berjarak sama, sedangkan tingkat kotak makin renggang dan tingkat atom hidrogen makin rapat?
5. Mengapa energi titik nol tidak dapat dihilangkan dengan pendinginan? Hubungkan dengan asas ketidakpastian.
6. Mengapa $D_0$ dan bukan $D_e$ yang diukur dalam percobaan termokimia?

## Subbab 5.5: Fungsi gelombang: kuantum vs klasik

7. Di mana partikel kuantum paling mungkin ditemukan pada keadaan dasar, dan di mana partikel klasik? Mengapa berbeda?
8. Apa arti penembusan ke daerah terlarang secara klasik? Apakah energi kinetik di sana negatif?

## Subbab 5.6: Operator tangga

9. Mengapa metode operator tangga tidak memerlukan penyelesaian persamaan diferensial? Apa yang memastikan tangga berhenti di bawah?

## Subbab 5.7: Getaran molekul diatom dan massa tereduksi

10. Mengapa frekuensi getaran ditentukan oleh perbandingan $k/\mu$, dan bagaimana ini menjelaskan pita ulur X–H yang tinggi?

## Subbab 5.8: Aturan seleksi inframerah

11. Mengapa molekul diatom homonuklir tidak aktif IR, tetapi aktif Raman?
12. Mengapa spektrum IR gas HCl berupa deretan garis, bukan satu garis? Mengapa pusat pita kosong?
13. Bagaimana anharmonisitas tampak dalam spektrum IR? Sebutkan dua akibatnya.

## Subbab 5.9: Anharmonisitas dan potensial Morse

14. Mengapa ekstrapolasi Birge–Sponer cenderung melebih-lebihkan energi disosiasi?

## Subbab 5.10: Efek isotop

15. Apa peran aproksimasi Born–Oppenheimer dalam efek isotop? Apa yang sama dan apa yang berbeda pada H₂ dan D₂?
16. Mengapa efek isotop kinetik menurun bila suhu naik?
17. Mengapa obat terdeuterasi dapat bertahan lebih lama dalam tubuh?

## Subbab 5.11: Mode normal molekul poliatom

18. Apa itu mode normal, dan mengapa konsep ini mengubah masalah banyak atom menjadi kumpulan osilator terpisah?
19. Mengapa molekul besar menunjukkan frekuensi gugus yang khas, padahal mode normalnya melibatkan semua atom?

## Subbab 5.12: Penyelesaian numerik: metode Numerov

20. Apa keunggulan metode Numerov dibandingkan beda hingga biasa? Bagaimana metode tembak menemukan nilai eigen?
21. Bagaimana teka-teki pembuka bab (perbedaan H₂O dan D₂O) terjawab oleh teori bab ini?

# Soal

%%SOAL%%

# Jawaban

%%JAWABAN%%

# Pembahasan soal terpilih

**Soal {{dua}}.** Dari definisi $\mathbf R$ dan $\mathbf r$: $\mathbf r_A = \mathbf R + \tfrac{m_B}{M}\mathbf r$ dan $\mathbf r_B = \mathbf R - \tfrac{m_A}{M}\mathbf r$. Turunkan terhadap waktu dan masukkan:

$$
\tfrac12m_A\left(\dot{\mathbf R} + \tfrac{m_B}{M}\dot{\mathbf r}\right)^2 + \tfrac12m_B\left(\dot{\mathbf R} - \tfrac{m_A}{M}\dot{\mathbf r}\right)^2 = \tfrac12M\dot{\mathbf R}^2 + \left(\tfrac{m_Am_B}{M} - \tfrac{m_Bm_A}{M}\right)\dot{\mathbf R}\cdot\dot{\mathbf r} + \tfrac12\,\frac{m_Am_B(m_B + m_A)}{M^2}\,\dot{\mathbf r}^2 .
$$

Suku tengah nol dan koefisien suku terakhir adalah $m_Am_B/M = \mu$.

*Cara berpikir:* pemisahan ini berlaku untuk energi kinetik dan, karena potensial hanya bergantung pada $\mathbf r$, untuk Hamiltonian seluruhnya. Dalam mekanika kuantum hasilnya sama: $\hat H = \hat H_\text{pm} + \hat H_\text{rel}$, dan fungsi gelombang menjadi hasil kali (pemisahan variabel, subbab 4.4). Atom hidrogen di Bab 7 dipisahkan dengan cara yang sama, dengan $\mu$ elektron–proton.

**Soal {{hermit3}}.** Dari (5.11) dengan $\varepsilon = 7$: $a_3 = \tfrac{2(1) + 1 - 7}{(2)(3)}a_1 = -\tfrac23$, lalu $a_5 = \tfrac{2(3) + 1 - 7}{(4)(5)}a_3 = 0$, dan semua koefisien berikutnya nol. Polinomnya $\xi - \tfrac23\xi^3 = -\tfrac{1}{12}(8\xi^3 - 12\xi) = -\tfrac{1}{12}H_3$.

*Cara berpikir:* pemilihan $\varepsilon = 2v + 1$ membuat pembilang rekursi nol tepat pada $k = v$, sehingga deret "dipotong" menjadi polinom. Normalisasi menentukan tetapan pengali; konvensi Hermite memilih koefisien pangkat tertinggi $2^v$.

**Soal {{zpe}}.** $G(0) = \tfrac12\omega_e - \tfrac14\omega_ex_e = 1495{,}48 - 13{,}21 = 1482{,}27$ cm⁻¹ $= 0{,}1838$ eV. $D_0 = 4{,}618 - 0{,}184 = 4{,}434$ eV.

*Cara berpikir:* nilai termokimia $D_0(\text{HCl}) = 4{,}434$ eV (427,8 kJ/mol) cocok. Energi titik nol menyumbang 4% energi ikatan; untuk perbandingan dengan ketelitian kimia (4 kJ/mol), koreksi ini tidak boleh diabaikan, dan program kimia komputasi menambahkannya secara otomatis (koreksi ZPE, Bab 17).

**Soal {{tangga}}.** $\hat x^2 = \tfrac{\hbar}{2\mu\omega}(\hat a + \hat a^\dagger)^2 = \tfrac{\hbar}{2\mu\omega}(\hat a^2 + \hat a^{\dagger2} + \hat a\hat a^\dagger + \hat a^\dagger\hat a)$. Suku $\hat a^2$ dan $\hat a^{\dagger2}$ mengubah $v$ sebesar 2, sehingga unsur diagonalnya nol. $\langle v|\hat a^\dagger\hat a|v\rangle = v$ dan $\langle v|\hat a\hat a^\dagger|v\rangle = v + 1$. Jadi $\langle v|x^2|v\rangle = \tfrac{\hbar}{2\mu\omega}(2v + 1)$. Dengan $\hat p = i\sqrt{\mu\hbar\omega/2}(\hat a^\dagger - \hat a)$, $\hat p^2 = -\tfrac{\mu\hbar\omega}{2}(\hat a^{\dagger2} + \hat a^2 - \hat a^\dagger\hat a - \hat a\hat a^\dagger)$, dan unsur diagonalnya $\tfrac{\mu\hbar\omega}{2}(2v + 1)$.

*Cara berpikir:* tanpa satu integral pun, kita mendapat (5.16) dan teorema virial: $\langle p^2\rangle/2\mu = \tfrac12\mu\omega^2\langle x^2\rangle = \tfrac12E_v$. Setiap unsur matriks pangkat $x$ dan $p$ dapat dihitung dengan "menghitung jalan" di tangga.

**Soal {{bs}}.** Garis lurus terbaik melalui lima titik $(v + 1, \Delta G)$ adalah $\Delta G = 4387{,}5 - 229{,}7(v + 1)$. Dengan (5.25): $\omega_e = 4387{,}5$ cm⁻¹ dan $\omega_ex_e = 114{,}9$ cm⁻¹. Birge–Sponer: $D_e = \omega_e^2/4\omega_ex_e = 41\,901$ cm⁻¹ $= 5{,}20$ eV; $G(0) = 2165{,}0$ cm⁻¹; $D_0 = 39\,736$ cm⁻¹ $= 4{,}93$ eV, 10% di atas nilai sebenarnya.

*Cara berpikir:* grafik $\Delta G$ terhadap $v$ untuk H₂ sebenarnya melengkung ke bawah pada $v$ tinggi (tingkat-tingkat atas lebih rapat daripada ramalan linear), sehingga garis lurus dari lima titik pertama memberi luas yang terlalu besar. Inilah keterbatasan umum ekstrapolasi Birge–Sponer: hasilnya batas atas, dan makin sedikit tingkat yang terukur, makin besar kesalahannya (bandingkan dengan I₂, yang meleset 49%).

**Soal {{kie}}.** Dari Contoh 5.42, $\Delta E_0 = 385{,}4$ cm⁻¹. Syaratnya $hc\Delta E_0/kT = \ln 3$, jadi $T = (385{,}4)(1{,}4388\ \text{cm K})/1{,}0986 = 505$ K.

*Cara berpikir:* efek isotop kinetik turun dari 6,4 pada 298 K ke 3 pada 505 K. Ketergantungan suhu ini diuji dalam percobaan: bila $k_H/k_D$ mengikuti (5.31), model energi titik nol sudah cukup; bila efeknya jauh lebih besar dan hampir tidak bergantung suhu, penerobosan berperan.

**Soal {{hdo}}.** $2E_0(\text{HDO}) = 2727 + 1402 + 3707 = 7836$ cm⁻¹; $E_0(\text{H}_2\text{O}) + E_0(\text{D}_2\text{O}) = 4504 + 3318{,}5 = 7822{,}5$ cm⁻¹. $\Delta E_0 = 13{,}5$ cm⁻¹ $= 0{,}16$ kJ/mol. $K \approx 4e^{-13{,}5 \times 1{,}4388/298{,}15} = 4 \times 0{,}937 = 3{,}75$.

*Cara berpikir:* nilai terukur sekitar 3,8, sangat dekat dengan faktor statistik 4: energi titik nol campuran hampir aditif. Bandingkan dengan H₂ + D₂ (Contoh 5.43), tempat penyimpangannya jauh lebih besar karena hanya ada satu mode dan isotopnya mengubah massa tereduksi hampir dua kali lipat. Untuk kimia air berat, akibatnya praktis: dalam campuran H₂O dan D₂O, sebagian besar deuterium berada sebagai HDO.

**Soal {{fermi}}.** Nilai eigen matriks $\begin{pmatrix}E_1 & W\\ W & E_2\end{pmatrix}$ adalah $\bar E \pm \tfrac12\sqrt{\Delta^2 + 4W^2}$, dengan $\Delta = E_1 - E_2$. Pemisahan teramati $1388 - 1285 = 103$ cm⁻¹ $= \sqrt{\Delta^2 + 4W^2}$. (a) $\Delta = 0$: $W = 51{,}5$ cm⁻¹. (b) $\Delta = 10$: $W = \tfrac12\sqrt{103^2 - 10^2} = 51{,}3$ cm⁻¹.

*Cara berpikir:* bila kedua tingkat hampir berdegenerasi, pemisahan teramati praktis $2W$ dan kedua tingkat tercampur hampir 50 : 50. Karena itu kedua pita Raman hampir sama kuat, meskipun hanya satu di antaranya ($v_1 = 1$) yang "seharusnya" aktif Raman: intensitas dipinjam melalui pencampuran. Gejala peminjaman intensitas ini muncul lagi dalam spektroskopi elektronik (Bab 15).

**Soal {{aba}}.** Misalkan simpangan $x_1$ (A kiri), $x_2$ (B), $x_3$ (A kanan); $V = \tfrac12k(x_2 - x_1)^2 + \tfrac12k(x_3 - x_2)^2$. Ulur simetris: $x_3 = -x_1$, $x_2 = 0$; persamaan gerak atom A: $m_A\ddot x_1 = -k(x_1 - x_2) = -kx_1$, jadi $\omega_\text{sim} = \sqrt{k/m_A}$; atom B tidak bergerak. Ulur asimetris: $x_3 = x_1$, dan pusat massa diam, $2m_Ax_1 + m_Bx_2 = 0$, sehingga $x_2 = -2m_Ax_1/m_B$. Maka $m_A\ddot x_1 = k(x_2 - x_1) = -k(1 + 2m_A/m_B)x_1$, jadi $\omega_\text{asim}^2 = k(1/m_A + 2/m_B)$. Perbandingan $\omega_\text{asim}/\omega_\text{sim} = \sqrt{1 + 2m_A/m_B} = \sqrt{1 + 2(15{,}995)/12} = 1{,}915$, sehingga ramalannya $1333 \times 1{,}915 = 2552$ cm⁻¹.

*Cara berpikir:* nilai terukur 2349 cm⁻¹, 8% lebih rendah. Selisihnya menunjukkan bahwa kedua ikatan C=O tidak bebas: ada tetapan gaya **interaksi** $k_{12}$ yang membuat peregangan satu ikatan melemahkan yang lain. Selain itu, 1333 cm⁻¹ sendiri adalah nilai rata-rata pasangan resonansi Fermi (soal {{fermi}}). Medan gaya dengan suku silang inilah yang ditentukan oleh analisis koordinat normal dan dihitung langsung oleh program kimia komputasi.

**Soal {{numerov}}.** Dengan $V = x^4$, selang $[-5, 5]$, dan 2001 titik, pencarian bagi dua memberi $E_0 = 0{,}6680$, $E_1 = 2{,}3936$, $E_2 = 4{,}6968$ (dan $E_3 = 7{,}3357$).

*Cara berpikir:* selisih antartingkat **membesar** (1,73; 2,30; 2,64), berbeda dengan osilator harmonik. Untuk potensial $V \propto |x|^n$, tingkat-tingkat tinggi berskala $E_v \propto v^{2n/(n+2)}$: $n = 1$ memberi $v^{2/3}$ (makin rapat), $n = 2$ memberi $v$ (berjarak sama), $n = 4$ memberi $v^{4/3}$, dan $n \to \infty$ (dinding kotak) memberi $v^2$. Osilator harmonik adalah satu-satunya kasus yang berjarak sama: kasus perbatasan antara kotak dan sumur yang melandai.

# Bacaan lanjut

1. I. N. Levine, *Quantum Chemistry*, edisi ke-7 (Pearson, 2014), Bab 4. Osilator harmonik dengan deret pangkat, getaran molekul diatom, dan metode Numerov.
2. D. A. McQuarrie, *Quantum Chemistry*, edisi ke-2 (University Science Books, 2008), Bab 5. Osilator harmonik dan spektroskopi rotasi–getaran dengan banyak contoh numerik.
3. P. Atkins dan R. Friedman, *Molecular Quantum Mechanics*, edisi ke-5 (Oxford University Press, 2011), Bab 2 dan 10. Operator tangga, unsur matriks, dan spektroskopi getaran.
4. G. Herzberg, *Spectra of Diatomic Molecules*, edisi ke-2 (Van Nostrand, 1950). Rujukan klasik tentang tetapan getaran, potensial Morse, dan Birge–Sponer.
5. E. B. Wilson, J. C. Decius, dan P. C. Cross, *Molecular Vibrations* (McGraw-Hill, 1955; Dover, 1980). Teori mode normal dan analisis koordinat normal yang lengkap.
6. L. Melander dan W. H. Saunders, *Reaction Rates of Isotopic Molecules* (Wiley, 1980). Teori dan percobaan efek isotop kinetik.
7. W. H. Press dkk., *Numerical Recipes*, edisi ke-3 (Cambridge University Press, 2007), Bab 17 dan 18. Metode tembak dan masalah nilai batas.
