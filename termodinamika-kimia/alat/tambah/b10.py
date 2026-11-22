import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import soal, tanya, bahas
N = 10
S = {
'10.1': ['Hitung Δ$_\\text{mix}$*G* dan Δ$_\\text{mix}$*S* untuk 1 mol benzena dan 1 mol toluena pada 25 °C (anggap ideal). ||| −3,44 kJ; +11,5 J K⁻¹',
         'Mengapa Δ$_\\text{mix}$*H* = 0 dan Δ$_\\text{mix}$*V* = 0 untuk larutan ideal? ||| interaksi A–B sama dengan rata-rata A–A dan B–B; ukuran molekul serupa'],
'10.2': ['Campuran benzena–toluena dengan $x_\\text{benzena}$ = 0,30 pada 25 °C. Hitung tekanan uap total dan fraksi mol benzena dalam uap. ||| 6,46 kPa; 0,59',
         'Mengapa uap di atas campuran ideal selalu lebih kaya akan komponen yang lebih mudah menguap? ||| tekanan parsialnya lebih besar per fraksi mol cairan',
         'Pasangan mana yang paling mendekati larutan ideal: (a) benzena–toluena, (b) air–etanol, (c) heksana–air? ||| (a)'],
'10.3': ['Tetapan Henry O₂ dalam air pada 25 °C 769 L atm mol⁻¹. Hitung kelarutan O₂ dari udara (0,21 atm) dalam mol L⁻¹ dan mg L⁻¹. ||| $2{,}7 \\times 10^{-4}$ mol L⁻¹; 8,7 mg L⁻¹',
         'Minuman bersoda dikemas dengan CO₂ 4,0 atm ($K_\\text{H}$ = 29,4 L atm mol⁻¹). Berapa gram CO₂ larut per liter? ||| 6,0 g L⁻¹',
         'Mengapa penyelam yang naik terlalu cepat dapat mengalami penyakit dekompresi? ||| N₂ yang larut di darah pada tekanan tinggi keluar sebagai gelembung ketika tekanan turun cepat'],
'10.4': ['Larutan dengan fraksi mol zat terlarut 0,050 dalam air pada 25 °C. Berapa penurunan tekanan uapnya? ||| 0,158 kPa (menjadi 3,01 kPa)',
         'Mengapa penurunan tekanan uap tidak bergantung pada jenis zat terlarut yang tidak mudah menguap? ||| hanya mengencerkan pelarut: $\\mu_\\text{A}$ turun sebesar *RT* ln $x_\\text{A}$'],
'10.5': ['Hitung tetapan krioskopik benzena dari $T_\\text{f}$ = 278,65 K dan Δ$_\\text{fus}$*H* = 10,59 kJ mol⁻¹. ||| 4,76 K kg mol⁻¹ (terukur 5,12)',
         'Sebanyak 2,00 kg etilena glikol dicampur dengan 5,00 kg air. Perkirakan titik bekunya dengan rumus larutan encer. ||| ≈ −12 °C',
         'Mengapa garam lebih efektif daripada gula untuk mencairkan es di jalan, per mol yang ditambahkan? ||| garam terurai menjadi dua ion atau lebih; sifat koligatif menghitung jumlah partikel'],
'10.6': ['Hitung tekanan osmotik darah (≈ 0,30 osmol L⁻¹) pada 37 °C. ||| 774 kPa (7,6 atm)',
         'Larutan polimer 5,0 g L⁻¹ mempunyai tekanan osmotik 0,80 kPa pada 25 °C. Hitung massa molarnya. ||| $1{,}5 \\times 10^4$ g mol⁻¹',
         'Mengapa osmometri lebih cocok daripada penurunan titik beku untuk menentukan massa molar protein? ||| efeknya jauh lebih besar dan mudah diukur pada konsentrasi kecil'],
'10.7': ['Tekanan uap air di atas suatu larutan garam 2,90 kPa pada 25 °C ($p^*$ = 3,169 kPa). Hitung aktivitas air. ||| 0,915',
         'Dalam model larutan reguler dengan $W/RT$ = 1, hitung γ$_\\text{A}$ pada $x_\\text{A}$ = 0,50. ||| 1,28',
         'Hitung γ$_\\pm$ MgSO₄ 0,0010 mol kg⁻¹ dengan hukum pembatas. ||| 0,74'],
'10.8': ['Hitung kekuatan ion larutan MgSO₄ 0,10 mol kg⁻¹, Na₂SO₄ 0,050 mol kg⁻¹, dan LaCl₃ 0,010 mol kg⁻¹. ||| 0,40; 0,15; 0,060',
         'Hitung γ$_\\pm$ Na₂SO₄ 0,050 mol kg⁻¹ dengan hukum Debye–Hückel yang diperluas. ||| 0,52',
         'Hitung γ$_\\pm$ MgSO₄ 0,010 mol kg⁻¹ dengan bentuk diperluas. ||| 0,46',
         'Hitung γ$_\\pm$ NaCl 0,10 mol kg⁻¹ dengan persamaan Davies dan bandingkan dengan nilai terukur 0,778. ||| 0,782',
         'Hitung panjang Debye air laut (*I* ≈ 0,7 mol L⁻¹) pada 25 °C. ||| 0,36 nm',
         '@baso4 [P] $K_\\text{sp}$ BaSO₄ = $1{,}08 \\times 10^{-10}$ pada 25 °C. Hitung kelarutannya dalam air murni dan dalam KNO₃ 0,10 mol kg⁻¹ (persamaan Davies). Mengapa efeknya jauh lebih besar daripada untuk AgCl? ||| $1{,}04 \\times 10^{-5}$ dan $2{,}8 \\times 10^{-5}$ mol kg⁻¹; log γ$_\\pm$ sebanding |*z*$_+$*z*$_-$| = 4',
         'Mengapa garam asing menaikkan kelarutan garam sukar larut, sedangkan garam dengan ion senama menurunkannya? ||| garam asing hanya menurunkan γ (atmosfer ion); ion senama menaikkan hasil kali konsentrasi secara langsung',
         'Mengapa koefisien aktivitas satu jenis ion saja tidak dapat diukur? ||| larutan harus netral; ion tidak dapat ditambahkan tanpa ion lawan'],
}
for k, b in S.items(): print(k, soal(N, k, b))
print(tanya(N, '10.8', ['Mengapa larutan NaCl 0,01 mol kg⁻¹ sudah menyimpang 10% dari perilaku ideal, sedangkan larutan sukrosa pada konsentrasi yang sama hampir tidak?','Apa yang dimaksud atmosfer ion, dan mengapa keberadaannya menurunkan potensial kimia ion?','Mengapa panjang Debye yang pendek di dalam sel penting bagi interaksi antarprotein?']))
print(tanya(N, '10.3', ['Apa beda keadaan acuan hukum Raoult dan hukum Henry, dan mengapa zat terlarut encer memerlukan acuan Henry?']))
print(tanya(N, '10.6', ['Mengapa tekanan osmotik larutan encer mirip dengan tekanan gas ideal, $\\Pi = cRT$, padahal pelarutnya cair?']))
print(bahas(N, r'''**Soal {{baso4}}.** Dalam air murni, $s_0 = \sqrt{K_\text{sp}} = \sqrt{1{,}08 \times 10^{-10}} = 1{,}04 \times 10^{-5}$ mol kg⁻¹. Dalam KNO₃ 0,10 mol kg⁻¹, kekuatan ion ditentukan oleh KNO₃, *I* = 0,10, dan untuk BaSO₄ $|z_+z_-| = 4$. Persamaan Davies memberi
$$
\log\gamma_\pm = -(0{,}509)(4)\left(\frac{0{,}316}{1{,}316} - 0{,}030\right) = -0{,}428 , \qquad \gamma_\pm = 0{,}373 ,
$$
sehingga $s = s_0/\gamma_\pm = 2{,}8 \times 10^{-5}$ mol kg⁻¹, hampir tiga kali kelarutan dalam air murni. Untuk AgCl pada kekuatan ion yang sama, γ$_\pm$ ≈ 0,78 dan kenaikannya hanya sekitar 28%.

*Cara berpikir:* efek garam bekerja melalui γ, dan log γ sebanding dengan perkalian muatan ion. Ion bermuatan dua mempunyai atmosfer yang empat kali "lebih kuat", sehingga stabilisasinya oleh garam asing jauh lebih besar. Dalam praktik analisis, pencucian endapan BaSO₄ dengan larutan garam pekat dapat melarutkan endapan secara berarti; karena itu endapan dicuci dengan air atau larutan yang mengandung ion senama. Untuk kekuatan ion 0,1, hasil Davies sudah merupakan taksiran, sehingga angka ini sebaiknya dibaca "sekitar dua sampai tiga kali".'''))
