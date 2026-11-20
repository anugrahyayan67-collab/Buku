# Ringkasan Bab 6

| Gagasan | Rumus atau hasil | Subbab |
|---|---|---|
| Gas ideal, *T* dan *V* | $\Delta S = nC_{V,\text{m}}\ln(T_2/T_1) + nR\ln(V_2/V_1)$ | 6.1 |
| Gas ideal, *T* dan *p* | $\Delta S = nC_{p,\text{m}}\ln(T_2/T_1) - nR\ln(p_2/p_1)$ | 6.2 |
| Cairan dan padatan | $\Delta S \approx C_p\ln(T_2/T_1)$ | 6.2 |
| Pencampuran | $\Delta_\text{mix}S = -nR\sum x_J\ln x_J$; gas identik: 0 | 6.3 |
| Transisi pada suhu lain | jalan reversibel melalui suhu transisi normal | 6.4 |
| Pemanasan | $\Delta S = \int C_p\,dT/T$; dengan $a + bT + c/T^2$: $a\ln(T_2/T_1) + b\Delta T - \tfrac c2(T_2^{-2} - T_1^{-2})$ | 6.5 |
| Hukum ketiga | $S = 0$ untuk kristal sempurna pada 0 K | 6.6 |
| Debye | $C_p \approx aT^3$; $S(T) = C_p(T)/3$ | 6.6 |
| Entropi mutlak | jumlah sumbangan padat, peleburan, cair, penguapan, gas | 6.6 |
| Entropi reaksi | $\Delta_\text{r}S^\circ = \sum\nu S_\text{m}^\circ(\text{hasil}) - \sum\nu S_\text{m}^\circ(\text{pereaksi})$ | 6.7 |
| Arah reaksi | $\Delta S_\text{total} = \Delta_\text{r}S - \Delta_\text{r}H/T > 0$; suhu peralihan $T = \Delta_\text{r}H/\Delta_\text{r}S$ | 6.8 |

**Jawaban kuis cepat.** **6.1** Tidak nol. Entropi fungsi keadaan, dan keadaan akhirnya sama dengan ekspansi isotermal reversibel ke volume dua kali (suhu gas ideal tidak berubah pada ekspansi bebas), sehingga $\Delta S = R\ln2 = 5{,}76$ J K⁻¹ per mol. **6.2** $\Delta S = -R\ln0{,}1 = +19{,}1$ J K⁻¹; tekanan turun berarti volume bertambah, sehingga molekul mempunyai lebih banyak tempat. **6.3** Pada $x = \tfrac12$, yaitu $R\ln2 = 5{,}76$ J K⁻¹ mol⁻¹; pada $x = 0{,}1$, 2,70 J K⁻¹ mol⁻¹. **6.4** Penurunan entropi air tepat diimbangi kenaikan entropi lingkungan; es dan air berada dalam kesetimbangan dan dapat hidup berdampingan tanpa batas waktu. **6.5** Untuk $C_p$ tetap, Δ*S* bergantung pada **perbandingan** suhu, bukan selisihnya; keduanya melipatduakan suhu. **6.6** Ikatan kovalen intan yang sangat kaku dan atom karbon yang ringan membuat getaran kisinya berfrekuensi sangat tinggi, sehingga hampir tidak tereksitasi pada suhu kamar. **6.7** (a) Positif, karena terbentuk gas. (b) Hampir nol, jumlah mol gas tetap (nilainya +20 J K⁻¹ mol⁻¹, positif karena HCl kurang simetris). **6.8** Pada suhu rendah: Δ*H* negatif menguntungkan, Δ*S* negatif merugikan, dan suku entalpi lebih menentukan pada suhu rendah.

# Pertanyaan

1. Mengapa entropi gas ideal bertambah bila suhunya naik? Jelaskan dengan gambaran molekul.
2. Tunjukkan bahwa (6.1) memberi Δ*S* = 0 untuk proses adiabatik reversibel, tetapi tidak untuk ekspansi bebas.
3. Mengapa kenaikan tekanan pada suhu tetap menurunkan entropi gas?
4. Mengapa entropi pencampuran selalu positif?
5. Apa isi paradoks Gibbs dan bagaimana penyelesaiannya?
6. Jelaskan strategi menghitung Δ*S* untuk proses tak reversibel seperti pembekuan air lewat dingin.
7. Mengapa titik leleh adalah suhu ketika $\Delta S_\text{total}$ untuk peleburan sama dengan nol?
8. Mengapa entropi dapat mempunyai nilai mutlak, sedangkan energi dalam dan entalpi tidak?
9. Mengapa hukum *T*³ Debye diperlukan dalam pengukuran entropi mutlak?
10. Mengapa sumbangan terbesar pada entropi suatu gas pada suhu kamar biasanya berasal dari penguapan?
11. Mengapa entropi standar unsur tidak nol, padahal entalpi pembentukan standarnya nol?
12. Jelaskan mengapa entropi molar standar Ar lebih besar daripada He.
13. Mengapa perubahan jumlah mol gas biasanya menentukan tanda entropi reaksi?
14. Jelaskan keempat kombinasi tanda Δ*H* dan Δ*S* serta akibatnya pada spontanitas.
15. Mengapa reaksi yang spontan pada suhu kamar, seperti sintesis amonia, tetap memerlukan katalis?

# Soal

%%SOAL%%

# Jawaban

%%JAWABAN%%

# Pembahasan soal terpilih

**Soal {{campurT}}.** (a) Wadah kaku dan terisolasi, sehingga *q* = 0, *w* = 0, dan Δ*U* = 0. Kedua gas monoatomik mempunyai $C_{V,\text{m}} = \tfrac32R$ yang sama, sehingga kalor yang dilepas Ar sama dengan yang diterima He: $\tfrac32R(T - 300) = \tfrac32R(400 - T)$, dan $T = 350$ K.

Untuk (b): entropi fungsi keadaan, jadi kita pilih jalan reversibel yang mudah: setiap gas diubah suhunya pada volume tetap, lalu dimuaikan secara isotermal ke volume total 2*V*. Dengan (6.1):
$$
\Delta S = \tfrac32R\left(\ln\frac{350}{300} + \ln\frac{350}{400}\right) + 2R\ln2 = 0{,}26 + 11{,}53 = +11{,}78\ \text{J K}^{-1} .
$$
Sumbangan termal positif walaupun kalor yang berpindah sama besar: He menerima kalor pada suhu yang lebih rendah, sehingga entropi yang diperolehnya lebih besar daripada yang hilang dari Ar (bandingkan Contoh 5.12). Tetapi sumbangan itu kecil dibanding entropi pencampuran, karena selisih suhunya tidak besar. Sistem terisolasi, sehingga Δ*S* ini adalah Δ*S* total, dan positif sesuai (5.12).

**Soal {{benzen}}.** Jalan reversibel melalui titik leleh normal (278,6 K):
$$
\Delta S_\text{sistem} = 136{,}1\ln\frac{278{,}6}{268{,}6} - \frac{9870}{278{,}6} + 122{,}0\ln\frac{268{,}6}{278{,}6} = 4{,}98 - 35{,}43 - 4{,}46 = -34{,}9\ \text{J K}^{-1} .
$$
Entalpi dengan jalan yang sama: $\Delta H = (136{,}1)(10) - 9870 - (122{,}0)(10) = -9729$ J. Lingkungan pada 268,6 K: $\Delta S_\text{lingk} = 9729/268{,}6 = +36{,}2$ J K⁻¹. Total $+1{,}3$ J K⁻¹: pembekuan spontan.

*Cara berpikir:* setiap langkah jalan khayal harus reversibel dan menghubungkan keadaan awal dan akhir yang **sama** dengan proses sebenarnya. Untuk lingkungan, sebaliknya, yang dipakai adalah kalor **sebenarnya** yang dilepaskan pada suhu sebenarnya.

**Soal {{adiabeku}}.** (a) Termos terisolasi dan tekanannya tetap, sehingga $\Delta H = 0$. Bayangkan jalan dua langkah: seluruh air dipanaskan sebagai cairan dari −10 °C ke 0 °C, lalu sebagian *f* membeku pada 0 °C. Kalor untuk langkah pertama harus disediakan oleh langkah kedua: $f(6010) = (75{,}3)(10)$, sehingga $f = 0{,}125$. Hanya seperdelapan air yang membeku.

Untuk (b), kita memakai jalan yang sama:
$$
\Delta S = 75{,}3\ln\frac{273{,}15}{263{,}15} - \frac{(0{,}125)(6010)}{273{,}15} = 2{,}81 - 2{,}76 = +0{,}05\ \text{J K}^{-1} .
$$
Karena termos terisolasi, tidak ada kalor yang masuk ke lingkungan, $\Delta S_\text{lingk} = 0$, dan Δ*S* sistem adalah Δ*S* total. Hasilnya positif, sesuai dengan (5.12): proses spontan dalam sistem terisolasi menaikkan entropi. Nilainya kecil karena keadaan akhir (es dan air pada 0 °C) sudah setimbang; yang tak reversibel hanyalah awal prosesnya.

**Soal {{numerik}}.** Di bawah 10 K: $S(10) = C_p(10)/3 = 0{,}14$ J K⁻¹ mol⁻¹. Di atas 10 K, integral $\int C_p/T\,dT$ dihitung dengan aturan trapesium:

```python
import numpy as np
T  = np.array([10, 20, 50, 100, 150, 200, 250, 298.15])
Cp = np.array([0.43, 3.1, 14.2, 21.5, 23.8, 24.6, 25.0, 25.3])
S = Cp[0]/3 + np.trapezoid(Cp/T, T)
print(S)          # 46.6 J/(K mol)
```

*Cara berpikir:* hampir separuh entropi berasal dari daerah di bawah 100 K, walaupun kapasitas kalor di sana kecil, karena dibagi suhu yang kecil pula. Karena itulah pengukuran kalorimetri entropi harus dimulai pada suhu serendah mungkin. Dengan titik data yang lebih rapat, hasilnya lebih teliti; aturan trapesium dengan titik yang jarang cenderung meleset beberapa persen.

**Soal {{pauling}}.** (a) Setiap atom H mempunyai dua posisi, sehingga ada $2^{2N}$ susunan. (b) Dari $2^4 = 16$ susunan empat atom H di sekitar satu O, yang tepat dua dekat ada $\binom{4}{2} = 6$. Jadi hanya 6/16 susunan yang memenuhi syarat untuk setiap O. (c) Pauling menganggap syarat di setiap O bebas satu sama lain, sehingga
$$
W = 2^{2N}\left(\frac{6}{16}\right)^N = \left(4 \times \frac{6}{16}\right)^N = \left(\frac32\right)^N , \qquad S = k\ln W = Nk\ln\frac32 .
$$
Per mol, $S = R\ln\tfrac32 = 3{,}37$ J K⁻¹ mol⁻¹, sangat dekat dengan entropi residu es terukur, sekitar 3,4 J K⁻¹ mol⁻¹ (Contoh 5.16).

**Soal {{tanur}}.** $\Delta_\text{r}H^\circ = 3(-110{,}53) - (-824{,}2) = +492{,}6$ kJ mol⁻¹. $\Delta_\text{r}S^\circ = 2(27{,}28) + 3(197{,}67) - 87{,}4 - 3(5{,}74) = +543{,}0$ J K⁻¹ mol⁻¹. Suhu peralihan:
$$
T = \frac{\Delta_\text{r}H^\circ}{\Delta_\text{r}S^\circ} = \frac{492\,600}{543{,}0} = 907\ \text{K} \approx 630\ ^\circ\text{C} .
$$

*Cara berpikir:* reduksi bijih besi dengan karbon sangat endoterm, tetapi menghasilkan tiga mol gas CO dari padatan, sehingga entropinya naik sangat besar. Di atas sekitar 900 K entropi menang. Tanur tinggi bekerja jauh di atas suhu ini (lebih dari 1500 °C di bagian bawah), baik untuk mempercepat reaksi maupun untuk mencairkan besi yang terbentuk.

# Bacaan lanjut

1. P. Atkins, J. de Paula, dan J. Keeler, *Atkins' Physical Chemistry*, edisi ke-12 (Oxford University Press, 2023), Topik 3B–3C. Perubahan entropi, hukum ketiga, dan entropi reaksi.
2. I. N. Levine, *Physical Chemistry*, edisi ke-6 (McGraw-Hill, 2009), Bab 3 dan 5. Perhitungan entropi dan entropi ketiga hukum.
3. W. F. Giauque dan J. O. Clayton, "The heat capacity and entropy of nitrogen", *J. Am. Chem. Soc.* **55**, 4875–4889 (1933). Contoh klasik penentuan entropi kalorimetri.
4. D. A. McQuarrie dan J. D. Simon, *Molecular Thermodynamics* (University Science Books, 1999), Bab 21. Perbandingan entropi kalorimetri dan entropi statistik.
