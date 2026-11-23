# Bab 9 · Dasar Logika

**Logika** adalah cara berpikir yang rapi: dari hal yang sudah pasti benar, kita menarik kesimpulan yang **pasti** benar juga, bukan sekadar menebak. Semua bab sebelumnya sebenarnya memakai logika. Bab ini melatih logikanya secara langsung.

## Pernyataan: benar atau salah

**Pernyataan** adalah kalimat yang bisa ditentukan **benar** atau **salah**.

- "7 × 8 = 56" → pernyataan **benar**.
- "Persegi punya 5 sisi" → pernyataan **salah**.
- "Tutup pintunya!" → **bukan** pernyataan (perintah, tidak bisa benar atau salah).
- "□ + 3 = 10" → belum bisa ditentukan sebelum kotaknya diisi. Kalimat seperti ini disebut **kalimat terbuka** (Bab 8). Kalau □ = 7, kalimatnya menjadi benar.

## Kata "tidak", "dan", "atau"

::: ingat
**Ingat!**

- **tidak** membalik nilai: "6 bilangan ganjil" salah, maka "6 **tidak** bilangan ganjil" benar.
- **dan** benar hanya kalau **kedua** bagian benar. "8 genap **dan** 8 lebih dari 5" → benar (keduanya benar). "8 genap **dan** 8 lebih dari 10" → salah.
- **atau** benar kalau **paling sedikit satu** bagian benar. "8 genap **atau** 8 lebih dari 10" → benar.
:::

## Semua, beberapa, tidak ada

<div class="gbr"><svg width="420" height="150" viewBox="0 0 420 150" font-family="Inter,sans-serif" font-size="12" font-weight="700">
<rect x="5" y="5" width="410" height="140" rx="8" fill="#f7fbff" stroke="#9fb3c8"/>
<ellipse cx="150" cy="78" rx="130" ry="60" fill="#cfe6fb" stroke="#1f7fc4" stroke-width="2"/>
<ellipse cx="110" cy="85" rx="55" ry="32" fill="#ffe1c2" stroke="#e07b22" stroke-width="2"/>
<circle cx="345" cy="78" r="42" fill="#d6f2e6" stroke="#1a8a6a" stroke-width="2"/>
<g fill="#12406a" text-anchor="middle"><text x="150" y="44">hewan berkaki empat</text><text x="110" y="90">kucing</text><text x="345" y="83">ikan</text></g>
</svg><div class="ket">Lingkaran di dalam lingkaran: semua kucing berkaki empat. Lingkaran terpisah: tidak ada ikan yang berkaki empat.</div></div>

- **Semua** kucing berkaki empat. Lingkaran "kucing" seluruhnya ada **di dalam** lingkaran "berkaki empat".
- Tetapi **tidak** benar bahwa semua hewan berkaki empat adalah kucing. Ada bagian biru di luar lingkaran kucing (anjing, kambing).
- **Beberapa** hewan berkaki empat adalah kucing.
- **Tidak ada** ikan yang berkaki empat. Lingkarannya terpisah.

::: awas
**Hati-hati!** "Semua A adalah B" **tidak** sama dengan "semua B adalah A". Semua persegi adalah persegi panjang, tetapi tidak semua persegi panjang adalah persegi (Bab 10).
:::

## Jika … maka …

"**Jika** hari hujan, **maka** jalan basah." Kalimat ini dianggap benar. Apa yang bisa kita simpulkan?

| Yang diketahui | Kesimpulan | Pasti? |
|---|---|:-:|
| Hari hujan. | Jalan basah. | ✓ pasti |
| Jalan **tidak** basah. | Hari **tidak** hujan. | ✓ pasti |
| Jalan basah. | Hari hujan? | ✗ belum tentu (mungkin disiram) |
| Hari tidak hujan. | Jalan tidak basah? | ✗ belum tentu |

::: ingat
**Ingat!** Dari "jika P maka Q": kalau P terjadi, Q **pasti** terjadi. Kalau Q **tidak** terjadi, P **pasti tidak** terjadi. Kebalikannya (Q terjadi, jadi P?) **belum tentu**.
:::

::: contoh
**Contoh 1.** "Jika sebuah bilangan berakhiran 0, maka bilangan itu habis dibagi 10." Bilangan 470 berakhiran 0. Kesimpulannya?

Bagian "jika" terjadi, jadi bagian "maka" pasti terjadi: **470 habis dibagi 10**. Cek: 470 : 10 = 47 ✓.
:::

## Contoh penyangkal

Untuk membuktikan pernyataan "semua …" **salah**, cukup satu contoh yang tidak cocok. Contoh itu disebut **contoh penyangkal**.

::: contoh
**Contoh 2.** Dodi berkata: "Semua bilangan ganjil adalah bilangan prima." Benarkah?

Coba 9. Sembilan ganjil, tetapi 9 = 3 × 3, jadi bukan prima. Satu contoh ini sudah cukup: pernyataan Dodi **salah**.
:::

::: tips
**Satu contoh tidak cukup untuk membuktikan benar.** 3, 5, dan 7 memang ganjil dan prima, tetapi itu belum membuktikan "semua". Satu contoh penyangkal sudah cukup untuk membuktikan salah.
:::

## Penalaran urutan

::: contoh
**Contoh 3.** Andi lebih tinggi daripada Budi. Citra lebih pendek daripada Budi. Dewi lebih tinggi daripada Andi. Urutkan dari yang paling tinggi.

Tulis satu per satu di garis. Andi di atas Budi. Citra di bawah Budi. Dewi di atas Andi. Urutannya: **Dewi, Andi, Budi, Citra**.
:::

## Teka-teki dengan tabel

Kalau ada beberapa orang dan beberapa pilihan, buat **tabel**. Beri tanda ✗ untuk yang tidak mungkin, sampai tersisa satu ✓ di setiap baris.

::: contoh
**Contoh 4.** Ani, Bima, dan Caca masing-masing memelihara satu hewan: kucing, ikan, atau burung (tidak ada yang sama).

- Ani tidak memelihara hewan yang bisa terbang.
- Bima alergi bulu, jadi tidak memelihara kucing atau burung.

Siapa memelihara apa?

| | Kucing | Ikan | Burung |
|:-:|:-:|:-:|:-:|
| Ani | **✓** | ✗ | ✗ |
| Bima | ✗ | **✓** | ✗ |
| Caca | ✗ | ✗ | **✓** |

Petunjuk 2: Bima pasti **ikan** (hanya itu yang tersisa baginya). Ikan sudah diambil, dan Ani tidak memelihara burung (petunjuk 1), jadi Ani **kucing**. Yang tersisa, Caca **burung**.
:::

## Logika ganjil dan genap

Kita bisa menebak hasil tanpa menghitung:

| Operasi | Hasil |
|:-:|:-:|
| genap + genap | genap |
| ganjil + ganjil | genap |
| genap + ganjil | ganjil |
| ganjil × ganjil | ganjil |
| genap × apa saja | genap |

Alasannya: bilangan ganjil adalah "pasangan-pasangan ditambah satu yang sendirian". Dua bilangan ganjil berarti ada dua yang sendirian, dan keduanya menjadi satu pasangan baru, sehingga hasilnya genap.

::: latihan
**Latihan Bab 9** · [lihat kunci jawaban →](#kunci9)

1. Mana yang pernyataan? (a) 15 : 3 = 5 (b) Kerjakan PR-mu! (c) Segitiga punya 4 sudut. Untuk yang pernyataan, tentukan benar atau salah.
2. Benar atau salah: "12 genap **dan** 12 habis dibagi 5"?
3. Benar atau salah: "12 genap **atau** 12 habis dibagi 5"?
4. "Semua siswa kelas 5 memakai seragam." Rudi memakai seragam. Apakah Rudi pasti siswa kelas 5?
5. "Jika lampu menyala, maka ada listrik." Ternyata tidak ada listrik. Apa kesimpulannya?
6. Beri contoh penyangkal untuk: "Semua bilangan yang habis dibagi 2 juga habis dibagi 4."
7. Tanpa menghitung, apakah 137 + 259 ganjil atau genap? Jelaskan.
8. Eka lebih tua daripada Fani. Gita lebih tua daripada Eka. Hana lebih muda daripada Fani. Siapa yang paling tua dan siapa yang paling muda?
:::
