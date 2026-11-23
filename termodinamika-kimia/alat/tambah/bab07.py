import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import sisip, soal
N = 7
print(sisip(N, '7.3', r'''::: {.contoh}
**Contoh 7.t1 · Kantong dingin instan**

Kantong dingin untuk cedera olahraga berisi amonium nitrat padat dan sekantong air. Ketika kantong ditekan, garam itu larut dan kantong menjadi dingin. Untuk pelarutan NH₄NO₃, $\Delta H = +25{,}7$ kJ mol⁻¹ dan $\Delta S = +108{,}7$ J K⁻¹ mol⁻¹. Tunjukkan bahwa pelarutan ini spontan pada 25 °C, dan tentukan suhu di bawah mana ia tidak lagi spontan.

**Penyelesaian.** Pada 298,15 K:
$$
\Delta G = 25{,}7 - (298{,}15)(0{,}1087) = 25{,}7 - 32{,}4 = -6{,}7\ \text{kJ mol}^{-1} .
$$
Batasnya adalah suhu tempat Δ*G* = 0: $T = \Delta H/\Delta S = 25{,}7/0{,}1087 = 236$ K, atau sekitar −37 °C.

**Memahami hasil.** Pelarutan ini **menyerap** kalor dan tetap berlangsung sendiri, karena ion-ion yang tersebar di dalam air mempunyai entropi jauh lebih besar daripada kisi kristal yang teratur. Energi untuk mendinginkan kantong "dibayar" oleh entropi. Contoh ini menghapus anggapan lama bahwa proses spontan harus melepaskan kalor; yang menentukan adalah tanda Δ*G*, bukan tanda Δ*H*.
:::''', 'Kantong dingin instan'))

print(sisip(N, '7.4', r'''::: {.terapan}
**Terapan: reaksi berpasangan dalam sel.** Banyak reaksi yang diperlukan sel hidup mempunyai Δ*G* positif, misalnya pembentukan glutamin dari glutamat dan amonia ($\Delta G^{\circ\prime} = +14{,}2$ kJ mol⁻¹). Sel tidak dapat melanggar hukum kedua, tetapi dapat **memasangkan** reaksi yang tidak spontan dengan reaksi yang sangat spontan, yaitu hidrolisis ATP ($-30{,}5$ kJ mol⁻¹). Enzim glutamin sintetase melakukannya lewat zat antara bersama: glutamat lebih dulu bereaksi dengan ATP membentuk glutamil fosfat, yang kemudian bereaksi dengan amonia. Reaksi bersihnya
$$
\text{glutamat} + \text{NH}_3 + \text{ATP} \to \text{glutamin} + \text{ADP} + \text{P}_\text{i} , \qquad \Delta G^{\circ\prime} = 14{,}2 - 30{,}5 = -16{,}3\ \text{kJ mol}^{-1} .
$$
Karena *G* fungsi keadaan, Δ*G* reaksi bersih adalah jumlah Δ*G* kedua tahap. Pasangan ini bukan sekadar "menjumlahkan di atas kertas": tanpa zat antara bersama, energi ATP akan lepas sebagai kalor dan tidak dapat menggerakkan pembentukan glutamin. (Tanda aksen pada $\Delta G^{\circ\prime}$ menandai keadaan standar biokimia, pH 7, yang dibahas di Bab 10.)
:::

::: {.contoh}
**Contoh 7.t2 · Berapa foton untuk satu glukosa?**

Fotosintesis membalik pembakaran glukosa: $6\text{CO}_2 + 6\text{H}_2\text{O} \to \text{C}_6\text{H}_{12}\text{O}_6 + 6\text{O}_2$, dengan $\Delta_\text{r}G^\circ = +2879$ kJ mol⁻¹. Energi didatangkan oleh cahaya merah 680 nm. (a) Hitung energi satu mol foton itu. (b) Berapa mol foton paling sedikit yang diperlukan per mol glukosa? (c) Tumbuhan sebenarnya memakai sekitar 48 foton per glukosa. Berapa efisiensinya?

**Penyelesaian.** (a) $E_\text{m} = N_\text{A}hc/\lambda = (6{,}022 \times 10^{23})(6{,}626 \times 10^{-34})(2{,}998 \times 10^8)/(680 \times 10^{-9})$ J mol⁻¹ $= 175{,}9$ kJ mol⁻¹.

(b) Kerja bukan-ekspansi yang diberikan cahaya harus paling sedikit $\Delta_\text{r}G^\circ$: $2879/175{,}9 = 16{,}4$, jadi paling sedikit 17 mol foton.

(c) $2879/(48 \times 175{,}9) = 0{,}34$, atau 34%.

**Memahami hasil.** Energi Gibbs memberi batas bawah yang tidak dapat ditawar: tidak ada mekanisme, sepandai apa pun, yang membuat glukosa dengan kurang dari 17 foton merah. Tumbuhan memakai hampir tiga kali lipat, karena setiap tahap pemindahan elektron harus cukup "menurun" (Δ*G* negatif) agar berlangsung cepat dan tidak balik. Kehilangan itu harga yang dibayar untuk laju, tema yang akan kita temui lagi pada sel elektrokimia.
:::''', 'Berapa foton untuk satu glukosa'))

print(sisip(N, '7.6', r'''::: {.contoh}
**Contoh 7.t3 · Energi yang diperlukan untuk menjauhkan molekul**

Satu mol N₂ ($a = 1{,}370$ L² bar mol⁻²) memuai secara isotermal dari 1,00 L ke 10,0 L. Hitung Δ*U* menurut persamaan van der Waals.

**Rencana.** Tekanan dalam $\pi_T = (\partial U/\partial V)_T = an^2/V^2$ diintegralkan terhadap volume.

**Penyelesaian.**
$$
\Delta U = \int_{V_1}^{V_2}\frac{an^2}{V^2}dV = an^2\left(\frac{1}{V_1} - \frac{1}{V_2}\right) = (1{,}370)(1)\left(1 - 0{,}100\right)\ \text{L bar} = 1{,}233\ \text{L bar} = 123\ \text{J} .
$$

**Memahami hasil.** Untuk gas ideal, Δ*U* proses ini nol. Gas nyata memerlukan 123 J untuk menarik molekul-molekulnya saling menjauh. Bila ekspansi itu berlangsung ke dalam vakum tanpa kalor dari luar (ekspansi Joule), energi itu diambil dari gerak molekul sendiri, sehingga gas sedikit mendingin. Bandingkan dengan energi kinetik translasi $\tfrac32RT = 3{,}7$ kJ mol⁻¹ pada 298 K: pendinginannya kecil, sekitar 3%, tetapi nyata dan terukur.
:::''', 'Energi yang diperlukan untuk menjauhkan molekul'))

print(sisip(N, '7.8', r'''::: {.contoh}
**Contoh 7.t4 · Tekanan uap air dari tabel energi Gibbs**

Untuk $\text{H}_2\text{O}(l) \to \text{H}_2\text{O}(g)$ pada 298,15 K, $\Delta_\text{vap}G^\circ = +8{,}55$ kJ mol⁻¹. Pada tekanan uap berapa air cair dan uapnya berada dalam kesetimbangan?

**Penyelesaian.** *G* cairan hampir tidak bergantung pada tekanan, sedangkan $G_\text{m}$ uap mengikuti $G_\text{m}^\circ + RT\ln(p/p^\circ)$. Kesetimbangan berarti $\Delta G = 0$:
$$
0 = \Delta_\text{vap}G^\circ + RT\ln\frac{p}{p^\circ} \quad\Rightarrow\quad p = p^\circ\exp\left(-\frac{\Delta_\text{vap}G^\circ}{RT}\right) = (1\ \text{bar})\exp\left(-\frac{8550}{(8{,}314)(298{,}15)}\right) = 0{,}0317\ \text{bar} .
$$

**Memahami hasil.** Hasilnya 3,17 kPa, tepat tekanan uap air pada 25 °C yang tercantum di tabel. $\Delta_\text{vap}G^\circ$ positif **tidak** berarti air tidak menguap; artinya air tidak menguap menjadi uap **bertekanan 1 bar**. Selama tekanan parsial uap di udara di bawah 3,17 kPa, Δ*G* penguapan negatif dan air di gelas terbuka terus menguap. Inilah gagasan inti Bab 9: kesetimbangan tercapai ketika suku $RT\ln p$ tepat menghapus $\Delta G^\circ$.
:::''', 'Tekanan uap air dari tabel'))

print(sisip(N, '7.9', r'''::: {.contoh}
**Contoh 7.t5 · Metana yang terurai pada suhu tinggi**

Untuk metana, $\Delta_\text{f}H^\circ = -74{,}81$ kJ mol⁻¹; entropi standar CH₄(g), C(grafit), dan H₂(g) berturut-turut 186,26; 5,74; dan 130,68 J K⁻¹ mol⁻¹. Anggap Δ*H* dan Δ*S* tidak bergantung pada suhu. (a) Hitung $\Delta_\text{f}G^\circ$ CH₄ pada 1000 K. (b) Di atas suhu berapa metana tidak stabil terhadap unsur-unsurnya?

**Penyelesaian.** $\Delta_\text{f}S^\circ = 186{,}26 - 5{,}74 - 2(130{,}68) = -80{,}84$ J K⁻¹ mol⁻¹.

(a) $\Delta_\text{f}G^\circ(1000\ \text{K}) = -74{,}81 - (1000)(-0{,}080\,84) = +6{,}0$ kJ mol⁻¹.

(b) $T = 74{,}81/0{,}080\,84 = 925$ K.

**Memahami hasil.** Pada suhu kamar metana stabil ($\Delta_\text{f}G^\circ = -50{,}7$ kJ mol⁻¹), tetapi di atas sekitar 650 °C ia cenderung terurai menjadi karbon dan hidrogen, karena tiga molekul gas lebih kacau daripada satu molekul gas dan padatan. Kecenderungan ini dimanfaatkan dalam **pirolisis metana**, cara membuat hidrogen tanpa melepaskan CO₂: karbonnya tertinggal sebagai padatan. Stabilitas termodinamika bukan sifat tetap suatu senyawa; ia selalu "pada suhu berapa".
:::''', 'Metana yang terurai'))

soal(N, '7.2', [r'Dua mol gas ideal memuai secara isotermal pada 300 K dari 5,0 L ke 25,0 L. Hitung Δ*A* dan kerja maksimumnya. ||| −8,03 kJ; 8,03 kJ'])
soal(N, '7.3', [r'Tunjukkan bahwa pelarutan NH₄NO₃ (Contoh 7.t1) tidak spontan pada −50 °C. Berapa Δ*G*-nya? ||| +1,4 kJ mol⁻¹',
                r'Reaksi dengan Δ*H* < 0 dan Δ*S* < 0 spontan pada suhu rendah atau tinggi? Berikan satu contoh. ||| suhu rendah; misalnya pembekuan air'])
soal(N, '7.4', [r'Sebuah reaksi biosintesis mempunyai $\Delta G^{\circ\prime} = +50$ kJ mol⁻¹. Berapa molekul ATP paling sedikit yang harus dihidrolisis bersamanya agar reaksi bersihnya spontan? ||| 2 (bersih −11 kJ mol⁻¹)',
                r'Hitung energi satu mol foton 700 nm. Berapa mol foton itu paling sedikit untuk membuat satu mol glukosa? ||| 170,9 kJ mol⁻¹; 17'])
soal(N, '7.6', [r'Satu mol CO₂ ($a = 3{,}640$ L² bar mol⁻²) memuai secara isotermal dari 0,500 L ke 5,00 L. Hitung Δ*U* menurut van der Waals. ||| +655 J'])
soal(N, '7.8', [r'Untuk benzena, $\Delta_\text{f}G^\circ$ cair dan gas berturut-turut 124,3 dan 129,7 kJ mol⁻¹. Taksir tekanan uap benzena pada 25 °C. ||| 0,113 bar'])
soal(N, '7.9', [r'Dengan data Contoh 7.t5, hitung $\Delta_\text{f}G^\circ$ CH₄ pada 1200 K. ||| +22,2 kJ mol⁻¹'])
