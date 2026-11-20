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

## Subbab 12.1: Energi Gibbs reaksi dan kemajuan reaksi

Pakai $R = 8{,}314$ J K⁻¹ mol⁻¹, *RT* = 2,479 kJ mol⁻¹ pada 25 °C, data Tabel 7.1, dan anggap gas ideal kecuali disebutkan lain. Soal dikelompokkan menurut tingkat: **dasar**, **menengah**, dan **tantangan ★**. Soal bertanda **[P]** dibahas di akhir bab.

**Dasar**

**1.** Apa yang dimaksud kemajuan reaksi ξ? Bila ξ = 0,40 mol untuk $\text{N}_2 + 3\text{H}_2 \rightarrow 2\text{NH}_3$, berapa mol NH₃ terbentuk?

**2.** Untuk campuran dengan $p_{\text{N}_2\text{O}_4} = 0{,}50$ bar dan $p_{\text{NO}_2} = 0{,}50$ bar pada 25 °C, hitung $\Delta_\text{r}G$ untuk $\text{N}_2\text{O}_4 \rightarrow 2\text{NO}_2$. Ke mana reaksi berjalan?

**Menengah**

**3.** Mengapa kurva *G* terhadap ξ selalu mempunyai minimum di antara kedua ujung?

**4.** Apa beda $\Delta_\text{r}G$ dan $\Delta_\text{r}G^\circ$?

**Tantangan ★**

**5.** [P] ★ (Python) Mulai dari 1 mol N₂O₄ pada 25 °C dan 1 bar, tuliskan energi Gibbs campuran sebagai fungsi kemajuan reaksi, $G(\xi) = (1 - \xi)\mu_{\text{N}_2\text{O}_4} + 2\xi\,\mu_{\text{NO}_2}$, dengan $\mu_\text{J} = \Delta_\text{f}G^\circ_\text{J} + RT\ln x_\text{J}$ (Tabel 7.1). Cari ξ yang membuat *G* minimum secara numerik, dan bandingkan dengan Contoh 12.6.

## Subbab 12.2: Energi Gibbs standar reaksi dan tetapan kesetimbangan

**Dasar**

**6.** Hitung *K* pada 25 °C untuk $\text{SO}_2 + \tfrac12\text{O}_2 \rightleftharpoons \text{SO}_3$ ($\Delta_\text{r}G^\circ = -70{,}87$ kJ mol⁻¹).

**7.** Berapa *K* untuk reaksi dengan $\Delta_\text{r}G^\circ = -20{,}0$ kJ mol⁻¹ pada 25 °C?

**8.** Berapa $\Delta_\text{r}G^\circ$ untuk reaksi dengan $K = 1{,}0 \times 10^{-3}$ pada 25 °C?

**Menengah**

**9.** Hitung *K* untuk $2\text{NO}_2 \rightleftharpoons \text{N}_2\text{O}_4$ pada 25 °C.

**10.** Reaksi mempunyai $\Delta_\text{r}H^\circ = +50$ kJ mol⁻¹ dan $\Delta_\text{r}S^\circ = +150$ J K⁻¹ mol⁻¹. Hitung *K* pada 400 K.

**11.** [P] Dari Contoh 12.2, hitung *K* pada 25 °C untuk $\text{CO}_2 + \text{H}_2 \rightleftharpoons \text{CO} + \text{H}_2\text{O}(g)$, dan jelaskan aturan yang dipakai.

## Subbab 12.3: K, K_c, dan K_x

**Dasar**

**12.** Untuk $\text{PCl}_5 \rightleftharpoons \text{PCl}_3 + \text{Cl}_2$, *K* = 1,8 pada 523 K. Hitung $K_c$ dengan $c^\circ = 1$ mol L⁻¹.

**13.** Tuliskan *K* untuk $\text{C}(s) + \text{CO}_2(g) \rightleftharpoons 2\text{CO}(g)$.

**Menengah**

**14.** Hitung tekanan penguraian CaCO₃ pada 1200 K (data Contoh 12.13, Δ*H*° dan Δ*S*° tetap).

**15.** Mengapa padatan murni tidak muncul dalam *K*?

## Subbab 12.4: Menghitung komposisi kesetimbangan

**Dasar**

**16.** Dalam Contoh 12.7, bila mula-mula hanya ada 2,00 mol HI, berapa mol H₂ pada kesetimbangan?

**17.** Hitung fraksi PCl₅ yang terurai pada 523 K dan 1,00 bar (*K* = 1,8).

**Menengah**

**18.** Ulangi Contoh 12.8 (c) dengan perbandingan CO : H₂O = 1 : 2.

**19.** [P] Hitung fraksi PCl₅ yang terurai pada 523 K dan 5,00 bar. Bandingkan dengan 1,00 bar dan jelaskan.

**20.** Mengapa tabel kesetimbangan harus memakai jumlah pada kesetimbangan, bukan jumlah awal?

**Tantangan ★**

**21.** ★ Untuk $\text{N}_2\text{O}_4 \rightleftharpoons 2\text{NO}_2$, turunkan $\alpha = \sqrt{K/(K + 4p/p^\circ)}$.

## Subbab 12.5: Pengaruh tekanan dan gas lembam

**Dasar**

**22.** Hitung fraksi N₂O₄ yang terurai pada 25 °C dan 4,00 bar.

**23.** Untuk reaksi mana tekanan tidak berpengaruh pada komposisi kesetimbangan: (a) $\text{H}_2 + \text{I}_2 \rightleftharpoons 2\text{HI}$; (b) $\text{N}_2\text{O}_4 \rightleftharpoons 2\text{NO}_2$; (c) $\text{CO} + \text{H}_2\text{O} \rightleftharpoons \text{CO}_2 + \text{H}_2$?

**Menengah**

**24.** Mengapa menambahkan argon pada volume tetap tidak menggeser kesetimbangan, tetapi pada tekanan tetap menggeser?

**25.** Apakah *K* bergantung pada tekanan? Bagaimana dengan $K_x$?

## Subbab 12.6: Pengaruh suhu: persamaan van 't Hoff

**Dasar**

**26.** *K* suatu reaksi berlipat dua bila suhu dinaikkan dari 25 °C ke 35 °C. Hitung $\Delta_\text{r}H^\circ$.

**27.** Hitung *K* sintesis amonia pada 600 K dengan Δ*H*° tetap.

**Menengah**

**28.** Turunkan persamaan van 't Hoff dari (12.3) dan persamaan Gibbs–Helmholtz.

**29.** Tunjukkan bahwa persamaan Clausius–Clapeyron adalah kasus khusus persamaan van 't Hoff.

**30.** Mengapa plot van 't Hoff untuk sintesis amonia (Gambar 12.2) sedikit melengkung?

**Tantangan ★**

**31.** [P] ★ (Python) Pakai rumus kotak Lebih dalam subbab 12.6 untuk menghitung *K* sintesis amonia pada 500 K dan 723 K dari $K(298{,}15\ \text{K}) = 5{,}81 \times 10^5$, $\Delta_\text{r}H^\circ = -92{,}22$ kJ mol⁻¹, dan $\Delta_\text{r}C_p^\circ = -45{,}5$ J K⁻¹ mol⁻¹. Bandingkan dengan hasil tanpa koreksi kapasitas kalor.

## Subbab 12.7: Asas Le Chatelier secara termodinamika

**Dasar**

**32.** Bagaimana kesetimbangan $\text{N}_2\text{O}_4 \rightleftharpoons 2\text{NO}_2$ bergeser bila (a) suhu dinaikkan, (b) tekanan dinaikkan, (c) NO₂ ditambahkan pada volume tetap?

**Menengah**

**33.** [P] Tunjukkan bahwa menambahkan sedikit N₂ ke campuran N₂–H₂–NH₃ yang setimbang pada tekanan total tetap menggeser reaksi ke kiri bila $x_{\text{N}_2} > \tfrac12$.

**34.** Mengapa katalis tidak menggeser kesetimbangan?

## Subbab 12.8: Kesetimbangan dalam industri dan biokimia

**Dasar**

**35.** Dari Gambar 12.3, taksir fraksi mol amonia pada kesetimbangan pada 450 °C dan 100 bar.

**36.** Reaksi $\text{A} + \text{H}^+ \rightarrow \text{B}$ mempunyai $\Delta_\text{r}G^\circ = -10{,}0$ kJ mol⁻¹. Hitung $\Delta_\text{r}G^{\circ\prime}$ pada 25 °C.

**Menengah**

**37.** Hitung Δ*G* hidrolisis ATP pada 37 °C di sel otot dengan [ATP] = 5,0 mmol L⁻¹, [ADP] = 0,50 mmol L⁻¹, dan [Pᵢ] = 5,0 mmol L⁻¹.

**38.** Mengapa pabrik amonia tidak beroperasi pada 300 °C, padahal hasil kesetimbangannya jauh lebih tinggi?

**39.** Mengapa hasil amonia terukur pada 300 bar lebih tinggi daripada perhitungan gas ideal?

**Tantangan ★**

**40.** ★ Pada 723 K dan 300 bar, koefisien fugasitas N₂, H₂, dan NH₃ kira-kira 1,14; 1,09; dan 0,91. Hitung $K_\varphi = \varphi_{\text{NH}_3}^2/(\varphi_{\text{N}_2}\varphi_{\text{H}_2}^3)$ dan fraksi mol amonia dengan cara Contoh 12.16, lalu bandingkan.

**41.** [P] ★ (Python) Gas umpan proses kontak berisi 10% SO₂, 11% O₂, dan 79% N₂ (fraksi mol). Hitung konversi SO₂ pada kesetimbangan $\text{SO}_2 + \tfrac12\text{O}_2 \rightleftharpoons \text{SO}_3$ pada 700 K dan 1 bar, dengan *K* = 290.


# Jawaban

::: {.panjang}
| No. | Jawaban | No. | Jawaban |
|---|---|---|---|
| 1 | perubahan banyaknya zat dibagi koefisiennya; 0,80 mol | 22 | 0,096 |
| 2 | +3,01 kJ mol⁻¹; ke kiri | 23 | (a) dan (c) |
| 3 | suku pencampuran menurunkan *G* dengan kemiringan tak hingga di dekat zat murni | 24 | volume tetap: tekanan parsial tidak berubah; tekanan tetap: tekanan parsial turun |
| 4 | $\Delta_\text{r}G$ bergantung pada komposisi saat itu; $\Delta_\text{r}G^\circ$ pada keadaan standar | 25 | *K* tidak; $K_x = K(p/p^\circ)^{-\Delta\nu}$ bergantung |
| 5 | ξ = 0,189; sama dengan α Contoh 12.6 | 26 | +52,9 kJ mol⁻¹ |
| 6 | $2{,}6 \times 10^{12}$ | 27 | $4{,}3 \times 10^{-3}$ |
| 7 | $3{,}2 \times 10^3$ | 28 | $d\ln K/dT = -d(\Delta G^\circ/RT)/dT = \Delta H^\circ/RT^2$ |
| 8 | +17,1 kJ mol⁻¹ | 29 | penguapan sebagai reaksi dengan $K = p/p^\circ$ |
| 9 | 6,74 | 30 | $\Delta_\text{r}H^\circ$ berubah dengan suhu karena $\Delta_\text{r}C_p^\circ \ne 0$ |
| 10 | 20 | 31 | 0,094 dan $3{,}6 \times 10^{-5}$ (tanpa koreksi: 0,17 dan $1{,}9 \times 10^{-4}$) |
| 11 | $9{,}7 \times 10^{-6}$ | 32 | (a) kanan; (b) kiri; (c) kiri |
| 12 | 0,041 | 33 | $\partial\ln Q/\partial n_{\text{N}_2} = 2/n - 1/n_{\text{N}_2}$ |
| 13 | $(p_\text{CO}/p^\circ)^2/(p_{\text{CO}_2}/p^\circ)$ | 34 | tidak mengubah $\Delta_\text{r}G^\circ$, hanya laju |
| 14 | 4,2 bar | 35 | sekitar 0,14 |
| 15 | aktivitasnya satu | 36 | +29,95 kJ mol⁻¹ |
| 16 | 0,220 mol | 37 | −50,1 kJ mol⁻¹ |
| 17 | 0,80 | 38 | laju reaksi terlalu lambat |
| 18 | 58% | 39 | koefisien fugasitas NH₃ kecil |
| 19 | 0,51 | 40 | 0,56; $x_{\text{NH}_3} = 0{,}34$ (Contoh 12.16: 0,35) |
| 20 | *K* hanya berlaku pada kesetimbangan | 41 | 98,7% |
| 21 | dari $K = 4\alpha^2p/[(1 - \alpha^2)p^\circ]$ |  |  |
:::


# Pembahasan soal terpilih

**Soal 5.** Dengan $x_{\text{N}_2\text{O}_4} = (1 - \xi)/(1 + \xi)$ dan $x_{\text{NO}_2} = 2\xi/(1 + \xi)$ pada 1 bar:

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

**Soal 11.** Reaksi yang diminta adalah kebalikan reaksi pergeseran air–gas pada Contoh 12.2 (c), yang mempunyai $K = 1{,}03 \times 10^5$. Membalik reaksi membalik tanda $\Delta_\text{r}G^\circ$, sehingga *K* dibalik:
$$
K = \frac{1}{1{,}03 \times 10^5} = 9{,}7 \times 10^{-6} .
$$

*Cara berpikir:* $\ln K = -\Delta_\text{r}G^\circ/RT$ dan $\Delta_\text{r}G^\circ$ adalah fungsi keadaan yang mengikuti stoikiometri. Apa yang berlaku untuk $\Delta_\text{r}G^\circ$ (dibalik → berganti tanda, dijumlahkan → dijumlahkan, dikalikan *n* → dikalikan *n*) berlaku untuk ln *K*, sehingga *K* masing-masing dibalik, dikalikan, dan dipangkatkan. Pada 25 °C, reaksi balik ini praktis tidak berjalan; tetapi pada suhu tinggi, seperti di Contoh 12.8, *K* naik mendekati 1 dan reaksi ini menjadi berarti.

**Soal 19.** Dengan α fraksi terurai: PCl₅ 1 − α, PCl₃ α, Cl₂ α, total 1 + α. Seperti pada N₂O₄,
$$
K = \frac{\alpha^2}{1 - \alpha^2}\cdot\frac{p}{p^\circ} \quad\Rightarrow\quad \alpha = \sqrt{\frac{K}{K + p/p^\circ}} = \sqrt{\frac{1{,}8}{6{,}8}} = 0{,}51 .
$$
Pada 1,00 bar, $\alpha = \sqrt{1{,}8/2{,}8} = 0{,}80$.

*Cara berpikir:* reaksi menambah satu mol gas (Δν = +1), sehingga tekanan tinggi menekan penguraian, sesuai Le Chatelier. Besarnya pergeseran diberikan oleh $K_x = K(p/p^\circ)^{-1}$: menaikkan tekanan lima kali menurunkan $K_x$ lima kali, dan α turun dari 0,80 ke 0,51. Pengaruh tekanan tidak pernah membuat *K* sendiri berubah.

**Soal 31.**

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

**Soal 33.** Dengan $p_\text{J} = (n_\text{J}/n)p$, $\ln Q = 2\ln n_{\text{NH}_3} + 2\ln n - \ln n_{\text{N}_2} - 3\ln n_{\text{H}_2} + \text{tetapan}$. Turunkan terhadap $n_{\text{N}_2}$, dengan *n* juga bertambah:
$$
\frac{\partial\ln Q}{\partial n_{\text{N}_2}} = \frac{2}{n} - \frac{1}{n_{\text{N}_2}} .
$$
Turunan ini positif, sehingga *Q* naik di atas *K* dan reaksi bergeser ke kiri, bila $n_{\text{N}_2} > n/2$, yaitu $x_{\text{N}_2} > \tfrac12$.

*Cara berpikir:* menambah N₂ menaikkan tekanan parsial N₂ (suku $-1/n_{\text{N}_2}$) tetapi juga menambah mol total, yang mengencerkan semua gas lain (suku $2/n$, dari Δν = −2). Bila N₂ sudah melimpah, penambahan berikutnya hampir tidak menaikkan fraksi molnya, sedangkan pengencerannya tetap terasa. Kesimpulan umumnya: untuk menilai arah, hitung *Q*; jangan mengandalkan kata "melawan gangguan".

**Soal 41.** Basis 1 mol umpan: SO₂ 0,10; O₂ 0,11; N₂ 0,79. Dengan konversi *X*: SO₂ $0{,}10(1 - X)$, O₂ $0{,}11 - 0{,}05X$, SO₃ $0{,}10X$, total $1 - 0{,}05X$. Pada 1 bar, $K = x_{\text{SO}_3}/(x_{\text{SO}_2}x_{\text{O}_2}^{1/2})$:

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
