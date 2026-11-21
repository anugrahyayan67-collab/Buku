import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import soal, tanya, bahas
N = 6
S = {
'6.1': ['Hitung Δ*S* untuk 1,00 mol argon yang dipanaskan dari 300 K ke 600 K pada volume tetap, lalu bila sekaligus volumenya menjadi dua kali. ||| +8,64 J K⁻¹; +14,41 J K⁻¹',
        'Mengapa Δ*S* untuk pemanasan pada volume tetap memakai $C_V$, sedangkan pada tekanan tetap memakai $C_p$? ||| kalor reversibelnya masing-masing $C_V\\,dT$ dan $C_p\\,dT$',
        'Untuk gas ideal, mengapa suku volume dalam *dS* hanya bergantung pada *V*, tidak pada *T*? ||| $(\\partial p/\\partial T)_V = nR/V$ tidak memuat *T*'],
'6.2': ['Hitung Δ*S* untuk 1 mol N₂ yang dipanaskan dari 300 K ke 500 K pada tekanan tetap, dan untuk pemampatan isotermal 1 mol gas ideal dari 1 bar ke 10 bar. ||| +14,9 J K⁻¹; −19,1 J K⁻¹',
        'Hitung Δ*S* untuk 2,00 mol O₂ dari 25 °C dan 1,00 bar ke 100 °C dan 5,00 bar. ||| −13,7 J K⁻¹',
        'Mengapa entropi gas turun ketika dimampatkan pada suhu tetap? Jelaskan dari sudut molekul. ||| volume yang tersedia lebih kecil: lebih sedikit cara menempatkan molekul'],
'6.3': ['Hitung Δ$_\\text{mix}$*S* untuk 1 mol N₂ dan 1 mol O₂ pada suhu dan tekanan sama. ||| +11,5 J K⁻¹',
        'Hitung Δ$_\\text{mix}$*S* per mol udara (78% N₂, 21% O₂, 1% Ar). ||| 4,72 J K⁻¹ mol⁻¹',
        'Hitung Δ$_\\text{mix}$*S* untuk 2,00 mol He dan 3,00 mol Ar pada suhu dan tekanan sama. ||| +28,0 J K⁻¹',
        'Mengapa mencampur dua bagian gas yang **sama** tidak menaikkan entropi (paradoks Gibbs)? ||| molekul identik tidak dapat dibedakan; tidak ada susunan baru'],
'6.4': ['Hitung Δ$_\\text{vap}$*S* benzena (Δ$_\\text{vap}$*H* = 30,72 kJ mol⁻¹, $T_\\text{b}$ = 353,2 K). Apakah mengikuti aturan Trouton? ||| 87,0 J K⁻¹ mol⁻¹; ya',
        'Dengan aturan Trouton (85 J K⁻¹ mol⁻¹), perkirakan titik didih cairan dengan Δ$_\\text{vap}$*H* = 29,8 kJ mol⁻¹. ||| ≈ 351 K',
        'Etanol meleleh pada 159 K dengan Δ$_\\text{fus}$*H* = 4,93 kJ mol⁻¹. Hitung Δ$_\\text{fus}$*S*. ||| 31,0 J K⁻¹ mol⁻¹',
        'Dari Gambar 6.2, mengapa metana menyimpang ke bawah dari aturan Trouton? ||| titik didih sangat rendah: gasnya masih rapat, entropi gas kecil'],
'6.5': ['Hitung Δ*S* untuk memanaskan 1,00 mol air cair dari 0 °C ke 100 °C. ||| +23,5 J K⁻¹',
        'Hitung Δ*S* untuk mengubah 1,00 mol es −10 °C menjadi uap 110 °C ($C_p$: es 37,8; cair 75,3; uap 33,6 J K⁻¹ mol⁻¹). ||| +156,8 J K⁻¹',
        'Untuk aluminium, $C_{p,\\text{m}} = 20{,}67 + 0{,}012\\,38\\,T$ J K⁻¹ mol⁻¹. Hitung Δ*S* untuk memanaskan 1 mol dari 300 K ke 600 K. ||| +18,0 J K⁻¹',
        'Dari Gambar 6.3, mengapa lompatan entropi pada titik didih jauh lebih besar daripada pada titik leleh? ||| perbedaan keteraturan cair–gas jauh lebih besar daripada padat–cair'],
'6.6': ['Pada suhu sangat rendah $C_p \\approx aT^3$ (hukum Debye). Tunjukkan bahwa $S(T) = C_p(T)/3$, lalu hitung *S* pada 10 K bila $C_p$ = 0,50 J K⁻¹ mol⁻¹. ||| 0,17 J K⁻¹ mol⁻¹',
        'Mengapa hukum ketiga memungkinkan kita menulis entropi **mutlak**, padahal energi dalam dan entalpi hanya punya nilai relatif? ||| ada titik nol alami: kristal sempurna pada 0 K mempunyai *S* = 0',
        'Mengapa nol mutlak tidak dapat dicapai dalam jumlah langkah yang berhingga? ||| setiap langkah pendinginan menurunkan suhu makin sedikit ketika semua kurva *S*(*T*) menyatu di *S* = 0'],
'6.7': ['Hitung Δ$_\\text{r}$*S*° untuk 2H₂(g) + O₂(g) → 2H₂O(l) dan N₂ + 3H₂ → 2NH₃. ||| −326,7 J K⁻¹; −198,8 J K⁻¹',
        'Hitung Δ$_\\text{r}$*S*° untuk CaCO₃(s) → CaO(s) + CO₂(g) dan I₂(s) → I₂(g). ||| +160,6 J K⁻¹; +144,6 J K⁻¹',
        'Hitung Δ*S*° untuk C(grafit) → C(intan) dan jelaskan tandanya. ||| −3,36 J K⁻¹; intan lebih kaku',
        'Tanpa tabel, ramalkan tanda Δ*S*° untuk (a) 2SO₂ + O₂ → 2SO₃, (b) NH₄Cl(s) → NH₃(g) + HCl(g), (c) H₂(g) + Cl₂(g) → 2HCl(g). ||| (a) −; (b) +; (c) ≈ 0'],
'6.8': ['Untuk sintesis amonia pada 298 K (Δ*H*° = −92,22 kJ), hitung Δ*S* lingkungan dan Δ*S* total. ||| +309,3; +110,6 J K⁻¹',
        '@kalsinasi [P] Untuk CaCO₃ → CaO + CO₂ (Δ*H*° = +178,3 kJ), hitung Δ*S* total pada 298 K, lalu perkirakan suhu terendah tempat penguraian spontan pada 1 bar. ||| −437 J K⁻¹; ≈ 1110 K',
        'Hitung Δ*S* sistem, lingkungan, dan total untuk penguapan 1 mol air pada 25 °C dan 1 bar (Δ$_\\text{vap}$*H* = 44,01 kJ mol⁻¹). Mengapa air tetap menguap dari gelas di udara? ||| +118,9; −147,6; −28,7 J K⁻¹; tekanan parsial uap di udara jauh di bawah 1 bar'],
}
for k, b in S.items(): print(k, soal(N, k, b))
print(tanya(N, '6.3', ['Mengapa pencampuran gas ideal selalu spontan walaupun tidak ada kalor yang dilepas atau diserap?']))
print(tanya(N, '6.4', ['Apa yang dikatakan aturan Trouton tentang perubahan "banyaknya cara" ketika cairan menjadi gas, dan mengapa nilainya hampir sama untuk banyak cairan?']))
print(tanya(N, '6.6', ['Apa yang dimaksud kristal sempurna dalam hukum ketiga, dan mengapa kaca atau es biasa tidak memenuhinya?']))
print(tanya(N, '6.7', ['Mengapa reaksi yang menghasilkan lebih banyak mol gas hampir selalu mempunyai Δ$_\\text{r}$*S*° positif?']))
print(tanya(N, '6.8', ['Reaksi eksoterm menaikkan entropi lingkungan. Mengapa kenaikan itu lebih besar bila lingkungannya dingin?']))
print(bahas(N, r'''**Soal {{kalsinasi}}.** Dari Tabel 6.1, Δ$_\text{r}$*S*° = 39,75 + 213,74 − 92,9 = +160,6 J K⁻¹. Pada 298 K, lingkungan kehilangan kalor 178,3 kJ, sehingga
$$
\Delta S_\text{ling} = -\frac{\Delta H}{T} = -\frac{178\,300\ \text{J}}{298{,}15\ \text{K}} = -598\ \text{J K}^{-1}, \qquad \Delta S_\text{total} = 160{,}6 - 598 = -437\ \text{J K}^{-1} .
$$
Penguraian tidak spontan. Penguraian menjadi spontan bila $\Delta S_\text{total} = \Delta S - \Delta H/T > 0$, yaitu $T > \Delta H/\Delta S = 178\,300/160{,}6 = 1110$ K, dengan anggapan Δ*H* dan Δ*S* tidak bergantung suhu.

*Cara berpikir:* reaksi ini berebut antara dua kecenderungan. Entropi sistem naik karena satu mol gas terbentuk dari padatan, tetapi entropi lingkungan turun karena reaksi menyerap banyak kalor. Penurunan kedua mengecil sebanding 1/*T*, sedangkan kenaikan pertama hampir tetap, sehingga pada suhu cukup tinggi sistem menang. Itulah sebabnya tungku kapur dipanaskan sampai sekitar 900–1000 °C. Persaingan "Δ*H* lawan *T*Δ*S*" ini akan diringkas di Bab 7 menjadi satu besaran, energi Gibbs, dan suhu 1110 K adalah suhu tempat Δ*G*° = 0. Nilai sebenarnya (sekitar 1100 K) sangat dekat, karena Δ*H* dan Δ*S* reaksi ini hampir tidak berubah dengan suhu.'''))
