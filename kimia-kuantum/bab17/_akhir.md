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

1. Mengapa hampiran Born–Oppenheimer memungkinkan konsep permukaan energi potensial, dan apa saja yang ditentukan oleh permukaan itu?
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

%%SOAL%%

# Jawaban

%%JAWABAN%%

# Pembahasan soal terpilih

**Soal {{ekt}}.** Setiap orbital ruang terisi $\psi_a$ menghasilkan dua spin-orbital, $\psi_a\alpha$ dan $\psi_a\beta$. Suku satu elektron: $\sum_ih_{ii} = \sum_a(h_{aa} + h_{aa}) = 2\sum_ah_{aa}$, karena operator $\hat h$ tidak bekerja pada spin dan $\langle\alpha|\alpha\rangle = \langle\beta|\beta\rangle = 1$. Untuk suku dua elektron, ambil sepasang orbital ruang $(a, b)$; ada empat kombinasi spin ($\alpha\alpha$, $\alpha\beta$, $\beta\alpha$, $\beta\beta$). Integral Coulomb $J$ tidak bergantung pada spin, sehingga keempatnya menyumbang $J_{ab}$: total $4J_{ab}$. Integral pertukaran hanya tidak nol untuk spin sama: $2K_{ab}$. Dengan faktor $\tfrac12$ di depan jumlah ganda: $\tfrac12\sum_{ab}(4J_{ab} - 2K_{ab}) = \sum_{ab}(2J_{ab} - K_{ab})$, yaitu (17.4).

*Cara berpikir:* untuk $a = b$, suku $2J_{aa} - K_{aa} = J_{aa}$ adalah tolakan antara dua elektron berpasangan dalam orbital yang sama, satu-satunya tolakan yang benar-benar ada di antara keduanya. Untuk $a \neq b$, empat tolakan Coulomb dikurangi dua "koreksi pertukaran" untuk pasangan spin sejajar: elektron berspin sama saling menghindar (lubang Fermi), sehingga tolakan bersihnya lebih kecil.

**Soal {{eel}}.** Untuk kulit tertutup, (17.8) menjadi $E_\text{el} = \sum_a(\varepsilon_a + h_{aa})$ dengan jumlah atas orbital ruang terisi. Masukkan $\psi_a = \sum_\mu C_{\mu a}\phi_\mu$: $h_{aa} = \sum_{\mu\nu}C_{\mu a}^*C_{\nu a}H_{\mu\nu}$ dan $\varepsilon_a = \langle\psi_a|\hat f|\psi_a\rangle = \sum_{\mu\nu}C_{\mu a}^*C_{\nu a}F_{\mu\nu}$. Maka

$$
E_\text{el} = \sum_{\mu\nu}\left(\sum_aC_{\mu a}^*C_{\nu a}\right)(H_{\mu\nu} + F_{\mu\nu}) = \tfrac12\sum_{\mu\nu}P_{\nu\mu}(H_{\mu\nu} + F_{\mu\nu}) ,
$$

karena $\sum_aC_{\mu a}^*C_{\nu a} = \tfrac12P_{\nu\mu}$ menurut (17.11).

*Cara berpikir:* rumus ini adalah yang benar-benar dipakai program untuk menghitung energi pada setiap siklus SCF. Ia hanya memerlukan matriks kecil $\mathbf H$, $\mathbf F$, dan $\mathbf P$, bukan orbital satu per satu. Karena energi HF stasioner terhadap variasi orbital, galat energi orde kedua dalam galat $\mathbf P$; energi berkonvergensi lebih cepat daripada matriks kerapatan, sehingga kriteria konvergensi selalu memeriksa keduanya.

**Soal {{gauss1}}.** Dengan $\psi = (2\alpha/\pi)^{3/4}e^{-\alpha r^2}$, energi kinetik $\langle T\rangle = \tfrac32\alpha$ (setengah dari $\langle p^2\rangle = 3\alpha$, karena tiap arah menyumbang $\alpha$ seperti osilator harmonik) dan $\langle V\rangle = -\langle 1/r\rangle = -4\pi(2\alpha/\pi)^{3/2}\int_0^\infty r\,e^{-2\alpha r^2}dr = -2\sqrt{2\alpha/\pi}$. Jadi $E(\alpha) = \tfrac32\alpha - 2\sqrt{2\alpha/\pi}$. Syarat $dE/d\alpha = \tfrac32 - \sqrt{2/\pi\alpha} = 0$ memberi $\alpha = 8/9\pi = 0{,}2829$, dan $E = \tfrac{4}{3\pi} - \tfrac{8}{3\pi} = -\tfrac{4}{3\pi} = -0{,}4244\ E_h$.

*Cara berpikir:* di titik optimum $\langle V\rangle = -2\langle T\rangle$, teorema virial. Energi 15% terlalu tinggi menunjukkan betapa satu fungsi Gauss tidak cukup, dan menjelaskan mengapa basis praktis memakai kontraksi beberapa fungsi Gauss (STO-3G) dan, untuk ketelitian tinggi, banyak fungsi dengan eksponen berbeda.

**Soal {{dipol}}.** Geser titik asal sejauh $\mathbf a$, sehingga setiap posisi menjadi $\mathbf r' = \mathbf r - \mathbf a$. Dari (17.27):

$$
\boldsymbol\mu' = \sum_AZ_A(\mathbf R_A - \mathbf a) - \int(\mathbf r - \mathbf a)\rho\,d\mathbf r = \boldsymbol\mu - \mathbf a\left(\sum_AZ_A - N\right) = \boldsymbol\mu - Q\mathbf a ,
$$

dengan $Q$ muatan total. Untuk molekul netral $Q = 0$ dan $\boldsymbol\mu' = \boldsymbol\mu$.

*Cara berpikir:* untuk ion, program biasanya melaporkan momen dipol terhadap pusat massa atau pusat muatan inti, dan angkanya bermakna hanya bila titik asalnya disebut. Hal yang sama berlaku untuk momen multipol yang lebih tinggi: momen kuadrupol tidak bergantung pada titik asal hanya bila muatan dan dipolnya nol.

**Soal {{kH2}}.** 1 $E_h$/bohr² $= 4{,}3597 \times 10^{-18}$ J $/(5{,}2918 \times 10^{-11}\ \text{m})^2 = 1556{,}9$ N/m, sehingga $k = 0{,}5729 \times 1556{,}9 = 892$ N/m. Dengan $\mu = \tfrac12(1{,}00783)$ u $= 8{,}368 \times 10^{-28}$ kg: $\omega = \sqrt{k/\mu} = 1{,}032 \times 10^{15}$ s⁻¹ dan $\tilde\nu = \omega/2\pi c = 5481$ cm⁻¹.

*Cara berpikir:* HF/STO-3G memberi ikatan yang 55% terlalu kaku dan frekuensi 25% terlalu tinggi. Sebagian karena basis minimal (eksponen tetap $\zeta = 1{,}24$ tidak dapat menyesuaikan diri ketika ikatan meregang), sebagian karena HF: tanpa korelasi, energi naik terlalu cepat saat ikatan diregangkan, karena bagian ionik fungsi gelombang RHF makin tidak sesuai. CI penuh dalam basis yang sama sudah menurunkan frekuensinya ke 5002 cm⁻¹.

**Soal {{cilim}}.** Pada $R \to \infty$ tumpang tindih nol, $\sigma_{g,u} = (a \pm b)/\sqrt2$, dan semua integral dua pusat yang melibatkan hasil kali $ab$ atau tolakan $1/R$ hilang. Maka $h_{11} = h_{22} = \varepsilon_\text{H}$ (energi atom H dalam basis), dan dengan uraian $(\sigma\sigma|\sigma\sigma)$ atas fungsi atom: $J_{11} = J_{22} = J_{12} = K_{12} = \tfrac14[(aa|aa) + (bb|bb)] = \tfrac12(aa|aa)$. Jadi $H_{00} = H_{DD} = 2\varepsilon_\text{H} + \tfrac12(aa|aa)$ dan $H_{0D} = \tfrac12(aa|aa)$. Matriks $\begin{pmatrix}h & k\\ k & h\end{pmatrix}$ mempunyai nilai eigen terendah $h - k = 2\varepsilon_\text{H}$ dengan vektor $(1, -1)/\sqrt2$, sehingga $c_D = -c_0$. RHF ($= H_{00}$) berada $\tfrac12(aa|aa)$ di atasnya; untuk STO-3G, $(aa|aa) = 0{,}7746\ E_h$, sehingga galat RHF di jarak tak hingga $0{,}387\ E_h$, lebih dari 1000 kJ/mol.

*Cara berpikir:* $(\sigma_g^2 - \sigma_u^2)/\sqrt2 = (ab + ba)/\sqrt2$ (setelah dinormalisasi ulang): bagian ionik $a^2$ dan $b^2$ saling meniadakan, dan yang tersisa adalah fungsi Heitler–London kovalen murni (subbab 11.11). Galat RHF $\tfrac12(aa|aa)$ adalah energi tolakan rata-rata dari bagian ionik H⁻ yang tidak fisis. Dua konfigurasi berbobot sama adalah definisi korelasi statik.

**Soal {{mp01}}.** $\Phi_0$ adalah fungsi eigen $\hat H^{(0)} = \sum_i\hat f(i)$ dengan nilai eigen $E^{(0)} = \sum_i\varepsilon_i$ (jumlah atas spin-orbital terisi). Koreksi orde pertama $E^{(1)} = \langle\Phi_0|\hat H - \hat H^{(0)}|\Phi_0\rangle = E_\text{HF} - \sum_i\varepsilon_i$, karena $\langle\Phi_0|\hat H|\Phi_0\rangle = E_\text{HF}$ menurut definisi. Jumlahnya $E^{(0)} + E^{(1)} = E_\text{HF}$. Secara eksplisit, $E^{(1)} = -\tfrac12\sum_{ij}(J_{ij} - K_{ij})$, koreksi untuk tolakan yang dihitung dua kali dalam $\sum\varepsilon_i$.

*Cara berpikir:* teori perturbasi MP "menemukan kembali" Hartree–Fock pada orde pertama, sehingga semua korelasi muncul mulai orde kedua. Pembagian lain (misalnya Epstein–Nesbet) memberi deret yang berbeda; pembagian Møller–Plesset dipilih karena konsisten ukuran pada setiap orde.

**Soal {{xc1}}.** Untuk satu elektron, fungsi gelombang tepat adalah satu orbital $\phi$ dengan $\rho = |\phi|^2$, dan energi tepat $E = T + \int v\rho$ tanpa tolakan apa pun. Sistem Kohn–Sham satu elektron mempunyai orbital yang sama, sehingga $T_s = T$. Dari (17.47), $E = T_s + \int v\rho + J[\rho] + E_{xc}[\rho]$; agar sama dengan energi tepat, $E_{xc}[\rho] = -J[\rho]$. Karena tidak ada elektron lain untuk dikorelasikan, $E_c = 0$ dan $E_x = -J$.

*Cara berpikir:* syarat ini, kebebasan dari interaksi diri satu elektron, dipenuhi otomatis oleh HF ($J_{ii} = K_{ii}$) tetapi tidak oleh LDA dan GGA. Untuk atom H, LSDA memberi $J + E_{xc} = +0{,}020\ E_h$ (Contoh 17.52). Koreksi interaksi diri Perdew–Zunger dan fungsional hibrida adalah dua cara memulihkan syarat ini sebagian.

**Soal {{born}}.** Isi bola konduktor berjari-jari $a$ sedikit demi sedikit dari muatan 0 sampai $q$. Pada muatan antara $q'$, potensial permukaan dalam vakum $\phi = q'/4\pi\varepsilon_0a$, dan kerja untuk menambah $dq'$ adalah $\phi\,dq'$. Kerja total $W_\text{vak} = \int_0^q\frac{q'}{4\pi\varepsilon_0a}dq' = \frac{q^2}{8\pi\varepsilon_0a}$. Dalam dielektrik, potensial berkurang dengan faktor $\varepsilon_r$, sehingga $W_\text{diel} = q^2/8\pi\varepsilon_0\varepsilon_ra$. Energi bebas solvasi elektrostatik adalah selisihnya (memindahkan ion bermuatan dari vakum ke pelarut sama dengan membuang muatan di vakum lalu mengisinya kembali di pelarut): $\Delta G = W_\text{diel} - W_\text{vak} = -\frac{q^2}{8\pi\varepsilon_0a}(1 - 1/\varepsilon_r)$. Dikali $N_A$ dengan $q = ze$: (17.56).

*Cara berpikir:* faktor $(1 - 1/\varepsilon_r)$ sudah 0,987 untuk air, sehingga energi solvasi ion hampir tidak peka terhadap $\varepsilon_r$ bila pelarutnya polar, tetapi sangat peka terhadap jari-jari rongga. Model kontinum modern pada dasarnya adalah perumuman persamaan Born untuk rongga berbentuk molekul dan rapat muatan sembarang.

**Soal {{rasio}}.** Untuk dua jalur dari reaktan yang sama, $k_1/k_2 = \exp[-(\Delta G_1^\ddagger - \Delta G_2^\ddagger)/RT]$, karena faktor $k_BT/h$ dan $\kappa$ (bila serupa) saling meniadakan. Dengan $\Delta\Delta G^\ddagger = 6$ kJ/mol: pada 298 K, $e^{6000/2479} = e^{2{,}42} = 11{,}3$; pada 348 K, $e^{6000/2894} = e^{2{,}07} = 7{,}9$.

*Cara berpikir:* perbandingan produk kinetik hanya memerlukan selisih penghalang dua keadaan transisi yang sering mirip strukturnya, sehingga galat metode banyak yang meniadakan diri; ketelitian 2–4 kJ/mol untuk selisih semacam ini sering dapat dicapai dengan DFT yang baik, padahal penghalang mutlaknya mungkin meleset 10 kJ/mol. Menaikkan suhu menurunkan selektivitas, sesuai pengalaman sintesis bahwa reaksi selektif sering dijalankan pada suhu rendah.

# Bacaan lanjut

1. A. Szabo dan N. S. Ostlund, *Modern Quantum Chemistry: Introduction to Advanced Electronic Structure Theory* (Dover, 1996). Penurunan Hartree–Fock, persamaan Roothaan, CI, MP, dan CC yang sangat jernih, dengan contoh H₂ dan HeH⁺ dalam basis minimal.
2. F. Jensen, *Introduction to Computational Chemistry*, edisi ke-3 (Wiley, 2017). Tinjauan menyeluruh metode, basis, sifat molekul, dan praktik perhitungan.
3. C. J. Cramer, *Essentials of Computational Chemistry: Theories and Models*, edisi ke-2 (Wiley, 2004). Sangat baik untuk mekanika molekul, metode semiempiris, solvasi, dan studi kasus.
4. T. Helgaker, P. Jørgensen, dan J. Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000). Rujukan lanjut untuk integral Gauss, basis berkorelasi konsisten, dan teori *coupled-cluster*.
5. W. Koch dan M. C. Holthausen, *A Chemist's Guide to Density Functional Theory*, edisi ke-2 (Wiley-VCH, 2001). Pengantar DFT yang ditulis untuk kimiawan, lengkap dengan penilaian kinerja fungsional.
6. I. N. Levine, *Quantum Chemistry*, edisi ke-7 (Pearson, 2014), Bab 13–17. Hartree–Fock molekul, korelasi, DFT, dan metode semiempiris pada tingkat buku kuliah.
