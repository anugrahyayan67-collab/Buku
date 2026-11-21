# Bab 12 Kesetimbangan Kimia

Pada awal abad ke-20, dunia menghadapi krisis yang jarang diingat sekarang: pupuk nitrogen hampir habis. Sumber utamanya, endapan sendawa di gurun Chili, diperkirakan hanya cukup untuk beberapa dasawarsa, padahal udara yang kita hirup berisi 78% nitrogen. Masalahnya, molekul N₂ hampir tidak mau bereaksi. Fritz Haber berhasil mereaksikannya dengan hidrogen menjadi amonia, tetapi reaksi itu tidak pernah berjalan tuntas. Pada suhu yang cukup tinggi agar reaksi berlangsung cepat, hanya beberapa persen amonia terbentuk sebelum reaksi seolah-olah berhenti. Pertanyaan yang harus dijawab Haber adalah pertanyaan termodinamika: di titik mana reaksi berhenti, dan bagaimana titik itu dapat digeser?

Jawabannya, yang kini memberi makan hampir separuh umat manusia, ada di bab ini. Setiap reaksi kimia dalam sistem tertutup akhirnya mencapai **kesetimbangan**, keadaan ketika reaksi maju dan reaksi balik berlangsung sama cepat sehingga komposisi tidak berubah lagi. Di Kimia Dasar, kesetimbangan dirumuskan lewat tetapan kesetimbangan *K* dan asas Le Chatelier, yang dihafal sebagai aturan. Di sini kita akan menurunkan keduanya dari potensial kimia. Hasil utamanya adalah salah satu persamaan terpenting dalam kimia:

$$
\Delta_\text{r}G^\circ = -RT\ln K .
$$

Dengan persamaan ini, tabel energi Gibbs pembentukan dari Bab 7 berubah menjadi tabel tetapan kesetimbangan untuk reaksi apa pun. Dan dengan persamaan Gibbs–Helmholtz dari Bab 7, kita akan memperoleh cara meramalkan bagaimana *K* berubah dengan suhu: persamaan van 't Hoff.

::: {.strategi}
**Pertanyaan pembuka**

1. Mengapa reaksi berhenti sebelum pereaksi habis, padahal Δ*G*° negatif?
2. Apa hubungan antara energi Gibbs standar reaksi dan tetapan kesetimbangan?
3. Mengapa tetapan kesetimbangan reaksi yang sama dapat dinyatakan dalam beberapa bentuk (*K*, *K*_c, *K*_x)?
4. Bagaimana tekanan dan gas lembam menggeser kesetimbangan?
5. Mengapa sintesis amonia dilakukan pada 450 °C dan 200–300 bar, padahal hasilnya lebih besar pada suhu rendah?
6. Apakah asas Le Chatelier selalu benar?
7. Bagaimana sel hidup menjalankan reaksi yang Δ*G*°-nya positif?
:::

::: {.tujuan}
**Tujuan belajar**

Setelah mempelajari bab ini, kamu mampu:

1. Mendefinisikan kemajuan reaksi dan energi Gibbs reaksi, serta menjelaskan mengapa *G* mempunyai minimum.
2. Menurunkan $\Delta_\text{r}G = \Delta_\text{r}G^\circ + RT\ln Q$ dan $\Delta_\text{r}G^\circ = -RT\ln K$.
3. Mengubah *K* menjadi *K*_c dan *K*_x, dan menangani kesetimbangan heterogen.
4. Menghitung komposisi kesetimbangan dari *K* dan komposisi awal.
5. Meramalkan pengaruh tekanan dan gas lembam pada komposisi kesetimbangan.
6. Memakai persamaan van 't Hoff untuk menghitung *K* pada suhu lain dan $\Delta_\text{r}H^\circ$ dari data *K*.
7. Menjelaskan asas Le Chatelier secara termodinamika beserta batasnya.
8. Memakai keadaan standar biokimia dan menghitung Δ*G* reaksi dalam sel.
:::

::: {.mat}
**Prasyarat**

Dari Bab 7: $\Delta_\text{r}G^\circ$ dari tabel (Tabel 7.1) dan persamaan Gibbs–Helmholtz (subbab 7.7). Dari Bab 9 dan 10: potensial kimia gas ideal $\mu = \mu^\circ + RT\ln(p/p^\circ)$, zat terlarut $\mu = \mu^\circ + RT\ln a$, dan fugasitas. Dari Kimia Dasar: stoikiometri dan tabel "awal–perubahan–kesetimbangan". Dari matematika: logaritma dan eksponen, serta menyelesaikan persamaan kuadrat.
:::

## 12.1 Energi Gibbs reaksi dan kemajuan reaksi

Ambil reaksi sederhana yang dapat dilihat dengan mata: $\text{N}_2\text{O}_4(g) \rightleftharpoons 2\text{NO}_2(g)$. Dinitrogen tetroksida tidak berwarna; nitrogen dioksida berwarna cokelat. Masukkan N₂O₄ murni ke dalam labu tertutup pada suhu kamar, dan warna cokelat muncul, makin pekat, lalu berhenti pada kepekatan tertentu. Mengapa berhenti di situ?

Untuk menjawabnya, kita perlu satu variabel yang menyatakan sejauh mana reaksi telah berjalan. Untuk reaksi umum $\sum\nu_\text{J}\text{J} = 0$, dengan koefisien stoikiometri $\nu_\text{J}$ positif untuk hasil dan negatif untuk pereaksi, banyaknya setiap zat berubah sesuai stoikiometri: $dn_\text{J} = \nu_\text{J}\,d\xi$. Variabel ξ disebut **kemajuan reaksi**, dengan satuan mol. Untuk N₂O₄ → 2NO₂, bila ξ = 0,3 mol, berarti 0,3 mol N₂O₄ telah bereaksi dan 0,6 mol NO₂ telah terbentuk.

Pada suhu dan tekanan tetap, persamaan fundamental (9.5) memberi perubahan energi Gibbs ketika reaksi maju sebesar *dξ*:
$$
dG = \sum_\text{J}\mu_\text{J}\,dn_\text{J} = \left(\sum_\text{J}\nu_\text{J}\mu_\text{J}\right)d\xi .
$$
Laju perubahan *G* terhadap kemajuan reaksi diberi nama:

::: {.inti}
$$
\Delta_\text{r}G = \left(\frac{\partial G}{\partial\xi}\right)_{T,p} = \sum_\text{J}\nu_\text{J}\mu_\text{J} . \qquad \text{(12.1)}
$$
**Energi Gibbs reaksi**: kemiringan kurva *G* terhadap ξ pada komposisi saat itu. Bila $\Delta_\text{r}G < 0$, reaksi maju spontan; bila $\Delta_\text{r}G > 0$, reaksi balik yang spontan; bila $\Delta_\text{r}G = 0$, sistem dalam kesetimbangan.
:::

Perhatikan bahwa $\Delta_\text{r}G$ di sini **bukan** selisih energi Gibbs antara keadaan awal dan akhir. Ia adalah turunan, yang nilainya berubah ketika komposisi berubah, karena setiap potensial kimia bergantung pada komposisi. Huruf Δ dipertahankan karena, seperti akan kita lihat, ia dapat dihitung sebagai "hasil dikurangi pereaksi" dari potensial kimia.

Mengapa *G* mempunyai minimum? Gambar 12.1 menjawabnya. Bila potensial kimia setiap zat tidak bergantung pada komposisi, *G* akan berubah lurus dari N₂O₄ murni ke NO₂ murni (garis putus-putus), dan reaksi akan berjalan tuntas ke arah ujung yang lebih rendah, atau tidak sama sekali. Tetapi begitu sedikit NO₂ terbentuk, kedua gas **bercampur**, dan pencampuran selalu menurunkan *G* (subbab 9.5). Suku pencampuran ini paling curam di dekat zat murni, sehingga kurva *G* selalu turun dulu, berapa pun posisi kedua ujungnya. Minimum kurva, tempat kemiringan $\Delta_\text{r}G$ nol, adalah kesetimbangan.

![Gambar 12.1 Energi Gibbs campuran N₂O₄–NO₂ terhadap kemajuan reaksi pada 25 °C dan 1 bar, mulai dari 1 mol N₂O₄. Garis putus-putus: tanpa suku pencampuran. Kurva: dengan pencampuran. Walaupun NO₂ murni mempunyai *G* lebih tinggi daripada N₂O₄ murni, kurva mempunyai minimum pada ξ ≈ 0,19 mol, yaitu kesetimbangan.](fig/gxi.png){width=72%}

::: {.contoh}
**Contoh 12.1 · Ke mana reaksi berjalan?**

Pada 25 °C, $\Delta_\text{r}G^\circ = +4{,}73$ kJ mol⁻¹ untuk $\text{N}_2\text{O}_4(g) \rightarrow 2\text{NO}_2(g)$. Suatu campuran berisi N₂O₄ dengan tekanan parsial 0,80 bar dan NO₂ 0,20 bar. Hitung $\Delta_\text{r}G$ dan tentukan arah reaksi.

**Penyelesaian.** Dari (12.1) dengan $\mu_\text{J} = \mu_\text{J}^\circ + RT\ln(p_\text{J}/p^\circ)$:
$$
\Delta_\text{r}G = 2\mu_{\text{NO}_2} - \mu_{\text{N}_2\text{O}_4} = \Delta_\text{r}G^\circ + RT\ln\frac{(p_{\text{NO}_2}/p^\circ)^2}{p_{\text{N}_2\text{O}_4}/p^\circ} = 4{,}73 + (2{,}479)\ln\frac{(0{,}20)^2}{0{,}80} = 4{,}73 - 7{,}43 = -2{,}70\ \text{kJ mol}^{-1} .
$$
Negatif: N₂O₄ masih terurai lebih lanjut.

**Memahami hasil.** Δ*G*° positif tidak berarti reaksi tidak terjadi. Ia hanya berarti reaksi tidak spontan bila **semua** zat berada pada keadaan standarnya (masing-masing 1 bar). Pada campuran yang miskin hasil, suku logaritma negatif dan dapat mengalahkan Δ*G*°. Setiap reaksi berjalan ke arah yang menurunkan *G* dari komposisi tempat ia berada.
:::

::: {.kuis}
**Kuis cepat 12.1** Mengapa kurva *G* pada Gambar 12.1 tidak pernah mempunyai minimum tepat di ξ = 0 atau ξ = 1?
:::

## 12.2 Energi Gibbs standar reaksi dan tetapan kesetimbangan

Contoh 12.1 sudah memperlihatkan polanya. Secara umum, untuk setiap zat $\mu_\text{J} = \mu_\text{J}^\circ + RT\ln a_\text{J}$, dengan $a_\text{J}$ aktivitas (untuk gas ideal $a = p/p^\circ$, untuk zat terlarut encer ideal $a = b/b^\circ$, untuk padatan dan cairan murni $a = 1$). Masukkan ke (12.1):
$$
\Delta_\text{r}G = \sum\nu_\text{J}\mu_\text{J}^\circ + RT\sum\nu_\text{J}\ln a_\text{J} = \Delta_\text{r}G^\circ + RT\ln\prod_\text{J}a_\text{J}^{\nu_\text{J}} .
$$
Hasil kali di ruas kanan disebut **kuosien reaksi** *Q*: aktivitas hasil dipangkatkan koefisiennya, dibagi aktivitas pereaksi dipangkatkan koefisiennya. Maka

::: {.inti}
$$
\Delta_\text{r}G = \Delta_\text{r}G^\circ + RT\ln Q , \qquad Q = \prod_\text{J}a_\text{J}^{\nu_\text{J}} . \qquad \text{(12.2)}
$$
**Energi Gibbs reaksi pada komposisi apa pun.** $\Delta_\text{r}G^\circ$ tetap (bergantung pada suhu saja); seluruh ketergantungan pada komposisi ada di *Q*.
:::

Pada kesetimbangan, $\Delta_\text{r}G = 0$, dan nilai *Q* pada saat itu diberi nama **tetapan kesetimbangan** *K*:

::: {.inti}
$$
\Delta_\text{r}G^\circ = -RT\ln K , \qquad K = \left(\prod_\text{J}a_\text{J}^{\nu_\text{J}}\right)_\text{setimbang} . \qquad \text{(12.3)}
$$
**Hubungan dasar kesetimbangan kimia.** *K* tidak bersatuan, karena setiap aktivitas tidak bersatuan, dan hanya bergantung pada suhu.
:::

Inilah "hukum aksi massa" Kimia Dasar, kini diturunkan, bukan dihafal. Penurunan ini juga menjelaskan dua hal yang di Kimia Dasar hanya disebut aturan. Pertama, padatan dan cairan murni tidak muncul dalam *K*, karena aktivitasnya satu. Kedua, *K* tidak bersatuan, karena setiap tekanan selalu dibagi tekanan standar dan setiap molalitas dibagi molalitas standar.

Persamaan (12.3) juga dapat dibaca sebagai $K = e^{-\Delta_\text{r}G^\circ/RT}$. Hubungan eksponensial ini membuat *K* sangat peka terhadap $\Delta_\text{r}G^\circ$. Pada 25 °C, *RT* = 2,48 kJ mol⁻¹, sehingga setiap 5,7 kJ mol⁻¹ pada $\Delta_\text{r}G^\circ$ mengubah *K* sepuluh kali lipat.

Tabel 12.1 Hubungan $\Delta_\text{r}G^\circ$ dan *K* pada 25 °C.

| $\Delta_\text{r}G^\circ$ (kJ mol⁻¹) | −100 | −50 | −10 | 0 | +10 | +50 | +100 |
|---|---|---|---|---|---|---|---|
| *K* | $3 \times 10^{17}$ | $6 \times 10^8$ | 57 | 1 | 0,018 | $1{,}7 \times 10^{-9}$ | $3 \times 10^{-18}$ |

Reaksi dengan $\Delta_\text{r}G^\circ$ di bawah sekitar −50 kJ mol⁻¹ praktis berjalan tuntas; di atas +50 kJ mol⁻¹, praktis tidak berjalan. Hanya reaksi dengan $|\Delta_\text{r}G^\circ|$ kurang dari beberapa puluh kJ mol⁻¹ yang menghasilkan campuran kesetimbangan dengan pereaksi dan hasil dalam jumlah yang sebanding. Untuk reaksi-reaksi itulah perhitungan kesetimbangan paling penting.

Gambar 12.2 menampilkan hubungan yang sama sebagai garis lurus: log *K* berbanding lurus dengan $-\Delta_\text{r}G^\circ$, dengan kemiringan $1/(RT\ln10)$. Pada suhu yang lebih tinggi garisnya lebih landai, sehingga $\Delta_\text{r}G^\circ$ yang sama menghasilkan *K* yang lebih dekat ke 1: energi termal yang lebih besar membuat selisih energi Gibbs yang sama "kurang menentukan". Perlu diingat bahwa $\Delta_\text{r}G^\circ$ sendiri juga berubah dengan suhu (subbab 12.6); gambar ini hanya memperlihatkan peran *RT* di penyebut.

![Gambar 12.2 Logaritma tetapan kesetimbangan terhadap $\Delta_\text{r}G^\circ$ pada 298,15 K dan 1000 K. Daerah hijau: reaksi praktis tuntas; daerah jingga: praktis tidak berjalan. Hanya reaksi di antara keduanya yang menghasilkan campuran pereaksi dan hasil dalam jumlah sebanding.](fig/logK.png){width=80%}

::: {.contoh}
**Contoh 12.2 · Tiga tetapan dari tabel**

Hitung *K* pada 25 °C untuk (a) $\text{N}_2\text{O}_4(g) \rightleftharpoons 2\text{NO}_2(g)$; (b) $\text{N}_2(g) + 3\text{H}_2(g) \rightleftharpoons 2\text{NH}_3(g)$; (c) $\text{CO}(g) + \text{H}_2\text{O}(g) \rightleftharpoons \text{CO}_2(g) + \text{H}_2(g)$. Pakai Tabel 7.1.

**Penyelesaian.** (a) $\Delta_\text{r}G^\circ = 2(51{,}31) - 97{,}89 = +4{,}73$ kJ mol⁻¹; $K = \exp(-4730/2479) = 0{,}148$.

(b) $\Delta_\text{r}G^\circ = 2(-16{,}45) = -32{,}90$ kJ mol⁻¹; $K = \exp(32\,900/2479) = 5{,}8 \times 10^5$.

(c) $\Delta_\text{r}G^\circ = -394{,}36 - (-137{,}17 - 228{,}57) = -28{,}62$ kJ mol⁻¹; $K = 1{,}0 \times 10^5$.

**Memahami hasil.** Pada suhu kamar, sintesis amonia dan reaksi pergeseran air–gas sangat menguntungkan: kesetimbangannya jauh di sisi hasil. Masalah keduanya di industri adalah **laju**: pada 25 °C keduanya praktis tidak berjalan. Untuk mempercepatnya, suhu dinaikkan, dan seperti akan kita lihat di subbab 12.6, kenaikan suhu justru menurunkan *K* kedua reaksi eksoterm ini. Penguraian N₂O₄, dengan *K* mendekati satu, adalah contoh kesetimbangan yang benar-benar "di tengah".
:::

::: {.contoh}
**Contoh 12.3 · Aturan penggabungan *K***

Dari Contoh 12.2 (b), hitung *K* untuk (a) $\tfrac12\text{N}_2 + \tfrac32\text{H}_2 \rightleftharpoons \text{NH}_3$; (b) $2\text{NH}_3 \rightleftharpoons \text{N}_2 + 3\text{H}_2$.

**Penyelesaian.** (a) $\Delta_\text{r}G^\circ$ separuhnya, sehingga $\ln K$ separuhnya: $K = (5{,}8 \times 10^5)^{1/2} = 7{,}6 \times 10^2$. (b) $\Delta_\text{r}G^\circ$ berganti tanda: $K = 1/(5{,}8 \times 10^5) = 1{,}7 \times 10^{-6}$.

**Memahami hasil.** Karena $\ln K$ sebanding dengan $\Delta_\text{r}G^\circ$, dan $\Delta_\text{r}G^\circ$ mengikuti stoikiometri seperti entalpi dalam hukum Hess, aturan-aturan *K* dari Kimia Dasar langsung terbukti: mengalikan persamaan reaksi dengan *n* memangkatkan *K* dengan *n*; membalik reaksi membalik *K*; menjumlahkan reaksi mengalikan *K*-nya. Nilai *K* selalu harus disertai persamaan reaksi yang dimaksud.
:::

::: {.kuis}
**Kuis cepat 12.2** Suatu reaksi mempunyai *K* = 1. Berapa $\Delta_\text{r}G^\circ$-nya? Apakah ini berarti pada kesetimbangan jumlah pereaksi dan hasil sama?
:::

## 12.3 *K*, *K*_c, dan *K*_x

Tetapan (12.3) disebut tetapan kesetimbangan **termodinamika**, karena memakai aktivitas. Untuk gas ideal, aktivitas adalah $p_\text{J}/p^\circ$, sehingga *K* dapat ditulis sebagai $K = \prod(p_\text{J}/p^\circ)^{\nu_\text{J}}$. Dalam praktik, komposisi gas sering lebih mudah dinyatakan dengan konsentrasi molar atau fraksi mol, sehingga kita perlu cara mengubahnya.

Dengan $p_\text{J} = [\text{J}]RT$ (gas ideal) dan $p_\text{J} = x_\text{J}p$ (hukum Dalton):

$$
K = K_c\left(\frac{c^\circ RT}{p^\circ}\right)^{\Delta\nu} , \qquad K = K_x\left(\frac{p}{p^\circ}\right)^{\Delta\nu} , \qquad \text{(12.4)}
$$

dengan $K_c = \prod([\text{J}]/c^\circ)^{\nu_\text{J}}$, $K_x = \prod x_\text{J}^{\nu_\text{J}}$, dan $\Delta\nu = \sum\nu_\text{J}$ (gas) perubahan banyaknya mol gas dalam reaksi. Bila $\Delta\nu = 0$, ketiganya sama.

Bentuk kedua sangat penting: **K tidak bergantung pada tekanan, tetapi K_x bergantung**. Komposisi kesetimbangan (fraksi mol) adalah yang kita amati, dan bila $\Delta\nu \ne 0$, ia berubah ketika tekanan total berubah. Ini akan kita pakai di subbab 12.5.

::: {.contoh}
**Contoh 12.4 · *K*_c untuk N₂O₄**

Hitung $K_c$ untuk $\text{N}_2\text{O}_4 \rightleftharpoons 2\text{NO}_2$ pada 25 °C, dengan *K* = 0,148 dan $c^\circ = 1$ mol L⁻¹.

**Penyelesaian.** Δν = 2 − 1 = 1. Dengan $c^\circ RT/p^\circ = (1\ \text{mol L}^{-1})(0{,}083\,14\ \text{L bar K}^{-1}\text{mol}^{-1})(298{,}15\ \text{K})/(1\ \text{bar}) = 24{,}79$:
$$
K_c = \frac{K}{24{,}79} = \frac{0{,}148}{24{,}79} = 5{,}98 \times 10^{-3} .
$$

**Memahami hasil.** Satu liter gas ideal pada 1 bar dan 25 °C hanya berisi 0,040 mol, jauh di bawah 1 mol L⁻¹, sehingga konsentrasi dalam mol L⁻¹ kecil dan $K_c$ jauh lebih kecil daripada *K*. Kedua tetapan menggambarkan kesetimbangan yang sama; yang berbeda hanya keadaan acuannya.
:::

### Kesetimbangan heterogen

Bila padatan atau cairan murni ikut bereaksi, aktivitasnya satu dan mereka tidak muncul dalam *K*. Untuk penguraian batu kapur, $\text{CaCO}_3(s) \rightleftharpoons \text{CaO}(s) + \text{CO}_2(g)$, tetapan kesetimbangannya hanya $K = p_{\text{CO}_2}/p^\circ$. Tekanan CO₂ di atas campuran CaCO₃ dan CaO pada kesetimbangan, yang disebut **tekanan penguraian**, ditentukan oleh suhu saja, sesuai dengan aturan fasa (Contoh 11.2).

::: {.contoh}
**Contoh 12.5 · Tekanan penguraian batu kapur**

Untuk penguraian CaCO₃, $\Delta_\text{r}G^\circ(298\ \text{K}) = +130{,}4$ kJ mol⁻¹ dan $\Delta_\text{r}G^\circ(1000\ \text{K}) = +17{,}6$ kJ mol⁻¹ (Bab 7, Soal 35). Hitung tekanan penguraian pada kedua suhu.

**Penyelesaian.** Pada 298 K: $K = \exp(-130\,400/2479) = 1{,}4 \times 10^{-23}$, sehingga $p_{\text{CO}_2} = 1{,}4 \times 10^{-23}$ bar. Pada 1000 K: $K = \exp[-17\,600/(8{,}314 \times 1000)] = 0{,}12$, sehingga $p_{\text{CO}_2} = 0{,}12$ bar.

**Memahami hasil.** Pada suhu kamar, batu kapur sama sekali stabil: tekanan CO₂ di udara ($4 \times 10^{-4}$ bar) jauh di atas tekanan penguraiannya, sehingga yang cenderung terjadi justru sebaliknya, kapur tohor menyerap CO₂ dan kembali menjadi batu kapur (itulah sebabnya plester kapur mengeras di udara). Pada 1000 K, tekanan penguraian 0,12 bar, sudah jauh di atas tekanan CO₂ udara, sehingga batu kapur di dalam tanur yang terbuka terurai terus. Tanur kapur dijalankan sekitar 900–1000 °C supaya penguraiannya cepat.
:::

::: {.kuis}
**Kuis cepat 12.3** Untuk reaksi $\text{H}_2(g) + \text{I}_2(g) \rightleftharpoons 2\text{HI}(g)$, apakah *K*, *K*_c, dan *K*_x sama? Mengapa?
:::
