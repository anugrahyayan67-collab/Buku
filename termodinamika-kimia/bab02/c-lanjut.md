## 2.7 Persamaan virial dan suhu Boyle

Persamaan van der Waals lahir dari gambaran molekul, tetapi angkanya hanya kasar. Bila kita memerlukan ketelitian tinggi untuk gas pada tekanan rendah sampai sedang, ada cara lain yang lebih jujur: alih-alih menebak bentuk persamaan, kita mengembangkan *Z* sebagai deret pangkat dari konsentrasi, lalu menentukan koefisiennya dari percobaan.

Gagasannya sederhana. Pada konsentrasi nol, gas ideal dan $Z = 1$. Bila konsentrasi bertambah sedikit, penyimpangan pertama yang muncul berasal dari pasangan molekul yang saling berinteraksi; peluang dua molekul bertemu sebanding dengan konsentrasi $1/V_\text{m}$. Penyimpangan berikutnya berasal dari tiga molekul yang bertemu bersamaan, sebanding dengan $1/V_\text{m}^2$, dan seterusnya. Hasilnya adalah **persamaan virial**:

$$
Z = \frac{pV_\text{m}}{RT} = 1 + \frac{B}{V_\text{m}} + \frac{C}{V_\text{m}^2} + \cdots \qquad \text{(2.9)}
$$

*B* disebut **koefisien virial kedua**, *C* koefisien virial ketiga. Keduanya bergantung pada suhu, tetapi tidak pada tekanan. Untuk tekanan yang tidak terlalu tinggi, cukup suku pertama, dan karena $1/V_\text{m} \approx p/RT$, bentuk yang paling praktis adalah

$$
Z \approx 1 + \frac{Bp}{RT} . \qquad \text{(2.10)}
$$

Tanda *B* langsung memberi tahu pengaruh mana yang menang. Bila *B* negatif, tarikan menang dan $Z < 1$; bila positif, tolakan menang. Persamaan van der Waals, bila dikembangkan untuk konsentrasi kecil, memberi gambaran yang jelas tentang tanda itu:

$$
B = b - \frac{a}{RT} . \qquad \text{(2.11)}
$$

Pada suhu rendah, suku tarikan $a/RT$ besar dan *B* negatif. Pada suhu tinggi, molekul bergerak begitu cepat sehingga tarikan tidak sempat berpengaruh, suku itu mengecil, dan *B* menjadi positif. Di antara keduanya ada suhu tempat $B = 0$, yang disebut **suhu Boyle** $T_\text{B}$. Pada suhu itu, kedua pengaruh saling menghapus dan gas nyata berperilaku hampir ideal dalam rentang tekanan yang lebar. Menurut van der Waals, $T_\text{B} = a/Rb$.

| Gas | *B* pada 273 K (cm³ mol⁻¹) | $T_\text{B}$ terukur (K) |
|---|---|---|
| He | +11,9 | 22,6 |
| N₂ | −10,5 | 327,2 |
| Ar | −21,7 | 411,5 |
| O₂ | −22,0 | 405,9 |
| CO₂ | −149,7 | 714,8 |

Tabel 2.3 Koefisien virial kedua dan suhu Boyle.

::: {.contoh}
**Contoh 2.8 · Koreksi virial untuk CO₂**

Untuk CO₂ pada 273 K, $B = -149{,}7$ cm³ mol⁻¹. Hitung *Z* pada 1,00 bar dan 10,0 bar, lalu persentase kesalahan bila volumenya dihitung dengan persamaan gas ideal.

**Penyelesaian.** Dengan $B = -0{,}1497$ L mol⁻¹ dan $RT = (0{,}083\,14)(273{,}15) = 22{,}71$ L bar mol⁻¹:
$$
Z(1\ \text{bar}) = 1 + \frac{(-0{,}1497)(1{,}00)}{22{,}71} = 0{,}9934 , \qquad Z(10\ \text{bar}) = 1 - \frac{(0{,}1497)(10{,}0)}{22{,}71} = 0{,}934 .
$$
Persamaan gas ideal memberi volume 0,7% terlalu besar pada 1 bar dan 7% terlalu besar pada 10 bar.

**Memahami hasil.** Bahkan pada tekanan atmosfer, CO₂ menyimpang hampir satu persen dari gas ideal, cukup besar untuk mengganggu penentuan massa molar yang teliti (Contoh 1.6). Untuk N₂ ($B = -10{,}5$ cm³ mol⁻¹), penyimpangan yang sama hanya 0,05%. Perbedaan ini mencerminkan kekuatan tarikan: *a* CO₂ hampir tiga kali *a* N₂.
:::

::: {.contoh}
**Contoh 2.9 · Suhu Boyle menurut van der Waals**

Hitung suhu Boyle N₂ dan He dari tetapan van der Waals, lalu bandingkan dengan Tabel 2.3.

**Penyelesaian.** N₂: $T_\text{B} = a/Rb = 1{,}370/[(0{,}083\,14)(0{,}0387)] = 426$ K. He: $0{,}0346/[(0{,}083\,14)(0{,}0238)] = 17{,}5$ K.

**Memahami hasil.** Untuk kedua gas, van der Waals meramalkan orde besaran yang benar, tetapi meleset sekitar 25–30% (327 K dan 22,6 K terukur). Kesimpulan kualitatifnya tetap benar: nitrogen pada suhu kamar berada sedikit di bawah suhu Boylenya, sehingga *Z*-nya sangat dekat dengan 1; helium pada suhu kamar jauh di atas suhu Boylenya, sehingga *Z*-nya selalu sedikit di atas 1.
:::

::: {.kuis}
**Kuis cepat 2.7** Pada 600 K, koefisien virial kedua CO₂ menjadi jauh lebih kecil nilai mutlaknya daripada pada 273 K. Mengapa?
:::

## 2.8 Persamaan keadaan lain

Persamaan van der Waals mudah dipahami, tetapi kita sudah melihat kelemahannya: volume kritisnya meleset jauh, dan massa jenis cairannya kurang tepat. Sejak 1873, ratusan persamaan keadaan lain telah diusulkan. Dua di antaranya dipakai sangat luas dalam teknik kimia, dan keduanya dapat dipandang sebagai van der Waals yang "disetel ulang".

**Persamaan Redlich–Kwong (1949)** mempertahankan koreksi ukuran, tetapi membuat suku tarikan melemah dengan suhu:

$$
p = \frac{RT}{V_\text{m} - b} - \frac{a}{\sqrt T\,V_\text{m}(V_\text{m} + b)} , \qquad a = 0{,}427\,48\frac{R^2T_\text{c}^{5/2}}{p_\text{c}} , \quad b = 0{,}086\,64\frac{RT_\text{c}}{p_\text{c}} . \qquad \text{(2.12)}
$$

Faktor $1/\sqrt T$ mencerminkan kenyataan bahwa pada suhu tinggi molekul-molekul bertemu terlalu singkat untuk merasakan tarikan penuh.

**Persamaan Peng–Robinson (1976)** menambahkan satu parameter lagi, **faktor asentrik** ω, yang mengukur seberapa jauh molekul menyimpang dari bentuk bulat. Persamaan ini memberi massa jenis cairan dan tekanan uap yang cukup teliti untuk kebanyakan hidrokarbon, dan menjadi persamaan bawaan dalam perangkat lunak simulasi pabrik kimia.

Ketiga persamaan ini berbentuk pangkat tiga dalam $V_\text{m}$, sehingga semuanya dapat diselesaikan dengan cara yang sama seperti Contoh 2.4. Yang membedakannya hanyalah ketelitian.

::: {.contoh}
**Contoh 2.10 · Membandingkan tiga persamaan**

Hitung tekanan satu mol CO₂ dalam 0,500 L pada 300 K menurut persamaan gas ideal, van der Waals, dan Redlich–Kwong ($T_\text{c} = 304{,}1$ K, $p_\text{c} = 73{,}8$ bar).

**Penyelesaian.** Gas ideal: 49,9 bar. Van der Waals: 40,0 bar (Contoh 2.3). Untuk Redlich–Kwong, tetapannya:
$$
a = 0{,}427\,48\frac{(0{,}083\,14)^2(304{,}1)^{2{,}5}}{73{,}8} = 64{,}6\ \text{L}^2\,\text{bar K}^{1/2}\,\text{mol}^{-2} , \qquad b = 0{,}086\,64\frac{(0{,}083\,14)(304{,}1)}{73{,}8} = 0{,}0297\ \text{L mol}^{-1} .
$$
Maka
$$
p = \frac{(0{,}083\,14)(300)}{0{,}500 - 0{,}0297} - \frac{64{,}6}{\sqrt{300}\,(0{,}500)(0{,}5297)} = 53{,}0 - 14{,}1 = 39{,}0\ \text{bar} .
$$

**Memahami hasil.** Kedua persamaan gas nyata sepakat dalam rentang 3%, sementara persamaan gas ideal meleset sekitar 25%. Pada kondisi yang jauh dari titik kritis dan dari daerah cairan, pilihan persamaan gas nyata tidak terlalu penting; yang penting adalah tidak memakai persamaan gas ideal.
:::

::: {.kuis}
**Kuis cepat 2.8** Mengapa persamaan keadaan teknik seperti Peng–Robinson memerlukan lebih banyak data zat (misalnya faktor asentrik) daripada persamaan van der Waals?
:::

## 2.9 Efek Joule–Thomson dan pencairan gas

Teka-teki pembuka masih menyisakan satu pertanyaan: mengapa mulut tabung pemadam CO₂ diselimuti es ketika disemprotkan? Jawabannya terletak pada apa yang terjadi ketika gas nyata memuai.

Pada 1852, James Joule dan William Thomson (kelak Lord Kelvin) mengalirkan gas melalui sumbat berpori dari daerah bertekanan tinggi ke daerah bertekanan rendah, di dalam pipa yang terisolasi sehingga tidak ada kalor yang masuk atau keluar. Mereka menemukan bahwa kebanyakan gas **mendingin** setelah melewati sumbat itu. Perubahan suhu per satuan penurunan tekanan disebut **koefisien Joule–Thomson**:

$$
\mu_\text{JT} = \left(\frac{\partial T}{\partial p}\right)_H . \qquad \text{(2.13)}
$$

Indeks *H* berarti prosesnya terjadi pada entalpi tetap; arti entalpi akan kita bahas di Bab 4. Bila $\mu_\text{JT} > 0$, penurunan tekanan menurunkan suhu: gas mendingin.

Mengapa gas mendingin? Lihat kembali potensial Lennard-Jones. Pada tekanan tinggi, molekul-molekul rata-rata cukup dekat untuk berada di dalam sumur tarikan. Ketika gas memuai, jarak rata-rata antarmolekul bertambah, dan molekul harus "memanjat keluar" dari sumur itu. Energi untuk memanjat diambil dari energi kinetik molekul sendiri, karena tidak ada kalor yang masuk dari luar. Energi kinetik rata-rata yang berkurang berarti suhu yang turun. Untuk gas ideal, yang tidak mempunyai tarikan, $\mu_\text{JT} = 0$.

Tetapi tarikan bukan satu-satunya pengaruh. Pada suhu tinggi, molekul bergerak begitu cepat sehingga tumbukan keras (daerah tolakan) lebih berperan daripada tarikan, dan pemuaian justru melepaskan energi: gas **memanas**. Suhu tempat $\mu_\text{JT}$ berganti tanda disebut **suhu inversi**. Untuk kebanyakan gas, suhu inversinya jauh di atas suhu kamar, sehingga mereka mendingin bila memuai. Untuk helium (40 K) dan hidrogen (sekitar 200 K), suhu inversinya di bawah suhu kamar, sehingga keduanya **memanas** ketika memuai pada suhu kamar. Persamaan van der Waals memberi taksiran sederhana:

$$
\mu_\text{JT} \approx \frac{1}{C_{p,\text{m}}}\left(\frac{2a}{RT} - b\right) , \qquad T_\text{inv} \approx \frac{2a}{Rb} = 2T_\text{B} , \qquad \text{(2.14)}
$$

dengan $C_{p,\text{m}}$ kapasitas kalor molar pada tekanan tetap. Lagi-lagi tampak persaingan antara tarikan (*a*) dan ukuran (*b*).

| Gas | $\mu_\text{JT}$ pada 298 K (K atm⁻¹) | Suhu inversi atas (K) |
|---|---|---|
| He | −0,062 | 40 |
| N₂ | +0,27 | 621 |
| Ar | +0,42 | 723 |
| CO₂ | +1,11 | 1500 |

Tabel 2.4 Koefisien Joule–Thomson pada 1 atm dan suhu inversi.

::: {.contoh}
**Contoh 2.11 · Pendinginan nitrogen dan pemanasan helium**

(a) Taksir koefisien Joule–Thomson N₂ pada 298 K dari (2.14), dengan $C_{p,\text{m}} = 29{,}1$ J K⁻¹ mol⁻¹. (b) Gas N₂ dan He masing-masing dialirkan melalui katup dari 200 atm ke 1 atm pada suhu awal 298 K. Taksir perubahan suhunya dengan nilai $\mu_\text{JT}$ Tabel 2.4.

**Penyelesaian.** (a) Dalam satuan SI, $a = 0{,}1370$ Pa m⁶ mol⁻² dan $b = 3{,}87 \times 10^{-5}$ m³ mol⁻¹:
$$
\mu_\text{JT} \approx \frac{1}{29{,}1}\left(\frac{2(0{,}1370)}{(8{,}314)(298{,}15)} - 3{,}87 \times 10^{-5}\right) = 2{,}47 \times 10^{-6}\ \text{K Pa}^{-1} = 0{,}25\ \text{K atm}^{-1} ,
$$
dekat dengan nilai terukur 0,27 K atm⁻¹.

(b) N₂: $\Delta T \approx \mu_\text{JT}\Delta p = (0{,}27)(-199) \approx -54$ K. He: $\Delta T \approx (-0{,}062)(-199) \approx +12$ K.

**Memahami hasil.** Taksiran (b) kasar karena $\mu_\text{JT}$ berubah dengan tekanan dan suhu selama pemuaian, tetapi tandanya pasti benar: nitrogen mendingin puluhan derajat, helium memanas. Satu kali pemuaian belum cukup untuk mencairkan nitrogen (titik didihnya 77 K). Pada **proses Linde**, gas yang telah didinginkan oleh pemuaian dipakai untuk mendinginkan gas yang baru masuk sebelum memuai, sehingga suhunya turun makin rendah pada setiap putaran sampai akhirnya gas mencair. Helium harus didinginkan lebih dulu di bawah 40 K dengan cara lain sebelum proses ini dapat bekerja.
:::

**Kembali ke tabung pemadam.** Kini bunga es di mulut tabung CO₂ dapat dijelaskan. CO₂ cair menyembur keluar dan sebagian langsung menguap. Penguapan itu sendiri menyerap kalor dalam jumlah besar, dan gas yang memuai dari sekitar 64 bar ke 1 bar mendingin lebih jauh karena efek Joule–Thomson ($\mu_\text{JT}$ CO₂ termasuk yang terbesar). Suhunya turun sampai di bawah −78 °C, sehingga sebagian CO₂ membeku menjadi "salju" es kering, dan uap air dari udara membeku di mulut tabung.

::: {.kuis}
**Kuis cepat 2.9** Mengapa tabung hidrogen yang bocor dengan cepat pada suhu kamar dapat menimbulkan bahaya kebakaran tambahan karena efek Joule–Thomson?
:::

## 2.10 Fluida superkritis

Apa yang terjadi bila suatu zat dipanaskan dan ditekan sekaligus sampai melewati suhu dan tekanan kritisnya? Ia tidak lagi dapat disebut gas, karena massa jenisnya dapat setinggi cairan, tetapi juga tidak dapat disebut cairan, karena ia mengisi seluruh wadah dan tidak mempunyai permukaan. Zat dalam keadaan ini disebut **fluida superkritis**.

Keistimewaan fluida superkritis datang dari dekat titik kritis, tempat isoterm hampir mendatar (Gambar 2.3). Di daerah itu, perubahan tekanan yang kecil mengubah volume molar, dan karena itu massa jenis, dengan sangat besar. Dengan memutar katup tekanan, kimiawan dapat "menyetel" massa jenis fluida dari mirip gas sampai mirip cairan. Kemampuan melarutkan zat bergantung pada massa jenis, sehingga daya pelarut fluida superkritis juga dapat disetel.

Fluida superkritis yang paling banyak dipakai adalah CO₂, karena titik kritisnya mudah dicapai (31 °C, 74 bar), murah, tidak beracun, dan tidak meninggalkan sisa: setelah tekanan diturunkan, CO₂ langsung menjadi gas dan pergi. Pemakaiannya antara lain:

* **Dekafeinasi kopi.** Biji kopi basah dilewati CO₂ superkritis, yang melarutkan kafein tetapi menyisakan sebagian besar senyawa aroma.
* **Ekstraksi bahan alam**: minyak atsiri, ekstrak hop untuk bir, dan senyawa obat dari tumbuhan, tanpa pelarut organik beracun.
* **Kromatografi fluida superkritis** dan **pencucian kering** tanpa pelarut terklorinasi.

Karena menggantikan pelarut organik yang mencemari, CO₂ superkritis menjadi salah satu contoh utama **kimia hijau**.

::: {.contoh}
**Contoh 2.12 · Massa jenis CO₂ superkritis**

CO₂ superkritis untuk ekstraksi sering dipakai pada 40 °C dan 100 bar. Hitung massa jenisnya menurut persamaan gas ideal dan persamaan van der Waals, lalu bandingkan dengan nilai terukur, sekitar 630 g L⁻¹.

**Penyelesaian.** Gas ideal: $\rho = pM/RT = (100)(44{,}01)/[(0{,}083\,14)(313{,}15)] = 169$ g L⁻¹. Van der Waals: akar tunggal persamaan pangkat tiga (kode Contoh 2.4) adalah $V_\text{m} = 0{,}0905$ L mol⁻¹, sehingga $\rho = 44{,}01/0{,}0905 = 487$ g L⁻¹.

**Memahami hasil.** Persamaan gas ideal meleset hampir empat kali lipat; massa jenis sebenarnya sekitar dua pertiga massa jenis air, jauh lebih mirip cairan daripada gas. Persamaan van der Waals menangkap perubahan besar itu, tetapi masih meleset 23%, karena kondisi ini dekat dengan titik kritis, daerah tempat persamaan itu paling lemah. Untuk merancang proses ekstraksi, insinyur memakai persamaan Peng–Robinson atau tabel data terukur.
:::

::: {.kuis}
**Kuis cepat 2.10** Mengapa air superkritis (di atas 374 °C dan 221 bar) dapat melarutkan minyak, padahal air biasa tidak? Petunjuk: pikirkan apa yang terjadi pada ikatan hidrogen dan massa jenisnya.
:::

### Menuju bab berikutnya

Sampai di sini kita telah mempelajari **keadaan** gas: hubungan antara *p*, *V*, *T*, dan *n*, baik untuk gas ideal maupun gas nyata. Termodinamika yang sesungguhnya dimulai ketika keadaan itu **berubah**. Bila gas memuai mendorong piston, ia melakukan kerja; bila dipanaskan, ia menerima kalor. Di Bab 3 kita akan menghitung kerja dan kalor dengan teliti, dan menemukan hukum pertama termodinamika: energi tidak dapat diciptakan atau dimusnahkan, hanya berpindah dalam bentuk kerja atau kalor.
