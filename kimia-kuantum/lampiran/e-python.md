# Lampiran E Python untuk Kimia Kuantum

Sejak Bab 5, banyak contoh dalam buku ini memakai potongan program Python. Lampiran ini mengumpulkan alat-alat dasar yang diperlukan: NumPy untuk larik dan aljabar linear, SciPy untuk integrasi dan persamaan nilai eigen, dan Matplotlib untuk grafik. Semua potongan program di bawah telah dijalankan (Python 3 dengan NumPy 2), dan keluarannya dicantumkan.

## E.1 Persiapan

Pasang pustaka yang diperlukan dengan `pip install numpy scipy matplotlib`. Untuk kimia kuantum yang lebih serius, pustaka sumber terbuka **PySCF** (seluruhnya dalam Python) dan **Psi4** menyediakan Hartree–Fock, DFT, MP2, dan *coupled-cluster* dengan antarmuka Python; **ASE** membantu membangun dan memanipulasi struktur molekul. Program pendamping Bab 17 (folder `bab17/kode`) memperlihatkan cara semua itu bekerja dari dasar.

Tiga kebiasaan menghindarkan sebagian besar kesalahan: (1) bekerja dalam **satuan atom** di dalam program dan mengonversi hanya di akhir (Lampiran A); (2) memakai **operasi larik** NumPy alih-alih perulangan Python, yang puluhan sampai ratusan kali lebih cepat; (3) selalu memeriksa program dengan kasus yang jawabannya diketahui (atom hidrogen, osilator harmonik, partikel dalam kotak) sebelum memakainya untuk soal baru.

## E.2 Larik dan integrasi pada kisi

Fungsi gelombang dinyatakan sebagai larik nilai pada kisi titik. Integrasi dengan aturan trapesium:

```python
import numpy as np
r = np.linspace(0, 10, 2001)          # kisi r (bohr)
psi = np.exp(-r) / np.sqrt(np.pi)     # orbital 1s hidrogen
P = 4 * np.pi * r**2 * psi**2         # fungsi distribusi radial
print(np.trapezoid(P, r))             # normalisasi
print(np.trapezoid(r * P, r))         # <r> = 1,5 bohr
print(r[np.argmax(P)])                # jari-jari paling mungkin
```

Keluaran: 0,9999995; 1,4999952; 1,0. Selisih kecil dari 1 dan 1,5 berasal dari kisi yang berhenti di $r = 10$; memperpanjang kisi menghilangkannya. (Pada NumPy versi 1, fungsi ini bernama `np.trapz`.)

Untuk integral yang lebih teliti, `scipy.integrate.quad` memakai kuadratur adaptif dan memberi taksiran galatnya:

```python
import numpy as np
from scipy.integrate import quad, dblquad
f = lambda r: r**4 * np.exp(-2 * r) * 4          # <r^2> untuk 1s
print(quad(f, 0, np.inf))                        # (nilai, taksiran galat)
# rata-rata cos^2(theta) pada bola satuan
g = lambda th, ph: np.cos(th)**2 * np.sin(th) / (4 * np.pi)
print(dblquad(g, 0, 2 * np.pi, 0, np.pi)[0])
```

Keluaran: $(3{,}0000,\ 2{,}2 \times 10^{-9})$ dan 0,33333. Hasil pertama adalah $\langle r^2\rangle = 3a_0^2$; yang kedua adalah $\langle\cos^2\theta\rangle = \tfrac13$, yang muncul dalam perataan interaksi dipol (subbab 16.5). Perhatikan urutan argumen `dblquad`: fungsi menerima variabel dalam lebih dahulu.

## E.3 Nilai eigen dan vektor eigen

Hampir setiap masalah kimia kuantum berakhir dengan diagonalisasi matriks. Untuk matriks simetris (Hermitian), selalu pakai `numpy.linalg.eigh`, yang lebih cepat dan lebih stabil daripada `eig` dan mengembalikan nilai eigen terurut naik. Contoh: metode Hückel untuk butadiena (subbab 13.5).

```python
import numpy as np
n = 4                                  # butadiena: rantai 4 karbon
H = np.zeros((n, n))
for i in range(n - 1):
    H[i, i + 1] = H[i + 1, i] = 1.0    # satuan beta, alfa = 0
x, C = np.linalg.eigh(H)
print(np.round(x[::-1], 4))            # E = alfa + x beta (beta < 0)
print(np.round(C[:, -1], 4))           # koefisien orbital terendah
```

Keluaran: $x = 1{,}618;\ 0{,}618;\ -0{,}618;\ -1{,}618$ dan koefisien orbital terendah $0{,}3717;\ 0{,}6015;\ 0{,}6015;\ 0{,}3717$. Karena $\beta < 0$, nilai $x$ terbesar adalah orbital berenergi terendah.

Untuk basis yang tidak ortogonal diperlukan masalah nilai eigen **diperumum** $\mathbf H\mathbf C = \mathbf S\mathbf C\mathbf E$ (subbab 8.4 dan 17.3), yang ditangani `scipy.linalg.eigh` dengan dua argumen:

```python
import numpy as np
from scipy.linalg import eigh
H = np.array([[-1.1204, -0.9584], [-0.9584, -1.1204]])   # Hcore H2/STO-3G
S = np.array([[1.0, 0.6593], [0.6593, 1.0]])
e, C = eigh(H, S)                      # HC = SCe
print(np.round(e, 4))
print(np.round(C[:, 0], 4))
```

Keluaran: nilai eigen $-1{,}2528$ dan $-0{,}4755$, dengan vektor eigen terendah $(-0{,}5489, -0{,}5489)$, ternormalisasi dalam metrik $\mathbf S$ (tanda keseluruhan vektor eigen sembarang).

## E.4 Persamaan Schrödinger satu dimensi dengan beda hingga

Turunan kedua pada kisi seragam berjarak $h$ dihampiri dengan $\psi''_i \approx (\psi_{i+1} - 2\psi_i + \psi_{i-1})/h^2$. Hamiltonian menjadi matriks tridiagonal, dan keadaan-keadaan terendahnya diperoleh dengan diagonalisasi. Untuk osilator harmonik (satuan $\hbar = m = \omega = 1$):

```python
import numpy as np
from scipy.linalg import eigh_tridiagonal
L, N = 8.0, 2000                       # satuan hbar = m = omega = 1
x = np.linspace(-L, L, N); h = x[1] - x[0]
V = 0.5 * x**2
diag = 1.0 / h**2 + V                  # -1/2 d2/dx2 dengan beda hingga tiga titik
off = -0.5 / h**2 * np.ones(N - 1)
E, psi = eigh_tridiagonal(diag, off, select='i', select_range=(0, 4))
print(np.round(E, 5))
```

Keluaran: 0,5; 1,49999; 2,49997; 3,49995; 4,49992, sesuai $E_v = v + \tfrac12$ dengan galat $O(h^2)$. Ganti satu baris `V = ...` untuk potensial lain: Morse, kotak, sumur ganda inversi amonia. Metode tembak dengan rumus Numerov (subbab 5.12 dan 7.13) memberi ketelitian $O(h^4)$ dan lebih cocok untuk satu atau beberapa keadaan.

## E.5 Metode variasi linear dengan basis Gauss

Contoh berikut menggabungkan metode variasi linear (subbab 8.4) dan basis Gauss (subbab 17.5): atom hidrogen dengan himpunan fungsi Gauss $s$ "berjenjang genap" (eksponen membentuk deret geometri). Integral antara dua fungsi Gauss $s$ di pusat yang sama: $S = (\pi/p)^{3/2}$, $T = 3ab/p\cdot S$, $V = -2\pi/p$ dengan $p = a + b$ (Lampiran B.2).

```python
import numpy as np
from scipy.linalg import eigh
alfa = 0.05 * 3.0**np.arange(10)       # basis Gauss "even-tempered"
a, b = np.meshgrid(alfa, alfa); p = a + b
S = (np.pi / p)**1.5                   # tumpang tindih
T = 3 * a * b / p * S                  # energi kinetik
V = -2 * np.pi / p                     # tarikan inti Z = 1
for n in [1, 2, 4, 6, 10]:
    E = eigh((T + V)[:n, :n], S[:n, :n], eigvals_only=True)
    print(n, round(E[0], 6))
```

Keluaran: $n = 1$: $-0{,}281825$; 2: $-0{,}393044$; 4: $-0{,}489772$; 6: $-0{,}499503$; 10: $-0{,}499981\ E_h$. Energi turun monoton menuju $-0{,}5$ (teorema variasi): dengan sepuluh fungsi Gauss, galatnya tinggal $1{,}9 \times 10^{-5}\ E_h$. Satu fungsi dengan eksponen 0,05 jauh dari optimum ($8/9\pi = 0{,}283$), itulah sebabnya energinya buruk.

## E.6 Transformasi Fourier

`numpy.fft` menghitung transformasi Fourier diskret dengan algoritme cepat. Untuk sinyal yang dicuplik dengan selang $\Delta t$, sumbu frekuensi diperoleh dengan `np.fft.fftfreq(N, dt)`, dan `np.fft.fftshift` menata ulang hasil agar frekuensi nol di tengah. Contoh lengkap untuk FID NMR ada di Contoh 16.36. Hal yang sama dipakai untuk spektrum inframerah dari fungsi korelasi dipol dalam simulasi dinamika molekul, dan untuk menghitung spektrum dari paket gelombang (subbab 3.5).

## E.7 Grafik dengan koma desimal

Buku ini memakai koma desimal. Matplotlib dapat diatur agar label sumbu mengikutinya:

```python
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
koma = FuncFormatter(lambda v, pos: ('%g' % v).replace('.', ','))
r = np.linspace(0, 20, 500)
fig, ax = plt.subplots(figsize=(4, 3))
P = {1: 4 * r**2 * np.exp(-2 * r),                # P(r) = r^2 R(r)^2, orbital 1s
     2: r**2 * (2 - r)**2 * np.exp(-r) / 8}       # dan orbital 2s
for n, f in P.items():
    ax.plot(r, f, label=f'{n}s')
ax.xaxis.set_major_formatter(koma); ax.yaxis.set_major_formatter(koma)
ax.set_xlabel('r (bohr)'); ax.set_ylabel('P(r)'); ax.legend()
fig.savefig('radial.png', dpi=220, bbox_inches='tight')
```

Baris `matplotlib.use('Agg')` diperlukan bila program dijalankan tanpa layar (misalnya di server); hapus bila bekerja dalam Jupyter.

## E.8 Ringkasan fungsi yang paling sering dipakai

| Tugas | Fungsi |
|---|---|
| Kisi titik | `np.linspace`, `np.arange`, `np.meshgrid` |
| Integral pada kisi | `np.trapezoid`, `scipy.integrate.simpson` |
| Integral adaptif | `scipy.integrate.quad`, `dblquad`, `tplquad` |
| Nilai eigen matriks simetris | `np.linalg.eigh`, `scipy.linalg.eigh(A, B)` |
| Nilai eigen tridiagonal | `scipy.linalg.eigh_tridiagonal` |
| Sistem persamaan linear | `np.linalg.solve` |
| Kontraksi tensor (integral dua elektron) | `np.einsum` |
| Akar dan minimum | `scipy.optimize.brentq`, `root`, `minimize`, `minimize_scalar` |
| Fungsi khusus | `scipy.special` (`erf`, `gamma`, `gammainc`, `eval_hermite`, `genlaguerre`, `sph_harm_y`) |
| Persamaan diferensial biasa | `scipy.integrate.solve_ivp` |
| Transformasi Fourier | `np.fft.fft`, `fftfreq`, `fftshift` |
| Tetapan fisika | `scipy.constants` (nilai CODATA) |

Untuk transformasi integral dua elektron dari basis atom ke basis orbital molekul, `np.einsum('pqrs,pi,qj,rk,sl->ijkl', I, C, C, C, C, optimize=True)` melakukan transformasi empat indeks dalam satu baris; argumen `optimize=True` membuatnya berskala $N^5$ alih-alih $N^8$. Baris inilah inti program MP2 dan *coupled-cluster* di folder kode Bab 17.
