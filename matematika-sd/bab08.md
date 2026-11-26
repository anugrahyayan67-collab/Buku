# Bab 8 · Aljabar Dasar: Kotak Kosong dan Urutan Hitung

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

::: contoh
**Contoh 5 (model batang).** Harga sebuah buku 2 kali harga sebuah pensil. Harga keduanya Rp9.000. Berapa harga pensil?

Gambar harga pensil sebagai **satu batang** □. Harga buku = **dua batang** yang sama.

<div class="gbr"><svg width="380" height="80" viewBox="0 0 380 80" font-family="Inter,sans-serif" font-size="12" font-weight="700">
<text x="0" y="24" fill="#12406a">pensil</text><rect x="60" y="8" width="80" height="24" rx="3" fill="#cfe6fb" stroke="#1f7fc4" stroke-width="2"/><text x="100" y="25" text-anchor="middle" fill="#12406a">□</text>
<text x="0" y="60" fill="#12406a">buku</text><rect x="60" y="44" width="80" height="24" rx="3" fill="#cfe6fb" stroke="#1f7fc4" stroke-width="2"/><rect x="140" y="44" width="80" height="24" rx="3" fill="#cfe6fb" stroke="#1f7fc4" stroke-width="2"/><text x="100" y="61" text-anchor="middle" fill="#12406a">□</text><text x="180" y="61" text-anchor="middle" fill="#12406a">□</text>
<path d="M232 8 L240 8 L240 68 L232 68" fill="none" stroke="#e07b22" stroke-width="2"/><text x="250" y="43" fill="#b5541c">jumlah Rp9.000</text>
</svg></div>

Semuanya ada **3 batang** yang sama, jadi 3 × □ = 9.000 dan □ = 9.000 : 3 = **Rp3.000**. Harga buku 2 × 3.000 = Rp6.000. Cek: 3.000 + 6.000 = 9.000 ✓.
:::

::: ingat
**Ingat!** □ + □ + □ boleh ditulis 3 × □, dan □ + 2 × □ = 3 × □. Kotak yang sama boleh **dikumpulkan** seperti menghitung batang.
:::

::: latihan
**Latihan Bab 8** · [lihat kunci jawaban →](#kunci8)

1. □ + 38 = 75
2. □ − 24 = 56
3. 8 × □ = 72
4. 90 − □ = 35
5. 4 × □ − 6 = 30
6. 36 − 4 × 5 + 2 = …
7. (36 − 4) × (5 + 2) = …
8. Umur ayah 3 kali umur Rina. Jumlah umur mereka 48 tahun. Berapa umur Rina? (Petunjuk: Rina = □, ayah = 3 × □.)
:::
