## 16.8 Model vektor, pulsa, dan FID

### Dari spin tunggal ke magnetisasi

Spektrometer tidak melihat satu spin, melainkan magnetisasi $\mathbf M$, jumlah momen magnet semua inti dalam sampel. Karena (16.13) berlaku untuk nilai harap setiap spin dan bersifat linear, magnetisasi juga mematuhi persamaan gerak klasik

$$
\frac{d\mathbf M}{dt} = \gamma\,\mathbf M \times \mathbf B(t) . \qquad \text{(16.31)}
$$

Pada kesetimbangan, $\mathbf M = M_0\hat{\mathbf z}$ (subbab 16.3), sejajar medan, sehingga tidak berpresesi dan tidak menghasilkan sinyal. Untuk mendapat sinyal, magnetisasi harus dimiringkan menjauhi sumbu $z$. Inilah tugas **pulsa** gelombang radio.

### Kerangka berputar

Medan pulsa $\mathbf B_1$ berputar dalam bidang $xy$ dengan frekuensi pemancar $\omega$ yang dekat dengan $\omega_0$ (medan linear $2B_1\cos\omega t$ dapat diuraikan menjadi dua komponen berputar berlawanan; hanya komponen yang berputar searah presesi yang berpengaruh). Dilihat dari laboratorium, gerak $\mathbf M$ di bawah $B_0$ dan $B_1$ sekaligus rumit. Tetapi bila kita memandangnya dari **kerangka berputar**, sistem koordinat $x'y'z$ yang berputar terhadap $z$ dengan frekuensi $\omega$, medan $\mathbf B_1$ tampak diam, misalnya sepanjang $x'$. Dalam kerangka ini, gerak presesi dengan frekuensi $\omega$ "dihapus" seperti penumpang komidi putar yang melihat penumpang lain diam. Medan statis yang tersisa berkurang sebesar $\omega/\gamma$, dan magnetisasi merasakan **medan efektif**

$$
\mathbf B_\text{ef} = \left(B_0 - \frac\omega\gamma\right)\hat{\mathbf z} + B_1\hat{\mathbf x}' = \frac{\Omega}{\gamma}\hat{\mathbf z} + B_1\hat{\mathbf x}' , \qquad \text{(16.32)}
$$

dengan $\Omega = \omega_0 - \omega$ **frekuensi ofset**. Tepat pada resonansi ($\Omega = 0$), medan efektif hanya $B_1$ sepanjang $x'$, dan magnetisasi berpresesi mengelilingi sumbu $x'$ dengan frekuensi **nutasi** $\omega_1 = \gamma B_1$. Pulsa sepanjang $t_p$ memutar $\mathbf M$ sebesar **sudut balik**

$$
\theta = \gamma B_1t_p . \qquad \text{(16.33)}
$$

Pulsa **90°** ($\theta = \pi/2$) memindahkan seluruh magnetisasi dari $z$ ke sumbu $-y'$ (dengan aturan tangan kanan untuk $\gamma > 0$). Pulsa **180°** membalikkannya ke $-z$, menukar populasi $\alpha$ dan $\beta$. Ini adalah osilasi Rabi (Contoh 4.44) yang dilihat secara klasik: populasi berpindah bolak-balik dengan frekuensi $\omega_1$ selama medan resonansi menyala.

Kerangka berputar juga menjelaskan apa yang terjadi di luar resonansi. Bila $|\Omega| \ll \omega_1$, medan efektif hampir sejajar $x'$ dan pulsa masih bekerja dengan baik. Bila $|\Omega| \gtrsim \omega_1$, medan efektif condong ke $z$, dan magnetisasi hanya sedikit dimiringkan. Agar semua garis dalam spektrum tereksitasi merata, pulsa harus pendek dan kuat: $\omega_1/2\pi$ harus lebih besar daripada lebar spektrum. Pulsa 90° untuk proton biasanya 5–15 μs.

![Gambar 16.7 Model vektor dalam kerangka berputar. (a) Pulsa B₁ sepanjang x′ memutar M₀ dari sumbu z ke −y′ (pulsa 90°). (b) Setelah pulsa, magnetisasi transversal berpresesi dengan frekuensi ofset Ω sambil meluruh (T₂), dan M_z pulih (T₁). (c) Bagian riil FID yang berisi dua garis (+120 Hz dan −250 Hz). (d) Spektrum hasil transformasi Fourier-nya (Contoh 16.36).](fig/c_vektor.png){width=96%}

### Peluruhan induksi bebas dan transformasi Fourier

Setelah pulsa 90°, pemancar dimatikan. Magnetisasi transversal berpresesi dengan frekuensi Larmornya sendiri dan menginduksi tegangan bolak-balik di kumparan. Sinyal ini meluruh karena relaksasi (subbab 16.9) dan disebut **peluruhan induksi bebas** (*free induction decay*, FID). Penerima mencampurnya dengan frekuensi pembawa, sehingga yang direkam hanyalah frekuensi ofset. Untuk satu jenis inti dengan ofset $\Omega$,

$$
s(t) = M_0\sin\theta\;e^{i\Omega t}\,e^{-t/T_2} , \qquad \text{(16.34)}
$$

dengan $T_2$ waktu peluruhan magnetisasi transversal. Penerima mengukur dua komponen, $M_{x'}$ dan $M_{y'}$, yang digabung menjadi satu bilangan kompleks; dengan cara ini arah presesi, dan karena itu tanda $\Omega$, dapat dibedakan (**deteksi kuadratur**).

Bila sampel mengandung banyak jenis inti, FID adalah jumlah banyak sinusoid teredam, satu untuk setiap garis. Untuk mengurai jumlah ini menjadi komponen-komponennya, kita memakai **transformasi Fourier** (subbab 2.9):

$$
S(\nu) = \int_0^\infty s(t)\,e^{-i2\pi\nu t}\,dt . \qquad \text{(16.35)}
$$

Untuk (16.34), integralnya adalah fungsi Lorentz dengan pusat di $\nu = \Omega/2\pi$ dan lebar setengah tinggi

$$
\Delta\nu_{1/2} = \frac{1}{\pi T_2} . \qquad \text{(16.36)}
$$

Peluruhan yang lambat memberi garis yang tajam. Ini adalah hubungan Fourier umum antara lama hidup dan lebar spektrum (subbab 15.3).

**NMR transformasi Fourier** (FT-NMR), yang dikembangkan Richard Ernst pada tahun 1966, mengubah NMR. Spektrometer gelombang malar (*continuous wave*) yang lebih tua menyapu frekuensi perlahan dan mengamati satu unsur resolusi setiap saat. Pulsa pendek mengeksitasi semua garis sekaligus, dan FID berisi informasi tentang semuanya. Bila spektrum mempunyai $M$ unsur resolusi, FT-NMR memperoleh S/N yang $\sqrt M$ kali lebih besar dalam waktu yang sama (**keunggulan Fellgett**). Keunggulan ini memungkinkan NMR ¹³C rutin, dan pulsa yang dapat dirangkai bebas membuka jalan ke NMR dua dimensi (subbab 16.10). Ernst menerima Hadiah Nobel Kimia 1991 untuk kedua sumbangan ini.

### Persamaan Bloch

Felix Bloch (1946) menambahkan relaksasi ke (16.31) secara fenomenologis:

$$
\frac{dM_x}{dt} = \gamma(\mathbf M \times \mathbf B)_x - \frac{M_x}{T_2}, \quad
\frac{dM_y}{dt} = \gamma(\mathbf M \times \mathbf B)_y - \frac{M_y}{T_2}, \quad
\frac{dM_z}{dt} = \gamma(\mathbf M \times \mathbf B)_z - \frac{M_z - M_0}{T_1} . \qquad \text{(16.37)}
$$

Komponen transversal meluruh ke nol dengan waktu $T_2$, dan komponen longitudinal kembali ke $M_0$ dengan waktu $T_1$. Persamaan Bloch adalah model kerja hampir semua NMR berpulsa dan MRI; asal-usul kedua waktu relaksasi kita bahas di subbab berikut.

::: {.dalam}
**Pengambilan cuplikan dan resolusi digital**

FID direkam sebagai $N$ titik dengan selang waktu $\Delta t$ (*dwell time*). Menurut teorema Nyquist, deteksi kuadratur dengan selang $\Delta t$ dapat membedakan frekuensi dalam jendela selebar $\text{SW} = 1/\Delta t$ (*spectral width*); frekuensi di luar jendela "terlipat" ke dalam (*aliasing*). Lama perekaman $t_\text{aq} = N\Delta t = N/\text{SW}$ menentukan resolusi digital $1/t_\text{aq}$: dua garis yang lebih dekat dari sekitar $1/t_\text{aq}$ tidak dapat dipisahkan, betapapun tajamnya garis aslinya. Agar resolusi tidak dibatasi perekaman, $t_\text{aq}$ harus beberapa kali $T_2$. Sebaliknya, merekam jauh lebih lama daripada $T_2$ hanya menambah derau, karena sinyalnya sudah habis.
:::

::: {.contoh}
**Contoh 16.33 · Kuat medan pulsa**

Pulsa 90° untuk proton pada spektrometer 400 MHz lamanya 10 μs. Hitung $\omega_1$, $B_1$, dan $\nu_1 = \omega_1/2\pi$. Apakah pulsa ini cukup untuk mengeksitasi rentang proton 12 ppm? Bagaimana untuk ¹³C (220 ppm pada 100,6 MHz) dengan $\nu_1$ yang sama?

**Penyelesaian.** $\omega_1 = (\pi/2)/t_p = 1{,}571 \times 10^5$ rad/s, $B_1 = \omega_1/\gamma_\text{H} = 0{,}587$ mT, $\nu_1 = 25$ kHz. Rentang proton $12 \times 400 = 4{,}8$ kHz, jadi $|\Omega|/2\pi \le 2{,}4$ kHz bila pembawa di tengah: jauh lebih kecil daripada $\nu_1$. Rentang ¹³C $220 \times 100{,}6 = 22$ kHz, yaitu $\pm11$ kHz dari tengah: sebanding dengan $\nu_1$.

**Memahami hasil.** Untuk proton, eksitasi praktis seragam. Untuk ¹³C dengan $\nu_1 = 25$ kHz, garis di tepi spektrum (karbonil) mengalami medan efektif yang condong, sehingga sudut baliknya meleset dan fasenya bergeser. Spektrometer modern mengatasinya dengan pulsa yang lebih kuat atau pulsa berbentuk khusus (*adiabatic*, *composite*). Medan $B_1$ sebesar setengah militesla dihasilkan oleh kumparan kecil di sekeliling sampel dengan daya beberapa puluh watt.
:::

::: {.contoh}
**Contoh 16.34 · Sudut balik kecil**

Dengan $B_1$ dari Contoh 16.33, berapa lama pulsa 30°? Berapa komponen longitudinal dan transversal magnetisasi sesudahnya, sebagai pecahan $M_0$?

**Penyelesaian.** $t_p = (30/90) \times 10\ \mu\text{s} = 3{,}3$ μs. $M_z = M_0\cos30° = 0{,}866\,M_0$; $M_\perp = M_0\sin30° = 0{,}500\,M_0$.

**Memahami hasil.** Pulsa 30° memberi separuh sinyal maksimum tetapi hanya menghabiskan 13% magnetisasi longitudinal. Bila perekaman diulang cepat, magnetisasi tidak sempat pulih penuh di antara pulsa (subbab 16.9), dan pulsa kecil semacam ini memberi S/N per satuan waktu yang lebih besar daripada pulsa 90°. Perekaman ¹³C rutin hampir selalu memakai pulsa 30°–45°.
:::

::: {.contoh}
**Contoh 16.35 · Merancang perekaman**

Spektrum proton direkam pada 400 MHz dengan jendela 12 ppm dan 32 768 titik kompleks. Hitung lebar jendela dalam Hz, selang cuplikan, lama perekaman, dan resolusi digital. Bila $T_2^*$ sekitar 0,5 s, apakah perekaman cukup panjang?

**Penyelesaian.** SW $= 12 \times 400 = 4800$ Hz; $\Delta t = 1/4800 = 208$ μs; $t_\text{aq} = 32\,768/4800 = 6{,}83$ s; resolusi digital $4800/32\,768 = 0{,}146$ Hz per titik. Dengan $T_2^* = 0{,}5$ s, lebar garis $1/\pi T_2^* = 0{,}64$ Hz, dan $t_\text{aq}$ sekitar 14 kali $T_2^*$.

**Memahami hasil.** Resolusi digital 0,15 Hz jauh lebih halus daripada lebar garis 0,64 Hz, sehingga yang membatasi pemisahan garis adalah $T_2^*$, bukan lama perekaman. Separuh waktu perekaman terakhir hampir hanya merekam derau; dalam praktik orang sering memakai $t_\text{aq}$ sekitar 3–4 s dan memperpanjang data dengan nol (*zero filling*) sebelum transformasi.
:::

::: {.contoh}
**Contoh 16.36 · Transformasi Fourier dengan NumPy**

Buatlah FID buatan yang berisi dua garis, di +120 Hz (amplitudo 1) dan −250 Hz (amplitudo 0,5), dengan $T_2 = 0{,}2$ s, lalu lakukan transformasi Fourier dan temukan puncak-puncaknya.

**Penyelesaian.**

```python
import numpy as np
SW, N, T2 = 1000.0, 4096, 0.2                 # lebar spektrum (Hz), banyak titik, T2 (s)
t = np.arange(N) / SW                         # waktu cuplik
fid = (np.exp(2j*np.pi*120*t) + 0.5*np.exp(-2j*np.pi*250*t)) * np.exp(-t/T2)
spek = np.fft.fftshift(np.fft.fft(fid)).real  # bagian riil = spektrum serapan
f = np.fft.fftshift(np.fft.fftfreq(N, 1/SW))  # sumbu frekuensi (Hz)
puncak = [f[i] for i in range(1, N-1) if spek[i] > spek[i-1]
          and spek[i] > spek[i+1] and spek[i] > 0.1*spek.max()]
print(puncak)
```

Keluarannya: puncak di −250,0 Hz dan 120,1 Hz, dengan perbandingan tinggi sekitar 1 : 2.

**Memahami hasil.** Puncak kedua tercatat di 120,1 Hz, bukan 120,0, karena titik-titik frekuensi berjarak $\text{SW}/N = 0{,}24$ Hz. Lebar setengah tinggi garis yang sebenarnya $1/\pi T_2 = 1{,}6$ Hz, hanya beberapa titik digital. Tanda frekuensi terbaca benar berkat deteksi kuadratur: FID kompleks $e^{-i2\pi(250)t}$ berputar berlawanan arah dengan $e^{+i2\pi(120)t}$. Dengan hanya satu komponen riil, kedua arah putar tidak dapat dibedakan dan setiap garis akan muncul berpasangan di $\pm\nu$.
:::

::: {.contoh}
**Contoh 16.37 · Keunggulan Fellgett**

Spektrum proton selebar 4800 Hz dengan resolusi 0,5 Hz. Berapa banyak unsur resolusi, dan berapa kali S/N FT-NMR lebih besar daripada sapuan gelombang malar dalam waktu ukur yang sama?

**Penyelesaian.** $M = 4800/0{,}5 = 9600$ unsur. Keunggulan S/N $\sqrt{9600} \approx 98$.

**Memahami hasil.** Untuk S/N yang sama, penghematan waktunya $M \approx 10^4$ kali: percobaan sehari dengan cara lama menjadi beberapa detik. Keunggulan ini paling berharga bila spektrum lebar dan sebagian besar "kosong", seperti spektrum ¹³C. Hal yang sama berlaku bagi spektroskopi inframerah transformasi Fourier (FTIR) dengan interferometer.
:::

::: {.kuis}
**Kuis cepat 16.8**

Setelah pulsa 180°, berapa besar sinyal FID-nya? Bila $B_1$ dilipatduakan, berapa lama pulsa 90° yang baru?
:::

## 16.9 Relaksasi T₁ dan T₂

### Dua cara kembali ke kesetimbangan

Setelah pulsa, sistem spin berada di luar kesetimbangan dan kembali ke sana melalui dua proses yang berbeda sifat.

**Relaksasi longitudinal** (relaksasi spin–kisi), dengan waktu $T_1$, mengembalikan $M_z$ ke $M_0$. Secara mikroskopis, ini adalah pemulihan selisih populasi Boltzmann: spin-spin harus melepaskan energi ke "kisi", yaitu derajat kebebasan translasi dan rotasi molekul. Karena energi berpindah, proses ini memerlukan transisi yang sesungguhnya, dirangsang oleh medan magnet yang berfluktuasi pada frekuensi Larmor.

**Relaksasi transversal** (relaksasi spin–spin), dengan waktu $T_2$, menghapus $M_x$ dan $M_y$. Ini adalah hilangnya **koherensi fase**: spin-spin yang semula berpresesi serempak perlahan-lahan tidak sefase, karena masing-masing merasakan medan lokal yang sedikit berbeda dan berubah-ubah. Tidak perlu ada perpindahan energi; cukup penyebaran frekuensi. Setiap proses yang memulihkan $M_z$ juga merusak $M_\perp$, sehingga selalu $T_2 \le 2T_1$; dalam cairan bermolekul kecil, $T_1 \approx T_2$, sedangkan dalam molekul besar dan padatan $T_2 \ll T_1$.

Dari persamaan Bloch (16.37) tanpa medan pulsa:

$$
M_z(t) = M_0 + [M_z(0) - M_0]\,e^{-t/T_1}, \qquad M_\perp(t) = M_\perp(0)\,e^{-t/T_2} . \qquad \text{(16.38)}
$$

### Mengukur T₁: pemulihan inversi

Urutan pulsa **180° – τ – 90°** mengukur $T_1$. Pulsa 180° membalik magnetisasi ke $-M_0$. Selama jeda $\tau$, $M_z$ pulih menurut (16.38) dengan $M_z(0) = -M_0$:

$$
M_z(\tau) = M_0\left(1 - 2e^{-\tau/T_1}\right) . \qquad \text{(16.39)}
$$

Pulsa 90° kemudian "membaca" $M_z(\tau)$ sebagai sinyal FID. Untuk $\tau$ pendek sinyalnya negatif, untuk $\tau$ panjang positif, dan nol pada $\tau_0 = T_1\ln2$. Setiap garis dalam spektrum mempunyai $T_1$-nya sendiri.

### Mengukur T₂: gema spin

Lebar garis yang teramati biasanya lebih besar daripada $1/\pi T_2$, karena medan magnet tidak seragam sempurna di seluruh volume sampel. Spin di bagian sampel yang berbeda berpresesi dengan frekuensi sedikit berbeda dan cepat kehilangan fase; peluruhan bersih FID ditandai $T_2^*$, dengan $1/T_2^* = 1/T_2 + 1/T_2^\text{inh}$. Erwin Hahn (1950) menemukan cara memisahkan kedua sumbangan: urutan **90° – τ – 180° – τ – gema**. Setelah pulsa 90°, spin-spin menyebar dalam bidang transversal; spin yang lebih cepat mendahului, yang lebih lambat tertinggal. Pulsa 180° membalik seluruh "kipas" spin dalam bidang transversal, sehingga yang tadinya di depan kini di belakang, tetapi masih berlari lebih cepat. Setelah selang $\tau$ yang sama, semua spin berkumpul kembali dan menghasilkan **gema spin**. Ketidakseragaman medan yang tetap terhapus; yang tidak terhapus hanyalah fluktuasi acak yang sesungguhnya, sehingga tinggi gema meluruh sebagai $e^{-2\tau/T_2}$. Analogi yang sering dipakai: pelari dengan kecepatan berbeda yang disuruh berbalik arah pada saat yang sama akan tiba kembali di garis start bersamaan.

![Gambar 16.8 Relaksasi. (a) Pemulihan inversi: M_z(τ) dari −M₀ ke M₀, melewati nol pada τ = T₁ ln 2. (b) Peluruhan transversal dengan T₂ dan T₂*. (c) T₁ dan T₂ relaksasi dipol–dipol sebagai fungsi waktu korelasi τ_c pada 400 MHz (model BPP, dua proton berjarak 1,52 Å); T₁ minimum pada ω₀τ_c ≈ 0,62.](fig/c_relaksasi.png){width=96%}

### Mekanisme: medan lokal yang berfluktuasi

Mengapa spin berelaksasi? Spin inti terisolasi dalam medan yang benar-benar statis tidak akan pernah berelaksasi, karena tidak ada yang menginduksi transisi. Dalam cairan, setiap proton merasakan medan magnet kecil dari momen magnet proton tetangganya. Untuk dua proton dalam molekul air (jarak 1,52 Å), medan dipol ini sekitar 0,8 mT. Molekul berputar acak, sehingga medan lokal ini berfluktuasi. Fluktuasinya dicirikan oleh **waktu korelasi** $\tau_c$, waktu rata-rata molekul berputar sekitar satu radian. Spektrum frekuensi fluktuasi itu, **rapat spektral**,

$$
J(\omega) = \frac{2\tau_c}{1 + \omega^2\tau_c^2} , \qquad \text{(16.40)}
$$

mendatar sampai sekitar $\omega \sim 1/\tau_c$ lalu jatuh. Relaksasi $T_1$ memerlukan komponen fluktuasi pada frekuensi transisi, $\omega_0$ dan $2\omega_0$. Untuk dua spin identik yang berjarak $r$, teori Bloembergen, Purcell, dan Pound (BPP, 1948) memberi

$$
\frac1{T_1} = \frac{3}{10}\left(\frac{\mu_0}{4\pi}\right)^2\frac{\gamma^4\hbar^2}{r^6}\left[\frac{\tau_c}{1 + \omega_0^2\tau_c^2} + \frac{4\tau_c}{1 + 4\omega_0^2\tau_c^2}\right] . \qquad \text{(16.41)}
$$

Relaksasi $T_2$, selain menerima sumbangan yang sama, juga menerima sumbangan dari fluktuasi berfrekuensi nol (medan lokal yang hampir statis menyebarkan fase), sehingga mengandung suku $3\tau_c$ yang tidak bergantung pada $\omega_0$.

Tiga rezim muncul (Gambar 16.8, panel c):

- **Penyempitan ekstrem** ($\omega_0\tau_c \ll 1$), molekul kecil dalam pelarut encer: $1/T_1 = 1/T_2 \propto \tau_c$. Molekul yang berputar lebih cepat berelaksasi lebih lambat, karena energi fluktuasinya tersebar di rentang frekuensi yang lebar dan hanya sedikit yang jatuh di $\omega_0$.
- **Minimum $T_1$** di $\omega_0\tau_c \approx 0{,}62$: fluktuasi paling efisien pada frekuensi Larmor.
- **Gerak lambat** ($\omega_0\tau_c \gg 1$), makromolekul dan padatan: $T_1$ panjang lagi, tetapi $T_2$ terus memendek karena suku frekuensi nol. Garisnya melebar. Inilah sebabnya NMR protein besar sulit: protein 30 kDa mempunyai $\tau_c$ sekitar 10 ns, dan garis-garisnya puluhan Hz lebarnya.

Ketergantungan pada $r^{-6}$ juga penting: relaksasi didominasi oleh tetangga terdekat. Ion paramagnetik dengan elektron tak berpasangan, yang momen magnetnya ratusan kali lebih besar daripada momen proton, mempercepat relaksasi secara dramatis; inilah prinsip bahan kontras gadolinium dalam MRI (subbab 16.12).

### Efek Overhauser inti

Relaksasi dipol–dipol antara dua spin juga mengandung transisi "silang" yang membalik kedua spin bersamaan ($\alpha\beta \leftrightarrow \beta\alpha$ dan $\alpha\alpha \leftrightarrow \beta\beta$). Akibatnya, mengganggu populasi satu spin (S) mengubah populasi spin tetangganya (I). Bila spin S dijenuhkan (populasinya disamakan dengan penyinaran terus-menerus), intensitas sinyal I berubah dengan faktor $1 + \eta$, dengan batas atas pada penyempitan ekstrem

$$
\eta_\text{maks} = \frac{\gamma_S}{2\gamma_I} . \qquad \text{(16.42)}
$$

Ini **efek Overhauser inti** (NOE). Untuk ¹³C dengan proton dijenuhkan, $\eta_\text{maks} = \gamma_\text{H}/2\gamma_\text{C} = 1{,}99$: sinyal ¹³C hampir tiga kali lebih kuat, bonus yang selalu dipakai dalam perekaman ¹³C rutin. Untuk dua proton, $\eta_\text{maks} = 0{,}5$. Karena laju relaksasi silang sebanding dengan $r^{-6}$, NOE antarproton hanya teramati bila jaraknya kurang dari sekitar 5 Å, dan besarnya dapat dipakai sebagai "penggaris" jarak (subbab 16.10).

::: {.contoh}
**Contoh 16.38 · Membaca T₁ dari titik nol**

Dalam percobaan pemulihan inversi, sinyal suatu proton melewati nol pada $\tau = 0{,}69$ s. Hitung $T_1$. Berapa jeda antarperekaman yang diperlukan agar magnetisasi pulih 99%?

**Penyelesaian.** $T_1 = \tau_0/\ln2 = 0{,}69/0{,}693 = 1{,}0$ s. Pemulihan $1 - e^{-t/T_1} = 0{,}99$ memerlukan $t = T_1\ln100 = 4{,}6$ s; aturan praktis "lima kali $T_1$" memberi pemulihan 99,3%.

**Memahami hasil.** Untuk analisis kuantitatif (qNMR), jeda antarperekaman harus sekitar lima kali $T_1$ terpanjang dalam sampel; bila tidak, garis yang $T_1$-nya panjang (misalnya karbon kuaterner atau proton aromatik terisolasi) tampak lebih kecil daripada seharusnya. Untuk spektrum rutin yang tujuannya hanya mengenali struktur, jeda pendek dengan pulsa kecil lebih efisien (Contoh 16.34).
:::

::: {.contoh}
**Contoh 16.39 · Lebar garis dan waktu relaksasi**

Hitung lebar setengah tinggi garis untuk (a) molekul kecil dengan $T_2 = 1{,}0$ s, (b) homogenitas medan yang memberi $T_2^* = 0{,}3$ s, (c) sinyal protein dengan $T_2 = 20$ ms.

**Penyelesaian.** $\Delta\nu_{1/2} = 1/\pi T_2$: (a) 0,32 Hz; (b) 1,06 Hz; (c) 15,9 Hz.

**Memahami hasil.** Pada molekul kecil, lebar garis biasanya ditentukan oleh homogenitas magnet, bukan oleh relaksasi alami; itu sebabnya setiap sampel "di-*shim*", yaitu medan diratakan dengan kumparan koreksi. Pada protein, garis 16 Hz lebih lebar daripada banyak kopling $J$, sehingga multiplet menjadi kabur; ini salah satu alasan NMR protein memakai metode dua dan tiga dimensi.
:::

::: {.contoh}
**Contoh 16.40 · Relaksasi proton air menurut BPP**

Hitung $T_1$ dari interaksi dipol–dipol di dalam satu molekul air ($r = 1{,}52$ Å) dengan $\tau_c = 2{,}6$ ps pada 400 MHz. Bandingkan dengan $T_1$ air murni terukur, sekitar 3,6 s pada 25 °C.

**Penyelesaian.** $\omega_0\tau_c = 2\pi(4 \times 10^8)(2{,}6 \times 10^{-12}) = 0{,}0065 \ll 1$, sehingga kurung dalam (16.41) praktis $5\tau_c$:

$$
\frac1{T_1} = \frac32\left(\frac{\mu_0}{4\pi}\right)^2\frac{\gamma^4\hbar^2\tau_c}{r^6} = 0{,}18\ \text{s}^{-1}, \qquad T_1 = 5{,}6\ \text{s} .
$$

**Memahami hasil.** Interaksi di dalam molekul menerangkan sekitar dua pertiga laju relaksasi air; sisanya berasal dari proton molekul tetangga (relaksasi antarmolekul). Kesesuaian orde ini adalah salah satu keberhasilan awal teori BPP. Oksigen terlarut, yang paramagnetik, juga memperpendek $T_1$ secara nyata; untuk pengukuran yang teliti, sampel harus dihilangkan gasnya.
:::

::: {.contoh}
**Contoh 16.41 · Molekul kecil dan protein**

Menurut model Stokes–Einstein–Debye, $\tau_c = 4\pi\eta a^3/3k_BT$ untuk bola berjari-jari $a$ dalam pelarut berviskositas $\eta$. Hitung $\tau_c$ dan $\omega_0\tau_c$ pada 600 MHz untuk molekul kecil ($a = 0{,}3$ nm) dan protein globular ($a = 2{,}0$ nm) dalam air ($\eta = 0{,}89$ mPa s, 298 K).

**Penyelesaian.** Molekul kecil: $\tau_c = 4\pi(0{,}89 \times 10^{-3})(0{,}3 \times 10^{-9})^3/3(1{,}381 \times 10^{-23})(298) = 24$ ps, $\omega_0\tau_c = 0{,}09$. Protein: $\tau_c = 7{,}2$ ns, $\omega_0\tau_c = 27$.

**Memahami hasil.** Molekul kecil berada dalam rezim penyempitan ekstrem; protein jauh di rezim gerak lambat, dengan $T_2$ pendek dan NOE antarproton yang bahkan bertanda negatif. Karena $\tau_c \propto a^3 \propto$ massa molekul, lebar garis tumbuh kira-kira lurus dengan ukuran protein. Teknik TROSY (Kurt Wüthrich dan rekan, 1997) memanfaatkan saling peniadaan dua mekanisme relaksasi untuk memperluas jangkauan NMR ke kompleks protein ratusan kilodalton.
:::

::: {.contoh}
**Contoh 16.42 · Overhauser untuk ¹³C dan ¹⁵N**

Hitung faktor peningkatan maksimum $1 + \eta_\text{maks}$ untuk sinyal ¹³C dan ¹⁵N bila proton dijenuhkan, dalam rezim penyempitan ekstrem.

**Penyelesaian.** ¹³C: $\eta = \gamma_\text{H}/2\gamma_\text{C} = 26{,}75/(2 \times 6{,}728) = 1{,}99$, faktor 2,99. ¹⁵N: $\eta = 26{,}75/(2 \times (-2{,}713)) = -4{,}93$, faktor $-3{,}93$.

**Memahami hasil.** Untuk ¹⁵N, yang $\gamma$-nya negatif, NOE membalik sinyal dan memperbesarnya hampir empat kali. Bila mekanisme relaksasi lain ikut bekerja, $\eta$ lebih kecil daripada nilai maksimum, dan untuk ¹⁵N sinyalnya dapat menjadi hampir nol ($1 + \eta \approx 0$): sinyal yang "hilang" secara misterius. Spektroskopis ¹⁵N karena itu sering mematikan penyinaran proton selama jeda (*inverse gated decoupling*).
:::

::: {.contoh}
**Contoh 16.43 · Sudut Ernst**

Perekaman diulang setiap $T_R = 1{,}0$ s untuk inti dengan $T_1 = 3{,}0$ s. Sudut balik yang memberi sinyal terbesar per perekaman dalam keadaan tunak adalah sudut Ernst, $\cos\theta_E = e^{-T_R/T_1}$. Hitung $\theta_E$.

**Penyelesaian.** $\cos\theta_E = e^{-1/3} = 0{,}717$, $\theta_E = 44°$.

**Memahami hasil.** Dengan pengulangan cepat, pulsa 90° justru boros: ia menghabiskan seluruh $M_z$, yang tidak sempat pulih. Sudut Ernst memberi kompromi terbaik antara besar sinyal tiap pulsa dan pemulihan antarpulsa. Prinsip yang sama dipakai dalam MRI cepat (pencitraan gradien-gema), dengan sudut balik 5°–30°.
:::

::: {.kuis}
**Kuis cepat 16.9**

Mengapa gema spin dapat menghapus pengaruh ketidakseragaman medan statis tetapi tidak dapat menghapus fluktuasi medan lokal yang acak? Bila viskositas pelarut dinaikkan, bagaimana $T_1$ molekul kecil berubah?
:::

## 16.10 Konsep NMR dua dimensi

### Dua sumbu waktu, dua sumbu frekuensi

Spektrum molekul besar dalam satu dimensi berisi ratusan garis yang saling bertumpuk. Gagasan NMR dua dimensi, yang dikemukakan Jean Jeener pada tahun 1971 dan diwujudkan oleh Ernst, adalah menyebar spektrum ke bidang dua frekuensi sehingga garis-garis yang bertumpuk terpisah, dan sekaligus menunjukkan **hubungan** antarinti. Setiap percobaan 2D mempunyai empat tahap:

1. **Persiapan**: pulsa yang menciptakan magnetisasi transversal.
2. **Evolusi** selama $t_1$: magnetisasi berpresesi dengan frekuensi inti asalnya.
3. **Pencampuran**: pulsa atau selang yang memindahkan magnetisasi antarinti yang berhubungan (melalui kopling $J$ atau relaksasi silang).
4. **Deteksi** selama $t_2$: FID direkam, dan magnetisasi berpresesi dengan frekuensi inti tujuannya.

Percobaan diulang untuk ratusan nilai $t_1$ yang bertambah teratur. Sinyal $s(t_1, t_2)$ ditransformasi Fourier terhadap kedua waktu, menghasilkan spektrum $S(F_1, F_2)$. Puncak di $(\nu_A, \nu_A)$, pada diagonal, berasal dari magnetisasi yang tidak berpindah. Puncak di $(\nu_A, \nu_X)$, **puncak silang**, berasal dari magnetisasi yang berevolusi dengan frekuensi A lalu dideteksi dengan frekuensi X. Puncak silang adalah bukti bahwa A dan X "berhubungan".

### Percobaan-percobaan utama

**COSY** (*correlation spectroscopy*) memakai urutan paling sederhana, 90° – $t_1$ – 90° – $t_2$. Pulsa kedua memindahkan magnetisasi antarproton yang berkopling $J$. Puncak silang menunjukkan proton yang terpisah dua atau tiga ikatan, sehingga COSY memetakan jaringan H–C–C–H dalam molekul.

**TOCSY** (*total correlation*) memakai pencampuran yang lebih panjang (penguncian spin) sehingga magnetisasi menyebar ke seluruh sistem spin yang saling berkopling, misalnya semua proton dalam satu residu asam amino atau satu cincin gula.

**HSQC** (*heteronuclear single-quantum coherence*) menghubungkan setiap proton dengan karbon (atau nitrogen) yang mengikatnya langsung melalui ¹J. Magnetisasi dimulai dari proton, dipindahkan ke ¹³C untuk berevolusi selama $t_1$, lalu dikembalikan ke proton untuk dideteksi. Karena dimulai dan dideteksi pada proton, kepekaannya jauh lebih besar daripada perekaman ¹³C langsung. **HMBC** melakukan hal serupa untuk kopling jarak jauh (²J dan ³J), sehingga menghubungkan proton dengan karbon kuaterner dan karbonil.

**NOESY** memakai relaksasi silang sebagai pencampuran: puncak silang muncul antara proton yang **berdekatan dalam ruang** (kurang dari sekitar 5 Å), tidak peduli seberapa jauh terpisah melalui ikatan. Intensitasnya sebanding dengan $r^{-6}$ (subbab 16.9).

Gabungan COSY/TOCSY (siapa bertetangga melalui ikatan), HSQC/HMBC (proton mana pada karbon mana), dan NOESY (siapa berdekatan dalam ruang) cukup untuk menentukan struktur lengkap bahan alam yang rumit. Untuk protein, NOESY memberi ribuan batas jarak antarproton, dan struktur tiga dimensinya dihitung sebagai susunan atom yang memenuhi semua batas itu. Metode ini membawa Kurt Wüthrich ke Hadiah Nobel Kimia 2002.

![Gambar 16.9 Spektrum COSY 1-propanol (simulasi skematis). Puncak diagonal (lingkaran pada garis miring) adalah spektrum 1D biasa. Puncak silang (di luar diagonal) menghubungkan CH₃ (0,94 ppm) dengan CH₂ tengah (1,57 ppm), dan CH₂ tengah dengan OCH₂ (3,58 ppm); tidak ada puncak silang antara CH₃ dan OCH₂ yang terpisah empat ikatan.](fig/c_cosy.png){width=70%}

::: {.dalam}
**Mengapa pulsa kedua memindahkan magnetisasi**

Untuk dua spin A dan X yang berkopling, keadaan sistem dapat diuraikan atas hasil kali operator spin. Pulsa 90° pertama (terhadap sumbu $x$) mengubah $\hat I_{zA}$ menjadi $-\hat I_{yA}$. Selama $t_1$, magnetisasi A berpresesi dengan frekuensi $\Omega_A$ dan sekaligus berevolusi di bawah kopling. Evolusi kopling mengubah sebagian $\hat I_{yA}$ menjadi **magnetisasi antifase** $2\hat I_{xA}\hat I_{zX}$ dengan faktor $\sin(\pi Jt_1)$, dan presesi geseran kimia mencampur komponen $x$ dan $y$ dengan faktor $\cos\Omega_At_1$ dan $\sin\Omega_At_1$. Jadi pada akhir $t_1$ terdapat suku seperti $2\hat I_{yA}\hat I_{zX}\sin(\pi Jt_1)\sin(\Omega_At_1)$: tidak dapat diukur langsung, tetapi "mengingat" frekuensi A. Pulsa 90° kedua mengubah $\hat I_{yA} \to \hat I_{zA}$ dan $\hat I_{zX} \to -\hat I_{yX}$, sehingga suku itu menjadi $-2\hat I_{zA}\hat I_{yX}$: magnetisasi antifase spin X yang dapat diukur. Selama $t_2$ ia berpresesi dengan frekuensi X, sedangkan amplitudonya dimodulasi oleh $\Omega_A$ selama $t_1$: puncak silang di $(\nu_A, \nu_X)$. Jadi kopling $J$ adalah "jembatan" perpindahan, dan tanpa kopling tidak ada puncak silang. Bahasa hasil kali operator ini, yang dikembangkan oleh Sørensen, Ernst, dan rekan (1983), adalah alat kerja perancang urutan pulsa.
:::

::: {.contoh}
**Contoh 16.44 · Penggaris NOE**

Dalam spektrum NOESY suatu peptida, puncak silang antara dua proton geminal suatu gugus CH₂ (jarak tetap 1,78 Å) mempunyai volume 100, dan puncak silang antara dua proton pada residu berbeda bervolume 5. Taksir jarak kedua proton itu, dengan menganggap gerak molekul sama untuk kedua pasangan.

**Penyelesaian.** Karena volume $\propto r^{-6}$: $r = 1{,}78\,(100/5)^{1/6} = 1{,}78 \times 1{,}648 = 2{,}93$ Å.

**Memahami hasil.** Ketergantungan $r^{-6}$ membuat penggaris NOE "lunak": galat 50% pada volume hanya menimbulkan galat sekitar 7% pada jarak. Dalam praktik, NOE dikelompokkan menjadi kuat (< 2,8 Å), sedang (< 3,5 Å), dan lemah (< 5 Å), dan struktur dihitung dengan batas-batas atas ini. Puncak berjarak 2,9 Å antarresidu yang jauh dalam urutan adalah petunjuk lipatan protein.
:::

::: {.contoh}
**Contoh 16.45 · Biaya waktu dimensi kedua**

Spektrum COSY direkam dengan 256 nilai $t_1$, masing-masing 8 perekaman, dan setiap perekaman (termasuk jeda) memakan 2,0 s. Hitung lama percobaan. Bila jendela spektrum $F_1$ selebar 4800 Hz, berapa resolusi digital pada $F_1$?

**Penyelesaian.** $256 \times 8 \times 2{,}0 = 4096$ s $\approx 68$ menit. Resolusi $F_1$: $4800/256 = 18{,}8$ Hz per titik.

**Memahami hasil.** Dimensi tidak langsung $F_1$ jauh lebih kasar daripada $F_2$, karena setiap titik $t_1$ memerlukan satu percobaan utuh. Kopling kecil tidak terurai di $F_1$, dan resolusi yang lebih baik berarti waktu yang lebih panjang. Teknik modern seperti pencuplikan tak seragam (*non-uniform sampling*) merekam hanya sebagian nilai $t_1$ dan merekonstruksi sisanya secara matematis, menghemat waktu beberapa kali.
:::

::: {.contoh}
**Contoh 16.46 · Membaca COSY**

Spektrum ¹H 1-propanol, CH₃CH₂CH₂OH, menunjukkan sinyal di 0,94 (t, 3H), 1,57 (sekstet, 2H), 3,58 (t, 2H), dan sinyal OH yang lebar. Ramalkan puncak silang COSY. Mengapa tidak ada puncak silang 0,94–3,58?

**Penyelesaian.** Puncak silang di (0,94; 1,57) dan (1,57; 3,58), masing-masing muncul berpasangan simetris terhadap diagonal. Proton CH₃ dan OCH₂ terpisah empat ikatan (H–C–C–C–H), dengan ⁴J hampir nol, sehingga tidak ada pemindahan magnetisasi.

**Memahami hasil.** Mengikuti puncak silang dari satu sinyal ke sinyal berikutnya ("berjalan" sepanjang rantai) adalah cara membaca COSY: CH₃ → CH₂ → CH₂O. Untuk molekul yang lebih besar, setiap jalur semacam itu mengidentifikasi satu fragmen yang terhubung, dan HMBC kemudian menyambungkan fragmen-fragmen melalui atom tanpa proton.
:::

::: {.contoh}
**Contoh 16.47 · Keuntungan deteksi proton**

Dalam HSQC, polarisasi dimulai pada proton (faktor $\gamma_\text{H}/\gamma_X$ dibandingkan polarisasi X) dan sinyal dideteksi pada proton (faktor $(\gamma_\text{H}/\gamma_X)^{3/2}$ dari (16.16)). Hitung keuntungan total dibandingkan deteksi langsung X tanpa NOE, untuk X = ¹³C dan ¹⁵N.

**Penyelesaian.** Keuntungan $(\gamma_\text{H}/|\gamma_X|)^{5/2}$: ¹³C: $3{,}98^{5/2} = 32$; ¹⁵N: $9{,}86^{5/2} = 305$.

**Memahami hasil.** Untuk ¹⁵N keuntungannya tiga ratus kali, setara dengan percepatan sekitar sembilan puluh ribu kali dalam waktu. Inilah sebabnya spektrum ¹H–¹⁵N HSQC, yang memberi satu puncak untuk setiap ikatan N–H rantai utama protein, menjadi "sidik jari" baku dalam biologi struktur, sedangkan spektrum ¹⁵N langsung hampir tidak pernah direkam untuk protein.
:::

::: {.kuis}
**Kuis cepat 16.10**

Dalam spektrum HSQC, mengapa karbon kuaterner tidak memberi puncak? Puncak silang NOESY menunjukkan kedekatan dalam ruang; apa yang ditunjukkan puncak silang COSY?
:::
