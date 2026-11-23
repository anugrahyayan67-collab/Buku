import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import soal, tanya, bahas
N = 12
S = {
'12.1': ['Untuk N₂O₄ ⇌ 2NO₂ pada 25 °C (Δ$_\\text{r}$*G*° = +4,73 kJ), hitung Δ$_\\text{r}$*G* bila $p_{\\text{N}_2\\text{O}_4}$ = 0,50 bar dan $p_{\\text{NO}_2}$ = 0,20 bar. Ke mana reaksi berjalan? ||| −1,53 kJ mol⁻¹; ke kanan',
         'Mengapa kurva *G* terhadap ξ (Gambar 12.1) mempunyai minimum, walaupun Δ$_\\text{r}$*G*° positif? ||| suku pencampuran *RT* Σ *n* ln *x* selalu menurunkan *G* di antara kedua ujung',
         'Apa arti Δ$_\\text{r}$*G* = 0 dan apa beda maknanya dengan Δ$_\\text{r}$*G*° = 0? ||| Δ$_\\text{r}$*G* = 0: setimbang; Δ$_\\text{r}$*G*° = 0: *K* = 1'],
'12.2': ['Hitung Δ$_\\text{r}$*G*° dan *K* pada 25 °C untuk N₂O₄ ⇌ 2NO₂ (Δ$_\\text{f}$*G*°: NO₂ 51,31; N₂O₄ 97,89 kJ mol⁻¹). ||| +4,73 kJ; 0,148',
         'Hitung *K* pada 25 °C untuk 2SO₂ + O₂ ⇌ 2SO₃ (Δ$_\\text{f}$*G*°: SO₂ −300,19; SO₃ −371,06). Mengapa proses kontak tetap memerlukan katalis? ||| $6{,}8 \\times 10^{24}$; reaksi sangat lambat tanpa katalis',
         'Hitung *K* reaksi pergeseran air–gas CO + H₂O(g) ⇌ CO₂ + H₂ pada 25 °C. ||| $1{,}0 \\times 10^5$',
         'Bila *K* reaksi A ⇌ B adalah 10, berapa *K* untuk 2B ⇌ 2A? ||| 0,010'],
'12.3': ['Ubah *K* = 0,148 untuk N₂O₄ ⇌ 2NO₂ pada 25 °C menjadi *K*$_\\text{c}$ (*c*° = 1 mol L⁻¹). ||| 0,0060',
         'Mengapa padatan dan cairan murni tidak muncul dalam ungkapan *K*? ||| aktivitasnya 1 (keadaan standarnya sendiri)',
         'Kapan *K*$_\\text{x}$ bergantung pada tekanan total, dan kapan tidak? ||| bergantung bila Δν$_\\text{gas}$ ≠ 0'],
'12.4': ['Hitung derajat disosiasi N₂O₄ pada 25 °C dan tekanan total 1,00 bar, lalu pada 10,0 bar (*K* = 0,148). ||| 0,189; 0,061',
         'Untuk H₂ + I₂(g) ⇌ 2HI dengan *K* = 54 pada 700 K, mulai dari 1,00 mol H₂ dan 1,00 mol I₂, berapa mol HI pada kesetimbangan? ||| 1,57 mol',
         'Mengapa untuk reaksi dengan *K* sangat besar kita boleh menganggap reaksi berjalan sempurna lalu menghitung sisa kecil pereaksi? ||| pendekatan itu menghindari pengurangan dua bilangan besar yang hampir sama'],
'12.5': ['Mengapa menambah gas lembam pada volume tetap tidak menggeser kesetimbangan gas ideal, tetapi menambahnya pada tekanan tetap dapat menggesernya? ||| volume tetap: tekanan parsial tidak berubah; tekanan tetap: tekanan parsial semua gas turun',
         'Ke arah mana kesetimbangan 2SO₂ + O₂ ⇌ 2SO₃ bergeser bila tekanan dinaikkan, dan mengapa *K* tidak berubah? ||| ke kanan (mol gas berkurang); *K* hanya bergantung pada suhu'],
'12.6': ['*K* suatu reaksi menjadi dua kali bila suhu naik dari 25 °C ke 35 °C. Berapa Δ$_\\text{r}$*H*°? ||| +52,9 kJ mol⁻¹',
         'Dengan Δ$_\\text{r}$*H*° = +57,2 kJ mol⁻¹, hitung *K* N₂O₄ ⇌ 2NO₂ pada 350 K dari *K* = 0,148 pada 298 K. ||| 4,5',
         'Mengapa plot ln *K* terhadap 1/*T* berupa garis lurus, dan apa arti kemiringannya? ||| van \'t Hoff dengan Δ$_\\text{r}$*H*° tetap; kemiringan −Δ$_\\text{r}$*H*°/*R*'],
'12.7': ['Jelaskan secara termodinamika mengapa menurunkan suhu menaikkan hasil amonia, tetapi pabrik tetap bekerja pada sekitar 450 °C. ||| reaksi eksoterm: *K* naik pada suhu rendah; tetapi laju terlalu lambat',
         'Apakah asas Le Chatelier selalu benar? Berikan contoh menambah satu pereaksi yang justru mengurangi hasil. ||| tidak selalu; menambah N₂ pada campuran kaya N₂ dapat mengurangi hasil NH₃ (Contoh 12.14)'],
'12.8': ['Mengapa proses Haber–Bosch memakai tekanan sekitar 200–300 bar, padahal kompresor sangat mahal? ||| Δν$_\\text{gas}$ = −2: tekanan tinggi menaikkan hasil kesetimbangan',
         'Mengapa reaksi biokimia memakai keadaan standar biokimia (pH 7)? ||| [H⁺] dalam sel sekitar 10⁻⁷ M; keadaan standar 1 M H⁺ jauh dari kenyataan'],
'12.9': ['Hitung *K*$_\\text{sp}$ AgBr pada 25 °C dari Δ$_\\text{f}$*G*°: Ag⁺ +77,11; Br⁻ −103,96; AgBr(s) −96,90 kJ mol⁻¹. ||| $5{,}3 \\times 10^{-13}$',
         'Suatu asam lemah mempunyai Δ$_\\text{r}$*G*° ionisasi +34,0 kJ mol⁻¹. Hitung p*K*$_\\text{a}$-nya pada 25 °C. ||| 5,96',
         'Asam format mempunyai *K*$_\\text{a}$ = 1,8 × 10⁻⁴. Hitung Δ$_\\text{r}$*G*° ionisasinya. ||| +21,4 kJ mol⁻¹',
         'Hitung pH air murni pada 37 °C (p*K*$_\\text{w}$ = 13,62). Apakah darah pH 7,4 basa? ||| 6,81; ya, 0,6 satuan di atas netral',
         'Mengapa nilai Δ$_\\text{f}$*G*° untuk satu jenis ion tidak dapat diukur, dan konvensi apa yang dipakai? ||| larutan harus netral; Δ$_\\text{f}$*G*°(H⁺, aq) = 0',
         '@kwt [P] Ionisasi air mempunyai Δ$_\\text{r}$*H*° = +55,84 kJ mol⁻¹ dan Δ$_\\text{r}$*C*$_p$° ≈ −215 J K⁻¹ mol⁻¹ pada 25 °C. Hitung p*K*$_\\text{w}$ pada 100 °C dengan dan tanpa koreksi Δ*C*$_p$, lalu bandingkan dengan nilai terukur 12,26. ||| tanpa: 12,03; dengan: ≈ 12,26'],
}
for k, b in S.items(): print(k, soal(N, k, b))
print(tanya(N, '12.9', ['Mengapa tabel *K*$_\\text{a}$ dan *K*$_\\text{sp}$ tidak perlu dihafal bila tersedia tabel energi Gibbs pembentukan ion?','Mengapa pH larutan netral bergantung pada suhu?']))
print(tanya(N, '12.6', ['Mengapa reaksi endoterm makin disukai pada suhu tinggi, ditinjau dari entropi lingkungan?']))
print(tanya(N, '12.2', ['Mengapa *K* tidak bersatuan, padahal tampak seperti perbandingan tekanan atau konsentrasi?']))
print(tanya(N, '12.4', ['Mengapa komposisi kesetimbangan tidak bergantung pada arah kita mendekatinya (dari pereaksi atau dari hasil)?']))
