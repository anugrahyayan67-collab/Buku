import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import sisip, soal
N = 6
print(sisip(N, '6.1', r'''::: {.dalam}
**Lebih dalam: entropi gas nyata.** Penurunan (6.1) memakai $p/T = nR/V$, yang hanya berlaku untuk gas ideal. Untuk zat apa pun, Bab 7 akan menunjukkan (dengan hubungan Maxwell) bahwa
$$
dS = \frac{C_V}{T}dT + \left(\frac{\partial p}{\partial T}\right)_V dV .
$$
Untuk gas van der Waals, $p = nRT/(V - nb) - an^2/V^2$, sehingga $(\partial p/\partial T)_V = nR/(V - nb)$. Tetapan *a* tidak muncul sama sekali, dan perubahan entropi isotermalnya
$$
\Delta S = nR\ln\frac{V_2 - nb}{V_1 - nb} .
$$
Hasilnya sama dengan gas ideal, tetapi dengan volume "bebas" $V - nb$ sebagai ganti *V*. Masuk akal: entropi menghitung tempat yang tersedia bagi molekul, dan bagian volume yang ditempati molekul lain tidak tersedia.
:::

::: {.contoh}
**Contoh 6.t1 · Entropi ekspansi CO₂ nyata**

Satu mol CO₂ ($b = 0{,}042\,67$ L mol⁻¹) memuai secara isotermal dari 0,500 L ke 1,000 L. Hitung Δ*S* menurut persamaan van der Waals dan bandingkan dengan gas ideal.

**Penyelesaian.** Van der Waals: $\Delta S = R\ln\frac{1{,}000 - 0{,}0427}{0{,}500 - 0{,}0427} = (8{,}314)\ln2{,}093 = 6{,}14$ J K⁻¹. Gas ideal: $R\ln2 = 5{,}76$ J K⁻¹.

**Memahami hasil.** Gas nyata memperoleh entropi 7% lebih banyak, karena pada volume kecil sebagian ruang sudah "dipesan" oleh molekul-molekul lain, sehingga pelipatduaan volume total lebih dari melipatduakan ruang yang benar-benar bebas. Pada volume besar, *b* tidak berarti lagi dan kedua hasil menyatu.
:::''', 'Entropi ekspansi CO₂ nyata'))

print(sisip(N, '6.2', r'''::: {.contoh}
**Contoh 6.t2 · Mengisi tabung selam**

Udara diisikan ke tabung selam sampai 200 bar. Bila pemampatan dari 1 bar dilakukan pada suhu tetap 25 °C, hitung perubahan entropi per mol udara dan kalor minimum yang harus dibuang ke lingkungan.

**Penyelesaian.** Dari (6.3): $\Delta S = -R\ln200 = -44{,}1$ J K⁻¹ mol⁻¹. Pada proses isotermal reversibel, kalor yang dibuang $|q| = T|\Delta S| = (298{,}15)(44{,}1)$ J $= 13{,}1$ kJ per mol.

**Memahami hasil.** Penurunan entropi udara harus diimbangi kenaikan entropi lingkungan, dan itu terjadi lewat kalor yang dibuang. Inilah sebabnya kompresor tabung selam dilengkapi pendingin dan tabung yang baru diisi terasa hangat: bila kalor itu tidak dibuang, suhu udara di dalam tabung naik jauh dan tekanannya turun ketika tabung kemudian mendingin.
:::''', 'Mengisi tabung selam'))

print(sisip(N, '6.3', r'''::: {.contoh}
**Contoh 6.t3 · Pencampuran gas yang volumenya berbeda**

Satu mol He dalam wadah bervolume *V* dan satu mol Ar dalam wadah bervolume 3*V*, keduanya pada suhu yang sama, dihubungkan sehingga bercampur. Hitung Δ*S*.

**Penyelesaian.** Rumus (6.4) tidak dapat dipakai langsung karena tekanan awal kedua gas berbeda. Kembali ke prinsip: setiap gas memuai secara isotermal ke volume total 4*V*, tanpa memengaruhi gas lain. He: $R\ln(4V/V) = 11{,}53$ J K⁻¹. Ar: $R\ln(4V/3V) = 2{,}39$ J K⁻¹. Totalnya 13,92 J K⁻¹.

**Memahami hasil.** Helium, yang mula-mula paling terkurung, memperoleh kenaikan entropi terbesar. Rumus (6.4) hanyalah kasus khusus prinsip ini untuk gas-gas yang mula-mula bertekanan sama. Bila ragu, selalu kembali ke gambaran setiap gas memuai sendiri-sendiri.
:::''', 'Pencampuran gas yang volumenya berbeda'))

print(sisip(N, '6.5', r'''::: {.contoh}
**Contoh 6.t4 · Dari es ke uap**

Hitung perubahan entropi satu mol H₂O dari es pada −20 °C sampai uap pada 120 °C, pada tekanan 1 atm. Pakai $C_{p,\text{m}}$ es 37,7, air 75,3, uap 33,6 J K⁻¹ mol⁻¹; $\Delta_\text{fus}H = 6{,}01$ kJ mol⁻¹ (0 °C); $\Delta_\text{vap}H = 40{,}66$ kJ mol⁻¹ (100 °C).

**Penyelesaian.**

| Langkah | J K⁻¹ |
|---|---|
| Es 253 → 273 K: $37{,}7\ln(273{,}15/253{,}15)$ | 2,87 |
| Peleburan: 6010/273,15 | 22,00 |
| Air 273 → 373 K: $75{,}3\ln(373{,}15/273{,}15)$ | 23,49 |
| Penguapan: 40 660/373,15 | 108,96 |
| Uap 373 → 393 K: $33{,}6\ln(393{,}15/373{,}15)$ | 1,75 |
| **Jumlah** | **159,1** |

**Memahami hasil.** Dua pertiga kenaikan entropi berasal dari penguapan saja. Pemanasan air cair sejauh 100 K menyumbang sama besar dengan peleburan, karena kapasitas kalor air cair yang besar. Pola ini sama dengan argon pada Contoh 6.9: perubahan fasa, terutama penguapan, mendominasi entropi.
:::''', 'Dari es ke uap'))

print(sisip(N, '6.6', r'''::: {.terapan}
**Kaca dan entropi yang membeku.** Kaca jendela, plastik, dan permen keras adalah padatan **amorf**: molekul-molekulnya tersusun acak seperti cairan, tetapi tidak dapat bergerak. Ketika cairan pembentuk kaca didinginkan cukup cepat, molekul-molekulnya kehilangan kemampuan menata diri sebelum sempat membentuk kristal, dan ketidakteraturan cairan "membeku" di tempat. Akibatnya kaca mempunyai entropi residu pada 0 K, seperti CO dan es, tetapi jauh lebih besar. Kaca tidak berada dalam kesetimbangan: secara termodinamika ia "ingin" mengkristal, tetapi lajunya pada suhu kamar dapat lebih lambat daripada umur semesta. Hukum ketiga hanya berlaku untuk kristal **sempurna** dalam kesetimbangan.
:::''', 'Kaca dan entropi yang membeku'))

print(sisip(N, '6.7', r'''::: {.contoh}
**Contoh 6.t5 · Ion yang menata air**

Entropi molar standar ion dalam larutan (J K⁻¹ mol⁻¹): Na⁺(aq) 59,0; Mg²⁺(aq) −138,1; Cl⁻(aq) 56,5. Entropi padatan: NaCl 72,13; MgCl₂ 89,62. Hitung entropi pelarutan standar NaCl dan MgCl₂.

**Penyelesaian.** NaCl: $59{,}0 + 56{,}5 - 72{,}13 = +43{,}4$ J K⁻¹ mol⁻¹. MgCl₂: $-138{,}1 + 2(56{,}5) - 89{,}62 = -114{,}7$ J K⁻¹ mol⁻¹.

**Memahami hasil.** Mengejutkan: pelarutan MgCl₂ **menurunkan** entropi, padahal ion-ion yang semula terkunci dalam kristal menjadi bebas bergerak. Penyebabnya adalah air. Ion Mg²⁺ kecil dan bermuatan dua, sehingga medan listriknya sangat kuat dan menata molekul-molekul air di sekitarnya menjadi selubung hidrasi yang sangat teratur. Keteraturan air itu lebih besar daripada kebebasan yang diperoleh ion. Entropi ion dalam larutan diukur relatif terhadap H⁺(aq), yang ditetapkan nol; karena itu nilai negatif seperti Mg²⁺ dimungkinkan.
:::''', 'Ion yang menata air'))

print(sisip(N, '6.8', r'''::: {.contoh}
**Contoh 6.t6 · Mengapa air tidak mendidih pada 25 °C**

Untuk $\text{H}_2\text{O}(l) \to \text{H}_2\text{O}(g)$ pada 298 K, $\Delta_\text{vap}H^\circ = 44{,}01$ kJ mol⁻¹ dan $\Delta_\text{vap}S^\circ = 118{,}9$ J K⁻¹ mol⁻¹. (a) Hitung $\Delta S_\text{total}$ untuk penguapan menjadi uap bertekanan 1 bar. (b) Taksir titik didih normal air.

**Penyelesaian.** (a) $\Delta S_\text{total} = 118{,}9 - 44\,010/298{,}15 = -28{,}7$ J K⁻¹ mol⁻¹ < 0: tidak spontan. (b) $T = 44\,010/118{,}9 = 370$ K, sekitar 97 °C.

**Memahami hasil.** Pada 25 °C, air tidak dapat menguap menjadi uap **bertekanan 1 bar**. Tetapi air tetap menguap dari gelas yang terbuka, karena uap di udara bertekanan parsial jauh lebih kecil daripada 1 bar, dan entropi uap bertambah ketika tekanannya lebih rendah (persamaan 6.3). Penguapan berhenti ketika tekanan uap air di atas cairan mencapai tekanan uap jenuhnya, sekitar 0,032 bar pada 25 °C. Hubungan antara tekanan uap dan suhu akan kita turunkan di Bab 8. Taksiran titik didih meleset 3 K karena Δ*H* dan Δ*S* dianggap tetap dari 25 °C sampai 100 °C.
:::''', 'Mengapa air tidak mendidih pada 25 °C'))

soal(N, '6.1', [r'Dua mol CO₂ memuai secara isotermal dari 0,200 L ke 2,00 L. Hitung Δ*S* menurut van der Waals ($b = 0{,}042\,67$ L mol⁻¹, per mol) dan gas ideal. ||| per mol: 0,100 → 1,00 L mol⁻¹; van der Waals 21,0; ideal 19,1 J K⁻¹ mol⁻¹'])
soal(N, '6.2', [r'Berapa kalor minimum yang dibuang per mol bila udara dimampatkan secara isotermal pada 25 °C dari 1 bar ke 200 bar? ||| 13,1 kJ'])
soal(N, '6.3', [r'Satu mol He dalam *V* dan satu mol Ar dalam 3*V* dicampur pada suhu sama. Hitung Δ*S*. ||| +13,9 J K⁻¹',
                r'Hitung entropi pencampuran 3,00 mol gas yang terdiri atas tiga komponen dengan jumlah mol sama. ||| +27,4 J K⁻¹'])
soal(N, '6.5', [r'Hitung Δ*S* satu mol air dari cair 50 °C ke uap 150 °C pada 1 atm (data Contoh 6.t4). ||| +124 J K⁻¹'])
soal(N, '6.7', [r'Mengapa entropi pelarutan MgCl₂ negatif, sedangkan NaCl positif? ||| Mg²⁺ kecil bermuatan 2+ menata air hidrasi sangat kuat'])
soal(N, '6.8', [r'Taksir titik didih normal air dari $\Delta_\text{vap}H^\circ$ dan $\Delta_\text{vap}S^\circ$ pada 298 K. Mengapa tidak tepat 373 K? ||| 370 K; Δ*H*, Δ*S* berubah dengan suhu',
                r'Mengapa air tetap menguap dari gelas terbuka pada 25 °C, walaupun $\Delta S_\text{total}$ penguapan standar negatif? ||| tekanan parsial uap di udara jauh di bawah 1 bar'])
