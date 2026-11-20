# Ringkasan Bab 12

| Gagasan | Rumus atau hasil | Subbab |
|---|---|---|
| Energi Gibbs reaksi | $\Delta_\text{r}G = (\partial G/\partial\xi)_{T,p} = \sum\nu_\text{J}\mu_\text{J}$; setimbang bila nol | 12.1 |
| Kuosien reaksi | $\Delta_\text{r}G = \Delta_\text{r}G^\circ + RT\ln Q$, $Q = \prod a_\text{J}^{\nu_\text{J}}$ | 12.2 |
| Tetapan kesetimbangan | $\Delta_\text{r}G^\circ = -RT\ln K$; setiap 5,7 kJ mol⁻¹ = faktor 10 pada 25 °C | 12.2 |
| Bentuk lain | $K = K_c(c^\circ RT/p^\circ)^{\Delta\nu} = K_x(p/p^\circ)^{\Delta\nu}$; padatan murni *a* = 1 | 12.3 |
| Komposisi | nyatakan semua jumlah dengan ξ atau α, masukkan ke *K* | 12.4 |
| Tekanan dan gas lembam | *K* tetap; $K_x$ berubah bila Δν ≠ 0; lembam pada *p* tetap = pengenceran | 12.5 |
| van 't Hoff | $d\ln K/dT = \Delta_\text{r}H^\circ/RT^2$; $\ln(K_2/K_1) = -(\Delta_\text{r}H^\circ/R)(1/T_2 - 1/T_1)$ | 12.6 |
| Le Chatelier | benar untuk *T* dan *p*; untuk komposisi bandingkan *Q* dengan *K* | 12.7 |
| Keadaan standar biokimia | $\Delta_\text{r}G^{\circ\prime} = \Delta_\text{r}G^\circ + \nu RT\ln10^{-7}$ | 12.8 |

**Jawaban kuis cepat.** **12.1** Di kedua ujung, suku pencampuran membuat kemiringan *G* menuju −∞ (atau +∞), sehingga kurva selalu turun dulu menjauhi zat murni. **12.2** $\Delta_\text{r}G^\circ = 0$. Tidak: *K* = 1 berarti hasil kali aktivitas hasil sama dengan hasil kali aktivitas pereaksi (dengan pangkat koefisiennya), bukan jumlahnya sama. **12.3** Ya, karena Δν = 0, sehingga faktor $(c^\circ RT/p^\circ)^{\Delta\nu}$ dan $(p/p^\circ)^{\Delta\nu}$ sama dengan satu. **12.4** 0,220 mol, sama dengan Contoh 12.7 (kesetimbangan tidak bergantung pada arah pendekatan). **12.5** Tidak berpengaruh, karena tekanan parsial setiap gas tidak berubah. **12.6** Miring ke bawah (kemiringan $-\Delta_\text{r}H^\circ/R$ negatif), karena *K* naik ketika 1/*T* turun. **12.7** Tidak. Katalis tidak mengubah $\Delta_\text{r}G^\circ$, sehingga *K* tetap; ia hanya mempercepat tercapainya kesetimbangan. **12.8** Karena tidak ada H⁺ dalam *Q*, perubahan keadaan standar H⁺ tidak berpengaruh.

# Pertanyaan

1. Mengapa reaksi dengan $\Delta_\text{r}G^\circ$ positif tetap menghasilkan sedikit hasil?
2. Apa arti fisis $\Delta_\text{r}G$ sebagai kemiringan kurva *G* terhadap ξ?
3. Mengapa tetapan kesetimbangan termodinamika tidak bersatuan?
4. Mengapa *K* sangat peka terhadap $\Delta_\text{r}G^\circ$?
5. Jelaskan aturan penggabungan *K* dengan hukum Hess untuk energi Gibbs.
6. Mengapa plester kapur mengeras di udara?
7. Mengapa komposisi kesetimbangan reaksi dengan Δν = 0 tidak bergantung pada tekanan?
8. Mengapa reaksi yang menambah jumlah mol gas hampir tuntas pada tekanan sangat rendah?
9. Bagaimana gas lembam yang menumpuk merugikan pabrik amonia?
10. Apa hubungan antara persamaan van 't Hoff dan persamaan Clausius–Clapeyron?
11. Bagaimana $\Delta_\text{r}H^\circ$ suatu reaksi dapat diukur tanpa kalorimeter?
12. Berikan contoh kegagalan asas Le Chatelier dan jelaskan sebabnya.
13. Mengapa proses Haber–Bosch dijalankan pada 400–500 °C?
14. Mengapa biokimiawan memerlukan keadaan standar yang berbeda?
15. Mengapa Δ*G* hidrolisis ATP di dalam sel jauh lebih negatif daripada $\Delta_\text{r}G^{\circ\prime}$?

# Soal

%%SOAL%%

# Jawaban

%%JAWABAN%%

# Pembahasan soal terpilih

**Soal {{gxi}}.** Dengan $x_{\text{N}_2\text{O}_4} = (1 - \xi)/(1 + \xi)$ dan $x_{\text{NO}_2} = 2\xi/(1 + \xi)$ pada 1 bar:

```python
import math
from scipy.optimize import minimize_scalar
RT = 8.314*298.15/1000                     # kJ/mol
G = lambda x: ((1 - x)*(97.89 + RT*math.log((1 - x)/(1 + x)))
               + 2*x*(51.31 + RT*math.log(2*x/(1 + x))))
r = minimize_scalar(G, bounds=(1e-9, 1 - 1e-9), method='bounded')
print(r.x, G(r.x))                         # 0.189  96.94 kJ
```

Minimum terletak di ξ = 0,189, tepat α pada Contoh 12.6, dengan *G* = 96,94 kJ, di bawah kedua ujung (97,89 kJ untuk N₂O₄ murni dan 102,62 kJ untuk NO₂ murni). Mencari minimum *G* dan menyelesaikan $Q = K$ adalah dua cara menghitung hal yang sama, karena kemiringan $dG/d\xi$ adalah $\Delta_\text{r}G$ (12.1), dan kemiringan itu nol tepat ketika $Q = K$. Perangkat lunak teknik kimia untuk reaktor dengan banyak reaksi sekaligus memakai cara pertama: meminimumkan *G* langsung, tanpa menulis satu tetapan kesetimbangan pun.

**Soal {{hess}}.** Reaksi yang diminta adalah kebalikan reaksi pergeseran air–gas pada Contoh 12.2 (c), yang mempunyai $K = 1{,}03 \times 10^5$. Membalik reaksi membalik tanda $\Delta_\text{r}G^\circ$, sehingga *K* dibalik:
$$
K = \frac{1}{1{,}03 \times 10^5} = 9{,}7 \times 10^{-6} .
$$

*Cara berpikir:* $\ln K = -\Delta_\text{r}G^\circ/RT$ dan $\Delta_\text{r}G^\circ$ adalah fungsi keadaan yang mengikuti stoikiometri. Apa yang berlaku untuk $\Delta_\text{r}G^\circ$ (dibalik → berganti tanda, dijumlahkan → dijumlahkan, dikalikan *n* → dikalikan *n*) berlaku untuk ln *K*, sehingga *K* masing-masing dibalik, dikalikan, dan dipangkatkan. Pada 25 °C, reaksi balik ini praktis tidak berjalan; tetapi pada suhu tinggi, seperti di Contoh 12.8, *K* naik mendekati 1 dan reaksi ini menjadi berarti.

**Soal {{pcl}}.** Dengan α fraksi terurai: PCl₅ 1 − α, PCl₃ α, Cl₂ α, total 1 + α. Seperti pada N₂O₄,
$$
K = \frac{\alpha^2}{1 - \alpha^2}\cdot\frac{p}{p^\circ} \quad\Rightarrow\quad \alpha = \sqrt{\frac{K}{K + p/p^\circ}} = \sqrt{\frac{1{,}8}{6{,}8}} = 0{,}51 .
$$
Pada 1,00 bar, $\alpha = \sqrt{1{,}8/2{,}8} = 0{,}80$.

*Cara berpikir:* reaksi menambah satu mol gas (Δν = +1), sehingga tekanan tinggi menekan penguraian, sesuai Le Chatelier. Besarnya pergeseran diberikan oleh $K_x = K(p/p^\circ)^{-1}$: menaikkan tekanan lima kali menurunkan $K_x$ lima kali, dan α turun dari 0,80 ke 0,51. Pengaruh tekanan tidak pernah membuat *K* sendiri berubah.

**Soal {{vtc}}.**

```python
import math
R, T1, K1, H, dCp = 8.314, 298.15, 5.81e5, -92220, -45.5
for T2 in (500, 723):
    a = -(H - T1*dCp)/R*(1/T2 - 1/T1) + dCp/R*math.log(T2/T1)   # dengan koreksi
    b = -H/R*(1/T2 - 1/T1)                                        # tanpa koreksi
    print(T2, K1*math.exp(a), K1*math.exp(b))
# 500  0.094    0.17
# 723  3.6e-05  1.9e-04
```

Koreksi kapasitas kalor menurunkan *K* hampir dua kali pada 500 K dan lima kali pada 723 K. Alasannya: $\Delta_\text{r}C_p^\circ$ negatif membuat $\Delta_\text{r}H^\circ$ makin negatif ketika suhu naik (hukum Kirchhoff), sehingga *K* turun lebih cepat daripada ramalan dengan Δ*H*° tetap. Makin lebar rentang suhunya, makin besar koreksinya.

**Soal {{lechat}}.** Dengan $p_\text{J} = (n_\text{J}/n)p$, $\ln Q = 2\ln n_{\text{NH}_3} + 2\ln n - \ln n_{\text{N}_2} - 3\ln n_{\text{H}_2} + \text{tetapan}$. Turunkan terhadap $n_{\text{N}_2}$, dengan *n* juga bertambah:
$$
\frac{\partial\ln Q}{\partial n_{\text{N}_2}} = \frac{2}{n} - \frac{1}{n_{\text{N}_2}} .
$$
Turunan ini positif, sehingga *Q* naik di atas *K* dan reaksi bergeser ke kiri, bila $n_{\text{N}_2} > n/2$, yaitu $x_{\text{N}_2} > \tfrac12$.

*Cara berpikir:* menambah N₂ menaikkan tekanan parsial N₂ (suku $-1/n_{\text{N}_2}$) tetapi juga menambah mol total, yang mengencerkan semua gas lain (suku $2/n$, dari Δν = −2). Bila N₂ sudah melimpah, penambahan berikutnya hampir tidak menaikkan fraksi molnya, sedangkan pengencerannya tetap terasa. Kesimpulan umumnya: untuk menilai arah, hitung *Q*; jangan mengandalkan kata "melawan gangguan".

**Soal {{kontak}}.** Basis 1 mol umpan: SO₂ 0,10; O₂ 0,11; N₂ 0,79. Dengan konversi *X*: SO₂ $0{,}10(1 - X)$, O₂ $0{,}11 - 0{,}05X$, SO₃ $0{,}10X$, total $1 - 0{,}05X$. Pada 1 bar, $K = x_{\text{SO}_3}/(x_{\text{SO}_2}x_{\text{O}_2}^{1/2})$:

```python
from scipy.optimize import brentq
def f(X):
    nt = 1 - 0.05*X
    so2, o2, so3 = 0.10*(1 - X)/nt, (0.11 - 0.05*X)/nt, 0.10*X/nt
    return so3/(so2*o2**0.5) - 290
print(brentq(f, 1e-6, 0.999999))   # 0.987
```

Konversi 98,7%. Walaupun *K* turun dari $2{,}6 \times 10^{12}$ pada suhu kamar menjadi 290 pada 700 K, oksigen berlebih dan nitrogen yang tidak ikut bereaksi masih memungkinkan hampir seluruh SO₂ teroksidasi. Pada 1000 K (*K* = 1,8), perhitungan yang sama hanya memberi 36%; inilah sebabnya pabrik mendinginkan gas di antara lapisan katalis.

# Bacaan lanjut

1. P. Atkins, J. de Paula, dan J. Keeler, *Atkins' Physical Chemistry*, edisi ke-12 (Oxford University Press, 2023), Topik 6A–6B. Kesetimbangan kimia dan tanggapannya terhadap kondisi.
2. I. N. Levine, *Physical Chemistry*, edisi ke-6 (McGraw-Hill, 2009), Bab 6 dan 11. Kesetimbangan gas ideal dan larutan nonideal.
3. J. de Heer, "The principle of Le Chatelier and Braun", *Journal of Chemical Education* 34, 375–380 (1957). Analisis klasik tentang batas asas Le Chatelier, termasuk contoh nitrogen.
4. V. Smil, *Enriching the Earth: Fritz Haber, Carl Bosch, and the Transformation of World Food Production* (MIT Press, 2001). Sejarah dan dampak proses Haber–Bosch.
5. D. L. Nelson dan M. M. Cox, *Lehninger Principles of Biochemistry*, edisi ke-8 (Macmillan, 2021), Bab 13. Keadaan standar biokimia dan energetika ATP.
