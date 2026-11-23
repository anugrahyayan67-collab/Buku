import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import sisip, soal
N = 5
print(sisip(N, '5.1', r'''::: {.terapan}
**Makhluk hidup dan hukum kedua.** Sel hidup membangun protein dan DNA yang sangat teratur dari molekul-molekul kecil yang tersebar. Apakah kehidupan melanggar hukum kedua? Tidak. Organisme adalah sistem terbuka. Ia mengambil makanan (atau cahaya matahari bagi tumbuhan), yang menyimpan energi dalam bentuk yang terkumpul, lalu mengeluarkan kalor, CO₂, dan air, yang jauh lebih tersebar. Kenaikan entropi lingkungan karena kalor dan zat buangan itu selalu lebih besar daripada penurunan entropi di dalam sel. Kita hidup dengan terus-menerus "mengekspor" entropi; berhenti makan berarti berhenti mampu melakukannya.
:::''', 'Makhluk hidup dan hukum kedua'))

print(sisip(N, '5.2', r'''::: {.contoh}
**Contoh 5.t1 · Efisiensi mesin bensin ideal**

Mesin bensin dapat dimodelkan dengan **siklus Otto**: kompresi adiabatik, pembakaran cepat pada volume tetap, ekspansi adiabatik, dan pembuangan kalor pada volume tetap. Untuk siklus ini, efisiensinya hanya bergantung pada perbandingan kompresi $r = V_\text{maks}/V_\text{min}$:
$$
\eta_\text{Otto} = 1 - r^{1 - \gamma} .
$$
Hitung efisiensi ideal untuk $r = 8$ dan $r = 10$ dengan $\gamma = 1{,}40$, lalu bandingkan dengan efisiensi mesin mobil nyata, sekitar 25–30%.

**Penyelesaian.** $r = 8$: $\eta = 1 - 8^{-0{,}40} = 0{,}565$. $r = 10$: $\eta = 1 - 10^{-0{,}40} = 0{,}602$.

**Memahami hasil.** Mesin nyata hanya mencapai setengah efisiensi ideal ini, karena gesekan, kebocoran kalor melalui dinding silinder, pembakaran yang tidak seketika, dan gas buang yang masih panas. Rumus ini juga menjelaskan mengapa perbandingan kompresi yang lebih tinggi menaikkan efisiensi; batasnya adalah ketukan mesin (*knocking*), yaitu penyalaan dini campuran bensin dan udara yang terlalu panas karena dimampatkan (bandingkan Contoh 3.11). Bensin dengan angka oktan lebih tinggi tahan terhadap penyalaan dini, sehingga memungkinkan perbandingan kompresi lebih tinggi.
:::''', 'Efisiensi mesin bensin ideal'))

print(sisip(N, '5.4', r'''::: {.contoh}
**Contoh 5.t2 · Berapa kerja yang tersimpan dalam air panas?**

Satu kilogram air pada 90 °C didinginkan sampai suhu lingkungan, 20 °C. (a) Berapa kalor yang dilepaskan? (b) Berapa kerja maksimum yang dapat diperoleh bila kalor itu dimasukkan ke serangkaian mesin Carnot yang membuang kalor ke lingkungan 20 °C?

**Rencana.** Suhu air turun selama proses, sehingga efisiensi Carnot berubah terus. Untuk setiap kalor kecil $dq = -C\,dT$ yang dilepaskan air pada suhu *T*, mesin Carnot memberi kerja $dw = (1 - T_0/T)\,dq$ dengan $T_0 = 293{,}15$ K.

**Penyelesaian.** (a) $q = C\Delta T = (4184\ \text{J K}^{-1})(70\ \text{K}) = 293$ kJ.

(b) Mengintegralkan dari $T_1 = 363{,}15$ K ke $T_0$:
$$
|w|_\text{maks} = \int_{T_0}^{T_1}C\left(1 - \frac{T_0}{T}\right)dT = C\left[(T_1 - T_0) - T_0\ln\frac{T_1}{T_0}\right] = 4184\left[70 - 293{,}15\ln\frac{363{,}15}{293{,}15}\right]\ \text{J} = 30{,}2\ \text{kJ} .
$$

**Memahami hasil.** Hanya sekitar 10% kalor air panas yang dapat diubah menjadi kerja; sisanya pasti terbuang ke lingkungan. Kerja maksimum ini disebut **eksergi**. Air panas suam-suam kuku banyak mengandung energi, tetapi sedikit eksergi. Itulah sebabnya "limbah panas" dari pabrik, walaupun jumlah energinya besar, sukar dimanfaatkan untuk menghasilkan listrik, dan lebih sering dipakai langsung untuk pemanasan.
:::

::: {.dalam}
**Lebih dalam: skala suhu termodinamika.** Persamaan (5.2) memberi cara mendefinisikan suhu yang sama sekali tidak bergantung pada zat termometrik. Jalankan mesin Carnot antara benda yang suhunya hendak diukur dan sel titik tripel air; perbandingan kalor yang dipertukarkan sama dengan perbandingan suhunya: $T = 273{,}16\ \text{K} \times |q|/|q_3|$. Karena efisiensi Carnot berlaku untuk semua zat kerja, skala ini universal. Bila zat kerjanya gas ideal, perhitungan subbab 5.4 menunjukkan bahwa skala ini identik dengan skala termometer gas ideal (persamaan 1.1). Inilah alasan kelvin disebut satuan suhu **termodinamika**, dan alasan nol mutlak tidak dapat dicapai: mesin Carnot yang membuang kalor ke 0 K akan berefisiensi 100%, melanggar pernyataan Kelvin.
:::''', 'Berapa kerja yang tersimpan dalam air panas'))

print(sisip(N, '5.5', r'''::: {.contoh}
**Contoh 5.t3 · Pompa kalor atau pemanas listrik?**

Sebuah ruangan memerlukan 10 kWh kalor per hari. Bandingkan listrik yang diperlukan oleh pemanas listrik biasa dan oleh pompa kalor nyata dengan COP 3,5.

**Penyelesaian.** Pemanas listrik mengubah listrik menjadi kalor satu banding satu: 10 kWh. Pompa kalor: $10/3{,}5 = 2{,}9$ kWh.

**Memahami hasil.** Pompa kalor menghemat hampir tiga perempat listrik, karena ia tidak **membuat** kalor dari listrik, melainkan **memindahkan** kalor yang sudah ada di udara luar. Pemanas listrik, sebaliknya, memakai energi berkualitas tinggi (listrik, yang dapat diubah seluruhnya menjadi kerja) untuk menghasilkan energi berkualitas rendah (kalor pada suhu kamar). Dari sudut hukum kedua, itu pemborosan: eksergi listrik dibuang begitu saja.
:::''', 'Pompa kalor atau pemanas listrik'))

print(sisip(N, '5.6', r'''::: {.contoh}
**Contoh 5.t4 · Aturan Trouton**

Hitung entropi penguapan pada titik didih normal untuk benzena (30,8 kJ mol⁻¹, 353,2 K), karbon tetraklorida (30,0 kJ mol⁻¹, 349,9 K), sikloheksana (30,0 kJ mol⁻¹, 353,9 K), air (40,66 kJ mol⁻¹, 373,15 K), dan etanol (38,6 kJ mol⁻¹, 351,4 K). Apa polanya?

**Penyelesaian.** Dari (5.9): benzena 87,2; CCl₄ 85,7; sikloheksana 84,8; air 109,0; etanol 109,8 J K⁻¹ mol⁻¹.

**Memahami hasil.** Untuk cairan nonpolar, entropi penguapan hampir sama, sekitar 85 J K⁻¹ mol⁻¹. Pengamatan ini disebut **aturan Trouton**. Alasannya: penguapan membebaskan molekul dari ruang cairan ke ruang gas yang kira-kira sama besar untuk semua zat pada tekanan 1 atm, sehingga kenaikan "penyebarannya" pun kira-kira sama. Air dan etanol menyimpang jauh ke atas, karena molekul-molekulnya di dalam cairan sudah tertata oleh ikatan hidrogen; penguapan menghancurkan keteraturan tambahan itu. Aturan Trouton berguna untuk menaksir entalpi penguapan dari titik didih: $\Delta_\text{vap}H \approx (85\ \text{J K}^{-1}\text{mol}^{-1})T_\text{b}$.
:::''', 'Aturan Trouton'))

print(sisip(N, '5.7', r'''::: {.contoh}
**Contoh 5.t5 · Entropi pencampuran dua gas**

Satu mol N₂ dan satu mol O₂, masing-masing pada 1 bar dan 25 °C, dipisahkan oleh sekat di dalam wadah. Sekat dibuka dan kedua gas bercampur pada suhu tetap. Hitung perubahan entropinya.

**Penyelesaian.** Setiap gas, yang bersifat ideal, memuai dari volumenya semula ke volume total, dua kali lebih besar, tanpa memengaruhi gas lain. Untuk masing-masing gas $\Delta S = R\ln2$, sehingga
$$
\Delta S_\text{campur} = 2R\ln2 = 11{,}5\ \text{J K}^{-1} .
$$
Tidak ada kalor yang dipertukarkan (gas ideal, suhu tetap), sehingga $\Delta S_\text{lingk} = 0$ dan $\Delta S_\text{total} = +11{,}5$ J K⁻¹.

**Memahami hasil.** Pencampuran gas spontan sepenuhnya karena entropi, tanpa sumbangan energi sama sekali. Rumus umumnya, $\Delta S_\text{campur} = -nR\sum x_J\ln x_J$, akan diturunkan di Bab 10 dan menjadi dasar termodinamika larutan.
:::

::: {.awas}
**Entropi sistem boleh turun.** Hukum kedua hanya melarang penurunan entropi **total** (sistem terisolasi atau semesta). Entropi sistem yang tidak terisolasi dapat turun, misalnya ketika air membeku atau gas dimampatkan, asalkan entropi lingkungannya naik sekurang-kurangnya sebanyak itu. Kesalahan yang sering terjadi adalah menyimpulkan bahwa suatu proses tidak mungkin hanya karena $\Delta S_\text{sistem} < 0$.
:::''', 'Entropi pencampuran dua gas'))

print(sisip(N, '5.8', r'''::: {.contoh}
**Contoh 5.t6 · Entropi setumpuk kartu yang dikocok**

Satu pak kartu remi berisi 52 kartu berbeda. (a) Berapa "entropi susunan" pak kartu yang dikocok sempurna menurut rumus Boltzmann? (b) Bandingkan dengan perubahan entropi termal ketika pak kartu itu (kapasitas kalor sekitar 100 J K⁻¹) dihangatkan dari 25 °C ke 26 °C.

**Penyelesaian.** (a) Ada $52!$ susunan, sehingga $S = k\ln52! = (1{,}381 \times 10^{-23})(156{,}4) = 2{,}2 \times 10^{-21}$ J K⁻¹.

(b) $\Delta S = C\ln(T_2/T_1) = 100\ln(299{,}15/298{,}15) = 0{,}34$ J K⁻¹.

**Memahami hasil.** Menghangatkan kartu satu derajat saja menaikkan entropinya $10^{20}$ kali lebih banyak daripada mengocoknya. Entropi termodinamika hampir seluruhnya berasal dari susunan **molekul** dan energinya, yang jumlahnya mencapai $10^{23}$, bukan dari susunan benda-benda makroskopik. "Kamar yang berantakan" adalah perumpamaan yang berguna untuk memahami entropi, tetapi entropi kamar itu sendiri hampir tidak berubah karena berantakan.
:::

::: {.dalam}
**Lebih dalam: rumus Stirling dan entropi pencampuran.** Untuk *N* yang besar, $\ln N! \approx N\ln N - N$ (rumus Stirling). Bila $N_A$ molekul A dan $N_B$ molekul B ditempatkan pada $N = N_A + N_B$ tempat, banyaknya susunan adalah $W = N!/(N_A!\,N_B!)$. Dengan rumus Stirling,
$$
\ln W \approx N\ln N - N_A\ln N_A - N_B\ln N_B = -N(x_A\ln x_A + x_B\ln x_B) ,
$$
dengan $x_A = N_A/N$. Mengalikan dengan *k* dan memakai $Nk = nR$:
$$
\Delta S_\text{campur} = -nR(x_A\ln x_A + x_B\ln x_B) .
$$
Untuk $x_A = x_B = \tfrac12$ dan $n = 2$ mol, hasilnya $2R\ln2$, sama dengan Contoh 5.t5 yang dihitung dari ekspansi isotermal. Sekali lagi, menghitung susunan dan menghitung kalor reversibel memberi jawaban yang sama.
:::''', 'Entropi setumpuk kartu'))

soal(N, '5.2', [r'Hitung efisiensi ideal siklus Otto dengan perbandingan kompresi 9 dan $\gamma = 1{,}40$. ||| 0,585'])
soal(N, '5.4', [r'Berapa kerja maksimum yang dapat diperoleh dari 1,00 kg air yang mendingin dari 60 °C ke lingkungan 20 °C? ||| 10,5 kJ (dari 167 kJ kalor)',
                r'Mengapa nol mutlak tidak dapat dicapai menurut efisiensi Carnot? ||| mesin yang membuang kalor ke 0 K berefisiensi 100%, melanggar Kelvin'])
soal(N, '5.5', [r'Pompa kalor nyata dengan COP 3,0 memanaskan rumah. Berapa kWh listrik untuk 15 kWh kalor? ||| 5,0 kWh'])
soal(N, '5.6', [r'Taksir entalpi penguapan toluena (titik didih 383,8 K) dengan aturan Trouton. ||| ≈ 32,6 kJ mol⁻¹ (terukur 33,2)',
                r'Mengapa entropi penguapan metana (73 J K⁻¹ mol⁻¹) di bawah nilai Trouton? ||| titik didih sangat rendah; volume molar gas pada 1 atm lebih kecil, sehingga kenaikan "ruang" lebih kecil'])
soal(N, '5.7', [r'Hitung entropi pencampuran 1,00 mol Ar dengan 3,00 mol He pada suhu dan tekanan tetap. ||| +18,7 J K⁻¹',
                r'Hitung Δ*S* total ketika 1,00 kg air 100 °C dicampur dengan 1,00 kg air 0 °C dalam wadah terisolasi. ||| +101 J K⁻¹'])
soal(N, '5.8', [r'Hitung $\ln 100!$ secara tepat dan dengan rumus Stirling. Berapa persen selisihnya? ||| 363,7 dan 360,5; 0,9%',
                r'Berapa entropi susunan 10 kartu berbeda yang dikocok, dalam J K⁻¹? ||| $2{,}09 \times 10^{-22}$ J K⁻¹'])
