# Bab 6 · Aljabar Dasar: Kotak Kosong, Urutan Hitung, dan Pola

Aljabar terdengar sulit, padahal kamu sudah memakainya sejak kelas 1: *"3 + □ = 8, kotaknya diisi berapa?"* Kotak kosong itu adalah **bilangan yang belum diketahui**. Di SMP nanti kotak diganti huruf, misalnya *n* + 3 = 8. Isinya sama saja.

## Mengisi kotak kosong dengan operasi kebalikan

Bayangkan kalimat matematika seperti **timbangan yang seimbang**. Untuk menemukan isi kotak, kita "membuka" operasi yang menempel pada kotak dengan **operasi kebalikannya**:

| Yang menempel pada kotak | Dibuka dengan |
|:-:|:-:|
| + (tambah) | − (kurang) |
| − (kurang) | + (tambah) |
| × (kali) | : (bagi) |
| : (bagi) | × (kali) |

::: contoh
**Contoh 1.**

- □ + 27 = 50 → □ = 50 − 27 = **23**. Cek: 23 + 27 = 50 ✓
- □ − 15 = 40 → □ = 40 + 15 = **55**. Cek: 55 − 15 = 40 ✓
- 6 × □ = 42 → □ = 42 : 6 = **7**. Cek: 6 × 7 = 42 ✓
- □ : 4 = 9 → □ = 9 × 4 = **36**. Cek: 36 : 4 = 9 ✓
:::

::: awas
**Hati-hati!** Pada **40 − □ = 15** kotaknya ada di belakang tanda kurang. Pikirkan: *"40 dikurangi berapa supaya tinggal 15?"* Jawabannya □ = 40 − 15 = **25**, bukan 55. Begitu juga **36 : □ = 4** → □ = 36 : 4 = 9. Selalu **cek** dengan memasukkan jawabanmu ke soal.
:::

## Kotak dengan dua langkah

Kalau kotak terkena dua operasi, buka dari **yang paling luar** (yang terakhir dikerjakan), seperti membuka kado: bungkus luar dulu, baru kotak di dalamnya.

::: contoh
**Contoh 2.** 3 × □ + 5 = 26.

Kotak dikali 3 dulu, lalu ditambah 5. Buka yang terakhir dulu:

1. Buang "+ 5": 3 × □ = 26 − 5 = 21.
2. Buang "3 ×": □ = 21 : 3 = **7**.

Cek: 3 × 7 + 5 = 21 + 5 = 26 ✓
:::

## Urutan hitung (operasi campuran)

Berapa 2 + 3 × 4? Kalau dikerjakan dari kiri: 5 × 4 = 20. Kalau perkalian dulu: 2 + 12 = 14. Supaya semua orang mendapat jawaban yang sama, ada aturan urutan:

::: ingat
**Ingat!** Urutan mengerjakan:

1. Yang di dalam **kurung ( )** dulu.
2. Lalu **kali dan bagi**, dari kiri ke kanan.
3. Terakhir **tambah dan kurang**, dari kiri ke kanan.

Jadi 2 + 3 × 4 = 2 + 12 = **14**, sedangkan (2 + 3) × 4 = 5 × 4 = **20**.
:::

::: contoh
**Contoh 3.** Hitung 48 : 6 + 5 × (9 − 7).

Kurung: 9 − 7 = 2 → 48 : 6 + 5 × 2. Kali dan bagi: 48 : 6 = 8 dan 5 × 2 = 10 → 8 + 10. Tambah: **18**.
:::

::: awas
**Hati-hati!** Kali dan bagi **setara**, begitu juga tambah dan kurang. Yang setara dikerjakan dari kiri ke kanan. 20 − 5 + 3 = 15 + 3 = **18**, bukan 20 − 8 = 12.
:::

## Mengubah soal cerita menjadi kalimat matematika

Inilah kegunaan aljabar sebenarnya. Kata-kata diubah menjadi kalimat dengan kotak, lalu diselesaikan.

::: contoh
**Contoh 4.** Dina punya beberapa kelereng. Ia diberi 12 kelereng oleh kakaknya, sehingga kelerengnya menjadi 30. Berapa kelereng Dina mula-mula?

Kalimat matematika: □ + 12 = 30. Maka □ = 30 − 12 = **18** kelereng.
:::

## Pola bilangan

Pola adalah aturan yang **berulang**. Untuk melanjutkan pola, cari aturannya dengan melihat **selisih** dua bilangan yang berdekatan.

::: contoh
**Contoh 5.**

- 3, 7, 11, 15, … selisihnya selalu **+ 4**. Berikutnya **19, 23**.
- 2, 6, 18, 54, … setiap bilangan **× 3**. Berikutnya **162**.
- 1, 4, 9, 16, 25, … ini 1 × 1, 2 × 2, 3 × 3, 4 × 4, 5 × 5 (**bilangan persegi**). Berikutnya 6 × 6 = **36**.
:::

<div class="gbr"><svg width="420" height="95" viewBox="0 0 420 95" font-family="Inter,sans-serif">
<g fill="#1f7fc4"><rect x="20" y="40" width="14" height="14" rx="2"/>
<rect x="80" y="26" width="14" height="14" rx="2"/><rect x="96" y="26" width="14" height="14" rx="2"/><rect x="80" y="42" width="14" height="14" rx="2"/><rect x="96" y="42" width="14" height="14" rx="2"/>
<rect x="160" y="14" width="14" height="14" rx="2"/><rect x="176" y="14" width="14" height="14" rx="2"/><rect x="192" y="14" width="14" height="14" rx="2"/><rect x="160" y="30" width="14" height="14" rx="2"/><rect x="176" y="30" width="14" height="14" rx="2"/><rect x="192" y="30" width="14" height="14" rx="2"/><rect x="160" y="46" width="14" height="14" rx="2"/><rect x="176" y="46" width="14" height="14" rx="2"/><rect x="192" y="46" width="14" height="14" rx="2"/></g>
<g fill="#e07b22"><rect x="260" y="2" width="14" height="14" rx="2"/><rect x="276" y="2" width="14" height="14" rx="2"/><rect x="292" y="2" width="14" height="14" rx="2"/><rect x="308" y="2" width="14" height="14" rx="2"/><rect x="260" y="18" width="14" height="14" rx="2"/><rect x="276" y="18" width="14" height="14" rx="2"/><rect x="292" y="18" width="14" height="14" rx="2"/><rect x="308" y="18" width="14" height="14" rx="2"/><rect x="260" y="34" width="14" height="14" rx="2"/><rect x="276" y="34" width="14" height="14" rx="2"/><rect x="292" y="34" width="14" height="14" rx="2"/><rect x="308" y="34" width="14" height="14" rx="2"/><rect x="260" y="50" width="14" height="14" rx="2"/><rect x="276" y="50" width="14" height="14" rx="2"/><rect x="292" y="50" width="14" height="14" rx="2"/><rect x="308" y="50" width="14" height="14" rx="2"/></g>
<g font-size="13" font-weight="700" fill="#12406a" text-anchor="middle"><text x="27" y="85">1</text><text x="95" y="85">4</text><text x="183" y="85">9</text><text x="291" y="85">16</text><text x="380" y="50">…</text></g>
</svg><div class="ket">Bilangan persegi: banyak kotak pada persegi yang sisinya 1, 2, 3, 4, …</div></div>

::: latihan
**Latihan Bab 6** · [lihat kunci jawaban →](#kunci6)

1. □ + 38 = 75
2. □ − 24 = 56
3. 8 × □ = 72
4. 90 − □ = 35
5. 4 × □ − 6 = 30
6. 36 − 4 × 5 + 2 = …
7. (36 − 4) × (5 + 2) = …
8. Lanjutkan pola: 5, 11, 17, 23, …, … dan 3, 6, 12, 24, …, …
:::
