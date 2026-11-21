import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import sisip, soal
N = 6
sisip(N, '6.1', r'''
::: {.contoh}
**Contoh 6.t1 · Magneton Bohr dari arus melingkar**

Elektron yang mengorbit dengan momentum sudut $L$ setara dengan arus melingkar. Tunjukkan bahwa momen magnetnya $\mu = (e/2m_e)L$, lalu hitung nilainya untuk $L = \hbar$.

**Penyelesaian.** Elektron bermuatan $e$ dengan laju $v$ pada lingkaran berjari-jari $r$ mengitari lintasan dengan periode $T = 2\pi r/v$, sehingga arusnya $I = e/T = ev/2\pi r$. Momen magnet loop adalah arus kali luas:

$$
\mu = I\pi r^2 = \frac{ev}{2\pi r}\pi r^2 = \frac{evr}{2} = \frac{e}{2m_e}(m_evr) = \frac{e}{2m_e}L .
$$

Untuk $L = \hbar$: $\mu_B = e\hbar/2m_e = (1{,}602 \times 10^{-19})(1{,}0546 \times 10^{-34})/(2 \times 9{,}109 \times 10^{-31}) = 9{,}274 \times 10^{-24}$ J/T.

**Memahami hasil.** Perbandingan $\mu/L = e/2m_e$ (rasio giromagnetik) tidak bergantung pada jari-jari atau laju orbit, jadi hasil klasik ini tetap berlaku dalam mekanika kuantum. Satuan $\mu_B$ inilah yang mengukur kemagnetan atom, efek Zeeman (subbab 7.12), dan ESR (Bab 16). Untuk spin elektron, perbandingannya hampir dua kali lebih besar (faktor $g \approx 2$), yang tidak dapat dijelaskan secara klasik.
:::
''', 'Magneton Bohr dari arus melingkar')
sisip(N, '6.6', r'''
::: {.contoh}
**Contoh 6.t2 · Sudut kerucut momentum sudut**

Dalam model vektor, sudut antara $\mathbf L$ dan sumbu $z$ memenuhi $\cos\theta = m/\sqrt{\ell(\ell + 1)}$. Hitung semua sudut yang diizinkan untuk $\ell = 1$, 2, dan 3. Berapa sudut terkecil untuk tiap $\ell$?

**Penyelesaian.**

| $\ell$ | sudut yang diizinkan |
|---|---|
| 1 | 45,0°, 90,0°, 135,0° |
| 2 | 35,3°, 65,9°, 90,0°, 114,1°, 144,7° |
| 3 | 30,0°, 54,7°, 73,2°, 90,0°, 106,8°, 125,3°, 150,0° |

Sudut terkecil ($m = \ell$) adalah 45,0°, 35,3°, dan 30,0°.

**Memahami hasil.** Vektor momentum sudut tidak pernah sejajar sumbu $z$, karena itu akan membuat $L_x$ dan $L_y$ sama-sama tepat nol, melanggar asas ketidakpastian untuk komponen yang tidak komut. Makin besar $\ell$, makin kecil sudut terkecilnya: untuk $\ell = 100$ sudut itu tinggal 5,7°, dan pada batas klasik ($\ell$ sangat besar) momentum sudut dapat sejajar sumbu mana pun, seperti gasing biasa.
:::
''', 'Sudut kerucut momentum sudut')
sisip(N, '6.8', r'''
::: {.contoh}
**Contoh 6.t3 · Massa tereduksi molekul diatom**

Hitung massa tereduksi (dalam u) untuk ¹H₂, ¹H³⁵Cl, ²H³⁵Cl, dan ¹²C¹⁶O. Massa atom: ¹H 1,007825; ²H 2,014102; ¹²C 12,000000; ¹⁶O 15,994915; ³⁵Cl 34,968853 u.

**Penyelesaian.** $\mu = m_Am_B/(m_A + m_B)$:

| Molekul | $\mu$ (u) |
|---|---|
| ¹H₂ | 0,5039 |
| ¹H³⁵Cl | 0,9796 |
| ²H³⁵Cl | 1,9044 |
| ¹²C¹⁶O | 6,8562 |

**Memahami hasil.** Untuk hidrida dengan atom berat, $\mu$ hampir sama dengan massa hidrogen: atom berat praktis diam, dan yang berputar serta bergetar adalah hidrogen. Mengganti H dengan D hampir menggandakan $\mu$, sehingga konstanta rotasi turun hampir setengahnya dan frekuensi getaran turun dengan faktor hampir $\sqrt2$. Untuk CO, kedua atom berat dan sebanding, sehingga $\mu$ jauh dari massa salah satu atomnya.
:::
''', 'Massa tereduksi molekul diatom')
sisip(N, '6.9', r'''
::: {.contoh}
**Contoh 6.t4 · Panjang ikatan HCl dari konstanta rotasi**

Konstanta rotasi H³⁵Cl adalah $\tilde B = 10{,}593$ cm⁻¹. Hitung momen inersia dan panjang ikatannya. Perkirakan juga $\tilde B$ untuk D³⁵Cl, dengan menganggap panjang ikatannya sama.

**Penyelesaian.** $\tilde B = h/(8\pi^2cI)$, sehingga

$$
I = \frac{h}{8\pi^2c\tilde B} = \frac{6{,}626 \times 10^{-34}}{8\pi^2(2{,}998 \times 10^{10})(10{,}593)} = 2{,}642 \times 10^{-47}\ \text{kg m}^2 .
$$

Dengan $\mu = 0{,}9796$ u $= 1{,}6267 \times 10^{-27}$ kg: $r = \sqrt{I/\mu} = 1{,}275 \times 10^{-10}$ m $= 127{,}5$ pm. Untuk DCl, $\tilde B$ berbanding terbalik dengan $\mu$: $\tilde B_\text{DCl} = 10{,}593 \times 0{,}9796/1{,}9044 = 5{,}449$ cm⁻¹.

**Memahami hasil.** Spektroskopi rotasi memberi panjang ikatan dengan ketelitian sepersepuluh pikometer, jauh lebih teliti daripada difraksi sinar-X untuk molekul gas. Karena energi elektronik hampir tidak bergantung pada isotop, panjang ikatan H³⁵Cl dan D³⁵Cl hampir sama; selisih kecil yang terukur berasal dari energi titik nol getaran yang berbeda (subbab 5.10).
:::
''', 'Panjang ikatan HCl dari konstanta rotasi')
sisip(N, '6.10', r'''
::: {.contoh}
**Contoh 6.t5 · Mengukur panjang ikatan CO dari awan antarbintang**

Garis rotasi $J = 1 \to 0$ ¹²C¹⁶O teramati pada 115,2712 GHz. Hitung konstanta rotasi (GHz dan cm⁻¹) dan panjang ikatan CO.

**Penyelesaian.** Transisi $J \to J + 1$ berada pada $2B(J + 1)$; untuk $J = 0 \to 1$, $\nu = 2B$, jadi $B = 57{,}636$ GHz $= 1{,}9225$ cm⁻¹. Momen inersia $I = h/(8\pi^2B) = 1{,}456 \times 10^{-46}$ kg m², dan dengan $\mu = 6{,}8562$ u:

$$
r = \sqrt{I/\mu} = 113{,}1\ \text{pm}.
$$

**Memahami hasil.** Satu garis gelombang mikro dari awan berjarak ratusan tahun cahaya memberi panjang ikatan dengan ketelitian sepersepuluh pikometer, sama dengan di laboratorium. Ikatan CO (113 pm) lebih pendek daripada ikatan rangkap dua C=O dalam keton (± 121 pm), sesuai dengan orde ikatan tiga yang diramalkan teori orbital molekul (Bab 11).
:::

::: {.terapan}
**Kaitan kimia · Mengapa oven gelombang mikro bekerja**

Oven gelombang mikro bekerja pada 2,45 GHz, energi foton hanya 0,082 cm⁻¹ atau 1 J/mol. Ini **bukan** frekuensi resonansi rotasi air: dalam air cair molekul tidak berputar bebas, sehingga tidak ada garis tajam. Yang terjadi adalah **pemanasan dielektrik**: medan listrik yang berubah arah 2,45 miliar kali per detik terus memutar dipol air yang saling terikat oleh ikatan hidrogen, dan gesekan antarmolekul mengubah energinya menjadi kalor. Frekuensi 2,45 GHz dipilih karena menembus makanan beberapa sentimeter; frekuensi yang lebih tinggi diserap terlalu cepat di permukaan.
:::
''', 'Mengukur panjang ikatan CO dari awan')
sisip(N, '6.11', r'''
::: {.contoh}
**Contoh 6.t6 · Garis rotasi terkuat pada suhu kamar**

Tingkat rotasi yang paling banyak terisi adalah $J_\text{maks} \approx \sqrt{k_BT/2hc\tilde B} - \tfrac12$. Hitung $J_\text{maks}$ dan fungsi partisi rotasi $q \approx k_BT/hc\tilde B$ pada 298 K untuk HCl ($\tilde B = 10{,}59$ cm⁻¹) dan CO ($\tilde B = 1{,}92$ cm⁻¹).

**Penyelesaian.** Pada 298 K, $k_BT/hc = 207{,}1$ cm⁻¹.

HCl: $J_\text{maks} = \sqrt{207{,}1/21{,}19} - 0{,}5 = 2{,}6$, jadi $J = 3$ (atau 2); $q = 19{,}6$.

CO: $J_\text{maks} = \sqrt{207{,}1/3{,}85} - 0{,}5 = 6{,}8$, jadi $J = 7$; $q = 108$.

**Memahami hasil.** Molekul ringan dengan $\tilde B$ besar hanya mengisi beberapa tingkat rotasi; molekul berat mengisi puluhan. Fungsi partisi rotasi ini masuk langsung ke entropi dan tetapan kesetimbangan gas: kontribusi rotasi pada entropi molar CO pada 298 K adalah $R(\ln q + 1) \approx 47$ J K⁻¹ mol⁻¹, sekitar seperempat dari entropi standarnya.
:::
''', 'Garis rotasi terkuat pada suhu kamar')
sisip(N, '6.12', r'''
::: {.contoh}
**Contoh 6.t7 · Seberapa besar distorsi sentrifugal?**

Konstanta distorsi sentrifugal molekul diatom dapat ditaksir dari $\tilde D \approx 4\tilde B^3/\tilde\nu^2$. Untuk HCl, $\tilde B = 10{,}593$ cm⁻¹ dan $\tilde\nu = 2991$ cm⁻¹. Hitung $\tilde D$ dan bandingkan suku distorsi $\tilde DJ^2(J + 1)^2$ dengan $\tilde BJ(J + 1)$ untuk $J = 10$.

**Penyelesaian.** $\tilde D = 4(10{,}593)^3/(2991)^2 = 5{,}3 \times 10^{-4}$ cm⁻¹ (nilai terukur $5{,}3 \times 10^{-4}$ cm⁻¹). Untuk $J = 10$: $\tilde BJ(J + 1) = 1165$ cm⁻¹ dan $\tilde DJ^2(J + 1)^2 = 6{,}4$ cm⁻¹, perbandingannya 0,55%.

**Memahami hasil.** Koreksinya kecil, tetapi jauh lebih besar daripada ketelitian spektroskopi gelombang mikro (sepersejuta). Rumus taksiran ini menunjukkan hubungan yang menarik: dari spektrum rotasi saja ($\tilde B$ dan $\tilde D$) kita dapat menghitung frekuensi getaran, yaitu kekakuan ikatan, tanpa mengukur spektrum inframerah.
:::
''', 'Seberapa besar distorsi sentrifugal')
soal(N, '6.1', [r'Berapa momen magnet orbital (dalam $\mu_B$) elektron dengan $\ell = 2$, $m_\ell = -1$ sepanjang sumbu $z$? Berapa besar momen totalnya? ||| $+1\,\mu_B$ (berlawanan dengan $L_z$); $\sqrt6\,\mu_B$'])
soal(N, '6.6', [r'Berapa sudut terkecil antara $\mathbf L$ dan sumbu $z$ untuk $\ell = 10$ dan $\ell = 100$? ||| 17,5°; 5,7°'])
soal(N, '6.8', [r'Hitung massa tereduksi ¹⁴N₂ (14,003074 u) dan ¹H¹²⁷I (126,904473 u). ||| 7,0015 u; 0,9999 u'])
soal(N, '6.9', [r'Konstanta rotasi ¹H₂ adalah 60,85 cm⁻¹. Hitung panjang ikatannya. ||| 74,1 pm',
                r'Panjang ikatan ¹H¹⁹F 91,7 pm (¹⁹F: 18,998403 u). Hitung $\tilde B$. ||| 20,9 cm⁻¹'])
soal(N, '6.10', [r'Pada frekuensi berapa (GHz) garis $J = 2 \to 3$ ¹²C¹⁶O, bila $B = 57{,}636$ GHz dan distorsi diabaikan? ||| 345,8 GHz'])
soal(N, '6.11', [r'Hitung $J_\text{maks}$ untuk HCl pada 1000 K dan untuk CO pada 10 K (awan antarbintang). ||| 5,2 (J = 5); 0,85 (J = 1)'])
soal(N, '6.12', [r'Dengan $\tilde D = 5{,}3 \times 10^{-4}$ cm⁻¹, berapa geseran garis $J = 15 \to 16$ HCl akibat distorsi, $4\tilde D(J + 1)^3$? ||| 8,7 cm⁻¹'])
print('selesai')
