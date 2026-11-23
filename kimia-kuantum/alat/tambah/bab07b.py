import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import sisip, soal
N = 7
sisip(N, '7.2', r'''
::: {.dalam}
**Lebih dalam · Mengapa energi tidak bergantung pada $m$**

Dalam persamaan radial, bilangan kuantum magnetik $m$ tidak muncul sama sekali; yang muncul hanya $\ell(\ell + 1)$ dari operator $\hat L^2$. Alasannya adalah simetri: potensial Coulomb hanya bergantung pada jarak $r$, sehingga memutar sistem tidak mengubah energinya. Bilangan $m$ hanya menyatakan arah momentum sudut terhadap sumbu $z$ yang kita pilih sendiri; karena sumbu $z$ tidak istimewa, semua arah berenergi sama. Itulah sebabnya setiap tingkat dengan $\ell$ tertentu selalu mempunyai degenerasi $2\ell + 1$, untuk **semua** potensial sentral, bukan hanya Coulomb. Degenerasi ini baru pecah bila ada sesuatu yang memilih arah, misalnya medan magnet luar (efek Zeeman, subbab 7.12) atau medan ligan dalam kristal (Bab 14).
:::

::: {.contoh}
**Contoh 7.t9 · Menghitung keadaan dalam setiap kulit**

Daftarkan semua kombinasi $(\ell, m)$ untuk $n = 1$ sampai 4 dan tunjukkan bahwa banyaknya keadaan ruang dalam kulit ke-$n$ adalah $n^2$.

**Penyelesaian.** Untuk setiap $\ell$ ada $2\ell + 1$ nilai $m$, dan $\ell$ berjalan dari 0 sampai $n - 1$:

| $n$ | subkulit | banyak keadaan |
|---|---|---|
| 1 | 1s (1) | 1 |
| 2 | 2s (1), 2p (3) | 4 |
| 3 | 3s (1), 3p (3), 3d (5) | 9 |
| 4 | 4s (1), 4p (3), 4d (5), 4f (7) | 16 |

Secara umum $\sum_{\ell=0}^{n-1}(2\ell + 1) = n^2$, karena jumlah $n$ bilangan ganjil pertama adalah $n^2$.

**Memahami hasil.** Dengan dua arah spin (Bab 9), setiap kulit memuat $2n^2$ elektron: 2, 8, 18, 32. Angka-angka itu muncul sebagai panjang periode tabel periodik (2, 8, 8, 18, 18, 32, 32), walaupun dalam atom berelektron banyak urutan pengisiannya mengikuti energi, bukan $n$ saja.
:::
''', 'Mengapa energi tidak bergantung pada')
sisip(N, '7.3', r'''
::: {.contoh}
**Contoh 7.t10 · Membangun dan menormalkan $R_{20}$**

Dengan rekursi deret untuk $n = 2$, $\ell = 0$, fungsi radialnya berbentuk $R_{20} = N(1 - r/2)e^{-r/2}$ (satuan bohr). Tentukan konstanta normalisasi $N$ dan letak simpulnya.

**Penyelesaian.** Syarat normalisasi $\int_0^\infty R^2r^2\,dr = 1$. Dengan $\int_0^\infty r^ke^{-r}dr = k!$:

$$
N^2\int_0^\infty\left(r^2 - r^3 + \tfrac14r^4\right)e^{-r}dr = N^2\left(2 - 6 + \tfrac{24}{4}\right) = 2N^2 = 1,
$$

sehingga $N = 1/\sqrt2$ dan $R_{20} = \tfrac{1}{2\sqrt2}(2 - r)e^{-r/2}$. Simpulnya di $r = 2$ bohr $= 106$ pm.

**Memahami hasil.** Integral yang tampak rumit selesai dalam satu baris karena semua suku berbentuk $r^ke^{-r}$, dan rumus faktorial menyelesaikannya. Seluruh perhitungan nilai harap atom hidrogen bekerja dengan cara yang sama. Simpul di 2 bohr memisahkan cuping dalam kecil yang menembus dekat inti dari cuping luar yang besar.
:::

::: {.dalam}
**Lebih dalam · Polinom Laguerre**

Polinom yang dihasilkan rekursi (7.9) sudah dikenal ahli matematika jauh sebelum mekanika kuantum: polinom Laguerre terasosiasi $L_{n-\ell-1}^{2\ell+1}(\rho)$ dengan $\rho = 2Zr/n$. Fungsi radial lengkapnya adalah

$$
R_{n\ell}(r) = \sqrt{\left(\frac{2Z}{n}\right)^3\frac{(n - \ell - 1)!}{2n\,(n + \ell)!}}\;e^{-\rho/2}\rho^\ell L_{n-\ell-1}^{2\ell+1}(\rho) .
$$

Rumus ini jarang perlu dihafal. Yang penting adalah strukturnya: faktor $\rho^\ell$ membuat orbital dengan $\ell > 0$ nol di inti, faktor eksponensial membuatnya meluruh di jauh, dan polinom berderajat $n - \ell - 1$ memberi tepat $n - \ell - 1$ simpul radial. Pustaka Python seperti SciPy menyediakan `scipy.special.genlaguerre` untuk menghitungnya.
:::
''', 'Membangun dan menormalkan')
sisip(N, '7.7', r'''
::: {.contoh}
**Contoh 7.t11 · Membangun $p_x$ dan $p_y$ dari orbital kompleks**

Bagian sudut orbital $p$ kompleks adalah $Y_1^{\pm1} = \mp\sqrt{3/8\pi}\,\sin\theta\,e^{\pm i\phi}$. Tunjukkan bahwa kombinasi $p_x = (Y_1^{-1} - Y_1^{1})/\sqrt2$ dan $p_y = i(Y_1^{-1} + Y_1^{1})/\sqrt2$ riil, dan tentukan arahnya.

**Penyelesaian.** Dengan $e^{\pm i\phi} = \cos\phi \pm i\sin\phi$:

$$
Y_1^{-1} - Y_1^{1} = \sqrt{\tfrac{3}{8\pi}}\sin\theta\,(e^{-i\phi} + e^{i\phi}) = 2\sqrt{\tfrac{3}{8\pi}}\sin\theta\cos\phi ,
$$

sehingga $p_x = \sqrt{3/4\pi}\,\sin\theta\cos\phi = \sqrt{3/4\pi}\,(x/r)$. Dengan cara yang sama $p_y = \sqrt{3/4\pi}\,(y/r)$. Keduanya riil, berarah sepanjang sumbu $x$ dan $y$, dan tetap ternormalkan karena $Y_1^{\pm1}$ ortonormal.

**Memahami hasil.** $p_x$ dan $p_y$ bukan fungsi eigen $\hat L_z$; masing-masing adalah campuran setara $m = +1$ dan $m = -1$. Tetapi karena keduanya mempunyai energi dan $\ell$ yang sama, campuran apa pun tetap merupakan keadaan stasioner. Kimiawan memakai orbital riil karena arahnya jelas dan cocok untuk menggambarkan ikatan; fisikawan memakai orbital kompleks bila ada medan magnet yang memilih sumbu $z$.
:::
''', 'Membangun $p_x$ dan $p_y$')
sisip(N, '7.13', r'''
::: {.contoh}
**Contoh 7.t12 · Menembak energi 1s dengan metode Numerov**

Tuliskan program Python singkat yang mencari energi keadaan dasar hidrogen dengan metode Numerov (subbab 5.12) dan pembagian dua interval, lalu bandingkan dengan nilai tepat $-0{,}5$ hartree.

**Penyelesaian.** Untuk $\ell = 0$, $u = rR$ memenuhi $u'' = -k^2(r)u$ dengan $k^2 = 2(E + 1/r)$. Program berikut mengintegrasi dari $r \approx 0$ ($u = 0$) sampai $r = 30$ bohr dan mencari $E$ yang membuat $u(30) = 0$:

```python
import numpy as np
def ujung(E, rmax=30.0, N=6000):
    h = rmax / N; r = np.arange(N + 1) * h
    k2 = np.zeros(N + 1); k2[1:] = 2 * (E + 1 / r[1:])
    u = np.zeros(N + 1); u[1] = h
    for i in range(1, N):
        u[i+1] = (2*u[i]*(1 - 5*h*h*k2[i]/12) - u[i-1]*(1 + h*h*k2[i-1]/12)) / (1 + h*h*k2[i+1]/12)
    return u[-1]
a, b = -0.6, -0.4
for _ in range(60):
    m = (a + b) / 2
    a, b = (a, m) if ujung(a) * ujung(m) < 0 else (m, b)
print(m)    # -0.49999
```

Hasilnya $E = -0{,}499\,99$ hartree, sesuai nilai tepat sampai lima angka.

**Memahami hasil.** Program yang sama menyelesaikan potensial apa pun cukup dengan mengganti satu baris `k2`. Itulah yang dilakukan pada soal potensial Yukawa di akhir bab, dan prinsip yang sama (integrasi persamaan radial dengan potensial efektif) dipakai metode Hartree–Fock atom di Bab 9.
:::
''', 'Menembak energi 1s dengan metode Numerov')
soal(N, '7.2', [r'Berapa banyak keadaan ruang (tanpa spin) dengan $n = 5$? Berapa di antaranya yang mempunyai $\ell = 3$? ||| 25; 7'])
soal(N, '7.3', [r'Normalkan $R_{21} = N\,r\,e^{-r/2}$ (satuan bohr). ||| $N = 1/(2\sqrt6)$'])
soal(N, '7.7', [r'Tunjukkan bahwa $d_{xy} \propto \sin^2\theta\sin2\phi$ adalah kombinasi $Y_2^{2}$ dan $Y_2^{-2}$. Kombinasi apa yang memberi $d_{x^2-y^2}$? ||| $d_{xy} \propto i(Y_2^{-2} - Y_2^{2})$; $d_{x^2-y^2} \propto Y_2^{2} + Y_2^{-2}$'])
soal(N, '7.13', [r'(Python) Ubah program Contoh 7.t12 untuk mencari energi 2s ($E$ antara $-0{,}2$ dan $-0{,}1$). ||| $-0{,}125$ hartree'])
print('selesai')
