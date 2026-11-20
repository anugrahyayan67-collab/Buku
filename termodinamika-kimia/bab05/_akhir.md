# Ringkasan Bab 5

| Gagasan | Rumus atau hasil | Subbab |
|---|---|---|
| Proses spontan | terjadi dengan sendirinya; kebalikannya tidak; laju diatur kinetika | 5.1 |
| Mesin kalor | $|w| = q_\text{h} - |q_\text{c}|$; $\eta = |w|/q_\text{h} = 1 - |q_\text{c}|/q_\text{h}$ | 5.2 |
| Hukum kedua (Kelvin, Clausius) | kalor tidak dapat diubah seluruhnya menjadi kerja dalam siklus; kalor tidak mengalir sendiri dari dingin ke panas | 5.2 |
| Siklus Carnot | 2 isoterm reversibel + 2 adiabat reversibel; $V_\text{B}/V_\text{A} = V_\text{C}/V_\text{D}$ | 5.3 |
| Efisiensi Carnot | $|q_\text{c}|/q_\text{h} = T_\text{c}/T_\text{h}$; $\eta = 1 - T_\text{c}/T_\text{h}$ | 5.4 |
| Koefisien kinerja | pendingin $T_\text{c}/(T_\text{h} - T_\text{c})$; pompa kalor $T_\text{h}/(T_\text{h} - T_\text{c})$ | 5.5 |
| Entropi | $dS = dq_\text{rev}/T$; fungsi keadaan; $\oint dq_\text{rev}/T = 0$ | 5.6 |
| Δ*S* sederhana | isotermal gas ideal $nR\ln(V_2/V_1)$; transisi $\Delta_\text{trs}H/T_\text{trs}$; pemanasan $C_p\ln(T_2/T_1)$ | 5.6 |
| Ketaksamaan Clausius | $dS \ge dq/T$; terisolasi: $\Delta S \ge 0$ | 5.7 |
| Spontanitas | $\Delta S_\text{total} = \Delta S_\text{sistem} + \Delta S_\text{lingk} > 0$; $\Delta S_\text{lingk} = -q_\text{sistem}/T = -\Delta H/T$ | 5.7 |
| Boltzmann | $S = k\ln W$; entropi residu $R\ln2$ (CO), $R\ln\tfrac32$ (es) | 5.8 |

**Jawaban kuis cepat.** **5.1** Tidak. Contohnya perkaratan besi, atau perubahan intan menjadi grafit, yang spontan tetapi tidak teramati dalam miliaran tahun. **5.2** Hukum kedua (pernyataan Kelvin): kapal itu akan mengubah kalor dari satu sumber seluruhnya menjadi kerja dalam siklus tanpa membuang kalor ke penampung yang lebih dingin. **5.3** Suhu berubah pada kedua tahap adiabatik; kalor dipertukarkan pada kedua tahap isotermal. **5.4** Menurunkan $T_\text{c}$: η naik dari 0,500 ke 0,517, sedangkan menaikkan $T_\text{h}$ hanya memberi 0,508. **5.5** Tidak. Kulkas membuang ke dapur kalor yang diambilnya ditambah kerja listriknya, sehingga dapur justru makin panas. **5.6** Sama: entropi fungsi keadaan, dan keadaan awal serta akhir gas sama. Yang berbeda adalah perubahan entropi lingkungan. **5.7** Pembekuan melepaskan kalor ke lingkungan, sehingga entropi lingkungan naik; kenaikan itu sedikit lebih besar daripada penurunan entropi air. **5.8** Nol, karena $W = 1$ dan $\ln1 = 0$. Inilah isi hukum ketiga (Bab 6).

# Pertanyaan

1. Mengapa hukum pertama tidak dapat menentukan arah suatu proses?
2. Berikan tiga contoh proses spontan dan jelaskan masing-masing sebagai penyebaran materi atau energi.
3. Mengapa setiap mesin kalor harus membuang sebagian kalor ke penampung yang lebih dingin?
4. Jelaskan dengan kata-katamu sendiri kesetaraan pernyataan Kelvin dan Clausius.
5. Mengapa siklus Carnot harus terdiri atas dua isoterm dan dua adiabat?
6. Mengapa efisiensi Carnot tidak bergantung pada zat kerja mesin?
7. Mengapa pembangkit listrik berusaha memakai uap sepanas mungkin?
8. Mengapa koefisien kinerja pompa kalor dapat lebih besar dari 1 tanpa melanggar hukum pertama?
9. Apa yang membuat $q_\text{rev}/T$ menjadi fungsi keadaan, padahal $q_\text{rev}$ sendiri bukan?
10. Mengapa Δ*S* sistem dihitung sepanjang jalan reversibel walaupun prosesnya tak reversibel?
11. Mengapa penguapan mempunyai perubahan entropi jauh lebih besar daripada peleburan?
12. Apa arti "entropi diciptakan" dalam proses tak reversibel?
13. Jelaskan mengapa kompres dingin bekerja walaupun prosesnya endoterm.
14. Apa yang dihitung oleh *W* dalam rumus Boltzmann?
15. Mengapa hukum kedua, walaupun bersifat statistik, tidak pernah dilanggar dalam sistem makroskopik?
16. Apa asal entropi residu CO dan es?

# Soal

%%SOAL%%

# Jawaban

%%JAWABAN%%

# Pembahasan soal terpilih

**Soal {{carnot}}.** Untuk gas diatomik, $\gamma = 7/5$ dan $1/(\gamma - 1) = 5/2$. Volume ujung adiabat:
$$
V_\text{C} = V_\text{B}\left(\frac{T_\text{h}}{T_\text{c}}\right)^{5/2} = (15{,}0)(2)^{2{,}5} = 84{,}9\ \text{L} , \qquad V_\text{D} = (5{,}00)(2)^{2{,}5} = 28{,}3\ \text{L} .
$$
Kalor tahap isotermal: $q_\text{h} = nRT_\text{h}\ln(V_\text{B}/V_\text{A}) = (2)(8{,}314)(600)\ln3 = +10{,}96$ kJ dan $q_\text{c} = -(2)(8{,}314)(300)\ln3 = -5{,}48$ kJ. Kerja ekspansi adiabatik: $w = nC_{V,\text{m}}\Delta T = (2)(\tfrac52)(8{,}314)(-300) = -12{,}47$ kJ. Efisiensi: $(10{,}96 - 5{,}48)/10{,}96 = 0{,}50 = 1 - 300/600$.

*Cara berpikir:* kerja tahap adiabatik (12,47 kJ) lebih besar daripada kalor yang diterima (10,96 kJ), tetapi tidak ada yang aneh: kerja itu dibayar oleh energi dalam gas dan dikembalikan pada tahap adiabatik kompresi. Yang menentukan efisiensi hanya kedua tahap isotermal.

**Soal {{beku}}.** Lingkungan pada −10 °C (263,15 K) menerima kalor 5,63 kJ:
$$
\Delta S_\text{lingk} = \frac{+5630}{263{,}15} = +21{,}4\ \text{J K}^{-1} , \qquad \Delta S_\text{total} = -20{,}6 + 21{,}4 = +0{,}8\ \text{J K}^{-1} > 0 .
$$
Pembekuan spontan. (Nilai $\Delta H$ dan $\Delta S$ pada −10 °C dihitung dari nilai pada 0 °C dengan memperhitungkan perbedaan kapasitas kalor air dan es, cara yang akan dibahas di Bab 6.)

*Cara berpikir:* pada 0 °C, $\Delta S_\text{lingk} = 6010/273{,}15 = 22{,}0$ J K⁻¹ tepat mengimbangi $\Delta S_\text{sistem} = -22{,}0$ J K⁻¹: itulah keadaan setimbang. Di bawah 0 °C, kalor yang sama dibagi suhu yang lebih rendah, sehingga entropi lingkungan naik lebih banyak dan pembekuan menang. Di atas 0 °C, yang terjadi sebaliknya, dan es mencair.

**Soal {{pauling}}.** Dengan $W = (3/2)^{N_\text{A}}$:
$$
S_\text{residu} = k\ln\left(\tfrac32\right)^{N_\text{A}} = R\ln\tfrac32 = (8{,}314)(0{,}405) = 3{,}37\ \text{J K}^{-1}\text{mol}^{-1} .
$$

*Cara berpikir:* setiap atom O dikelilingi empat atom H, dua dekat (ikatan kovalen) dan dua jauh (ikatan hidrogen). Ada $\binom42 = 6$ cara memilih dua H yang dekat, tetapi setiap ikatan O···H–O juga harus konsisten dengan tetangganya, yang secara rata-rata memotong pilihan itu menjadi 3/2 per molekul. Kecocokan dengan pengukuran kalorimetri (3,4 J K⁻¹ mol⁻¹) membuktikan bahwa susunan proton dalam es memang acak.

# Bacaan lanjut

1. P. Atkins, J. de Paula, dan J. Keeler, *Atkins' Physical Chemistry*, edisi ke-12 (Oxford University Press, 2023), Topik 3A. Hukum kedua, mesin Carnot, dan entropi.
2. I. N. Levine, *Physical Chemistry*, edisi ke-6 (McGraw-Hill, 2009), Bab 3. Penurunan entropi yang sangat teliti dari mesin kalor.
3. P. W. Atkins, *Four Laws That Drive the Universe* (Oxford University Press, 2007). Pengantar populer yang jernih tentang keempat hukum termodinamika.
4. D. A. McQuarrie dan J. D. Simon, *Molecular Thermodynamics* (University Science Books, 1999), Bab 20. Entropi statistik dan rumus Boltzmann.
5. L. Pauling, "The structure and entropy of ice and of other crystals with some randomness of atomic arrangement", *J. Am. Chem. Soc.* **57**, 2680–2684 (1935).
