import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import soal, tanya, bahas, sisip
N = 3
print(sisip(N, '3.7', r'''::: {.contoh}
**Contoh 3.xiso · Memampatkan dalam satu, dua, dan tak terhingga tahap**

Sebanyak 2,00 mol gas ideal pada 300 K dimampatkan secara isotermal dari 50,0 L ke 10,0 L. Hitung kerja yang harus diberikan bila pemampatan dilakukan (a) secara reversibel, (b) dalam satu tahap dengan tekanan luar tetap sama dengan tekanan akhir, (c) dalam dua tahap, mula-mula ke 25,0 L dengan tekanan luar sama dengan tekanan gas pada 25,0 L, lalu ke 10,0 L.

**Gambaran fisis.** Pada pemampatan, piston harus didorong dengan tekanan yang **paling sedikit** sama dengan tekanan gas di akhir setiap tahap. Makin sedikit tahap, makin besar tekanan yang harus dipakai sejak awal, dan makin banyak kerja yang "terbuang".

**Penyelesaian.** (a) Dari (3.10), $w = -nRT\ln(V_2/V_1) = -(2{,}00)(8{,}314)(300)\ln(10{,}0/50{,}0) = +8{,}03$ kJ.

(b) Tekanan akhir $p_2 = nRT/V_2 = (2{,}00)(8{,}314)(300)/(0{,}0100\ \text{m}^3) = 4{,}99$ bar, sehingga $w = -p_2(V_2 - V_1) = -(4{,}99 \times 10^5\ \text{Pa})(-0{,}0400\ \text{m}^3) = +19{,}95$ kJ.

(c) Tekanan gas pada 25,0 L adalah 2,00 bar. Tahap pertama: $w_1 = -(2{,}00 \times 10^5)(-0{,}0250) = +4{,}99$ kJ. Tahap kedua: $w_2 = -(4{,}99 \times 10^5)(-0{,}0150) = +7{,}48$ kJ. Totalnya +12,47 kJ.

**Memahami hasil.** Pemampatan satu tahap memerlukan kerja dua setengah kali kerja reversibel, dan dua tahap sudah memangkas kelebihan itu lebih dari separuh. Dengan makin banyak tahap, kerjanya terus turun dan mendekati 8,03 kJ, tetapi tidak pernah lebih kecil. Pada pemuaian, urutannya terbalik: proses reversibel memberi kerja **paling banyak**. Kedua pernyataan itu adalah satu gagasan: proses reversibel adalah batas efisiensi, dan kerja yang hilang di proses nyata menjadi kalor yang harus dibuang (Bab 5 menyebut ukurannya entropi).
:::''', 'Memampatkan dalam satu, dua'))
S = {
'3.1': ['Sebutkan tiga contoh fungsi keadaan dan dua besaran yang bergantung pada jalur. ||| misalnya *U*, *p*, *T*; *q*, *w*',
        'Pendaki naik dari kaki ke puncak gunung lewat jalan landai atau tebing. Besaran apa yang sama untuk kedua jalan, dan apa yang berbeda? Kaitkan dengan *U*, *q*, dan *w*. ||| beda ketinggian sama (seperti Δ*U*); panjang jalan dan tenaga berbeda (seperti *q*, *w*)',
        'Mengapa energi dalam mutlak suatu zat tidak pernah perlu diketahui dalam termodinamika? ||| yang diukur dan dipakai hanya perubahannya, Δ*U*'],
'3.2': ['Gas memuai dari 3,00 L ke 8,00 L melawan tekanan luar tetap 1,50 bar. Hitung *w* dalam joule. ||| −750 J',
        'Sebanyak 6,50 g seng bereaksi dengan HCl berlebih pada 25 °C dan 1 atm. Hitung kerja ekspansi oleh H₂ yang terbentuk. ||| −246 J',
        'Hitung kerja ketika 1,00 mol air menguap pada 100 °C dan 1 atm, dengan dan tanpa memperhitungkan volume cairan (18,8 cm³ mol⁻¹). ||| −3,102 kJ dan −3,100 kJ; volume cairan dapat diabaikan',
        'Mengapa reaksi dalam larutan hampir tidak melakukan kerja ekspansi? ||| perubahan volume cairan dan padatan sangat kecil'],
'3.3': ['Hitung kerja untuk memampatkan 1,00 mol gas ideal secara isotermal reversibel pada 300 K dari 1,00 bar ke 10,0 bar. ||| +5,74 kJ',
        'Mengapa kerja reversibel adalah kerja **paling besar** yang dapat diperoleh dari pemuaian, tetapi kerja **paling kecil** yang diperlukan untuk pemampatan? ||| tekanan luar selalu sama dengan tekanan gas, nilai terbesar yang masih memungkinkan pemuaian dan terkecil yang memungkinkan pemampatan',
        'Pada Gambar 3.3, butir pasir diambil satu per satu. Apa yang terjadi pada kerja bila butirnya dibuat makin kecil dan makin banyak? ||| mendekati kerja reversibel'],
'3.4': ['Hitung kalor untuk memanaskan 250 g aluminium dari 20 °C ke 80 °C ($c$ = 0,897 J g⁻¹ K⁻¹). ||| 13,5 kJ',
        'Sebanyak 100 g air 80 °C dicampur dengan 200 g air 20 °C dalam wadah terisolasi. Berapa suhu akhirnya? ||| 40 °C',
        'Logam 50,0 g pada 100,0 °C dimasukkan ke 100,0 g air 20,0 °C; suhu akhir 24,3 °C. Hitung kalor jenis logam itu. ||| 0,475 J g⁻¹ K⁻¹',
        'Kapasitas kalor molar air cair 75,3 J K⁻¹ mol⁻¹. Hitung kalor jenisnya, lalu jelaskan mengapa air dipakai sebagai pendingin mesin. ||| 4,18 J g⁻¹ K⁻¹; menyerap banyak kalor per gram dengan kenaikan suhu kecil'],
'3.5': ['Sistem menerima kalor 250 J dan melakukan kerja 120 J. Berapa Δ*U*? ||| +130 J',
        'Gas dimampatkan dengan kerja 500 J dan sementara itu melepas kalor 180 J. Berapa Δ*U*, dan apakah suhunya naik bila gas ideal? ||| +320 J; naik',
        'Baterai 1,50 V mengalirkan arus 2,00 A selama 60,0 s sambil melepas kalor 20 J. Berapa perubahan energi dalam baterai? ||| −200 J',
        'Mengapa mesin abadi jenis pertama mustahil? ||| siklus kembali ke keadaan awal: Δ*U* = 0, sehingga −*w* = *q*; kerja tidak dapat diperoleh tanpa kalor'],
'3.6': ['Untuk satu mol gas ideal, apakah $dq = C_V\\,dT + (RT/V)\\,dV$ merupakan diferensial eksak? Uji dengan turunan silang. ||| tidak: ∂C$_V$/∂*V* = 0 ≠ ∂(*RT*/*V*)/∂*T* = *R*/*V*',
        'Tunjukkan bahwa $dU = C_V\\,dT$ untuk gas ideal adalah diferensial eksak. ||| bergantung hanya pada *T*; turunan silang keduanya nol',
        'Dari Gambar 3.4, urutkan kerja yang dilakukan gas pada jalur A, B, dan C, lalu jelaskan mengapa Δ*U* sama untuk ketiganya. ||| $|w_A| < |w_C| < |w_B|$; *U* fungsi keadaan, kedua ujung bersuhu sama'],
'3.7': ['Sebanyak 0,500 mol N₂ memuai secara isotermal reversibel pada 298 K dari 1,00 bar ke 0,200 bar. Hitung *q*. ||| +1,99 kJ',
        'Gas yang sama memuai dari 1,00 bar ke 0,200 bar melawan tekanan luar tetap 0,200 bar. Hitung *w* dan *q*. ||| *w* = −0,99 kJ; *q* = +0,99 kJ',
        'Mengapa pada proses isotermal gas ideal *q* = −*w*? ||| Δ*U* = 0 karena *U* gas ideal hanya bergantung pada *T*'],
'3.8': ['Udara (γ = 1,40) pada 300 K dimampatkan secara adiabatik reversibel sampai volumenya setengah. Berapa suhu akhir dan perbandingan tekanannya? ||| 396 K; 2,64',
        'Argon pada 1,00 bar dan 300 K dimampatkan secara adiabatik reversibel sampai 10,0 bar. Hitung suhu akhir dan kerja per mol. ||| 754 K; +5,66 kJ mol⁻¹',
        'Gas diatomik pada 400 K memuai secara adiabatik reversibel sampai volumenya dua kali. Hitung suhu akhirnya. ||| 303 K',
        '@adb [P] Satu mol gas ideal diatomik pada 300 K dan 10,0 bar memuai sampai 1,00 bar. Bandingkan suhu akhir dan kerjanya untuk (a) adiabatik reversibel dan (b) adiabatik melawan tekanan luar tetap 1,00 bar. ||| (a) 155 K, *w* = −3,01 kJ; (b) 223 K, *w* = −1,60 kJ'],
'3.9': ['Ramalkan $C_{V,\\text{m}}$ CH₄ tanpa getaran dan CO₂ dengan semua getaran aktif menurut ekuipartisi. ||| 24,9 J K⁻¹ mol⁻¹; 54,0 J K⁻¹ mol⁻¹',
        'Hitung γ untuk gas monoatomik, molekul tak linear tanpa getaran, dan CO₂ dengan semua getaran aktif. ||| 1,67; 1,33; 1,15',
        'Hitung energi dalam translasi dan rotasi 1 mol N₂ pada 298 K. ||| 6,20 kJ',
        'Mengapa getaran Cl₂ sudah menyumbang pada suhu kamar, sedangkan getaran H₂ belum? ||| ikatan Cl₂ lemah dan atomnya berat: frekuensi getaran rendah, jarak tingkat energi kecil dibanding *kT*'],
}
for k, b in S.items(): print(k, soal(N, k, b))
print(tanya(N, '3.2', ['Mengapa kerja ekspansi dihitung dengan tekanan luar, bukan tekanan gas? Kapan keduanya sama?']))
print(tanya(N, '3.4', ['Mengapa kapasitas kalor pada tekanan tetap selalu lebih besar daripada pada volume tetap, padahal zatnya sama?']))
print(tanya(N, '3.5', ['Kalor dan kerja keduanya adalah energi yang berpindah. Apa yang membedakan keduanya dari sudut gerak molekul?']))
print(tanya(N, '3.8', ['Mengapa gas yang dimampatkan secara adiabatik menjadi panas, padahal tidak ada kalor yang masuk?']))
print(tanya(N, '3.9', ['Asas ekuipartisi meramalkan $C_{V,\\text{m}}$ yang tidak bergantung suhu. Mengapa kapasitas kalor nyata justru naik bertangga dengan suhu (Gambar 3.7)?']))
