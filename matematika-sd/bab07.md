# Bab 7 · Pola Bilangan

Matematika sering disebut *ilmu tentang pola*. **Pola** adalah aturan yang terus berulang. Kalau kamu menemukan aturannya, kamu bisa menebak apa yang datang berikutnya, bahkan yang ke-100, tanpa menulis semuanya. Inilah latihan logika yang paling dasar: **mengamati, menemukan aturan, lalu menguji aturan itu.**

## Langkah menemukan pola

::: tips
**Tiga langkah.**

1. **Amati** beberapa suku pertama.
2. **Cari aturannya.** Hitung selisih dua bilangan berdekatan. Kalau selisihnya tidak tetap, coba perbandingannya (dikali berapa?).
3. **Uji** aturan itu pada semua suku yang ada. Aturan yang benar harus cocok untuk semuanya, bukan cuma dua suku pertama.
:::

## Pola tambah dan pola kurang

::: contoh
**Contoh 1.**

- 4, 7, 10, 13, … selisihnya selalu **+3**. Berikutnya **16, 19**.
- 50, 44, 38, 32, … selisihnya **−6**. Berikutnya **26, 20**.
:::

## Pola kali dan pola bagi

::: contoh
**Contoh 2.**

- 3, 6, 12, 24, … selisihnya 3, 6, 12 (tidak tetap). Cek perbandingannya: setiap suku **×2**. Berikutnya **48, 96**.
- 800, 400, 200, 100, … setiap suku **:2**. Berikutnya **50, 25**.
:::

## Pola yang selisihnya ikut berpola

Kadang selisihnya sendiri yang berpola.

::: contoh
**Contoh 3.** 2, 3, 5, 8, 12, …

Selisihnya +1, +2, +3, +4, jadi selisih berikutnya +5. Suku berikutnya 12 + 5 = **17**, lalu 17 + 6 = **23**.
:::

## Bilangan istimewa yang berpola

<div class="gbr"><svg width="560" height="120" viewBox="0 0 560 120" font-family="Inter,sans-serif" font-size="12" font-weight="700">
<g fill="#e07b22"><circle cx="30" cy="80" r="7"/>
<circle cx="80" cy="80" r="7"/><circle cx="96" cy="80" r="7"/><circle cx="88" cy="66" r="7"/>
<circle cx="140" cy="80" r="7"/><circle cx="156" cy="80" r="7"/><circle cx="172" cy="80" r="7"/><circle cx="148" cy="66" r="7"/><circle cx="164" cy="66" r="7"/><circle cx="156" cy="52" r="7"/>
<circle cx="215" cy="80" r="7"/><circle cx="231" cy="80" r="7"/><circle cx="247" cy="80" r="7"/><circle cx="263" cy="80" r="7"/><circle cx="223" cy="66" r="7"/><circle cx="239" cy="66" r="7"/><circle cx="255" cy="66" r="7"/><circle cx="231" cy="52" r="7"/><circle cx="247" cy="52" r="7"/><circle cx="239" cy="38" r="7"/></g>
<g fill="#12406a" text-anchor="middle"><text x="30" y="108">1</text><text x="88" y="108">3</text><text x="156" y="108">6</text><text x="239" y="108">10</text><text x="290" y="84">…</text></g>
<text x="150" y="18" text-anchor="middle" fill="#b5541c">bilangan segitiga</text>
<g fill="#1f7fc4"><rect x="340" y="74" width="12" height="12" rx="2"/>
<rect x="380" y="60" width="12" height="12" rx="2"/><rect x="394" y="60" width="12" height="12" rx="2"/><rect x="380" y="74" width="12" height="12" rx="2"/><rect x="394" y="74" width="12" height="12" rx="2"/>
<rect x="434" y="46" width="12" height="12" rx="2"/><rect x="448" y="46" width="12" height="12" rx="2"/><rect x="462" y="46" width="12" height="12" rx="2"/><rect x="434" y="60" width="12" height="12" rx="2"/><rect x="448" y="60" width="12" height="12" rx="2"/><rect x="462" y="60" width="12" height="12" rx="2"/><rect x="434" y="74" width="12" height="12" rx="2"/><rect x="448" y="74" width="12" height="12" rx="2"/><rect x="462" y="74" width="12" height="12" rx="2"/></g>
<g fill="#12406a" text-anchor="middle"><text x="346" y="108">1</text><text x="393" y="108">4</text><text x="454" y="108">9</text><text x="505" y="84">…</text></g>
<text x="420" y="18" text-anchor="middle" fill="#1f7fc4">bilangan persegi</text>
</svg></div>

| Nama | Pola | Aturan |
|---|---|---|
| Bilangan genap | 2, 4, 6, 8, 10, … | +2; bisa dibagi 2 |
| Bilangan ganjil | 1, 3, 5, 7, 9, … | +2; dibagi 2 bersisa 1 |
| Bilangan persegi | 1, 4, 9, 16, 25, … | 1×1, 2×2, 3×3, 4×4, … |
| Bilangan segitiga | 1, 3, 6, 10, 15, … | +2, +3, +4, +5, … |
| Fibonacci | 1, 1, 2, 3, 5, 8, 13, … | setiap suku = jumlah dua suku sebelumnya |

::: tips
**Fakta menarik.** Jumlah bilangan ganjil berurutan dari 1 selalu bilangan persegi: 1 + 3 = 4, 1 + 3 + 5 = 9, 1 + 3 + 5 + 7 = 16. Coba lihat gambar bilangan persegi: setiap persegi baru dibuat dengan menambah satu "siku" berisi 3, lalu 5, lalu 7 kotak.
:::

## Mencari suku jauh tanpa menulis semuanya

Pola tambah 4, 7, 10, 13, … (beda 3). Berapa suku ke-20? Kita tidak perlu menulis 20 bilangan. Dari suku ke-1 ke suku ke-20 ada **19 langkah**, setiap langkah +3:

$$\text{suku ke-20} = 4 + 19 \times 3 = 4 + 57 = 61$$

::: ingat
**Ingat!** Untuk pola tambah: **suku ke-n = suku pertama + (n − 1) × beda.** Kurangi 1 karena suku pertama belum melangkah.
:::

## Pola berulang dan sisa pembagian

Manik-manik disusun berulang: **merah, kuning, biru, merah, kuning, biru, …** Warna manik ke-50 apa?

Polanya berulang setiap **3** manik. Bagi 50 dengan 3: 50 : 3 = 16 sisa **2** (Bab 4). Artinya 16 putaran penuh, lalu maju 2 lagi: merah (1), kuning (2). Jadi manik ke-50 berwarna **kuning**.

<div class="gbr"><svg width="360" height="40" viewBox="0 0 360 40"><g stroke="#12406a" stroke-width="1.5"><circle cx="20" cy="20" r="13" fill="#e74c3c"/><circle cx="55" cy="20" r="13" fill="#f4c430"/><circle cx="90" cy="20" r="13" fill="#1f7fc4"/><circle cx="125" cy="20" r="13" fill="#e74c3c"/><circle cx="160" cy="20" r="13" fill="#f4c430"/><circle cx="195" cy="20" r="13" fill="#1f7fc4"/><circle cx="230" cy="20" r="13" fill="#e74c3c"/><circle cx="265" cy="20" r="13" fill="#f4c430"/><circle cx="300" cy="20" r="13" fill="#1f7fc4"/></g><text x="335" y="26" font-family="Inter,sans-serif" font-size="16" font-weight="700" fill="#12406a">…</text></svg></div>

::: awas
**Hati-hati!** Kalau sisanya **0**, berarti tepat di akhir putaran, yaitu warna **terakhir** (biru), bukan warna pertama. Manik ke-30: 30 : 3 = 10 sisa 0 → biru.
:::

::: latihan
**Latihan Bab 7** · [lihat kunci jawaban →](#kunci7)

1. Lanjutkan dua suku: 6, 11, 16, 21, …
2. Lanjutkan dua suku: 90, 81, 72, 63, …
3. Lanjutkan dua suku: 2, 6, 18, 54, …
4. Lanjutkan dua suku: 1, 2, 4, 7, 11, …
5. Lanjutkan dua suku Fibonacci: 1, 1, 2, 3, 5, 8, 13, …
6. Berapa suku ke-15 dari pola 5, 9, 13, 17, …?
7. Bendera disusun berulang: merah, putih, hijau, kuning. Bendera ke-38 berwarna apa?
8. Berapa 1 + 3 + 5 + 7 + 9 + 11? (Petunjuk: lihat fakta menarik.)
:::
