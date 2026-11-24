# Sistem Menulis Novel Berseri (untuk aplikasi novel)

Sistem ini dibuat untuk satu masalah utama: **AI lupa detail awal ketika cerita sudah panjang**, sehingga di tengah cerita muncul bentrokan (nama berubah, umur berubah, tokoh yang sudah mati muncul lagi, janji cerita tidak ditepati).

Jawabannya bukan "prompt yang lebih pintar", tetapi **ingatan di luar kepala AI**:

1. **Story Bible** (`bible.md`) — semua fakta yang sudah terkunci: tokoh, tempat, aturan dunia, garis waktu, rahasia, utas yang belum selesai.
2. **Log bab** (`log-bab.md`) — ringkasan setiap bab (± 100–150 kata) + fakta baru yang muncul di bab itu.
3. **Paket konteks** — sebelum menulis bab berikutnya, skrip `kit.py` merakit Bible + semua ringkasan + akhir bab terakhir + rencana bab ini menjadi satu teks. Teks itulah yang diberikan ke AI. AI tidak pernah menulis dari ingatan.
4. **Audit kontinuitas** — setiap bab yang selesai diperiksa terhadap Bible sebelum di-upload.

## Isi folder

| Berkas | Fungsi |
|---|---|
| `CLAUDE.md` | Aturan tetap untuk Claude Code (otomatis dibaca bila kamu bekerja di folder ini) |
| `prompt/00-aturan-penulis.md` | "Instruksi sistem" untuk AI mana pun: gaya, larangan, format bab |
| `prompt/01-riset-pasar.md` | Riset novel yang sedang ramai di aplikasi → **pola**, bukan isi |
| `prompt/02-konsep.md` | Premis, judul, blurb/sinopsis aplikasi, hook bab 1 |
| `prompt/03-bible-awal.md` | Mengisi Story Bible dari konsep |
| `prompt/04-kerangka.md` | Kerangka arc dan rencana per bab (kurva ketegangan) |
| `prompt/05-tulis-bab.md` | Menulis satu bab dari paket konteks |
| `prompt/06-cek-kontinuitas.md` | Audit bab terhadap Bible (mencari bentrokan) |
| `prompt/07-perbarui-ingatan.md` | Ringkasan bab + fakta baru → masuk Bible dan log |
| `prompt/08-teknik-ketegangan.md` | Buku saku: cliffhanger, adegan tegang, tempo, pola genre |
| `templat/` | Bible, log bab, dan kerangka kosong |
| `kit.py` | Alat bantu: `baru`, `paket`, `cek`, `status` |
| `novel-contoh/` | Contoh terisi (drama balas dendam, 1 bab dipendekkan + rencana 3 bab), untuk melihat format Bible, log, dan kerangka |

## Alur kerja

### A. Sekali di awal (± 1–2 jam)
1. **Riset pasar** — `prompt/01-riset-pasar.md`. Pilih genre, minta AI (yang punya akses web) menganalisis 5–10 novel paling ramai di genre itu: pola hook, tipe tokoh, kapan konflik besar muncul, panjang bab, jenis cliffhanger. Simpan hasilnya di `riset/`.
2. **Konsep** — `prompt/02-konsep.md`. Hasil: logline, judul, blurb aplikasi, 3 tokoh inti, "janji" cerita ke pembaca.
3. **Buat folder novel**: `python3 kit.py baru judul-novelmu` → menyalin templat.
4. **Isi Bible** — `prompt/03-bible-awal.md`. Baca ulang dan perbaiki sendiri. Bible adalah sumber kebenaran.
5. **Kerangka** — `prompt/04-kerangka.md`. Kerangka arc pertama (20–40 bab) + rencana per bab.

### B. Setiap bab (ulangi terus)
1. `python3 kit.py paket judul-novelmu 12` → membuat `judul-novelmu/_paket/bab-012.md`.
2. Beri AI: isi `prompt/00-aturan-penulis.md` + isi `prompt/05-tulis-bab.md` + paket tadi. AI menulis bab 12.
3. Simpan ke `judul-novelmu/bab/012.md`, lalu `python3 kit.py cek judul-novelmu 12` (jumlah kata, nama asing yang tidak ada di Bible, frasa klise AI, paragraf terlalu panjang).
4. Audit — `prompt/06-cek-kontinuitas.md` dengan paket + bab baru. Perbaiki semua bentrokan.
5. Perbarui ingatan — `prompt/07-perbarui-ingatan.md`. Tempel ringkasan ke `log-bab.md` dan fakta baru ke `bible.md`.
6. **Baca sendiri**, edit, baru upload.

> Kalau kamu memakai **Claude Code** di folder ini, cukup bilang: *"tulis bab 12 novel judul-novelmu"*. `CLAUDE.md` membuat Claude menjalankan langkah 1–5 sendiri.

### Tanpa Python / Claude Code (hanya aplikasi chat)
Rakit paketnya sendiri dengan menyalin, berurutan: **Fakta terkunci** → **Status tokoh terbaru** → **Utas terbuka** (dari `bible.md`) → sisa `bible.md` → semua ringkasan di `log-bab.md` → ± 500 kata terakhir bab sebelumnya → rencana bab ini dari `kerangka.md`. Selalu mulai **percakapan baru** untuk setiap bab; percakapan yang terlalu panjang justru membuat AI makin pelupa.

### Batas `kit.py cek`
`cek` menangkap salah ketik nama dan nama baru di **tengah** kalimat, frasa klise, pengulangan, paragraf kepanjangan, dan bagian FAKTA BARU yang hilang. Nama di **awal** kalimat tidak bisa dibedakan dari kata biasa, jadi itu tugas audit kontinuitas (prompt 06). Skrip tidak menilai logika cerita; itu juga tugas audit 06 dan matamu sendiri.

## Kenapa cara ini mencegah bentrokan
- AI hanya "ingat" yang ada di depannya. Paket konteks memastikan semua fakta penting **selalu** ada di depannya, berapa pun panjang novelnya (ringkasan 150 kata × 100 bab ≈ 15 000 kata, masih muat).
- **Fakta terkunci** di Bible ditulis sebagai daftar pendek yang tidak boleh dilanggar (umur, warna mata, siapa tahu rahasia apa, siapa sudah mati).
- **Status tokoh per bab** (di mana, terluka atau tidak, tahu apa) diperbarui tiap bab, sehingga tokoh tidak tiba-tiba tahu hal yang belum pernah ia dengar.
- **Utas terbuka** (janji ke pembaca: misteri, foreshadowing) dicatat, supaya dibayar di akhir dan tidak dilupakan.

## Catatan penting soal aplikasi dan uang
- **Baca ketentuan aplikasinya dulu.** Beberapa platform mensyaratkan karya asli, melarang atau membatasi konten buatan AI, dan bisa membatalkan kontrak. Sistem ini memposisikan AI sebagai **asisten**: kamu yang menentukan cerita, mengedit, dan bertanggung jawab atas naskah.
- **"Tiru pola, bukan isi."** Trope (nikah kontrak, balas dendam, CEO dingin, sistem, reinkarnasi) bebas dipakai siapa saja. Menyalin alur spesifik, adegan, nama, atau kalimat novel orang lain = plagiat, dan bisa membuat akun diblokir.
- Penghasilan di aplikasi novel umumnya bergantung pada kontrak (eksklusif/non-eksklusif), syarat jumlah kata, dan **konsistensi update** (banyak penulis update harian). Sistem ini membantu kecepatan dan konsistensi; laris atau tidaknya tetap ditentukan cerita dan pembaca.
