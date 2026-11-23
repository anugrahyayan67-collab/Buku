import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import soal, tanya, bahas
N = 9
S = {
'9.1': ['Sebutkan tiga besaran molar parsial selain volume, dan tuliskan definisinya sebagai turunan parsial. ||| $H_\\text{A} = (\\partial H/\\partial n_\\text{A})_{T,p,n_\\text{B}}$, demikian pula *S* dan *G* (= μ)',
        'Mengapa besaran molar parsial adalah besaran intensif? ||| perbandingan dua besaran ekstensif; tidak bergantung ukuran sampel, hanya komposisi',
        'Volume total campuran adalah $V = n_\\text{A}V_\\text{A} + n_\\text{B}V_\\text{B}$. Mengapa rumus ini benar walaupun $V_\\text{A}$ dan $V_\\text{B}$ berubah dengan komposisi? ||| teorema Euler: *V* fungsi homogen derajat satu dalam jumlah mol',
        'Mengapa volume molar parsial dapat bernilai negatif, sedangkan volume molar zat murni tidak pernah? ||| menyatakan perubahan volume larutan, bukan ruang yang ditempati molekul; ion kecil bermuatan besar memampatkan air di sekitarnya'],
'9.2': ['Dalam campuran etanol–air pada suatu komposisi, $V_\\text{etanol}$ = 56,0 dan $V_\\text{air}$ = 17,0 cm³ mol⁻¹. Hitung volume campuran 1,00 mol etanol dan 1,00 mol air, dan bandingkan dengan jumlah volume murninya. ||| 73,0 cm³ lawan 76,8 cm³',
        'Volume molar parsial NaCl dalam larutan encer sekitar 16,6 cm³ mol⁻¹. Berapa pertambahan volume bila 0,500 mol NaCl dilarutkan dalam 1 kg air? ||| ≈ 8,3 cm³',
        'Volume molar parsial MgSO₄ dalam larutan sangat encer sekitar −1,4 cm³ mol⁻¹. Apa yang terjadi pada volume larutan bila 0,10 mol garam ditambahkan, dan mengapa? ||| berkurang 0,14 cm³; ion menarik dan memampatkan molekul air (elektrostriksi)',
        'Jelaskan cara membaca volume molar parsial kedua komponen dari satu garis singgung pada kurva $V_\\text{m}$ terhadap *x* (Gambar 9.1). ||| perpotongan garis singgung dengan sumbu $x$ = 0 dan $x$ = 1'],
'9.3': ['Hitung $\\mu_\\text{A} - \\mu_\\text{A}^*$ pada 25 °C untuk $x_\\text{A}$ = 0,50 dan 0,90 dalam campuran ideal. ||| −1,72 dan −0,26 kJ mol⁻¹',
        'Hitung tekanan osmotik larutan sukrosa 0,10 mol L⁻¹ pada 25 °C. ||| 248 kPa',
        'Iodin terbagi antara CCl₄ dan air dengan *K* = 85. Berapa fraksi iodin yang tertinggal dalam 50 mL air setelah diekstraksi sekali dengan 10 mL CCl₄, dan setelah dua kali dengan 5 mL? ||| 5,6%; 1,1%',
        'Dari Gambar 9.3, mengapa membuang sisa kotoran yang tinggal sedikit memerlukan usaha paling besar? ||| μ kotoran sangat rendah pada $x$ kecil; diperlukan kerja besar untuk mengeluarkannya',
        'Mengapa potensial kimia menentukan arah perpindahan zat antarfasa, padahal konsentrasi tidak selalu? ||| zat berpindah ke μ lebih rendah; μ juga memuat interaksi dan keadaan standar setiap fasa'],
'9.4': ['Dalam campuran biner pada $x_\\text{B}$ = 0,30, $V_\\text{B}$ naik 0,80 cm³ mol⁻¹ untuk suatu perubahan kecil komposisi. Berapa perubahan $V_\\text{A}$? ||| −0,34 cm³ mol⁻¹',
        'Tunjukkan dari persamaan Gibbs–Duhem bahwa bila $\\mu_\\text{B}$ naik, $\\mu_\\text{A}$ harus turun. ||| $x_\\text{A}d\\mu_\\text{A} = -x_\\text{B}d\\mu_\\text{B}$',
        'Mengapa persamaan Gibbs–Duhem dapat dipakai untuk memeriksa konsistensi data tekanan uap campuran? ||| kedua koefisien aktivitas tidak bebas; data yang melanggar hubungan itu pasti salah ukur',
        'Pada Gambar 9.2, mengapa ketika $V_\\text{etanol}$ mencapai minimum, $V_\\text{air}$ mencapai maksimum pada komposisi yang sama? ||| Gibbs–Duhem: kemiringan keduanya berlawanan tanda dan nol bersamaan'],
'9.5': ['Hitung kenaikan potensial kimia O₂ bila tekanan parsialnya naik dari 0,21 bar ke 1,00 bar pada 25 °C. ||| +3,87 kJ mol⁻¹',
        'Hitung kenaikan potensial kimia 1 mol gas ideal yang dimampatkan dari 1 bar ke 100 bar pada 25 °C. ||| +11,4 kJ mol⁻¹',
        'Dengan $\\ln\\varphi \\approx Bp/RT$, hitung φ N₂ pada 25 °C dan 50 bar ($B$ = −5,2 cm³ mol⁻¹) dan CO₂ pada 10 bar ($B$ = −125 cm³ mol⁻¹). ||| 0,990; 0,951',
        'Koefisien fugasitas H₂ pada 300 bar dan 25 °C sekitar 1,20. Berapa fugasitasnya, dan mengapa φ > 1? ||| 360 bar; tolakan (volume molekul) lebih penting daripada tarikan yang sangat lemah',
        'Dari Gambar 9.5, berapa tekanan efektif CO₂ pada 45 bar dan 300 K? ||| ≈ 37 bar (φ ≈ 0,81)',
        '@fug [P] Turunkan $\\ln\\varphi = \\int_0^p (Z - 1)\\,dp/p$ dari $d\\mu = V_\\text{m}\\,dp$, lalu pakai untuk gas yang mengikuti $Z = 1 + Bp/RT$. ||| $\\ln\\varphi = Bp/RT$'],
}
for k, b in S.items(): print(k, soal(N, k, b))
print(tanya(N, '9.1', ['Mengapa 50 mL etanol dan 50 mL air tidak menghasilkan 100 mL campuran? Jelaskan dari sudut molekul.']))
print(tanya(N, '9.2', ['Apa arti fisis volume molar parsial yang negatif?']))
print(tanya(N, '9.3', ['Mengapa potensial kimia disebut "tekanan untuk keluar" suatu zat dari fasanya?', 'Mengapa ln *x* dalam rumus potensial kimia campuran ideal berasal dari entropi, bukan dari energi interaksi?']))
print(tanya(N, '9.5', ['Fugasitas sering disebut "tekanan yang dikoreksi". Koreksi apa yang dimaksud, dan mengapa koreksinya dapat membuat *f* lebih besar atau lebih kecil dari *p*?']))
print(bahas(N, r'''**Soal {{fug}}.** Pada suhu tetap, $d\mu = V_\text{m}\,dp$ untuk gas apa pun. Untuk gas ideal, $V_\text{m} = RT/p$, sehingga $d\mu^\text{id} = RT\,dp/p$. Untuk gas nyata kita **mendefinisikan** fugasitas supaya bentuknya sama: $d\mu = RT\,d\ln f$. Mengurangkan kedua persamaan,
$$
RT\,d\ln\frac{f}{p} = \left(V_\text{m} - \frac{RT}{p}\right)dp = \frac{RT}{p}(Z - 1)\,dp ,
$$
karena $V_\text{m} = ZRT/p$. Pada $p \to 0$ semua gas ideal, sehingga $f/p \to 1$ dan $\ln(f/p) \to 0$. Mengintegrasikan dari 0 sampai *p* memberi $\ln\varphi = \int_0^p (Z - 1)\,dp/p$. Bila $Z - 1 = Bp/RT$, integrannya $B/RT$ yang tetap, sehingga $\ln\varphi = Bp/RT$.

*Cara berpikir:* fugasitas tidak memerlukan teori baru; ia hanya menghimpun seluruh ketakidealan ke dalam satu besaran, sehingga semua rumus potensial kimia gas ideal tetap dapat dipakai. Yang diperlukan untuk menghitungnya hanyalah *Z* sebagai fungsi tekanan, dari persamaan keadaan mana pun di Bab 2. Tanda *B* langsung memberi tanda ln φ: tarikan (*B* < 0) membuat φ < 1, tolakan (*B* > 0) membuat φ > 1. Gagasan yang sama dipakai di Bab 10 untuk larutan nyata: aktivitas berperan seperti fugasitas, dan koefisien aktivitas seperti φ.'''))
