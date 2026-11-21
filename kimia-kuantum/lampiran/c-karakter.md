# Lampiran C Tabel Karakter Grup Titik Umum

Tabel karakter dipakai di Bab 10 dan seterusnya untuk memberi label simetri orbital, getaran, dan keadaan elektronik, serta untuk menentukan aturan seleksi. Lampiran ini memuat grup titik yang paling sering dijumpai dalam kimia. Semua tabel berhingga telah diperiksa memenuhi hubungan ortogonalitas $\sum_cg_c\chi_i(c)\chi_j(c) = h\,\delta_{ij}$ dan $\sum_id_i^2 = h$.

## C.1 Cara membaca dan memakai tabel

Setiap tabel memuat: nama grup (pojok kiri atas); kelas operasi simetri dengan banyaknya operasi di depannya (misalnya $2C_3$ berarti dua operasi rotasi $C_3$ dalam satu kelas); label representasi tak tereduksi (baris) dengan karakternya; dan dua kolom fungsi basis. Kolom "Linear, rotasi" menunjukkan simetri koordinat $x$, $y$, $z$ (yang menentukan aktivitas inframerah dan aturan seleksi dipol listrik) dan rotasi $R_x$, $R_y$, $R_z$. Kolom "Kuadrat" menunjukkan simetri hasil kali dua koordinat (yang menentukan aktivitas Raman dan simetri orbital d).

Konvensi label (Mulliken): A dan B berdimensi satu (simetris dan antisimetris terhadap sumbu utama), E berdimensi dua, T berdimensi tiga; indeks g/u menyatakan simetris/antisimetris terhadap inversi; aksen ′/″ menyatakan simetris/antisimetris terhadap $\sigma_h$; indeks 1/2 menyatakan simetris/antisimetris terhadap $C_2$ tegak lurus sumbu utama atau terhadap $\sigma_v$.

**Rumus reduksi.** Banyaknya kali representasi tak tereduksi $\Gamma_i$ muncul dalam representasi tereduksi dengan karakter $\chi(c)$ adalah

$$
n_i = \frac1h\sum_cg_c\,\chi_i(c)\,\chi(c) ,
$$

dengan $h$ orde grup dan $g_c$ banyaknya operasi dalam kelas $c$ (subbab 10.6).

**Hasil kali langsung.** Karakter hasil kali langsung adalah hasil kali karakter. Aturan cepat: $g \times g = u \times u = g$, $g \times u = u$; $\prime \times \prime = \prime\prime \times \prime\prime = \prime$, $\prime \times \prime\prime = \prime\prime$; A × B = B, B × B = A (untuk grup dengan satu jenis B); $1 \times 1 = 2 \times 2 = 1$, $1 \times 2 = 2$. Integral $\int\psi_a\hat O\psi_b\,d\tau$ dapat tidak nol hanya bila hasil kali langsung $\Gamma_a \times \Gamma_O \times \Gamma_b$ memuat representasi simetris penuh.

**Menentukan grup titik.** Urutan pemeriksaan yang lazim: (1) linear? Bila ya, ada pusat inversi → $D_{\infty h}$, tidak ada → $C_{\infty v}$. (2) Simetri tinggi (beberapa sumbu $C_3$)? Tetrahedron → $T_d$, oktahedron/kubus → $O_h$, ikosahedron → $I_h$. (3) Cari sumbu utama $C_n$ dengan $n$ terbesar. Bila tidak ada sumbu sama sekali: bidang cermin → $C_s$, pusat inversi → $C_i$, tidak ada apa-apa → $C_1$. (4) Ada $n$ sumbu $C_2$ tegak lurus $C_n$? Bila ya, grup D: dengan $\sigma_h$ → $D_{nh}$, dengan $n$ bidang $\sigma_d$ → $D_{nd}$, tanpa bidang → $D_n$. Bila tidak, grup C: dengan $\sigma_h$ → $C_{nh}$, dengan $n$ bidang $\sigma_v$ → $C_{nv}$, tanpa bidang → $C_n$ (atau $S_{2n}$ bila ada sumbu rotasi tak wajar $S_{2n}$ saja).

## C.2 Grup-grup berhingga

**C~1~** (contoh: CHFClBr)

| C~1~ | E | Linear, rotasi | Kuadrat |
|---|---|---|---|
| A | 1 |  | semua |

**C~s~** (contoh: HOCl, CH₂ClBr)

| C~s~ | E | σ~h~ | Linear, rotasi | Kuadrat |
|---|---|---|---|---|
| A′ | 1 | 1 | x, y, R~z~ | x², y², z², xy |
| A″ | 1 | −1 | z, R~x~, R~y~ | yz, xz |

**C~i~** (contoh: meso-CHClBr–CHClBr, konformasi anti)

| C~i~ | E | i | Linear, rotasi | Kuadrat |
|---|---|---|---|---|
| A~g~ | 1 | 1 | R~x~, R~y~, R~z~ | x², y², z², xy, xz, yz |
| A~u~ | 1 | −1 | x, y, z |  |

**C~2~** (contoh: H₂O₂)

| C~2~ | E | C~2~ | Linear, rotasi | Kuadrat |
|---|---|---|---|---|
| A | 1 | 1 | z, R~z~ | x², y², z², xy |
| B | 1 | −1 | x, y, R~x~, R~y~ | yz, xz |

**C~2v~** (contoh: H₂O, CH₂Cl₂, SO₂)

| C~2v~ | E | C~2~ | σ~v~(xz) | σ~v~′(yz) | Linear, rotasi | Kuadrat |
|---|---|---|---|---|---|---|
| A~1~ | 1 | 1 | 1 | 1 | z | x², y², z² |
| A~2~ | 1 | 1 | −1 | −1 | R~z~ | xy |
| B~1~ | 1 | −1 | 1 | −1 | x, R~y~ | xz |
| B~2~ | 1 | −1 | −1 | 1 | y, R~x~ | yz |

**C~3v~** (contoh: NH₃, CHCl₃, CH₃F)

| C~3v~ | E | 2C~3~ | 3σ~v~ | Linear, rotasi | Kuadrat |
|---|---|---|---|---|---|
| A~1~ | 1 | 1 | 1 | z | x² + y², z² |
| A~2~ | 1 | 1 | −1 | R~z~ |  |
| E | 2 | −1 | 0 | (x, y), (R~x~, R~y~) | (x² − y², xy), (xz, yz) |

**C~4v~** (contoh: BrF₅, XeOF₄)

| C~4v~ | E | 2C~4~ | C~2~ | 2σ~v~ | 2σ~d~ | Linear, rotasi | Kuadrat |
|---|---|---|---|---|---|---|---|
| A~1~ | 1 | 1 | 1 | 1 | 1 | z | x² + y², z² |
| A~2~ | 1 | 1 | 1 | −1 | −1 | R~z~ |  |
| B~1~ | 1 | −1 | 1 | 1 | −1 |  | x² − y² |
| B~2~ | 1 | −1 | 1 | −1 | 1 |  | xy |
| E | 2 | 0 | −2 | 0 | 0 | (x, y), (R~x~, R~y~) | (xz, yz) |

**C~2h~** (contoh: trans-N₂H₂, trans-CHCl=CHCl)

| C~2h~ | E | C~2~ | i | σ~h~ | Linear, rotasi | Kuadrat |
|---|---|---|---|---|---|---|
| A~g~ | 1 | 1 | 1 | 1 | R~z~ | x², y², z², xy |
| B~g~ | 1 | −1 | 1 | −1 | R~x~, R~y~ | xz, yz |
| A~u~ | 1 | 1 | −1 | −1 | z |  |
| B~u~ | 1 | −1 | −1 | 1 | x, y |  |

**D~2h~** (contoh: C₂H₄, naftalena, B₂H₆)

| D~2h~ | E | C~2~(z) | C~2~(y) | C~2~(x) | i | σ(xy) | σ(xz) | σ(yz) | Linear, rotasi | Kuadrat |
|---|---|---|---|---|---|---|---|---|---|---|
| A~g~ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  | x², y², z² |
| B~1g~ | 1 | 1 | −1 | −1 | 1 | 1 | −1 | −1 | R~z~ | xy |
| B~2g~ | 1 | −1 | 1 | −1 | 1 | −1 | 1 | −1 | R~y~ | xz |
| B~3g~ | 1 | −1 | −1 | 1 | 1 | −1 | −1 | 1 | R~x~ | yz |
| A~u~ | 1 | 1 | 1 | 1 | −1 | −1 | −1 | −1 |  |  |
| B~1u~ | 1 | 1 | −1 | −1 | −1 | −1 | 1 | 1 | z |  |
| B~2u~ | 1 | −1 | 1 | −1 | −1 | 1 | −1 | 1 | y |  |
| B~3u~ | 1 | −1 | −1 | 1 | −1 | 1 | 1 | −1 | x |  |

**D~3h~** (contoh: BF₃, PCl₅, CO₃²⁻)

| D~3h~ | E | 2C~3~ | 3C~2~ | σ~h~ | 2S~3~ | 3σ~v~ | Linear, rotasi | Kuadrat |
|---|---|---|---|---|---|---|---|---|
| A~1~′ | 1 | 1 | 1 | 1 | 1 | 1 |  | x² + y², z² |
| A~2~′ | 1 | 1 | −1 | 1 | 1 | −1 | R~z~ |  |
| E′ | 2 | −1 | 0 | 2 | −1 | 0 | (x, y) | (x² − y², xy) |
| A~1~″ | 1 | 1 | 1 | −1 | −1 | −1 |  |  |
| A~2~″ | 1 | 1 | −1 | −1 | −1 | 1 | z |  |
| E″ | 2 | −1 | 0 | −2 | 1 | 0 | (R~x~, R~y~) | (xz, yz) |

**D~3d~** (contoh: etana (goyang), sikloheksana (kursi))

| D~3d~ | E | 2C~3~ | 3C~2~ | i | 2S~6~ | 3σ~d~ | Linear, rotasi | Kuadrat |
|---|---|---|---|---|---|---|---|---|
| A~1g~ | 1 | 1 | 1 | 1 | 1 | 1 |  | x² + y², z² |
| A~2g~ | 1 | 1 | −1 | 1 | 1 | −1 | R~z~ |  |
| E~g~ | 2 | −1 | 0 | 2 | −1 | 0 | (R~x~, R~y~) | (x² − y², xy), (xz, yz) |
| A~1u~ | 1 | 1 | 1 | −1 | −1 | −1 |  |  |
| A~2u~ | 1 | 1 | −1 | −1 | −1 | 1 | z |  |
| E~u~ | 2 | −1 | 0 | −2 | 1 | 0 | (x, y) |  |

**D~4h~** (contoh: XeF₄, [PtCl₄]²⁻)

| D~4h~ | E | 2C~4~ | C~2~ | 2C~2~′ | 2C~2~″ | i | 2S~4~ | σ~h~ | 2σ~v~ | 2σ~d~ | Linear, rotasi | Kuadrat |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A~1g~ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  | x² + y², z² |
| A~2g~ | 1 | 1 | 1 | −1 | −1 | 1 | 1 | 1 | −1 | −1 | R~z~ |  |
| B~1g~ | 1 | −1 | 1 | 1 | −1 | 1 | −1 | 1 | 1 | −1 |  | x² − y² |
| B~2g~ | 1 | −1 | 1 | −1 | 1 | 1 | −1 | 1 | −1 | 1 |  | xy |
| E~g~ | 2 | 0 | −2 | 0 | 0 | 2 | 0 | −2 | 0 | 0 | (R~x~, R~y~) | (xz, yz) |
| A~1u~ | 1 | 1 | 1 | 1 | 1 | −1 | −1 | −1 | −1 | −1 |  |  |
| A~2u~ | 1 | 1 | 1 | −1 | −1 | −1 | −1 | −1 | 1 | 1 | z |  |
| B~1u~ | 1 | −1 | 1 | 1 | −1 | −1 | 1 | −1 | −1 | 1 |  |  |
| B~2u~ | 1 | −1 | 1 | −1 | 1 | −1 | 1 | −1 | 1 | −1 |  |  |
| E~u~ | 2 | 0 | −2 | 0 | 0 | −2 | 0 | 2 | 0 | 0 | (x, y) |  |

**D~6h~** (contoh: benzena)

| D~6h~ | E | 2C~6~ | 2C~3~ | C~2~ | 3C~2~′ | 3C~2~″ | i | 2S~3~ | 2S~6~ | σ~h~ | 3σ~d~ | 3σ~v~ | Linear, rotasi | Kuadrat |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A~1g~ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  | x² + y², z² |
| A~2g~ | 1 | 1 | 1 | 1 | −1 | −1 | 1 | 1 | 1 | 1 | −1 | −1 | R~z~ |  |
| B~1g~ | 1 | −1 | 1 | −1 | 1 | −1 | 1 | −1 | 1 | −1 | 1 | −1 |  |  |
| B~2g~ | 1 | −1 | 1 | −1 | −1 | 1 | 1 | −1 | 1 | −1 | −1 | 1 |  |  |
| E~1g~ | 2 | 1 | −1 | −2 | 0 | 0 | 2 | 1 | −1 | −2 | 0 | 0 | (R~x~, R~y~) | (xz, yz) |
| E~2g~ | 2 | −1 | −1 | 2 | 0 | 0 | 2 | −1 | −1 | 2 | 0 | 0 |  | (x² − y², xy) |
| A~1u~ | 1 | 1 | 1 | 1 | 1 | 1 | −1 | −1 | −1 | −1 | −1 | −1 |  |  |
| A~2u~ | 1 | 1 | 1 | 1 | −1 | −1 | −1 | −1 | −1 | −1 | 1 | 1 | z |  |
| B~1u~ | 1 | −1 | 1 | −1 | 1 | −1 | −1 | 1 | −1 | 1 | −1 | 1 |  |  |
| B~2u~ | 1 | −1 | 1 | −1 | −1 | 1 | −1 | 1 | −1 | 1 | 1 | −1 |  |  |
| E~1u~ | 2 | 1 | −1 | −2 | 0 | 0 | −2 | −1 | 1 | 2 | 0 | 0 | (x, y) |  |
| E~2u~ | 2 | −1 | −1 | 2 | 0 | 0 | −2 | 1 | 1 | −2 | 0 | 0 |  |  |

**T~d~** (contoh: CH₄, CCl₄, [NiCl₄]²⁻)

| T~d~ | E | 8C~3~ | 3C~2~ | 6S~4~ | 6σ~d~ | Linear, rotasi | Kuadrat |
|---|---|---|---|---|---|---|---|
| A~1~ | 1 | 1 | 1 | 1 | 1 |  | x² + y² + z² |
| A~2~ | 1 | 1 | 1 | −1 | −1 |  |  |
| E | 2 | −1 | 2 | 0 | 0 |  | (2z² − x² − y², x² − y²) |
| T~1~ | 3 | 0 | −1 | 1 | −1 | (R~x~, R~y~, R~z~) |  |
| T~2~ | 3 | 0 | −1 | −1 | 1 | (x, y, z) | (xy, xz, yz) |

**O~h~** (contoh: SF₆, [Co(NH₃)₆]³⁺)

| O~h~ | E | 8C~3~ | 6C~2~ | 6C~4~ | 3C~2~(=C~4~²) | i | 6S~4~ | 8S~6~ | 3σ~h~ | 6σ~d~ | Linear, rotasi | Kuadrat |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A~1g~ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  | x² + y² + z² |
| A~2g~ | 1 | 1 | −1 | −1 | 1 | 1 | −1 | 1 | 1 | −1 |  |  |
| E~g~ | 2 | −1 | 0 | 0 | 2 | 2 | 0 | −1 | 2 | 0 |  | (2z² − x² − y², x² − y²) |
| T~1g~ | 3 | 0 | −1 | 1 | −1 | 3 | 1 | 0 | −1 | −1 | (R~x~, R~y~, R~z~) |  |
| T~2g~ | 3 | 0 | 1 | −1 | −1 | 3 | −1 | 0 | −1 | 1 |  | (xy, xz, yz) |
| A~1u~ | 1 | 1 | 1 | 1 | 1 | −1 | −1 | −1 | −1 | −1 |  |  |
| A~2u~ | 1 | 1 | −1 | −1 | 1 | −1 | 1 | −1 | −1 | 1 |  |  |
| E~u~ | 2 | −1 | 0 | 0 | 2 | −2 | 0 | 1 | −2 | 0 |  |  |
| T~1u~ | 3 | 0 | −1 | 1 | −1 | −3 | −1 | 0 | 1 | 1 | (x, y, z) |  |
| T~2u~ | 3 | 0 | 1 | −1 | −1 | −3 | 1 | 0 | 1 | −1 |  |  |

## C.3 Grup linear

**C~∞v~** (contoh: HCl, CO, HCN)

| C~∞v~ | E | 2C~∞~^φ^ | ∞σ~v~ | Linear, rotasi | Kuadrat |
|---|---|---|---|---|---|
| A~1~ = Σ⁺ | 1 | 1 | 1 | z | x² + y², z² |
| A~2~ = Σ⁻ | 1 | 1 | −1 | R~z~ |  |
| E~1~ = Π | 2 | 2 cos φ | 0 | (x, y), (R~x~, R~y~) | (xz, yz) |
| E~2~ = Δ | 2 | 2 cos 2φ | 0 |  | (x² − y², xy) |
| E~3~ = Φ | 2 | 2 cos 3φ | 0 |  |  |

**D~∞h~** (contoh: H₂, N₂, CO₂, C₂H₂)

| D~∞h~ | E | 2C~∞~^φ^ | ∞σ~v~ | i | 2S~∞~^φ^ | ∞C~2~ | Linear, rotasi | Kuadrat |
|---|---|---|---|---|---|---|---|---|
| Σ~g~⁺ | 1 | 1 | 1 | 1 | 1 | 1 |  | x² + y², z² |
| Σ~g~⁻ | 1 | 1 | −1 | 1 | 1 | −1 | R~z~ |  |
| Π~g~ | 2 | 2 cos φ | 0 | 2 | −2 cos φ | 0 | (R~x~, R~y~) | (xz, yz) |
| Δ~g~ | 2 | 2 cos 2φ | 0 | 2 | 2 cos 2φ | 0 |  | (x² − y², xy) |
| Σ~u~⁺ | 1 | 1 | 1 | −1 | −1 | −1 | z |  |
| Σ~u~⁻ | 1 | 1 | −1 | −1 | −1 | 1 |  |  |
| Π~u~ | 2 | 2 cos φ | 0 | −2 | 2 cos φ | 0 | (x, y) |  |
| Δ~u~ | 2 | 2 cos 2φ | 0 | −2 | −2 cos 2φ | 0 |  |  |

Untuk grup linear, rumus reduksi biasa tidak dapat dipakai langsung karena ordenya tak berhingga. Cara praktisnya adalah mereduksi ke subgrup berhingga yang sesuai: $C_{2v}$ untuk $C_{\infty v}$ dan $D_{2h}$ untuk $D_{\infty h}$, lalu menghubungkan kembali labelnya (misalnya $\Sigma_g^+ \to A_g$, $\Sigma_u^+ \to B_{1u}$, $\Pi_u \to B_{2u} + B_{3u}$).

## C.4 Grup titik beberapa molekul

| Molekul | Grup | Molekul | Grup |
|---|---|---|---|
| H₂O, SO₂, CH₂Cl₂, formaldehida | $C_{2v}$ | CH₄, CCl₄, P₄ | $T_d$ |
| NH₃, PCl₃, CHCl₃ | $C_{3v}$ | SF₆, [Fe(CN)₆]⁴⁻ | $O_h$ |
| BF₃, SO₃, CO₃²⁻, PF₅ | $D_{3h}$ | etilena, naftalena, diborana | $D_{2h}$ |
| XeF₄, [PtCl₄]²⁻, siklobutadiena (persegi) | $D_{4h}$ | benzena | $D_{6h}$ |
| etana (goyang), sikloheksana (kursi) | $D_{3d}$ | etana (eklips) | $D_{3h}$ |
| H₂O₂ | $C_2$ | trans-N₂H₂, trans-dikloroetena | $C_{2h}$ |
| HOCl, CH₂ClBr | $C_s$ | CHFClBr | $C_1$ |
| HCl, HCN, OCS | $C_{\infty v}$ | H₂, CO₂, C₂H₂ | $D_{\infty h}$ |

