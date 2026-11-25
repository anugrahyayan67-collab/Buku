## 3.4 Matriks dan representasi

Sejauh ini simetri kita gambarkan dengan kata-kata dan gambar. Untuk menghitung, kita perlu mengubahnya menjadi angka. Caranya adalah melihat apa yang dilakukan setiap operasi terhadap sesuatu yang bisa ditulis sebagai bilangan: koordinat sebuah titik, sebuah vektor, atau sebuah orbital.

### Operasi simetri sebagai matriks

Letakkan molekul air dalam bidang *xz*, dengan sumbu C₂ sepanjang *z*. Ambil sebuah titik sembarang dengan koordinat (*x*, *y*, *z*) dan lihat ke mana setiap operasi membawanya:

* **E** tidak mengubah apa pun: (*x*, *y*, *z*) → (*x*, *y*, *z*).
* **C₂** (putar 180° mengelilingi *z*): *x* dan *y* berganti tanda, *z* tetap: (*x*, *y*, *z*) → (−*x*, −*y*, *z*).
* **σᵥ(*xz*)** (cermin bidang molekul): hanya *y* yang berganti tanda: (*x*, −*y*, *z*).
* **σᵥ′(*yz*)** (cermin tegak lurus bidang molekul): hanya *x* yang berganti tanda: (−*x*, *y*, *z*).

Setiap perubahan ini dapat ditulis sebagai perkalian matriks 3 × 3 dengan vektor kolom koordinat. Untuk C₂, misalnya:

$$\begin{pmatrix} -1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} -x \\ -y \\ z \end{pmatrix}$$

Keempat matriks C₂ᵥ semuanya diagonal:

$$E = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \quad C_2 = \begin{pmatrix} -1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \quad \sigma_v = \begin{pmatrix} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \quad \sigma_v' = \begin{pmatrix} -1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

### Operasi yang berurutan dan sifat grup

Apa yang terjadi bila dua operasi dilakukan berurutan? Lakukan σᵥ(*xz*) lalu C₂ pada titik (*x*, *y*, *z*): cermin membawanya ke (*x*, −*y*, *z*), lalu putaran membawanya ke (−*x*, *y*, *z*). Hasil akhirnya sama dengan satu operasi σᵥ′(*yz*). Kita menuliskannya sebagai C₂σᵥ = σᵥ′ (operasi yang dilakukan lebih dulu ditulis di kanan, seperti dalam perkalian matriks). Mengalikan matriksnya memberi hasil yang sama, dan itulah gunanya matriks: **perkalian operasi menjadi perkalian matriks**.

Bila semua pasangan dikerjakan, kita memperoleh **tabel perkalian** grup C₂ᵥ:

Tabel 3.2 Tabel perkalian C₂ᵥ (operasi kolom dilakukan lebih dulu, lalu operasi baris).

| | E | C₂ | σᵥ | σᵥ′ |
|---|---|---|---|---|
| **E** | E | C₂ | σᵥ | σᵥ′ |
| **C₂** | C₂ | E | σᵥ′ | σᵥ |
| **σᵥ** | σᵥ | σᵥ′ | E | C₂ |
| **σᵥ′** | σᵥ′ | σᵥ | C₂ | E |

Tabel ini memperlihatkan empat sifat yang menjadikan himpunan operasi simetri sebuah **grup** dalam arti matematis:

1. **Tertutup.** Hasil kali dua operasi selalu operasi lain dalam himpunan itu. Tidak pernah muncul operasi "baru".
2. **Ada identitas.** E dikalikan dengan apa pun tidak mengubahnya.
3. **Setiap operasi mempunyai kebalikan.** Di C₂ᵥ setiap operasi adalah kebalikan dirinya sendiri, karena melakukannya dua kali kembali ke E. Di C₃ᵥ, kebalikan C₃ adalah C₃².
4. **Asosiatif.** (AB)C = A(BC), seperti perkalian matriks.

Perhatikan juga bahwa setiap baris dan setiap kolom tabel memuat setiap operasi tepat satu kali, seperti teka-teki sudoku. Sifat ini berlaku untuk tabel perkalian grup mana pun.

### Representasi dan karakter

Himpunan matriks yang mengalikan dirinya mengikuti tabel perkalian grup disebut **representasi** grup itu. Keempat matriks di atas adalah representasi C₂ᵥ dengan **basis** (*x*, *y*, *z*). Matriks itu berukuran 3 × 3, sehingga representasinya berdimensi 3.

Menulis matriks lengkap untuk setiap operasi cepat sekali menjadi merepotkan. Untungnya, untuk hampir semua keperluan kimia kita cukup memakai satu bilangan dari setiap matriks: **karakter**-nya, yaitu jumlah unsur diagonal (*trace*), diberi lambang χ (chi).

::: {.inti}
**Karakter** sebuah operasi R dalam suatu representasi adalah jumlah unsur diagonal matriksnya:

$$\chi(R) = \sum_i M_{ii}(R) \qquad \text{(3.1)}$$

Karakter tidak bergantung pada pilihan sumbu koordinat, dan operasi-operasi yang "sejenis" (satu kelas, lihat di bawah) selalu mempunyai karakter yang sama.
:::

Untuk basis (*x*, *y*, *z*) pada C₂ᵥ, karakternya: χ(E) = 3, χ(C₂) = −1, χ(σᵥ) = 1, χ(σᵥ′) = 1.

### Memecah representasi: tereduksi dan tak tereduksi

Matriks C₂ᵥ di atas istimewa: semuanya diagonal. Artinya *x* tidak pernah bercampur dengan *y* atau *z*; setiap operasi hanya mengalikan *x* dengan +1 atau −1. Jadi representasi tiga dimensi itu sebenarnya tersusun dari tiga representasi satu dimensi yang berjalan sendiri-sendiri:

| Basis | E | C₂ | σᵥ(*xz*) | σᵥ′(*yz*) |
|---|---|---|---|---|
| *x* | 1 | −1 | 1 | −1 |
| *y* | 1 | −1 | −1 | 1 |
| *z* | 1 | 1 | 1 | 1 |
| jumlah | 3 | −1 | 1 | 1 |

Representasi yang dapat dipecah menjadi bagian-bagian yang lebih kecil disebut **tereduksi**. Bagian terkecil yang tidak dapat dipecah lagi disebut **representasi tak tereduksi** (disingkat *irep*). Karakter representasi tereduksi selalu sama dengan jumlah karakter irep penyusunnya, seperti terlihat pada baris "jumlah" di atas.

Sekarang lakukan hal yang sama untuk amonia (grup C₃ᵥ), dengan sumbu C₃ sepanjang *z*. Putaran 120° mengelilingi *z* tidak lagi hanya mengubah tanda *x* atau *y*. Ia **mencampur** keduanya:

$$C_3 = \begin{pmatrix} \cos 120° & -\sin 120° & 0 \\ \sin 120° & \cos 120° & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} -\tfrac12 & -\tfrac{\sqrt3}{2} & 0 \\ \tfrac{\sqrt3}{2} & -\tfrac12 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

Koordinat *z* tetap terpisah (kotak kanan bawah), tetapi *x* dan *y* terkunci bersama dalam blok 2 × 2. Tidak ada cara memilih sumbu sehingga blok itu menjadi diagonal untuk semua operasi C₃ᵥ sekaligus. Akibatnya, dalam C₃ᵥ, pasangan (*x*, *y*) membentuk **satu irep berdimensi dua**, dengan karakter χ(E) = 2, χ(C₃) = −½ − ½ = −1, dan χ(σᵥ) = 0.

Inilah asal-usul **degenerasi** dalam kimia. Dua fungsi yang bersama-sama membentuk irep berdimensi dua akan selalu mempunyai energi yang sama, karena simetri molekul mengubah yang satu menjadi campuran keduanya. Orbital 2p~*x*~ dan 2p~*y*~ nitrogen dalam NH₃ setara energinya bukan karena kebetulan, melainkan karena simetri C₃ memaksanya.

::: {.dalam}
**Kelas.** Dalam C₃ᵥ, putaran C₃ dan C₃² selalu mempunyai karakter yang sama, demikian pula ketiga cermin σᵥ. Operasi-operasi yang demikian membentuk satu **kelas**. Secara matematis, A dan B sekelas bila ada operasi X dalam grup sehingga B = X⁻¹AX. Secara fisis: A dan B adalah "operasi yang sama, dilihat dari sudut pandang yang diputar". Ketiga σᵥ amonia sekelas karena C₃ membawa satu bidang cermin ke bidang cermin yang lain. Dalam tabel karakter, operasi sekelas dikumpulkan dalam satu kolom, misalnya "2C₃" dan "3σᵥ".
:::

::: {.kuis}
**Kuis cepat 3.4** Dengan tabel perkalian C₂ᵥ, tentukan hasil σᵥ′σᵥC₂. Lalu tuliskan matriks operasi *i* (inversi) untuk basis (*x*, *y*, *z*) dan hitung karakternya.
:::

## 3.5 Tabel karakter

Untuk setiap grup titik, irep-irepnya beserta karakternya telah disusun sekali untuk selamanya dalam sebuah **tabel karakter**. Kita tidak perlu menurunkannya sendiri; kita perlu dapat **membacanya**. Lampiran B memuat tabel karakter grup-grup yang paling sering dipakai dalam kimia anorganik.

Tabel 3.3 Tabel karakter C₂ᵥ.

| C₂ᵥ | E | C₂ | σᵥ(*xz*) | σᵥ′(*yz*) | linear, rotasi | kuadrat |
|---|---|---|---|---|---|---|
| A₁ | 1 | 1 | 1 | 1 | *z* | *x*², *y*², *z*² |
| A₂ | 1 | 1 | −1 | −1 | *R*~*z*~ | *xy* |
| B₁ | 1 | −1 | 1 | −1 | *x*, *R*~*y*~ | *xz* |
| B₂ | 1 | −1 | −1 | 1 | *y*, *R*~*x*~ | *yz* |

Tabel 3.4 Tabel karakter C₃ᵥ.

| C₃ᵥ | E | 2C₃ | 3σᵥ | linear, rotasi | kuadrat |
|---|---|---|---|---|---|
| A₁ | 1 | 1 | 1 | *z* | *x*² + *y*², *z*² |
| A₂ | 1 | 1 | −1 | *R*~*z*~ | |
| E | 2 | −1 | 0 | (*x*, *y*), (*R*~*x*~, *R*~*y*~) | (*x*² − *y*², *xy*), (*xz*, *yz*) |

### Cara membaca tabel karakter

**Pojok kiri atas** memuat nama grup. **Baris atas** memuat kelas-kelas operasi, dengan jumlah operasi dalam setiap kelas ("2C₃" berarti dua operasi, C₃ dan C₃²). Jumlah semua operasi adalah orde grup *h*: untuk C₃ᵥ, *h* = 1 + 2 + 3 = 6.

**Kolom pertama** memuat label irep, disebut **lambang Mulliken**:

* **A** atau **B**: irep berdimensi satu. A bila simetris terhadap sumbu utama (karakter Cₙ = +1), B bila antisimetris (−1).
* **E**: berdimensi dua. **T**: berdimensi tiga. (Jangan tertukar antara irep E dan operasi identitas E; konteksnya selalu jelas.)
* Indeks **1** dan **2**: simetris atau antisimetris terhadap C₂ yang tegak lurus sumbu utama, atau, bila tidak ada, terhadap σᵥ.
* Indeks **g** dan **u** (dari bahasa Jerman *gerade*, genap, dan *ungerade*, ganjil): simetris atau antisimetris terhadap inversi *i*. Hanya muncul pada grup yang mempunyai pusat inversi.
* Tanda **′** dan **″**: simetris atau antisimetris terhadap σₕ.

Irep pertama, yang karakternya semua +1, disebut **irep simetris total**. Fungsi yang termasuk irep ini tidak berubah oleh operasi apa pun.

**Kolom karakter** dibaca seperti ini: untuk irep berdimensi satu, karakter +1 berarti fungsinya tidak berubah oleh operasi itu, dan −1 berarti fungsinya berganti tanda. Untuk irep berdimensi lebih tinggi, karakter adalah jumlah diagonal matriks yang mencampur fungsi-fungsinya.

**Dua kolom kanan** memuat **fungsi basis**: fungsi sederhana yang berperilaku seperti irep di barisnya. Kolom "linear" memuat *x*, *y*, *z* (juga arah translasi dan arah momen dipol) dan rotasi *R*~*x*~, *R*~*y*~, *R*~*z*~. Kolom "kuadrat" memuat hasil kali dua koordinat. Kolom-kolom inilah yang paling sering dipakai: dari sana kita langsung tahu simetri orbital p (sama dengan *x*, *y*, *z*), orbital d (sama dengan *xy*, *xz*, *yz*, *x*² − *y*², *z*²), serta mode getaran yang aktif IR dan Raman (subbab 3.7).

::: {.contoh}
**Contoh 3.5 · Membaca tabel karakter C₂ᵥ**

Molekul H₂O terletak dalam bidang *xz*. Tentukan irep untuk (a) orbital 2p~*x*~, 2p~*y*~, 2p~*z*~, dan 2s oksigen; (b) orbital 3d~*xy*~ sebuah atom logam pada posisi O; (c) rotasi molekul mengelilingi sumbu *z*.

**Penyelesaian.** (a) Orbital p berperilaku seperti koordinatnya. Dari kolom linear: 2p~*x*~ → **B₁**, 2p~*y*~ → **B₂**, 2p~*z*~ → **A₁**. Orbital s berbentuk bola dan tidak berubah oleh operasi apa pun: **A₁**.

Mari periksa satu dengan tangan. 2p~*y*~ mempunyai cuping + di *y* positif dan cuping − di *y* negatif. C₂ membalik *y*, sehingga cuping bertukar tanda: karakter −1. σᵥ(*xz*) juga membalik *y*: −1. σᵥ′(*yz*) memuat sumbu *y*, sehingga orbital tidak berubah: +1. Karakter (1, −1, −1, 1) cocok dengan B₂.

(b) Dari kolom kuadrat, *xy* → **A₂**.

(c) *R*~*z*~ → **A₂**.

**Memahami hasil.** Oksigen dalam H₂O mempunyai dua orbital A₁ (2s dan 2p~*z*~), satu B₁ (2p~*x*~), dan satu B₂ (2p~*y*~). Di subbab 3.8 kita akan melihat bahwa kedua orbital 1s hidrogen membentuk kombinasi A₁ dan B₁ saja. Akibatnya 2p~*y*~ (B₂), yang tegak lurus bidang molekul, tidak mempunyai pasangan dan menjadi orbital tak berikatan. Satu baris tabel karakter sudah meramalkan sebuah fakta yang terukur dalam spektrum fotoelektron air (Bab 4).
:::

### Sifat-sifat tabel karakter

Tabel karakter mematuhi beberapa aturan yang dapat dipakai untuk memeriksa tabel atau melengkapi yang belum lengkap:

1. **Jumlah irep sama dengan jumlah kelas.** C₂ᵥ: 4 kelas, 4 irep. C₃ᵥ: 3 kelas, 3 irep. Tabel karakter selalu persegi.
2. **Jumlah kuadrat dimensi irep sama dengan orde grup:**

$$\sum_i d_i^2 = h \qquad \text{(3.2)}$$

   Untuk C₃ᵥ: 1² + 1² + 2² = 6 = *h*. Untuk T~d~: 1² + 1² + 2² + 3² + 3² = 24.
3. **Baris-baris saling ortogonal.** Bila karakter dua irep yang berbeda dikalikan untuk setiap operasi lalu dijumlahkan (dengan memperhitungkan jumlah operasi dalam setiap kelas), hasilnya nol. Bila sebuah baris dikalikan dengan dirinya sendiri, hasilnya *h*.

::: {.contoh}
**Contoh 3.6 · Memeriksa ortogonalitas**

Periksa aturan 3 untuk irep A₁ dan E, dan untuk E dengan dirinya sendiri, dalam C₃ᵥ.

**Penyelesaian.** Setiap kelas disumbang (jumlah operasi) × χ₁ × χ₂.

A₁ dengan E: 1(1)(2) + 2(1)(−1) + 3(1)(0) = 2 − 2 + 0 = **0**. Ortogonal.

E dengan E: 1(2)(2) + 2(−1)(−1) + 3(0)(0) = 4 + 2 + 0 = **6** = *h*.

**Memahami hasil.** Irep-irep sebuah grup berperilaku seperti sumbu-sumbu yang saling tegak lurus dalam ruang berdimensi *h*. Sifat inilah yang membuat rumus reduksi di subbab berikutnya bekerja: untuk mengetahui "seberapa banyak" sebuah irep terkandung dalam representasi tereduksi, kita cukup memproyeksikannya ke irep itu, seperti mencari komponen *x* sebuah vektor dengan perkalian titik.
:::

::: {.kuis}
**Kuis cepat 3.5** Dalam O~h~, kelima orbital d terbagi menjadi dua kelompok. Dengan tabel O~h~ di Lampiran B, tentukan irep masing-masing kelompok dan berapa orbital di setiap kelompok.
:::

## 3.6 Representasi tereduksi dan rumus reduksi

Kebanyakan sifat molekul yang menarik, misalnya gerak semua atom atau himpunan orbital semua ligan, menghasilkan representasi **tereduksi** yang besar. Tugas kita adalah menguraikannya menjadi irep-irep. Untuk basis (*x*, *y*, *z*) pada C₂ᵥ kita dapat melakukannya dengan melihat, tetapi untuk 12 koordinat atom amonia atau 21 koordinat SF₆, kita memerlukan rumus.

::: {.inti}
**Rumus reduksi.** Banyaknya irep *i* dalam representasi tereduksi Γ adalah

$$n_i = \frac{1}{h}\sum_{\text{kelas}} N \,\chi_\Gamma(R)\,\chi_i(R) \qquad \text{(3.3)}$$

dengan *h* orde grup, *N* jumlah operasi dalam kelas, χ~Γ~ karakter representasi tereduksi, dan χ~*i*~ karakter irep *i* (dari tabel).
:::

Rumus ini langsung mengikuti dari ortogonalitas di subbab 3.5: perkalian dengan baris irep *i* "menyaring" hanya bagian Γ yang berasal dari irep itu, dan pembagian dengan *h* menormalkannya. Hasilnya harus selalu bilangan bulat tak negatif; pecahan berarti ada kesalahan hitung, biasanya pada karakter Γ.

### Menghitung karakter tanpa menulis matriks

Untuk gerak atom-atom sebuah molekul, setiap atom membawa tiga koordinat (*x*, *y*, *z*), sehingga molekul dengan *N* atom mempunyai representasi berdimensi 3*N*, disebut Γ₃N. Matriksnya besar, tetapi karakternya mudah dihitung dengan dua pengamatan:

1. **Atom yang berpindah tempat tidak menyumbang apa pun pada karakter.** Bila operasi memindahkan atom A ke posisi atom B, koordinat A berpindah ke baris B dalam matriks, sehingga unsur diagonalnya nol.
2. **Atom yang tidak berpindah menyumbang karakter matriks 3 × 3 untuk operasi itu**, yang sama untuk semua atom dan dapat dihitung sekali: E menyumbang 3, Cₙ menyumbang 1 + 2 cos(360°/*n*), σ menyumbang 1, *i* menyumbang −3, dan Sₙ menyumbang −1 + 2 cos(360°/*n*).

Tabel 3.5 Sumbangan karakter per atom yang tidak berpindah.

| Operasi | E | C₂ | C₃ | C₄ | C₆ | σ | *i* | S₃ | S₄ | S₆ |
|---|---|---|---|---|---|---|---|---|---|---|
| sumbangan | 3 | −1 | 0 | 1 | 2 | 1 | −3 | −2 | −1 | 0 |

::: {.strategi}
**Langkah menguraikan Γ₃N**

1. Tentukan grup titik dan ambil tabel karakternya.
2. Untuk setiap kelas, hitung jumlah atom yang **tidak berpindah**.
3. Kalikan dengan sumbangan per atom (Tabel 3.5): hasilnya χ(Γ₃N).
4. Pakai rumus reduksi untuk setiap irep.
5. Periksa: jumlah dimensi semua irep yang diperoleh harus 3*N*.
:::

::: {.contoh}
**Contoh 3.7 · Γ₃N air dan amonia**

Uraikan Γ₃N untuk (a) H₂O (C₂ᵥ) dan (b) NH₃ (C₃ᵥ).

**Penyelesaian.** (a) Atom yang tidak berpindah: E, 3 atom; C₂, hanya O (1); σᵥ(*xz*), bidang molekul, ketiganya (3); σᵥ′(*yz*), hanya O (1). Dikalikan sumbangan (3, −1, 1, 1):

| C₂ᵥ | E | C₂ | σᵥ(*xz*) | σᵥ′(*yz*) |
|---|---|---|---|---|
| atom tetap | 3 | 1 | 3 | 1 |
| χ(Γ₃N) | 9 | −1 | 3 | 1 |

Rumus reduksi dengan *h* = 4:

* *n*(A₁) = ¼[9(1) + (−1)(1) + 3(1) + 1(1)] = ¼(12) = 3
* *n*(A₂) = ¼[9 − 1 − 3 − 1] = ¼(4) = 1
* *n*(B₁) = ¼[9 + 1 + 3 − 1] = ¼(12) = 3
* *n*(B₂) = ¼[9 + 1 − 3 + 1] = ¼(8) = 2

Γ₃N = 3A₁ + A₂ + 3B₁ + 2B₂. Pemeriksaan: 3 + 1 + 3 + 2 = 9 = 3 × 3. ✓

(b) Amonia: E, 4 atom; C₃, hanya N (1); σᵥ, N dan satu H yang terletak di bidang itu (2). Dikalikan sumbangan (3, 0, 1): χ(Γ₃N) = (12, 0, 2). Dengan *h* = 6:

* *n*(A₁) = ⅙[1(12)(1) + 2(0)(1) + 3(2)(1)] = ⅙(18) = 3
* *n*(A₂) = ⅙[12 + 0 − 6] = ⅙(6) = 1
* *n*(E) = ⅙[1(12)(2) + 2(0)(−1) + 3(2)(0)] = ⅙(24) = 4

Γ₃N = 3A₁ + A₂ + 4E. Pemeriksaan: 3 + 1 + 4 × 2 = 12 = 3 × 4. ✓

**Memahami hasil.** Kedua hasil ini memuat **semua** gerak atom: translasi molekul utuh, rotasi molekul utuh, dan getaran. Di subbab berikutnya kita memisahkan getaran dari yang lain, lalu memakai kolom fungsi basis untuk meramalkan spektrum.
:::

::: {.awas}
**Awas: lupa mengalikan dengan jumlah operasi dalam kelas.** Dalam C₃ᵥ, kelas 3σᵥ memuat tiga operasi. Bila faktor 3 dilupakan, *n*(A₁) untuk amonia menjadi ⅙(12 + 0 + 2) = 7/3, bukan bilangan bulat. Hasil pecahan adalah tanda pasti ada kesalahan. Biasakan menulis kolom *N* di atas tabel sebelum mulai menghitung.
:::

::: {.kuis}
**Kuis cepat 3.6** Representasi tereduksi Γ dalam C₃ᵥ mempunyai karakter (3, 0, 1). Uraikan dengan rumus reduksi. Basis apa yang mungkin menghasilkannya?
:::
