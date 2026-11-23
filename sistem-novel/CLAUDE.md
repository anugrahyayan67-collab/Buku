# Aturan tetap: sistem menulis novel

Folder ini berisi sistem menulis novel berseri untuk aplikasi novel. Bahasa percakapan dengan penulis: santai. Bahasa novel: mengikuti `gaya` di Bible novel itu (umumnya Indonesia populer yang mengalir).

## Prinsip
1. **Jangan menulis dari ingatan.** Sebelum menulis atau mengedit bab apa pun, jalankan `python3 kit.py paket <novel> <N>` dan baca paketnya utuh. Bible dan log bab adalah sumber kebenaran; percakapan sebelumnya bukan.
2. **Fakta terkunci tidak boleh dilanggar.** Bila rencana bab menuntut melanggar fakta terkunci, berhenti dan tanyakan ke penulis.
3. **Tiru pola, bukan isi.** Riset novel populer hanya diambil polanya (trope, struktur, ritme). Jangan menyalin nama, adegan spesifik, atau kalimat.
4. **Penulis yang memutuskan.** Keputusan cerita besar (siapa mati, siapa pelaku, pasangan akhir) ditanyakan dulu kecuali sudah ada di kerangka.

## Bila diminta "tulis bab N novel X"
1. `python3 kit.py paket X N` lalu baca `X/_paket/bab-NNN.md`.
2. Ikuti `prompt/00-aturan-penulis.md` dan `prompt/05-tulis-bab.md`. Tulis ke `X/bab/NNN.md`.
3. `python3 kit.py cek X N`; perbaiki semua peringatan yang memang masalah.
4. Jalankan audit `prompt/06-cek-kontinuitas.md` sendiri terhadap paket; perbaiki bentrokan.
5. Jalankan `prompt/07-perbarui-ingatan.md`: tambahkan ringkasan ke `X/log-bab.md`, perbarui status tokoh, fakta baru, dan utas terbuka di `X/bible.md`.
6. Laporkan singkat: jumlah kata, cliffhanger yang dipakai, fakta baru yang dikunci, utas yang dibuka/ditutup.

## Bila diminta riset, konsep, Bible, atau kerangka
Pakai prompt `01`–`04` yang sesuai. Hasil riset disimpan di `riset/`, sisanya di folder novel.
