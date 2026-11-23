## 9.10 Korelasi elektron

### Apa yang hilang dari Hartree–Fock

Metode Hartree–Fock memberi energi total atom dengan galat kurang dari 1%: untuk neon, $-128{,}547\ E_h$ terhadap nilai eksak $-128{,}938\ E_h$. Tetapi galat 0,3% itu sebesar $0{,}39\ E_h$, sekitar 1000 kJ/mol, lebih besar daripada energi hampir semua ikatan kimia. Selisih ini mempunyai nama khusus. **Energi korelasi** didefinisikan (Löwdin, 1955) sebagai

$$
E_\text{kor} = E_\text{eksak} - E_\text{HF} , \qquad \text{(9.33)}
$$

dengan $E_\text{eksak}$ energi nonrelativistik eksak dan $E_\text{HF}$ batas Hartree–Fock (basis lengkap). Karena HF adalah metode variasi, $E_\text{kor}$ selalu negatif.

Dari mana galat itu? Dalam satu determinan, setiap elektron bergerak dalam medan **rata-rata** elektron lain. Peluang menemukan elektron berspin $\alpha$ di suatu titik tidak dipengaruhi oleh posisi sesaat elektron berspin $\beta$: rapat peluang dua elektron berspin berlawanan hanyalah hasil kali rapat masing-masing. Elektron yang sebenarnya saling menolak dan menyesuaikan geraknya secara sesaat: bila satu elektron berada di sisi kiri inti, yang lain cenderung di sisi kanan. Penyesuaian gerak yang tidak tertangkap oleh medan rata-rata inilah **korelasi elektron**.

Elektron berspin **sama** sebenarnya sudah sebagian berkorelasi dalam HF, karena antisimetri menggali lubang Fermi di sekitar setiap elektron (subbab 9.3). Elektron berspin **berlawanan** tidak mempunyai lubang apa pun dalam HF. Fungsi gelombang yang sebenarnya menggali **lubang Coulomb** di sekitar setiap elektron untuk elektron lain dari spin mana pun. Karena itu, sebagian besar energi korelasi berasal dari pasangan elektron berspin berlawanan, terutama yang menempati orbital ruang yang sama.

### Seberapa besar?

Energi korelasi atom ringan (selisih nilai eksak dan batas HF):

| Atom | He | Li | Be | B | C | N | O | F | Ne |
|---|---|---|---|---|---|---|---|---|---|
| $-E_\text{kor}$ (m$E_h$) | 42,0 | 45,3 | 94,3 | 124,9 | 156,4 | 188,3 | 257,9 | 324,6 | 390,5 |
| $-E_\text{kor}$ (eV) | 1,14 | 1,23 | 2,57 | 3,40 | 4,26 | 5,12 | 7,02 | 8,83 | 10,63 |

Pola-polanya bermakna. Litium hampir sama dengan helium: elektron 2s yang jauh hampir tidak berkorelasi dengan pasangan 1s. Berilium melonjak dua kali lipat: pasangan 2s² berkorelasi kuat (lihat korelasi statis di bawah). Dari B ke N, setiap elektron 2p baru berspin sejajar dengan yang lain (aturan Hund) dan hanya menambah sekitar $0{,}03\ E_h$. Pada O, F, dan Ne, elektron 2p mulai berpasangan dengan spin berlawanan di orbital yang sama, dan setiap pasangan baru menambah sekitar $0{,}07\ E_h$. Secara kasar, setiap pasangan elektron berspin berlawanan dalam orbital yang sama menyumbang 1–2 eV energi korelasi (Gambar 9.5).

![Gambar 9.5 Energi korelasi atom He sampai Ne (nilai mutlak), terhadap jumlah elektron. Lonjakan pada Be (pasangan 2s² dengan korelasi statis) dan kenaikan tajam dari N ke Ne (elektron 2p mulai berpasangan) menunjukkan bahwa korelasi didominasi pasangan elektron berspin berlawanan.](fig/c_korelasi.png){width=72%}

### Korelasi dinamis dan korelasi statis

Kimiawan membedakan dua jenis korelasi.

**Korelasi dinamis** adalah penghindaran sesaat jarak pendek antara elektron-elektron, yang selalu ada. Ia berkaitan dengan bentuk fungsi gelombang di dekat $r_{12} = 0$: fungsi gelombang eksak mempunyai "puncak lancip" (*cusp*) ketika dua elektron bertemu, dengan kemiringan $\partial\Psi/\partial r_{12} = \tfrac12\Psi$ (syarat cusp Kato), sama seperti cusp elektron–inti yang membuat orbital 1s lancip di inti. Fungsi yang disusun dari orbital-orbital mulus tidak mempunyai cusp ini, sehingga diperlukan sangat banyak determinan untuk menirunya. Itulah sebabnya perhitungan korelasi konvergen lambat terhadap ukuran basis, dan mengapa metode modern "berkorelasi eksplisit" memasukkan $r_{12}$ langsung ke fungsi gelombang, kembali ke gagasan Hylleraas 1929 (Contoh 8.16).

**Korelasi statis** (atau nondinamis) muncul bila dua atau lebih konfigurasi hampir sama energinya, sehingga satu determinan bukan lagi gambaran yang baik bahkan secara kualitatif. Contoh klasik: berilium, yang orbital 2s dan 2p-nya dekat, sehingga konfigurasi $1s^2 2p^2$ bercampur kuat dengan $1s^2 2s^2$ (Contoh 9.35); molekul yang ikatannya diregangkan menuju disosiasi (Contoh 9.36); diradikal; dan banyak senyawa logam transisi. Untuk sistem-sistem ini diperlukan fungsi gelombang multikonfigurasi sejak awal.

### Melampaui Hartree–Fock

Semua metode korelasi memperluas fungsi gelombang HF dengan determinan-determinan lain yang diperoleh dengan memindahkan elektron dari orbital terisi ke orbital kosong ("tereksitasi"):

$$
\Psi = c_0\Phi_\text{HF} + \sum_{i,a}c_i^a\Phi_i^a + \sum_{i<j,\,a<b}c_{ij}^{ab}\Phi_{ij}^{ab} + \cdots \qquad \text{(9.34)}
$$

Bila koefisiennya ditentukan dengan metode variasi linear (subbab 8.4), metodenya disebut **interaksi konfigurasi** (CI); bila semua determinan yang mungkin dalam suatu basis disertakan, hasilnya **CI penuh**, penyelesaian eksak dalam basis itu. Teori perturbasi Møller–Plesset (MP2, kotak di subbab 8.8) dan metode *coupled cluster* adalah cara lain menentukan koefisien yang sama, dan teori fungsional kerapatan mencoba memasukkan korelasi melalui fungsional kerapatan (Bab 17). Teorema Brillouin (subbab 9.14) menunjukkan bahwa eksitasi tunggal $\Phi_i^a$ tidak bercampur langsung dengan $\Phi_\text{HF}$; sumbangan utama berasal dari eksitasi **ganda**, yaitu pasangan elektron yang bersama-sama "menghindar" ke orbital kosong.

::: {.inti}
**Korelasi elektron**

$E_\text{kor} = E_\text{eksak} - E_\text{HF} < 0$. Ia berasal dari penghindaran sesaat antarelektron yang tidak tertangkap medan rata-rata, terutama pasangan berspin berlawanan (lubang Coulomb). Korelasi dinamis: jarak pendek, selalu ada, konvergen lambat. Korelasi statis: hampir-degenerasi konfigurasi, memerlukan fungsi multikonfigurasi. Besarnya sekitar 1–2 eV per pasangan elektron, sebanding dengan energi ikatan kimia.
:::

::: {.contoh}
**Contoh 9.33 · Lubang Coulomb dalam angka**

Untuk helium, nilai rata-rata tolakan antarelektron adalah $1{,}0258\ E_h$ dalam fungsi HF dan $0{,}9458\ E_h$ dalam fungsi eksak. Energinya $-2{,}86168$ (HF) dan $-2{,}90372\ E_h$ (eksak), dan keduanya memenuhi teorema virial ($\langle T\rangle = -E$, $\langle V\rangle = 2E$). (a) Hitung perubahan $\langle T\rangle$, $\langle V_{ee}\rangle$, dan $\langle V_{ne}\rangle$ dari HF ke eksak. (b) Tafsirkan.

**Penyelesaian.** (a) $\Delta\langle T\rangle = 2{,}90372 - 2{,}86168 = +0{,}0420$. $\Delta\langle V\rangle = 2(-0{,}0420) = -0{,}0841$. $\Delta\langle V_{ee}\rangle = 0{,}9458 - 1{,}0258 = -0{,}0800$. Jadi $\Delta\langle V_{ne}\rangle = -0{,}0841 + 0{,}0800 = -0{,}0041\ E_h$.

(b) Korelasi menurunkan tolakan antarelektron sebesar $0{,}080\ E_h$ (2,2 eV), dengan "biaya" energi kinetik $0{,}042\ E_h$, sementara tarikan inti hampir tidak berubah. Hasil bersihnya adalah energi korelasi, $-0{,}042\ E_h$.

**Memahami hasil.** Elektron-elektron membayar penghindaran dengan energi kinetik: untuk saling menjauh pada saat-saat tertentu, fungsi gelombang harus melengkung lebih tajam, yang menaikkan energi kinetik (subbab 3.7). Keseimbangan antara keduanya diatur oleh teorema virial. Pola yang sama berlaku pada ikatan kimia (subbab 11.15): pembentukan ikatan juga merupakan tawar-menawar antara energi kinetik dan potensial.
:::

::: {.contoh}
**Contoh 9.34 · Korelasi dan energi ikatan**

Energi korelasi neon $-0{,}391\ E_h$ dan atom fluor $-0{,}325\ E_h$. (a) Nyatakan dalam kJ/mol dan bandingkan dengan energi ikatan F–F (158 kJ/mol). (b) Metode HF meramalkan bahwa molekul F₂ **tidak** terikat ($D_e \approx -1{,}4$ eV), padahal nilai terukurnya $+1{,}66$ eV. Apa artinya?

**Penyelesaian.** (a) Ne: $-1025$ kJ/mol; F: $-852$ kJ/mol. Keduanya lima sampai enam kali energi ikatan F–F.

(b) Selisih energi korelasi antara molekul F₂ dan dua atom F lebih dari 3 eV, lebih besar daripada energi ikatan itu sendiri. Ketika ikatan terbentuk, dua elektron yang tadinya di atom berbeda menjadi pasangan dalam satu orbital ikatan, dan pasangan baru ini (bersama perubahan pada pasangan elektron bebas) menambah energi korelasi.

**Memahami hasil.** Untuk sebagian besar reaksi, galat HF dalam energi reaksi berorde puluhan sampai ratusan kJ/mol, sehingga HF tidak cukup untuk termokimia kuantitatif. Kasus F₂ ekstrem karena ikatannya lemah dan atomnya padat dengan pasangan elektron bebas yang saling tolak. Pelajarannya: korelasi elektron bukan koreksi kecil yang dapat diabaikan dalam kimia, melainkan bagian yang menentukan untuk energi ikatan, energi aktivasi, dan seluruh gaya dispersi (subbab 8.10).
:::

::: {.contoh}
**Contoh 9.35 · Berilium: korelasi statis**

Pada berilium, selisih energi orbital 2s dan 2p kecil, sehingga konfigurasi $1s^2 2p^2$ ($^1$S) bercampur dengan $1s^2 2s^2$. Energi HF berilium $-14{,}5730\ E_h$, fungsi dua konfigurasi yang dioptimumkan (MCSCF) memberi $-14{,}6169\ E_h$, dan energi eksak $-14{,}6674\ E_h$. (a) Berapa bagian energi korelasi yang ditangkap oleh satu konfigurasi tambahan? (b) Bandingkan dengan neon, yang energi korelasinya empat kali lebih besar tetapi dengan fungsi dua konfigurasi hanya memperoleh sebagian kecil.

**Penyelesaian.** (a) $E_\text{kor} = -0{,}0943\ E_h$. Fungsi dua konfigurasi memperoleh $-14{,}6169 + 14{,}5730 = -0{,}0439\ E_h$, atau 46%.

(b) Pada neon tidak ada orbital kosong yang dekat dengan orbital terisi; korelasinya tersebar atas sangat banyak eksitasi ganda yang masing-masing kecil (korelasi dinamis), sehingga tidak ada satu konfigurasi pun yang dominan.

**Memahami hasil.** Separuh energi korelasi berilium berasal dari satu konfigurasi saja: tanda korelasi statis. Secara fisika, campuran $2s^2$ dan $2p^2$ memungkinkan kedua elektron valensi berada di sisi berlawanan dari inti (korelasi sudut), karena orbital 2s + λ2p dan 2s − λ2p menunjuk ke arah berlawanan. Gagasan yang sama muncul pada hibridisasi sp berilium dalam BeH₂ (subbab 12.3), dan pada molekul yang ikatannya diregangkan.
:::

::: {.contoh}
**Contoh 9.36 · Disosiasi H₂ dalam satu determinan**

Dalam metode HF terbatas (RHF), kedua elektron H₂ menempati orbital ikatan $\sigma_g = (a + b)/\sqrt2$, dengan $a$ dan $b$ orbital 1s pada kedua inti. Pada jarak sangat jauh, fungsi ruangnya $\sigma_g(1)\sigma_g(2) = \tfrac12[a_1a_2 + b_1b_2] + \tfrac12[a_1b_2 + b_1a_2]$. (a) Tafsirkan kedua bagian. (b) Hitung energi RHF pada jarak tak hingga, dengan energi H⁻ "beku" (dua elektron di 1s hidrogen) $-1 + \tfrac58 = -0{,}375\ E_h$. (c) Bandingkan dengan energi dua atom H yang benar.

**Penyelesaian.** (a) Bagian pertama **ionik** (kedua elektron pada inti yang sama: H⁻ + H⁺), bagian kedua **kovalen** (satu elektron pada setiap inti: H + H), masing-masing dengan bobot 50%.

(b) Pada jarak tak hingga kedua bagian tidak berinteraksi, sehingga energinya rata-rata berbobot: $\tfrac12(-0{,}375) + \tfrac12(-1{,}000) = -0{,}6875\ E_h$.

(c) Dua atom H: $-1{,}000\ E_h$. RHF salah $0{,}3125\ E_h = 8{,}5$ eV.

**Memahami hasil.** Satu determinan memaksa bobot ionik dan kovalen selalu sama, padahal pada jarak jauh fungsi yang benar sepenuhnya kovalen. Kegagalan ini adalah contoh paling jelas korelasi statis, dan penyebab kurva energi potensial RHF naik terlalu tinggi saat ikatan putus. Fungsi dua konfigurasi $c_1\sigma_g^2 - c_2\sigma_u^2$ memperbaikinya sepenuhnya, karena pengurangan $\sigma_u^2$ menghapus bagian ionik; ini juga titik temu antara teori orbital molekul dan teori ikatan valensi (subbab 11.12). Untuk reaksi kimia yang memutus ikatan, metode multikonfigurasi atau metode HF tak terbatas (UHF) diperlukan.
:::

::: {.contoh}
**Contoh 9.37 · Energi ionisasi neon pada tiga tingkat teori**

Energi HF neon $-128{,}5471\ E_h$, energi HF ion Ne⁺ ($^2$P) $-127{,}8178\ E_h$, energi orbital 2p HF $-0{,}8504\ E_h$, dan energi ionisasi terukur 21,56 eV. (a) Hitung energi ionisasi menurut Koopmans dan menurut selisih dua perhitungan HF (ΔSCF). (b) Pisahkan galat Koopmans menjadi relaksasi dan korelasi. (c) Berapa energi korelasi Ne⁺?

**Penyelesaian.** (a) Koopmans: $0{,}8504\ E_h = 23{,}14$ eV. ΔSCF: $-127{,}8178 + 128{,}5471 = 0{,}7293\ E_h = 19{,}84$ eV.

(b) Relaksasi: $23{,}14 - 19{,}84 = 3{,}30$ eV (menurunkan energi ionisasi). Korelasi: $21{,}56 - 19{,}84 = 1{,}72$ eV (menaikkannya kembali).

(c) $E(\text{Ne}^+)$ eksak $= -128{,}9376 + 21{,}56/27{,}211 = -128{,}1451\ E_h$, sehingga $E_\text{kor}(\text{Ne}^+) = -128{,}1451 + 127{,}8178 = -0{,}327\ E_h$, dibandingkan $-0{,}391\ E_h$ untuk Ne.

**Memahami hasil.** Mencabut satu elektron 2p menghapus beberapa pasangan elektron, sehingga ion mempunyai energi korelasi $0{,}063\ E_h$ (1,7 eV) lebih kecil daripada atom netral. Inilah sebabnya ΔSCF, yang memperhitungkan relaksasi tetapi tidak korelasi, terlalu rendah, sedangkan Koopmans, yang mengabaikan keduanya, terlalu tinggi; kebetulan kedua galat Koopmans sebagian saling menghapus. Dalam kimia komputasi, energi ionisasi dan afinitas elektron yang teliti (galat di bawah 0,1 eV) memerlukan metode berkorelasi seperti coupled cluster, karena selisih energi korelasi antara spesies dengan jumlah elektron berbeda tidak pernah dapat diabaikan.
:::

::: {.kuis}
**Kuis cepat 9.10**

(a) Mengapa energi korelasi selalu negatif? (b) Mengapa elektron berspin sejajar menyumbang lebih sedikit energi korelasi daripada elektron berspin berlawanan? (c) Gaya dispersi London termasuk korelasi dinamis atau statis?
:::

