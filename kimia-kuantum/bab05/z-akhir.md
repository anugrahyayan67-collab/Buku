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

## Subbab 5.1: Osilator klasik

Gunakan tetapan di Bab 1 dan massa isotop $m(^1\text{H}) = 1{,}00783$ u, $m(^2\text{H}) = 2{,}01410$ u, $m(^{12}\text{C}) = 12$ u, $m(^{16}\text{O}) = 15{,}9949$ u, $m(^{35}\text{Cl}) = 34{,}9689$ u. Soal dikelompokkan menurut tingkat: **dasar**, **menengah**, dan **tantangan ★**. Soal bertanda **[P]** dibahas di akhir bab.

**Dasar**

**1.** Benda bermassa 0,50 kg tergantung pada pegas dengan $k = 200$ N/m. Hitung $\omega$, $\nu$, dan periodenya.

**2.** Benda pada soal sebelumnya disimpangkan 5,0 cm lalu dilepas. Hitung energi total dan kecepatan maksimumnya.

**3.** Tunjukkan dengan substitusi bahwa $x(t) = A\cos(\omega t + \varphi)$ memenuhi $m\ddot x = -kx$ bila $\omega = \sqrt{k/m}$.

**4.** Hitung peluang klasik bahwa osilator berada di $|x| < A/2$, dengan (5.5).

**Menengah**

**5.** Untuk potensial Lennard-Jones $V = 4\varepsilon[(\sigma/r)^{12} - (\sigma/r)^6]$, tentukan $r_e$ dan $k = V''(r_e)$. Hitung $k$ dan $\tilde\nu$ harmonik untuk Ar₂ ($\varepsilon/k_B = 119{,}8$ K, $\sigma = 3{,}405$ Å, $\mu = 19{,}98$ u).

**6.** [P] Untuk dua benda dengan $\mathbf R = (m_A\mathbf r_A + m_B\mathbf r_B)/M$ dan $\mathbf r = \mathbf r_A - \mathbf r_B$, tunjukkan bahwa $\tfrac12m_A\dot{\mathbf r}_A^2 + \tfrac12m_B\dot{\mathbf r}_B^2 = \tfrac12M\dot{\mathbf R}^2 + \tfrac12\mu\dot{\mathbf r}^2$.

**7.** Getaran O–H dalam molekul besar sering dimodelkan sebagai atom H yang bergetar terhadap O yang diam. Berapa persen frekuensinya berubah bila massa tereduksi O–H dipakai sebagai gantinya?

**Tantangan ★**

**8.** ★ Tunjukkan bahwa untuk osilator klasik, rata-rata waktu energi kinetik dan energi potensial masing-masing $\tfrac12E$.

## Subbab 5.2: Persamaan Schrödinger osilator

**Dasar**

**9.** Hitung $\alpha = \mu\omega/\hbar$ dan $\alpha^{-1/2}$ untuk HCl ($\tilde\nu = 2990{,}95$ cm⁻¹, $\mu = 0{,}97959$ u).

**10.** Tunjukkan bahwa $\psi = e^{-bx^2}$ adalah fungsi eigen Hamiltonian osilator hanya bila $b = \alpha/2$. Berapa energinya?

**11.** Tunjukkan bahwa $\psi = xe^{-\alpha x^2/2}$ adalah fungsi eigen dengan $E = \tfrac32\hbar\omega$.

**12.** Dalam bentuk tak berdimensi, keadaan dengan $\varepsilon = 7$ mempunyai energi berapa dalam $\hbar\omega$?

**Menengah**

**13.** Tunjukkan bahwa $\alpha$ berdimensi m⁻² dan $\xi = \sqrt\alpha\,x$ tak berdimensi.

**14.** Tunjukkan bahwa $e^{+\xi^2/2}$ juga memenuhi (5.8) secara asimtotik untuk $\xi$ besar. Mengapa ditolak?

**15.** Tunjukkan bahwa $\psi = (2\xi^2 - 1)e^{-\xi^2/2}$ memenuhi (5.8) dan tentukan $\varepsilon$.

**16.** Hitung $1/\sqrt\alpha$ (pm) untuk ¹²C¹⁶O ($\tilde\nu = 2170$ cm⁻¹, $\mu = 6{,}8562$ u).

**Tantangan ★**

**17.** ★ Tunjukkan bahwa potensial $V = \tfrac12k(x - x_0)^2 + V_0$ memberi tingkat energi $V_0 + (v + \tfrac12)\hbar\omega$ dan fungsi gelombang yang tergeser ke $x_0$.

## Subbab 5.3: Penyelesaian deret dan polinom Hermite

**Dasar**

**18.** Dengan rekursi $H_{n+1} = 2\xi H_n - 2nH_{n-1}$, hitung $H_3$ dan $H_4$.

**19.** Tentukan akar $H_2$ dan $H_3$.

**20.** Verifikasi $H_n' = 2nH_{n-1}$ untuk $n = 3$.

**Menengah**

**21.** [P] Dengan rekursi koefisien (5.11), mulai dari $a_1 = 1$, $a_0 = 0$, dan $\varepsilon = 7$, bangun polinomnya. Tunjukkan bahwa ia sebanding dengan $H_3$.

**22.** Tuliskan $\psi_2$ ternormalisasi dalam $x$ dan $\alpha$.

**23.** Tunjukkan $\int H_1H_3e^{-\xi^2}d\xi = 0$ dengan integral Gauss.

**24.** Bila $\varepsilon = 1{,}2$, deret tidak berhenti. Tunjukkan bahwa untuk $k$ besar $a_{k+2}/a_k \to 2/k$, dan jelaskan mengapa ini berperilaku seperti $e^{\xi^2}$.

**25.** Dengan rekursi, bangun $H_5(y)$.

**Tantangan ★**

**26.** ★ Fungsi pembangkit Hermite adalah $e^{2\xi t - t^2} = \sum_nH_n(\xi)t^n/n!$. Uraikan sampai $t^2$ dan peroleh $H_0$, $H_1$, $H_2$.

## Subbab 5.4: Tingkat energi dan energi titik nol

**Dasar**

**27.** Hitung energi titik nol harmonik HBr ($\omega_e = 2648{,}98$ cm⁻¹) dalam cm⁻¹, kJ/mol, dan eV.

**28.** Panjang gelombang transisi $v = 0 \to 1$ HF menurut model harmonik ($\omega_e = 4138{,}3$ cm⁻¹)? Nilai terukur pita dasar 3961,4 cm⁻¹ setara berapa µm?

**29.** Dalam model harmonik, berapa energi yang diperlukan untuk eksitasi $v = 0 \to 3$ HCl?

**Menengah**

**30.** Untuk Br₂ ($\tilde\nu = 323{,}2$ cm⁻¹) pada 298 K, hitung $N_1/N_0$, $q_\text{vib}$, dan fraksi molekul pada $v = 1$.

**31.** Pada suhu berapa $N_1/N_0 = 0{,}10$ untuk N₂ ($\tilde\nu = 2358{,}6$ cm⁻¹)?

**32.** Energi getaran rata-rata di atas energi titik nol adalah $\langle E\rangle = hc\tilde\nu/(e^x - 1)$, $x = hc\tilde\nu/kT$. Hitung untuk I₂ ($\tilde\nu = 214{,}5$ cm⁻¹) pada 298 K.

**33.** [P] Untuk HCl, $D_e = 4{,}618$ eV, $\omega_e = 2990{,}95$ cm⁻¹, $\omega_ex_e = 52{,}82$ cm⁻¹. Hitung $D_0$.

**Tantangan ★**

**34.** ★ Kapasitas kalor getaran molar adalah $C = R\,x^2e^x/(e^x - 1)^2$. Hitung untuk Cl₂ ($\tilde\nu = 559{,}7$ cm⁻¹) pada 298 K, dan bandingkan dengan nilai klasik $R$.

## Subbab 5.5: Fungsi gelombang: kuantum vs klasik

**Dasar**

**35.** Tentukan titik balik klasik (dalam $\xi$) untuk $v = 0$, 1, dan 2.

**36.** Di mana $|\psi_1|^2$ maksimum?

**37.** Hitung peluang bahwa osilator keadaan dasar berada di $|\xi| < 0{,}5$.

**Menengah**

**38.** Hitung secara numerik peluang berada di luar titik balik untuk $v = 3$.

**39.** Hitung $\sqrt{\langle x^2\rangle}$ untuk HCl pada $v = 2$.

**40.** Berapa $\langle T\rangle$ untuk $v = 3$ dalam $\hbar\omega$?

**41.** Hitung $\Delta x\,\Delta p$ untuk $v = 1$.

**42.** Untuk keadaan dasar, berapa peluang osilator berada di dalam $|y| < 0{,}5$?

**Tantangan ★**

**43.** ★ Untuk $v = 10$, hitung secara numerik peluang berada di $|\xi| < \xi_t/2$ dan bandingkan dengan nilai klasik $\tfrac13$.

## Subbab 5.6: Operator tangga

**Dasar**

**44.** Hitung $\hat a\psi_1$ dan $\hat a^\dagger\psi_2$.

**45.** Hitung $\langle 3|x|2\rangle$ dalam satuan $\sqrt{\hbar/2\mu\omega}$.

**46.** Nyatakan $\hat p$ dengan $\hat a$ dan $\hat a^\dagger$.

**Menengah**

**47.** Hitung $\langle 2|x^2|0\rangle$.

**48.** Buktikan $[\hat N, \hat a^\dagger] = \hat a^\dagger$ dengan $\hat N = \hat a^\dagger\hat a$.

**49.** [P] Dengan operator tangga, buktikan $\langle v|x^2|v\rangle = (2v + 1)\hbar/2\mu\omega$ dan $\langle v|p^2|v\rangle = (2v + 1)\mu\hbar\omega/2$.

**50.** Hitung $\langle 1|x^4|1\rangle$.

**51.** Dengan operator tangga, tunjukkan bahwa $\langle v|\hat p^2|v\rangle = (2v + 1)\hbar^2\alpha/2$, lalu periksa bahwa $\langle T\rangle = \langle V\rangle$.

**Tantangan ★**

**52.** ★ Hitung $\langle 1|x^3|0\rangle$ dan $\langle 3|x^3|0\rangle$. Mengapa unsur ini penting untuk anharmonisitas?

## Subbab 5.7: Getaran molekul diatom dan massa tereduksi

**Dasar**

**53.** Hitung tetapan gaya HBr ($\tilde\nu = 2648{,}98$ cm⁻¹, $\mu = 0{,}9951$ u).

**54.** Ramalkan $\tilde\nu$ DBr dari data HBr ($m(^{79}\text{Br}) = 78{,}918$ u).

**55.** Molekul mana yang frekuensinya lebih tinggi, H₂ atau HD? Hitung $\omega_e(\text{HD})$.

**Menengah**

**56.** Hitung tetapan gaya NO ($\tilde\nu = 1904{,}2$ cm⁻¹). Letakkan di antara N₂ dan O₂, dan hubungkan dengan orde ikatan 2,5.

**57.** Ikatan tunggal C–C mempunyai $k \approx 450$ N/m. Perkirakan $\tilde\nu$ bila diperlakukan sebagai diatom dengan $\mu = 6$ u.

**58.** Ramalkan $\omega_e$ untuk ¹⁵N₂ ($m = 15{,}0001$ u) dari ¹⁴N₂ (2358,57 cm⁻¹).

**59.** CO bebas menyerap di 2143 cm⁻¹; dalam karbonil logam di 2000 cm⁻¹. Berapa persen tetapan gaya C–O turun?

**60.** Hitung tetapan gaya Cl₂ ($\tilde\nu = 560$ cm⁻¹, ³⁵Cl 34,969 u) dan bandingkan dengan F₂.

**Tantangan ★**

**61.** ★ Klorin alami mengandung ³⁵Cl₂, ³⁵Cl³⁷Cl, dan ³⁷Cl₂. Hitung $\tilde\nu$ untuk ³⁵Cl³⁷Cl dari ³⁵Cl₂ (559,7 cm⁻¹) dan perbandingan kelimpahan ketiganya.

## Subbab 5.8: Aturan seleksi inframerah

**Dasar**

**62.** Manakah yang aktif IR: H₂, HCl, tekuk CO₂, getaran N₂O, ulur simetris CH₄, getaran O₃?

**63.** Pada HBr, $B \approx 8{,}46$ cm⁻¹. Perkirakan lebar celah di pusat pita.

**64.** Pada 298 K, nilai $J$ dengan populasi rotasi terbesar untuk HCl ($B = 10{,}44$ cm⁻¹)?

**Menengah**

**65.** Hitung perbandingan intensitas pita panas $2 \leftarrow 1$ terhadap $1 \leftarrow 0$ untuk HCl ($\tilde\nu = 2886$ cm⁻¹) pada 1000 K.

**66.** Untuk $\mu(x) = \mu_0 + \mu_1x + \mu_2x^2$, tunjukkan bahwa transisi $2 \leftarrow 0$ tidak nol meskipun potensialnya harmonik.

**67.** Mengapa spektrum IR HCl tidak memiliki cabang Q? Molekul NO mempunyai cabang Q; apa bedanya?

**68.** Hitung pergeseran isotop pusat pita H⁸¹Br terhadap H⁷⁹Br ($\tilde\nu_0 = 2558{,}9$ cm⁻¹; $m(^{81}\text{Br}) = 80{,}916$ u).

**Tantangan ★**

**69.** ★ Mengapa intensitas IR suatu getaran sebanding dengan $(d\mu/dx)^2$ dan bukan dengan $\mu_0^2$? Berikan contoh molekul dengan dipol besar tetapi pita ulur lemah, atau sebaliknya.

## Subbab 5.9: Anharmonisitas dan potensial Morse

**Dasar**

**70.** Untuk CO ($\omega_e = 2169{,}81$, $\omega_ex_e = 13{,}29$ cm⁻¹), hitung pita dasar dan nada atas pertama.

**71.** Untuk HCl, $k = 516{,}3$ N/m dan $D_e = 4{,}618$ eV. Hitung parameter Morse $a$.

**72.** Pada jarak berapa (di sisi $r < r_e$) potensial Morse HCl bernilai $D_e$?

**Menengah**

**73.** [P] Selisih tingkat getaran H₂ yang terukur adalah $\Delta G_{1/2} = 4161{,}2$; $\Delta G_{3/2} = 3925{,}8$; $\Delta G_{5/2} = 3695{,}4$; $\Delta G_{7/2} = 3467{,}9$; $\Delta G_{9/2} = 3241{,}6$ cm⁻¹. Cocokkan dengan garis lurus, tentukan $\omega_e$ dan $\omega_ex_e$, lalu taksir $D_0$ dengan Birge–Sponer. Bandingkan dengan 4,478 eV.

**74.** Berapa banyak tingkat terikat HCl menurut Birge–Sponer ($\omega_e = 2990{,}95$, $\omega_ex_e = 52{,}82$ cm⁻¹)?

**75.** Untuk I₂, $\omega_e = 214{,}50$ dan $\omega_ex_e = 0{,}614$ cm⁻¹. Taksir $D_e$ dengan Birge–Sponer, dan bandingkan dengan nilai sebenarnya 1,556 eV.

**76.** Tunjukkan bahwa untuk (5.24), $\Delta G_{v+1/2} = 0$ pada $v + 1 = \omega_e/2\omega_ex_e$.

**Tantangan ★**

**77.** ★ Dengan uraian Taylor $e^{-y} = 1 - y + \tfrac12y^2 - \cdots$, tunjukkan bahwa potensial Morse di dekat $r_e$ adalah $D_ea^2(r - r_e)^2 - D_ea^3(r - r_e)^3 + \cdots$, sehingga $k = 2D_ea^2$.

## Subbab 5.10: Efek isotop

**Dasar**

**78.** Ramalkan $\omega_e$ untuk T₂ dari data H₂ ($m(^3\text{H}) = 3{,}01605$ u).

**79.** Ramalkan $k_H/k_D$ maksimum pada 298 K untuk pemutusan ikatan O–H (3400 cm⁻¹).

**80.** Hitung pergeseran ulur C–H (2900 cm⁻¹) bila ¹²C diganti ¹³C.

**Menengah**

**81.** [P] Pada suhu berapa $k_H/k_D = 3$ untuk pemutusan C–H (2900 cm⁻¹), menurut (5.31)?

**82.** [P] Mode normal HDO gas: 2727, 1402, 3707 cm⁻¹. Dengan data Contoh 5.46, hitung $\Delta E_0$ untuk H₂O + D₂O ⇌ 2HDO dan perkirakan $K$ pada 298 K (faktor statistik 4).

**83.** Dengan data H₂ di Contoh 5.40, ramalkan $D_0$ untuk T₂.

**84.** Efek isotop ¹⁶O/¹⁸O pada pemutusan ikatan C–O (1050 cm⁻¹, $\mu$ diatom C–O) berapa pada 298 K?

**Tantangan ★**

**85.** ★ Mengapa efek isotop kinetik dapat jauh lebih besar daripada nilai (5.31) pada suhu rendah, dan mengapa efek ini disebut "sidik jari" penerobosan?

## Subbab 5.11: Mode normal molekul poliatom

**Dasar**

**86.** Berapa banyak mode getaran HCN, SO₂, C₂H₄, CH₃Cl, dan naftalena (C₁₀H₈)?

**87.** Hitung energi titik nol harmonik CO₂ (1333; 667 ×2; 2349 cm⁻¹).

**88.** Molekul linear $N$ atom mempunyai $N - 1$ mode ulur. Berapa mode tekuknya? Periksa untuk CO₂.

**Menengah**

**89.** Hitung energi titik nol harmonik CH₄ (2917; 1534 ×2; 3019 ×3; 1306 ×3 cm⁻¹).

**90.** Mengapa semua mode N₂O (N=N=O) aktif IR, sedangkan ulur simetris CO₂ tidak?

**91.** [P] Pada CO₂, dua tingkat tak tergandeng berenergi hampir sama ($\approx 1335$ cm⁻¹) bercampur dan teramati di 1285 dan 1388 cm⁻¹. Dengan model 2 × 2 (Contoh 2.35), taksir unsur penggandeng $W$ bila selisih tingkat tak tergandeng (a) nol, (b) 10 cm⁻¹.

**92.** Berapa mode getaran NH₃ dan C₂H₆?

**93.** Pada panjang gelombang berapa (μm) mode ulur asimetris CO₂ (2349 cm⁻¹) menyerap? Mengapa mode ini tidak penting untuk efek rumah kaca bumi?

**Tantangan ★**

**94.** [P] ★ Untuk molekul linear A–B–A dengan pegas $k$ di tiap ikatan (tekuk diabaikan), tunjukkan $\omega_\text{sim} = \sqrt{k/m_A}$ dan $\omega_\text{asim} = \sqrt{k(1/m_A + 2/m_B)}$. Ramalkan ulur asimetris CO₂ dari ulur simetris 1333 cm⁻¹.

## Subbab 5.12: Penyelesaian numerik: metode Numerov

**Dasar**

**95.** Untuk $\hbar = \mu = 1$, tunjukkan bahwa $f_i = 1 + \tfrac{h^2}{6}(E - V_i)$.

**96.** Bila langkah $h$ dibagi tiga, galat energi Numerov mengecil berapa kali?

**97.** Untuk $v = 10$ osilator ($\hbar = \mu = \omega = 1$), hitung panjang gelombang de Broglie lokal di $x = 0$ dan langkah maksimum menurut aturan 10 titik per panjang gelombang.

**Menengah**

**98.** [P] Jalankan program subbab 5.12 untuk $V = x^4$ ($\hbar = \mu = 1$, selang $[-5, 5]$) dan cari tiga tingkat terendah.

**99.** Ubah program untuk $V = |x|$ dan cari empat tingkat terendah. Bandingkan dengan nol-nol fungsi Airy.

**100.** Untuk sumur ganda $V = V_0(x^2 - a^2)^2/a^4$ dengan $a = 1{,}5$, hitung pemisahan dua tingkat terendah untuk $V_0 = 3$, 5, dan 7.

**101.** Mengapa untuk tingkat tinggi lebih baik mengintegrasikan dari kedua tepi dan mencocokkan di tengah?

**Tantangan ★**

**102.** ★ Terapkan program pada potensial Morse HCl ($D_e = 4{,}618$ eV, $a = 1{,}868$ Å⁻¹, $r_e = 1{,}2746$ Å) dan bandingkan tiga tingkat terendah dengan rumus Morse.


# Jawaban

::: {.panjang}
| No. | Jawaban | No. | Jawaban |
|---|---|---|---|
| 1 | 20 rad/s; 3,18 Hz; 0,314 s | 52 | $3(\hbar/2\mu\omega)^{3/2}$; $\sqrt6(\hbar/2\mu\omega)^{3/2}$; suku $x^3$ potensial menggandengkan $\Delta v = \pm1, \pm3$ |
| 2 | 0,25 J; 1,0 m/s | 53 | 411 N/m |
| 3 | $\ddot x = -\omega^2x$ | 54 | 1886 cm⁻¹ |
| 4 | $\tfrac2\pi\arcsin\tfrac12 = \tfrac13$ | 55 | H₂; 3812 cm⁻¹ |
| 5 | $r_e = 2^{1/6}\sigma = 3{,}82$ Å; $k = 57{,}1\,\varepsilon/\sigma^2 = 0{,}815$ N/m; 26 cm⁻¹ | 56 | 1595 N/m; antara 1177 (O₂) dan 2295 (N₂) |
| 6 | lihat pembahasan | 57 | 1128 cm⁻¹ |
| 7 | frekuensi 3,0% lebih rendah (faktor 0,970) | 58 | 2278,8 cm⁻¹ |
| 8 | $\langle\sin^2\rangle = \langle\cos^2\rangle = \tfrac12$ | 59 | 13% |
| 9 | $8{,}69 \times 10^{21}$ m⁻²; 10,7 pm | 60 | 323 N/m; lebih lunak dari F₂ (471 N/m) |
| 10 | $E = \tfrac12\hbar\omega$ | 61 | 552,1 cm⁻¹; 9 : 6 : 1 (57,4% : 36,7% : 5,9%) |
| 11 | substitusi langsung | 62 | HCl, tekuk CO₂, semua mode N₂O dan O₃; H₂ dan ulur simetris CH₄ tidak |
| 12 | $3{,}5\,\hbar\omega$ | 63 | $4B \approx 34$ cm⁻¹ |
| 13 | $[\mu\omega/\hbar] = \text{kg s}^{-1}/(\text{J s}) = \text{m}^{-2}$ | 64 | $J = 3$ |
| 14 | tidak dapat dinormalisasi | 65 | 0,031 |
| 15 | $\varepsilon = 5$, $E = \tfrac52\hbar\omega$ | 66 | $\mu_2\langle 2|x^2|0\rangle = \sqrt2\,\mu_2\hbar/2\mu\omega$ |
| 16 | 4,76 pm | 67 | HCl: momentum sudut elektron nol, $\Delta J = 0$ terlarang; NO: elektron mempunyai momentum sudut ($\Pi$), $\Delta J = 0$ diizinkan |
| 17 | substitusi $y = x - x_0$ | 68 | 0,40 cm⁻¹ |
| 18 | $8\xi^3 - 12\xi$; $16\xi^4 - 48\xi^2 + 12$ | 69 | unsur $\mu_0\langle 1|0\rangle = 0$; contoh: CO (dipol 0,11 D, pita kuat karena $d\mu/dx$ besar) |
| 19 | $\pm0{,}707$; $0$ dan $\pm1{,}225$ | 70 | 2143,2; 4259,9 cm⁻¹ |
| 20 | $24\xi^2 - 12 = 6(4\xi^2 - 2)$ | 71 | 1,868 Å⁻¹ |
| 21 | $\xi - \tfrac23\xi^3 = -\tfrac{1}{12}H_3$ | 72 | $r_e - \ln2/a = r_e - 0{,}371$ Å |
| 22 | $(\alpha/\pi)^{1/4}(2\alpha x^2 - 1)e^{-\alpha x^2/2}/\sqrt2$ | 73 | $\omega_e = 4387{,}5$; $\omega_ex_e = 114{,}9$; $D_0 \approx 4{,}93$ eV (10% terlalu besar) |
| 23 | $12\sqrt\pi - 12\sqrt\pi = 0$ | 74 | $v_\text{maks} = 27{,}8$; 28 tingkat |
| 24 | koefisien $e^{\xi^2}$: $b_{k+2}/b_k = 1/(k/2 + 1) \to 2/k$ | 75 | 2,32 eV; 49% terlalu besar |
| 25 | $32y^5 - 160y^3 + 120y$ | 76 | dari (5.25) |
| 26 | $1$; $2\xi$; $4\xi^2 - 2$ | 77 | suku kubik negatif: potensial lebih lunak di sisi peregangan |
| 27 | 1324,5 cm⁻¹; 15,8 kJ/mol; 0,164 eV | 78 | 2544 cm⁻¹ |
| 28 | 2,42 µm; 2,52 µm | 79 | 9,3 |
| 29 | $3\omega_e = 8973$ cm⁻¹ | 80 | 2891 cm⁻¹ (turun 9 cm⁻¹) |
| 30 | 0,210; 1,266; 0,166 | 81 | 505 K |
| 31 | 1474 K | 82 | $\Delta E_0 = 13{,}5$ cm⁻¹; $K \approx 3{,}75$ |
| 32 | 118 cm⁻¹ = 1,41 kJ/mol | 83 | 4,591 eV |
| 33 | 4,434 eV | 84 | 1,06 |
| 34 | $0{,}563R = 4{,}68$ J K⁻¹ mol⁻¹ | 85 | penerobosan sangat peka massa; lihat Contoh 3.43 |
| 35 | $\pm1$; $\pm\sqrt3$; $\pm\sqrt5$ | 86 | 4; 3; 12; 9; 48 |
| 36 | $\xi = \pm1$ | 87 | 2508 cm⁻¹ = 30,0 kJ/mol |
| 37 | $\text{erf}(0{,}5) = 0{,}520$ | 88 | $2N - 4$; CO₂: 2 |
| 38 | 0,085 | 89 | 9480 cm⁻¹ = 113 kJ/mol |
| 39 | 17,0 pm | 90 | N₂O tidak mempunyai pusat inversi |
| 40 | $\tfrac74$ | 91 | (a) 51,5 cm⁻¹; (b) 51,3 cm⁻¹ |
| 41 | $\tfrac32\hbar$ | 92 | 6; 18 |
| 42 | 0,520 | 93 | 4,26 μm; jauh dari puncak pancaran bumi (± 10 μm) |
| 43 | 0,352 (klasik 0,333) | 94 | faktor 1,915; 2552 cm⁻¹ (terukur 2349) |
| 44 | $\psi_0$; $\sqrt3\,\psi_3$ | 95 | $g = 2(V - E)$ |
| 45 | $\sqrt3$ | 96 | 81 |
| 46 | $\hat p = i\sqrt{\mu\hbar\omega/2}\,(\hat a^\dagger - \hat a)$ | 97 | $2\pi/\sqrt{21} = 1{,}37$; $h \lesssim 0{,}14$ |
| 47 | $\sqrt2\,\hbar/2\mu\omega$ | 98 | 0,6680; 2,3936; 4,6968 |
| 48 | $\hat a^\dagger[\hat a, \hat a^\dagger] = \hat a^\dagger$ | 99 | 0,8086; 1,8558; 2,5781; 3,2446 |
| 49 | lihat pembahasan | 100 | 0,112; 0,043; 0,018 |
| 50 | $15(\hbar/2\mu\omega)^2$ | 101 | bagian yang meluruh di daerah terlarang tidak stabil secara numerik bila diintegrasikan ke arah meluruh |
| 51 | $\langle T\rangle = \langle V\rangle = \tfrac12(v + \tfrac12)\hbar\omega$ | 102 | 1480,4; 4351,3; 7102,0 cm⁻¹ (cocok); pita dasar 2870,8 cm⁻¹ |
:::


# Pembahasan soal terpilih

**Soal 6.** Dari definisi $\mathbf R$ dan $\mathbf r$: $\mathbf r_A = \mathbf R + \tfrac{m_B}{M}\mathbf r$ dan $\mathbf r_B = \mathbf R - \tfrac{m_A}{M}\mathbf r$. Turunkan terhadap waktu dan masukkan:

$$
\tfrac12m_A\left(\dot{\mathbf R} + \tfrac{m_B}{M}\dot{\mathbf r}\right)^2 + \tfrac12m_B\left(\dot{\mathbf R} - \tfrac{m_A}{M}\dot{\mathbf r}\right)^2 = \tfrac12M\dot{\mathbf R}^2 + \left(\tfrac{m_Am_B}{M} - \tfrac{m_Bm_A}{M}\right)\dot{\mathbf R}\cdot\dot{\mathbf r} + \tfrac12\,\frac{m_Am_B(m_B + m_A)}{M^2}\,\dot{\mathbf r}^2 .
$$

Suku tengah nol dan koefisien suku terakhir adalah $m_Am_B/M = \mu$.

*Cara berpikir:* pemisahan ini berlaku untuk energi kinetik dan, karena potensial hanya bergantung pada $\mathbf r$, untuk Hamiltonian seluruhnya. Dalam mekanika kuantum hasilnya sama: $\hat H = \hat H_\text{pm} + \hat H_\text{rel}$, dan fungsi gelombang menjadi hasil kali (pemisahan variabel, subbab 4.4). Atom hidrogen di Bab 7 dipisahkan dengan cara yang sama, dengan $\mu$ elektron–proton.

**Soal 21.** Dari (5.11) dengan $\varepsilon = 7$: $a_3 = \tfrac{2(1) + 1 - 7}{(2)(3)}a_1 = -\tfrac23$, lalu $a_5 = \tfrac{2(3) + 1 - 7}{(4)(5)}a_3 = 0$, dan semua koefisien berikutnya nol. Polinomnya $\xi - \tfrac23\xi^3 = -\tfrac{1}{12}(8\xi^3 - 12\xi) = -\tfrac{1}{12}H_3$.

*Cara berpikir:* pemilihan $\varepsilon = 2v + 1$ membuat pembilang rekursi nol tepat pada $k = v$, sehingga deret "dipotong" menjadi polinom. Normalisasi menentukan tetapan pengali; konvensi Hermite memilih koefisien pangkat tertinggi $2^v$.

**Soal 33.** $G(0) = \tfrac12\omega_e - \tfrac14\omega_ex_e = 1495{,}48 - 13{,}21 = 1482{,}27$ cm⁻¹ $= 0{,}1838$ eV. $D_0 = 4{,}618 - 0{,}184 = 4{,}434$ eV.

*Cara berpikir:* nilai termokimia $D_0(\text{HCl}) = 4{,}434$ eV (427,8 kJ/mol) cocok. Energi titik nol menyumbang 4% energi ikatan; untuk perbandingan dengan ketelitian kimia (4 kJ/mol), koreksi ini tidak boleh diabaikan, dan program kimia komputasi menambahkannya secara otomatis (koreksi ZPE, Bab 17).

**Soal 49.** $\hat x^2 = \tfrac{\hbar}{2\mu\omega}(\hat a + \hat a^\dagger)^2 = \tfrac{\hbar}{2\mu\omega}(\hat a^2 + \hat a^{\dagger2} + \hat a\hat a^\dagger + \hat a^\dagger\hat a)$. Suku $\hat a^2$ dan $\hat a^{\dagger2}$ mengubah $v$ sebesar 2, sehingga unsur diagonalnya nol. $\langle v|\hat a^\dagger\hat a|v\rangle = v$ dan $\langle v|\hat a\hat a^\dagger|v\rangle = v + 1$. Jadi $\langle v|x^2|v\rangle = \tfrac{\hbar}{2\mu\omega}(2v + 1)$. Dengan $\hat p = i\sqrt{\mu\hbar\omega/2}(\hat a^\dagger - \hat a)$, $\hat p^2 = -\tfrac{\mu\hbar\omega}{2}(\hat a^{\dagger2} + \hat a^2 - \hat a^\dagger\hat a - \hat a\hat a^\dagger)$, dan unsur diagonalnya $\tfrac{\mu\hbar\omega}{2}(2v + 1)$.

*Cara berpikir:* tanpa satu integral pun, kita mendapat (5.16) dan teorema virial: $\langle p^2\rangle/2\mu = \tfrac12\mu\omega^2\langle x^2\rangle = \tfrac12E_v$. Setiap unsur matriks pangkat $x$ dan $p$ dapat dihitung dengan "menghitung jalan" di tangga.

**Soal 73.** Garis lurus terbaik melalui lima titik $(v + 1, \Delta G)$ adalah $\Delta G = 4387{,}5 - 229{,}7(v + 1)$. Dengan (5.25): $\omega_e = 4387{,}5$ cm⁻¹ dan $\omega_ex_e = 114{,}9$ cm⁻¹. Birge–Sponer: $D_e = \omega_e^2/4\omega_ex_e = 41\,901$ cm⁻¹ $= 5{,}20$ eV; $G(0) = 2165{,}0$ cm⁻¹; $D_0 = 39\,736$ cm⁻¹ $= 4{,}93$ eV, 10% di atas nilai sebenarnya.

*Cara berpikir:* grafik $\Delta G$ terhadap $v$ untuk H₂ sebenarnya melengkung ke bawah pada $v$ tinggi (tingkat-tingkat atas lebih rapat daripada ramalan linear), sehingga garis lurus dari lima titik pertama memberi luas yang terlalu besar. Inilah keterbatasan umum ekstrapolasi Birge–Sponer: hasilnya batas atas, dan makin sedikit tingkat yang terukur, makin besar kesalahannya (bandingkan dengan I₂, yang meleset 49%).

**Soal 81.** Dari Contoh 5.42, $\Delta E_0 = 385{,}4$ cm⁻¹. Syaratnya $hc\Delta E_0/kT = \ln 3$, jadi $T = (385{,}4)(1{,}4388\ \text{cm K})/1{,}0986 = 505$ K.

*Cara berpikir:* efek isotop kinetik turun dari 6,4 pada 298 K ke 3 pada 505 K. Ketergantungan suhu ini diuji dalam percobaan: bila $k_H/k_D$ mengikuti (5.31), model energi titik nol sudah cukup; bila efeknya jauh lebih besar dan hampir tidak bergantung suhu, penerobosan berperan.

**Soal 82.** $2E_0(\text{HDO}) = 2727 + 1402 + 3707 = 7836$ cm⁻¹; $E_0(\text{H}_2\text{O}) + E_0(\text{D}_2\text{O}) = 4504 + 3318{,}5 = 7822{,}5$ cm⁻¹. $\Delta E_0 = 13{,}5$ cm⁻¹ $= 0{,}16$ kJ/mol. $K \approx 4e^{-13{,}5 \times 1{,}4388/298{,}15} = 4 \times 0{,}937 = 3{,}75$.

*Cara berpikir:* nilai terukur sekitar 3,8, sangat dekat dengan faktor statistik 4: energi titik nol campuran hampir aditif. Bandingkan dengan H₂ + D₂ (Contoh 5.43), tempat penyimpangannya jauh lebih besar karena hanya ada satu mode dan isotopnya mengubah massa tereduksi hampir dua kali lipat. Untuk kimia air berat, akibatnya praktis: dalam campuran H₂O dan D₂O, sebagian besar deuterium berada sebagai HDO.

**Soal 91.** Nilai eigen matriks $\begin{pmatrix}E_1 & W\\ W & E_2\end{pmatrix}$ adalah $\bar E \pm \tfrac12\sqrt{\Delta^2 + 4W^2}$, dengan $\Delta = E_1 - E_2$. Pemisahan teramati $1388 - 1285 = 103$ cm⁻¹ $= \sqrt{\Delta^2 + 4W^2}$. (a) $\Delta = 0$: $W = 51{,}5$ cm⁻¹. (b) $\Delta = 10$: $W = \tfrac12\sqrt{103^2 - 10^2} = 51{,}3$ cm⁻¹.

*Cara berpikir:* bila kedua tingkat hampir berdegenerasi, pemisahan teramati praktis $2W$ dan kedua tingkat tercampur hampir 50 : 50. Karena itu kedua pita Raman hampir sama kuat, meskipun hanya satu di antaranya ($v_1 = 1$) yang "seharusnya" aktif Raman: intensitas dipinjam melalui pencampuran. Gejala peminjaman intensitas ini muncul lagi dalam spektroskopi elektronik (Bab 15).

**Soal 94.** Misalkan simpangan $x_1$ (A kiri), $x_2$ (B), $x_3$ (A kanan); $V = \tfrac12k(x_2 - x_1)^2 + \tfrac12k(x_3 - x_2)^2$. Ulur simetris: $x_3 = -x_1$, $x_2 = 0$; persamaan gerak atom A: $m_A\ddot x_1 = -k(x_1 - x_2) = -kx_1$, jadi $\omega_\text{sim} = \sqrt{k/m_A}$; atom B tidak bergerak. Ulur asimetris: $x_3 = x_1$, dan pusat massa diam, $2m_Ax_1 + m_Bx_2 = 0$, sehingga $x_2 = -2m_Ax_1/m_B$. Maka $m_A\ddot x_1 = k(x_2 - x_1) = -k(1 + 2m_A/m_B)x_1$, jadi $\omega_\text{asim}^2 = k(1/m_A + 2/m_B)$. Perbandingan $\omega_\text{asim}/\omega_\text{sim} = \sqrt{1 + 2m_A/m_B} = \sqrt{1 + 2(15{,}995)/12} = 1{,}915$, sehingga ramalannya $1333 \times 1{,}915 = 2552$ cm⁻¹.

*Cara berpikir:* nilai terukur 2349 cm⁻¹, 8% lebih rendah. Selisihnya menunjukkan bahwa kedua ikatan C=O tidak bebas: ada tetapan gaya **interaksi** $k_{12}$ yang membuat peregangan satu ikatan melemahkan yang lain. Selain itu, 1333 cm⁻¹ sendiri adalah nilai rata-rata pasangan resonansi Fermi (soal 91). Medan gaya dengan suku silang inilah yang ditentukan oleh analisis koordinat normal dan dihitung langsung oleh program kimia komputasi.

**Soal 98.** Dengan $V = x^4$, selang $[-5, 5]$, dan 2001 titik, pencarian bagi dua memberi $E_0 = 0{,}6680$, $E_1 = 2{,}3936$, $E_2 = 4{,}6968$ (dan $E_3 = 7{,}3357$).

*Cara berpikir:* selisih antartingkat **membesar** (1,73; 2,30; 2,64), berbeda dengan osilator harmonik. Untuk potensial $V \propto |x|^n$, tingkat-tingkat tinggi berskala $E_v \propto v^{2n/(n+2)}$: $n = 1$ memberi $v^{2/3}$ (makin rapat), $n = 2$ memberi $v$ (berjarak sama), $n = 4$ memberi $v^{4/3}$, dan $n \to \infty$ (dinding kotak) memberi $v^2$. Osilator harmonik adalah satu-satunya kasus yang berjarak sama: kasus perbatasan antara kotak dan sumur yang melandai.

# Bacaan lanjut

1. I. N. Levine, *Quantum Chemistry*, edisi ke-7 (Pearson, 2014), Bab 4. Osilator harmonik dengan deret pangkat, getaran molekul diatom, dan metode Numerov.
2. D. A. McQuarrie, *Quantum Chemistry*, edisi ke-2 (University Science Books, 2008), Bab 5. Osilator harmonik dan spektroskopi rotasi–getaran dengan banyak contoh numerik.
3. P. Atkins dan R. Friedman, *Molecular Quantum Mechanics*, edisi ke-5 (Oxford University Press, 2011), Bab 2 dan 10. Operator tangga, unsur matriks, dan spektroskopi getaran.
4. G. Herzberg, *Spectra of Diatomic Molecules*, edisi ke-2 (Van Nostrand, 1950). Rujukan klasik tentang tetapan getaran, potensial Morse, dan Birge–Sponer.
5. E. B. Wilson, J. C. Decius, dan P. C. Cross, *Molecular Vibrations* (McGraw-Hill, 1955; Dover, 1980). Teori mode normal dan analisis koordinat normal yang lengkap.
6. L. Melander dan W. H. Saunders, *Reaction Rates of Isotopic Molecules* (Wiley, 1980). Teori dan percobaan efek isotop kinetik.
7. W. H. Press dkk., *Numerical Recipes*, edisi ke-3 (Cambridge University Press, 2007), Bab 17 dan 18. Metode tembak dan masalah nilai batas.
