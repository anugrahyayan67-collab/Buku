import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import sisip, soal
N = 4
sisip(N, '4.2', r'''
::: {.contoh}
**Contoh 4.t1 · Fungsi eigen momentum dan energi kinetik**

Periksa apakah (a) $e^{ikx}$, (b) $\sin kx$, dan (c) $e^{-x^2}$ merupakan fungsi eigen $\hat p_x = -i\hbar\,d/dx$ dan $\hat T = -(\hbar^2/2m)\,d^2/dx^2$. Bila ya, tuliskan nilai eigennya.

**Penyelesaian.**

(a) $\hat p_xe^{ikx} = \hbar k\,e^{ikx}$ dan $\hat Te^{ikx} = (\hbar^2k^2/2m)e^{ikx}$. Fungsi eigen keduanya.

(b) $\hat p_x\sin kx = -i\hbar k\cos kx$, bukan kelipatan $\sin kx$, jadi **bukan** fungsi eigen momentum. Tetapi $\hat T\sin kx = (\hbar^2k^2/2m)\sin kx$, jadi fungsi eigen energi kinetik.

(c) $\hat p_xe^{-x^2} = 2i\hbar x\,e^{-x^2}$ dan $\hat Te^{-x^2} = -(\hbar^2/2m)(4x^2 - 2)e^{-x^2}$. Bukan fungsi eigen keduanya.

**Memahami hasil.** $\sin kx = (e^{ikx} - e^{-ikx})/2i$ adalah campuran setara momentum $+\hbar k$ dan $-\hbar k$, jadi momentumnya tidak tertentu walaupun energinya tertentu. Itulah keadaan partikel dalam kotak: energinya terkuantisasi tepat, tetapi pengukuran momentum memberi $+\hbar k$ atau $-\hbar k$ dengan peluang sama. Fungsi Gauss bukan fungsi eigen operator mana pun di atas, tetapi akan menjadi fungsi eigen operator Hamilton osilator harmonik (Bab 5).
:::
''', 'Fungsi eigen momentum dan energi kinetik')
sisip(N, '4.4', r'''
::: {.contoh}
**Contoh 4.t2 · Berapa suku dalam operator Hamilton molekul air?**

Tuliskan struktur operator Hamilton lengkap molekul H₂O (10 elektron, 3 inti) dan hitung banyaknya suku energi kinetik dan suku Coulomb.

**Penyelesaian.** Energi kinetik: satu suku untuk setiap partikel, $10 + 3 = 13$ suku. Interaksi Coulomb: setiap pasangan partikel satu suku.

| Jenis pasangan | banyak suku |
|---|---|
| elektron–elektron, $\binom{10}{2}$ | 45 (tolakan) |
| elektron–inti, $10 \times 3$ | 30 (tarikan) |
| inti–inti, $\binom{3}{2}$ | 3 (tolakan) |

Jumlahnya 13 suku kinetik dan 78 suku Coulomb, dan fungsi gelombangnya bergantung pada $3 \times 13 = 39$ koordinat (ditambah spin).

**Memahami hasil.** Molekul tiga atom sudah memerlukan persamaan diferensial dalam 39 variabel; tidak ada harapan menyelesaikannya secara tepat. Seluruh sisa buku ini adalah strategi untuk menyederhanakan masalah ini: memisahkan gerak inti dari elektron (pendekatan Born–Oppenheimer, Bab 11), mengganti tolakan elektron dengan medan rata-rata (Hartree–Fock, Bab 9 dan 17), dan memanfaatkan simetri (Bab 10).
:::
''', 'Berapa suku dalam operator Hamilton molekul air')
sisip(N, '4.7', r'''
::: {.contoh}
**Contoh 4.t3 · Fungsi gelombang mana yang dapat diterima?**

Untuk partikel yang bergerak di seluruh sumbu $x$ ($-\infty < x < \infty$), mana yang dapat menjadi fungsi gelombang: (a) $e^{-x^2}$, (b) $e^{x}$, (c) $\sin x$, (d) $1/x$, (e) $e^{-|x|}$?

**Penyelesaian.**

(a) Dapat diterima: kontinu, bernilai tunggal, dan dapat dinormalkan.

(b) Tidak: membesar tanpa batas untuk $x \to \infty$, jadi tidak dapat dinormalkan.

(c) Tidak sebagai keadaan terikat: tidak dapat dinormalkan di seluruh sumbu (integral $\sin^2$ tak hingga), walaupun dapat menyatakan keadaan hamburan seperti gelombang bidang.

(d) Tidak: tak hingga di $x = 0$ dan $\int|1/x|^2dx$ divergen di sana.

(e) Dapat diterima: kontinu dan dapat dinormalkan. Turunannya melompat di $x = 0$, yang hanya diperbolehkan bila potensial di titik itu tak hingga, misalnya potensial fungsi delta $V = -\alpha\delta(x)$, yang keadaan dasarnya memang berbentuk $e^{-\kappa|x|}$.

**Memahami hasil.** Syarat-syarat ini bukan aturan formal belaka. Fungsi yang tidak dapat dinormalkan tidak dapat ditafsirkan sebagai peluang; fungsi yang turunannya melompat memberi energi kinetik tak hingga kecuali dibayar oleh potensial yang juga tak hingga. "Puncak" (*cusp*) fungsi 1s atom hidrogen di inti adalah contoh nyata: potensial Coulomb tak hingga di $r = 0$ mengizinkan turunan yang patah.
:::
''', 'Fungsi gelombang mana yang dapat diterima')
sisip(N, '4.9', r'''
::: {.contoh}
**Contoh 4.t4 · Mengekspansi fungsi parabola dalam keadaan kotak**

Partikel dalam kotak $0 \le x \le L$ berada dalam keadaan ternormalkan $\psi = \sqrt{30/L^5}\,x(L - x)$. Koefisien ekspansinya dalam keadaan eigen kotak adalah $c_n = 8\sqrt{15}/(n\pi)^3$ untuk $n$ ganjil dan 0 untuk $n$ genap. Hitung peluang pengukuran energi memberi $E_1$ dan $E_3$, periksa bahwa jumlah semua peluang 1, dan hitung $\langle E\rangle$ dalam satuan $E_1$.

**Penyelesaian.** $c_1 = 0{,}99928$, sehingga $P_1 = 0{,}99856$. $c_3 = 0{,}03701$, $P_3 = 0{,}00137$. Jumlah $\sum_{n\ \text{ganjil}}960/(n\pi)^6 = 1$ (dengan $\sum 1/n^6$ untuk $n$ ganjil $= \pi^6/960$). Energi rata-rata:

$$
\langle E\rangle = \sum_nP_nn^2E_1 = \frac{960}{\pi^6}E_1\sum_{n\ \text{ganjil}}\frac{1}{n^4} = \frac{960}{\pi^6}\cdot\frac{\pi^4}{96}E_1 = \frac{10}{\pi^2}E_1 = 1{,}0132\,E_1 .
$$

**Memahami hasil.** Parabola sangat mirip dengan gelombang sinus keadaan dasar, sehingga 99,86% peluangnya jatuh di $n = 1$, dan energi rata-ratanya hanya 1,3% di atas $E_1$. Koefisien genap nol karena parabola simetris terhadap tengah kotak, sedangkan keadaan $n$ genap antisimetris. Perhitungan yang sama, tetapi untuk fungsi uji dan Hamiltonian yang lebih rumit, adalah inti metode variasi (Bab 8): energi rata-rata fungsi uji selalu di atas energi keadaan dasar.
:::
''', 'Mengekspansi fungsi parabola dalam keadaan kotak')
sisip(N, '4.12', r'''
::: {.contoh}
**Contoh 4.t5 · Mengukur superposisi dua keadaan**

Partikel dalam kotak berada dalam keadaan $\Psi = (\psi_1 + \psi_2)/\sqrt2$. (a) Apa saja hasil pengukuran energi yang mungkin dan berapa peluangnya? (b) Berapa $\langle E\rangle$? (c) Bila pengukuran memberi $E_2$, dalam keadaan apa partikel sesudahnya, dan apa hasil pengukuran energi berikutnya?

**Penyelesaian.**

(a) Hanya $E_1$ atau $E_2$, masing-masing dengan peluang $|1/\sqrt2|^2 = \tfrac12$.

(b) $\langle E\rangle = \tfrac12E_1 + \tfrac12(4E_1) = 2{,}5\,E_1$, nilai yang tidak pernah teramati dalam satu pengukuran.

(c) Sesudah memberi $E_2$, keadaannya $\psi_2$; pengukuran berikutnya pasti memberi $E_2$ lagi.

**Memahami hasil.** Nilai harap adalah rata-rata banyak pengukuran pada sistem yang disiapkan sama, bukan hasil satu pengukuran. Pengukuran juga mengubah keadaan: sebelum diukur partikel berada dalam superposisi, sesudahnya berada dalam keadaan eigen yang sesuai dengan hasilnya. Inilah perbedaan mendasar antara superposisi kuantum dan ketidaktahuan biasa (campuran statistik).
:::
''', 'Mengukur superposisi dua keadaan')
sisip(N, '4.13', r'''
::: {.contoh}
**Contoh 4.t6 · Superposisi yang berdenyut**

Elektron dalam kotak 1,0 nm berada dalam superposisi $(\psi_1 + \psi_2)/\sqrt2$. Rapat peluangnya berubah terhadap waktu dengan frekuensi sudut $(E_2 - E_1)/\hbar$. Hitung periode denyut itu.

**Penyelesaian.** Dengan $\Psi(x,t) = [\psi_1e^{-iE_1t/\hbar} + \psi_2e^{-iE_2t/\hbar}]/\sqrt2$:

$$
|\Psi|^2 = \tfrac12\left[\psi_1^2 + \psi_2^2 + 2\psi_1\psi_2\cos\frac{(E_2 - E_1)t}{\hbar}\right].
$$

$E_1 = h^2/8m_eL^2 = 0{,}376$ eV dan $E_2 - E_1 = 3E_1 = 1{,}128$ eV. Periodenya $T = h/(E_2 - E_1) = 3{,}67$ fs.

**Memahami hasil.** Keadaan stasioner tidak berubah terhadap waktu; hanya superposisi keadaan berenergi berbeda yang "bergerak", dengan elektron berayun dari satu sisi kotak ke sisi lain. Periode beberapa femtodetik inilah skala waktu gerak elektron dalam molekul, dan pulsa laser femtodetik dan attodetik kini dapat menyiapkan dan memotret gerak seperti ini secara langsung.
:::
''', 'Superposisi yang berdenyut')
soal(N, '4.2', [r'Apakah $\cos kx$ fungsi eigen $\hat p_x^2$? Bila ya, berapa nilai eigennya? ||| Ya; $\hbar^2k^2$'])
soal(N, '4.4', [r'Berapa suku Coulomb dalam operator Hamilton lengkap molekul NH₃ (10 elektron, 4 inti)? ||| 91'])
soal(N, '4.7', [r'Mengapa $\psi = e^{i\phi/2}$ tidak dapat diterima untuk partikel pada cincin, sedangkan $e^{i\phi}$ dapat? ||| tidak bernilai tunggal: berubah tanda setelah satu putaran'])
soal(N, '4.9', [r'Untuk keadaan parabola Contoh 4.t4, berapa peluang mendapat $E_5$? ||| $6{,}4 \times 10^{-5}$'])
soal(N, '4.12', [r'Untuk $\Psi = (\psi_1 + i\psi_3)/\sqrt2$ dalam kotak, berapa $\langle E\rangle$ dalam satuan $E_1$? Apakah faktor $i$ mengubah hasilnya? ||| 5; tidak'])
soal(N, '4.13', [r'Berapa periode denyut superposisi $\psi_1$ dan $\psi_2$ untuk elektron dalam kotak 0,50 nm? ||| 0,92 fs'])
print('selesai')
