import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import sisip, soal
N = 9
print(sisip(N, '9.2', r'''::: {.contoh}
**Contoh 9.t21 · Garis singgung dari data laboratorium**

Di laboratorium, rumus empiris belum tersedia; yang ada hanya hasil pengukuran. Tiga larutan NaCl dalam 1,000 kg air pada 25 °C mempunyai volume berikut:

| $n_\text{NaCl}$ (mol) | 0,900 | 1,000 | 1,100 |
|---|---|---|---|
| *V* (cm³) | 1019,53 | 1021,47 | 1023,43 |

Taksir volume molar parsial NaCl pada 1,000 mol kg⁻¹.

**Penyelesaian.** Kemiringan kurva di titik tengah ditaksir dengan selisih terpusat:
$$
V_\text{NaCl} \approx \frac{V(1{,}100) - V(0{,}900)}{1{,}100 - 0{,}900} = \frac{1023{,}43 - 1019{,}53}{0{,}200} = 19{,}5\ \text{cm}^3\ \text{mol}^{-1} .
$$

**Memahami hasil.** Hasilnya sama dengan Contoh 9.2, yang memakai turunan rumus. Dalam praktik, selisih volumenya hanya beberapa sentimeter kubik dari sekitar seribu, sehingga volume harus diukur sangat teliti, biasanya dengan **piknometer** atau densitometer osilasi yang mengukur rapatan sampai enam angka penting. Kesalahan 0,01 cm³ pada setiap volume sudah mengubah hasil sekitar 0,1 cm³ mol⁻¹.
:::''', 'Garis singgung dari data laboratorium'))

print(sisip(N, '9.4', r'''Persamaan Gibbs–Duhem juga dapat dipakai untuk **membangun** potensial kimia satu komponen dari komponen lain. Contoh berikut melakukannya, dan hasilnya akan menjadi titik awal Bab 10.

::: {.contoh}
**Contoh 9.t22 · Dari pelarut ke zat terlarut**

Misalkan dalam suatu campuran dua zat, pada suhu dan tekanan tetap, potensial kimia A mengikuti $\mu_\text{A} = \mu_\text{A}^* + RT\ln x_\text{A}$ pada semua komposisi. Pakai persamaan Gibbs–Duhem untuk menentukan bentuk $\mu_\text{B}$.

**Rencana.** Nyatakan $d\mu_\text{A}$ dengan $dx_\text{A}$, pakai $d\mu_\text{B} = -(x_\text{A}/x_\text{B})\,d\mu_\text{A}$, lalu integralkan.

**Penyelesaian.** $d\mu_\text{A} = RT\,dx_\text{A}/x_\text{A}$. Maka
$$
d\mu_\text{B} = -\frac{x_\text{A}}{x_\text{B}}\cdot\frac{RT\,dx_\text{A}}{x_\text{A}} = -\frac{RT\,dx_\text{A}}{x_\text{B}} = \frac{RT\,dx_\text{B}}{x_\text{B}} ,
$$
karena $dx_\text{A} = -dx_\text{B}$. Integralkan: $\mu_\text{B} = \text{tetapan} + RT\ln x_\text{B}$. Pada $x_\text{B} = 1$ (B murni), $\mu_\text{B} = \mu_\text{B}^*$, sehingga tetapannya $\mu_\text{B}^*$:
$$
\mu_\text{B} = \mu_\text{B}^* + RT\ln x_\text{B} .
$$

**Memahami hasil.** Bila satu komponen mengikuti hukum logaritma ini di seluruh rentang komposisi, komponen lain **harus** mengikutinya juga. Campuran seperti itu disebut **larutan ideal**, dan rumus $\mu = \mu^* + RT\ln x$ akan menjadi alat utama Bab 10. Perhatikan kemiripannya dengan (9.11) untuk gas: fraksi mol dalam larutan memainkan peran yang sama dengan tekanan parsial dalam gas.
:::''', 'Dari pelarut ke zat terlarut'))

print(sisip(N, '9.5', r'''::: {.contoh}
**Contoh 9.t23 · Kerja minimum mengisi tabung selam**

Udara diisikan ke tabung selam dari 1 bar sampai 200 bar pada 25 °C. Anggap udara gas ideal. (a) Berapa kenaikan potensial kimia O₂ dan N₂ per mol? (b) Berapa kerja minimum per mol udara?

**Penyelesaian.** (a) Tekanan parsial setiap gas naik dengan faktor 200, karena komposisi tidak berubah. Dari (9.11), untuk setiap gas: $\Delta\mu = RT\ln200 = (2479)(5{,}298) = 13{,}1$ kJ mol⁻¹.

(b) Pada suhu dan tekanan yang berubah secara reversibel pada suhu tetap, kerja minimum sama dengan kenaikan energi Gibbs: $w_\text{min} = \sum n_\text{J}\Delta\mu_\text{J} = (0{,}79 + 0{,}21)(13{,}1) = 13{,}1$ kJ per mol udara.

**Memahami hasil.** Hasil ini tepat sama dengan kalor yang harus dibuang kompresor dalam Contoh 6.11: pada proses isotermal gas ideal, Δ*H* = 0, sehingga $\Delta G = -T\Delta S$, dan seluruh kerja yang masuk keluar lagi sebagai kalor. Energi yang "tersimpan" di dalam tabung bukan energi dalam yang lebih besar, tetapi energi Gibbs yang lebih besar, yaitu entropi yang lebih kecil. Ketika penyelam menghirup udara itu melalui regulator, kemampuan melakukan kerja tersebut terbuang sebagai pemuaian tak reversibel.
:::''', 'Kerja minimum mengisi tabung selam'))

soal(N, '9.1', [r'Satu mol air ditambahkan ke danau etanol murni. Berapa kira-kira pertambahan volumenya (lihat Gambar 9.2)? ||| sekitar 14 cm³'])
soal(N, '9.2', [r'Pada larutan sukrosa dengan 1,000 kg air, volume 1063,9; 1066,1; dan 1068,3 cm³ untuk 0,290; 0,300; dan 0,310 mol sukrosa. Taksir volume molar parsial sukrosa. ||| 220 cm³ mol⁻¹'])
soal(N, '9.3', [r'Mengapa potensial kimia disebut "suhu bagi materi"? ||| menentukan arah aliran zat seperti suhu menentukan arah aliran kalor',
                r'Iodin dalam sistem air–CCl₄ setimbang. Bila sedikit CCl₄ murni ditambahkan, ke mana iodin berpindah mula-mula? ||| dari air ke CCl₄ (μ di CCl₄ turun)'])
soal(N, '9.4', [r'Bila $\mu_\text{A} = \mu_\text{A}^* + RT\ln x_\text{A} + w x_\text{B}^2$, dengan *w* tetap, tentukan $\mu_\text{B}$ dengan Gibbs–Duhem. ||| $\mu_\text{B} = \mu_\text{B}^* + RT\ln x_\text{B} + w x_\text{A}^2$'])
soal(N, '9.5', [r'Hitung kenaikan potensial kimia O₂ bila udara dimampatkan dari 1 bar ke 50 bar pada 25 °C. ||| 9,70 kJ mol⁻¹',
                r'Dari Gambar 9.3, taksir selisih $\mu_\text{nyata} - \mu_\text{ideal}$ untuk H₂ pada 300 bar dan 25 °C. ||| sekitar +0,57 kJ mol⁻¹ (φ ≈ 1,26)',
                r'Mengapa tabel $\Delta_\text{f}G^\circ$ tetap dapat dipakai untuk gas nyata? ||| keadaan standarnya gas ideal hipotetis pada 1 bar; penyimpangan masuk ke φ'])
