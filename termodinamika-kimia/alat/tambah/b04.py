import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import soal, tanya, bahas
N = 4
S = {
'4.1': ['Untuk pembakaran propana $\\text{C}_3\\text{H}_8(g) + 5\\text{O}_2(g) \\to 3\\text{CO}_2(g) + 4\\text{H}_2\\text{O}(l)$ pada 25 °C, hitung $\\Delta H - \\Delta U$. ||| −7,44 kJ mol⁻¹ (Δ*n*$_\\text{gas}$ = −3)',
        'Δ*H*° sintesis amonia $\\text{N}_2 + 3\\text{H}_2 \\to 2\\text{NH}_3$ adalah −92,22 kJ mol⁻¹ pada 25 °C. Hitung Δ*U*°. ||| −87,26 kJ mol⁻¹',
        'Untuk reaksi apa Δ*H* dan Δ*U* praktis sama? Berikan dua contoh. ||| reaksi tanpa perubahan mol gas, misalnya H₂ + Cl₂ → 2HCl atau reaksi dalam larutan'],
'4.2': ['Hitung kalor untuk memanaskan 2,00 mol argon dari 300 K ke 400 K pada tekanan tetap dan pada volume tetap. ||| 4,16 kJ; 2,49 kJ',
        '$C_{p,\\text{m}}$ CO₂ pada 25 °C adalah 37,1 J K⁻¹ mol⁻¹. Perkirakan $C_{V,\\text{m}}$-nya. ||| 28,8 J K⁻¹ mol⁻¹',
        'Mengapa untuk cairan dan padatan $C_p \\approx C_V$, sedangkan untuk gas selisihnya *R* per mol? ||| cairan dan padatan hampir tidak memuai saat dipanaskan, sehingga kerja pemuaian sangat kecil'],
'4.3': ['Sebanyak 0,640 g naftalena (C₁₀H₈) dibakar dalam bom kalorimeter (*C* = 10,2 kJ K⁻¹); suhu naik 2,513 K. Hitung Δ$_\\text{c}$*U* dan Δ$_\\text{c}$*H* per mol. ||| −5133 kJ mol⁻¹; −5138 kJ mol⁻¹',
        'Sebanyak 50,0 mL HCl 1,00 M dicampur dengan 50,0 mL NaOH 1,00 M dalam kalorimeter gelas gabus; suhu naik 6,7 K. Anggap larutan seperti air. Hitung entalpi penetralan per mol air. ||| −56 kJ mol⁻¹',
        'Mengapa bom kalorimeter mengukur Δ*U*, sedangkan kalorimeter gelas gabus mengukur Δ*H*? ||| bom bervolume tetap (*q*$_V$ = Δ*U*); gelas gabus terbuka pada tekanan tetap (*q*$_p$ = Δ*H*)',
        'Mengapa kapasitas kalor bom kalorimeter harus dikalibrasi dulu, misalnya dengan asam benzoat? ||| kalor diserap seluruh peralatan (bom, air, pengaduk), yang kapasitas kalornya tidak dapat dihitung tepat'],
'4.4': ['Berapa kalor untuk melelehkan 100 g es pada 0 °C, dan untuk menguapkan 1,00 L air pada 100 °C? ||| 33,4 kJ; 2,26 MJ',
        'Hitung kalor untuk mengubah 50,0 g es pada −10 °C menjadi uap pada 100 °C ($c_\\text{es}$ = 2,09 J g⁻¹ K⁻¹). ||| 151 kJ',
        'Seorang pelari menguapkan 500 g keringat pada 37 °C (Δ$_\\text{vap}$*H* = 43,4 kJ mol⁻¹). Berapa kalor yang dibuang tubuhnya? ||| 1,20 MJ',
        'Mengapa luka bakar karena uap air 100 °C lebih parah daripada karena air mendidih 100 °C? ||| uap melepas entalpi penguapan yang besar saat mengembun di kulit'],
'4.5': ['Satu tabung elpiji berisi 3,00 kg propana. Berapa kalor yang dilepas bila semuanya dibakar (Δ$_\\text{c}$*H*° = −2220 kJ mol⁻¹)? ||| 151 MJ',
        'Δ$_\\text{f}$*H*°(H₂O, l) = −285,83 kJ mol⁻¹. Tuliskan persamaan termokimia untuk elektrolisis 2 mol air cair beserta Δ*H*°-nya. ||| 2H₂O(l) → 2H₂(g) + O₂(g); +571,66 kJ',
        'Mengapa persamaan termokimia harus menyebut wujud setiap zat? Berikan contoh dengan air. ||| entalpi bergantung wujud; H₂O(l) dan H₂O(g) berbeda 44 kJ mol⁻¹'],
'4.6': ['Entalpi pembakaran grafit −393,51 dan intan −395,41 kJ mol⁻¹. Hitung Δ*H*° untuk C(grafit) → C(intan). ||| +1,90 kJ mol⁻¹',
        'Dari S(s) + O₂ → SO₂, Δ*H*° = −296,83 kJ mol⁻¹, dan SO₂ + ½O₂ → SO₃, Δ*H*° = −98,9 kJ mol⁻¹, hitung Δ$_\\text{f}$*H*°(SO₃, g). ||| −395,7 kJ mol⁻¹',
        'Pada Gambar 4.2, mengapa panjang panah langsung C → CO₂ harus sama dengan jumlah kedua panah lewat CO? ||| entalpi fungsi keadaan; awal dan akhir sama'],
'4.7': ['Hitung Δ$_\\text{c}$*H*° metana dari Tabel 4.1. ||| −890,4 kJ mol⁻¹',
        'Hitung Δ$_\\text{c}$*H*° glukosa dari Tabel 4.1, lalu nyatakan per gram. ||| −2802,7 kJ mol⁻¹; −15,6 kJ g⁻¹',
        'Hitung Δ$_\\text{r}$*H*° untuk reduksi bijih besi $\\text{Fe}_2\\text{O}_3 + 3\\text{CO} \\to 2\\text{Fe} + 3\\text{CO}_2$. ||| −24,7 kJ mol⁻¹',
        'Hitung Δ$_\\text{r}$*H*° kalsinasi batu kapur CaCO₃ → CaO + CO₂ (Δ$_\\text{f}$*H*°(CaO) = −635,09 kJ mol⁻¹). ||| +178,3 kJ mol⁻¹',
        'Hitung Δ$_\\text{c}$*H*° asetilena (hasil H₂O cair) dan jelaskan mengapa nyala oksiasetilena sangat panas. ||| −1299,6 kJ mol⁻¹; Δ$_\\text{f}$*H*° asetilena positif menambah kalor yang dilepas',
        'Hitung Δ$_\\text{r}$*H*° oksidasi amonia pada proses Ostwald $4\\text{NH}_3 + 5\\text{O}_2 \\to 4\\text{NO} + 6\\text{H}_2\\text{O}(g)$. ||| −905,5 kJ'],
'4.8': ['Taksir Δ*H* untuk H₂ + Cl₂ → 2HCl dari entalpi ikatan. ||| −184 kJ',
        'Taksir Δ*H* sintesis amonia dari entalpi ikatan dan bandingkan dengan −92,2 kJ dari tabel. ||| −75 kJ',
        'Taksir Δ*H* hidrogenasi etena dan klorinasi metana (CH₄ + Cl₂ → CH₃Cl + HCl) dari entalpi ikatan. ||| −124 kJ; −115 kJ',
        'Dari Gambar 4.5, langkah mana dalam siklus Born–Haber NaCl yang melepas energi, dan mengapa NaCl tetap terbentuk walaupun ionisasi Na sangat endoterm? ||| afinitas elektron dan pembentukan kisi; energi kisi yang besar menebus ionisasi'],
'4.9': ['Hitung Δ$_\\text{f}$*H*° H₂O(g) pada 100 °C dari nilainya pada 25 °C ($C_{p,\\text{m}}$: H₂O(g) 33,58; H₂ 28,82; O₂ 29,36 J K⁻¹ mol⁻¹). ||| −242,6 kJ mol⁻¹',
        'Dari Gambar 4.6, perkirakan Δ$_\\text{vap}$*H* air pada 60 °C. ||| ≈ 42,3 kJ mol⁻¹',
        'Kapan hukum Kirchhoff dengan Δ$C_p$ tetap mulai tidak memadai? ||| rentang suhu lebar, atau ada perubahan fasa di antaranya'],
'4.10': ['Hitung kalor pembakaran per kilogram untuk H₂ (−285,8), CH₄ (−890,3), dan oktana (−5470 kJ mol⁻¹). ||| 142; 55,5; 47,9 MJ kg⁻¹',
         '@co2 [P] Berapa gram CO₂ dilepas per megajoule kalor dari metana dan dari oktana? Apa artinya bagi peralihan bahan bakar? ||| 49 g MJ⁻¹ dan 64 g MJ⁻¹; gas alam melepas sekitar 23% lebih sedikit CO₂ per energi',
         'Mengapa kalor pembakaran bahan bakar biasanya dinyatakan dengan air **cair** sebagai hasil (nilai kalor atas), dan kapan nilai kalor bawah lebih tepat? ||| standar kalorimetri; mesin dan tungku membuang air sebagai uap'],
}
for k, b in S.items(): print(k, soal(N, k, b))
print(tanya(N, '4.1', ['Entalpi didefinisikan sebagai *H* = *U* + *pV*. Mengapa besaran buatan ini lebih berguna daripada *U* untuk reaksi di labu terbuka?']))
print(tanya(N, '4.6', ['Mengapa hukum Hess bukan hukum baru, melainkan akibat langsung dari sifat entalpi sebagai fungsi keadaan?']))
print(tanya(N, '4.7', ['Mengapa entalpi pembentukan unsur dalam keadaan acuannya ditetapkan nol, dan mengapa pilihan itu tidak memengaruhi entalpi reaksi?']))
print(tanya(N, '4.8', ['Mengapa entalpi reaksi yang ditaksir dari entalpi ikatan rata-rata hanya cocok untuk reaksi fase gas?']))
print(tanya(N, '4.10', ['Hidrogen melepas kalor paling banyak per kilogram, tetapi sedikit per liter. Mengapa kedua ukuran itu sama penting untuk bahan bakar kendaraan?']))
print(bahas(N, r'''**Soal {{co2}}.** Pembakaran satu mol metana menghasilkan satu mol CO₂ (44,01 g) dan melepas 890,3 kJ, sehingga
$$
\frac{44{,}01\ \text{g}}{0{,}8903\ \text{MJ}} = 49{,}4\ \text{g MJ}^{-1} .
$$
Satu mol oktana menghasilkan 8 mol CO₂ (352,1 g) dan melepas 5470 kJ: $352{,}1/5{,}470 = 64{,}4$ g MJ⁻¹. Untuk energi yang sama, metana melepas $1 - 49{,}4/64{,}4 = 23\%$ lebih sedikit CO₂.

*Cara berpikir:* untuk membandingkan bahan bakar secara adil, bagilah dengan besaran yang benar-benar diinginkan, yaitu energi, bukan massa atau mol. Metana unggul karena sebagian besar energinya berasal dari pembentukan air (empat ikatan O–H per karbon), bukan dari pembentukan CO₂. Makin besar perbandingan H/C, makin sedikit CO₂ per energi; hidrogen murni adalah batasnya, dengan nol CO₂. Perhitungan ini belum memasukkan kebocoran metana, gas rumah kaca yang jauh lebih kuat daripada CO₂.'''))
