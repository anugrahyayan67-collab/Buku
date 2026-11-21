import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import soal, tanya, bahas
N = 13
S = {
'13.1': ['Tuliskan diagram sel untuk reaksi Zn(s) + 2Ag⁺(aq) → Zn²⁺(aq) + 2Ag(s), dan tentukan anode dan katodenya. ||| Zn|Zn²⁺‖Ag⁺|Ag; anode Zn, katode Ag',
         'Mengapa jembatan garam diperlukan dalam sel Daniell? ||| menjaga kenetralan listrik kedua larutan tanpa mencampurnya',
         'Apa beda sel galvani dan sel elektrolisis dari sudut Δ*G*? ||| galvani: Δ*G* < 0, menghasilkan kerja; elektrolisis: Δ*G* > 0, memerlukan kerja dari luar'],
'13.2': ['Hitung Δ$_\\text{r}$*G* sel Daniell yang tegangannya 1,10 V. ||| −212 kJ mol⁻¹',
         'Hitung tegangan standar sel bahan bakar H₂–O₂ dari Δ$_\\text{r}$*G*° = −237,13 kJ per mol H₂O(l). ||| 1,229 V',
         'Mengapa tegangan sel tidak bergantung pada cara kita menuliskan koefisien reaksi, padahal Δ$_\\text{r}$*G* bergantung? ||| Δ*G* dan *n* sama-sama berlipat; *E* = −Δ*G*/*nF* tetap'],
'13.3': ['Hitung *E*° sel Cu|Cu²⁺‖Ag⁺|Ag dan Zn|Zn²⁺‖Ag⁺|Ag dari Tabel 13.1. ||| 0,460 V; 1,562 V',
         'Logam mana di Tabel 13.1 yang larut dalam HCl 1 M dengan melepaskan H₂? ||| logam dengan *E*° < 0: Li, Na, Zn, Fe',
         'Mengapa *E*° tidak dikalikan dengan koefisien reaksi ketika menggabungkan setengah sel? ||| *E*° besaran intensif (energi per muatan)'],
'13.4': ['Hitung tegangan sel Daniell dengan [Zn²⁺] = 1,0 M dan [Cu²⁺] = 0,010 M pada 25 °C. ||| 1,04 V',
         'Hitung potensial elektrode hidrogen (1 bar H₂) dalam larutan pH 5,0. ||| −0,296 V',
         'Mengapa potensial elektrode yang melibatkan H⁺ bergantung pada pH? ||| [H⁺] muncul dalam suku logaritma Nernst'],
'13.5': ['Hitung *K* reaksi sel Daniell pada 25 °C (*E*° = 1,10 V). ||| $1{,}5 \\times 10^{37}$',
         'Reaksi dengan satu elektron mempunyai *E*° = 0,10 V. Hitung *K*-nya pada 25 °C. ||| 49',
         'Hitung *K*$_\\text{sp}$ AgCl dari *E*°(AgCl/Ag) = 0,222 V dan *E*°(Ag⁺/Ag) = 0,800 V. ||| $1{,}7 \\times 10^{-10}$'],
'13.6': ['Suatu sel dua elektron mempunyai d*E*°/d*T* = −4,0 × 10⁻⁴ V K⁻¹ dan *E*° = 1,10 V pada 25 °C. Hitung Δ$_\\text{r}$*S*° dan Δ$_\\text{r}$*H*°. ||| −77,2 J K⁻¹ mol⁻¹; −235 kJ mol⁻¹',
         'Mengapa pengukuran tegangan pada beberapa suhu memberi Δ*S* reaksi tanpa kalorimeter? ||| (∂Δ*G*/∂*T*)$_p$ = −Δ*S* dan Δ*G* = −*nFE*'],
'13.7': ['Hitung tegangan sel konsentrasi Cu|Cu²⁺(0,0010 M)‖Cu²⁺(0,10 M)|Cu pada 25 °C. ||| 0,059 V',
         'Hitung potensial membran sel saraf yang ditentukan K⁺ (140 mM di dalam, 5 mM di luar) pada 37 °C. ||| 89 mV',
         'Mengapa elektrode kaca harus dikalibrasi dengan larutan penyangga, padahal responsnya mengikuti Nernst? ||| ada potensial asimetri dan sambungan cairan yang tidak diketahui'],
'13.8': ['Bandingkan energi per mol elektron baterai litium-ion (3,7 V) dan per mol reaksi aki timbal (2,05 V, dua elektron). ||| 357 kJ per mol e⁻; 396 kJ per mol reaksi (198 kJ per mol e⁻)',
         'Mengapa litium dipakai pada baterai berenergi tinggi? ||| *E*° sangat negatif dan massa sangat kecil: energi per kilogram besar'],
'13.9': ['Hitung potensial batas Zn²⁺/Zn, Cu²⁺/Cu, dan Mg²⁺/Mg untuk aktivitas ion 10⁻⁶ (*E*°: Zn −0,762; Cu +0,340; Mg −2,37 V). ||| −0,939; +0,162; −2,55 V',
         'Berapa kemiringan garis Pourbaix untuk reaksi yang memakai 2 H⁺ dan 2 elektron, dan untuk 3 H⁺ dan 1 elektron? ||| −0,059 V per pH; −0,177 V per pH',
         'Hitung potensial O₂/H₂O dan H₂O/H₂ pada pH 8 (tekanan gas 1 bar). ||| +0,756 V; −0,473 V',
         'Berapa massa anode magnesium yang habis per tahun bila arus perlindungan rata-rata 1,0 A? ||| 4,0 kg',
         'Mengapa tembaga tidak berkarat di air netral bebas oksigen, tetapi besi berkarat? Pakai potensial batas logam dan garis H₂O/H₂. ||| batas Cu (+0,16 V) di atas garis H₂O/H₂ (−0,41 V): air tidak dapat mengoksidasi Cu; batas Fe (−0,62 V) di bawahnya',
         '@pb [P] Turunkan persamaan garis batas Fe(OH)₃/Fe²⁺ pada diagram Pourbaix besi dan tunjukkan bahwa garis itu melewati titik (pH 3,15; 0,771 V) dengan kemiringan −0,177 V per pH. ||| $E = E^\\circ{}\' - 0{,}177\\,\\text{pH} - 0{,}059\\,16\\log[\\text{Fe}^{2+}]$'],
}
for k, b in S.items(): print(k, soal(N, k, b))
print(tanya(N, '13.9', ['Apa arti tiga jenis garis (mendatar, tegak, miring) pada diagram Pourbaix?','Mengapa tulangan baja di dalam beton tidak berkarat, tetapi mulai berkarat setelah beton terkarbonasi?','Mengapa proteksi katodik tidak boleh berlebihan?']))
print(tanya(N, '13.4', ['Mengapa tegangan baterai turun perlahan ketika dipakai, lalu jatuh tajam menjelang habis?']))
print(tanya(N, '13.6', ['Mengapa sel dengan Δ*S* positif dapat menghasilkan kerja listrik lebih besar daripada −Δ*H*?']))
print(bahas(N, r'''**Soal {{pb}}.** Reaksinya $\text{Fe(OH)}_3(s) + 3\text{H}^+ + e^- \rightleftharpoons \text{Fe}^{2+} + 3\text{H}_2\text{O}$. Persamaan Nernst untuk setengah reaksi ini adalah
$$
E = E^{\circ\prime} - 0{,}059\,16\log\frac{[\text{Fe}^{2+}]}{[\text{H}^+]^3} = E^{\circ\prime} - 0{,}059\,16\log[\text{Fe}^{2+}] - 3(0{,}059\,16)\,\text{pH} ,
$$
karena $-\log[\text{H}^+]^3 = 3\,\text{pH}$. Jadi kemiringannya $-0{,}177$ V per pH. Untuk menentukan $E^{\circ\prime}$ tanpa data tambahan, perhatikan bahwa garis ini harus bertemu dengan dua garis lain di satu titik: garis tegak Fe³⁺/Fe(OH)₃ pada pH 3,15 (Contoh 13.18) dan garis mendatar Fe³⁺/Fe²⁺ pada 0,771 V. Di titik itu ketiga spesies (Fe³⁺, Fe²⁺, Fe(OH)₃) setimbang bersama, sehingga semua persamaan batas harus memberi potensial yang sama. Dengan $[\text{Fe}^{2+}] = 10^{-6}$, garis kita adalah $E = 0{,}771 - 0{,}177(\text{pH} - 3{,}15)$.

*Cara berpikir:* diagram Pourbaix tidak memerlukan data baru di luar *E*° dan *K*$_\text{sp}$; setiap garis adalah persamaan Nernst atau ungkapan *K* yang ditulis dalam pH. Titik pertemuan tiga garis adalah "titik tripel" diagram ini, dan sama seperti titik tripel diagram fasa (Bab 8), aturan fasa menjamin bahwa ketiga batas bertemu di satu titik. Kemiringan garis cukup dihitung dari perbandingan H⁺ terhadap elektron, sehingga bentuk diagram dapat diramalkan bahkan sebelum angka pastinya dihitung.'''))
