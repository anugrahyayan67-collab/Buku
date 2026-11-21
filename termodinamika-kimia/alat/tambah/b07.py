import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import soal, tanya, bahas
N = 7
S = {
'7.1': ['Hitung Δ$_\\text{r}$*G*° sintesis amonia pada 298 K dari Δ*H*° = −92,22 kJ dan Δ*S*° = −198,75 J K⁻¹. ||| −32,96 kJ',
        'Mengapa kriteria Δ*G* < 0 lebih praktis daripada Δ*S*$_\\text{total}$ > 0, padahal keduanya setara? ||| hanya memakai besaran sistem; lingkungan tercakup lewat −Δ*H*/*T* pada *T* dan *p* tetap',
        'Kriteria Δ*G* < 0 hanya berlaku pada syarat apa? ||| suhu dan tekanan tetap, tanpa kerja selain kerja ekspansi'],
'7.2': ['Hitung Δ*A* untuk 1,00 mol gas ideal yang memuai isotermal dari *V* ke 2*V* pada 300 K. ||| −1,73 kJ',
        'Pada syarat apa Δ*A* < 0 menjadi kriteria spontanitas? ||| suhu dan volume tetap',
        'Mengapa Δ*A* disebut "energi bebas", dan apa yang "tidak bebas" dari energi dalam? ||| −Δ*A* adalah kerja maksimum; *T*Δ*S* harus dipertukarkan sebagai kalor'],
'7.3': ['Hitung Δ*G* pelelehan 1 mol es pada −10 °C dan +10 °C (Δ*H* = 6,01 kJ, Δ*S* = 22,0 J K⁻¹ dianggap tetap). ||| +0,22 kJ; −0,22 kJ',
        'Dari Gambar 7.2, golongkan: (a) pembakaran metana, (b) penguapan air, (c) dimerisasi 2NO₂ → N₂O₄, (d) N₂ + 2O₂ → 2NO₂. ||| (a) selalu spontan; (b) spontan pada *T* tinggi; (c) spontan pada *T* rendah; (d) tidak pernah',
        'Suatu reaksi mempunyai Δ*H*° = +40 kJ dan Δ*S*° = +120 J K⁻¹. Di atas suhu berapa reaksi spontan pada keadaan standar? ||| 333 K',
        'Mengapa Δ*G* = 0 pada titik leleh normal? ||| kedua fasa setimbang pada 1 atm; tidak ada arah yang disukai'],
'7.4': ['Hitung kerja listrik maksimum dari pembakaran 1 mol glukosa (Δ*G*° = −2879 kJ) dan dari sel bahan bakar H₂–O₂ per mol H₂O(l). ||| 2879 kJ; 237 kJ (tegangan 1,23 V)',
        'Mengapa kerja bukan-ekspansi maksimum sama dengan −Δ*G*, bukan −Δ*H*? ||| sebagian energi *T*Δ*S* harus dipertukarkan sebagai kalor dengan lingkungan',
        'Bila Δ*S* reaksi positif, dapatkah kerja listrik maksimum melebihi −Δ*H*? Jelaskan. ||| ya; sel menyerap kalor dari lingkungan dan mengubahnya menjadi kerja'],
'7.5': ['Turunkan $dG = V\\,dp - S\\,dT$ dari $G = H - TS$ dan $dH = T\\,dS + V\\,dp$. ||| *dG* = *dH* − *T dS* − *S dT*',
        'Dari *dG* = *V dp* − *S dT*, apa variabel alami *G*, dan mengapa itu membuat *G* cocok untuk kimia? ||| *T* dan *p*, yang mudah dikendalikan di laboratorium',
        'Tuliskan persamaan fundamental untuk *dU*, *dH*, *dA*, *dG*. ||| *T dS* − *p dV*; *T dS* + *V dp*; −*S dT* − *p dV*; −*S dT* + *V dp*'],
'7.6': ['Dengan hubungan Maxwell $(\\partial S/\\partial p)_T = -(\\partial V/\\partial T)_p$, hitung perubahan entropi 1 mol air bila tekanan naik 100 bar ($\\alpha$ = 2,07 × 10⁻⁴ K⁻¹, $V_\\text{m}$ = 18,07 cm³ mol⁻¹). ||| −0,037 J K⁻¹ mol⁻¹',
        'Turunkan hubungan Maxwell dari $dA = -S\\,dT - p\\,dV$. ||| $(\\partial S/\\partial V)_T = (\\partial p/\\partial T)_V$',
        'Dengan kotak termodinamika (Gambar 7.3), tuliskan turunan $(\\partial G/\\partial T)_p$ dan $(\\partial H/\\partial p)_S$. ||| −*S*; *V*'],
'7.7': ['Δ$_\\text{r}$*G*° sintesis amonia −32,90 kJ pada 298 K dan Δ$_\\text{r}$*H*° −92,22 kJ. Dengan Gibbs–Helmholtz (Δ*H* tetap), hitung Δ$_\\text{r}$*G*° pada 500 K. ||| +7,3 kJ',
        'Mengapa persamaan Gibbs–Helmholtz memakai *G*/*T* dan bukan *G* saja? ||| $\\partial(G/T)/\\partial T = -H/T^2$ hanya memuat *H*, yang hampir tetap',
        'Pada Gambar 7.1, mengapa garis uap paling curam? ||| kemiringan −*S*$_\\text{m}$; entropi uap paling besar'],
'7.8': ['Hitung kenaikan $G_\\text{m}$ gas ideal yang dimampatkan dari 1 bar ke 10 bar pada 298 K, dan air cair dari 1 bar ke 100 bar. ||| +5,71 kJ mol⁻¹; +0,179 kJ mol⁻¹',
        'Pada tekanan berapa grafit dan intan setimbang pada 298 K, bila Δ*G*° = +2,90 kJ mol⁻¹ dan rapatannya 2,26 dan 3,51 g cm⁻³ (anggap tak termampatkan)? ||| ≈ 15 kbar (1,5 GPa)',
        'Mengapa tekanan hampir tidak memengaruhi energi Gibbs zat padat (Gambar 7.4)? ||| volume molarnya kecil: *V*Δ*p* kecil'],
'7.9': ['Hitung Δ$_\\text{r}$*G*° pembakaran metana dan etanol (hasil H₂O cair) dari tabel. ||| −817,9; −1325,3 kJ mol⁻¹',
        'Hitung Δ$_\\text{r}$*G*° untuk 2NO + O₂ → 2NO₂ dan 3O₂ → 2O₃. ||| −70,5 kJ; +326,4 kJ',
        'Hitung Δ$_\\text{r}$*G*° penguraian CaCO₃ pada 298 K dari tabel. ||| +130,4 kJ',
        'Benzena mempunyai Δ$_\\text{f}$*G*° = +124,3 kJ mol⁻¹. Mengapa benzena tetap dapat disimpan bertahun-tahun? ||| tidak stabil secara termodinamika terhadap unsur, tetapi peruraiannya sangat lambat (stabil kinetik)',
        '@ellingham [P] Dari Gambar 7.5, perkirakan suhu terendah tempat karbon (menjadi CO) dapat mereduksi FeO pada keadaan standar, lalu jelaskan mengapa garis CO turun sedangkan garis oksida logam naik. ||| ≈ 1020 K; Δ*S*° pembentukan CO positif (gas bertambah), oksida logam negatif'],
}
for k, b in S.items(): print(k, soal(N, k, b))
print(tanya(N, '7.2', ['Kapan kimiawan memakai energi Helmholtz, dan kapan energi Gibbs? Berikan satu contoh situasi untuk masing-masing.']))
print(tanya(N, '7.4', ['Mengapa tubuh manusia dapat dipandang sebagai mesin isotermal yang dibatasi Δ*G*, bukan mesin kalor yang dibatasi efisiensi Carnot?']))
print(tanya(N, '7.6', ['Apa gunanya hubungan Maxwell bila semua besaran di dalamnya dapat diukur langsung? Petunjuk: entropi tidak dapat diukur langsung.']))
print(tanya(N, '7.8', ['Mengapa energi Gibbs gas bergantung kuat pada tekanan, sedangkan energi Gibbs cairan hampir tidak?']))
print(tanya(N, '7.9', ['Mengapa nilai Δ$_\\text{f}$*G*° yang negatif tidak menjamin bahwa senyawa itu akan terbentuk dengan cepat dari unsurnya?']))
print(bahas(N, r'''**Soal {{ellingham}}.** Untuk satu mol O₂: $2\text{C} + \text{O}_2 \to 2\text{CO}$, Δ*H*° = −221,1 kJ, Δ*S*° = 2(197,67) − 2(5,74) − 205,14 = +178,7 J K⁻¹; $2\text{Fe} + \text{O}_2 \to 2\text{FeO}$, Δ*H*° = −544,0 kJ, Δ*S*° = −138,2 J K⁻¹. Reaksi reduksi $2\text{FeO} + 2\text{C} \to 2\text{Fe} + 2\text{CO}$ adalah selisih keduanya, dengan Δ*H*° = +322,9 kJ dan Δ*S*° = +316,9 J K⁻¹. Δ*G*° = 0 pada
$$
T = \frac{322\,900\ \text{J}}{316{,}9\ \text{J K}^{-1}} \approx 1020\ \text{K} .
$$
Di atas suhu itu garis CO berada di bawah garis FeO pada Gambar 7.5, dan karbon "menang" merebut oksigen.

*Cara berpikir:* kemiringan setiap garis Ellingham adalah −Δ*S*°, dan Δ*S*° hampir seluruhnya ditentukan oleh perubahan jumlah mol gas. Pembentukan oksida padat menghabiskan satu mol gas, sehingga Δ*S*° ≈ −200 J K⁻¹ dan garisnya naik. Pembentukan CO mengubah 1 mol O₂ menjadi 2 mol CO, sehingga Δ*S*° positif dan garisnya turun. Karena itu, pada suhu cukup tinggi karbon dapat mereduksi hampir semua oksida, dan batas praktisnya ditentukan oleh suhu yang dapat dicapai tanur. Penalaran "tanda Δ*S* dari mol gas" ini adalah alat cepat yang sama dengan Gambar 7.2.'''))
