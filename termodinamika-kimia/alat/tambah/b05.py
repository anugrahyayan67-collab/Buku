import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import soal, tanya, bahas
N = 5
S = {
'5.1': ['Manakah yang spontan: (a) es mencair pada 10 °C, (b) garam terpisah sendiri dari larutannya, (c) besi berkarat di udara lembap, (d) kalor mengalir dari kopi dingin ke tangan yang hangat? ||| (a) dan (c)',
        'Mengapa "spontan" tidak berarti "cepat"? Berikan contoh. ||| spontan menyatakan arah, bukan laju; intan → grafit spontan tetapi sangat lambat',
        'Reaksi yang endoterm, seperti melarutnya NH₄NO₃ dalam air, tetap berlangsung spontan. Apa artinya bagi gagasan bahwa reaksi spontan selalu melepas energi? ||| keliru; yang menentukan arah adalah entropi total'],
'5.2': ['Mesin menyerap 2000 J dari reservoir panas dan membuang 1200 J ke reservoir dingin per siklus. Hitung kerja dan efisiensinya. ||| 800 J; 0,40',
        'Nyatakan hukum kedua menurut Kelvin–Planck dan menurut Clausius, lalu jelaskan mengapa keduanya setara. ||| mesin yang melanggar satu dapat dipakai membuat mesin yang melanggar yang lain',
        'Mengapa mesin kalor harus membuang sebagian kalornya ke reservoir dingin? ||| tanpa membuang kalor, entropi yang masuk bersama $q_\\text{h}$ tidak dapat keluar; siklus tidak kembali ke keadaan awal'],
'5.3': ['Pada tahap mana dalam siklus Carnot gas menyerap kalor, dan pada tahap mana suhunya berubah? ||| isotermal panas; kedua tahap adiabatik',
        'Mengapa tahap isotermal siklus Carnot harus dijalankan sangat lambat? ||| supaya reversibel: suhu gas hampir sama dengan reservoir',
        'Pada Gambar 5.2, mengapa luas di dalam siklus sama dengan kerja bersih per siklus? ||| kerja = −∮*p dV*; luas di bawah ekspansi dikurangi luas di bawah kompresi'],
'5.4': ['Hitung efisiensi Carnot untuk mesin antara 600 K dan 300 K, dan antara 1100 K dan 310 K. ||| 0,50; 0,72',
        'Pembangkit listrik 1000 MW bekerja dengan efisiensi 38%. Berapa kalor yang dibuang ke sungai atau menara pendingin per detik? ||| 1630 MW',
        'Dua mesin Carnot dirangkai: yang pertama antara 900 K dan 600 K, yang kedua memakai kalor buangan pertama dan membuang ke 300 K. Berapa efisiensi gabungannya? ||| 2/3, sama dengan satu mesin 900 K → 300 K',
        'Dari Gambar 5.3, mengapa menaikkan $T_\\text{h}$ dari 800 K ke 1400 K hanya menaikkan efisiensi Carnot sekitar 15 poin persen? ||| kurva mendatar: $1 - T_\\text{c}/T_\\text{h}$ makin peka hanya bila $T_\\text{h}$ kecil'],
'5.5': ['Hitung COP maksimum pendingin dengan ruang beku −18 °C dan dapur 25 °C, serta pompa kalor antara 0 °C dan 35 °C. ||| 5,9; 8,8',
        'Berapa kerja minimum untuk mengambil 100 kJ kalor dari ruang beku −18 °C ke dapur 25 °C? ||| 16,9 kJ',
        'Pompa kalor memasok 10,0 kW kalor ke rumah pada 40 °C dari udara luar 5 °C. Berapa daya listrik minimumnya? ||| 1,12 kW',
        'Lemari es dibiarkan terbuka di ruangan tertutup. Apakah ruangan menjadi dingin? Jelaskan dengan hukum pertama dan kedua. ||| tidak; ruangan memanas karena kerja kompresor ikut menjadi kalor'],
'5.6': ['Hitung Δ*S* untuk melelehkan 1 mol es pada 0 °C dan menguapkan 1 mol air pada 100 °C. ||| +22,0 J K⁻¹; +109,0 J K⁻¹',
        'Hitung Δ*S* untuk 2,00 mol gas ideal yang volumenya menjadi dua kali pada suhu tetap. ||| +11,5 J K⁻¹',
        'Hitung Δ*S* untuk memanaskan 1,00 kg air dari 20 °C ke 80 °C. ||| +779 J K⁻¹',
        'Dari Gambar 5.6, mengapa siklus Carnot berbentuk persegi panjang pada diagram *T*–*S*? ||| isotermal: *T* tetap (mendatar); adiabatik reversibel: *S* tetap (tegak)'],
'5.7': ['Kalor 1000 J mengalir langsung dari benda 400 K ke benda 300 K. Hitung Δ*S* total. ||| +0,833 J K⁻¹',
        '@campurair [P] Sebanyak 100 g air 80 °C dicampur dengan 100 g air 20 °C dalam wadah terisolasi. Hitung Δ*S* total dan jelaskan tandanya. ||| +3,62 J K⁻¹; proses spontan tak reversibel',
        'Satu mol gas ideal memuai bebas ke ruang hampa sampai volumenya dua kali. Hitung Δ*S* sistem, lingkungan, dan total. ||| +5,76; 0; +5,76 J K⁻¹',
        'Mengapa entropi sistem boleh turun, misalnya air membeku di lemari es, tanpa melanggar hukum kedua? ||| entropi lingkungan naik lebih banyak; yang tidak boleh turun adalah entropi total'],
'5.8': ['Berapa peluang keempat molekul gas berada di separuh kiri wadah? Dan peluang 100 molekul? ||| 1/16; $7{,}9 \\times 10^{-31}$',
        'Gunakan $S = k\\ln W$ untuk menghitung kenaikan entropi 1 mol gas yang volumenya menjadi dua kali, dengan $W$ naik menjadi $2^{N_\\text{A}}$ kali. ||| $R\\ln2$ = 5,76 J K⁻¹ mol⁻¹',
        'Kristal CO pada 0 K mempunyai entropi sisa sekitar *R* ln 2. Jelaskan asalnya. ||| setiap molekul dapat menghadap C–O atau O–C dengan energi hampir sama'],
}
for k, b in S.items(): print(k, soal(N, k, b))
print(tanya(N, '5.2', ['Mengapa kalor tidak dapat diubah seluruhnya menjadi kerja dalam siklus, padahal kerja dapat diubah seluruhnya menjadi kalor (misalnya oleh gesekan)?']))
print(tanya(N, '5.4', ['Efisiensi Carnot tidak bergantung pada zat kerja. Mengapa hal ini mengejutkan, dan apa yang dibuktikannya tentang skala suhu?']))
print(tanya(N, '5.6', ['Mengapa Δ*S* harus dihitung dengan kalor reversibel walaupun proses yang sebenarnya tak reversibel?']))
print(tanya(N, '5.7', ['Jelaskan mengapa hukum kedua sering dikatakan menetapkan "arah waktu".']))
print(tanya(N, '5.8', ['Hukum kedua menurut Boltzmann bersifat statistik. Mengapa kita tidak pernah melihat pelanggarannya dalam sistem makroskopik?']))
print(bahas(N, r'''**Soal {{campurair}}.** Kedua bagian air bermassa sama, jadi suhu akhirnya rata-rata, 50 °C = 323,15 K. Proses nyata ini tak reversibel, tetapi entropi adalah fungsi keadaan, sehingga kita boleh menghitung Δ*S* setiap bagian sepanjang pemanasan atau pendinginan reversibel antara keadaan yang sama:
$$
\Delta S = mc\ln\frac{T_\text{akhir}}{T_\text{awal}} .
$$
Air panas: $(100)(4{,}184)\ln(323{,}15/353{,}15) = -37{,}13$ J K⁻¹. Air dingin: $(100)(4{,}184)\ln(323{,}15/293{,}15) = +40{,}75$ J K⁻¹. Totalnya +3,62 J K⁻¹. Wadah terisolasi, jadi entropi lingkungan tidak berubah.

*Cara berpikir:* air dingin menerima kalor yang sama besar dengan yang dilepas air panas, tetapi pada suhu yang lebih rendah. Karena kenaikan entropi sebanding dengan $dq/T$, joule yang sama "bernilai" lebih banyak entropi bagi benda dingin. Itulah sebabnya pencampuran ini selalu menaikkan entropi total, dan kebalikannya, air hangat memisah sendiri menjadi bagian panas dan dingin, tidak pernah terjadi. Pola "hitung Δ*S* lewat jalur reversibel pengganti" dipakai lagi di Bab 6 untuk perubahan fasa dan reaksi.'''))
