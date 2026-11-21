# Pemetaan model untuk penyusunan buku

Ditetapkan November 2026. Model yang dipakai hanya **Claude Opus 5.5** dan **Claude Sonnet 5.5**. Fable 5.2 dan Haiku 5.5 tidak dipakai.

## Dasar pertimbangan

| Model | Harga API (input / output per 1 jt token) | Relatif | Catatan dari tolok ukur resmi |
|---|---|---|---|
| Opus 5.5 | $4 / $20 | 2× | Penalaran multidisiplin (HLE) 67,7%; terbaik untuk penurunan matematis |
| Sonnet 5.5 | $2 / $10 | 1× | HLE 64,5%; pekerjaan pengetahuan setara Opus pada effort high; kuat untuk pekerjaan terminal/kode |
| Fable 5.2 | $8 / $40 | 4× | Tidak dipakai: dua kali harga Opus, dan Opus sudah cukup untuk tingkat buku S1 |
| Haiku 5.5 | $0,10 / $0,50 | ± 1/20× | Tidak dipakai: terlalu riskan untuk isi ilmiah; pekerjaan mekanis sudah murah di Sonnet |

Di Claude Code berlangganan yang terpakai adalah kuota, dengan perbandingan kira-kira sama (Opus ± 2× Sonnet).

## Peta tetap

| Tahap | Model | Effort |
|---|---|---|
| Kerangka buku, pedoman, daftar subbab | Opus 5.5 | high |
| Menulis materi dan penurunan rumus | Opus 5.5 | high |
| Bab tersulit Kimia Kuantum (Bab 8–14, 17) | Opus 5.5 | xhigh |
| Contoh soal, soal latihan, jawaban, pembahasan | Opus 5.5 (Sonnet 5.5 bila kuota menipis) | high |
| Pemeriksaan ulang angka dan rujukan satu bab | Sonnet 5.5 | high |
| Gambar matplotlib, build bab, cetak buku, indeks | Sonnet 5.5 | medium |
| Tata letak, CSS, sampul | Sonnet 5.5 | medium |
| Perbaikan kecil (salah ketik, label, cetak ulang) | Sonnet 5.5 | low–medium |

Ganti model dan effort lewat `/model` di Claude Code. Alur satu bab yang dianjurkan:
1. **Opus 5.5 · high**: tulis materi, contoh, kuis, soal, jawaban.
2. **Sonnet 5.5 · medium**: buat gambar, bangun PDF bab, perbaiki tampilan.
3. **Sonnet 5.5 · high**: periksa ulang angka dan rujukan, lalu commit.

## Revisi buku (ditetapkan November 2026, atas permintaan penyusun)

Revisi total memakai **Opus 5.5 saja**, effort disesuaikan jenis pekerjaan. Rincian untuk *Termodinamika Kimia* ada di `termodinamika-kimia/REVISI.md`.

| Pekerjaan revisi | Model | Effort |
|---|---|---|
| Baca kritis, kalimat penjelas, tambah isi/contoh/soal tantangan | Opus 5.5 | high |
| Verifikasi angka, ejaan/notasi, gambar, indeks, lampiran, desain, cetak | Opus 5.5 | medium |
