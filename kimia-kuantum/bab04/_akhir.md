# Ringkasan Bab 4

| Gagasan | Rumus | Subbab |
|---|---|---|
| Operator linear | $\hat A(c_1f + c_2g) = c_1\hat Af + c_2\hat Ag$ | 4.1 |
| Komutator kanonik | $[\hat x, \hat p_x] = i\hbar$; $\ [\hat A, \hat B\hat C] = [\hat A, \hat B]\hat C + \hat B[\hat A, \hat C]$ | 4.1 |
| Persamaan nilai eigen | $\hat Af = af$; kombinasi fungsi eigen terdegenerasi tetap fungsi eigen | 4.2 |
| Operator dasar | $\hat x = x$; $\ \hat p_x = -i\hbar\,\partial_x$; $\ \hat L_z = -i\hbar\,\partial_\phi$ | 4.3 |
| Hamiltonian molekul | kinetik inti + kinetik elektron + tarikan e–inti + tolakan e–e + tolakan inti–inti | 4.4 |
| Pemisahan variabel | $\hat H = \hat H_1 + \hat H_2 \Rightarrow \psi = \psi_a\psi_b$, $E = E_a + E_b$ | 4.4 |
| Kotak 3D | $E = \tfrac{h^2}{8m}\left(\tfrac{n_x^2}{a^2} + \tfrac{n_y^2}{b^2} + \tfrac{n_z^2}{c^2}\right)$ | 4.5 |
| Energi Fermi | $E_F = \tfrac{\hbar^2}{2m}(3\pi^2n)^{2/3}$ | 4.5 |
| Nilai harap | $\langle A\rangle = \int\psi^*\hat A\psi\,d\tau$ | 4.6 |
| Teorema Ehrenfest | $\tfrac{d}{dt}\langle A\rangle = \tfrac i\hbar\langle[\hat H, \hat A]\rangle$; $\ \tfrac{d\langle x\rangle}{dt} = \tfrac{\langle p\rangle}{m}$, $\ \tfrac{d\langle p\rangle}{dt} = -\langle V'\rangle$ | 4.6 |
| Syarat fungsi gelombang | bernilai tunggal, malar, turunan malar ($V$ berhingga), dapat dinormalisasi | 4.7 |
| Hermitian | $\int f^*\hat Ag = \int g(\hat Af)^*$; nilai eigen riil, fungsi eigen ortogonal | 4.8 |
| Ekspansi | $\psi = \sum c_n\phi_n$, $\ c_n = \langle\phi_n|\psi\rangle$, $\ \sum|c_n|^2 = 1$ | 4.9 |
| Komut ⇔ fungsi eigen bersama | $[\hat A, \hat B] = 0$ | 4.10 |
| Relasi Robertson | $\Delta A\,\Delta B \ge \tfrac12|\langle[\hat A, \hat B]\rangle|$ | 4.10 |
| Paritas; Laporte | $\hat\Pi\psi_{n\ell m} = (-1)^\ell\psi_{n\ell m}$; transisi hanya g ↔ u | 4.11 |
| Pengukuran | hasil = nilai eigen; peluang $|c_n|^2$; sesudahnya keadaan $\phi_n$ | 4.12 |
| Evolusi waktu | $\Psi(t) = e^{-i\hat Ht/\hbar}\Psi(0)$ | 4.13 |
| Notasi Dirac | $\langle m|\hat A|n\rangle = A_{mn}$; $\ \sum|n\rangle\langle n| = \hat 1$; $\ \mathbf{Hc} = E\mathbf c$ | 4.14 |

**Jawaban kuis cepat.** **4.1** $[\hat D, x^3]f = (x^3f)' - x^3f' = 3x^2f$, jadi $3x^2$. Tidak: $[\hat D, e^x] = e^x$. **4.2** Tidak; $\hat A(f + g) = af + bg$, bukan kelipatan $f + g$ jika $a \ne b$. **4.3** $-\hbar^2(\partial_x^2 + \partial_y^2)$; $\tfrac12\kappa(x^2 + y^2 + z^2)$. **4.4** $3 \times \tfrac12h\nu = \tfrac32h\nu$. **4.5** Enam: semua permutasi $(1, 2, 3)$. **4.6** Nol; setiap pengukuran memberi nilai eigen yang sama. **4.7** $\cos(3\phi/2)$ tidak (berubah tanda setelah satu putaran); $\cos 3\phi$ ya. **4.8** $\hat x^2$ ya; $i\hat x$ tidak (anti-Hermitian); $\hat p_x^2$ ya. **4.9** 0,20. **4.10** Ya; ya. **4.11** u; 3d → 4s g → g, terlarang; 3d → 4p g → u, diizinkan. **4.12** Sekitar 100 kali; tidak pernah. **4.13** Postulat 3 (dengan Postulat 2); Postulat 6. **4.14** (a) $\langle\psi|\psi\rangle = 1$; (b) $\langle\phi|\psi\rangle = 0$; (c) $\langle\psi|\hat H|\psi\rangle$; (d) $|\langle n|\psi\rangle|^2$.

# Pertanyaan

1. Mengapa operator besaran fisis harus linear? Apa hubungannya dengan asas superposisi?
2. Mengapa urutan operator penting? Beri contoh dua operator yang tidak komut dan makna fisisnya.
3. Apa arti degenerasi, dan mengapa kita bebas memilih basis dalam ruang terdegenerasi?
4. Orbital $p_x$ dan $p_{+1}$: mana yang "benar"? Kapan masing-masing lebih berguna?
5. Mengapa operator momentum memuat $i$?
6. Mengapa suku tolakan elektron–elektron mencegah pemisahan variabel dalam atom berelektron banyak?
7. Bagaimana simetri menghasilkan degenerasi, dan bagaimana penurunan simetri memecahnya? Beri contoh kimia.
8. Mengapa elektron dalam logam hampir tidak menyumbang pada kapasitas kalor, padahal jumlahnya sangat banyak?
9. Apa beda nilai harap dan nilai eigen? Kapan keduanya sama?
10. Dalam arti apa mekanika Newton adalah limit mekanika kuantum (teorema Ehrenfest)?
11. Mengapa fungsi gelombang harus bernilai tunggal? Apa akibatnya bagi momentum sudut?
12. Mengapa nilai eigen operator Hermitian riil? Mengapa fungsi eigennya ortogonal?
13. Apa arti kelengkapan, dan mengapa dalam praktik basis selalu dipotong? Apa akibatnya?
14. Mengapa dua besaran yang operatornya komut dapat diukur serentak dengan tajam?
15. Bagaimana relasi ketidakpastian Heisenberg mengikuti dari komutator?
16. Mengapa transisi d–d dalam kompleks oktahedral lemah? Mengapa kompleks tetrahedral lebih berwarna?
17. Apa yang terjadi pada fungsi gelombang ketika diukur? Mengapa pengukuran mengganggu?
18. Apa beda superposisi dan campuran statistik? Mengapa benda makroskopik tidak teramati dalam superposisi?
19. Sebutkan postulat-postulat mekanika kuantum dengan kalimatmu sendiri.
20. Mengapa persamaan Schrödinger dapat diubah menjadi soal diagonalisasi matriks? Apa hubungannya dengan kimia komputasi?
21. Mengapa Heisenberg dan Schrödinger, dengan matematika yang tampak berbeda, memperoleh hasil yang sama?

# Soal

%%SOAL%%

# Jawaban

%%JAWABAN%%

# Pembahasan soal terpilih

**Soal {{komut}}.** Dengan induksi dan (4.2): $[\hat x^n, \hat p_x] = \hat x^{n-1}[\hat x, \hat p_x] + [\hat x^{n-1}, \hat p_x]\hat x = i\hbar\hat x^{n-1} + [\hat x^{n-1}, \hat p_x]\hat x$. Jika $[\hat x^{n-1}, \hat p_x] = i\hbar(n - 1)\hat x^{n-2}$, maka hasilnya $i\hbar\hat x^{n-1} + i\hbar(n - 1)\hat x^{n-1} = i\hbar n\hat x^{n-1}$. Langsung juga: $(-i\hbar)[x^n(f') - (x^nf)'] = i\hbar nx^{n-1}f$. Dengan cara yang sama $[\hat x, \hat p_x^n] = i\hbar n\hat p_x^{n-1}$.

*Cara berpikir:* komutator dengan $\hat p_x$ bekerja seperti $i\hbar\,d/d\hat x$, dan komutator dengan $\hat x$ seperti $i\hbar\,d/d\hat p_x$. Untuk fungsi yang dapat diuraikan menjadi deret pangkat, $[f(\hat x), \hat p_x] = i\hbar f'(\hat x)$. Inilah jembatan antara komutator kuantum dan kurung Poisson mekanika klasik.

**Soal {{eigen2}}.** $\tfrac{d^2}{dx^2}\cos kx = -k^2\cos kx$ dan $\tfrac{d^2}{dx^2}\sin kx = -k^2\sin kx$: nilai eigen sama, $-k^2$. Kombinasi $\cos kx + i\sin kx = e^{ikx}$ memenuhi $\tfrac{d}{dx}e^{ikx} = ik\,e^{ikx}$, sedangkan $\cos kx$ sendiri tidak.

*Cara berpikir:* $d/dx$ dan $d^2/dx^2$ komut, sehingga dalam ruang terdegenerasi $\{\cos kx, \sin kx\}$ kita dapat memilih basis yang sekaligus fungsi eigen keduanya: $e^{\pm ikx}$. Untuk partikel bebas ini berarti memilih keadaan dengan momentum tertentu dalam tingkat energi yang terdegenerasi.

**Soal {{pisah}}.** $\hat H\psi = \hat H_x[X(x)Y(y)] + \hat H_y[X(x)Y(y)]$. Karena $\hat H_x$ hanya memuat $x$ dan turunan terhadap $x$, $Y(y)$ berperilaku seperti tetapan: $\hat H_x[XY] = Y\hat H_xX = E_xXY$. Begitu pula $\hat H_y[XY] = X\hat H_yY = E_yXY$. Jumlahnya $(E_x + E_y)XY$.

*Cara berpikir:* inilah alasan formal di balik pendekatan orbital: jika tolakan elektron diganti dengan medan rata-rata, Hamiltonian menjadi jumlah suku satu-elektron, fungsi gelombang menjadi hasil kali orbital, dan energi menjadi jumlah energi orbital (dengan koreksi untuk tolakan yang dihitung ganda, Bab 9).

**Soal {{fermi}}.** Tembaga: $(3\pi^2n)^{1/3} = (3\pi^2 \times 8{,}47 \times 10^{28})^{1/3} = 1{,}36 \times 10^{10}$ m⁻¹; $E_F = \hbar^2k_F^2/2m_e = 1{,}127 \times 10^{-18}$ J $= 7{,}03$ eV. Aluminium: $k_F = 1{,}75 \times 10^{10}$ m⁻¹, $E_F = 11{,}7$ eV.

*Cara berpikir:* $E_F \propto n^{2/3}$. Aluminium, dengan tiga elektron valensi tiap atom dan atom yang lebih rapat, mempunyai energi Fermi jauh lebih tinggi. Nilai-nilai ini cocok dengan lebar pita yang diukur dengan spektroskopi fotoelektron sinar-X, sebuah kemenangan model kotak tiga dimensi yang paling sederhana.

**Soal {{gausshid}}.** $\langle E\rangle(a) = \tfrac32a - 2\sqrt{2/\pi}\,a^{1/2}$. Turunkan: $\tfrac32 - \sqrt{2/\pi}\,a^{-1/2} = 0$, sehingga $a^{1/2} = \tfrac23\sqrt{2/\pi}$, $a = \tfrac{8}{9\pi} = 0{,}283$. Masukkan: $\langle E\rangle = \tfrac32\cdot\tfrac{8}{9\pi} - 2\sqrt{\tfrac2\pi}\cdot\tfrac23\sqrt{\tfrac2\pi} = \tfrac{4}{3\pi} - \tfrac{8}{3\pi} = -\tfrac{4}{3\pi} = -0{,}424\ E_h = -11{,}5$ eV.

*Cara berpikir:* fungsi Gauss tidak dapat meniru taring $e^{-r}$ di inti, sehingga energinya 15% di atas nilai tepat $-0{,}5\ E_h$, tetapi tidak pernah di bawahnya (teorema variasi, Bab 8). Di titik optimum $\langle V\rangle = -2\langle T\rangle$: teorema virial berlaku untuk fungsi uji yang dioptimalkan terhadap skala. Pengamatan ini adalah asal usul pemakaian kombinasi beberapa fungsi Gauss untuk meniru satu orbital Slater (basis STO-3G, Bab 17).

**Soal {{ehrenfest}}.** $V = -Fx$, sehingga $-\langle dV/dx\rangle = F$. Dengan (4.13): $d\langle p\rangle/dt = F$ dan $d\langle x\rangle/dt = \langle p\rangle/m$, jadi $d^2\langle x\rangle/dt^2 = F/m$.

*Cara berpikir:* untuk gaya yang tetap atau linear terhadap $x$, $\langle F(x)\rangle = F(\langle x\rangle)$ tepat, sehingga pusat paket mengikuti lintasan klasik tanpa penyimpangan, sementara lebar paketnya tetap menyebar secara kuantum. Elektron yang dipercepat dalam tabung sinar katode atau ion dalam spektrometer massa waktu terbang mengikuti mekanika Newton karena alasan ini.

**Soal {{hermit}}.** $\langle A^2\rangle = \int\psi^*\hat A(\hat A\psi)\,d\tau$. Dengan kehermitan, pindahkan satu $\hat A$ ke kiri: $= \int(\hat A\psi)^*(\hat A\psi)\,d\tau = \int|\hat A\psi|^2d\tau \ge 0$. Untuk energi kinetik, $\hat T = \hat p^2/2m$ dengan $\hat p$ Hermitian, sehingga $\langle T\rangle \ge 0$, dan sama dengan nol hanya jika $\hat p\psi = 0$, yaitu $\psi$ tetap di seluruh ruang, yang tidak dapat dinormalisasi.

*Cara berpikir:* energi kinetik setiap keadaan terikat positif. Itulah sebabnya energi keadaan dasar selalu di atas dasar potensial (energi titik nol), dan sebabnya dalam teorema virial $\langle T\rangle = -E > 0$ untuk keadaan terikat.

**Soal {{robertson}}.** $|\psi|^2 = \pi^{-1/2}e^{-x^2}$ adalah sebaran Gauss dengan $\sigma^2 = 1/2$, jadi $\Delta x = 1/\sqrt2$. $\langle p^2\rangle = \int|\psi'|^2dx = \pi^{-1/2}\int x^2e^{-x^2}dx = \tfrac12$, dan $\langle p\rangle = 0$, jadi $\Delta p = 1/\sqrt2$. Hasil kalinya $\tfrac12 = \hbar/2$.

*Cara berpikir:* keadaan dasar osilator mencapai batas Heisenberg dengan tanda sama dengan; ia adalah "keadaan paling klasik" yang mungkin. Keadaan koheren laser dan paket getaran dalam femtokimia mewarisi sifat ini.

**Soal {{laporte}}.** $[\text{Co}(\text{H}_2\text{O})_6]^{2+}$ oktahedral, mempunyai pusat inversi; transisi d–d g → g terlarang Laporte, sehingga serapannya lemah ($\varepsilon$ sekitar 5) dan warnanya pucat. Dalam HCl pekat terbentuk $[\text{CoCl}_4]^{2-}$ tetrahedral tanpa pusat inversi; orbital d bercampur dengan p sehingga transisi menjadi jauh lebih kuat ($\varepsilon$ sekitar 600), dan larutan menjadi biru tua.

*Cara berpikir:* perubahan warna merah muda → biru ini dipakai pada silika gel indikator kelembapan dan pada demonstrasi kesetimbangan Le Chatelier. Intensitasnya, bukan hanya warnanya, memberi tahu geometri.

**Soal {{ukur}}.** Dari $(1, 0)$, pengukuran $\sigma_x$ memberi $+1$ dengan peluang ½ dan meninggalkan $(1, 1)/\sqrt2$. Pengukuran $\sigma_z$ pada keadaan ini memberi $+1$ dengan peluang ½ dan meninggalkan $(1, 0)$. Pengukuran $\sigma_x$ lagi memberi $+1$ dengan peluang ½. Peluang total $1/8$.

*Cara berpikir:* setiap pengukuran operator yang tidak komut dengan sebelumnya "mengocok ulang" peluang. Jika pengukuran $\sigma_z$ di tengah dihilangkan, dua pengukuran $\sigma_x$ berurutan pasti memberi hasil sama, dan peluangnya ½. Menyisipkan pengukuran mengubah statistik: inti percobaan Stern–Gerlach berurutan (Bab 9).

**Soal {{matriks}}.** Unsur $\langle m|x|n\rangle$ dari rumus Contoh 3.24 dengan diagonal $1/2$; matriks 4 × 4 yang dihasilkan didiagonalkan dengan `numpy.linalg.eigvalsh`: 0,185; 0,395; 0,605; 0,815 (dalam $L$). Basis tiga fungsi memberi 0,235; 0,500; 0,765.

*Cara berpikir:* nilai eigen makin rapat dan makin mendekati tepi kotak ketika basis membesar, menuju spektrum malar $[0, L]$ operator posisi yang sesungguhnya. Pola nilai eigen yang simetris terhadap $L/2$ berasal dari paritas.

# Bacaan lanjut

1. I. N. Levine, *Quantum Chemistry*, edisi ke-7 (Pearson, 2014), Bab 3 dan 7. Operator, nilai harap, kotak tiga dimensi, operator Hermitian, dan postulat dengan sangat sistematis.
2. D. A. McQuarrie, *Quantum Chemistry*, edisi ke-2 (University Science Books, 2008), Bab 4. Postulat mekanika kuantum dengan banyak contoh.
3. P. Atkins dan R. Friedman, *Molecular Quantum Mechanics*, edisi ke-5 (Oxford University Press, 2011), Bab 1. Pendekatan berbasis notasi Dirac dan representasi matriks.
4. J. J. Sakurai dan J. Napolitano, *Modern Quantum Mechanics*, edisi ke-3 (Cambridge University Press, 2020), Bab 1. Dasar formal: ket, bra, operator, pengukuran, dengan percobaan Stern–Gerlach sebagai titik tolak.
5. C. Cohen-Tannoudji, B. Diu, dan F. Laloë, *Quantum Mechanics*, Jilid 1 (Wiley, 1977), Bab II–III. Uraian lengkap tentang ruang keadaan dan postulat, dengan banyak pelengkap.
