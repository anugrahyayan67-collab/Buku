# Ringkasan Bab 7

| Gagasan | Rumus atau hasil | Subbab |
|---|---|---|
| Kriteria tanpa lingkungan | pada *T*, *p* tetap: $\Delta G = -T\Delta S_\text{total}$ | 7.1 |
| Helmholtz | $A = U - TS$; $dA_{T,V} \le 0$; $|w|_\text{maks} = -\Delta A$ | 7.2 |
| Gibbs | $G = H - TS$; $dG_{T,p} \le 0$; $\Delta G = \Delta H - T\Delta S$ | 7.3 |
| Kerja bukan-ekspansi | $|w_\text{tambahan}|_\text{maks} = -\Delta G$; sel: $\Delta G = -nFE$ | 7.4 |
| Persamaan fundamental | $dU = TdS - pdV$; $dH = TdS + Vdp$; $dA = -SdT - pdV$; $dG = -SdT + Vdp$ | 7.5 |
| Turunan *G* | $(\partial G/\partial T)_p = -S$; $(\partial G/\partial p)_T = V$ | 7.5 |
| Hubungan Maxwell | $(\partial S/\partial V)_T = (\partial p/\partial T)_V$; $(\partial S/\partial p)_T = -(\partial V/\partial T)_p = -\alpha V$ | 7.6 |
| Tekanan dalam | $\pi_T = T(\partial p/\partial T)_V - p$; gas ideal 0; van der Waals $a/V_\text{m}^2$ | 7.6 |
| $C_p - C_V$ umum | $TV\alpha^2/\kappa_T$ | 7.6 |
| Gibbs–Helmholtz | $(\partial(G/T)/\partial T)_p = -H/T^2$; $\Delta G_2/T_2 = \Delta G_1/T_1 + \Delta H(1/T_2 - 1/T_1)$ | 7.7 |
| *G* dan tekanan | terkondensasi: $\Delta G = V\Delta p$; gas ideal: $G_\text{m} = G_\text{m}^\circ + RT\ln(p/p^\circ)$ | 7.8 |
| Energi Gibbs reaksi | $\Delta_\text{r}G^\circ = \sum\nu\Delta_\text{f}G^\circ(\text{hasil}) - \sum\nu\Delta_\text{f}G^\circ(\text{pereaksi})$ | 7.9 |

**Jawaban kuis cepat.** **7.1** Penurunannya memakai $q = \Delta H$, yang hanya berlaku pada tekanan tetap, dan $\Delta S_\text{lingk} = -\Delta H/T$, yang memerlukan suhu tetap. **7.2** Lebih besar. Tambahannya adalah kalor $T\Delta S$ yang diserap dari lingkungan. **7.3** Nol, karena cairan dan uap berada dalam kesetimbangan. **7.4** $\Delta S = (\Delta H - \Delta G)/T = +67$ J K⁻¹ mol⁻¹, positif. Kerja tambahan maksimumnya 120 kJ mol⁻¹. **7.5** Kemiringannya −*S*, dan entropi gas jauh lebih besar daripada cairan. **7.6** Berkurang: $(\partial S/\partial p)_T = -\alpha V < 0$ bila α positif. **7.7** Berkurang, karena $\partial(\Delta G/T)/\partial T = -\Delta H/T^2 < 0$ bila Δ*H* > 0; reaksi endoterm makin menguntungkan pada suhu tinggi. **7.8** Es, karena volume molarnya lebih besar. Akibatnya pada tekanan tinggi air cair menjadi lebih stabil pada 0 °C, dan titik leleh turun. **7.9** Intan terbentuk di dalam Bumi pada tekanan sangat tinggi, tempat ia stabil, lalu terbawa ke permukaan cukup cepat sehingga tidak sempat berubah menjadi grafit.

# Pertanyaan

1. Mengapa energi Gibbs disebut "bebas"? Bagian energi mana yang tidak bebas?
2. Jelaskan arti fisis suku *U* dan −*TS* dalam energi Helmholtz.
3. Mengapa energi Gibbs lebih berguna bagi kimiawan daripada energi Helmholtz?
4. Apa yang dimaksud kerja bukan-ekspansi? Berikan tiga contoh.
5. Jelaskan mengapa sel bahan bakar hidrogen dibatasi efisiensi 83%.
6. Bagaimana pembakaran glukosa dapat menghasilkan kerja lebih besar daripada kalornya tanpa melanggar hukum pertama?
7. Apa yang dimaksud variabel alami suatu fungsi termodinamika?
8. Mengapa hubungan Maxwell diturunkan dari sifat diferensial eksak?
9. Berikan satu contoh besaran yang sukar diukur yang dapat dihitung dengan hubungan Maxwell.
10. Apa arti fisis tekanan dalam, dan mengapa nilainya nol untuk gas ideal?
11. Mengapa *G* setiap zat turun bila suhu naik?
12. Jelaskan dengan Gambar 7.1 mengapa setiap zat akhirnya menguap pada suhu yang cukup tinggi.
13. Mengapa *G* gas jauh lebih peka terhadap tekanan daripada *G* cairan?
14. Apa yang dimaksud stabil secara termodinamika dan stabil secara kinetik? Berikan contohnya.
15. Mengapa ozon di stratosfer tetap ada walaupun penguraiannya spontan?

# Soal

%%SOAL%%

# Jawaban

%%JAWABAN%%

# Pembahasan soal terpilih

**Soal {{metanol}}.** Dari Tabel 7.1, dengan $\Delta_\text{f}G^\circ(\text{O}_2) = 0$:
$$
\Delta_\text{r}G^\circ = -394{,}36 + 2(-237{,}13) - (-166{,}27) = -702{,}4\ \text{kJ mol}^{-1} .
$$
Tegangan maksimum: $E = -\Delta_\text{r}G^\circ/nF = 702\,400/(6 \times 96\,485) = 1{,}21$ V.

*Cara berpikir:* banyaknya elektron dihitung dari perubahan bilangan oksidasi karbon (−2 dalam metanol menjadi +4 dalam CO₂) atau dari setengah reaksi oksigen ($\tfrac32$ O₂ menerima 6 elektron). Tegangan sel bahan bakar metanol hampir sama dengan sel hidrogen, karena keduanya pada dasarnya membentuk air dari hidrogen dan oksigen; yang berbeda adalah banyaknya elektron per molekul bahan bakar.

**Soal {{maxwell}}.** Untuk gas van der Waals, $p = nRT/(V - nb) - an^2/V^2$. Turunan terhadap *T* pada *V* tetap:
$$
\left(\frac{\partial p}{\partial T}\right)_V = \frac{nR}{V - nb} ,
$$
karena suku tarikan $-an^2/V^2$ tidak bergantung pada *T*. Menurut hubungan Maxwell ketiga, ini sama dengan $(\partial S/\partial V)_T$, yang tidak memuat *a*.

*Cara berpikir:* tarikan antarmolekul mengubah **energi** gas (tekanan dalam $an^2/V^2$), tetapi tidak mengubah banyaknya tempat yang tersedia bagi molekul, sehingga tidak mengubah entropinya. Hanya ukuran molekul (*b*) yang memengaruhi entropi.

**Soal {{hp}}.** (a) Bagi $dH = T\,dS + V\,dp$ dengan *dp* pada suhu tetap: $(\partial H/\partial p)_T = T(\partial S/\partial p)_T + V$. Hubungan Maxwell keempat mengganti $(\partial S/\partial p)_T$ dengan $-(\partial V/\partial T)_p = -\alpha V$, sehingga $(\partial H/\partial p)_T = V - TV\alpha = V(1 - \alpha T)$. (b) Untuk gas ideal, $\alpha = 1/T$, sehingga $1 - \alpha T = 0$: entalpi gas ideal tidak bergantung pada tekanan, sejalan dengan subbab 4.2. (c) Untuk air, $\alpha T = (2{,}07 \times 10^{-4})(298{,}15) = 0{,}062$, sehingga
$$
\Delta H_\text{m} \approx V_\text{m}(1 - \alpha T)\Delta p = (18{,}07 \times 10^{-6})(0{,}938)(1{,}00 \times 10^7)\ \text{J mol}^{-1} = 170\ \text{J mol}^{-1} .
$$
Hampir seluruhnya berasal dari suku $V\Delta p$; suku $-TV\alpha\Delta p$ hanya mengurangi 6%. Untuk cairan, Δ*H* karena tekanan biasanya diabaikan dibanding Δ*H* karena suhu: 170 J mol⁻¹ setara dengan memanaskan air sekitar 2 K.

**Soal {{gh}}.** Dari (7.13):
$$
\frac{\Delta G(1000)}{1000} = \frac{130{,}4}{298{,}15} + 178{,}3\left(\frac{1}{1000} - \frac{1}{298{,}15}\right) = 0{,}4374 - 0{,}4197 = 0{,}0176\ \text{kJ K}^{-1}\text{mol}^{-1} ,
$$
sehingga $\Delta G(1000\ \text{K}) = +17{,}6$ kJ mol⁻¹.

*Cara berpikir:* hasilnya sama dengan $\Delta H - T\Delta S = 178{,}3 - (1000)(0{,}1606) = +17{,}7$ kJ mol⁻¹, karena kedua cara memakai anggapan yang sama (Δ*H* tetap). Keuntungan Gibbs–Helmholtz baru terasa ketika Δ*S* tidak diketahui, atau ketika Δ*H* dinyatakan sebagai fungsi suhu dan persamaan (7.12) diintegralkan dengan lebih teliti.

**Soal {{virial}}.** Dari (7.9), $dG_\text{m} = V_\text{m}\,dp = (RT/p + B)\,dp$ pada suhu tetap. Mengintegralkan:
$$
\Delta G_\text{m} = RT\ln\frac{p_2}{p_1} + B(p_2 - p_1) .
$$
Untuk CO₂: suku ideal $(8{,}314)(273{,}15)\ln10 = 5229$ J mol⁻¹; suku virial $(-149{,}7 \times 10^{-6})(9{,}0 \times 10^5) = -135$ J mol⁻¹. Totalnya 5,09 kJ mol⁻¹, 2,6% lebih kecil daripada gas ideal. Tarikan antarmolekul (*B* negatif) membuat CO₂ lebih mudah dimampatkan, sehingga energi Gibbsnya naik lebih lambat. Suku koreksi inilah yang di subbab 9.5 akan diserap ke dalam **fugasitas**.

# Bacaan lanjut

1. P. Atkins, J. de Paula, dan J. Keeler, *Atkins' Physical Chemistry*, edisi ke-12 (Oxford University Press, 2023), Topik 3D–3E. Energi Helmholtz dan Gibbs, persamaan fundamental, dan hubungan Maxwell.
2. I. N. Levine, *Physical Chemistry*, edisi ke-6 (McGraw-Hill, 2009), Bab 4. Fungsi termodinamika dan hubungan Maxwell yang sangat sistematis.
3. H. B. Callen, *Thermodynamics and an Introduction to Thermostatistics*, edisi ke-2 (Wiley, 1985), Bab 5–7. Transformasi Legendre sebagai asal *H*, *A*, dan *G*.
4. D. Voet dan J. G. Voet, *Biochemistry*, edisi ke-4 (Wiley, 2011), Bab 3. Energi Gibbs dalam sel hidup dan peran ATP.
