# Lampiran B Integral Penting

Semua rumus di lampiran ini telah diperiksa secara numerik. Dalam rumus-rumus berikut $a > 0$, $n$ dan $m$ bilangan bulat tak negatif, dan $n!! = n(n - 2)(n - 4)\cdots$ (dengan $(-1)!! = 0!! = 1$).

## B.1 Fungsi eksponensial

$$
\int_0^\infty x^ne^{-ax}\,dx = \frac{n!}{a^{n+1}}, \qquad \int_0^\infty x^\nu e^{-ax}\,dx = \frac{\Gamma(\nu + 1)}{a^{\nu+1}} .
$$

Rumus pertama adalah alat utama semua integral atom hidrogen dan orbital Slater (subbab 7.9). Untuk batas atas berhingga:

$$
\int_0^Rx^ne^{-ax}\,dx = \frac{n!}{a^{n+1}}\left[1 - e^{-aR}\sum_{k=0}^n\frac{(aR)^k}{k!}\right] .
$$

## B.2 Fungsi Gauss

$$
\int_{-\infty}^\infty e^{-ax^2}dx = \sqrt{\frac\pi a}, \qquad \int_{-\infty}^\infty x^2e^{-ax^2}dx = \frac{1}{2a}\sqrt{\frac\pi a}, \qquad \int_{-\infty}^\infty x^4e^{-ax^2}dx = \frac{3}{4a^2}\sqrt{\frac\pi a} .
$$

Secara umum, untuk setengah garis,

$$
\int_0^\infty x^{2n}e^{-ax^2}dx = \frac{(2n - 1)!!}{2^{n+1}a^n}\sqrt{\frac\pi a}, \qquad \int_0^\infty x^{2n+1}e^{-ax^2}dx = \frac{n!}{2a^{n+1}} ,
$$

dan integral dengan pangkat ganjil dari $-\infty$ sampai $\infty$ bernilai nol. Dalam tiga dimensi: $\int e^{-ar^2}d\mathbf r = (\pi/a)^{3/2}$ dan $\int r^2e^{-ar^2}d\mathbf r = \tfrac{3}{2a}(\pi/a)^{3/2}$.

**Teorema hasil kali Gauss** (subbab 2.2 dan 17.3):

$$
e^{-a|\mathbf r - \mathbf A|^2}e^{-b|\mathbf r - \mathbf B|^2} = e^{-\frac{ab}{a + b}|\mathbf A - \mathbf B|^2}\,e^{-(a + b)|\mathbf r - \mathbf P|^2}, \qquad \mathbf P = \frac{a\mathbf A + b\mathbf B}{a + b} .
$$

**Integral dasar fungsi Gauss $s$ tak ternormalisasi** ($p = a + b$, $q = c + d$, $K_{AB} = e^{-ab|\mathbf A - \mathbf B|^2/p}$):

| Integral | Rumus |
|---|---|
| Tumpang tindih $(a\vert b)$ | $(\pi/p)^{3/2}K_{AB}$ |
| Energi kinetik $(a\vert -\tfrac12\nabla^2\vert b)$ | $\dfrac{ab}{p}\left(3 - \dfrac{2ab}{p}\vert\mathbf A - \mathbf B\vert^2\right)(\pi/p)^{3/2}K_{AB}$ |
| Tarikan inti $(a\vert 1/r_C\vert b)$ | $\dfrac{2\pi}{p}K_{AB}F_0(p\vert\mathbf P - \mathbf C\vert^2)$ |
| Tolakan $(ab\vert cd)$ | $\dfrac{2\pi^{5/2}}{pq\sqrt{p + q}}K_{AB}K_{CD}F_0\!\left(\dfrac{pq}{p + q}\vert\mathbf P - \mathbf Q\vert^2\right)$ |

Fungsi Gauss $s$ ternormalisasi adalah $(2a/\pi)^{3/4}e^{-ar^2}$.

## B.3 Fungsi Boys dan fungsi galat

$$
F_n(t) = \int_0^1u^{2n}e^{-tu^2}du, \qquad F_n(0) = \frac{1}{2n + 1}, \qquad F_0(t) = \frac12\sqrt{\frac\pi t}\,\operatorname{erf}(\sqrt t) ,
$$

$$
F_n(t) = \frac{\Gamma(n + \tfrac12)\,P(n + \tfrac12, t)}{2t^{n+1/2}}, \qquad F_n(t) = \frac{2tF_{n+1}(t) + e^{-t}}{2n + 1} ,
$$

dengan $P$ fungsi gamma tak lengkap teregularisasi (`scipy.special.gammainc`). Untuk $t$ besar, $F_n(t) \to (2n - 1)!!\sqrt{\pi}/2^{n+1}t^{n+1/2}$. Fungsi galat $\operatorname{erf}(x) = \tfrac{2}{\sqrt\pi}\int_0^xe^{-u^2}du$ dan $1/r = \tfrac{2}{\sqrt\pi}\int_0^\infty e^{-r^2t^2}dt$.

## B.4 Fungsi trigonometri

$$
\int_0^L\sin\frac{n\pi x}{L}\sin\frac{m\pi x}{L}\,dx = \frac L2\delta_{nm}, \qquad \int_0^{2\pi}e^{i(m - m')\varphi}d\varphi = 2\pi\delta_{mm'} ,
$$

$$
\int_0^L x\sin^2\frac{n\pi x}{L}\,dx = \frac{L^2}{4}, \qquad \frac2L\int_0^Lx^2\sin^2\frac{n\pi x}{L}\,dx = L^2\left(\frac13 - \frac{1}{2n^2\pi^2}\right) .
$$

Integral sudut yang sering muncul (dengan $x = \cos\theta$, $dx = -\sin\theta\,d\theta$):

| Integral | Nilai | Integral | Nilai |
|---|---|---|---|
| $\int_0^\pi\sin\theta\,d\theta$ | 2 | $\int_0^\pi\sin^3\theta\,d\theta$ | 4/3 |
| $\int_0^\pi\cos^2\theta\sin\theta\,d\theta$ | 2/3 | $\int_0^\pi\sin^5\theta\,d\theta$ | 16/15 |
| $\int_0^\pi\cos^4\theta\sin\theta\,d\theta$ | 2/5 | $\int_0^\pi\cos^2\theta\sin^3\theta\,d\theta$ | 4/15 |

Secara umum $\int_0^\pi\sin^{2k+1}\theta\,d\theta = 2\,\dfrac{(2k)!!}{(2k + 1)!!}$ dan $\int_0^\pi\cos^{2k}\theta\sin\theta\,d\theta = \dfrac{2}{2k + 1}$.

## B.5 Koordinat bola dan harmonik bola

Elemen volume $d\tau = r^2\sin\theta\,dr\,d\theta\,d\varphi$; sudut ruang $d\Omega = \sin\theta\,d\theta\,d\varphi$, dengan $\int d\Omega = 4\pi$. Harmonik bola ortonormal (Lampiran D):

$$
\int Y_\ell^{m*}Y_{\ell'}^{m'}\,d\Omega = \delta_{\ell\ell'}\delta_{mm'}, \qquad \sum_{m=-\ell}^\ell|Y_\ell^m(\theta, \varphi)|^2 = \frac{2\ell + 1}{4\pi}\ \ \text{(teorema Unsöld)} .
$$

Ekspansi Laplace untuk tolakan dua elektron:

$$
\frac{1}{r_{12}} = \sum_{\ell=0}^\infty\frac{4\pi}{2\ell + 1}\frac{r_<^\ell}{r_>^{\ell+1}}\sum_{m=-\ell}^\ell Y_\ell^{m*}(\theta_1, \varphi_1)Y_\ell^m(\theta_2, \varphi_2) ,
$$

dengan $r_<$ dan $r_>$ yang lebih kecil dan lebih besar di antara $r_1$ dan $r_2$. Untuk dua orbital s hanya suku $\ell = 0$ yang tersisa.

## B.6 Integral atom hidrogen dan orbital Slater

Nilai harap untuk ion mirip hidrogen dengan muatan inti $Z$ (satuan atom):

| Besaran | Rumus |
|---|---|
| $\langle r\rangle$ | $\dfrac{1}{2Z}\left[3n^2 - \ell(\ell + 1)\right]$ |
| $\langle r^2\rangle$ | $\dfrac{n^2}{2Z^2}\left[5n^2 + 1 - 3\ell(\ell + 1)\right]$ |
| $\langle 1/r\rangle$ | $\dfrac{Z}{n^2}$ |
| $\langle 1/r^2\rangle$ | $\dfrac{Z^2}{n^3(\ell + \tfrac12)}$ |
| $\langle 1/r^3\rangle$ ($\ell \geq 1$) | $\dfrac{Z^3}{n^3\ell(\ell + \tfrac12)(\ell + 1)}$ |
| $\vert\psi_{ns}(0)\vert^2$ | $\dfrac{Z^3}{\pi n^3}$ |

Integral dua pusat untuk orbital 1s Slater ($\zeta = 1$) pada atom A dan B yang berjarak $R$ (subbab 11.4):

| Integral | Rumus |
|---|---|
| Tumpang tindih $S = \langle 1s_A\vert 1s_B\rangle$ | $e^{-R}\left(1 + R + \tfrac13R^2\right)$ |
| Coulomb $\langle 1s_A\vert 1/r_B\vert 1s_A\rangle$ | $\dfrac1R - e^{-2R}\left(1 + \dfrac1R\right)$ |
| Pertukaran $\langle 1s_A\vert 1/r_A\vert 1s_B\rangle$ | $e^{-R}(1 + R)$ |
| Tolakan satu pusat $(1s1s\vert 1s1s)$ | $\tfrac58\zeta$ |

Untuk eksponen $\zeta$ sembarang, ganti $R$ dengan $\zeta R$ dalam ketiga rumus pertama dan kalikan integral Coulomb dan pertukaran dengan $\zeta$.

## B.7 Deret dan rumus lain yang berguna

$$
\sum_{v=0}^\infty e^{-vx} = \frac{1}{1 - e^{-x}}, \qquad \sum_{J=0}^\infty(2J + 1)e^{-J(J+1)x} \approx \frac1x + \frac13 + \frac{x}{15}\quad(x \ll 1) ,
$$

$$
\sum_{m=-j}^jm^2 = \tfrac13j(j + 1)(2j + 1), \qquad n! \approx \sqrt{2\pi n}\,(n/e)^n, \qquad \ln n! \approx n\ln n - n .
$$
