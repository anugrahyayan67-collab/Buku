# Bab 5 Arah Proses, Siklus Carnot, dan Entropi

Letakkan sebutir es batu di atas meja pada siang hari. Dalam beberapa menit ia mencair menjadi genangan air. Tunggulah sehari penuh: genangan itu tidak akan pernah membeku kembali dengan sendirinya, walaupun hukum pertama sama sekali tidak melarangnya. Energi yang diperlukan untuk membekukannya ada di dalam air itu sendiri; cukup bila air itu memberikan sebagian kalornya kepada udara di sekitarnya. Tetapi hal itu tidak pernah terjadi. Kalor mengalir dari udara hangat ke es, tidak pernah sebaliknya.

Di akhir Bab 4 kita menemui teka-teki serupa. Kompres dingin instan bekerja dengan menyerap kalor; kantong penghangat bekerja dengan melepaskan kalor. Keduanya terjadi dengan sendirinya. Jadi kalor yang dilepaskan atau diserap, yaitu tanda Δ*H*, bukanlah penentu arah suatu proses. Lalu apa?

Pertanyaan yang sama dihadapi para insinyur abad ke-19 dalam bentuk yang lebih praktis. Mesin uap mengubah kalor dari pembakaran batu bara menjadi kerja, tetapi selalu membuang sebagian besar kalornya ke sungai atau udara. Bahkan pembangkit listrik tercanggih saat ini hanya mengubah sekitar 40% kalor bahan bakarnya menjadi listrik. Apakah sisa 60% itu terbuang karena mesinnya kurang baik, atau karena alam memang melarang efisiensi yang lebih tinggi?

Ketiga pertanyaan ini dijawab oleh satu hukum, hukum kedua termodinamika, dan satu besaran, **entropi**. Bab ini membangun keduanya selangkah demi selangkah. Kita mulai dari pengamatan sederhana tentang proses spontan dan mesin kalor, menganalisis mesin ideal yang dirancang Sadi Carnot, dan dari analisis itu menemukan entropi sebagai fungsi keadaan baru. Kita akan melihat bahwa entropi semesta selalu bertambah dalam setiap proses spontan, dan akhirnya, mengikuti Ludwig Boltzmann, kita akan menemukan arti entropi di tingkat molekul: entropi adalah ukuran banyaknya cara molekul dapat menyusun dirinya.

::: {.strategi}
**Pertanyaan pembuka**

1. Mengapa kalor selalu mengalir dari benda panas ke benda dingin, tidak pernah sebaliknya?
2. Mengapa tidak ada mesin yang dapat mengubah semua kalor menjadi kerja?
3. Berapa efisiensi tertinggi yang mungkin bagi sebuah mesin kalor, dan apa yang menentukannya?
4. Mengapa kulkas memerlukan listrik untuk memindahkan kalor dari dalam ke luar?
5. Apa yang sebenarnya diukur oleh entropi?
6. Bagaimana suatu proses yang menyerap kalor dapat berlangsung dengan sendirinya?
:::

::: {.tujuan}
**Tujuan belajar**

Setelah mempelajari bab ini, kamu mampu:

1. Mengenali proses spontan dan menjelaskan mengapa hukum pertama tidak dapat menentukan arah proses.
2. Menyatakan hukum kedua menurut Kelvin dan Clausius serta menjelaskan kesetaraan keduanya.
3. Menghitung *q*, *w*, Δ*U*, Δ*H*, dan Δ*S* pada setiap tahap siklus Carnot gas ideal.
4. Menurunkan dan memakai efisiensi Carnot, $\eta = 1 - T_\text{c}/T_\text{h}$.
5. Menghitung koefisien kinerja mesin pendingin dan pompa kalor.
6. Menunjukkan dari siklus Carnot bahwa entropi adalah fungsi keadaan, dan menghitung Δ*S* untuk proses reversibel sederhana.
7. Memakai ketaksamaan Clausius untuk menentukan apakah suatu proses spontan, dengan menghitung perubahan entropi sistem dan lingkungan.
8. Menafsirkan entropi dengan rumus Boltzmann, $S = k\ln W$.
:::

::: {.mat}
**Prasyarat**

Dari Bab 3: kerja dan kalor pada proses isotermal dan adiabatik gas ideal (subbab 3.7–3.8). Dari Bab 4: entalpi dan kalor perubahan fisika (subbab 4.1, 4.4). Dari matematika: logaritma natural dan integral $\int dx/x$.
:::

## 5.1 Proses spontan dan arah perubahan

Di sekitar kita, banyak hal terjadi dengan sendirinya. Gas memenuhi ruang yang tersedia. Teh panas mendingin sampai suhu ruangan. Gula larut dalam kopi. Besi berkarat. Kayu terbakar bila dinyalakan. Proses-proses seperti ini disebut **proses spontan**: proses yang dapat berlangsung tanpa terus-menerus didorong dari luar.

Kata "spontan" dalam termodinamika tidak berarti "cepat". Berkaratnya besi spontan, tetapi berlangsung bertahun-tahun. Intan pada suhu kamar secara spontan cenderung berubah menjadi grafit, tetapi lajunya begitu lambat sehingga intan bertahan miliaran tahun. Termodinamika hanya mengatakan **apakah** suatu proses dapat terjadi dengan sendirinya; **seberapa cepat** ia terjadi adalah urusan kinetika (*Kimia Fisika 2*).

Setiap proses spontan mempunyai kebalikan yang **tidak** spontan. Gas tidak berkumpul sendiri di satu sudut wadah. Teh dingin tidak memanas sendiri dengan menyerap kalor dari udara yang lebih dingin. Gula tidak keluar sendiri dari larutan menjadi kristal di dasar cangkir. Kebalikan-kebalikan ini tidak melanggar hukum pertama: energi tetap kekal dalam semuanya. Hukum pertama mengizinkan kedua arah, tetapi alam hanya memilih satu.

Apa yang membedakan arah yang dipilih alam? Perhatikan pola yang sama di semua contoh itu. Pada gas yang memuai, molekul-molekul menyebar ke ruang yang lebih luas. Pada teh yang mendingin, energi termal teh menyebar ke udara di sekitarnya. Pada gula yang larut, molekul gula menyebar ke seluruh cairan. Proses spontan tampaknya selalu berupa **penyebaran**: materi dan energi menyebar dari keadaan yang terkumpul ke keadaan yang lebih tersebar. Besaran yang akan kita bangun di bab ini, entropi, adalah ukuran kuantitatif dari penyebaran itu.

::: {.contoh}
**Contoh 5.1 · Spontan atau tidak?**

Tentukan arah spontan proses berikut, lalu jelaskan dari sudut penyebaran: (a) campuran gas H₂ dan N₂ di dalam satu labu; (b) sepotong logam panas yang dicelupkan ke dalam air dingin; (c) tetesan tinta di dalam segelas air; (d) air pada −10 °C dan 1 atm.

**Penyelesaian.** (a) Kedua gas bercampur merata; mereka tidak memisah dengan sendirinya. Molekul masing-masing gas menyebar ke seluruh volume labu. (b) Kalor mengalir dari logam ke air sampai suhunya sama; energi termal menyebar dari benda kecil yang panas ke air yang lebih banyak. (c) Tinta menyebar ke seluruh air. (d) Air membeku menjadi es. Kasus ini tampak berlawanan dengan "penyebaran", karena molekul air justru menjadi lebih teratur. Kuncinya: pembekuan melepaskan kalor ke lingkungan, dan kalor itu menyebar di lingkungan.

**Memahami hasil.** Contoh (d) menunjukkan bahwa kita harus selalu memperhitungkan **lingkungan** juga, bukan hanya sistem. Sistem dapat menjadi lebih teratur asalkan lingkungannya menjadi cukup lebih "tersebar". Neraca keduanya akan kita hitung dengan teliti di subbab 5.7.
:::

::: {.terapan}
**Makhluk hidup dan hukum kedua.** Sel hidup membangun protein dan DNA yang sangat teratur dari molekul-molekul kecil yang tersebar. Apakah kehidupan melanggar hukum kedua? Tidak. Organisme adalah sistem terbuka. Ia mengambil makanan (atau cahaya matahari bagi tumbuhan), yang menyimpan energi dalam bentuk yang terkumpul, lalu mengeluarkan kalor, CO₂, dan air, yang jauh lebih tersebar. Kenaikan entropi lingkungan karena kalor dan zat buangan itu selalu lebih besar daripada penurunan entropi di dalam sel. Kita hidup dengan terus-menerus "mengekspor" entropi; berhenti makan berarti berhenti mampu melakukannya.
:::

::: {.kuis}
**Kuis cepat 5.1** Apakah reaksi spontan selalu berlangsung cepat? Berikan satu contoh reaksi spontan yang sangat lambat.
:::

## 5.2 Mesin kalor dan pernyataan hukum kedua

Hukum kedua termodinamika lahir bukan dari laboratorium kimia, melainkan dari ruang mesin. Pada awal abad ke-19, mesin uap telah mengubah dunia, tetapi tidak ada yang mengerti batas kemampuannya. Pertanyaan para insinyur sederhana: berapa banyak kerja yang dapat diperoleh dari sejumlah kalor?

Setiap **mesin kalor** bekerja dalam **siklus**: ia menerima kalor $q_\text{h}$ dari sumber panas bersuhu $T_\text{h}$ (misalnya ketel uap), melakukan kerja, membuang sebagian kalor $q_\text{c}$ ke penampung dingin bersuhu $T_\text{c}$ (misalnya sungai atau udara), lalu kembali ke keadaan awalnya untuk memulai siklus berikutnya. Karena keadaan awal dan akhir siklus sama, $\Delta U = 0$ untuk satu siklus penuh, dan hukum pertama memberi

$$
|w| = q_\text{h} - |q_\text{c}| .
$$

Ukuran keberhasilan mesin adalah **efisiensinya**, bagian kalor masuk yang diubah menjadi kerja:

$$
\eta = \frac{|w|}{q_\text{h}} = 1 - \frac{|q_\text{c}|}{q_\text{h}} . \qquad \text{(5.1)}
$$

Hukum pertama mengizinkan $\eta = 1$, yaitu mesin yang mengubah **semua** kalor menjadi kerja tanpa membuang apa pun. Mesin seperti ini akan sangat berharga: sebuah kapal dapat berlayar dengan mengambil kalor dari air laut dan mengubahnya seluruhnya menjadi kerja untuk memutar baling-baling. Tidak ada yang pernah berhasil membuatnya. Pengalaman ini dirumuskan menjadi hukum kedua oleh William Thomson (Lord Kelvin):

::: {.inti}
**Hukum kedua termodinamika (Kelvin).** Tidak ada proses siklus yang satu-satunya hasil adalah menyerap kalor dari satu sumber dan mengubahnya seluruhnya menjadi kerja.
:::

Setiap mesin kalor **harus** membuang sebagian kalor ke penampung yang lebih dingin. Rudolf Clausius merumuskan hukum yang sama dari sudut pandang lain:

::: {.inti}
**Hukum kedua termodinamika (Clausius).** Tidak ada proses yang satu-satunya hasil adalah memindahkan kalor dari benda yang lebih dingin ke benda yang lebih panas.
:::

Kedua pernyataan ini tampak berbeda, tetapi sebenarnya setara: bila salah satu dilanggar, yang lain juga pasti dilanggar. Misalkan ada mesin yang melanggar pernyataan Kelvin, mengubah kalor *q* seluruhnya menjadi kerja. Kerja itu dapat dipakai untuk menjalankan kulkas yang memindahkan kalor dari benda dingin ke benda panas. Gabungan keduanya akan memindahkan kalor dari dingin ke panas tanpa bantuan lain, melanggar pernyataan Clausius. Penalaran yang sama berlaku ke arah sebaliknya.

::: {.contoh}
**Contoh 5.2 · Ke mana perginya energi pembangkit listrik?**

Sebuah pembangkit listrik tenaga uap menghasilkan daya listrik 1000 MW dengan efisiensi 40%. (a) Berapa laju kalor yang diterima dari pembakaran batu bara? (b) Berapa laju kalor yang dibuang ke sungai? (c) Bila air sungai yang dipakai untuk pendinginan boleh naik suhunya paling banyak 10 K, berapa ton air per detik yang diperlukan?

**Penyelesaian.** (a) $q_\text{h} = |w|/\eta = 1000/0{,}40 = 2500$ MW.

(b) $|q_\text{c}| = q_\text{h} - |w| = 1500$ MW.

(c) $\dot m = |q_\text{c}|/(c_s\Delta T) = (1{,}5 \times 10^9\ \text{W})/[(4184\ \text{J kg}^{-1}\text{K}^{-1})(10\ \text{K})] = 3{,}6 \times 10^4$ kg s⁻¹, sekitar 36 ton air setiap detik.

**Memahami hasil.** Pembangkit itu membuang kalor ke sungai satu setengah kali lebih banyak daripada energi listrik yang dihasilkannya. Inilah sebabnya pembangkit besar selalu dibangun di tepi sungai, danau, atau laut, atau dilengkapi menara pendingin raksasa. Pertanyaannya: dapatkah insinyur yang lebih pandai menekan buangan itu sampai nol? Hukum kedua menjawab tidak. Seberapa kecil yang mungkin, akan kita hitung di subbab 5.4.
:::

::: {.contoh}
**Contoh 5.3 · Efisiensi mesin bensin ideal**

Mesin bensin dapat dimodelkan dengan **siklus Otto**: kompresi adiabatik, pembakaran cepat pada volume tetap, ekspansi adiabatik, dan pembuangan kalor pada volume tetap. Untuk siklus ini, efisiensinya hanya bergantung pada perbandingan kompresi $r = V_\text{maks}/V_\text{min}$:
$$
\eta_\text{Otto} = 1 - r^{1 - \gamma} .
$$
Hitung efisiensi ideal untuk $r = 8$ dan $r = 10$ dengan $\gamma = 1{,}40$, lalu bandingkan dengan efisiensi mesin mobil nyata, sekitar 25–30%.

**Penyelesaian.** $r = 8$: $\eta = 1 - 8^{-0{,}40} = 0{,}565$. $r = 10$: $\eta = 1 - 10^{-0{,}40} = 0{,}602$.

**Memahami hasil.** Mesin nyata hanya mencapai setengah efisiensi ideal ini, karena gesekan, kebocoran kalor melalui dinding silinder, pembakaran yang tidak seketika, dan gas buang yang masih panas. Rumus ini juga menjelaskan mengapa perbandingan kompresi yang lebih tinggi menaikkan efisiensi; batasnya adalah ketukan mesin (*knocking*), yaitu penyalaan dini campuran bensin dan udara yang terlalu panas karena dimampatkan (bandingkan Contoh 3.11). Bensin dengan angka oktan lebih tinggi tahan terhadap penyalaan dini, sehingga memungkinkan perbandingan kompresi lebih tinggi.
:::

::: {.kuis}
**Kuis cepat 5.2** Kapal yang mengambil kalor dari air laut dan mengubahnya seluruhnya menjadi kerja tidak melanggar hukum pertama. Hukum apa yang dilanggarnya, dan mengapa?
:::
