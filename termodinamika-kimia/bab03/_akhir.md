# Ringkasan Bab 3

| Gagasan | Rumus atau hasil | Subbab |
|---|---|---|
| Fungsi keadaan | Δ*U* hanya bergantung pada keadaan awal dan akhir; *q* dan *w* bergantung pada jalan | 3.1 |
| Konvensi IUPAC | *q*, *w* positif bila energi masuk ke sistem; $w = -W_\text{fisika}$ | 3.1 |
| Kerja ekspansi | $dw = -p_\text{ex}\,dV$; $p_\text{ex}$ tetap: $w = -p_\text{ex}\Delta V$; ruang hampa: $w = 0$ | 3.2 |
| Reaksi yang menghasilkan gas | $w = -\Delta n_\text{gas}RT$ | 3.2 |
| Isotermal reversibel | $w = -nRT\ln(V_2/V_1)$; kerja ekspansi maksimum | 3.3, 3.7 |
| Kalor | $q = C\Delta T$; $C_\text{m} = C/n$; $c_s = C/m$; kalibrasi listrik $q = I\mathcal Et$ | 3.4 |
| Hukum pertama | $\Delta U = q + w$; sistem terisolasi: $\Delta U = 0$ | 3.5 |
| Diferensial eksak | $M\,dx + N\,dy$ eksak bila $(\partial M/\partial y)_x = (\partial N/\partial x)_y$ | 3.6 |
| Gas ideal | *U* hanya fungsi *T*; $dU = nC_{V,\text{m}}dT$; isotermal: $\Delta U = 0$, $q = -w$ | 3.7 |
| Adiabatik reversibel | $TV^{\gamma - 1}$, $pV^\gamma$, $Tp^{(1-\gamma)/\gamma}$ tetap; $w = \Delta U = nC_{V,\text{m}}\Delta T$ | 3.8 |
| Ekuipartisi | ½*RT* per suku kuadrat per mol; $C_{V,\text{m}}$: monoatomik $\tfrac32R$, linear $\tfrac52R$, tak linear $3R$ (tanpa getaran) | 3.9 |
| Getaran kuantum | $C_{V,\text{m}}^\text{get} = Rx^2e^x/(e^x - 1)^2$, $x = hc\tilde\nu/kT$ | 3.9 |

**Jawaban kuis cepat.** **3.1** Sebagai kerja: gerakan tangan yang teratur melawan gesekan. Kenaikan suhu yang menyusul bukan bukti bahwa energi masuk sebagai kalor. **3.2** Nol, karena volume tidak berubah; energi yang dilepas reaksi seluruhnya menjadi kalor atau menaikkan suhu isi bejana. **3.3** Pada proses reversibel. Untuk memampatkan, tekanan luar harus sedikitnya sama dengan tekanan gas; proses satu tahap memakai tekanan luar sebesar tekanan akhir sepanjang jalan, sehingga kerjanya lebih besar (2,48 kJ dibanding 1,72 kJ). **3.4** Etanol, 4,184/2,44 = 1,71 kali kenaikan suhu air. **3.5** Sistem gabungan terisolasi, jadi $\Delta U = 0$. Campuran reaksi saja melepaskan energi ke dinding kalorimeter, jadi Δ*U*-nya negatif. **3.6** $\Delta U = 0$ karena *U* fungsi keadaan. *q* dan *w* tidak harus nol, tetapi jumlahnya nol: $q = -w$. Mesin kalor bekerja tepat dengan cara ini. **3.7** Seluruhnya dipakai gas untuk melakukan kerja pada lingkungan; energi dalam tidak berubah. **3.8** Udara yang turun masuk ke tekanan lebih tinggi dan dimampatkan hampir adiabatik, sehingga suhunya naik, sampai sekitar 10 K per kilometer turun. Ketika naik di sisi gunung yang lain, udara itu mendingin di bawah titik embun; uap airnya mengembun menjadi awan dan jatuh sebagai hujan, sehingga yang turun ke Probolinggo adalah udara yang sudah kering. **3.9** Gas monoatomik hanya mempunyai translasi, yang selalu aktif penuh. Getaran Cl₂ baru sebagian aktif pada suhu kamar dan makin aktif bila suhu naik.

# Pertanyaan

1. Mengapa nilai mutlak energi dalam tidak dapat (dan tidak perlu) diketahui?
2. Bedakan kerja dan kalor dari sudut gerak molekul.
3. Mengapa kerja ekspansi dihitung dengan tekanan luar, bukan tekanan gas?
4. Mengapa reaksi yang menghasilkan gas melakukan kerja walaupun tidak ada piston?
5. Jelaskan dengan diagram *p*–*V* mengapa kerja ekspansi bertahap selalu lebih kecil daripada kerja ekspansi reversibel.
6. Apa arti "reversibel" dalam termodinamika, dan mengapa tidak ada proses nyata yang benar-benar reversibel?
7. Mengapa $C_p$ selalu lebih besar daripada $C_V$?
8. Bagaimana percobaan Joule membuktikan bahwa kalor bukan zat, melainkan energi?
9. Mengapa mesin abadi jenis pertama mustahil?
10. Jelaskan perbedaan diferensial eksak dan tak eksak dengan contoh dari kehidupan sehari-hari.
11. Mengapa energi dalam gas ideal hanya bergantung pada suhu, sedangkan energi dalam gas nyata juga bergantung pada volume?
12. Mengapa adiabat lebih curam daripada isoterm pada diagram *p*–*V*?
13. Jelaskan mengapa pompa sepeda menjadi panas dan kaleng semprot menjadi dingin.
14. Apa isi asas ekuipartisi, dan mengapa asas itu gagal untuk getaran molekul pada suhu kamar?
15. Mengapa γ gas monoatomik lebih besar daripada γ gas poliatomik?

# Soal

%%SOAL%%

# Jawaban

%%JAWABAN%%

# Pembahasan soal terpilih

**Soal {{tahap}}.** Pada tahap ke-*k*, volume naik dari $V_{k-1}$ ke $V_k$ melawan tekanan luar $nRT/V_k$, sehingga $w = -\sum_k (nRT/V_k)(V_k - V_{k-1})$:

```python
import numpy as np
R, T = 8.314, 298.15
def w(N, V1=0.010, V2=0.020):
    V = np.linspace(V1, V2, N + 1)
    return -np.sum(R*T/V[1:] * np.diff(V))
for N in [1, 2, 5, 10, 100, 1000]:
    print(N, round(w(N)))       # -1239 -1446 -1601 -1658 -1712 -1718
```

Kerja mendekati $-RT\ln2 = -1718$ J ketika *N* bertambah.

*Cara berpikir:* jumlah ini adalah luas sekumpulan persegi panjang di bawah kurva tekanan gas (Gambar 3.1). Makin sempit persegi panjangnya, makin rapat mereka mengisi luas di bawah kurva, dan batasnya adalah integral (3.4). Proses reversibel adalah limit proses bertahap ketika jumlah tahapnya tak terhingga.

**Soal {{jalan}}.** Untuk gas ideal monoatomik, $\Delta U = \tfrac32nR\Delta T = \tfrac32(p_2V_2 - p_1V_1) = \tfrac32(30 - 20)$ bar L $= 15$ bar L $= 1500$ J untuk kedua jalan.

Jalan A: tekanan tetap 2,00 bar dari 10,0 ke 30,0 L, lalu volume tetap. $w = -(2{,}00)(20{,}0)$ bar L $= -4000$ J, $q = \Delta U - w = 5500$ J.

Jalan B: volume tetap dari 2,00 ke 1,00 bar (gas didinginkan), lalu tekanan tetap 1,00 bar dari 10,0 ke 30,0 L. $w = -(1{,}00)(20{,}0)$ bar L $= -2000$ J, $q = 3500$ J.

*Cara berpikir:* pada jalan A, gas memuai pada tekanan lebih tinggi sehingga melakukan kerja lebih banyak, dan untuk membayarnya ia harus menerima kalor lebih banyak. Selisih *q* kedua jalan tepat sama dengan selisih *w*-nya (2000 J), sehingga Δ*U* sama.

**Soal {{adb}}.** Dari $T = pV/nR$: $(pV/nR)V^{\gamma - 1} = \text{tetap}$, sehingga $pV^\gamma = \text{tetap}$ (*n* dan *R* tetap). Dari $V = nRT/p$: $T(nRT/p)^{\gamma - 1} = \text{tetap}$, sehingga $T^\gamma p^{1 - \gamma} = \text{tetap}$, atau $Tp^{(1 - \gamma)/\gamma} = \text{tetap}$.

*Cara berpikir:* ketiga bentuk adalah persamaan yang sama, dinyatakan dengan pasangan variabel yang berbeda. Pilih bentuk yang memuat dua variabel yang diketahui dalam soal; bentuk ketiga paling berguna bila tekanan diberikan, seperti pada pompa sepeda.

**Soal {{br2}}.** $x = hc\tilde\nu/kT = (1{,}4388\ \text{cm K})(323\ \text{cm}^{-1})/(298{,}15\ \text{K}) = 1{,}559$. Maka
$$
C_{V,\text{m}}^\text{get} = (8{,}314)\frac{(1{,}559)^2e^{1{,}559}}{(e^{1{,}559} - 1)^2} = 6{,}82\ \text{J K}^{-1}\text{mol}^{-1} ,
$$
dan $C_{V,\text{m}} = 20{,}79 + 6{,}82 = 27{,}6$ J K⁻¹ mol⁻¹.

*Cara berpikir:* Br₂ lebih berat dan ikatannya lebih lemah daripada Cl₂, sehingga frekuensi getarannya lebih rendah dan getarannya lebih "bangun" pada suhu kamar (6,8 dari 8,3 J K⁻¹ mol⁻¹, dibanding 4,7 untuk Cl₂). Urutan N₂ < Cl₂ < Br₂ dalam kapasitas kalor adalah urutan frekuensi getaran yang makin rendah.

# Bacaan lanjut

1. P. Atkins, J. de Paula, dan J. Keeler, *Atkins' Physical Chemistry*, edisi ke-12 (Oxford University Press, 2023), Topik 2A–2E. Kerja, kalor, hukum pertama, dan perubahan adiabatik.
2. I. N. Levine, *Physical Chemistry*, edisi ke-6 (McGraw-Hill, 2009), Bab 2. Pembahasan yang teliti tentang proses reversibel dan diferensial eksak.
3. H. B. Callen, *Thermodynamics and an Introduction to Thermostatistics*, edisi ke-2 (Wiley, 1985), Bab 1. Dasar-dasar termodinamika yang sangat jernih untuk pembaca yang ingin lebih dalam.
4. D. A. McQuarrie dan J. D. Simon, *Molecular Thermodynamics* (University Science Books, 1999), Bab 3–4. Kapasitas kalor dari sudut molekul dan mekanika statistik.

**Soal {{eksakq}}.** (a) Dalam bentuk $M\,dT + N\,dV$, $M = C_{V,\text{m}}$ dan $N = RT/V$. Maka $(\partial M/\partial V)_T = 0$, sedangkan $(\partial N/\partial T)_V = R/V$. Keduanya tidak sama, jadi tidak ada fungsi keadaan yang diferensialnya $dq_\text{rev}$. (b) Setelah dibagi *T*, $M = C_{V,\text{m}}/T$ dan $N = R/V$. Kini $(\partial M/\partial V)_T = 0$ dan $(\partial N/\partial T)_V = 0$, sehingga $dq_\text{rev}/T$ eksak. Fungsinya $f = C_{V,\text{m}}\ln T + R\ln V$ + tetapan. Pembagian dengan *T* mengubah besaran yang bergantung pada jalan menjadi fungsi keadaan. Fungsi keadaan baru ini adalah entropi, tokoh utama Bab 5 dan 6.

**Soal {{adbtak}}.** Karena $q = 0$, $\Delta U = w$. Kerja melawan tekanan luar tetap $p_\text{ex} = p_2$ adalah $w = -p_2(V_2 - V_1) = -R(T_2 - T_1p_2/p_1)$. Menyamakannya dengan $\Delta U = \tfrac32R(T_2 - T_1)$:
$$
\tfrac32(T_2 - 300) = -(T_2 - 30) \quad\Rightarrow\quad T_2 = \frac{450 + 30}{2{,}5}\ \text{K} = 192\ \text{K} .
$$
Kerjanya $w = \tfrac32(8{,}314)(192 - 300)$ J $= -1{,}35$ kJ. Ekspansi reversibel (Contoh 3.12) mendinginkan gas sampai 119 K dan menghasilkan kerja 2,25 kJ. Ekspansi tak reversibel melakukan kerja lebih kecil, sehingga energi dalam yang terpakai lebih sedikit dan suhunya turun lebih sedikit. Ini sejalan dengan subbab 3.3: proses reversibel memberikan kerja terbesar.
