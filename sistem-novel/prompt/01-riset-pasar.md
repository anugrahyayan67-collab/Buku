# 01 · Riset pasar: tiru pola, bukan isi

Pakai AI yang bisa mencari di web (Claude dengan pencarian web, atau Claude Code). Ganti bagian dalam `< >`.

```
Saya ingin menulis novel bergenre <genre, mis. romansa CEO / balas dendam istri / horor kampung / fantasi sistem> untuk aplikasi <nama aplikasi, mis. Fizzo / GoodNovel / KBM App / NovelToon / Wattpad>, pembaca Indonesia.

Langkah 1. Cari 5–10 judul yang sedang atau pernah sangat ramai di genre ini di aplikasi tersebut atau aplikasi sejenis (lihat peringkat, jumlah pembaca, ulasan, dan pembahasan di media sosial). Untuk setiap judul, catat yang bisa kamu pastikan: judul, aplikasi, perkiraan jumlah pembaca/bab, dan blurb. Tandai mana yang benar-benar kamu temukan sumbernya dan mana yang hanya dugaan. Jangan mengarang judul.

Langkah 2. Ekstrak POLA, bukan isi. Untuk setiap judul:
- Premis dalam satu kalimat (abstrak, tanpa nama).
- Trope utama (mis. nikah kontrak, identitas tersembunyi, kembali ke masa lalu, penghinaan lalu bangkit).
- Kail bab 1: apa yang terjadi di 300 kata pertama yang membuat orang lanjut.
- Kapan konflik besar pertama meledak (bab ke berapa kira-kira).
- Tipe tokoh utama dan lawan (luka masa lalu, keinginan, kekuatan tersembunyi).
- Siklus kepuasan pembaca: seberapa sering tokoh utama "menang" atau lawan "kena batunya".
- Jenis cliffhanger yang dominan.
- Panjang bab dan frekuensi update.
- Keluhan pembaca di ulasan (apa yang membuat mereka berhenti).

Langkah 3. Rangkum menjadi:
A. 7–10 pola yang muncul berulang (yang disukai pembaca).
B. 5 hal yang dikeluhkan pembaca (yang harus dihindari).
C. 3 celah: hal yang pembaca inginkan tetapi jarang diberikan judul-judul itu.
D. Tabel ritme: bab 1–3, 4–10, 11–30, 31+ — apa yang biasanya terjadi di setiap fase.

Aturan: jangan menyalin nama tokoh, adegan spesifik, atau kalimat dari novel mana pun. Yang kita ambil hanya struktur dan trope.
```

Simpan hasilnya di `riset/<genre>-<tanggal>.md`. Hasil riset ini dipakai di prompt 02 dan 04.

## Bekal awal (pola umum genre yang sering ramai di aplikasi novel Indonesia)

Ini titik awal saja; tetap jalankan riset di atas, karena selera pembaca bergerak.

| Genre | Kail khas | Siklus kepuasan |
|---|---|---|
| Romansa CEO / nikah kontrak | Pernikahan terpaksa, perbedaan status, perjanjian tertulis | Momen "melunak" kecil tiap 2–3 bab; cemburu; rahasia identitas |
| Balas dendam istri/menantu terhina | Dihina keluarga suami / dikhianati, lalu identitas asli (kaya/berkuasa) terungkap sedikit demi sedikit | Tokoh jahat "kena batunya" berkala; pembaca menunggu pembalasan |
| Kembali ke masa lalu / kesempatan kedua | Mati atau terpuruk, bangun di masa lalu dengan ingatan | Tokoh memakai pengetahuan masa depan untuk menang; dramatic irony |
| Fantasi sistem / kultivasi | Tokoh lemah mendapat "sistem"/kekuatan rahasia | Naik level teratur; meremehkan lalu dikalahkan |
| Horor lokal | Kampung, rumah warisan, pesugihan, ritual | Teror meningkat bertahap; satu aturan gaib dilanggar |
| Perselingkuhan / rumah tangga | Bukti perselingkuhan, istri diam-diam menyusun rencana | Bukti terkumpul; konfrontasi publik |
