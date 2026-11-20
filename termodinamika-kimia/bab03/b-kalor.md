## 3.4 Kalor dan kapasitas kalor

Cara kedua energi masuk atau keluar dari sistem adalah kalor. Bila sistem dan lingkungannya berbeda suhu dan batasnya tidak terisolasi, energi mengalir dari yang panas ke yang dingin sampai suhunya sama. Batas yang mengizinkan aliran kalor disebut **diatermik**, dan batas yang tidak mengizinkannya disebut **adiabatik**. Proses yang berlangsung di dalam wadah adiabatik, sehingga $q = 0$, disebut **proses adiabatik**.

Bagaimana kalor diukur? Kita tidak dapat melihat kalor mengalir, tetapi kita dapat melihat akibatnya: suhu berubah. Untuk sistem yang tidak mengalami reaksi atau perubahan fasa, kenaikan suhu sebanding dengan kalor yang diterima, dan tetapan kesebandingannya disebut **kapasitas kalor** *C*:

$$
q = C\,\Delta T . \qquad \text{(3.5)}
$$

Kapasitas kalor adalah besaran ekstensif: dua kali lebih banyak air memerlukan dua kali lebih banyak kalor untuk kenaikan suhu yang sama. Versi intensifnya adalah **kapasitas kalor spesifik** $c_s = C/m$ (per gram) dan **kapasitas kalor molar** $C_\text{m} = C/n$ (per mol). Air mempunyai kapasitas kalor spesifik yang luar biasa besar, 4,184 J K⁻¹ g⁻¹; itulah sebabnya laut menjaga iklim pantai tetap sejuk, dan itulah sebabnya kalori didefinisikan dari air (1 cal = 4,184 J tepat).

Ada satu kehalusan. Kapasitas kalor bergantung pada **kondisi** pemanasan. Bila volume dijaga tetap, semua kalor dipakai untuk menaikkan energi dalam; kapasitas kalor ini diberi lambang $C_V$. Bila tekanan dijaga tetap, sistem juga memuai dan melakukan kerja terhadap lingkungannya, sehingga diperlukan lebih banyak kalor untuk kenaikan suhu yang sama; kapasitas kalor ini diberi lambang $C_p$, dan selalu $C_p \ge C_V$. Hubungan keduanya akan kita bahas di Bab 4.

Alat untuk mengukur kalor disebut **kalorimeter**. Kalorimeter harus dikalibrasi lebih dulu: kita memasukkan sejumlah kalor yang diketahui, biasanya dari pemanas listrik, lalu mengukur kenaikan suhunya. Energi listrik yang diberikan arus *I* pada tegangan $\mathcal E$ selama waktu *t* adalah

$$
q = I\mathcal Et . \qquad \text{(3.6)}
$$

::: {.contoh}
**Contoh 3.4 · Kalibrasi kalorimeter**

Pemanas di dalam kalorimeter dialiri arus 2,00 A dari sumber 12,0 V selama 300 s. Suhu kalorimeter dan isinya naik 2,85 K. (a) Berapa kapasitas kalor kalorimeter? (b) Bila suatu reaksi di dalam kalorimeter yang sama menaikkan suhunya 1,62 K, berapa kalor yang dilepaskan reaksi itu?

**Penyelesaian.** (a) $q = I\mathcal Et = (2{,}00\ \text{A})(12{,}0\ \text{V})(300\ \text{s}) = 7200$ J. Maka $C = q/\Delta T = 7200/2{,}85 = 2526$ J K⁻¹ $= 2{,}53$ kJ K⁻¹.

(b) $q = C\,\Delta T = (2{,}53\ \text{kJ K}^{-1})(1{,}62\ \text{K}) = 4{,}09$ kJ dilepaskan reaksi.

**Memahami hasil.** Kalibrasi listrik sangat teliti karena arus, tegangan, dan waktu dapat diukur dengan ketelitian tinggi. Setelah kapasitas kalor diketahui, kalorimeter berubah menjadi "neraca kalor": cukup baca termometernya.
:::

::: {.contoh}
**Contoh 3.5 · Merebus air untuk teh**

Berapa kalor yang diperlukan untuk memanaskan 250 g air dari 25 °C sampai 100 °C? Berapa lama waktu yang diperlukan ketel listrik 800 W bila semua energinya masuk ke air?

**Penyelesaian.** $q = mc_s\,\Delta T = (250\ \text{g})(4{,}184\ \text{J K}^{-1}\text{g}^{-1})(75\ \text{K}) = 7{,}85 \times 10^4$ J $= 78{,}5$ kJ. Waktunya $t = q/P = 78\,450/800 = 98$ s.

**Memahami hasil.** Dalam kenyataan ketel memerlukan sekitar dua menit, karena sebagian energi memanaskan ketel itu sendiri dan udara di sekitarnya. Perhatikan bahwa kenaikan suhu dalam kelvin sama dengan kenaikan dalam derajat Celsius; untuk selisih suhu, kedua skala dapat dipertukarkan.
:::

::: {.kuis}
**Kuis cepat 3.4** Dua gelas berisi 100 g air dan 100 g etanol ($c_s = 2{,}44$ J K⁻¹ g⁻¹) menerima kalor yang sama. Mana yang suhunya naik lebih banyak, dan berapa kali?
:::

## 3.5 Hukum pertama termodinamika

Kita sekarang mempunyai semua bahan untuk merumuskan hukum pertama. Energi dalam sistem hanya dapat berubah melalui dua jalan: kerja yang dilakukan pada sistem dan kalor yang masuk ke sistem. Tidak ada jalan ketiga. Karena itu:

::: {.inti}
$$
\Delta U = q + w \qquad \text{(3.7)}
$$
**Hukum pertama termodinamika.** Perubahan energi dalam sistem sama dengan kalor yang diterimanya ditambah kerja yang dilakukan padanya. Untuk sistem terisolasi, $q = w = 0$, sehingga $\Delta U = 0$: energi dalam sistem terisolasi tetap.
:::

Bagaimana kita tahu hukum ini benar? Tidak ada penurunan matematisnya; hukum pertama adalah ringkasan dari pengalaman yang tidak pernah dilanggar. Bukti yang paling meyakinkan datang dari percobaan James Joule pada 1840-an. Joule menjatuhkan beban yang memutar kincir di dalam air yang terisolasi. Kincir mengaduk air, dan air menjadi hangat, persis seperti bila air itu dipanaskan dengan api. Kerja mekanis dan kalor menghasilkan efek yang sama, dan jumlah kerja yang diperlukan untuk menaikkan suhu satu gram air satu derajat selalu sama. Kalor bukan zat khusus, seperti yang diyakini sebelumnya, melainkan energi.

Akibat hukum pertama yang paling terkenal adalah mustahilnya **mesin abadi jenis pertama**: mesin yang terus bekerja tanpa diberi energi. Mesin semacam itu akan menghasilkan *w* negatif terus-menerus sambil kembali ke keadaan awalnya (Δ*U* = 0) tanpa menerima kalor, dan itu melanggar (3.7).

::: {.contoh}
**Contoh 3.6 · Membaca hukum pertama**

(a) Gas di dalam silinder menerima kalor 500 J dan mendorong piston dengan kerja 200 J. Berapa Δ*U*? (b) Gas lain dimampatkan dengan kerja 300 J sambil melepaskan kalor 450 J. Berapa Δ*U*?

**Penyelesaian.** (a) Kalor masuk: $q = +500$ J. Gas melakukan kerja, energi keluar: $w = -200$ J. Maka $\Delta U = +300$ J.

(b) Kerja dilakukan pada gas: $w = +300$ J. Kalor keluar: $q = -450$ J. Maka $\Delta U = -150$ J.

**Memahami hasil.** Langkah terpenting adalah menentukan tanda dengan bertanya "apakah energi masuk ke sistem atau keluar?" Setelah tanda benar, hukum pertama hanyalah penjumlahan. Pada (b), energi dalam gas turun walaupun ada kerja yang masuk, karena kalor yang keluar lebih besar.
:::

::: {.contoh}
**Contoh 3.7 · Percobaan Joule dalam angka**

Beban 10,0 kg dijatuhkan dari ketinggian 2,00 m sebanyak 20 kali. Setiap kali jatuh, beban memutar kincir di dalam 1,00 kg air dalam bejana terisolasi. Berapa kenaikan suhu air?

**Penyelesaian.** Kerja yang diberikan pada air sama dengan energi potensial yang dilepaskan beban: $w = 20mgh = 20(10{,}0)(9{,}807)(2{,}00)$ J $= 3923$ J. Bejana terisolasi, jadi $q = 0$ dan $\Delta U = w$. Kenaikan suhunya sama dengan bila air menerima kalor sebesar itu:
$$
\Delta T = \frac{3923\ \text{J}}{(1000\ \text{g})(4{,}184\ \text{J K}^{-1}\text{g}^{-1})} = 0{,}94\ \text{K} .
$$

**Memahami hasil.** Dua puluh kali menjatuhkan beban sepuluh kilogram dari ketinggian dua meter hanya menaikkan suhu satu liter air kurang dari satu derajat. Ini menunjukkan betapa besarnya energi yang tersimpan sebagai "panas" dibanding energi mekanis sehari-hari, dan mengapa Joule memerlukan termometer yang sangat teliti untuk membuktikan kesetaraan keduanya.
:::

::: {.kuis}
**Kuis cepat 3.5** Sebuah reaksi di dalam bom kalorimeter (volume tetap, terisolasi dari laboratorium) melepaskan energi. Berapa Δ*U* sistem gabungan "reaksi + kalorimeter"? Berapa Δ*U* campuran reaksi saja?
:::

## 3.6 Diferensial eksak dan tak eksak

Perbedaan antara fungsi keadaan dan besaran yang bergantung pada jalan mempunyai bahasa matematika yang tepat, dan bahasa itu akan sangat berguna di bab-bab berikutnya. Untuk perubahan yang sangat kecil, hukum pertama ditulis

$$
dU = dq + dw . \qquad \text{(3.8)}
$$

Ketiga suku tampak serupa, tetapi sifatnya berbeda. *dU* adalah **diferensial eksak**: perubahan kecil dari suatu fungsi yang benar-benar ada, sehingga integralnya antara dua keadaan selalu memberi $U_2 - U_1$, apa pun jalannya. *dq* dan *dw* adalah **diferensial tak eksak**: jumlah kecil energi yang berpindah, yang integralnya bergantung pada jalan. Banyak buku menulisnya dengan lambang khusus (đ*q*, đ*w*) untuk mengingatkan perbedaan ini.

::: {.mat}
**Matematika: diferensial total dan uji eksak.** Bila *f* adalah fungsi dua peubah *x* dan *y*, perubahan kecilnya adalah
$$
df = \left(\frac{\partial f}{\partial x}\right)_y dx + \left(\frac{\partial f}{\partial y}\right)_x dy .
$$
Turunan parsial $(\partial f/\partial x)_y$ berarti turunan *f* terhadap *x* dengan *y* dianggap tetap. Suatu ungkapan $M\,dx + N\,dy$ adalah diferensial eksak, yaitu ada fungsi *f* dengan $df = M\,dx + N\,dy$, jika dan hanya jika
$$
\left(\frac{\partial M}{\partial y}\right)_x = \left(\frac{\partial N}{\partial x}\right)_y ,
$$
karena kedua ruas sama dengan turunan kedua campuran $\partial^2 f/\partial x\,\partial y$. Uji ini akan kita pakai lagi untuk menurunkan hubungan Maxwell di Bab 7.
:::

Contoh berikut memperlihatkan perbedaan itu dengan angka.

::: {.contoh}
**Contoh 3.8 · Dua jalan, satu Δ*U***

Satu mol gas ideal monoatomik ($U_\text{m} = \tfrac32RT$ + tetapan) dibawa dari keadaan 1 (1,00 bar; 10,0 L) ke keadaan 2 (2,00 bar; 20,0 L) melalui dua jalan reversibel:
Jalan A: dipanaskan pada volume tetap sampai 2,00 bar, lalu dipanaskan pada tekanan tetap sampai 20,0 L.
Jalan B: dipanaskan pada tekanan tetap sampai 20,0 L, lalu dipanaskan pada volume tetap sampai 2,00 bar.
Hitung Δ*U*, *w*, dan *q* untuk kedua jalan.

**Penyelesaian.** Energi dalam hanya bergantung pada suhu, dan $nRT = pV$, sehingga $\Delta U = \tfrac32(p_2V_2 - p_1V_1) = \tfrac32(4000 - 1000)$ J $= 4500$ J untuk kedua jalan. (Ingat: 1 bar L = 100 J.)

Jalan A: kerja hanya terjadi pada langkah tekanan tetap, $w = -(2{,}00\ \text{bar})(10{,}0\ \text{L}) = -2000$ J. Maka $q = \Delta U - w = 6500$ J.

Jalan B: $w = -(1{,}00\ \text{bar})(10{,}0\ \text{L}) = -1000$ J, dan $q = 5500$ J.

**Memahami hasil.** Δ*U* sama untuk kedua jalan, sedangkan *q* dan *w* berbeda masing-masing 1000 J. Selisih itu saling menghapus dalam jumlah $q + w$. Inilah isi hukum pertama: walaupun kerja dan kalor masing-masing bergantung pada jalan, jumlahnya tidak.
:::

::: {.kuis}
**Kuis cepat 3.6** Gas dibawa melalui suatu siklus dan kembali ke keadaan awalnya. Berapa Δ*U* untuk siklus itu? Apakah *q* dan *w* juga harus nol?
:::
