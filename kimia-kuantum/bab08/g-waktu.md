## 8.11 Perturbasi bergantung waktu; interaksi radiasi dan materi

### Dari tingkat energi ke transisi

Sejauh ini perturbasi tidak bergantung waktu, dan pertanyaan kita adalah: bagaimana tingkat-tingkat energi bergeser? Dalam spektroskopi pertanyaannya lain. Gelombang cahaya adalah medan listrik yang berosilasi, $\hat H'(t)$ berubah terhadap waktu, dan yang kita ingin ketahui adalah: bila molekul mula-mula berada pada keadaan $i$, berapa peluang ia ditemukan pada keadaan $f$ setelah disinari selama waktu $t$? Untuk menjawabnya kita perlu persamaan Schrödinger bergantung waktu (subbab 3.2).

Misalkan $\hat H = \hat H^{(0)} + \hat H'(t)$, dengan keadaan stasioner tak terganggu $\Psi_n^{(0)} = \psi_ne^{-iE_nt/\hbar}$. Karena fungsi-fungsi itu lengkap, keadaan sistem pada setiap saat dapat diuraikan sebagai

$$
\Psi(t) = \sum_nc_n(t)\,\psi_n\,e^{-iE_nt/\hbar} . \qquad \text{(8.51)}
$$

Tanpa perturbasi, setiap $c_n$ tetap (keadaan stasioner hanya berputar fase). Dengan perturbasi, koefisien-koefisien berubah perlahan, dan $|c_n(t)|^2$ adalah peluang menemukan sistem pada keadaan $n$ saat $t$.

### Persamaan untuk koefisien

Masukkan (8.51) ke $i\hbar\,\partial\Psi/\partial t = (\hat H^{(0)} + \hat H')\Psi$. Turunan waktu mengenai $c_n$ dan faktor fase:

$$
\sum_n\left(i\hbar\dot c_n + E_nc_n\right)\psi_ne^{-iE_nt/\hbar} = \sum_nc_n\left(E_n + \hat H'\right)\psi_ne^{-iE_nt/\hbar} .
$$

Suku $E_nc_n$ di kedua ruas saling menghapus: bagian $\hat H^{(0)}$ hanya menghasilkan putaran fase yang sudah dipisahkan. Kalikan dari kiri dengan $\psi_m^*$ dan integralkan; ortonormalitas menyisakan satu suku di ruas kiri:

$$
i\hbar\,\dot c_m(t) = \sum_nc_n(t)\,H'_{mn}(t)\,e^{i\omega_{mn}t} , \qquad \omega_{mn} = \frac{E_m - E_n}{\hbar} . \qquad \text{(8.52)}
$$

Persamaan ini **eksak**: ia hanya menulis ulang persamaan Schrödinger dalam basis keadaan tak terganggu. Ia berupa sistem persamaan diferensial terkopel, satu untuk setiap keadaan, yang umumnya tidak dapat diselesaikan dalam bentuk tertutup.

### Penyelesaian orde pertama

Misalkan sistem mula-mula pasti berada pada keadaan $i$: $c_i(0) = 1$ dan $c_n(0) = 0$ untuk $n \ne i$. Bila perturbasi lemah, koefisien-koefisien hampir tidak berubah selama selang waktu yang ditinjau, sehingga di ruas kanan (8.52) kita boleh memakai nilai awalnya: $c_n \approx \delta_{ni}$. Persamaan untuk keadaan akhir $f \ne i$ menjadi $i\hbar\dot c_f = H'_{fi}(t)e^{i\omega_{fi}t}$, yang langsung dapat diintegralkan:

$$
c_f(t) \approx \frac{1}{i\hbar}\int_0^tH'_{fi}(t')\,e^{i\omega_{fi}t'}\,dt' , \qquad P_{i\to f}(t) = |c_f(t)|^2 . \qquad \text{(8.53)}
$$

Peluang transisi pada orde pertama adalah kuadrat mutlak "transformasi Fourier" unsur matriks perturbasi pada frekuensi Bohr $\omega_{fi}$. Perturbasi yang berubah lambat dibandingkan $1/\omega_{fi}$ hampir tidak menyebabkan transisi; perturbasi yang mengandung komponen frekuensi $\omega_{fi}$ menyebabkan transisi secara efisien.

### Perturbasi harmonik dan syarat resonansi

Gelombang cahaya dengan panjang gelombang jauh lebih besar daripada molekul (cahaya tampak: 400–700 nm, molekul: kurang dari 1 nm) praktis seragam di seluruh molekul. Medan listriknya $F(t) = F_0\cos\omega t$ sepanjang $z$, dan perturbasinya (pendekatan dipol)

$$
\hat H'(t) = -\hat\mu_zF_0\cos\omega t = -\frac{\hat\mu_zF_0}{2}\left(e^{i\omega t} + e^{-i\omega t}\right) .
$$

Masukkan ke (8.53); dengan $\mu_{fi} = \langle f|\hat\mu_z|i\rangle$, integral eksponensialnya elementer:

$$
c_f(t) = \frac{\mu_{fi}F_0}{2\hbar}\left[\frac{e^{i(\omega_{fi} + \omega)t} - 1}{\omega_{fi} + \omega} + \frac{e^{i(\omega_{fi} - \omega)t} - 1}{\omega_{fi} - \omega}\right] .
$$

Untuk serapan, $E_f > E_i$ dan $\omega_{fi} > 0$. Bila frekuensi cahaya dekat $\omega_{fi}$, penyebut suku kedua hampir nol dan suku itu jauh lebih besar daripada suku pertama, yang dapat diabaikan (**pendekatan gelombang berputar**). Dengan $|e^{ix} - 1|^2 = 4\sin^2(x/2)$:

$$
P_{i\to f}(t) = \frac{|\mu_{fi}|^2F_0^2}{\hbar^2}\,\frac{\sin^2[(\omega_{fi} - \omega)t/2]}{(\omega_{fi} - \omega)^2} . \qquad \text{(8.54)}
$$

Rumus ini memuat seluruh dasar spektroskopi:

1. **Syarat resonansi.** Peluang besar hanya bila $\omega \approx \omega_{fi}$, yaitu $\hbar\omega \approx E_f - E_i$. Syarat frekuensi Bohr, yang di Bab 1 dipostulatkan, kini diturunkan dari persamaan Schrödinger.
2. **Momen dipol transisi.** Peluang sebanding dengan $|\mu_{fi}|^2$. Bila $\mu_{fi} = 0$, transisi tidak terjadi pada orde pertama, berapa pun kuatnya cahaya: transisi itu **terlarang** (subbab 8.12).
3. **Intensitas.** Peluang sebanding dengan $F_0^2$, yaitu dengan intensitas cahaya.
4. **Emisi terangsang.** Bila $E_f < E_i$, suku pertama yang resonan pada $\omega \approx -\omega_{fi} = \omega_{if}$, dan rumusnya sama. Cahaya yang menyebabkan serapan $i \to f$ dengan peluang yang sama menyebabkan emisi $f \to i$. Inilah dasar laser (subbab 15.10).
5. **Ketidakpastian energi–waktu.** Fungsi $\sin^2(\Delta t/2)/\Delta^2$, dengan $\Delta = \omega_{fi} - \omega$, berpuncak di $\Delta = 0$ dengan tinggi $t^2/4$ dan lebar sekitar $2\pi/t$. Interaksi yang singkat tidak dapat membedakan frekuensi dengan tajam: $\Delta E\cdot t \sim h$.

### Melampaui orde pertama: osilasi Rabi

Tepat pada resonansi, (8.54) memberi $P = |\mu_{fi}|^2F_0^2t^2/4\hbar^2$, yang tumbuh tanpa batas dan akhirnya melampaui 1. Itu tanda bahwa pendekatan $c_i \approx 1$ sudah runtuh. Untuk sistem dua tingkat, (8.52) dengan pendekatan gelombang berputar dapat diselesaikan eksak. Hasilnya, dengan **frekuensi Rabi** $\Omega = |\mu_{fi}|F_0/\hbar$ dan penalaan $\delta = \omega - \omega_{fi}$:

$$
P_{i\to f}(t) = \frac{\Omega^2}{\Omega^2 + \delta^2}\,\sin^2\!\left(\frac{\sqrt{\Omega^2 + \delta^2}}{2}\,t\right) . \qquad \text{(8.55)}
$$

Pada resonansi, populasi berayun penuh antara kedua keadaan dengan periode $2\pi/\Omega$: **osilasi Rabi**. Pulsa yang lamanya $\pi/\Omega$ (**pulsa $\pi$**) memindahkan seluruh populasi ke keadaan atas; pulsa $\pi/2$ menghasilkan superposisi setara. Untuk $\Omega t \ll 1$, (8.55) kembali ke rumus orde pertama. Di luar resonansi, osilasinya lebih cepat tetapi tidak pernah lengkap.

::: {.inti}
**Perturbasi bergantung waktu orde pertama**

$$
c_f(t) = \frac{1}{i\hbar}\int_0^tH'_{fi}(t')e^{i\omega_{fi}t'}dt' , \qquad P_{i\to f} = \frac{|\mu_{fi}|^2F_0^2}{\hbar^2}\frac{\sin^2[(\omega_{fi} - \omega)t/2]}{(\omega_{fi} - \omega)^2} .
$$

Transisi memerlukan resonansi ($\hbar\omega \approx E_f - E_i$) dan momen dipol transisi tak nol. Untuk medan kuat atau waktu lama, populasi dua tingkat berosilasi dengan frekuensi Rabi $\Omega = |\mu_{fi}|F_0/\hbar$.
:::

### Perubahan mendadak dan perubahan lambat

Dua kasus batas lain sangat berguna dalam kimia. Bila Hamiltonian berubah **mendadak**, jauh lebih cepat daripada periode gerak sistem, fungsi gelombang tidak sempat berubah: tepat setelah perubahan, sistem masih berada dalam keadaan lama $\psi_i^\text{lama}$, yang sekarang harus diuraikan dalam fungsi-fungsi eigen Hamiltonian baru. Peluang menemukan sistem pada keadaan baru $f$ adalah $|\langle\psi_f^\text{baru}|\psi_i^\text{lama}\rangle|^2$ (**pendekatan mendadak**). Contohnya: ionisasi oleh foton sinar-X, yang mencabut elektron dalam waktu attodetik dan membuat elektron lain "terguncang" ke keadaan tereksitasi (satelit *shake-up* pada spektrum fotoelektron), dan peluruhan radioaktif.

Sebaliknya, bila Hamiltonian berubah **sangat lambat**, sistem yang mula-mula pada keadaan eigen ke-$n$ tetap pada keadaan eigen ke-$n$ Hamiltonian sesaat (**teorema adiabatik**). Pendekatan Born–Oppenheimer (subbab 11.1) bertumpu pada teorema ini: inti bergerak lambat, sehingga elektron selalu menyesuaikan diri dengan posisi inti sesaat. Kasus di antaranya, ketika dua kurva energi potensial saling mendekat dan inti melewati daerah itu dengan kecepatan tertentu, ditangani oleh rumus Landau–Zener dan menentukan hasil banyak reaksi fotokimia.

::: {.contoh}
**Contoh 8.52 · Peluruhan beta tritium**

Inti tritium (³H) meluruh menjadi ³He dengan memancarkan elektron cepat dan antineutrino dalam waktu jauh lebih singkat daripada periode orbit elektron atom. Muatan inti melompat dari $Z = 1$ ke $Z = 2$, sedangkan elektron atom mula-mula di 1s hidrogen. (a) Hitung peluang ion ³He⁺ yang terbentuk berada pada 1s, dengan $\langle 1s_{Z_1}|1s_{Z_2}\rangle = 8(Z_1Z_2)^{3/2}/(Z_1 + Z_2)^3$. (b) Peluang pada 2s ternyata tepat $\tfrac14$. Berapa peluang ke keadaan lain (termasuk ionisasi)? (c) Berapa energi rata-rata elektron setelah peluruhan?

**Penyelesaian.** (a) $\langle 1s_1|1s_2\rangle = 8(2)^{3/2}/3^3 = 0{,}8381$, sehingga $P(1s) = 0{,}7023 = 512/729$.

(b) $P(2s) = 0{,}25$. Sisanya $1 - 0{,}7023 - 0{,}25 = 0{,}0477$, tersebar ke $ns$ dengan $n \ge 3$ dan ke kontinu. Hanya keadaan s yang terisi, karena fungsi awal bersimetri bola dan perubahan muatan tidak merusak simetri itu.

(c) Energi rata-rata adalah nilai harap Hamiltonian baru dalam fungsi lama: $\langle 1s_1|-\tfrac12\nabla^2 - 2/r|1s_1\rangle = \tfrac12 - 2 = -1{,}5\ E_h$, di atas keadaan dasar He⁺ ($-2\ E_h$) sebesar $0{,}5\ E_h$.

**Memahami hasil.** Hampir 30% ion helium terbentuk dalam keadaan tereksitasi. Bila tritium terikat dalam molekul, misalnya CH₃T, perubahan mendadak itu memutus ikatan: CH₃He⁺ tidak stabil, dan sebagian besar ion yang terbentuk terfragmentasi. Peluang yang sama menentukan bentuk spektrum elektron beta di dekat titik akhirnya, yang dipakai dalam percobaan pengukuran massa neutrino (KATRIN): ketelitian percobaan itu bergantung pada perhitungan kimia kuantum tentang keadaan akhir molekul T₂ setelah peluruhan.
:::

::: {.contoh}
**Contoh 8.53 · Laser dan kejenuhan transisi**

Laser kontinu berintensitas $1{,}0$ W/cm² disetel tepat pada garis D natrium (589 nm), yang momen dipol transisinya $2{,}49\ ea_0$. (a) Hitung amplitudo medan listrik, $F_0 = \sqrt{2I/c\varepsilon_0}$. (b) Hitung frekuensi Rabi dan lama pulsa $\pi$. (c) Bandingkan dengan umur keadaan 3p (16,2 ns). Kapan teori perturbasi orde pertama berlaku?

**Penyelesaian.** (a) $I = 1{,}0 \times 10^4$ W/m², $F_0 = \sqrt{2(10^4)/(3{,}00 \times 10^8 \times 8{,}854 \times 10^{-12})} = 2{,}74 \times 10^3$ V/m.

(b) $\mu_{fi} = 2{,}49 \times 8{,}478 \times 10^{-30} = 2{,}11 \times 10^{-29}$ C m. $\Omega = \mu_{fi}F_0/\hbar = 5{,}5 \times 10^8$ rad/s; periode Rabi $2\pi/\Omega = 11{,}4$ ns; pulsa $\pi$: 5,7 ns.

(c) Periode Rabi lebih pendek daripada umur keadaan atas. Rumus orde pertama hanya berlaku untuk $t \ll 1/\Omega \approx 2$ ns.

**Memahami hasil.** Laser semacam pointer berdaya rendah yang difokuskan sudah cukup untuk "menjenuhkan" transisi atom yang kuat: populasi atas dan bawah hampir sama, dan serapan tidak lagi bertambah dengan intensitas. Dalam spektroskopi analitik biasa, dengan lampu yang intensitas per satuan frekuensinya jauh lebih kecil, peluang transisi per atom kecil dan teori orde pertama tepat; ini yang membuat hukum Beer–Lambert (subbab 15.2) linear. Dalam resonansi magnetik, osilasi Rabi dikendalikan dengan sengaja: pulsa $\pi/2$ dan $\pi$ adalah bahasa dasar NMR (Bab 16).
:::

::: {.contoh}
**Contoh 8.54 · Pulsa NMR $\pi/2$**

Dalam spektrometer NMR, medan magnet frekuensi radio $B_1$ yang berputar memberi frekuensi Rabi $\Omega = \gamma B_1$ untuk spin inti. Untuk proton, $\gamma = 2{,}675 \times 10^8$ rad s⁻¹ T⁻¹. (a) Bila pulsa $\pi/2$ untuk ¹H berlangsung 10 µs, berapa $\Omega/2\pi$ dan $B_1$? (b) Sebuah proton yang frekuensi resonansinya meleset $\delta = \Omega$ dari frekuensi pemancar: berapa peluang maksimum transisinya?

**Penyelesaian.** (a) Pulsa $\pi/2$: $\Omega t = \pi/2$, jadi $\Omega = \pi/(2 \times 10^{-5}) = 1{,}57 \times 10^5$ rad/s, $\Omega/2\pi = 25$ kHz. $B_1 = \Omega/\gamma = 5{,}9 \times 10^{-4}$ T $= 0{,}59$ mT.

(b) Dari (8.55), $P_\text{maks} = \Omega^2/(\Omega^2 + \delta^2) = \tfrac12$.

**Memahami hasil.** Pulsa sependek 10 µs mempunyai lebar spektrum sekitar puluhan kHz, cukup untuk mengeksitasi semua proton dalam rentang geseran kimia beberapa ppm pada spektrometer 400 MHz (1 ppm = 400 Hz). Proton yang resonansinya jauh dari pusat pulsa tereksitasi kurang sempurna, dan rumus Rabi menentukan seberapa jauh "jendela" eksitasinya. Gagasan yang sama, dengan pulsa laser femtodetik, dipakai untuk mengendalikan reaksi kimia secara koheren.
:::

::: {.contoh}
**Contoh 8.55 · Pulsa ultracepat dan paket gelombang**

Pulsa laser berbentuk Gauss mempunyai hasil kali lebar waktu dan lebar frekuensi (keduanya lebar penuh pada setengah maksimum) $\Delta\nu\,\Delta t = 0{,}441$. Hitung lebar spektrum dalam cm⁻¹ untuk pulsa 10 fs, 100 fs, dan 1 ps, dan bandingkan dengan jarak tingkat getaran I₂ dalam keadaan tereksitasi B (sekitar 120 cm⁻¹) dan jarak garis rotasi (sekitar 0,06 cm⁻¹).

**Penyelesaian.** $\Delta\tilde\nu = 0{,}441/(c\,\Delta t)$: 10 fs → 1471 cm⁻¹; 100 fs → 147 cm⁻¹; 1 ps → 14,7 cm⁻¹.

**Memahami hasil.** Pulsa 10 fs mengeksitasi belasan tingkat getaran sekaligus secara koheren, membentuk **paket gelombang** yang bergerak bolak-balik dalam sumur potensial seperti partikel klasik. Pulsa 100 fs mencakup satu atau dua tingkat getaran; pulsa 1 ps memilih satu tingkat getaran tetapi masih mencakup ratusan garis rotasi. Dengan pulsa femtodetik, Zewail (Nobel Kimia 1999) "memotret" pemutusan ikatan ICN dan NaI ketika sedang terjadi: makin pendek pulsa, makin tajam gambaran waktunya, tetapi makin kabur energinya, sesuai sifat kelima rumus (8.54).
:::

::: {.contoh}
**Contoh 8.56 · Persilangan kurva ionik dan kovalen NaCl**

Pada jarak besar, energi pasangan Na⁺ + Cl⁻ relatif terhadap atom netral Na + Cl adalah $I_\text{Na} - A_\text{Cl} - e^2/4\pi\varepsilon_0R$, dengan $I_\text{Na} = 5{,}139$ eV dan $A_\text{Cl} = 3{,}613$ eV, sedangkan energi pasangan netral hampir nol. (a) Pada jarak berapa kedua kurva bersilangan? (b) Ulangi untuk NaI ($A_\text{I} = 3{,}059$ eV). (c) Apa yang terjadi bila inti melewati persilangan itu dengan lambat atau cepat?

**Penyelesaian.** (a) Kurva bersilangan bila $e^2/4\pi\varepsilon_0R_c = I - A$. Dengan $e^2/4\pi\varepsilon_0 = 14{,}40$ eV Å: $R_c = 14{,}40/1{,}526 = 9{,}44$ Å.

(b) $R_c = 14{,}40/2{,}080 = 6{,}92$ Å.

(c) Kedua keadaan terkopel lemah di persilangan (elektron harus melompat sejauh hampir 1 nm), sehingga kurva-kurva yang sebenarnya saling menghindar dengan celah kecil (Gambar 8.5, kiri). Bila inti bergerak lambat, sistem tetap di kurva adiabatik bawah dan karakternya berubah dari ionik ke kovalen; bila cepat, sistem "melompati" celah dan tetap pada karakter semula.

**Memahami hasil.** Molekul NaCl dalam keadaan dasar bersifat ionik pada jarak kesetimbangan (2,36 Å), tetapi berdisosiasi menjadi atom **netral**, karena di jarak lebih dari 9,4 Å pasangan netral lebih stabil. Dalam percobaan femtokimia Zewail, pulsa laser mengeksitasi NaI ke kurva kovalen; paket gelombang berayun bolak-balik, dan setiap kali melewati persilangan di sekitar 7 Å sebagian kecil "bocor" menjadi atom Na dan I, sehingga atom netral muncul dalam semburan berkala. Peluang lolos setiap lintasan dihitung dengan rumus Landau–Zener, perluasan teori perturbasi bergantung waktu untuk dua keadaan yang selisih energinya berubah terhadap waktu. Mekanisme "harpun" dalam reaksi logam alkali dengan halogen bekerja dengan cara yang sama: elektron melompat pada jarak besar, lalu tarikan Coulomb menarik kedua ion.
:::

![Gambar 8.9 Kiri: peluang transisi sistem dua tingkat terhadap waktu (dalam satuan $1/\Omega$). Garis tebal: osilasi Rabi tepat pada resonansi; garis sedang dan tipis: dengan penalaan $\delta = \Omega$ dan $\delta = 2\Omega$; garis putus-putus: rumus orde pertama, yang hanya berlaku untuk $\Omega t \ll 1$. Kanan: peluang transisi orde pertama terhadap penalaan $\omega - \omega_{fi}$ setelah waktu $t$ dan $2t$; puncak makin tinggi dan sempit ketika waktu bertambah.](fig/c_rabi.png){width=95%}

::: {.kuis}
**Kuis cepat 8.11**

(a) Mengapa pendekatan dipol ($\hat H' = -\hat\mu\cdot\mathbf F$) baik untuk cahaya tampak, tetapi kurang baik untuk sinar-X? (b) Bila intensitas cahaya dilipatduakan, bagaimana peluang transisi orde pertama berubah? Bagaimana frekuensi Rabi berubah? (c) Dalam Contoh 8.52, mengapa peluang ke 2p nol?
:::

## 8.12 Momen dipol transisi, aturan seleksi, aturan emas Fermi

Aturan seleksi atom hidrogen sudah kita pakai sebagai pratinjau di subbab 7.11; sekarang kita menurunkannya dari momen dipol transisi.

### Momen dipol transisi

Rumus (8.54) menunjukkan bahwa kekuatan transisi ditentukan oleh **momen dipol transisi**

$$
\boldsymbol\mu_{fi} = \langle f|\hat{\boldsymbol\mu}|i\rangle = \int\psi_f^*\left(\sum_jq_j\mathbf r_j\right)\psi_i\,d\tau . \qquad \text{(8.56)}
$$

Besaran ini bukan momen dipol keadaan $i$ atau $f$, melainkan ukuran seberapa besar dipol yang berosilasi ketika sistem berada dalam superposisi $c_i\psi_i + c_f\psi_f$. Superposisi seperti itu mempunyai kerapatan muatan yang berayun dengan frekuensi $\omega_{fi}$ (subbab 3.4), dan dipol yang berayun itulah yang berinteraksi dengan medan cahaya, sebagaimana antena. Bila kerapatan superposisi berayun tanpa menggeser pusat muatan, $\boldsymbol\mu_{fi} = 0$ dan cahaya tidak dapat "memegang" transisi itu.

### Aturan seleksi dari simetri

Momen dipol transisi sering nol karena alasan simetri saja, tanpa perlu menghitung integral. Hasilnya adalah **aturan seleksi**: daftar transisi yang diizinkan ($\boldsymbol\mu_{fi} \ne 0$) dan yang terlarang. Beberapa sudah kita jumpai; sekarang semuanya dapat dilihat dari satu sudut pandang.

**Partikel dalam kotak.** Terhadap titik tengah kotak, $\psi_n$ genap untuk $n$ ganjil dan ganjil untuk $n$ genap, sedangkan $x - L/2$ ganjil. Integran $\psi_m(x - L/2)\psi_n$ genap, dan integralnya dapat tidak nol, hanya bila $\psi_m$ dan $\psi_n$ berparitas berlawanan: $\Delta n = m - n$ **ganjil**.

**Osilator harmonik.** $x = \sqrt{\hbar/2m\omega}(\hat a + \hat a^\dagger)$ hanya menaikkan atau menurunkan satu tingkat, sehingga $\Delta v = \pm1$ (subbab 5.8).

**Rotor tegar.** Komponen dipol molekul linear dalam kerangka laboratorium sebanding dengan $\cos\theta$ atau $\sin\theta\,e^{\pm i\phi}$, dan $\cos\theta\,Y_J^M$ adalah kombinasi $Y_{J+1}^M$ dan $Y_{J-1}^M$, sehingga $\Delta J = \pm1$ (subbab 6.10). Molekul juga harus mempunyai momen dipol permanen.

**Atom hidrogen dan atom lain.** Komponen-komponen $\mathbf r$ dapat ditulis $z = r\cos\theta$ dan $x \pm iy = r\sin\theta\,e^{\pm i\phi}$. Integral atas $\phi$, $\int_0^{2\pi}e^{-im'\phi}e^{iq\phi}e^{im\phi}d\phi$ dengan $q = 0, \pm1$, nol kecuali $m' = m + q$; jadi $\Delta m = 0, \pm1$. Integral atas $\theta$ memakai rumus rekursi harmonik bola, yang menyatakan $\cos\theta\,Y_\ell^m$ dan $\sin\theta\,e^{\pm i\phi}Y_\ell^m$ sebagai kombinasi harmonik dengan $\ell \pm 1$ saja; jadi

$$
\Delta\ell = \pm1 , \qquad \Delta m = 0, \pm1 , \qquad \Delta n \text{ sembarang} . \qquad \text{(8.57)}
$$

Aturan $\Delta\ell = \pm1$ mudah diingat: foton membawa satu satuan momentum sudut, sehingga momentum sudut atom harus berubah satu satuan. Transisi s → s, p → p, d → s terlarang; s → p, p → d diizinkan.

**Aturan Laporte.** Dalam atom atau molekul yang mempunyai pusat inversi, setiap keadaan genap (*gerade*, g) atau ganjil (*ungerade*, u) terhadap inversi, sedangkan $\hat{\boldsymbol\mu}$ ganjil. Maka hanya transisi **g ↔ u** yang diizinkan; g → g dan u → u terlarang. Ini aturan yang membuat transisi d–d ion logam transisi dalam kompleks oktahedral lemah: semua orbital d genap. Kompleks [Ti(H₂O)₆]³⁺ berwarna ungu pucat, dengan koefisien absorpsi molar sekitar 5 L mol⁻¹ cm⁻¹, sedangkan transisi transfer muatan yang diizinkan (misalnya pada ion permanganat) mempunyai koefisien ribuan kali lebih besar. Transisi d–d tetap teramati lemah karena getaran molekul sesaat merusak pusat inversi (Bab 14).

**Spin.** Operator dipol tidak menyentuh koordinat spin, sehingga $\boldsymbol\mu_{fi}$ memuat faktor tumpang tindih fungsi spin, yang nol bila spin total berubah: $\Delta S = 0$. Transisi singlet ↔ triplet terlarang. Inilah sebabnya keadaan $2^3$S helium hidup ribuan detik (Contoh 8.44) dan sebabnya fosforesensi (pancaran triplet → singlet) jauh lebih lambat daripada fluoresensi. Larangan ini dilonggarkan oleh kopling spin–orbit (subbab 9.13), yang kuat pada atom berat.

::: {.awas}
**"Terlarang" berarti "lemah", bukan "mustahil"**

Aturan seleksi diturunkan dengan beberapa pendekatan: dipol listrik (gelombang cahaya dianggap seragam), orde pertama, dan fungsi gelombang dengan simetri ideal. Bila pendekatan itu dilonggarkan, transisi "terlarang" muncul dengan intensitas kecil: melalui dipol magnet atau kuadrupol listrik (sekitar $10^{-5}$ sampai $10^{-8}$ kali transisi dipol listrik), melalui kopling dengan getaran (transisi d–d, pita benzena di 260 nm), atau melalui kopling spin–orbit (fosforesensi). Garis hijau 557,7 nm aurora berasal dari transisi terlarang atom oksigen yang hanya dapat muncul di atmosfer atas yang sangat renggang, karena di udara padat atom tereksitasi itu bertumbukan sebelum sempat memancar.
:::

::: {.contoh}
**Contoh 8.57 · Aturan seleksi atom hidrogen**

Dari keadaan $n = 3$ hidrogen (3s, 3p, 3d), transisi pancaran ke tingkat mana yang diizinkan? Garis Balmer-α (656 nm) terdiri atas transisi apa saja?

**Penyelesaian.** Dengan $\Delta\ell = \pm1$: 3s → 2p (diizinkan); 3s → 2s, 1s (terlarang). 3p → 2s dan 3p → 1s (diizinkan). 3d → 2p (diizinkan); 3d → 2s, 1s (terlarang). Balmer-α ($n = 3 \to 2$) terdiri atas tiga komponen: 3s → 2p, 3p → 2s, dan 3d → 2p.

**Memahami hasil.** Elektron di 3d tidak dapat langsung turun ke 1s; ia harus singgah di 2p dulu. Keadaan 2s sendiri tidak mempunyai jalan dipol listrik ke 1s ($\Delta\ell = 0$), sehingga ia **metastabil**: dalam ruang hampa ia meluruh dengan memancarkan dua foton sekaligus, dengan umur sekitar 0,12 s, sekitar $10^8$ kali umur 2p. Dalam alam semesta awal, peluruhan dua foton 2s → 1s adalah salah satu jalan utama atom hidrogen terbentuk dari plasma, sebuah aturan seleksi yang ikut menentukan sejarah kosmos.
:::

::: {.contoh}
**Contoh 8.58 · Zat warna sianin: transisi yang sangat kuat**

Dalam model elektron bebas, kation sianin dengan 8 elektron π mempunyai $L = 1{,}112$ nm (subbab 3.8). (a) Apakah transisi HOMO ($n = 4$) → LUMO ($n = 5$) diizinkan? (b) Hitung $\langle 4|x|5\rangle = 8L(4)(5)/[\pi^2(25 - 16)^2]$ dan momen dipol transisinya. Dengan dua elektron di HOMO, momen dipol transisi singlet adalah $\sqrt2\,e|\langle 4|x|5\rangle|$. (c) Bandingkan dengan transisi HOMO → $n = 6$.

**Penyelesaian.** (a) $\Delta n = 1$, ganjil: diizinkan.

(b) $\langle 4|x|5\rangle = 160L/81\pi^2 = 0{,}2001L = 0{,}223$ nm. $e \times 0{,}223$ nm $= 3{,}57 \times 10^{-29}$ C m $= 10{,}7$ D; dikali $\sqrt2$: 15,1 D.

(c) $\Delta n = 2$, genap: terlarang.

**Memahami hasil.** Momen dipol transisi 15 D sangat besar; ia sebanding dengan muatan elektron yang dipindahkan sejauh seperlima panjang molekul. Itulah sebabnya zat warna sianin termasuk penyerap terkuat yang dikenal, dengan koefisien absorpsi molar di atas $10^5$ L mol⁻¹ cm⁻¹. Momen dipol transisi tumbuh sebanding dengan panjang rantai, sehingga zat warna yang lebih panjang tidak hanya menyerap pada panjang gelombang lebih besar tetapi juga lebih kuat. Kekuatan osilator yang diramalkan model (lihat di bawah) sekitar 2,4, kira-kira dua kali nilai terukur yang berorde 1; model elektron bebas melebih-lebihkan delokalisasi.
:::

### Aturan emas Fermi

Rumus (8.54) menggambarkan transisi ke satu keadaan akhir yang tajam. Dalam banyak situasi penting, keadaan akhir membentuk **kontinu** atau pita yang sangat rapat: elektron yang dilepaskan pada ionisasi dapat mempunyai energi kinetik berapa saja, molekul dalam larutan mempunyai tingkat getaran pelarut yang tak terhitung, dan cahaya lampu mengandung frekuensi yang menyebar. Dalam situasi itu yang bermakna adalah **laju** transisi total ke semua keadaan akhir di sekitar energi tertentu.

Misalkan perturbasi tetap $\hat H'$ dinyalakan pada $t = 0$. Dari (8.53), $c_f = H'_{fi}(1 - e^{i\omega_{fi}t})/\hbar\omega_{fi}$, sehingga

$$
P_{i\to f}(t) = \frac{|H'_{fi}|^2}{\hbar^2}\,\frac{\sin^2(\omega_{fi}t/2)}{(\omega_{fi}/2)^2} .
$$

Misalkan $\rho(E)$ adalah **kerapatan keadaan** akhir: jumlah keadaan per satuan energi. Peluang total transisi ke selang energi di sekitar $E_i$ adalah

$$
P(t) = \int\frac{|H'_{fi}|^2}{\hbar^2}\,\frac{\sin^2(\omega_{fi}t/2)}{(\omega_{fi}/2)^2}\,\rho(E_f)\,dE_f .
$$

Untuk $t$ yang cukup besar, fungsi $\sin^2(xt/2)/(x/2)^2$ sangat tajam di $x = 0$, dengan lebar sekitar $2\pi/t$, sementara $|H'_{fi}|^2$ dan $\rho$ berubah perlahan. Keduanya dapat dikeluarkan dari integral dan dievaluasi di $E_f = E_i$. Dengan $dE_f = \hbar\,d\omega_{fi}$ dan integral baku

$$
\int_{-\infty}^\infty\frac{\sin^2(xt/2)}{(x/2)^2}\,dx = 2\pi t ,
$$

diperoleh $P(t) = (2\pi/\hbar)|H'_{fi}|^2\rho(E_i)\,t$. Peluang tumbuh **linear** terhadap waktu, sehingga lajunya tetap:

$$
W_{i\to f} = \frac{dP}{dt} = \frac{2\pi}{\hbar}\,|H'_{fi}|^2\,\rho(E_f)\Big|_{E_f = E_i} . \qquad \text{(8.58)}
$$

Inilah **aturan emas Fermi**: laju transisi sama dengan $2\pi/\hbar$ dikali kuadrat unsur matriks kopling dikali kerapatan keadaan akhir pada energi yang sama. Dengan perturbasi harmonik, $E_f = E_i$ diganti $E_f = E_i + \hbar\omega$ untuk serapan.

Penerapan pada radiasi yang tersebar dalam frekuensi (misalnya cahaya lampu atau radiasi termal) dengan kerapatan energi $\rho_\omega(\omega)$ per satuan frekuensi sudut, dan pada molekul yang berorientasi acak, memberi laju serapan

$$
W_{i\to f} = \frac{\pi|\boldsymbol\mu_{fi}|^2}{3\varepsilon_0\hbar^2}\,\rho_\omega(\omega_{fi}) , \qquad \text{(8.59)}
$$

dengan faktor $\tfrac13$ berasal dari perata-rataan arah. Laju ini sebanding dengan kerapatan radiasi; Einstein menyebut koefisiennya koefisien $B$. Dengan menuntut kesetimbangan dengan radiasi benda hitam (subbab 15.1), diperoleh pula laju **pancaran spontan**

$$
A_{f\to i} = \frac{\omega_{fi}^3|\boldsymbol\mu_{fi}|^2}{3\pi\varepsilon_0\hbar c^3} . \qquad \text{(8.60)}
$$

Faktor $\omega^3$ membuat pancaran spontan sangat cepat untuk transisi ultraungu (nanodetik) dan sangat lambat untuk transisi gelombang mikro dan radio (tahun sampai jutaan tahun), satu alasan mengapa laser sinar-X jauh lebih sulit dibuat daripada maser gelombang mikro.

### Kekuatan osilator

Kimiawan sering menyatakan kekuatan transisi dengan bilangan tak berdimensi, **kekuatan osilator**

$$
f_{fi} = \frac{2m_e\omega_{fi}}{3\hbar e^2}\,|\boldsymbol\mu_{fi}|^2 , \qquad \text{(8.61)}
$$

(dalam satuan atom, $f = \tfrac23\Delta E\,|\langle f|\mathbf r|i\rangle|^2$ untuk satu elektron). Namanya berasal dari model klasik elektron pada pegas: transisi dengan $f = 1$ menyerap sekuat satu osilator elektron klasik. **Aturan jumlah Thomas–Reiche–Kuhn** menyatakan bahwa jumlah kekuatan osilator dari satu keadaan ke semua keadaan lain sama dengan jumlah elektron: $\sum_ff_{fi} = N$. Satu elektron mempunyai "anggaran" kekuatan osilator sebesar 1, yang dibagi-bagi di antara semua transisinya. Kekuatan osilator dihubungkan dengan spektrum serapan terukur melalui

$$
f = 4{,}32 \times 10^{-9}\int\varepsilon(\tilde\nu)\,d\tilde\nu , \qquad \text{(8.62)}
$$

dengan $\varepsilon$ koefisien absorpsi molar dalam L mol⁻¹ cm⁻¹ dan $\tilde\nu$ dalam cm⁻¹. Transisi diizinkan mempunyai $f$ sekitar 0,1–1; transisi terlarang spin, $10^{-5}$ atau kurang.

::: {.inti}
**Laju transisi**

- Aturan emas Fermi: $W = (2\pi/\hbar)|H'_{fi}|^2\rho(E_f)$.
- Pancaran spontan: $A = \omega^3|\mu_{fi}|^2/3\pi\varepsilon_0\hbar c^3$; umur $\tau = 1/A$.
- Kekuatan osilator: $f = (2m_e\omega/3\hbar e^2)|\mu_{fi}|^2$; $\sum f = N$; $f = 4{,}32 \times 10^{-9}\int\varepsilon\,d\tilde\nu$.
- Aturan seleksi: $\mu_{fi} = 0$ karena simetri. Atom: $\Delta\ell = \pm1$, $\Delta m = 0, \pm1$; pusat inversi: g ↔ u; spin: $\Delta S = 0$.
:::

::: {.contoh}
**Contoh 8.59 · Umur keadaan 2p hidrogen**

Untuk transisi 2p → 1s hidrogen, $|\langle 1s|z|2p_0\rangle| = 0{,}7449\ a_0$ dan $\Delta E = 0{,}375\ E_h$. (a) Hitung kekuatan osilator serapan 1s → 2p (jumlah ketiga komponen $m$). (b) Hitung $A$ dan umur 2p. (c) Hitung lebar garis alami $A/2\pi$.

**Penyelesaian.** (a) Setiap komponen $2p_m$ terhubung ke 1s oleh satu komponen $\mathbf r$ dengan kuadrat unsur matriks 0,5549. $f = \tfrac23(0{,}375)(3 \times 0{,}5549) = 0{,}416$.

(b) $\omega = 0{,}375 \times 27{,}211\ \text{eV}/\hbar = 1{,}550 \times 10^{16}$ s⁻¹ ($\lambda = 121{,}5$ nm). $|\mu_{fi}|^2 = 0{,}5549(ea_0)^2 = 0{,}5549 \times (8{,}478 \times 10^{-30})^2$ C² m². Dengan (8.60): $A = 6{,}27 \times 10^8$ s⁻¹, $\tau = 1{,}60$ ns.

(c) $A/2\pi = 99{,}8$ MHz.

**Memahami hasil.** Transisi 1s → 2p (Lyman-α) memakai 42% anggaran kekuatan osilator elektron hidrogen; sisanya terbagi ke 1s → 3p (0,079), 1s → 4p (0,029), dan seterusnya, dan sekitar 44% ke kontinu ionisasi. Umur 1,6 ns adalah umur khas keadaan tereksitasi atom yang meluruh dengan transisi ultraungu yang diizinkan. Lebar garis alami 100 MHz sangat kecil dibandingkan frekuensi transisi ($2{,}5 \times 10^{15}$ Hz), sehingga garis atom sangat tajam; pada praktiknya lebar garis ditentukan oleh efek Doppler dan tumbukan (subbab 15.3).
:::

::: {.contoh}
**Contoh 8.60 · Natrium: satu transisi menghabiskan anggaran**

Umur keadaan 3p natrium adalah 16,2 ns, dan garis D berada di 589 nm. (a) Hitung $|\mu_{fi}|$ dari (8.60). (b) Hitung kekuatan osilator serapan 3s → 3p. (c) Tafsirkan dengan aturan jumlah TRK.

**Penyelesaian.** (a) $\omega = 2\pi c/\lambda = 3{,}20 \times 10^{15}$ s⁻¹. Dari $A = 1/\tau = 6{,}16 \times 10^7$ s⁻¹: $|\mu_{fi}|^2 = 3\pi\varepsilon_0\hbar c^3A/\omega^3$, sehingga $|\mu_{fi}| = 2{,}11 \times 10^{-29}$ C m $= 6{,}34$ D $= 2{,}49\ ea_0$.

(b) Untuk serapan dari 3s ke ketiga komponen 3p, $f = 0{,}96$.

(c) Elektron valensi natrium mempunyai anggaran 1 (sepuluh elektron teras hampir tidak terlibat pada energi ini). Transisi 3s → 3p sendiri menghabiskan 96% anggaran itu.

**Memahami hasil.** Hampir seluruh kemampuan elektron valensi natrium menyerap cahaya terpusat pada satu transisi. Itulah sebabnya garis D begitu terang dalam nyala dan lampu jalan, dan mengapa polarisabilitas natrium sangat besar (sekitar 24 Å³, lebih dari seratus kali helium): (8.47) didominasi oleh satu suku dengan momen dipol transisi besar dan energi kecil (2,1 eV). Atom alkali adalah "atom satu transisi" yang ideal, sehingga dipakai luas untuk pendinginan laser dan jam atom.
:::

::: {.contoh}
**Contoh 8.61 · Aturan jumlah untuk partikel dalam kotak**

Untuk elektron dalam kotak (satu dimensi, polarisasi sepanjang kotak), kekuatan osilator didefinisikan $f_{n1} = (2m_e\omega_{n1}/\hbar)|\langle n|x|1\rangle|^2$. (a) Hitung $f_{21}$. (b) Periksa dengan Python bahwa $\sum_nf_{n1} = 1$.

**Penyelesaian.** (a) Dengan $\hbar = m_e = L = 1$: $\omega_{21} = 3\pi^2/2$ dan $|\langle 2|x|1\rangle|^2 = (16/9\pi^2)^2$. Jadi $f_{21} = 2(3\pi^2/2)(256/81\pi^4) = 768/81\pi^2 = 0{,}9607$.

(b) Penjumlahan dengan Python:

```python
import numpy as np
f = 0.0
for n in range(2, 2000, 2):          # hanya n genap diizinkan
    w = (n*n - 1)*np.pi**2/2         # E_n - E_1 (hbar = m = L = 1)
    x = 8*n/(np.pi**2*(n*n - 1)**2)  # |<n|x|1>|
    f += 2*w*x*x
print(f)                             # 0.9999999999
```

**Memahami hasil.** Transisi 1 → 2 sendiri memakai 96% anggaran, dan semua transisi lain berbagi 4% sisanya. Pola ini, satu transisi terendah yang sangat kuat, khas sistem terkonjugasi: transisi HOMO → LUMO zat warna mendominasi spektrumnya, dan polarisabilitasnya (Contoh 8.48) didominasi oleh transisi yang sama. Aturan jumlah TRK sangat berguna untuk memeriksa perhitungan spektrum: bila jumlah kekuatan osilator yang dihitung jauh dari jumlah elektron, basisnya terlalu kecil.
:::

::: {.contoh}
**Contoh 8.62 · Dari kekuatan osilator ke koefisien absorpsi**

Sebuah pita serapan berbentuk Gauss mempunyai lebar penuh pada setengah maksimum 1500 cm⁻¹. Integral Gauss adalah $1{,}0645 \times$ tinggi $\times$ lebar. Berapa koefisien absorpsi molar puncaknya bila (a) $f = 1$ (transisi diizinkan kuat), (b) $f = 10^{-4}$ (transisi d–d atau terlarang)?

**Penyelesaian.** Dari (8.62), $\int\varepsilon\,d\tilde\nu = f/4{,}32 \times 10^{-9}$. (a) $f = 1$: integral $2{,}31 \times 10^8$; $\varepsilon_\text{maks} = 2{,}31 \times 10^8/(1{,}0645 \times 1500) = 1{,}45 \times 10^5$ L mol⁻¹ cm⁻¹. (b) $f = 10^{-4}$: $\varepsilon_\text{maks} = 14{,}5$ L mol⁻¹ cm⁻¹.

**Memahami hasil.** Larutan $10^{-5}$ M zat warna dengan $f = 1$ dalam kuvet 1 cm mempunyai absorbans 1,45: warnanya pekat walaupun konsentrasinya sangat kecil. Kompleks logam transisi dengan transisi d–d memerlukan konsentrasi sekitar $10^{-1}$ M untuk absorbans yang sama, sesuai pengalaman di laboratorium: larutan CuSO₄ 0,1 M hanya biru muda. Satu bilangan, $|\mu_{fi}|^2$, menentukan apakah suatu senyawa cocok sebagai zat warna, sebagai indikator, atau sebagai pigmen.
:::

![Gambar 8.10 Kiri: fungsi $\sin^2(xt/2)/(x/2)^2$ dibagi $2\pi t$, untuk tiga nilai $t$. Puncak makin tinggi dan sempit, sedangkan luasnya tetap satu: untuk waktu panjang fungsi ini menjadi fungsi delta, yang menghasilkan aturan emas Fermi. Kanan: diagram Grotrian atom hidrogen untuk $n \le 3$; garis menghubungkan pasangan tingkat dengan transisi dipol listrik yang diizinkan ($\Delta\ell = \pm1$). Tidak ada garis di dalam satu kolom $\ell$.](fig/c_emas.png){width=95%}

::: {.terapan}
**Aturan emas dalam kimia: transfer elektron**

Laju transfer elektron dari donor D ke akseptor A dalam larutan atau protein dapat ditulis dengan aturan emas: $k = (2\pi/\hbar)|H_{DA}|^2\,\text{(FCWD)}$, dengan $H_{DA}$ unsur matriks kopling elektronik dan FCWD "kerapatan keadaan" berbobot faktor Franck–Condon. Dalam teori Marcus, FCWD $= (4\pi\lambda k_BT)^{-1/2}\exp[-(\Delta G° + \lambda)^2/4\lambda k_BT]$, dengan $\lambda$ energi reorganisasi. Untuk $H_{DA} = 100$ cm⁻¹, $\lambda = 1{,}0$ eV, $\Delta G° = -0{,}5$ eV, dan 298 K, rumus ini memberi $k \approx 2 \times 10^{11}$ s⁻¹. Karena $|H_{DA}|^2$ meluruh eksponensial dengan jarak donor–akseptor, laju turun sekitar sepuluh kali setiap 1,5–2 Å di dalam protein. Pemisahan muatan dalam fotosintesis, respirasi, dan sel surya organik semuanya dirancang (oleh evolusi atau oleh kimiawan) dengan menyetel ketiga besaran dalam aturan emas ini.
:::

::: {.kuis}
**Kuis cepat 8.12**

(a) Manakah transisi dipol listrik yang diizinkan pada atom: 2s → 3d, 2p → 3d, 3p → 4f, 4f → 3d? (b) Ion [Co(H₂O)₆]²⁺ berwarna merah muda pucat, sedangkan [CoCl₄]²⁻ biru tua. Kompleks mana yang mempunyai pusat inversi, dan bagaimana hal itu menjelaskan perbedaan intensitas warnanya? (c) Mengapa pancaran spontan pada transisi gelombang mikro (misalnya garis 21 cm hidrogen) sangat lambat?
:::

### Menuju bab berikutnya

Metode pendekatan memberi energi atom helium dengan baik, tetapi masih ada satu unsur yang hilang: spin elektron dan asas Pauli. Bab 9 melengkapinya dan menjelaskan susunan tabel periodik.
