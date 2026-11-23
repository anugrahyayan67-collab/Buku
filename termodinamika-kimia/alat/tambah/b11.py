import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import soal, tanya, bahas
N = 11
S = {
'11.1': ['Berapa derajat kebebasan larutan NaCl jenuh yang setimbang dengan NaCl padat pada tekanan tetap? ||| *F*\' = 1 (hanya suhu)',
         'Mengapa jumlah komponen sistem CaCO₃(s) ⇌ CaO(s) + CO₂(g) adalah dua, bukan tiga? ||| ada satu reaksi yang mengaitkan ketiga zat: *C* = 3 − 1',
         'Mengapa dalam diagram dua komponen pada tekanan tetap kita memakai $F\' = C - P + 1$? ||| satu derajat kebebasan sudah dipakai untuk menetapkan tekanan'],
'11.2': ['Campuran benzena–toluena ($x_\\text{benzena}$ = 0,50) pada 25 °C. Hitung tekanan gelembung, dan tekanan embun untuk uap dengan $y_\\text{benzena}$ = 0,50. ||| 8,25 kPa; 5,84 kPa',
         'Pada suatu tekanan, campuran dengan $x_\\text{A}$ total 0,40 terpisah menjadi cair ($x_\\text{A}$ = 0,25) dan uap ($y_\\text{A}$ = 0,60). Berapa fraksi mol bahan yang menjadi uap? ||| 0,43',
         'Mengapa garis gelembung pada diagram *p*–*x* untuk larutan ideal berupa garis lurus, sedangkan garis embunnya melengkung? ||| $p = x_\\text{A}p_\\text{A}^* + x_\\text{B}p_\\text{B}^*$ linear dalam *x*; terhadap *y* tidak linear'],
'11.3': ['Mengapa kolom distilasi yang lebih tinggi memberi pemisahan lebih baik? ||| lebih banyak pelat teoretis: lebih banyak tahap penguapan–pengembunan',
         'Pada diagram *T*–*x*, mengapa daerah dua fasa disebut "lensa"? ||| dibatasi garis gelembung (bawah) dan garis embun (atas) yang bertemu di kedua titik didih murni'],
'11.4': ['Mengapa etanol 95,6% tidak dapat dimurnikan lebih lanjut dengan distilasi biasa? ||| membentuk azeotrop titik didih minimum dengan air',
         'Azeotrop titik didih maksimum terbentuk dari campuran dengan penyimpangan negatif. Jelaskan mengapa. ||| tarikan A–B lebih kuat; tekanan uap campuran minimum, titik didih maksimum',
         'Sebutkan dua cara memecah azeotrop etanol–air dalam industri. ||| distilasi azeotropik dengan pelarut ketiga (sikloheksana), saringan molekul, atau distilasi beda tekanan'],
'11.5': ['Dalam model larutan reguler, hitung suhu kritis kelarutan atas untuk *w* = 4,0 kJ mol⁻¹. ||| 241 K',
         'Bromobenzena (*M* = 157) didistilasi uap pada 1 atm; pada suhu didih campuran, tekanan uap air 94,3 kPa dan bromobenzena 7,0 kPa. Berapa gram bromobenzena per gram air di distilat? ||| 0,65 g',
         'Mengapa distilasi uap memungkinkan zat bertitik didih tinggi didistilasi di bawah 100 °C? ||| kedua cairan tak bercampur menyumbang tekanan uap penuh masing-masing; jumlahnya mencapai 1 atm di bawah 100 °C'],
'11.6': ['Hitung kelarutan ideal naftalena ($T_\\text{f}$ = 353,4 K, Δ$_\\text{fus}$*H* = 19,0 kJ mol⁻¹) dan bifenil (342,4 K, 18,6 kJ mol⁻¹) pada 25 °C. ||| $x$ = 0,30; 0,38',
         'Mengapa kurva pendinginan campuran non-eutektik mempunyai patahan sebelum bagian datar? ||| satu komponen mulai membeku: laju pendinginan berkurang karena kalor peleburan dilepas',
         'Mengapa garam ditaburkan di jalan bersalju tidak berguna bila suhu di bawah −21 °C? ||| di bawah suhu eutektik air–NaCl tidak ada cairan yang dapat terbentuk'],
'11.7': ['Pada diagram segitiga, di mana letak campuran berkomposisi 20% A, 30% B, 50% C? ||| titik yang berjarak 0,2 dari sisi BC, 0,3 dari sisi AC, 0,5 dari sisi AB',
         'Mengapa campuran dua titik pada diagram segitiga selalu terletak pada garis lurus yang menghubungkan keduanya? ||| keseimbangan massa: aturan tuas dalam dua dimensi'],
'11.8': ['Zat dengan *K* = 4,0 (organik/air) diekstraksi dari 100 mL air. Bandingkan sekali dengan 100 mL pelarut dan tiga kali dengan 33,3 mL. ||| tersisa 20% lawan 7,9%',
         'Mengapa ekstraksi berkali-kali dengan volume kecil lebih efektif daripada sekali dengan volume besar? ||| setiap tahap mengambil fraksi yang sama dari sisa; perkalian fraksi menurun cepat'],
'11.9': ['Dengan model ideal Contoh 11.18, hitung komposisi cairan dan padatan Cu–Ni yang setimbang pada 1600 K. ||| cair $x_\\text{Ni}$ = 0,61; padat 0,68',
         'Mengapa padatan yang membeku dari lelehan Cu–Ni selalu lebih kaya nikel daripada cairannya? ||| nikel bertitik leleh lebih tinggi: μ nikel padat relatif lebih rendah',
         'Apa perbedaan peleburan kongruen dan tak kongruen? Berikan satu contoh masing-masing. ||| kongruen: cairan berkomposisi sama (Mg₂Si); tak kongruen: terurai menjadi padatan lain + cairan (Na₂SO₄·10H₂O)',
         'Kotoran fosfor dalam silikon mempunyai *k* = 0,35. Setelah satu lintasan zona, berapa kadar relatifnya pada *x* = 0 dan *x* = 2*L*? ||| 0,35; 0,68',
         '@zona [P] Turunkan persamaan pemurnian zona satu lintasan (11.12) dengan menulis neraca kotoran untuk zona leleh yang bergerak sejauh *dx*. ||| $L\\,dC_\\text{l} = (C_0 - kC_\\text{l})\\,dx$; integrasi dengan $C_\\text{l}(0) = C_0$',
         'Mengapa pemurnian zona tidak efektif untuk kotoran dengan *k* ≈ 1? ||| padatan mengambil kotoran sebanyak kadarnya di cairan; tidak ada pemisahan'],
}
for k, b in S.items(): print(k, soal(N, k, b))
print(tanya(N, '11.9', ['Apa syarat struktur agar dua logam membentuk larutan padat dalam segala perbandingan?','Mengapa diagram lensa padat–cair mirip dengan diagram suhu–komposisi untuk distilasi campuran ideal?','Mengapa paduan cor perlu dianil supaya komposisinya merata?']))
print(tanya(N, '11.4', ['Mengapa titik azeotrop tidak dapat dilewati dengan distilasi bertingkat, berapa pun tinggi kolomnya?']))
print(bahas(N, r'''**Soal {{zona}}.** Misalkan zona leleh sepanjang *L* berada antara *x* dan *x* + *L*, dengan kadar kotoran $C_\text{l}$ yang merata (cairan teraduk). Ketika zona maju sejauh *dx*, di depannya meleleh padatan baru yang membawa kotoran $C_0\,dx$ (per satuan luas penampang), dan di belakangnya membeku padatan yang mengambil $kC_\text{l}\,dx$. Perubahan jumlah kotoran di zona adalah
$$
L\,dC_\text{l} = (C_0 - kC_\text{l})\,dx .
$$
Pada awal lintasan, zona dibentuk dari batang berkadar $C_0$, sehingga $C_\text{l}(0) = C_0$. Memisahkan variabel dan mengintegrasikan,
$$
\int_{C_0}^{C_\text{l}}\frac{dC_\text{l}}{C_0 - kC_\text{l}} = \frac{x}{L} \quad\Rightarrow\quad C_\text{l} = \frac{C_0}{k}\left[1 - (1 - k)e^{-kx/L}\right] .
$$
Padatan yang membeku di titik *x* berkadar $C = kC_\text{l}$, sehingga $C/C_0 = 1 - (1 - k)e^{-kx/L}$, yaitu (11.12).

*Cara berpikir:* banyak hasil kimia teknik diturunkan dengan pola yang sama: pilih "wadah" yang bergerak atau tetap (di sini zona leleh), tulis neraca masuk–keluar untuk langkah kecil, lalu integrasikan dengan syarat awal. Pola itu sama dengan penurunan ekstraksi berulang (subbab 11.8) dan distilasi Rayleigh. Koefisien distribusi *k* di dalamnya adalah hasil termodinamika murni, karena berasal dari kesamaan potensial kimia kotoran di padatan dan cairan, persis seperti diagram lensa.'''))
