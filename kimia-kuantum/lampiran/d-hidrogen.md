# Lampiran D Fungsi Gelombang Atom Hidrogen

Fungsi gelombang ion mirip hidrogen dengan muatan inti $Z$ (Bab 7) adalah $\psi_{n\ell m}(r, \theta, \varphi) = R_{n\ell}(r)\,Y_\ell^m(\theta, \varphi)$, dengan energi $E_n = -Z^2/2n^2$ hartree (massa inti tak berhingga). Semua fungsi di bawah ternormalisasi, $\int_0^\infty R_{n\ell}^2r^2dr = 1$ dan $\int|Y_\ell^m|^2d\Omega = 1$; normalisasinya telah diperiksa secara numerik.

## D.1 Fungsi radial

Dengan $\rho = Zr/a_0$, setiap fungsi radial ditulis $R_{n\ell}(r) = (Z/a_0)^{3/2}f_{n\ell}(\rho)$:

| Orbital | $f_{n\ell}(\rho)$ | Simpul radial ($\rho$) |
|---|---|---|
| 1s | $2\,e^{-\rho}$ | — |
| 2s | $\dfrac{1}{2\sqrt2}(2 - \rho)\,e^{-\rho/2}$ | 2 |
| 2p | $\dfrac{1}{2\sqrt6}\rho\,e^{-\rho/2}$ | — |
| 3s | $\dfrac{2}{81\sqrt3}(27 - 18\rho + 2\rho^2)\,e^{-\rho/3}$ | 1,902; 7,098 |
| 3p | $\dfrac{4}{81\sqrt6}\rho(6 - \rho)\,e^{-\rho/3}$ | 6 |
| 3d | $\dfrac{4}{81\sqrt{30}}\rho^2e^{-\rho/3}$ | — |
| 4s | $\dfrac{1}{768}(192 - 144\rho + 24\rho^2 - \rho^3)\,e^{-\rho/4}$ | 1,872; 6,611; 15,518 |
| 4p | $\dfrac{1}{256\sqrt{15}}\rho(80 - 20\rho + \rho^2)\,e^{-\rho/4}$ | 5,528; 14,472 |
| 4d | $\dfrac{1}{768\sqrt5}\rho^2(12 - \rho)\,e^{-\rho/4}$ | 12 |
| 4f | $\dfrac{1}{768\sqrt{35}}\rho^3e^{-\rho/4}$ | — |

Banyaknya simpul radial $n - \ell - 1$; banyaknya simpul sudut $\ell$. Bentuk umum, dengan polinom Laguerre terasosiasi $L_{n-\ell-1}^{2\ell+1}$:

$$
R_{n\ell}(r) = \sqrt{\left(\frac{2Z}{na_0}\right)^3\frac{(n - \ell - 1)!}{2n\,(n + \ell)!}}\;e^{-\rho'/2}\rho'^{\,\ell}L_{n-\ell-1}^{2\ell+1}(\rho'), \qquad \rho' = \frac{2Zr}{na_0} .
$$

Untuk orbital dengan $\ell = n - 1$ (1s, 2p, 3d, 4f), jari-jari paling mungkin adalah $n^2a_0/Z$ (1, 4, 9, 16 bohr untuk hidrogen). Untuk 2s dan 3s, maksimum terbesar fungsi distribusi radial berada di 5,24 dan 13,07 bohr. Nilai harap $\langle r\rangle$, $\langle 1/r\rangle$, dan lainnya ada di Lampiran B.6.

## D.2 Harmonik bola

Dengan fase Condon–Shortley, $Y_\ell^{-m} = (-1)^mY_\ell^{m*}$:

| $\ell$ | $m$ | $Y_\ell^m(\theta, \varphi)$ |
|---|---|---|
| 0 | 0 | $\dfrac{1}{\sqrt{4\pi}}$ |
| 1 | 0 | $\sqrt{\dfrac{3}{4\pi}}\cos\theta$ |
| 1 | ±1 | $\mp\sqrt{\dfrac{3}{8\pi}}\sin\theta\,e^{\pm i\varphi}$ |
| 2 | 0 | $\sqrt{\dfrac{5}{16\pi}}(3\cos^2\theta - 1)$ |
| 2 | ±1 | $\mp\sqrt{\dfrac{15}{8\pi}}\sin\theta\cos\theta\,e^{\pm i\varphi}$ |
| 2 | ±2 | $\sqrt{\dfrac{15}{32\pi}}\sin^2\theta\,e^{\pm2i\varphi}$ |
| 3 | 0 | $\sqrt{\dfrac{7}{16\pi}}(5\cos^3\theta - 3\cos\theta)$ |
| 3 | ±1 | $\mp\sqrt{\dfrac{21}{64\pi}}\sin\theta(5\cos^2\theta - 1)\,e^{\pm i\varphi}$ |
| 3 | ±2 | $\sqrt{\dfrac{105}{32\pi}}\sin^2\theta\cos\theta\,e^{\pm2i\varphi}$ |
| 3 | ±3 | $\mp\sqrt{\dfrac{35}{64\pi}}\sin^3\theta\,e^{\pm3i\varphi}$ |

## D.3 Orbital riil

Orbital riil adalah kombinasi $Y_\ell^m$ dan $Y_\ell^{-m}$ (subbab 7.7). Dalam koordinat Kartesius pada bola satuan ($x = \sin\theta\cos\varphi$, $y = \sin\theta\sin\varphi$, $z = \cos\theta$, atau bagi dengan pangkat $r$ yang sesuai):

| Orbital | Bagian sudut | Orbital | Bagian sudut |
|---|---|---|---|
| s | $\dfrac{1}{\sqrt{4\pi}}$ | $f_{z^3}$ | $\sqrt{\dfrac{7}{16\pi}}\,z(5z^2 - 3r^2)/r^3$ |
| p$_x$, p$_y$, p$_z$ | $\sqrt{\dfrac{3}{4\pi}}\,x/r$, $\ y/r$, $\ z/r$ | $f_{xz^2}$, $f_{yz^2}$ | $\sqrt{\dfrac{21}{32\pi}}\,x(5z^2 - r^2)/r^3$, $\ y(\ldots)$ |
| $d_{z^2}$ | $\sqrt{\dfrac{5}{16\pi}}\,(3z^2 - r^2)/r^2$ | $f_{xyz}$ | $\sqrt{\dfrac{105}{4\pi}}\,xyz/r^3$ |
| $d_{xz}$, $d_{yz}$, $d_{xy}$ | $\sqrt{\dfrac{15}{4\pi}}\,xz/r^2$, $\ yz/r^2$, $\ xy/r^2$ | $f_{z(x^2-y^2)}$ | $\sqrt{\dfrac{105}{16\pi}}\,z(x^2 - y^2)/r^3$ |
| $d_{x^2-y^2}$ | $\sqrt{\dfrac{15}{16\pi}}\,(x^2 - y^2)/r^2$ | $f_{x(x^2-3y^2)}$, $f_{y(3x^2-y^2)}$ | $\sqrt{\dfrac{35}{32\pi}}\,x(x^2 - 3y^2)/r^3$, $\ y(3x^2 - y^2)/r^3$ |

Hubungan dengan fungsi kompleks: p$_z = Y_1^0$, p$_x = (Y_1^{-1} - Y_1^1)/\sqrt2$, p$_y = i(Y_1^{-1} + Y_1^1)/\sqrt2$; $d_{z^2} = Y_2^0$, $d_{xz} = (Y_2^{-1} - Y_2^1)/\sqrt2$, $d_{yz} = i(Y_2^{-1} + Y_2^1)/\sqrt2$, $d_{x^2-y^2} = (Y_2^2 + Y_2^{-2})/\sqrt2$, $d_{xy} = -i(Y_2^2 - Y_2^{-2})/\sqrt2$.

## D.4 Ringkasan tingkat energi dan sifat

| $n$ | $E_n$ ($E_h$, $Z = 1$) | $E_n$ (eV) | Degenerasi $n^2$ | Orbital |
|---|---|---|---|---|
| 1 | −0,5000 | −13,606 | 1 | 1s |
| 2 | −0,1250 | −3,401 | 4 | 2s, 2p |
| 3 | −0,0556 | −1,512 | 9 | 3s, 3p, 3d |
| 4 | −0,0313 | −0,850 | 16 | 4s, 4p, 4d, 4f |

Dengan spin, degenerasi menjadi $2n^2$. Massa tereduksi elektron–proton menurunkan semua energi dengan faktor $\mu/m_e = 0{,}999456$ (subbab 7.4), dan struktur halus memecah tingkat dengan $j$ berbeda (subbab 9.13).
