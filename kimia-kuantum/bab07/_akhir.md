# Ringkasan Bab 7

| Gagasan | Rumus (satuan atom) | Subbab |
|---|---|---|
| Hamiltonian | $\hat H = -\tfrac12\nabla^2 - Z/r$; $\ a_0 = 52{,}918$ pm, $E_h = 27{,}211$ eV | 7.1 |
| Pemisahan | $\psi_{n\ell m} = R_{n\ell}(r)Y_\ell^m(\theta, \phi)$ | 7.2 |
| Persamaan radial | $-\tfrac12u'' + \left[-\tfrac Zr + \tfrac{\ell(\ell+1)}{2r^2}\right]u = Eu$, $\ u = rR$ | 7.2 |
| Bentuk penyelesaian | $u = r^{\ell+1}e^{-Zr/n}f(r)$; $\ f$ polinom berderajat $n - \ell - 1$ | 7.3 |
| Energi | $E_n = -\tfrac{\mu}{m_e}\tfrac{Z^2}{2n^2}$; $\ \ell = 0, \ldots, n - 1$; degenerasi $n^2$ | 7.3, 7.4 |
| Simpul | radial $n - \ell - 1$; sudut $\ell$; total $n - 1$ | 7.5 |
| Rapat di inti | $|\psi_{ns}(0)|^2 = Z^3/\pi n^3$; nol untuk $\ell > 0$ | 7.5 |
| Distribusi radial | $P(r) = r^2R_{n\ell}^2$; $\ r_\text{mp} = n^2/Z$ untuk $\ell = n - 1$ | 7.6 |
| Orbital riil | $p_x = (p_{-1} - p_{+1})/\sqrt2$, $\ p_y = i(p_{-1} + p_{+1})/\sqrt2$ | 7.7 |
| Nilai harap | $\langle r\rangle = [3n^2 - \ell(\ell+1)]/2Z$; $\ \langle 1/r\rangle = Z/n^2$ | 7.9 |
| Teorema virial | $\langle V\rangle = 2E$; $\ \langle T\rangle = -E$ | 7.9 |
| Mirip hidrogen; Moseley | $E \propto Z^2$, ukuran $\propto 1/Z$; $\ E_{K\alpha} \approx \tfrac34(Z - 1)^2(13{,}6\ \text{eV})$ | 7.10 |
| Aturan seleksi | $\Delta\ell = \pm1$, $\ \Delta m = 0, \pm1$, $\ \Delta n$ sembarang | 7.11 |
| Laju peluruhan | $A = \omega^3|\mathbf d|^2/3\pi\varepsilon_0\hbar c^3$; $\ \tau(2p) = 1{,}60$ ns | 7.11 |
| Zeeman normal | $E_Z = m_\ell\mu_BB$; triplet berjarak $\mu_BB$ | 7.12 |
| Numerov radial | $g = 2(V - E) + \ell(\ell+1)/r^2$; mulai dari $u = r^{\ell+1}$ | 7.13 |

**Jawaban kuis cepat.** **7.1** $-Z/r = -1$ hartree; karena hanya bergantung pada jarak dari inti, sehingga gayanya selalu menuju pusat. **7.2** Karena $\hat L^2$ yang muncul di persamaan radial hanya bergantung pada $\ell$; 16. **7.3** Derajat 1 ($n - \ell - 1$); hanya $\ell = 0$, karena $\ell \le n - 1$. **7.4** 16; 1,51 eV. **7.5** Dua simpul radial dan dua sudut; nol di inti berasal dari faktor $r^\ell$ yang ada pada setiap orbital dengan $\ell > 0$, bukan dari akar polinom radial. **7.6** 9 bohr; 4s, karena mempunyai lobus-lobus dalam di dekat inti. **7.7** Bukan; ya, dengan nilai eigen nol (Contoh 6.23); karena keduanya kombinasi linear fungsi-fungsi yang berdegenerasi. **7.8** Empat; dua kerucut, pada 54,7° dan 125,3°. **7.9** $\langle T\rangle = 1{,}51$ eV, $\langle V\rangle = -3{,}02$ eV; karena $\langle V\rangle = -Z\langle 1/r\rangle = 2E_n$ hanya bergantung pada $n$. **7.10** $a_0/3 = 17{,}6$ pm; $-13{,}6$ eV. **7.11** Dari keadaan 3p, yang dapat meluruh ke 1s dengan $\Delta\ell = -1$. **7.12** Tidak; ia campuran $m = +1$ dan $m = -1$ yang kini berenergi berbeda; karena $\ell = 0$ hanya mempunyai $m = 0$. **7.13** Karena $u \propto r^{\ell+1}$ adalah perilaku penyelesaian yang dapat diterima di dekat inti, sedangkan $u = 1$ membuat $R = 1/r$ tak hingga; karena elektron 3d hampir tidak menembus teras 1s², sehingga merasakan muatan efektif $+1$ seperti di hidrogen.

# Pertanyaan

1. Mengapa massa tereduksi, bukan massa elektron, yang muncul dalam energi atom hidrogen? Seberapa besar perbedaannya?
2. Apa keuntungan satuan atom? Apa yang harus diingat ketika membandingkan hasil dengan percobaan?
3. Mengapa elektron tidak jatuh ke inti menurut mekanika kuantum?
4. Bagaimana syarat kenormalan menghasilkan bilangan kuantum $n$? Bandingkan dengan osilator harmonik.
5. Mengapa $\ell$ dibatasi oleh $n - 1$?
6. Mengapa energi atom hidrogen tidak bergantung pada $\ell$, padahal persamaan radialnya bergantung? Apa yang merusak degenerasi ini dalam atom lain?
7. Apa beda simpul radial dan simpul sudut? Mengapa jumlah totalnya $n - 1$?
8. Mengapa hanya orbital s yang mempunyai rapat elektron tidak nol di inti? Sebutkan dua akibatnya yang dapat diukur.
9. Mengapa fungsi distribusi radial 1s nol di inti, padahal $|\psi|^2$ terbesar di sana?
10. Apa arti penembusan, dan bagaimana ia menjelaskan urutan energi s < p < d dalam atom berelektron banyak?
11. Kapan orbital kompleks lebih berguna daripada orbital riil, dan sebaliknya?
12. Mengapa tanda fungsi gelombang penting, padahal yang terukur adalah $|\psi|^2$?
13. Mengapa ada lima orbital d dan tujuh orbital f?
14. Apa isi teorema virial untuk atom hidrogen? Apa artinya bagi energi kinetik elektron ketika ikatan kimia terbentuk?
15. Mengapa hukum Moseley memastikan bahwa tabel periodik harus diurutkan menurut nomor atom?
16. Mengapa unsur berat memerlukan kimia kuantum relativistik?
17. Jelaskan aturan seleksi $\Delta\ell = \pm1$ dengan dua cara: momentum sudut foton dan paritas.
18. Mengapa keadaan 2s hidrogen metastabil? Apa analognya dalam kimia molekul?
19. Mengapa efek Zeeman normal selalu memberi tepat tiga garis?
20. Apa yang dapat dilakukan metode numerik yang tidak dapat dilakukan penyelesaian eksak? Berikan dua contoh dari bab ini.
21. Bagaimana teka-teki pembuka bab (2s dan 2p berenergi sama pada H, tetapi tidak pada Li) terjawab?

# Soal

%%SOAL%%

# Jawaban

%%JAWABAN%%

# Pembahasan soal terpilih

**Soal {{taksir}}.** $dE/dr = -1/r^3 + Z/r^2 = 0$ memberi $r = 1/Z$. Masukkan: $E = Z^2/2 - Z^2 = -Z^2/2$.

*Cara berpikir:* penskalaan $r \propto 1/Z$ dan $E \propto Z^2$ sudah terlihat dari analisis dimensi ini, tanpa menyelesaikan persamaan apa pun. Taksiran semacam ini juga menunjukkan mengapa elektron dalam atom berat sangat terikat dan sangat dekat ke inti: untuk emas, elektron 1s berada sekitar $1/79$ bohr dari inti dan terikat sekitar $79^2/2 \approx 3100$ hartree (lebih dari 80 keV).

**Soal {{rek3s}}.** Dengan $\kappa = \tfrac13$, $\ell = 0$, $Z = 1$: $a_1 = \tfrac{2[\tfrac13 - 1]}{(1)(2)}a_0 = -\tfrac23$; $a_2 = \tfrac{2[\tfrac23 - 1]}{(2)(3)}a_1 = \left(-\tfrac19\right)\left(-\tfrac23\right) = \tfrac{2}{27}$; $a_3 = \tfrac{2[1 - 1]}{(3)(4)}a_2 = 0$. Jadi $f = 1 - \tfrac23r + \tfrac{2}{27}r^2 = \tfrac{1}{27}(27 - 18r + 2r^2)$, dan $R = u/r = f\,e^{-r/3}$.

*Cara berpikir:* deret berhenti tepat pada $k = n - \ell - 1 = 2$. Tanda koefisien berganti-ganti, sehingga polinomnya mempunyai dua akar positif: dua simpul radial 3s (Contoh 7.14).

**Soal {{mp3s}}.** $P(r) = r^2R_{30}^2 \propto r^2(27 - 18r + 2r^2)^2e^{-2r/3}$. Turunan $P$ nol di simpul ($r = 1{,}90$ dan $7{,}10$) dan di tiga maksimum. Secara numerik, maksimum terbesar di $r = 13{,}07$ bohr (692 pm); dua maksimum kecil di sekitar 0,74 dan 4,19 bohr.

*Cara berpikir:* jari-jari paling mungkin 3s (13,07) lebih besar daripada 3d (9), tetapi 3s mempunyai dua lobus dalam yang menembus dekat inti. Gambar 7.2 memperlihatkan keduanya: 3s "lebih besar dan lebih dalam" sekaligus. Ukuran dan penembusan adalah dua sifat berbeda.

**Soal {{virial}}.** $\langle 1/r^2\rangle = \int_0^\infty4r^2e^{-2r}r^{-2}dr = 4\int_0^\infty e^{-2r}dr = 2$, sama dengan $Z^2/n^3(\ell + \tfrac12) = 1/(1 \cdot \tfrac12) = 2$. Dari $\langle T\rangle = \tfrac12$ hartree, $\langle p^2\rangle = 1$, sehingga $v_\text{rms} = 1$ satuan atom $= 2{,}19 \times 10^6$ m/s.

*Cara berpikir:* kecepatan rms elektron 1s sama dengan kecepatan orbit Bohr pertama ($\alpha c$). Nilai $\langle 1/r^2\rangle$ muncul dalam koreksi relativistik dan dalam kopling spin–orbit (Bab 9); ia berbanding terbalik dengan $\ell + \tfrac12$, sehingga koreksi terbesar untuk orbital s.

**Soal {{radial}}.** $\int_0^\infty R_{10}R_{21}r^3dr = \int_0^\infty 2e^{-r}\cdot\tfrac{1}{2\sqrt6}re^{-r/2}r^3dr = \tfrac{1}{\sqrt6}\int_0^\infty r^4e^{-3r/2}dr = \tfrac{1}{\sqrt6}\cdot\tfrac{4!}{(3/2)^5} = \tfrac{24}{7{,}594\sqrt6} = 1{,}290$. Bagian sudut $\int Y_0^0\cos\theta\,Y_1^0\,d\Omega = 1/\sqrt3$. Hasil kalinya $0{,}745 = 128\sqrt2/243$.

*Cara berpikir:* unsur matriks dipol transisi sepanjang 0,75 bohr: elektron yang "bergoyang" antara 1s dan 2p menggeser pusat muatannya sekitar 40 pm. Kekuatan osilator transisi Lyman-α, $f = \tfrac23\Delta E|\langle 1s|\mathbf r|2p\rangle|^2 = 0{,}416$, adalah salah satu yang terbesar di antara transisi atom.

**Soal {{yukawa}}.** Ganti satu baris program: `V = -np.exp(-r/lam)/r`. Dengan kisi 0,002 sampai 80 bohr: $\lambda = 100$: $-0{,}490$; $\lambda = 10$: $-0{,}407$; $\lambda = 5$: $-0{,}327$; $\lambda = 2$: $-0{,}148$; $\lambda = 1$: $-0{,}0103$ hartree. Keadaan 2s hilang (tidak terikat) sebelum $\lambda = 2$.

*Cara berpikir:* penyaringan muatan oleh elektron dan ion bebas di sekitarnya melemahkan ikatan; di bawah $\lambda_c \approx 0{,}84$ bohr tidak ada keadaan terikat sama sekali. Dalam plasma rapat (interior bintang, plasma laser), garis-garis spektrum tingkat tinggi menghilang satu per satu ketika tingkatnya melewati batas ionisasi: **penurunan energi ionisasi** yang teramati sebagai berakhirnya deret Balmer lebih awal daripada di laboratorium. Degenerasi $\ell$ juga pecah, karena potensialnya tidak lagi $1/r$ murni.

# Bacaan lanjut

1. I. N. Levine, *Quantum Chemistry*, edisi ke-7 (Pearson, 2014), Bab 6. Penyelesaian lengkap atom hidrogen, orbital riil, dan efek Zeeman.
2. D. A. McQuarrie, *Quantum Chemistry*, edisi ke-2 (University Science Books, 2008), Bab 7. Atom hidrogen dengan banyak gambar dan latihan.
3. H. A. Bethe dan E. E. Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms* (Springer, 1957; Dover, 2008). Rujukan klasik: nilai harap, unsur matriks, laju transisi, struktur halus, dan efek medan luar.
4. P. Atkins dan R. Friedman, *Molecular Quantum Mechanics*, edisi ke-5 (Oxford University Press, 2011), Bab 3. Atom hidrogen dan atom mirip hidrogen dengan sudut pandang kimia.
5. G. W. F. Drake (ed.), *Springer Handbook of Atomic, Molecular, and Optical Physics* (Springer, 2006). Data spektroskopi hidrogen dan ion mirip hidrogen dengan ketelitian tinggi.
6. P. Pyykkö, "Relativistic effects in chemistry: more common than you thought", *Annual Review of Physical Chemistry* 63, 45–64 (2012). Pengantar efek relativistik yang disinggung di Contoh 7.30.
