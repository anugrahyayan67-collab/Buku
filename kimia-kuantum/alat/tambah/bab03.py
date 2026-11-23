import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import sisip, soal
N = 3

print(sisip(N, '3.4', r'''::: {.awas}
**Stasioner tidak berarti diam.** Dalam keadaan stasioner rapat peluangnya tetap, dan untuk keadaan riil seperti $\psi_1$ dalam kotak $\langle p\rangle = 0$. Tetapi $\langle p^2\rangle$ tidak nol: elektron dalam keadaan dasar kotak 1,00 nm mempunyai energi kinetik 0,376 eV, setara dengan laju akar rata-rata kuadrat $\sqrt{2E_1/m_e} = 3{,}6 \times 10^5$ m/s. Yang tetap adalah **peluang**, bukan partikelnya. Gambaran "elektron diam di dalam orbital" sama kelirunya dengan gambaran "elektron mengitari inti pada lintasan".
:::

::: {.contoh}
**Contoh 3.t1 · Kebangkitan kuantum dalam kotak**

**Gambaran fisis.** Paket gelombang yang dibentuk dari banyak keadaan kotak mula-mula bergerak bolak-balik, lalu buyar karena setiap suku berputar dengan frekuensi berbeda. Apakah bentuk semula dapat kembali?

Tunjukkan bahwa superposisi **sembarang** keadaan partikel dalam kotak kembali tepat ke bentuk awalnya setelah waktu $T_\text{kb} = h/E_1$, lalu hitung $T_\text{kb}$ untuk (a) elektron dalam kotak 1,00 nm dan (b) proton dalam kotak 0,100 nm.

**Penyelesaian.** Karena $E_n = n^2E_1$, persamaan (3.10) menjadi $\Psi(x, t) = \sum_nc_n\psi_n(x)e^{-in^2E_1t/\hbar}$. Pada $t = T_\text{kb} = 2\pi\hbar/E_1 = h/E_1$, setiap faktor fase bernilai $e^{-2\pi in^2} = 1$, karena $n^2$ bilangan bulat. Jadi $\Psi(x, T_\text{kb}) = \Psi(x, 0)$, apa pun koefisien $c_n$-nya.

(a) $E_1 = 0{,}376$ eV, sehingga $T_\text{kb} = (4{,}136 \times 10^{-15}\ \text{eV·s})/(0{,}376\ \text{eV}) = 11{,}0$ fs.

(b) Untuk proton, $E_1 = h^2/8m_pL^2 = 20{,}5$ meV, dan $T_\text{kb} = 202$ fs.

**Memahami hasil.** Kebangkitan ini terjadi karena tingkat energinya berbanding **tepat** dengan bilangan bulat. Periode ayunan dua tingkat (Contoh 3.11) adalah $h/(E_2 - E_1) = T_\text{kb}/3$; periode kebangkitan adalah kelipatan persekutuan semua periode itu. Dalam molekul nyata tingkat-tingkatnya tidak tepat sebanding bilangan bulat, sehingga kebangkitannya hanya sebagian. Kebangkitan paket gelombang getaran dan rotasi molekul memang teramati dalam percobaan laser femtodetik, dan dipakai untuk mengukur tetapan molekul.
:::''', 'Kebangkitan kuantum dalam kotak'))

print(sisip(N, '3.5', r'''::: {.contoh}
**Contoh 3.t2 · Waktu lipat dua**

Berapa lama waktu yang diperlukan paket Gauss untuk melebar menjadi dua kali lebar awalnya? Hitung untuk (a) elektron dengan $\sigma_0 = 0{,}10$ nm; (b) molekul N₂ dengan $\sigma_0 = 0{,}10$ nm; (c) butir debu 1 µg dengan $\sigma_0 = 1$ µm.

**Rencana.** Dari (3.12), $\sigma = 2\sigma_0$ bila $\hbar t/2m\sigma_0^2 = \sqrt3$, sehingga $t_2 = 2\sqrt3\,m\sigma_0^2/\hbar$.

**Penyelesaian.** (a) $t_2 = 2\sqrt3\,(9{,}109 \times 10^{-31})(10^{-10})^2/(1{,}0546 \times 10^{-34}) = 3{,}0 \times 10^{-16}$ s $= 0{,}30$ fs.

(b) Massa N₂ $= 28$ u $= 4{,}65 \times 10^{-26}$ kg; $t_2 = 1{,}5 \times 10^{-11}$ s $= 15$ ps.

(c) $t_2 = 2\sqrt3\,(10^{-9})(10^{-6})^2/(1{,}0546 \times 10^{-34}) = 3{,}3 \times 10^{13}$ s, sekitar satu juta tahun.

**Memahami hasil.** Waktu lipat dua sebanding dengan $m\sigma_0^2$. Elektron yang dikurung dalam ukuran atom "lepas" dalam waktu lebih singkat daripada satu periode getaran molekul (sekitar 10 fs); molekul gas membutuhkan waktu ratusan kali selang tumbukannya; benda yang dapat dilihat dengan mikroskop tidak pernah melebar dalam waktu yang berarti. Batas antara dunia "kuantum" dan "klasik" ternyata bukan garis tajam, melainkan soal skala $m\sigma_0^2/\hbar$.
:::

::: {.contoh}
**Contoh 3.t3 · Elektron dalam tabung vakum**

Elektron berenergi 10 eV, yang dibentuk menjadi paket dengan $\sigma_0 = 1{,}0$ µm, menempuh jarak 1,0 cm dalam vakum. Berapa lama perjalanannya, dan berapa lebar paketnya ketika tiba?

**Penyelesaian.** Kecepatan grup $v = \sqrt{2E/m_e} = 1{,}88 \times 10^6$ m/s, sehingga $t = 0{,}010/v = 5{,}33$ ns. Faktor dalam (3.12): $\hbar t/2m_e\sigma_0^2 = 0{,}309$. Lebar akhirnya $\sigma = (1{,}0\ \text{µm})\sqrt{1 + 0{,}309^2} = 1{,}05$ µm.

**Memahami hasil.** Paket selebar 1 µm hampir tidak melebar selama perjalanan, sedangkan paket selebar 0,1 nm (Contoh 3.t2) melebar dua kali lipat dalam 0,3 fs. Perbedaannya berasal dari faktor $\sigma_0^2$: lebar awal $10^4$ kali lebih besar berarti pelebaran $10^8$ kali lebih lambat. Karena itu berkas elektron dalam mikroskop elektron dan tabung sinar katode dapat diperlakukan sebagai partikel yang bergerak pada lintasan, sementara elektron di dalam molekul tidak.
:::''', 'Elektron dalam tabung vakum'))

print(sisip(N, '3.9', r'''::: {.contoh}
**Contoh 3.t4 · Hukum skala sumur terhingga**

(a) Hitung $z_0$ untuk elektron dalam sumur $V_0 = 0{,}50$ eV selebar 1,0 nm. (b) Penyelesaian numerik (3.18) memberi $z = 0{,}992$ (genap) dan $z = 1{,}774$ (ganjil). Hitung kedua energinya. (c) Tanpa menghitung ulang, tentukan energi keadaan terikat sumur $V_0 = 2{,}0$ eV selebar 0,50 nm.

**Penyelesaian.** (a) $z_0 = \sqrt{2m_eV_0}\,(a/2)/\hbar$ dengan setengah lebar $0{,}50$ nm: $z_0 = 1{,}81$. Karena $\pi/2 < z_0 < \pi$, ada dua keadaan terikat.

(b) $E = \hbar^2z^2/[2m_e(a/2)^2]$. Untuk $z = 0{,}992$: $E_1 = 0{,}150$ eV. Untuk $z = 1{,}774$: $E_2 = 0{,}480$ eV, hanya 0,02 eV di bawah tepi sumur. (Bandingkan dengan sumur tak hingga 1,0 nm: 0,376 eV dan 1,50 eV.)

(c) Sumur kedua mempunyai $V_0$ empat kali lebih besar dan lebar setengahnya, sehingga $z_0 \propto a\sqrt{V_0}$ tidak berubah. Akar-akar $z$ pun sama, dan $E \propto z^2/a^2$ menjadi empat kali: 0,60 eV dan 1,92 eV.

**Memahami hasil.** Semua sumur dengan $z_0$ sama "berbentuk sama": jumlah keadaan terikatnya sama dan energinya, bila dinyatakan sebagai pecahan $V_0$, juga sama ($E/V_0 = z^2/z_0^2$; di sini 0,30 dan 0,96). Sumur 0,50 eV memberi tingkat yang jauh di bawah tingkat sumur tak hingga, karena keadaan keduanya menembus sejauh 1,4 nm ke dinding, lebih dari lebar sumur itu sendiri. Hukum skala ini berguna untuk titik kuantum: memperkecil ukuran titik sambil memperdalam sumurnya dapat mempertahankan jumlah tingkat terikat.
:::''', 'Hukum skala sumur terhingga'))

print(soal(N, '3.4', [
 r'Berapa waktu kebangkitan kuantum $T_\text{kb} = h/E_1$ untuk elektron dalam kotak 2,0 nm? ||| 44,0 fs (sebanding $L^2$)',
 r'Hitung $E_1$ dan waktu kebangkitan untuk proton dalam kotak 0,100 nm. Mengapa jauh lebih lama daripada elektron dalam kotak 1,00 nm? ||| 20,5 meV; 202 fs; $T_\text{kb} = 8mL^2/h$ sebanding massa',
]))
print(soal(N, '3.5', [
 r'Berapa waktu lipat dua paket Gauss atom He dengan $\sigma_0 = 0{,}050$ nm? ||| 0,55 ps',
 r'Elektron 100 eV dengan $\sigma_0 = 0{,}50$ µm menempuh 1,0 m dalam kolom mikroskop elektron. Berapa waktu tempuh dan lebar akhir paketnya? ||| 169 ns; 19,5 µm',
]))
print(soal(N, '3.9', [
 r'Sumur 0,50 eV selebar 2,0 nm: berapa $z_0$ dan banyaknya keadaan terikat elektron? ||| 3,62; 3 keadaan',
 r'Lebar sebuah sumur dilipatduakan dan kedalamannya dibagi empat. Apa yang terjadi pada $z_0$, banyaknya keadaan terikat, dan energi tingkat-tingkatnya? ||| $z_0$ dan banyaknya keadaan tetap; semua energi menjadi seperempatnya',
]))
