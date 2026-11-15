# Ringkasan Bab 17

| Gagasan | Rumus | Subbab |
|---|---|---|
| Hamiltonian elektronik | $\hat H_\text{el} = -\sum_i\tfrac12\nabla_i^2 - \sum_{iA}Z_A/r_{iA} + \sum_{i<j}1/r_{ij}$ | 17.1 |
| Energi determinan | $E_0 = \sum_ih_{ii} + \tfrac12\sum_{ij}(J_{ij} - K_{ij})$; $\ $kulit tertutup $2\sum_ah_{aa} + \sum_{ab}(2J_{ab} - K_{ab})$ | 17.2 |
| Persamaan Hartree–Fock | $\hat f\chi_i = \varepsilon_i\chi_i$, $\ \hat f = \hat h + \sum_j(\hat J_j - \hat K_j)$ | 17.2 |
| Energi orbital dan total | $\varepsilon_i = h_{ii} + \sum_j(J_{ij} - K_{ij})$; $\ E_0 = \tfrac12\sum_i(\varepsilon_i + h_{ii})$ | 17.2 |
| Persamaan Roothaan | $\mathbf F\mathbf C = \mathbf S\mathbf C\boldsymbol\varepsilon$; $\ P_{\mu\nu} = 2\sum_aC_{\mu a}C_{\nu a}^*$ | 17.3 |
| Matriks Fock dan energi | $F_{\mu\nu} = H_{\mu\nu} + \sum_{\lambda\sigma}P_{\lambda\sigma}[(\mu\nu|\sigma\lambda) - \tfrac12(\mu\lambda|\sigma\nu)]$; $\ E_\text{el} = \tfrac12\sum P_{\nu\mu}(H_{\mu\nu} + F_{\mu\nu})$ | 17.3 |
| Teorema Koopmans | $\text{EI}_i \approx -\varepsilon_i$ | 17.4 |
| Ekstrapolasi CBS | $E^\text{kor}_X = E^\text{kor}_\text{CBS} + AX^{-3}$ | 17.5 |
| Counterpoise | $\Delta E^\text{CP} = E_{AB}(AB) - E_A(AB) - E_B(AB)$ | 17.5 |
| Muatan Mulliken; dipol | $q_A = Z_A - \sum_{\mu \in A}(\mathbf P\mathbf S)_{\mu\mu}$; $\ \boldsymbol\mu = \sum Z_A\mathbf R_A - \int\mathbf r\rho$ | 17.7 |
| Invariansi uniter | $\psi_i' = \sum_jU_{ji}\psi_j$ tidak mengubah $\Psi$, $\mathbf P$, $E$ | 17.8 |
| Langkah Newton; frekuensi | $\Delta\mathbf q = -\mathbf H^{-1}\mathbf g$; $\ \tilde\nu_k = \sqrt{\lambda_k}/2\pi c$ (Hessian berbobot massa) | 17.9 |
| Termokimia | $E_\text{ZPE} = \tfrac12\sum h\nu_k$; $\ H = E_\text{el} + E_\text{ZPE} + E_\text{term} + RT$; $\ G = H - TS$ | 17.9 |
| Energi korelasi | $E_\text{kor} = E_\text{tepat} - E_\text{HF}^\text{batas}$ | 17.10 |
| Interaksi konfigurasi | $\Psi = c_0\Phi_0 + \sum c_i^a\Phi_i^a + \sum c_{ij}^{ab}\Phi_{ij}^{ab} + \cdots$; $\ \Delta E_Q \approx (1 - c_0^2)E^\text{kor}_\text{CISD}$ | 17.10 |
| MP2 | $E^{(2)} = \sum_{ijab}(ia|jb)[2(ia|jb) - (ib|ja)]/(\varepsilon_i + \varepsilon_j - \varepsilon_a - \varepsilon_b)$ | 17.11 |
| Coupled-cluster | $\Psi = e^{\hat T}\Phi_0$, $\ \hat T = \hat T_1 + \hat T_2 + \cdots$; CCSD(T) $\propto N^7$ | 17.12 |
| Komposit | $E[\text{tinggi/besar}] \approx E[\text{tinggi/kecil}] + E[\text{rendah/besar}] - E[\text{rendah/kecil}]$ | 17.12 |
| Thomas–Fermi, Dirac | $T_\text{TF} = C_F\int\rho^{5/3}$; $\ E_x^\text{LDA} = -C_x\int\rho^{4/3}$ | 17.13 |
| Kohn–Sham | $[-\tfrac12\nabla^2 + v + v_H + v_{xc}]\phi_i = \varepsilon_i\phi_i$; $\ E = T_s + \int v\rho + J + E_{xc}$ | 17.13 |
| GGA; B3LYP | $E_x = \int\rho\,\varepsilon_x^\text{LDA}F_x(s)$; $\ E_{xc}^\text{B3LYP}$: 20% HF, 72% B88, 81% LYP | 17.14 |
| Dispersi; Born | $E_\text{disp} = -\sum C_6/R^6 f_\text{redam}$; $\ \Delta G = -\tfrac{N_Az^2e^2}{8\pi\varepsilon_0a}(1 - 1/\varepsilon_r)$ | 17.15 |
| Teori keadaan transisi | $k = \kappa\,(k_BT/h)\,e^{-\Delta G^\ddagger/RT}$; $\ \kappa_\text{W} = 1 + \tfrac{1}{24}(h|\nu^\ddagger|/k_BT)^2$ | 17.16 |
| ZDO; medan gaya | $(\mu\nu|\lambda\sigma) \approx \delta_{\mu\nu}\delta_{\lambda\sigma}(\mu\mu|\lambda\lambda)$; $\ E = \sum k_r(r - r_0)^2 + \cdots$ | 17.17 |

**Jawaban kuis cepat.** **17.1** Fungsional B3LYP dengan basis 6-31G*; energi CCSD(T)/cc-pVTZ pada geometri yang dioptimasi dengan MP2/cc-pVDZ. Karena biaya $\propto N^7$, seribu kali kecepatan hanya memperbesar $N$ dengan faktor $1000^{1/7} = 2{,}7$. **17.2** Untuk $i = j$ kedua integrand identik; interaksi elektron dengan dirinya sendiri terhapus tepat. Tidak: jumlah energi orbital menghitung setiap tolakan dua kali; $E_\text{el} = \sum_a(\varepsilon_a + h_{aa})$. **17.3** Fungsi basis atom saling bertumpang tindih (tidak ortogonal), sedangkan Hückel sederhana menganggap $S = \mathbf 1$; banyaknya orbital molekul naik dari 7 ke 25, tetapi orbital terisi tetap 5. **17.4** Lubang di kulit inti sangat mengubah perisai elektron valensi sehingga relaksasinya besar, sedangkan untuk valensi relaksasi dan korelasi saling meniadakan; orbital terlokalisasi bukan fungsi eigen operator Fock. **17.5** 6: inti dari 6 primitif; 311: valensi tiga fungsi dari 3, 1, dan 1 primitif; ++: fungsi difus pada atom berat dan H; (2d,p): dua set d pada atom berat dan satu set p pada H. Fungsi Gauss mempunyai turunan nol di inti, dan jumlah berhingga fungsi mulus tetap mulus. **17.6** Empat: O 1s, O 2s, O 2p$_z$, dan $\text{H}_a + \text{H}_b$. Tidak lagi murni: dengan 6-31G* ada dua fungsi p$_x$ oksigen dan fungsi d$_{xz}$ yang juga bersimetri $b_1$, sehingga orbital itu campuran beberapa fungsi oksigen. **17.7** Momen dipol adalah nilai harap operator yang teramati, sedangkan muatan Mulliken bergantung pada aturan pembagian yang sembarang; daerah paling negatif berada di belakang oksigen, di sekitar pasangan elektron bebas. **17.8** Energi total dan momen dipol tidak berubah; energi orbital (unsur diagonal Fock) berubah dan kehilangan arti Koopmans. Korelasi dinamik berjangka pendek, dan sumbangan pasangan yang berjauhan meluruh kira-kira sebagai $R^{-6}$. **17.9** Tiga translasi dan tiga rotasi tidak mengubah energi; HF melebih-lebihkan kelengkungan permukaan dan perhitungan harmonik mengabaikan anharmonisitas. **17.10** Teorema Brillouin; eksitasi tunggal bercampur melalui unsur matriks dengan eksitasi ganda. Contoh korelasi statik: ikatan yang putus, diradikal, ozon, Cr₂. **17.11** $E^{(0)} + E^{(1)} = E_\text{HF}$; penyebut mendekati nol dan $E^{(2)}$ menyimpang. **17.12** Suku $\tfrac12\hat T_2^2$ dalam uraian eksponensial; sumbangan rangkap tiga ditaksir dengan teori perturbasi satu kali, bukan diiterasi bersama amplitudo lain. **17.13** Bahwa kerapatan menentukan potensial luar dan semua sifat keadaan dasar serta prinsip variasi untuk kerapatan, tetapi tidak bentuk fungsionalnya; karena energi kinetik adalah bagian terbesar energi dan rumus lokal untuknya sangat buruk, sedangkan $T_s$ dari orbital tepat untuk sistem pembanding. **17.14** Pertukaran HF bebas interaksi diri, sehingga mencampurnya membatalkan sebagian interaksi diri fungsional lokal; meta-GGA menambahkan rapat energi kinetik $\tau$ (atau $\nabla^2\rho$). **17.15** Dispersi adalah korelasi elektron jarak jauh, yang tidak terlihat oleh fungsional yang hanya bergantung pada kerapatan di sekitar setiap titik; karena $\Delta G \propto 1/a$. **17.16** Minimum tidak mempunyai frekuensi imajiner, keadaan transisi tepat satu; IRC diperlukan untuk memastikan bahwa TS menghubungkan reaktan dan produk yang dimaksud. **17.17** Parameternya dicocokkan dengan entalpi pembentukan percobaan sehingga menyerap korelasi dan galat basis; medan gaya memakai topologi ikatan yang tetap dan suku ikatan harmonik yang tidak dapat putus. **17.18** Struktur mungkin titik pelana, optimasi belum konvergen, atau kisi integrasi terlalu kasar; program dan versinya, metode/basis/kisi/model pelarut, dan koordinat semua struktur.

# Pertanyaan

1. Mengapa pendekatan Born–Oppenheimer memungkinkan konsep permukaan energi potensial, dan apa saja yang ditentukan oleh permukaan itu?
2. Apa yang dimaksud "medan rata-rata" dalam Hartree–Fock, dan gerak elektron macam apa yang hilang?
3. Mengapa operator Coulomb lokal sedangkan operator pertukaran nonlokal?
4. Mengapa energi total HF bukan jumlah energi orbital, padahal dalam teori Hückel ya?
5. Kapan UHF lebih baik daripada RHF, dan apa harga yang harus dibayar?
6. Mengapa persamaan Roothaan merupakan masalah nilai eigen diperumum, dan bagaimana diubah menjadi masalah biasa?
7. Mengapa prosedur SCF harus iteratif, dan apa gagasan di balik DIIS?
8. Mengapa teorema Koopmans cukup baik untuk ionisasi valensi tetapi buruk untuk afinitas elektron dan ionisasi inti?
9. Mengapa fungsi Gauss dipakai alih-alih fungsi Slater? Apa kerugiannya, dan bagaimana diatasi?
10. Kapan fungsi polarisasi dan fungsi difus diperlukan? Berikan contoh sifat yang peka terhadap masing-masing.
11. Mengapa energi korelasi berkonvergensi jauh lebih lambat terhadap basis daripada energi HF?
12. Mengapa muatan atom bukan besaran teramati, dan bagaimana sebaiknya muatan atom dipakai?
13. Orbital kanonik atau orbital terlokalisasi: mana yang "benar"? Jelaskan dengan contoh metana.
14. Mengapa frekuensi harmonik hasil hitungan perlu diskalakan sebelum dibandingkan dengan spektrum IR?
15. Bedakan korelasi dinamik dan korelasi statik, dan sebutkan metode yang cocok untuk masing-masing.
16. Apa arti konsistensi ukuran, dan mengapa CISD tidak memilikinya sedangkan CCSD memilikinya?
17. Mengapa CCSD(T) disebut standar emas, dan dalam keadaan apa ia gagal?
18. Apa isi kedua teorema Hohenberg–Kohn, dan apa peran sistem Kohn–Sham yang tanpa interaksi?
19. Mengapa B3LYP tanpa koreksi tidak dapat menggambarkan tumpukan π atau dimer gas mulia?
20. Apa galat interaksi diri, dan gejala apa saja yang ditimbulkannya dalam perhitungan DFT?
21. Mengapa efek relativistik penting untuk kimia emas tetapi kecil untuk perak?
22. Bagaimana memastikan bahwa struktur yang ditemukan program adalah keadaan transisi reaksi yang dimaksud?
23. Bagaimana teka-teki pembuka bab (persamaan yang mustahil diselesaikan, tetapi angka yang cukup teliti untuk merancang katalis) terjawab oleh isi bab ini?

# Soal

## Subbab 17.1: Peta metode

Satuan atom dipakai kecuali disebut lain; 1 $E_h$ = 2625,50 kJ/mol = 627,51 kkal/mol = 27,2114 eV = 219 474,6 cm⁻¹; 1 $ea_0$ = 2,5417 D. Program pendamping bab ini (folder kode) dapat dipakai untuk soal bertanda "program". Soal dikelompokkan menurut tingkat: **dasar**, **menengah**, dan **tantangan ★**. Soal bertanda **[P]** dibahas di akhir bab.

**Dasar**

**1.** Jelaskan arti notasi "MP2/6-31G*//HF/6-31G*".

**2.** Berapa kali lebih lama perhitungan CCSD ($N^6$) bila molekulnya tiga kali lebih besar?

**3.** Nyatakan 1 kkal/mol dalam m$E_h$ dan kJ/mol.

**Menengah**

**4.** Hitung banyaknya determinan CI penuh untuk CH₄ (9 orbital STO-3G, 5α5β) dan N₂ (10 orbital, 7α7β).

**Tantangan ★**

**5.** ★ Bila kecepatan komputer berlipat dua setiap dua tahun, berapa tahun diperlukan agar CCSD(T) dapat menangani molekul dua kali lebih besar dalam waktu yang sama?

## Subbab 17.2: Hartree–Fock untuk molekul

**Dasar**

**6.** Tuliskan energi HF atom Li ($1s^22s$) dengan integral $h$, $J$, dan $K$.

**7.** Batas HF He memberi $\varepsilon_{1s} = -0{,}91796$ dan $E = -2{,}86168\ E_h$. Tentukan $h$ dan $J$ orbital 1s.

**8.** Berapa nilai tepat $\langle\hat S^2\rangle$ untuk doblet, triplet, dan kuartet?

**Menengah**

**9.** Tunjukkan bahwa $K_{ij} = 0$ bila $\chi_i$ dan $\chi_j$ berspin berlawanan.

**Tantangan ★**

**10.** ★ [P] Turunkan ungkapan energi kulit tertutup (17.4) dari (17.3) dengan mengintegrasikan atas spin.

## Subbab 17.3: Persamaan Roothaan dan prosedur SCF

**Dasar**

**11.** Hitung banyaknya integral dua elektron berbeda untuk 13 fungsi basis.

**12.** H₂O dengan 6-31G* (19 fungsi): berapa orbital molekul, berapa terisi, berapa virtual?

**13.** Tunjukkan bahwa $\mathbf X = \mathbf S^{-1/2}$ memenuhi $\mathbf X^\dagger\mathbf S\mathbf X = \mathbf 1$ untuk $\mathbf S$ simetris positif.

**Menengah**

**14.** (Program) Dengan program SCF di subbab 17.3, hitung energi H₂ dan energi orbital pada $R = 1{,}0$; 1,4; dan 2,0 bohr. Di jarak mana energinya terendah?

**Tantangan ★**

**15.** ★ [P] Dengan (17.8) dan uraian LCAO, turunkan ungkapan energi (17.14).

## Subbab 17.4: Teorema Koopmans dan energi ionisasi

**Dasar**

**16.** He/STO-3G memberi $\varepsilon_{1s} = -0{,}8760\ E_h$. Taksir energi ionisasinya dan bandingkan dengan 24,59 eV.

**17.** NH₃/HF/6-31G* memberi $\varepsilon_\text{HOMO} = -0{,}4212\ E_h$. Taksir EI vertikal dan bandingkan dengan 10,85 eV.

**18.** CH₄/HF/6-31G* memberi $-\varepsilon$ = 14,84 eV ($t_2$) dan 25,67 eV ($a_1$); percobaan sekitar 14,4 dan 23,0 eV. Hitung galatnya.

**Menengah**

**19.** Untuk H₂O/6-31G**, Koopmans 13,53 eV, ΔSCF 10,82 eV, percobaan 12,62 eV. Taksir energi relaksasi dan selisih korelasi.

**Tantangan ★**

**20.** ★ LUMO H₂O/6-31G** berenergi $+0{,}2121\ E_h$. Apa ramalan Koopmans untuk afinitas elektron, dan mengapa tidak dapat dipercaya?

## Subbab 17.5: Fungsi basis

**Dasar**

**21.** Hitung banyaknya fungsi basis NH₃ dengan 6-31G** dan etanol dengan cc-pVDZ.

**22.** Jelaskan setiap bagian notasi 6-311++G(2d,p).

**23.** Berapa fungsi Gauss primitif dalam basis STO-3G untuk atom oksigen?

**Menengah**

**24.** Ekstrapolasikan energi korelasi MP2 H₂O dari cc-pVDZ ($-0{,}2016$) dan cc-pVTZ ($-0{,}2613\ E_h$) dengan (17.23), lalu bandingkan dengan ekstrapolasi TQ ($-0{,}2956$).

**25.** Untuk dimer air/6-31G: $E_{AB} = -151{,}979701$; $E_A(AB) = -75{,}984441$; $E_B(AB) = -75{,}985129$; $E_A = E_B = -75{,}983997\ E_h$. Hitung energi interaksi dengan dan tanpa counterpoise.

**Tantangan ★**

**26.** ★ [P] Untuk atom H dengan fungsi uji $e^{-\alpha r^2}$, tunjukkan $E(\alpha) = \tfrac32\alpha - 2\sqrt{2\alpha/\pi}$ dan tentukan $\alpha$ optimum dan energinya.

## Subbab 17.6: SCF untuk H₂O

**Dasar**

**27.** Berapa orbital molekul bersimetri $a_1$, $b_1$, dan $b_2$ dalam H₂O/STO-3G?

**28.** Tuliskan konfigurasi elektron keadaan dasar H₂O.

**29.** H₂O/6-31G* memberi $T = 75{,}8215$ dan $E = -76{,}0105\ E_h$. Hitung $-V/T$.

**Menengah**

**30.** Dengan koefisien orbital $1b_2$ (subbab 17.6) dan $S(\text{2p}_y, \text{H}) = \pm0{,}3111$, hitung populasi Mulliken oksigen dalam orbital ini.

**Tantangan ★**

**31.** ★ Dari $\varepsilon_\text{HOMO} = -0{,}4971$ dan $\varepsilon_\text{LUMO} = +0{,}2121\ E_h$ (6-31G**), hitung kekerasan kimia $\eta = \tfrac12(\varepsilon_\text{LUMO} - \varepsilon_\text{HOMO})$ dan potensial kimia $\mu = \tfrac12(\varepsilon_\text{HOMO} + \varepsilon_\text{LUMO})$ dalam eV.

## Subbab 17.7: Analisis populasi dan potensial elektrostatik

**Dasar**

**32.** Untuk HeH⁺, $(\mathbf P\mathbf S)_{\text{He}} = 1{,}7275$. Hitung muatan Mulliken kedua atom.

**33.** Nyatakan momen dipol 0,7265 $ea_0$ dalam debye.

**34.** Mengapa muatan Löwdin biasanya lebih kecil daripada muatan Mulliken untuk ikatan polar?

**Menengah**

**35.** Hitung momen dipol NH₃ model muatan titik dengan $q_\text{H} = +0{,}331$, $r = 1{,}012$ Å, $\angle\text{HNH} = 106{,}67°$. Bandingkan dengan 1,95 D (HF/6-31G*).

**Tantangan ★**

**36.** ★ [P] Tunjukkan bahwa momen dipol molekul netral tidak bergantung pada pilihan titik asal, sedangkan momen dipol ion bergantung.

## Subbab 17.8: OM terlokalisasi

**Dasar**

**37.** Untuk dua orbital ortonormal $\psi_1$, $\psi_2$ dan rotasi dengan sudut $\theta$ sembarang, tunjukkan bahwa $|\psi_1'|^2 + |\psi_2'|^2 = |\psi_1|^2 + |\psi_2|^2$.

**38.** Besaran teramati apa yang berubah bila orbital kanonik diganti orbital terlokalisasi?

**39.** Berapa orbital terlokalisasi inti, ikatan, dan pasangan bebas yang diharapkan untuk CH₃OH?

**Menengah**

**40.** Dari energi kanonik CH₄ ($a_1$: $-0{,}910$; $t_2$: $-0{,}519\ E_h$), hitung unsur diagonal dan unsur kopling matriks Fock dalam basis empat LMO setara.

**Tantangan ★**

**41.** ★ Dengan $\psi_\pm = (\psi_{3a_1} \pm \psi_{1b_1})/\sqrt2$ sebagai pendekatan pasangan bebas H₂O/STO-3G ($\varepsilon_{3a_1} = -0{,}4530$; $\varepsilon_{1b_1} = -0{,}3912$), hitung unsur diagonal dan kopling matriks Fock keduanya.

## Subbab 17.9: Optimasi geometri dan frekuensi getaran

**Dasar**

**42.** Tunjukkan bahwa langkah Newton dari titik mana pun mencapai minimum $E = \tfrac12k(x - x_0)^2$ dalam satu langkah.

**43.** Berapa banyak mode getaran C₆H₆, CO₂, dan HCN?

**44.** Frekuensi C=O formaldehida HF/6-31G* sekitar 2028 cm⁻¹. Kalikan dengan faktor 0,8953 dan bandingkan dengan 1746 cm⁻¹.

**Menengah**

**45.** Hitung ZPE H₂O dari frekuensi HF/6-31G* (1826, 4071, 4190 cm⁻¹) dengan dan tanpa faktor skala ZPE 0,9135.

**Tantangan ★**

**46.** ★ [P] Dari $d^2E/dR^2 = 0{,}5729\ E_h$/bohr² (H₂, HF/STO-3G), hitung tetapan gaya dalam N/m dan frekuensi harmonik; bandingkan dengan nilai percobaan 575 N/m dan 4401 cm⁻¹.

## Subbab 17.10: Energi korelasi dan interaksi konfigurasi

**Dasar**

**47.** Hitung energi korelasi He dari $E_\text{HF}^\text{batas} = -2{,}86168$ dan $E_\text{tepat} = -2{,}90372\ E_h$, dalam kJ/mol.

**48.** Hitung banyaknya determinan CISD (Ms = 0) untuk H₂O/STO-3G (5 orbital terisi, 2 virtual).

**49.** Hitung koreksi Davidson untuk $c_0 = 0{,}95$ dan $E^\text{kor}_\text{CISD} = -0{,}250\ E_h$.

**Menengah**

**50.** Mengapa pecahan energi korelasi yang dipulihkan CISD menurun bila banyaknya molekul yang tidak berinteraksi bertambah?

**Tantangan ★**

**51.** ★ [P] Untuk H₂ dalam basis minimal pada $R \to \infty$, tunjukkan bahwa $H_{00} = H_{DD}$, bahwa $c_D = -c_0$, dan bahwa CI penuh memberi tepat $2E(\text{H})$, sedangkan RHF terlalu tinggi $\tfrac12(aa|aa)$.

## Subbab 17.11: Teori perturbasi Møller–Plesset

**Dasar**

**52.** Untuk H₂/STO-3G pada $R = 2{,}0$ bohr: $\varepsilon_1 = -0{,}4665$, $\varepsilon_2 = 0{,}4209$, $K_{12} = 0{,}2005\ E_h$. Hitung $E^{(2)}$ dan bandingkan dengan korelasi FCI ($-0{,}0393\ E_h$).

**53.** Mengapa $E^{(2)}$ selalu negatif untuk keadaan dasar?

**54.** Hitung SCS-MP2 untuk H₂O/STO-3G dengan $E_\text{os} = -0{,}033468$ dan $E_\text{ss} = -0{,}002025\ E_h$.

**Menengah**

**55.** Berapa kali lebih lama MP2 dan CCSD bila banyaknya fungsi basis dilipatduakan?

**Tantangan ★**

**56.** ★ [P] Tunjukkan bahwa $E^{(0)} + E^{(1)} = E_\text{HF}$ dalam pembagian Møller–Plesset.

## Subbab 17.12: Metode coupled-cluster dan metode komposit

**Dasar**

**57.** Uraikan $e^{\hat T}$ dengan $\hat T = \hat T_1 + \hat T_2$ sampai orde tiga dan tunjukkan suku-suku yang menghasilkan eksitasi rangkap tiga.

**58.** Berapa kali lebih lama CCSD(T) bila molekul 1,5 kali lebih besar?

**59.** Apa yang ditunjukkan diagnostik T1 yang besar (> 0,02)?

**Menengah**

**60.** Taksir CCSD/6-31G* untuk H₂O dari CCSD/6-31G ($-0{,}135322$), MP2/6-31G ($-0{,}128796$), dan MP2/6-31G* ($-0{,}188472\ E_h$), lalu bandingkan dengan nilai sebenarnya $-0{,}197266\ E_h$.

**Tantangan ★**

**61.** ★ Model $N$ molekul H₂ tak berinteraksi dalam basis minimal: CISD mencampur keadaan dasar dengan $N$ eksitasi ganda (masing-masing $\Delta = 1{,}5773$ di atas, kopling $K = 0{,}18126\ E_h$), sehingga $E^\text{kor}_\text{CISD} = \tfrac12[\Delta - \sqrt{\Delta^2 + 4NK^2}]$. Hitung pecahan korelasi tepat yang dipulihkan untuk $N = 2$, 10, dan 100.

## Subbab 17.13: Teori fungsional kerapatan

**Dasar**

**62.** Hitung $C_F$ dan $C_x$.

**63.** Energi kinetik Thomas–Fermi atom H 0,289 $E_h$. Berapa untuk ion mirip hidrogen He⁺, dan berapa nilai tepatnya?

**64.** Rumus Dirac tak terpolarisasi memberi $-0{,}2127\ E_h$ untuk kerapatan atom H. Berapa bila spin terpolarisasi penuh (faktor $2^{1/3}$)?

**Menengah**

**65.** Untuk He/LDA: $\sum\varepsilon_i = -1{,}14052$, $J = 1{,}99586$, $E_{xc} = -0{,}97282$, $E = -2{,}83445\ E_h$. Hitung $\int v_{xc}\rho\,d\mathbf r$ dari (17.49).

**Tantangan ★**

**66.** ★ [P] Tunjukkan bahwa untuk sistem satu elektron fungsional tepat harus memenuhi $E_{xc}[\rho] = -J[\rho]$.

## Subbab 17.14: Fungsional LDA, GGA, hibrida

**Dasar**

**67.** Hitung $F_x^\text{PBE}$ pada $s = 1{,}5$.

**68.** Berapa persen pertukaran HF dalam B3LYP, PBE0, dan B2PLYP?

**69.** Anak tangga Yakub mana yang memakai rapat energi kinetik $\tau$?

**Menengah**

**70.** Untuk CAM-B3LYP ($\omega = 0{,}33$ bohr⁻¹), berapa $\operatorname{erf}(\omega r_{12})$ pada $r_{12} = 2$ bohr?

**Tantangan ★**

**71.** ★ (Program) Hitung energi pertukaran PBE atom H dari kerapatan tepat, memakai penskalaan spin $E_x[\rho_\uparrow, 0] = \tfrac12E_x[2\rho_\uparrow]$. Bandingkan dengan LSDA ($-0{,}268$) dan nilai tepat ($-0{,}3125\ E_h$).

## Subbab 17.15: Interaksi nonkovalen dan efek relativistik

**Dasar**

**72.** Hitung energi Born untuk Mg²⁺ ($a = 1{,}45$ Å, $\varepsilon_r = 78{,}4$).

**73.** Selisih energi bebas deprotonasi dua asam 17 kJ/mol. Berapa selisih pKa-nya pada 298 K?

**74.** Taksir $v/c$ dan penyusutan 1s untuk Pt ($Z = 78$) dan Pb (82).

**Menengah**

**75.** Dengan (17.54), hitung $C_6$ Ne–Ne ($\alpha = 2{,}67$, $I = 21{,}565$ eV) dan bandingkan dengan nilai teliti 6,38.

**Tantangan ★**

**76.** ★ [P] Turunkan persamaan Born (17.56) dari kerja pengisian bola bermuatan dalam vakum dan dalam dielektrik.

## Subbab 17.16: Reaksi kimia dan keadaan transisi

**Dasar**

**77.** Berapa perbandingan laju dua reaksi yang penghalangnya berbeda 5 kJ/mol pada 298 K?

**78.** Titik stasioner mempunyai nilai eigen Hessian (setelah proyeksi) 0,32; 0,15; $-0{,}04$. Apa jenisnya?

**79.** Hitung $\kappa_\text{W}$ untuk 800i cm⁻¹ pada 298 K.

**Menengah**

**80.** Berapa $\Delta G^\ddagger$ untuk reaksi orde pertama dengan waktu paruh 1 jam pada 298 K?

**Tantangan ★**

**81.** ★ [P] Dua jalur bersaing dari reaktan yang sama berbeda $\Delta\Delta G^\ddagger = 6$ kJ/mol. Hitung perbandingan produk kinetik pada 298 K dan 348 K, dan jelaskan mengapa hanya selisih penghalang yang diperlukan.

## Subbab 17.17: Metode semiempiris dan mekanika molekul

**Dasar**

**82.** Hitung energi torsi etana pada $\phi = 45°$ dengan $V_3 = 12$ kJ/mol.

**83.** Hitung energi Lennard-Jones pada $r = \sigma$ dan $r = 2\sigma$ (dalam $\varepsilon$).

**84.** Bandingkan banyaknya integral dua elektron HF/STO-3G (16 fungsi) dan integral NDDO valensi untuk etana.

**Menengah**

**85.** Ikatan C–H AMBER: $k_r = 340$ kkal mol⁻¹ Å⁻². Berapa energi untuk meregangkan 0,02 Å?

**Tantangan ★**

**86.** ★ Ikatan C=O AMBER mempunyai $k_r = 570$ kkal mol⁻¹ Å⁻² (bentuk tanpa $\tfrac12$). Hitung tetapan gaya fisika dalam N/m dan frekuensi harmonik dua benda C=O; bandingkan dengan pita keton 1715 cm⁻¹.

## Subbab 17.18: Program kimia kuantum dan alur kerja

**Dasar**

**87.** Nyatakan 0,0100 $E_h$ dalam kJ/mol, kkal/mol, eV, dan cm⁻¹.

**88.** Berapa multiplisitas keadaan dasar O₂, NO, CH₂, dan benzena?

**89.** Berapa koreksi keadaan standar (1 atm → 1 M) untuk dimerisasi 2A → A₂ pada 298 K?

**Menengah**

**90.** Tiga konformer berenergi bebas relatif 0, 2, dan 5 kJ/mol. Hitung populasinya pada 298 K.

**Tantangan ★**

**91.** ★ HF/6-31G* memberi $E(\text{H}_2\text{O}) = -76{,}010747$ dan $E(\text{H}_3\text{O}^+) = -76{,}289204\ E_h$ (geometri HF). Hitung afinitas proton elektronik, lalu taksir afinitas proton 298 K dengan koreksi ZPE sekitar $-30$ kJ/mol dan $\tfrac52RT$. Bandingkan dengan 691 kJ/mol.


# Jawaban

::: {.panjang}
| No. | Jawaban | No. | Jawaban |
|---|---|---|---|
| 1 | energi MP2/6-31G* pada geometri yang dioptimasi dengan HF/6-31G* | 47 | $-0{,}04204\ E_h = -110{,}4$ kJ/mol |
| 2 | $3^6 = 729$ kali | 48 | $1 + 20 + 120 = 141$ |
| 3 | 1,594 m$E_h$; 4,184 kJ/mol | 49 | $-0{,}0244\ E_h$ |
| 4 | 15 876; 14 400 | 50 | kuadrupel tak terhubung dibuang |
| 5 | $2^7 = 128$, tujuh kali lipat dua: 14 tahun | 51 | lihat pembahasan |
| 6 | $2h_{1s} + h_{2s} + J_{1s1s} + 2J_{1s2s} - K_{1s2s}$ | 52 | $-0{,}0227\ E_h$; 58% |
| 7 | $h = -1{,}94372$; $J = 1{,}02576\ E_h$ | 53 | pembilang positif, penyebut negatif |
| 8 | 0,75; 2,00; 3,75 | 54 | $-0{,}04084\ E_h$ |
| 9 | integral spin $\langle\alpha|\beta\rangle = 0$ muncul dua kali | 55 | 32 dan 64 kali |
| 10 | lihat pembahasan | 56 | lihat pembahasan |
| 11 | 4186 | 57 | $\hat T_1\hat T_2$ dan $\tfrac16\hat T_1^3$ |
| 12 | 19; 5; 14 | 58 | 17 kali |
| 13 | $\mathbf S^{-1/2}\mathbf S\mathbf S^{-1/2} = \mathbf 1$ | 59 | korelasi statik; satu determinan tidak memadai |
| 14 | $-1{,}0660$; $-1{,}1167$; $-1{,}0492\ E_h$; $\varepsilon_1 = -0{,}676$; $-0{,}578$; $-0{,}466$; terendah di sekitar 1,4 | 60 | $-0{,}194998$; galat 2,3 m$E_h$ |
| 15 | lihat pembahasan | 61 | 98,8%; 90,6%; 57,8% |
| 16 | 23,84 eV; terlalu kecil 0,75 eV karena basis minimal | 62 | 2,8712; 0,7386 |
| 17 | 11,46 eV; +0,6 eV | 63 | $Z^2 \times 0{,}289 = 1{,}157$; tepat 2,0 |
| 18 | +0,4 dan +2,7 eV | 64 | $-0{,}268\ E_h$ (tepat $-0{,}3125$) |
| 19 | relaksasi 2,71 eV; korelasi 1,80 eV | 65 | $-1{,}2748\ E_h$ |
| 20 | $-5{,}77$ eV (anion tak terikat); relaksasi dan korelasi searah, energi virtual bergantung basis | 66 | lihat pembahasan |
| 21 | 30; 72 | 67 | 1,306 |
| 22 | inti 6 primitif; valensi triple-zeta (3,1,1); difus pada atom berat dan H; dua set d pada atom berat, satu set p pada H | 68 | 20%; 25%; 53% |
| 23 | $5 \times 3 = 15$ | 69 | meta-GGA |
| 24 | $-0{,}2864\ E_h$; meleset 9,2 m$E_h$ | 70 | 0,649 |
| 25 | $-6{,}36$ dan $-7{,}35$ kkal/mol | 71 | $-0{,}306\ E_h$ |
| 26 | $\alpha = 8/9\pi$; $E = -4/3\pi = -0{,}4244\ E_h$ | 72 | $-1892$ kJ/mol |
| 27 | 4; 1; 2 | 73 | 2,98 |
| 28 | $(1a_1)^2(2a_1)^2(1b_2)^2(3a_1)^2(1b_1)^2$ | 74 | 0,569 dan 17,8%; 0,598 dan 19,9% |
| 29 | 2,0025 | 75 | 4,24 satuan atom; 34% terlalu kecil |
| 30 | 0,536 per elektron; 1,07 untuk dua elektron | 76 | lihat pembahasan |
| 31 | $\eta = 9{,}65$ eV; $\mu = -3{,}88$ eV | 77 | 7,5 |
| 32 | He +0,27; H +0,73 | 78 | titik pelana orde pertama (keadaan transisi) |
| 33 | 1,85 D | 79 | 1,62 |
| 34 | ortogonalisasi menyebar rapat tumpang tindih lebih merata | 80 | 94,2 kJ/mol |
| 35 | $z_\text{H} = 0{,}721$ bohr; 1,82 D | 81 | 11,3 dan 7,9 |
| 36 | $\boldsymbol\mu' = \boldsymbol\mu - Q\mathbf a$ | 82 | 1,76 kJ/mol |
| 37 | suku silang meniadakan diri | 83 | 0; $-0{,}0615\varepsilon$ |
| 38 | tidak ada | 84 | 9316; 351 |
| 39 | 2 inti, 5 ikatan, 2 pasangan bebas (9 = 18/2) | 85 | 0,136 kkal/mol |
| 40 | diagonal $-0{,}617$; kopling $-0{,}098\ E_h$ | 86 | 792 N/m; 1400 cm⁻¹; medan gaya tidak dirancang untuk frekuensi |
| 41 | diagonal $-0{,}4221$; kopling $-0{,}0309\ E_h$ | 87 | 26,25; 6,275; 0,2721; 2195 |
| 42 | $\Delta x = -k(x - x_0)/k$ | 88 | 3; 2; 3; 1 |
| 43 | 30; 4; 4 | 89 | $-7{,}93$ kJ/mol |
| 44 | 1816 cm⁻¹; masih 70 cm⁻¹ terlalu tinggi | 90 | 63,3%; 28,3%; 8,4% |
| 45 | 60,3 dan 55,1 kJ/mol | 91 | 731,1 kJ/mol; sekitar 707 kJ/mol; terlalu besar sekitar 16 kJ/mol |
| 46 | 892 N/m; 5481 cm⁻¹ |  |  |
:::


# Pembahasan soal terpilih

**Soal 10.** Setiap orbital ruang terisi $\psi_a$ menghasilkan dua spin-orbital, $\psi_a\alpha$ dan $\psi_a\beta$. Suku satu elektron: $\sum_ih_{ii} = \sum_a(h_{aa} + h_{aa}) = 2\sum_ah_{aa}$, karena operator $\hat h$ tidak bekerja pada spin dan $\langle\alpha|\alpha\rangle = \langle\beta|\beta\rangle = 1$. Untuk suku dua elektron, ambil sepasang orbital ruang $(a, b)$; ada empat kombinasi spin ($\alpha\alpha$, $\alpha\beta$, $\beta\alpha$, $\beta\beta$). Integral Coulomb $J$ tidak bergantung pada spin, sehingga keempatnya menyumbang $J_{ab}$: total $4J_{ab}$. Integral pertukaran hanya tidak nol untuk spin sama: $2K_{ab}$. Dengan faktor $\tfrac12$ di depan jumlah ganda: $\tfrac12\sum_{ab}(4J_{ab} - 2K_{ab}) = \sum_{ab}(2J_{ab} - K_{ab})$, yaitu (17.4).

*Cara berpikir:* untuk $a = b$, suku $2J_{aa} - K_{aa} = J_{aa}$ adalah tolakan antara dua elektron berpasangan dalam orbital yang sama, satu-satunya tolakan yang benar-benar ada di antara keduanya. Untuk $a \neq b$, empat tolakan Coulomb dikurangi dua "koreksi pertukaran" untuk pasangan spin sejajar: elektron berspin sama saling menghindar (lubang Fermi), sehingga tolakan bersihnya lebih kecil.

**Soal 15.** Untuk kulit tertutup, (17.8) menjadi $E_\text{el} = \sum_a(\varepsilon_a + h_{aa})$ dengan jumlah atas orbital ruang terisi. Masukkan $\psi_a = \sum_\mu C_{\mu a}\phi_\mu$: $h_{aa} = \sum_{\mu\nu}C_{\mu a}^*C_{\nu a}H_{\mu\nu}$ dan $\varepsilon_a = \langle\psi_a|\hat f|\psi_a\rangle = \sum_{\mu\nu}C_{\mu a}^*C_{\nu a}F_{\mu\nu}$. Maka

$$
E_\text{el} = \sum_{\mu\nu}\left(\sum_aC_{\mu a}^*C_{\nu a}\right)(H_{\mu\nu} + F_{\mu\nu}) = \tfrac12\sum_{\mu\nu}P_{\nu\mu}(H_{\mu\nu} + F_{\mu\nu}) ,
$$

karena $\sum_aC_{\mu a}^*C_{\nu a} = \tfrac12P_{\nu\mu}$ menurut (17.11).

*Cara berpikir:* rumus ini adalah yang benar-benar dipakai program untuk menghitung energi pada setiap siklus SCF. Ia hanya memerlukan matriks kecil $\mathbf H$, $\mathbf F$, dan $\mathbf P$, bukan orbital satu per satu. Karena energi HF stasioner terhadap variasi orbital, galat energi orde kedua dalam galat $\mathbf P$; energi berkonvergensi lebih cepat daripada matriks kerapatan, sehingga kriteria konvergensi selalu memeriksa keduanya.

**Soal 26.** Dengan $\psi = (2\alpha/\pi)^{3/4}e^{-\alpha r^2}$, energi kinetik $\langle T\rangle = \tfrac32\alpha$ (setengah dari $\langle p^2\rangle = 3\alpha$, karena tiap arah menyumbang $\alpha$ seperti osilator harmonik) dan $\langle V\rangle = -\langle 1/r\rangle = -4\pi(2\alpha/\pi)^{3/2}\int_0^\infty r\,e^{-2\alpha r^2}dr = -2\sqrt{2\alpha/\pi}$. Jadi $E(\alpha) = \tfrac32\alpha - 2\sqrt{2\alpha/\pi}$. Syarat $dE/d\alpha = \tfrac32 - \sqrt{2/\pi\alpha} = 0$ memberi $\alpha = 8/9\pi = 0{,}2829$, dan $E = \tfrac{4}{3\pi} - \tfrac{8}{3\pi} = -\tfrac{4}{3\pi} = -0{,}4244\ E_h$.

*Cara berpikir:* di titik optimum $\langle V\rangle = -2\langle T\rangle$, teorema virial. Energi 15% terlalu tinggi menunjukkan betapa satu fungsi Gauss tidak cukup, dan menjelaskan mengapa basis praktis memakai kontraksi beberapa fungsi Gauss (STO-3G) dan, untuk ketelitian tinggi, banyak fungsi dengan eksponen berbeda.

**Soal 36.** Geser titik asal sejauh $\mathbf a$, sehingga setiap posisi menjadi $\mathbf r' = \mathbf r - \mathbf a$. Dari (17.27):

$$
\boldsymbol\mu' = \sum_AZ_A(\mathbf R_A - \mathbf a) - \int(\mathbf r - \mathbf a)\rho\,d\mathbf r = \boldsymbol\mu - \mathbf a\left(\sum_AZ_A - N\right) = \boldsymbol\mu - Q\mathbf a ,
$$

dengan $Q$ muatan total. Untuk molekul netral $Q = 0$ dan $\boldsymbol\mu' = \boldsymbol\mu$.

*Cara berpikir:* untuk ion, program biasanya melaporkan momen dipol terhadap pusat massa atau pusat muatan inti, dan angkanya bermakna hanya bila titik asalnya disebut. Hal yang sama berlaku untuk momen multipol yang lebih tinggi: momen kuadrupol tidak bergantung pada titik asal hanya bila muatan dan dipolnya nol.

**Soal 46.** 1 $E_h$/bohr² $= 4{,}3597 \times 10^{-18}$ J $/(5{,}2918 \times 10^{-11}\ \text{m})^2 = 1556{,}9$ N/m, sehingga $k = 0{,}5729 \times 1556{,}9 = 892$ N/m. Dengan $\mu = \tfrac12(1{,}00783)$ u $= 8{,}368 \times 10^{-28}$ kg: $\omega = \sqrt{k/\mu} = 1{,}032 \times 10^{15}$ s⁻¹ dan $\tilde\nu = \omega/2\pi c = 5481$ cm⁻¹.

*Cara berpikir:* HF/STO-3G memberi ikatan yang 55% terlalu kaku dan frekuensi 25% terlalu tinggi. Sebagian karena basis minimal (eksponen tetap $\zeta = 1{,}24$ tidak dapat menyesuaikan diri ketika ikatan meregang), sebagian karena HF: tanpa korelasi, energi naik terlalu cepat saat ikatan diregangkan, karena bagian ionik fungsi gelombang RHF makin tidak sesuai. CI penuh dalam basis yang sama sudah menurunkan frekuensinya ke 5002 cm⁻¹.

**Soal 51.** Pada $R \to \infty$ tumpang tindih nol, $\sigma_{g,u} = (a \pm b)/\sqrt2$, dan semua integral dua pusat yang melibatkan hasil kali $ab$ atau tolakan $1/R$ hilang. Maka $h_{11} = h_{22} = \varepsilon_\text{H}$ (energi atom H dalam basis), dan dengan uraian $(\sigma\sigma|\sigma\sigma)$ atas fungsi atom: $J_{11} = J_{22} = J_{12} = K_{12} = \tfrac14[(aa|aa) + (bb|bb)] = \tfrac12(aa|aa)$. Jadi $H_{00} = H_{DD} = 2\varepsilon_\text{H} + \tfrac12(aa|aa)$ dan $H_{0D} = \tfrac12(aa|aa)$. Matriks $\begin{pmatrix}h & k\\ k & h\end{pmatrix}$ mempunyai nilai eigen terendah $h - k = 2\varepsilon_\text{H}$ dengan vektor $(1, -1)/\sqrt2$, sehingga $c_D = -c_0$. RHF ($= H_{00}$) berada $\tfrac12(aa|aa)$ di atasnya; untuk STO-3G, $(aa|aa) = 0{,}7746\ E_h$, sehingga galat RHF di jarak tak hingga $0{,}387\ E_h$, lebih dari 1000 kJ/mol.

*Cara berpikir:* $(\sigma_g^2 - \sigma_u^2)/\sqrt2 = (ab + ba)/\sqrt2$ (setelah dinormalisasi ulang): bagian ionik $a^2$ dan $b^2$ saling meniadakan, dan yang tersisa adalah fungsi Heitler–London kovalen murni (subbab 11.11). Galat RHF $\tfrac12(aa|aa)$ adalah energi tolakan rata-rata dari bagian ionik H⁻ yang tidak fisis. Dua konfigurasi berbobot sama adalah definisi korelasi statik.

**Soal 56.** $\Phi_0$ adalah fungsi eigen $\hat H^{(0)} = \sum_i\hat f(i)$ dengan nilai eigen $E^{(0)} = \sum_i\varepsilon_i$ (jumlah atas spin-orbital terisi). Koreksi orde pertama $E^{(1)} = \langle\Phi_0|\hat H - \hat H^{(0)}|\Phi_0\rangle = E_\text{HF} - \sum_i\varepsilon_i$, karena $\langle\Phi_0|\hat H|\Phi_0\rangle = E_\text{HF}$ menurut definisi. Jumlahnya $E^{(0)} + E^{(1)} = E_\text{HF}$. Secara eksplisit, $E^{(1)} = -\tfrac12\sum_{ij}(J_{ij} - K_{ij})$, koreksi untuk tolakan yang dihitung dua kali dalam $\sum\varepsilon_i$.

*Cara berpikir:* teori perturbasi MP "menemukan kembali" Hartree–Fock pada orde pertama, sehingga semua korelasi muncul mulai orde kedua. Pembagian lain (misalnya Epstein–Nesbet) memberi deret yang berbeda; pembagian Møller–Plesset dipilih karena konsisten ukuran pada setiap orde.

**Soal 66.** Untuk satu elektron, fungsi gelombang tepat adalah satu orbital $\phi$ dengan $\rho = |\phi|^2$, dan energi tepat $E = T + \int v\rho$ tanpa tolakan apa pun. Sistem Kohn–Sham satu elektron mempunyai orbital yang sama, sehingga $T_s = T$. Dari (17.47), $E = T_s + \int v\rho + J[\rho] + E_{xc}[\rho]$; agar sama dengan energi tepat, $E_{xc}[\rho] = -J[\rho]$. Karena tidak ada elektron lain untuk dikorelasikan, $E_c = 0$ dan $E_x = -J$.

*Cara berpikir:* syarat ini, kebebasan dari interaksi diri satu elektron, dipenuhi otomatis oleh HF ($J_{ii} = K_{ii}$) tetapi tidak oleh LDA dan GGA. Untuk atom H, LSDA memberi $J + E_{xc} = +0{,}020\ E_h$ (Contoh 17.52). Koreksi interaksi diri Perdew–Zunger dan fungsional hibrida adalah dua cara memulihkan syarat ini sebagian.

**Soal 76.** Isi bola konduktor berjari-jari $a$ sedikit demi sedikit dari muatan 0 sampai $q$. Pada muatan antara $q'$, potensial permukaan dalam vakum $\phi = q'/4\pi\varepsilon_0a$, dan kerja untuk menambah $dq'$ adalah $\phi\,dq'$. Kerja total $W_\text{vak} = \int_0^q\frac{q'}{4\pi\varepsilon_0a}dq' = \frac{q^2}{8\pi\varepsilon_0a}$. Dalam dielektrik, potensial berkurang dengan faktor $\varepsilon_r$, sehingga $W_\text{diel} = q^2/8\pi\varepsilon_0\varepsilon_ra$. Energi bebas solvasi elektrostatik adalah selisihnya (memindahkan ion bermuatan dari vakum ke pelarut sama dengan membuang muatan di vakum lalu mengisinya kembali di pelarut): $\Delta G = W_\text{diel} - W_\text{vak} = -\frac{q^2}{8\pi\varepsilon_0a}(1 - 1/\varepsilon_r)$. Dikali $N_A$ dengan $q = ze$: (17.56).

*Cara berpikir:* faktor $(1 - 1/\varepsilon_r)$ sudah 0,987 untuk air, sehingga energi solvasi ion hampir tidak peka terhadap $\varepsilon_r$ bila pelarutnya polar, tetapi sangat peka terhadap jari-jari rongga. Model kontinum modern pada dasarnya adalah perumuman persamaan Born untuk rongga berbentuk molekul dan rapat muatan sembarang.

**Soal 81.** Untuk dua jalur dari reaktan yang sama, $k_1/k_2 = \exp[-(\Delta G_1^\ddagger - \Delta G_2^\ddagger)/RT]$, karena faktor $k_BT/h$ dan $\kappa$ (bila serupa) saling meniadakan. Dengan $\Delta\Delta G^\ddagger = 6$ kJ/mol: pada 298 K, $e^{6000/2479} = e^{2{,}42} = 11{,}3$; pada 348 K, $e^{6000/2894} = e^{2{,}07} = 7{,}9$.

*Cara berpikir:* perbandingan produk kinetik hanya memerlukan selisih penghalang dua keadaan transisi yang sering mirip strukturnya, sehingga galat metode banyak yang meniadakan diri; ketelitian 2–4 kJ/mol untuk selisih semacam ini sering dapat dicapai dengan DFT yang baik, padahal penghalang mutlaknya mungkin meleset 10 kJ/mol. Menaikkan suhu menurunkan selektivitas, sesuai pengalaman sintesis bahwa reaksi selektif sering dijalankan pada suhu rendah.

# Bacaan lanjut

1. A. Szabo dan N. S. Ostlund, *Modern Quantum Chemistry: Introduction to Advanced Electronic Structure Theory* (Dover, 1996). Penurunan Hartree–Fock, persamaan Roothaan, CI, MP, dan CC yang sangat jernih, dengan contoh H₂ dan HeH⁺ dalam basis minimal.
2. F. Jensen, *Introduction to Computational Chemistry*, edisi ke-3 (Wiley, 2017). Tinjauan menyeluruh metode, basis, sifat molekul, dan praktik perhitungan.
3. C. J. Cramer, *Essentials of Computational Chemistry: Theories and Models*, edisi ke-2 (Wiley, 2004). Sangat baik untuk mekanika molekul, metode semiempiris, solvasi, dan studi kasus.
4. T. Helgaker, P. Jørgensen, dan J. Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000). Rujukan lanjut untuk integral Gauss, basis berkorelasi konsisten, dan teori *coupled-cluster*.
5. W. Koch dan M. C. Holthausen, *A Chemist's Guide to Density Functional Theory*, edisi ke-2 (Wiley-VCH, 2001). Pengantar DFT yang ditulis untuk kimiawan, lengkap dengan penilaian kinerja fungsional.
6. I. N. Levine, *Quantum Chemistry*, edisi ke-7 (Pearson, 2014), Bab 13–17. Hartree–Fock molekul, korelasi, DFT, dan metode semiempiris pada tingkat buku kuliah.
