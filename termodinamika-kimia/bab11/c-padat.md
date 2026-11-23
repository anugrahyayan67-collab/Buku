## 11.6 Kesetimbangan cair–padat dan eutektik

Sekarang turunkan suhu. Pada campuran dua cairan yang bercampur sempurna, salah satu komponen akhirnya mulai membeku. Kita sudah menghitung penurunan titik beku untuk larutan encer (subbab 10.5). Kini kita perluas ke seluruh rentang komposisi.

Bayangkan B padat murni yang setimbang dengan larutan cair ideal berisi B. Syarat kesetimbangannya: potensial kimia B padat sama dengan potensial kimia B di dalam larutan,
$$
\mu_\text{B}^*(s) = \mu_\text{B}^*(l) + RT\ln x_\text{B} \quad\Rightarrow\quad \ln x_\text{B} = -\frac{\mu_\text{B}^*(l) - \mu_\text{B}^*(s)}{RT} = -\frac{\Delta_\text{fus}G}{RT} .
$$
Dengan persamaan Gibbs–Helmholtz, persis seperti penurunan subbab 10.5, tetapi kini tanpa pendekatan larutan encer:

::: {.inti}
$$
\ln x_\text{B} = -\frac{\Delta_\text{fus}H}{R}\left(\frac{1}{T} - \frac{1}{T_\text{f}^*}\right) . \qquad \text{(11.8)}
$$
**Kelarutan ideal.** Fraksi mol B dalam larutan jenuh pada suhu *T*, dengan $T_\text{f}^*$ titik leleh B murni. Persamaan yang sama, dibaca terbalik, memberi suhu mulai membeku larutan dengan komposisi $x_\text{B}$.
:::

Persamaan (11.8) mengandung kejutan: **pelarut tidak muncul di dalamnya**. Dalam pendekatan larutan ideal, kelarutan suatu padatan hanya bergantung pada titik leleh dan entalpi peleburannya sendiri. Padatan dengan titik leleh rendah dan entalpi peleburan kecil mudah larut; padatan dengan titik leleh tinggi sukar larut. Ini menjelaskan aturan praktis kimia organik: di antara isomer, yang titik lelehnya paling tinggi biasanya paling sukar larut.

::: {.contoh}
**Contoh 11.12 · Kelarutan naftalena**

Naftalena meleleh pada 80,2 °C (353,4 K) dengan $\Delta_\text{fus}H = 19{,}0$ kJ mol⁻¹. Hitung kelarutan idealnya pada 25 °C. Nilai terukur dalam benzena adalah $x = 0{,}296$; dalam heksana $x = 0{,}12$.

**Penyelesaian.**
$$
\ln x = -\frac{19\,010}{8{,}314}\left(\frac{1}{298{,}15} - \frac{1}{353{,}4}\right) = -(2286)(5{,}243 \times 10^{-4}) = -1{,}199 , \qquad x = 0{,}302 .
$$

**Memahami hasil.** Dalam benzena, yang molekulnya juga aromatik dan datar seperti naftalena, kelarutan terukur hampir tepat sama dengan ramalan ideal: larutannya hampir ideal. Dalam heksana, kelarutannya hanya 40% nilai ideal, karena naftalena dan heksana menyimpang positif dari Raoult (γ ≈ 2,5). Kelarutan ideal adalah batas atas yang baik untuk pelarut yang "mirip"; pelarut yang tidak mirip melarutkan lebih sedikit. Itulah wujud termodinamika dari aturan "*like dissolves like*".
:::

Bila kedua komponen dapat membeku, dan padatannya tidak saling melarutkan, diagram suhu–komposisinya mempunyai dua garis: garis tempat A mulai membeku (dari sisi kaya A) dan garis tempat B mulai membeku (dari sisi kaya B). Keduanya turun dari titik leleh murni masing-masing dan bertemu di satu titik: **titik eutektik** (dari bahasa Yunani: "mudah meleleh"). Gambar 11.5 memperlihatkan diagram seperti itu untuk benzena dan naftalena, dihitung seluruhnya dari (11.8).

![Gambar 11.5 Diagram fasa padat–cair benzena–naftalena, dihitung dengan persamaan kelarutan ideal (11.8). Garis kiri: benzena mulai membeku; garis kanan: naftalena mulai membeku. Keduanya bertemu di titik eutektik. Di bawah garis eutektik, campuran berupa dua padatan.](fig/eutektik.png){width=72%}

::: {.contoh}
**Contoh 11.13 · Titik eutektik benzena–naftalena**

Benzena: $T_\text{f}^* = 278{,}7$ K, $\Delta_\text{fus}H = 9{,}87$ kJ mol⁻¹. Naftalena: data Contoh 11.12. Tentukan suhu dan komposisi eutektik.

**Rencana.** Di titik eutektik, kedua padatan setimbang dengan larutan yang sama, sehingga (11.8) berlaku untuk keduanya sekaligus, dan $x_\text{benzena} + x_\text{naftalena} = 1$. Cari *T* yang memenuhi syarat itu dengan mencoba nilai.

**Penyelesaian.** Pada 269,6 K: dari (11.8), $x_\text{benzena} = \exp[-(9870/8{,}314)(1/269{,}6 - 1/278{,}7)] = 0{,}866$ dan $x_\text{naftalena} = \exp[-(19\,010/8{,}314)(1/269{,}6 - 1/353{,}4)] = 0{,}134$. Jumlahnya 1,000. Titik eutektik: 269,6 K (−3,5 °C), dengan $x_\text{naftalena} = 0{,}134$.

**Memahami hasil.** Campuran eutektik membeku pada suhu terendah dari semua campuran, 9 K di bawah titik beku benzena murni dan 84 K di bawah naftalena. Pada titik eutektik ada tiga fasa (dua padatan, satu larutan) dalam sistem dua komponen pada tekanan tetap, sehingga $F' = 2 - 3 + 1 = 0$: suhu dan komposisi tertentu sepenuhnya. Komposisi eutektik terletak dekat komponen yang titik lelehnya lebih rendah, karena komponen itulah yang lebih mudah "menampung" yang lain.
:::

Bagaimana diagram seperti itu ditentukan di laboratorium? Dengan **kurva pendinginan**. Leburan dengan komposisi tertentu didinginkan perlahan dan suhunya dicatat terhadap waktu. Selama hanya cairan, suhu turun mulus. Ketika satu komponen mulai membeku, kalor peleburan yang dilepaskan memperlambat pendinginan, dan kurva **patah** (berubah kemiringan). Ketika suhu eutektik tercapai, kedua komponen membeku bersama pada suhu tetap, dan kurva menjadi **datar** sampai semua cairan habis. Panjang bagian datar itu sebanding dengan banyaknya cairan eutektik. Campuran yang tepat berkomposisi eutektik tidak mempunyai patahan, hanya bagian datar, seperti zat murni.

::: {.contoh}
**Contoh 11.14 · Kurva pendinginan solder**

Timah meleleh pada 232 °C dan timbal pada 327 °C. Paduan timah–timbal mempunyai titik eutektik pada 183 °C dan 61,9% massa timah. (a) Gambarkan kurva pendinginan untuk paduan 30% timah, yang mulai membeku pada sekitar 255 °C. (b) Mengapa solder elektronik klasik dibuat dengan komposisi sekitar 63% timah?

**Penyelesaian.** (a) Dari suhu tinggi, suhu turun mulus sampai 255 °C. Di sana kurva patah: padatan kaya timbal mulai mengendap dan cairan yang tersisa makin kaya timah, sehingga suhu terus turun tetapi lebih lambat. Pada 183 °C cairan sudah mencapai komposisi eutektik dan kurva datar sampai seluruh cairan membeku. Setelah itu suhu turun mulus lagi.

(b) Paduan eutektik meleleh dan membeku pada satu suhu, tanpa rentang "lembek" di antara padat dan cair. Solder yang membeku tajam tidak bergeser ketika komponen digerakkan sedikit selama pendinginan, sehingga sambungannya lebih andal. Suhu lelehnya juga yang terendah dari semua paduan timah–timbal, sehingga komponen elektronik tidak kepanasan.

**Memahami hasil.** Pada paduan logam nyata, kedua logam saling melarutkan sedikit dalam keadaan padat, sehingga fasa padatnya bukan timbal atau timah murni tetapi larutan padat kaya timbal dan kaya timah. Diagramnya sedikit lebih rumit, tetapi bentuk dasarnya, dua garis yang turun ke titik eutektik, tetap sama.
:::

::: {.terapan}
**Dari solder ke silikon murni.** Karena timbal beracun, solder elektronik modern memakai paduan timah–perak–tembaga (sekitar 96,5% Sn, 3% Ag, 0,5% Cu), yang juga hampir eutektik dan meleleh pada 217 °C. Prinsip kesetimbangan padat–cair juga dipakai sebaliknya, untuk **memurnikan**. Garis-garis pada Gambar 11.5 menunjukkan bahwa padatan yang mengendap dari cairan lebih murni daripada cairannya. Dalam **pemurnian zona**, batang silikon dilewatkan perlahan melalui pemanas yang melelehkan hanya satu zona tipis. Ketika zona leleh bergerak sepanjang batang, padatan yang membeku di belakangnya lebih murni, dan pengotor terbawa bersama zona leleh ke ujung batang. Setelah beberapa kali lewat, silikon untuk chip komputer mencapai kemurnian sembilan angka sembilan (99,9999999%).
:::

Diagram air–garam yang dipakai untuk menjelaskan garam di jalan (subbab 10.5) juga diagram eutektik. Garis kiri adalah garis beku es, yang turun dari 0 °C ketika garam ditambahkan; garis kanan adalah garis kelarutan garam (sebagai NaCl·2H₂O pada suhu rendah).

::: {.contoh}
**Contoh 11.15 · Eutektik air–garam**

Titik eutektik NaCl–air terletak pada −21,1 °C dan 23,3% massa NaCl. (a) Berapa molalitas NaCl larutan eutektik? (b) Berapa titik beku yang diramalkan rumus penurunan titik beku ideal untuk molalitas itu?

**Penyelesaian.** (a) Dalam 100 g larutan: 23,3 g NaCl (0,399 mol) dalam 76,7 g air. $b = 0{,}399/0{,}0767 = 5{,}20$ mol kg⁻¹.

(b) Dengan dua ion per satuan rumus: $\Delta T_\text{f} = (1{,}86)(2)(5{,}20) = 19{,}3$ K, titik beku −19,3 °C.

**Memahami hasil.** Rumus larutan encer ideal meleset hanya 2 K, walaupun larutannya sangat pekat. Kebetulan ini terjadi karena dua penyimpangan saling mengimbangi sebagian: ion-ion menurunkan aktivitas satu sama lain (Debye–Hückel), tetapi hidrasi ion yang kuat "mengikat" sebagian air sehingga air bebasnya lebih sedikit. Di bawah −21,1 °C, tidak ada larutan garam yang tetap cair; inilah batas bawah garam untuk mencairkan es di jalan. Untuk daerah yang lebih dingin dipakai CaCl₂, yang eutektiknya −51 °C.
:::

Tidak semua campuran padat–cair sesederhana ini. Bila A dan B membentuk **senyawa** padat, misalnya hidrat garam atau senyawa antarlogam, diagramnya tampak seperti dua diagram eutektik yang ditempel berdampingan, dengan senyawa itu di tengah sebagai "komponen" ketiga yang meleleh pada suhunya sendiri (peleburan **kongruen**). Beberapa senyawa terurai sebelum meleleh menjadi padatan lain dan cairan (peleburan **inkongruen**). Diagram fasa logam dan keramik yang dipakai dalam metalurgi dapat sangat rumit, tetapi semuanya disusun dari unsur-unsur yang sama: daerah satu fasa, daerah dua fasa dengan garis hubung, dan titik-titik tiga fasa tempat *F*′ = 0.

::: {.kuis}
**Kuis cepat 11.6** Mengapa kurva pendinginan campuran eutektik tidak mempunyai patahan, hanya bagian datar?
:::

## 11.7 Diagram segitiga tiga komponen

Untuk tiga komponen, aturan fasa memberi $F = 5 - P$. Pada suhu dan tekanan tetap, $F'' = 3 - P$: satu fasa mempunyai dua derajat kebebasan (dua fraksi mol bebas), sehingga komposisinya dapat digambarkan pada bidang. Cara yang paling praktis adalah **diagram segitiga sama sisi**.

Setiap sudut segitiga menyatakan satu komponen murni. Setiap sisi menyatakan campuran dua komponen yang berada di kedua ujungnya. Setiap titik di dalam segitiga menyatakan campuran ketiganya, dan fraksi setiap komponen dibaca sebagai jarak titik itu dari sisi di **seberang** sudut komponen tersebut: di sudut, fraksinya 1; di sisi seberangnya, 0. Garis-garis yang sejajar dengan satu sisi adalah garis dengan fraksi tetap untuk komponen di sudut seberangnya. Sifat geometris segitiga sama sisi menjamin bahwa ketiga fraksi selalu berjumlah satu.

![Gambar 11.6 Diagram segitiga air–kloroform–asam asetat pada suhu dan tekanan tetap (skematis). Air dan kloroform hampir tidak bercampur (sisi bawah), tetapi asam asetat larut dalam keduanya. Di bawah kurva, campuran terpisah menjadi dua lapisan; garis hubung menghubungkan komposisi lapisan yang setimbang. Titik P berisi 20% air, 30% kloroform, dan 50% asam asetat.](fig/segitiga.png){width=66%}

Gambar 11.6 memperlihatkan sistem yang khas untuk ekstraksi. Air dan kloroform hampir tidak saling melarutkan, sehingga hampir seluruh sisi bawah adalah daerah dua fasa. Asam asetat larut dalam keduanya. Ketika asam asetat ditambahkan, kedua lapisan saling melarutkan makin banyak, daerah dua fasa menyempit, dan akhirnya, di atas kurva, ketiganya bercampur menjadi satu fasa. Garis hubung di daerah dua fasa miring: asam asetat tidak terbagi sama rata di antara kedua lapisan.

::: {.contoh}
**Contoh 11.16 · Membaca dan mencampur**

(a) Jelaskan bagaimana titik P pada Gambar 11.6 menyatakan 20% air, 30% kloroform, dan 50% asam asetat. (b) Sebanyak 50 g campuran P dicampur dengan 50 g asam asetat murni. Di mana letak campuran baru pada diagram?

**Penyelesaian.** (a) P terletak pada garis mendatar setengah jalan ke puncak (asam asetat 50%), pada garis sejajar sisi kanan yang berjarak 0,2 dari sisi kanan menuju sudut air (air 20%), dan sisanya kloroform 30%.

(b) Komposisi baru, dalam 100 g: asam asetat $25 + 50 = 75$ g, air 10 g, kloroform 15 g, yaitu 10% air, 15% kloroform, 75% asam asetat. Titik ini terletak pada garis lurus dari P ke sudut asam asetat, tepat di tengahnya.

**Memahami hasil.** Mencampur dua campuran selalu memberi titik pada garis lurus yang menghubungkan keduanya, dan letaknya ditentukan oleh aturan tuas. Menambahkan satu komponen murni menggerakkan titik lurus menuju sudut komponen itu. Kedua sifat ini membuat diagram segitiga sangat berguna untuk merancang ekstraksi: setiap langkah pencampuran dan pemisahan dapat diikuti dengan penggaris.
:::

::: {.kuis}
**Kuis cepat 11.7** Pada diagram segitiga, di mana letak semua campuran yang perbandingan air terhadap kloroformnya 1 : 1?
:::

## 11.8 Ekstraksi dan sistem tiga komponen dalam praktik

**Ekstraksi pelarut** memanfaatkan sistem tiga komponen yang paling sederhana: zat terlarut B yang terbagi di antara dua pelarut yang tidak bercampur, misalnya air dan pelarut organik. Pada kesetimbangan, potensial kimia B sama di kedua lapisan. Bila keduanya larutan encer ideal, $\mu_\text{B} = \mu_\text{B}^\circ + RT\ln(c_\text{B}/c^\circ)$ di setiap lapisan, dengan $\mu_\text{B}^\circ$ yang berbeda untuk setiap pelarut. Menyamakan keduanya:

::: {.inti}
$$
K = \frac{c_\text{B}(\text{org})}{c_\text{B}(\text{air})} = \exp\left(-\frac{\mu_\text{B}^\circ(\text{org}) - \mu_\text{B}^\circ(\text{air})}{RT}\right) . \qquad \text{(11.9)}
$$
**Hukum distribusi Nernst.** Perbandingan konsentrasi zat terlarut di kedua lapisan tetap pada suhu tertentu, dan ditentukan oleh selisih potensial kimia standarnya di kedua pelarut.
:::

Inilah penjelasan kuantitatif dari Contoh 9.6: iodin terbagi dengan $K = 85$ antara CCl₄ dan air, yang berarti potensial kimia standarnya di dalam CCl₄ lebih rendah $RT\ln85 = 11{,}0$ kJ mol⁻¹ daripada di dalam air.

Berapa banyak zat terambil dalam satu kali ekstraksi? Misalkan $n_0$ mol B mula-mula ada dalam volume $V_\text{a}$ air, dan dikocok dengan volume $V_\text{o}$ pelarut organik. Bila $n$ mol tertinggal di air, maka $n_0 - n$ pindah ke pelarut organik, dan $K = [(n_0 - n)/V_\text{o}]/(n/V_\text{a})$. Fraksi yang tertinggal:

$$
\frac{n}{n_0} = \frac{1}{1 + KV_\text{o}/V_\text{a}} . \qquad \text{(11.10)}
$$

Bila ekstraksi diulang *k* kali dengan pelarut segar setiap kali, fraksi yang tertinggal dipangkatkan *k*.

::: {.contoh}
**Contoh 11.17 · Sekali banyak atau berkali-kali sedikit?**

Iodin dalam 100 mL air diekstraksi dengan total 50 mL CCl₄ (*K* = 85). Bandingkan fraksi iodin yang tertinggal di air bila pelarut dipakai (a) sekaligus, (b) dalam dua bagian 25 mL, (c) dalam tiga bagian 16,7 mL.

**Penyelesaian.** (a) $KV_\text{o}/V_\text{a} = (85)(50/100) = 42{,}5$: tertinggal $1/43{,}5 = 0{,}023$, atau 2,3%.

(b) $KV_\text{o}/V_\text{a} = 21{,}25$ setiap kali: tertinggal $(1/22{,}25)^2 = 0{,}0020$, atau 0,20%.

(c) $KV_\text{o}/V_\text{a} = 14{,}2$: tertinggal $(1/15{,}2)^3 = 0{,}000\,29$, atau 0,03%.

**Memahami hasil.** Dengan pelarut yang sama banyaknya, membaginya menjadi tiga bagian mengurangi sisa delapan puluh kali lipat. Ini aturan praktis yang diajarkan di setiap laboratorium organik: ekstraksi berulang dengan sedikit pelarut selalu lebih efisien. Alasannya matematis: setiap ekstraksi mengambil **fraksi** tetap dari yang tersisa, sehingga pengulangan memberi penurunan eksponensial.
:::

Ekstraksi sangat penting ketika *K* tidak besar. Untuk zat dengan *K* = 2, satu kali ekstraksi dengan volume pelarut sama hanya mengambil dua pertiga; untuk memperoleh 99% diperlukan lima kali ekstraksi. Dalam industri, ekstraksi dilakukan **berlawanan arah** di kolom atau rangkaian bejana: pelarut segar masuk dari satu ujung dan larutan umpan dari ujung lain, sehingga pada setiap tahap pelarut bertemu larutan yang komposisinya paling cocok. Prinsipnya sama dengan pelat-pelat distilasi: sederet tahap kesetimbangan yang masing-masing memperkaya sedikit.

::: {.terapan}
**Ekstraksi dalam industri dan analisis.** Penisilin dimurnikan dari kaldu fermentasi dengan ekstraksi ke butil asetat pada pH rendah, tempat penisilin tidak bermuatan dan lebih suka pelarut organik, lalu dikembalikan ke air pada pH tinggi, tempat ia bermuatan. Mengubah pH mengubah μ° efektif zat terlarut di dalam air, sehingga *K* dapat "dinyalakan" dan "dimatikan". Cara yang sama dipakai untuk memisahkan logam: ion uranium dan logam tanah jarang diekstraksi ke kerosin dengan bantuan senyawa pengompleks seperti tributil fosfat. Di laboratorium analisis, ekstraksi fase padat (SPE) memakai prinsip yang sama dengan fase organik yang terikat pada butir silika.
:::

Penambahan zat ketiga juga dapat **mengurangi** kelarutan. Bila garam dilarutkan dalam campuran air dan pelarut organik yang bercampur, seperti air dan aseton atau air dan etanol, ion-ion garam mengikat air begitu kuat sehingga potensial kimia pelarut organik di dalam air naik, dan campuran terpisah menjadi dua lapisan. Gejala ini disebut ***salting out***, dan dipakai untuk memisahkan pelarut organik dari air, serta untuk mengendapkan protein dengan amonium sulfat di laboratorium biokimia.

::: {.kuis}
**Kuis cepat 11.8** Suatu zat mempunyai *K* = 1 di antara eter dan air. Berapa kali ekstraksi dengan volume eter sama dengan volume air diperlukan agar 99% zat itu terambil?
:::

## 11.9 Larutan padat dan pemurnian zona

Diagram eutektik di subbab 11.6 menganggap kedua komponen sama sekali tidak saling melarutkan dalam keadaan padat: kristal A hanya berisi A, kristal B hanya berisi B. Untuk benzena dan naftalena anggapan itu baik, karena molekulnya terlalu berbeda untuk saling menggantikan di kisi kristal. Tetapi tembaga dan nikel, misalnya, mempunyai jari-jari atom yang hampir sama (128 dan 125 pm) dan kisi kristal yang sama (kubus berpusat muka). Atom nikel dapat menempati kedudukan atom tembaga di kisi tanpa merusaknya. Paduan Cu–Ni dengan komposisi berapa pun membentuk satu fasa padat yang homogen, yang disebut **larutan padat**. Seperti apa diagram fasanya?

### Diagram lensa

Bila larutan cair maupun larutan padat keduanya ideal, syarat kesetimbangan untuk setiap komponen *i* adalah kesamaan potensial kimianya di kedua fasa. Dengan cara yang sama seperti penurunan kelarutan ideal (11.8), syarat itu memberi
$$
\frac{x_i^\text{cair}}{x_i^\text{padat}} = \exp\left[-\frac{\Delta_\text{fus}H_i}{R}\left(\frac{1}{T} - \frac{1}{T_{\text{f},i}}\right)\right] \equiv K_i . \qquad \text{(11.11)}
$$
Pada suhu tertentu, $K_\text{Cu}$ dan $K_\text{Ni}$ dapat dihitung, dan dua persamaan $x_\text{Cu}^\text{padat} + x_\text{Ni}^\text{padat} = 1$ serta $K_\text{Cu}x_\text{Cu}^\text{padat} + K_\text{Ni}x_\text{Ni}^\text{padat} = 1$ menentukan komposisi kedua fasa. Hasilnya, untuk setiap suhu antara titik leleh kedua logam, adalah dua titik: komposisi cairan (pada **likuidus**) dan komposisi padatan (pada **solidus**) yang setimbang. Kedua kurva membentuk diagram berbentuk lensa (Gambar 11.7).

![Gambar 11.7 Diagram fasa Cu–Ni yang dihitung dari model larutan ideal untuk fasa cair dan padat, dengan titik leleh dan entalpi peleburan kedua logam murni. Di antara likuidus dan solidus, cairan dan larutan padat berada bersama; garis mendatar pada 1500 K menghubungkan komposisi kedua fasa itu.](fig/lensa.png){width=72%}

Bentuk ini sama dengan diagram suhu–komposisi untuk distilasi campuran ideal (subbab 11.3), dan itu bukan kebetulan: matematikanya sama, hanya peran "cair dan uap" diganti "padat dan cair". Padatan yang membeku selalu lebih kaya akan komponen dengan titik leleh lebih tinggi, sebagaimana uap selalu lebih kaya akan komponen yang lebih mudah menguap. Aturan tuas (subbab 11.2) berlaku tanpa perubahan untuk menghitung banyaknya kedua fasa.

::: {.contoh}
**Contoh 11.18 · Membekukan paduan Cu–Ni**

Untuk tembaga, $T_\text{f}$ = 1357,8 K dan Δ$_\text{fus}$*H* = 13,26 kJ mol⁻¹; untuk nikel, 1728,3 K dan 17,48 kJ mol⁻¹. Anggap kedua fasa ideal. (a) Pada 1500 K, berapa komposisi cairan dan padatan yang setimbang? (b) Lelehan paduan dengan $x_\text{Ni}$ = 0,38 didinginkan perlahan sampai 1500 K. Berapa fraksi mol bahan yang sudah membeku?

**Penyelesaian.** (a) Dari (11.11) pada 1500 K:
$$
K_\text{Cu} = \exp\left[-\frac{13\,260}{8{,}314}\left(\frac{1}{1500} - \frac{1}{1357{,}8}\right)\right] = 1{,}118 , \qquad K_\text{Ni} = \exp\left[-\frac{17\,480}{8{,}314}\left(\frac{1}{1500} - \frac{1}{1728{,}3}\right)\right] = 0{,}831 .
$$
Maka $x_\text{Cu}^\text{padat} = (1 - K_\text{Ni})/(K_\text{Cu} - K_\text{Ni}) = 0{,}589$, sehingga padatan berisi $x_\text{Ni}$ = 0,411. Cairannya berisi $x_\text{Cu}^\text{cair} = K_\text{Cu}(0{,}589) = 0{,}659$, yaitu $x_\text{Ni}$ = 0,341.

(b) Dengan aturan tuas, fraksi padat $= (0{,}38 - 0{,}341)/(0{,}411 - 0{,}341) = 0{,}56$.

**Memahami hasil.** Pada 1500 K, lebih dari separuh bahan sudah membeku, dan padatan yang terbentuk berisi nikel 7 poin persen lebih banyak daripada cairan di sekitarnya. Bila pendinginan berlangsung cepat, atom di dalam butir kristal tidak sempat berdifusi untuk menyamakan komposisi, sehingga pusat setiap butir kaya nikel dan tepinya kaya tembaga. Gejala ini, yang disebut **segregasi**, membuat paduan cor sering harus dipanaskan ulang (anil) supaya komposisinya merata. Model ideal ini hanya pendekatan; diagram Cu–Ni yang terukur sedikit lebih lebar, karena kedua larutan tidak sepenuhnya ideal.
:::

### Senyawa yang meleleh kongruen dan tak kongruen

Subbab 11.6 menyinggung bahwa A dan B dapat membentuk senyawa padat. Bila senyawa itu meleleh menjadi cairan yang komposisinya sama dengan senyawa itu sendiri, peleburannya disebut **kongruen**, dan diagramnya berupa dua diagram eutektik berdampingan dengan maksimum di komposisi senyawa. Contohnya Mg₂Si, yang meleleh kongruen pada sekitar 1100 °C.

Tidak semua senyawa sebaik itu. Natrium sulfat dekahidrat (garam Glauber, Na₂SO₄·10H₂O) tidak meleleh pada 32,4 °C, melainkan **terurai** menjadi padatan lain (Na₂SO₄ anhidrat) dan larutan jenuh yang komposisinya berbeda. Peleburan semacam ini disebut **tak kongruen**, dan suhu tempat tiga fasa itu berada bersama disebut **titik peritektik**. Pada titik itu, menurut aturan fasa untuk dua komponen pada tekanan tetap ($F' = C - P + 1 = 2 - 3 + 1 = 0$), suhu tertentu tunggal, sehingga kurva pendinginan memperlihatkan bagian datar, seperti pada titik eutektik. Garam Glauber dipakai sebagai bahan penyimpan kalor di bangunan justru karena titik peritektiknya dekat suhu ruang: ia menyerap kalor besar ketika "meleleh" pada siang hari dan melepasnya kembali pada malam hari.

### Pemurnian zona

Diagram lensa mempunyai akibat praktis yang sangat penting: bila sedikit kotoran B terdapat dalam A, padatan yang membeku dari lelehan **tidak** mempunyai komposisi yang sama dengan lelehannya. Perbandingan konsentrasi kotoran di padatan terhadap di cairan yang setimbang disebut **koefisien distribusi** *k*:
$$
k = \frac{C_\text{padat}}{C_\text{cair}} .
$$
Untuk kebanyakan kotoran dalam silikon, *k* jauh lebih kecil dari 1 (untuk besi dalam silikon sekitar 10⁻⁵, untuk fosfor 0,35). Kotoran lebih suka tinggal di cairan.

W. G. Pfann (1952) memanfaatkan hal ini dalam **pemurnian zona**. Batang padat dilewatkan perlahan melalui pemanas cincin, sehingga hanya satu zona sempit sepanjang *L* yang meleleh. Ketika zona itu bergerak sepanjang batang, padatan yang membeku di belakangnya mengambil kotoran sebanyak *k* kali kadar di cairan, dan sisanya terbawa maju oleh zona. Setelah satu lintasan, kadar kotoran pada jarak *x* dari ujung awal adalah
$$
\frac{C(x)}{C_0} = 1 - (1 - k)\,e^{-kx/L} , \qquad \text{(11.12)}
$$
dengan $C_0$ kadar awal yang seragam. Kotoran menumpuk di ujung akhir batang, yang kemudian dipotong dan dibuang.

![Gambar 11.8 Kadar kotoran sepanjang batang setelah satu lintasan pemurnian zona, menurut (11.12). Makin kecil koefisien distribusi *k*, makin bersih bagian awal batang. Lintasan berulang menurunkan kadar lebih jauh.](fig/zona.png){width=76%}

::: {.contoh}
**Contoh 11.19 · Satu lintasan pemurnian zona**

Batang silikon mengandung kotoran dengan *k* = 0,10 secara seragam. Setelah satu lintasan zona, berapa kadar kotoran relatif di ujung awal (*x* = 0), pada *x* = *L*, dan pada *x* = 5*L*? Bagaimana bila *k* = 0,50?

**Penyelesaian.** Untuk *k* = 0,10: pada *x* = 0, $C/C_0 = 1 - 0{,}90 = 0{,}10$; pada *x* = *L*, $1 - 0{,}90\,e^{-0{,}10} = 0{,}19$; pada *x* = 5*L*, $1 - 0{,}90\,e^{-0{,}50} = 0{,}45$. Untuk *k* = 0,50: 0,50; 0,70; 0,96.

**Memahami hasil.** Satu lintasan sudah menurunkan kotoran sepuluh kali di ujung awal bila *k* = 0,1, tetapi hanya dua kali bila *k* = 0,5. Dengan puluhan lintasan, kotoran dengan *k* kecil dapat diturunkan sampai tingkat bagian per miliar, kemurnian yang diperlukan silikon untuk transistor. Prinsipnya sama dengan distilasi bertingkat (subbab 11.3): setiap lintasan adalah satu "pelat teoretis", dan pemisahan menumpuk karena satu fasa selalu sedikit lebih kaya akan satu komponen daripada fasa lainnya.
:::

::: {.kuis}
**Kuis cepat 11.9** Mengapa garam dapur dan air membentuk diagram eutektik, sedangkan tembaga dan nikel membentuk larutan padat? Petunjuk: bandingkan ukuran dan jenis partikelnya.
:::

### Menuju bab berikutnya

Dalam tiga bab terakhir, potensial kimia menjelaskan semua kesetimbangan **fisika**: zat murni yang berubah fasa, pelarut yang bergerak melewati membran, campuran yang mendidih, membeku, atau terpisah menjadi lapisan. Dalam setiap kasus, zat berpindah dari satu fasa ke fasa lain sampai potensial kimianya sama di mana-mana.

Kesetimbangan **kimia** mengikuti prinsip yang sama dengan satu perubahan: kini zat tidak hanya berpindah tempat, tetapi berubah menjadi zat lain. Reaksi berlangsung sampai jumlah potensial kimia pereaksi, ditimbang dengan koefisien stoikiometri, sama dengan jumlah potensial kimia hasil. Bab 12 menunjukkan bahwa dari syarat sederhana itu, dan dari rumus $\mu = \mu^\circ + RT\ln a$ yang kita kumpulkan di Bab 9 dan 10, muncul tetapan kesetimbangan dan hubungan terkenal $\Delta_\text{r}G^\circ = -RT\ln K$.
