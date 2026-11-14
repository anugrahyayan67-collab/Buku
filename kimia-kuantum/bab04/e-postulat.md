## 4.13 Postulat mekanika kuantum

Seperti geometri Euklides yang dibangun di atas beberapa aksioma, mekanika kuantum (tanpa relativitas) dapat dirangkum dalam beberapa postulat. Postulat-postulat ini tidak dibuktikan; mereka dibenarkan oleh kecocokan semua ramalannya dengan percobaan, dari spektrum hidrogen sampai panjang ikatan molekul protein.

::: {.inti}
**Postulat 1 (keadaan).** Keadaan sistem dinyatakan sepenuhnya oleh fungsi gelombang $\Psi(q, t)$ yang bergantung pada koordinat semua partikel (termasuk spin) dan waktu. $|\Psi|^2d\tau$ adalah peluang konfigurasi partikel berada dalam elemen volume $d\tau$. $\Psi$ harus berperilaku baik (subbab 4.7).

**Postulat 2 (teramati).** Setiap besaran fisis yang dapat diukur dinyatakan oleh operator linear Hermitian. Operatornya dibangun dari ungkapan klasik dengan $\hat x = x$ dan $\hat p_x = -i\hbar\,\partial/\partial x$ (koordinat Kartesius); besaran tanpa padanan klasik (spin) didefinisikan tersendiri.

**Postulat 3 (hasil pengukuran).** Hasil pengukuran besaran $A$ hanya dapat berupa nilai eigen $\hat A$.

**Postulat 4 (kelengkapan dan peluang).** Fungsi eigen setiap operator teramati membentuk himpunan lengkap. Jika $\Psi = \sum c_n\phi_n$, peluang pengukuran memberi $a_n$ adalah $|c_n|^2$ (untuk $\Psi$ dan $\phi_n$ ternormalisasi); nilai harapnya $\langle A\rangle = \int\Psi^*\hat A\Psi\,d\tau$.

**Postulat 5 (evolusi waktu).** Selama tidak diukur, keadaan berubah menurut persamaan Schrödinger bergantung waktu, $i\hbar\,\partial\Psi/\partial t = \hat H\Psi$.

**Postulat 6 (reduksi keadaan).** Segera setelah pengukuran yang memberi $a_n$, keadaan sistem adalah fungsi eigen yang bersesuaian (atau proyeksi pada ruang fungsi eigen $a_n$ bila terdegenerasi).

**Postulat 7 (partikel identik, Bab 9).** Fungsi gelombang sistem elektron (atau fermion lain) harus antisimetris terhadap pertukaran dua partikel mana pun.
:::

### Evolusi waktu sebagai operator

Untuk $\hat H$ yang tidak bergantung waktu, Postulat 5 dapat diselesaikan secara formal:

$$
\Psi(t) = e^{-i\hat Ht/\hbar}\,\Psi(0) , \qquad \text{(4.19)}
$$

dengan eksponen operator didefinisikan oleh deret Taylor $e^{\hat A} = 1 + \hat A + \hat A^2/2! + \cdots$ Pada fungsi eigen $\hat H$, $e^{-i\hat Ht/\hbar}\psi_n = e^{-iE_nt/\hbar}\psi_n$, sehingga (4.19) sama dengan resep superposisi di subbab 3.4. Operator evolusi waktu $\hat U(t) = e^{-i\hat Ht/\hbar}$ adalah **uniter** ($\hat U^\dagger\hat U = 1$), yang berarti norma fungsi gelombang (peluang total) kekal.

### Tentang tafsiran

Postulat 6 adalah bagian yang paling banyak diperdebatkan. Tafsiran Kopenhagen (Bohr, Heisenberg) menerima pemisahan antara sistem kuantum dan alat ukur klasik tanpa menjelaskan lebih lanjut. Tafsiran lain (dunia banyak, teori de Broglie–Bohm, keruntuhan spontan) mencoba menghapus atau menjelaskan pemisahan itu. Bagi kimia, semua tafsiran itu memberi ramalan yang sama untuk setiap percobaan yang pernah dilakukan; perbedaan di antara mereka adalah soal filsafat, bukan soal angka. Gagasan dekoherensi (subbab 4.12) menjelaskan secara fisis mengapa superposisi makroskopik tidak teramati, tanpa menyelesaikan seluruh perdebatan.

::: {.contoh}
**Contoh 4.43 · Menerapkan semua postulat pada satu sistem**

Elektron dalam kotak 1,00 nm disiapkan pada $t = 0$ dalam keadaan $\Psi(0) = \tfrac{1}{\sqrt2}(\psi_1 + i\psi_2)$. (a) Tuliskan $\Psi(t)$ (Postulat 5). (b) Hasil apa yang mungkin pada pengukuran energi, dengan peluang berapa (Postulat 3 dan 4)? (c) Berapa $\langle x\rangle$ pada $t = 0$?

**Penyelesaian.** (a) $\Psi(t) = \tfrac{1}{\sqrt2}\left(\psi_1e^{-iE_1t/\hbar} + i\psi_2e^{-iE_2t/\hbar}\right)$ dengan $E_1 = 0{,}376$ eV, $E_2 = 1{,}504$ eV.

(b) $E_1$ atau $E_2$, masing-masing dengan peluang ½.

(c) Suku silang: $\langle x\rangle = \tfrac L2 + \tfrac12\cdot 2\,\text{Re}(1\cdot i)\langle 1|x|2\rangle = \tfrac L2 + 0 = \tfrac L2$.

**Memahami hasil.** Faktor fase relatif $i$ membuat suku silang $\text{Re}(c_1^*c_2) = 0$ pada $t = 0$: partikel tepat di tengah, tetapi sedang bergerak (ke kiri atau kanan, tergantung tanda). Seperempat periode kemudian, fase relatifnya menjadi riil dan partikel berada di salah satu sisi. Fase relatif, bukan hanya besar koefisien, menentukan apa yang terjadi.
:::

::: {.contoh}
**Contoh 4.44 · Evolusi sistem dua keadaan**

Dalam model dua keadaan inversi amonia (subbab 3.12), Hamiltonian dalam basis $\{|\text{A}\rangle, |\text{B}\rangle\}$ adalah $\hat H = \begin{pmatrix}E_0 & -\Delta/2\\ -\Delta/2 & E_0\end{pmatrix}$. Dengan (4.19), mulai dari $|\text{A}\rangle$, tentukan peluang menemukan molekul di $|\text{B}\rangle$ pada waktu $t$.

**Penyelesaian.** Fungsi eigen $\hat H$ adalah $\psi_\pm = (|\text{A}\rangle \pm |\text{B}\rangle)/\sqrt2$ dengan $E_\pm = E_0 \mp \Delta/2$. Karena $|\text{A}\rangle = (\psi_+ + \psi_-)/\sqrt2$:

$$
\Psi(t) = \frac{1}{\sqrt2}\left(\psi_+e^{-iE_+t/\hbar} + \psi_-e^{-iE_-t/\hbar}\right) = e^{-iE_0t/\hbar}\left[\cos\frac{\Delta t}{2\hbar}|\text{A}\rangle + i\sin\frac{\Delta t}{2\hbar}|\text{B}\rangle\right] .
$$

Peluang di $|\text{B}\rangle$: $\sin^2(\Delta t/2\hbar)$.

**Memahami hasil.** Molekul berpindah sepenuhnya ke $|\text{B}\rangle$ pada $t = \pi\hbar/\Delta = h/2\Delta$ dan kembali pada $t = h/\Delta$ (42 ps untuk NH₃). Rumus yang sama, dengan nama **osilasi Rabi**, menggambarkan sistem dua tingkat yang digerakkan medan resonansi: dasar NMR berpulsa (Bab 16), maser, dan bit kuantum.
:::

::: {.kuis}
**Kuis cepat 4.13**

Postulat mana yang menjamin bahwa hasil pengukuran energi atom hidrogen hanya $-13{,}6/n^2$ eV? Postulat mana yang memastikan bahwa pengukuran kedua yang segera dilakukan memberi hasil yang sama?
:::

## 4.14 Notasi Dirac dan representasi matriks

### Ket, bra, dan hasil kali dalam

Paul Dirac memperkenalkan notasi yang memisahkan **keadaan** dari **representasinya**. Keadaan ditulis sebagai **ket** $|\psi\rangle$, sebuah vektor dalam ruang keadaan (ruang Hilbert). Fungsi gelombang $\psi(x)$ adalah salah satu cara menyatakan vektor itu (dalam "representasi posisi"); koefisien $c_n$ dalam basis $\{|n\rangle\}$ adalah cara lain. Pasangannya, **bra** $\langle\phi|$, menyatakan pengambilan hasil kali dalam dengan $|\phi\rangle$. Kurung lengkapnya:

$$
\langle\phi|\psi\rangle = \int\phi^*\psi\,d\tau, \qquad \langle\phi|\hat A|\psi\rangle = \int\phi^*\hat A\psi\,d\tau . \qquad \text{(4.20)}
$$

Kumpulan aturan untuk notasi ini sederhana: $\langle\phi|\psi\rangle^* = \langle\psi|\phi\rangle$; operator Hermitian memenuhi $\langle\phi|\hat A|\psi\rangle^* = \langle\psi|\hat A|\phi\rangle$; dan nilai harap ditulis $\langle A\rangle = \langle\psi|\hat A|\psi\rangle$. Fungsi eigen ortonormal ditulis $|n\rangle$ dengan $\langle m|n\rangle = \delta_{mn}$.

### Relasi kelengkapan

Ekspansi (4.15) dalam notasi Dirac adalah $|\psi\rangle = \sum_n|n\rangle\langle n|\psi\rangle$, dengan $c_n = \langle n|\psi\rangle$. Karena ini berlaku untuk setiap $|\psi\rangle$,

$$
\sum_n|n\rangle\langle n| = \hat 1 . \qquad \text{(4.21)}
$$

"Menyisipkan satu" dalam bentuk ini adalah trik paling berguna dalam perhitungan kuantum. Operator $|n\rangle\langle n|$ sendiri adalah **operator proyeksi** pada keadaan $|n\rangle$.

### Operator sebagai matriks

Dengan menyisipkan (4.21) dua kali, setiap operator dapat dinyatakan oleh bilangan-bilangan

$$
A_{mn} = \langle m|\hat A|n\rangle , \qquad \text{(4.22)}
$$

yaitu **unsur matriks** $\hat A$ dalam basis $\{|n\rangle\}$. Persamaan $\hat A|\psi\rangle = |\phi\rangle$ menjadi perkalian matriks–vektor $\sum_nA_{mn}c_n = d_m$, dan persamaan Schrödinger $\hat H|\psi\rangle = E|\psi\rangle$ menjadi

$$
\sum_nH_{mn}c_n = Ec_m, \qquad \mathbf{Hc} = E\mathbf c . \qquad \text{(4.23)}
$$

Mencari tingkat energi berarti mendiagonalkan matriks Hamiltonian. Matriks operator Hermitian adalah matriks Hermitian. Dalam basis fungsi eigennya sendiri, matriks sebuah operator diagonal, dengan nilai eigen di diagonal. Heisenberg (1925) menemukan mekanika kuantum dalam bentuk matriks ini, beberapa bulan sebelum Schrödinger menemukan persamaan gelombangnya; Schrödinger kemudian membuktikan bahwa keduanya setara.

Dalam praktik, basis yang lengkap tak hingga, sehingga matriksnya dipotong. Hasilnya adalah pendekatan, yang membaik dengan menambah fungsi basis. Inilah **metode variasi linear** (Bab 8), dan inilah yang dilakukan setiap program kimia komputasi.

::: {.contoh}
**Contoh 4.45 · Matriks posisi dalam basis kotak**

Tuliskan matriks $\hat x$ (dalam satuan $L$) dalam basis tiga fungsi kotak terendah $\{|1\rangle, |2\rangle, |3\rangle\}$, dengan $\langle n|x|n\rangle = 1/2$ dan rumus $\langle m|x|n\rangle$ dari Contoh 3.21. Diagonalkan matriks itu.

**Penyelesaian.**

$$
\mathbf X = \begin{pmatrix}0{,}5 & -0{,}1801 & 0\\ -0{,}1801 & 0{,}5 & -0{,}1945\\ 0 & -0{,}1945 & 0{,}5\end{pmatrix} .
$$

$\langle 1|x|3\rangle = 0$ karena paritas. Nilai eigennya (dengan NumPy): 0,235; 0,500; 0,765.

**Memahami hasil.** Operator posisi mempunyai spektrum malar: setiap $x$ di dalam kotak adalah nilai eigen yang mungkin. Basis tiga fungsi hanya mampu "melihat" tiga posisi kasar: dekat kiri, tengah, dekat kanan. Makin besar basisnya, makin rapat nilai eigennya mengisi selang $[0, L]$. Basis berhingga selalu memberi gambaran yang kabur dari ruang yang sebenarnya tak hingga.
:::

::: {.contoh}
**Contoh 4.46 · Kotak dalam medan listrik: diagonalisasi**

Elektron dalam kotak 1,00 nm diletakkan dalam medan listrik $F$ sepanjang $x$, sehingga $\hat H = \hat H_0 + eF\hat x$. Dalam basis $\{|n\rangle\}$, $H_{mn} = E_m\delta_{mn} + eF\langle m|x|n\rangle$. Dengan basis 12 fungsi, diagonalisasi memberikan energi keadaan dasar 0,8476 eV untuk $F = 1{,}0 \times 10^9$ V/m. (a) Berapa pergeseran energinya di luar suku $eFL/2$? (b) Bandingkan dengan pergeseran kuadratik $-\tfrac12\alpha F^2$, dengan polarisabilitas $\alpha = 9{,}23 \times 10^{-39}$ C·m²/V dari teori perturbasi (Bab 8). (c) Nyatakan $\alpha$ sebagai volume polarisabilitas $\alpha/4\pi\varepsilon_0$.

**Penyelesaian.** (a) $E_1 + eFL/2 = 0{,}376 + 0{,}500 = 0{,}876$ eV; pergeserannya $0{,}8476 - 0{,}8760 = -0{,}0284$ eV.

(b) $-\tfrac12\alpha F^2 = -\tfrac12(9{,}23 \times 10^{-39})(10^{18}) = -4{,}61 \times 10^{-21}$ J $= -0{,}0288$ eV. Selisih 1,4%, karena pada medan sekuat ini suku-suku orde lebih tinggi mulai berperan.

(c) $\alpha/4\pi\varepsilon_0 = 8{,}3 \times 10^{-29}$ m³ $= 83$ Å³.

**Memahami hasil.** Medan menarik elektron ke satu sisi (Gambar 4.5 kanan), sehingga energinya turun lebih dari sekadar pergeseran rata-rata potensial. Volume polarisabilitas 83 Å³ berorde sama dengan polarisabilitas molekul terkonjugasi berukuran nanometer (puluhan sampai ratusan Å³), dan jauh di atas atom kecil (hidrogen 0,67 Å³). Inilah efek Stark kuadratik, dihitung dengan cara yang sama persis seperti program kimia komputasi menghitung polarisabilitas: membangun matriks Hamiltonian dalam basis, lalu mendiagonalkannya.
:::

![Gambar 4.5 Elektron dalam kotak 1 nm yang diberi medan listrik. Kiri: tiga energi terendah (dikurangi pergeseran rata-rata $eFL/2$) terhadap kuat medan, dari diagonalisasi matriks 12 × 12. Kanan: rapat peluang keadaan dasar tanpa medan dan dengan medan $1{,}5 \times 10^9$ V/m.](fig/c_stark.png){width=90%}

::: {.contoh}
**Contoh 4.47 · Menyisipkan relasi kelengkapan**

Tunjukkan bahwa unsur matriks hasil kali dua operator adalah hasil kali matriksnya, $(AB)_{m\ell} = \sum_nA_{mn}B_{n\ell}$.

**Penyelesaian.** $(AB)_{m\ell} = \langle m|\hat A\hat B|\ell\rangle = \langle m|\hat A\left(\sum_n|n\rangle\langle n|\right)\hat B|\ell\rangle = \sum_n\langle m|\hat A|n\rangle\langle n|\hat B|\ell\rangle = \sum_nA_{mn}B_{n\ell}$.

**Memahami hasil.** Hasil kali operator menjadi hasil kali matriks, dan komutator operator menjadi komutator matriks. Inilah sebabnya matriks Pauli (Contoh 2.30 di Bab 2) dapat menyatakan operator spin, dan sebabnya ketidakkomutatifan operator posisi dan momentum muncul sebagai ketidakkomutatifan matriks. Perhatikan bahwa jika basisnya dipotong, $(\mathbf{XP} - \mathbf{PX})$ tidak lagi persis $i\hbar\mathbf 1$: pemotongan basis merusak relasi kanonik di tepi basis.
:::

::: {.contoh}
**Contoh 4.48 · Operator proyeksi dan peluang**

Untuk keadaan segitiga $|f\rangle$ Contoh 4.29, tuliskan peluang pengukuran energi memberi $E_1$ dengan operator proyeksi $\hat P_1 = |1\rangle\langle 1|$. Tunjukkan bahwa $\hat P_1^2 = \hat P_1$.

**Penyelesaian.** Peluang $= \langle f|\hat P_1|f\rangle = \langle f|1\rangle\langle 1|f\rangle = |c_1|^2 = 0{,}9855$. $\hat P_1^2 = |1\rangle\langle 1|1\rangle\langle 1| = |1\rangle\langle 1| = \hat P_1$, karena $\langle 1|1\rangle = 1$.

**Memahami hasil.** Memproyeksikan dua kali sama dengan memproyeksikan sekali: itulah isi Postulat 6 dalam bentuk aljabar. Nilai eigen operator proyeksi hanya 0 dan 1: jawaban "tidak" atau "ya" atas pertanyaan "apakah sistem berada di $|1\rangle$?".
:::

::: {.contoh}
**Contoh 4.49 · Komutator kanonik dalam basis terpotong**

Dalam basis kotak, unsur matriks momentum adalah $\langle m|\hat p|n\rangle = -i\hbar\dfrac{4mn}{L(m^2 - n^2)}$ untuk $m + n$ ganjil (dan nol selain itu). Dengan Python, bentuk matriks $\mathbf X$ dan $\mathbf P$ berukuran 6 × 6, lalu hitung unsur diagonal $\mathbf{XP} - \mathbf{PX}$ dalam satuan $\hbar$. Mengapa unsur terakhir sangat menyimpang?

**Penyelesaian.** Unsur diagonalnya (dalam satuan $i\hbar$): 0,997; 0,977; 0,962; 0,805; 0,757; $-4{,}497$. Empat yang pertama mendekati 1, tetapi yang terakhir jauh dari 1, dan jumlah semuanya tepat nol.

**Memahami hasil.** Teras komutator dua matriks berhingga **selalu nol**, karena $\text{tr}(\mathbf{XP}) = \text{tr}(\mathbf{PX})$. Teras $i\hbar\mathbf 1$ berukuran $N$ adalah $iN\hbar \ne 0$. Jadi relasi kanonik $[\hat x, \hat p] = i\hbar$ **tidak mungkin** dipenuhi oleh matriks berhingga; posisi dan momentum hanya dapat dinyatakan dengan tepat dalam ruang berdimensi tak hingga. Basis terpotong merusak relasi itu justru di tepi basis. Pelajaran praktisnya: hasil yang bergantung pada fungsi basis tertinggi selalu paling tidak dapat dipercaya.
:::

::: {.kuis}
**Kuis cepat 4.14**

Dalam notasi Dirac, tuliskan (a) syarat normalisasi, (b) syarat ortogonalitas dua keadaan, (c) nilai harap $\hat H$, dan (d) peluang menemukan sistem $|\psi\rangle$ di keadaan $|n\rangle$.
:::
