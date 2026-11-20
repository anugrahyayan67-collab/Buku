## 13.4 Persamaan Nernst

Potensial standar berlaku bila semua zat dalam keadaan standar. Sel nyata hampir tidak pernah begitu: konsentrasi berubah ketika sel bekerja, dan tegangannya ikut berubah. Bagaimana?

Jawabannya sudah tersedia. Dari Bab 12, $\Delta_\text{r}G = \Delta_\text{r}G^\circ + RT\ln Q$. Bagi kedua ruas dengan −*nF* dan pakai (13.1):

::: {.inti}
$$
E = E^\circ - \frac{RT}{nF}\ln Q . \qquad \text{(13.3)}
$$
**Persamaan Nernst.** Pada 25 °C, $RT/F = 25{,}69$ mV, dan dalam logaritma basis sepuluh: $E = E^\circ - (0{,}059\,16\ \text{V}/n)\log Q$.
:::

Setiap kenaikan *Q* sepuluh kali menurunkan tegangan sel sebesar 59,16 mV dibagi *n*. Ketergantungan logaritmik ini membuat tegangan sel cukup stabil: konsentrasi harus berubah seratus kali agar tegangan sel dengan *n* = 2 berubah 59 mV. Itulah sebabnya baterai memberikan tegangan yang hampir tetap sepanjang sebagian besar umurnya, lalu jatuh tajam ketika pereaksinya hampir habis (*Q* menuju tak hingga).

::: {.contoh}
**Contoh 13.5 · Sel Daniell yang sudah dipakai**

Sel Daniell bekerja sampai [Zn²⁺] = 1,0 mol L⁻¹ dan [Cu²⁺] = 0,010 mol L⁻¹. Anggap aktivitas sama dengan konsentrasi. Hitung potensial selnya pada 25 °C.

**Penyelesaian.** $Q = [\text{Zn}^{2+}]/[\text{Cu}^{2+}] = 100$ (logam padat beraktivitas 1). Dari (13.3):
$$
E = 1{,}102 - \frac{0{,}059\,16}{2}\log100 = 1{,}102 - 0{,}059 = 1{,}043\ \text{V} .
$$

**Memahami hasil.** Setelah 99% ion tembaga habis, tegangan hanya turun 5%. Tegangan baru jatuh berarti ketika [Cu²⁺] mencapai sekitar 10⁻¹⁰ mol L⁻¹ atau kurang; tetapi pada saat itu sel praktis sudah kosong. Tegangan yang hampir tetap ini adalah ciri khas semua sel elektrokimia, dan alasan mengapa indikator baterai yang hanya membaca tegangan tidak dapat menaksir sisa isi dengan teliti.
:::

Persamaan Nernst juga berlaku untuk setiap setengah sel terhadap SHE. Untuk setengah reaksi $\text{Ox} + n\text{e}^- \rightarrow \text{Red}$:

$$
E = E^\circ - \frac{RT}{nF}\ln\frac{a_\text{Red}}{a_\text{Ox}} . \qquad \text{(13.4)}
$$

Bentuk ini paling berguna untuk setengah reaksi yang melibatkan H⁺, karena potensialnya bergantung pada pH. Untuk elektrode hidrogen pada tekanan H₂ 1 bar, $E = -(RT/F)\ln(1/a_{\text{H}^+}) = -0{,}059\,16\ \text{pH}$. Untuk elektrode oksigen, $E = 1{,}229 - 0{,}059\,16\ \text{pH}$. Kedua garis sejajar dan berjarak 1,229 V pada setiap pH. Gambar 13.2 memperlihatkan maknanya.

![Gambar 13.2 Jendela kestabilan air pada 25 °C dan tekanan gas 1 bar. Di atas garis atas, air dioksidasi menjadi O₂; di bawah garis bawah, air direduksi menjadi H₂. Pengoksidasi yang potensialnya di atas jendela atau pereduksi yang potensialnya di bawahnya secara termodinamika tidak stabil dalam air.](fig/airstabil.png){width=72%}

::: {.contoh}
**Contoh 13.6 · Permanganat pada pH berbeda**

Hitung potensial setengah sel $\text{MnO}_4^- + 8\text{H}^+ + 5\text{e}^- \rightarrow \text{Mn}^{2+} + 4\text{H}_2\text{O}$ pada pH 0 dan pH 3, dengan $[\text{MnO}_4^-] = [\text{Mn}^{2+}]$. Apakah permanganat dapat mengoksidasi ion klorida pada kedua pH itu?

**Penyelesaian.** Dari (13.4), dengan $a_\text{Ox}$ memuat $a_{\text{H}^+}^8$:
$$
E = 1{,}507 - \frac{0{,}059\,16}{5}\log\frac{1}{(10^{-\text{pH}})^8} = 1{,}507 - \frac{8}{5}(0{,}059\,16)\,\text{pH} .
$$
Pada pH 0: 1,507 V. Pada pH 3: 1,507 − 0,284 = 1,223 V.

Klorida dioksidasi bila potensial pengoksidasi melebihi $E^\circ(\text{Cl}_2/\text{Cl}^-) = 1{,}358$ V. Pada pH 0 bisa (1,507 > 1,358); pada pH 3 tidak.

**Memahami hasil.** Daya oksidasi permanganat sangat bergantung pada keasaman, karena delapan ion H⁺ ikut dalam reaksinya. Inilah alasan titrasi permanganometri selalu dilakukan dalam asam sulfat, bukan asam klorida: dalam HCl pekat, permanganat ikut mengoksidasi klorida dan hasil titrasi menjadi terlalu tinggi.
:::

::: {.kuis}
**Kuis cepat 13.4** Logam natrium (*E*° = −2,714 V) bereaksi hebat dengan air. Pakai Gambar 13.2 untuk menjelaskan mengapa.
:::

## 13.5 Potensial standar dan tetapan kesetimbangan

Ketika sel bekerja sampai habis, reaksi sel mencapai kesetimbangan, dan tegangannya nol: tidak ada lagi dorongan untuk memindahkan elektron. Pada saat itu *Q* = *K*. Dari (13.3) dengan *E* = 0:

::: {.inti}
$$
\ln K = \frac{nFE^\circ}{RT} , \qquad \log K = \frac{nE^\circ}{0{,}059\,16\ \text{V}}\quad(25\ ^\circ\text{C}) . \qquad \text{(13.5)}
$$
**Potensial standar dan tetapan kesetimbangan.** Setiap 59 mV pada *E*° (dibagi *n*) berarti faktor sepuluh pada *K*.
:::

Persamaan ini adalah gabungan $\Delta_\text{r}G^\circ = -nFE^\circ$ dan $\Delta_\text{r}G^\circ = -RT\ln K$, dan ia memberi cara yang sangat kuat untuk mengukur tetapan kesetimbangan, termasuk yang terlalu besar atau terlalu kecil untuk diukur dengan analisis komposisi.

::: {.contoh}
**Contoh 13.7 · Tetapan kesetimbangan sel Daniell**

Hitung *K* untuk $\text{Zn} + \text{Cu}^{2+} \rightleftharpoons \text{Zn}^{2+} + \text{Cu}$ pada 25 °C.

**Penyelesaian.** $\log K = (2)(1{,}102)/0{,}059\,16 = 37{,}26$, sehingga $K = 1{,}8 \times 10^{37}$.

**Memahami hasil.** Pada kesetimbangan, $[\text{Cu}^{2+}]/[\text{Zn}^{2+}] = 5{,}5 \times 10^{-38}$. Bila [Zn²⁺] = 1 mol L⁻¹, sisa ion tembaga kira-kira satu ion dalam $3 \times 10^{13}$ liter, setara dengan satu ion dalam air sebuah danau besar. Konsentrasi sekecil itu tidak dapat diukur dengan cara apa pun, tetapi tegangan sel mengukurnya secara tidak langsung dengan mudah. Reaksi ini praktis berjalan tuntas, dan itulah sebabnya serbuk seng dipakai untuk mengendapkan tembaga dan logam mulia dari larutan.
:::

Cara yang sama memberi hasil kali kelarutan. Trik yang dipakai: susun dua setengah sel yang reaksi selnya adalah reaksi pelarutan, walaupun reaksi itu bukan redoks.

::: {.contoh}
**Contoh 13.8 · Kelarutan perak klorida dari voltmeter**

Gabungkan setengah reaksi $\text{AgCl} + \text{e}^- \rightarrow \text{Ag} + \text{Cl}^-$ ($E^\circ = 0{,}2223$ V) dan $\text{Ag}^+ + \text{e}^- \rightarrow \text{Ag}$ ($E^\circ = 0{,}7996$ V) untuk menghitung $K_\text{sp}$ AgCl pada 25 °C.

**Penyelesaian.** Kurangkan setengah reaksi kedua dari yang pertama: $\text{AgCl}(s) \rightarrow \text{Ag}^+(aq) + \text{Cl}^-(aq)$, dengan *n* = 1 dan $E^\circ = 0{,}2223 - 0{,}7996 = -0{,}5773$ V. Dari (13.5):
$$
\ln K_\text{sp} = \frac{(96\,485)(-0{,}5773)}{(8{,}314)(298{,}15)} = -22{,}47 , \qquad K_\text{sp} = 1{,}7 \times 10^{-10} .
$$

**Memahami hasil.** Nilai ini sama dengan hasil pengukuran kelarutan langsung, $1{,}8 \times 10^{-10}$. Untuk garam yang jauh lebih sukar larut, seperti AgI ($K_\text{sp} \approx 10^{-16}$) atau HgS ($10^{-52}$), cara elektrokimia adalah satu-satunya yang praktis. Perhatikan bahwa reaksi sel yang dihitung tidak pernah benar-benar dijalankan dalam satu sel; kita cukup menggabungkan dua potensial dari tabel, karena keduanya diukur terhadap acuan yang sama.
:::

::: {.contoh}
**Contoh 13.9 · Mengapa titrasi redoks tajam**

Dalam titrasi Fe²⁺ dengan Ce⁴⁺ dalam asam sulfat, $E^\circ(\text{Ce}^{4+}/\text{Ce}^{3+}) = 1{,}61$ V dan $E^\circ(\text{Fe}^{3+}/\text{Fe}^{2+}) = 0{,}771$ V. Hitung *K* reaksi titrasi $\text{Ce}^{4+} + \text{Fe}^{2+} \rightleftharpoons \text{Ce}^{3+} + \text{Fe}^{3+}$.

**Penyelesaian.** $E^\circ = 1{,}61 - 0{,}771 = 0{,}839$ V, *n* = 1. $\log K = 0{,}839/0{,}059\,16 = 14{,}2$, sehingga $K = 1{,}5 \times 10^{14}$.

**Memahami hasil.** Pada titik ekivalen, perbandingan [Fe²⁺]/[Fe³⁺] sekitar $1/\sqrt{K} \approx 10^{-7}$: reaksi tuntas sampai sepersepuluh juta. Potensial larutan melompat hampir 0,8 V di sekitar titik ekivalen, karena yang menentukan potensial berpindah dari pasangan besi ke pasangan cerium. Lompatan inilah yang dideteksi oleh indikator redoks atau elektrode platina. Reaksi titrasi yang baik memerlukan selisih *E*° paling sedikit sekitar 0,3–0,4 V.
:::

::: {.kuis}
**Kuis cepat 13.5** Suatu reaksi sel mempunyai *E*° = 0 V. Berapa tetapan kesetimbangannya? Apakah sel ini dapat menghasilkan listrik?
:::
