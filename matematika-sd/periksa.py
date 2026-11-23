#!/usr/bin/env python3
"""Menghitung ulang semua jawaban latihan dan contoh hitungan (dasar kunci.md)."""
from fractions import Fraction as F
from math import ceil

def rb(n):  # format ribuan pakai titik
    return f"{n:,}".replace(",", ".")

print("== Contoh")
assert 2475 + 1368 == 3843 and 5302 - 1748 == 3554 and 37 + 48 + 63 == 148
assert 47 * 6 == 282 and 36 * 24 == 864 and 36 * 4 == 144 and 36 * 20 == 720
assert 864 // 4 == 216 and divmod(735, 6) == (122, 3) and 618 // 3 == 206
assert F(12, 18) == F(2, 3) and F(3, 4) * 20 == 15 and F(1, 2) + F(1, 3) == F(5, 6)
assert 48 // 6 + 5 * (9 - 7) == 18 and 2 + 3 * 4 == 14 and (2 + 3) * 4 == 20 and 20 - 5 + 3 == 18
assert (26 - 5) // 3 == 7 and 30 - 12 == 18
assert 180 - 50 - 70 == 60 and 2 * (12 + 8) == 40
assert F(22, 7) * 14 == 44 and F(22, 7) * 7 * 7 == 154
print("contoh OK")

J = {}
# Bab 1
J[1] = ["9.000 + 50 + 4", "30.000", "72.016", "60.099 < 60.990",
        "; ".join(rb(x) for x in sorted([3210, 3012, 3201, 3102])),
        rb(round(5462, -1)), rb(round(5462, -3)), "7.410"]
# Bab 2
sisa_beras = 25 - 7 - 9
J[2] = [rb(3658 + 2475), rb(40506 + 9897), rb(8000 - 2346), rb(7215 - 3468),
        str(25 + 75 + 68), f"{sisa_beras} kg", f"{rb(3450 + 1275 - 680)} buku", rb(7000 - 4528)]
# Bab 3
J[3] = [f"5 + 5 + 5 + 5 = {5*4}", str(7 * 8), str(9 * 6), str(4 * 25 * 13),
        f"8 × 20 + 8 × 3 = 160 + 24 = {8*23}", str(58 * 7), rb(45 * 32), f"{24*15} pensil"]
# Bab 4
q, r = divmod(45, 6)
J[4] = [str(56 // 8), str(63 // 7), "54 : 6 = 9 dan 54 : 9 = 6", f"{q} sisa {r}",
        str(936 // 3), str(1512 // 7), str(824 // 4), f"{ceil(150/40)} bus (3 bus hanya memuat 120 siswa)"]
assert 936 % 3 == 0 and 1512 % 7 == 0 and 824 % 4 == 0
# Bab 5
def fr(x): return f"{x.numerator}/{x.denominator}"
J[5] = ["dimakan 3/8, tersisa 5/8", fr(F(15, 20)), str(F(2, 3) * 12), "3/5 < 2/3 (9/15 < 10/15)",
        fr(F(2, 7) + F(3, 7)), f"3/12 + 8/12 = {fr(F(1,4)+F(2,3))}", f"{F(2,5)*30} buku", "senilai: 2/5 = 6/15 (atas dan bawah dikali 3)"]
assert F(3, 5) < F(2, 3) and F(2, 5) == F(6, 15)
# Bab 8 aljabar
def pola_tambah(a, d, n): return [a + d * k for k in range(n)]
J[8] = [str(75 - 38), str(56 + 24), str(72 // 8), str(90 - 35), str((30 + 6) // 4),
        str(36 - 4 * 5 + 2), str((36 - 4) * (5 + 2)),
        f"Rina {48//4} tahun, ayah {3*48//4} tahun"]
assert 4 * 9 - 6 == 30
# Bab 10 bangun datar
J[10] = ["persegi dan persegi panjang", "trapesium",
        "keduanya 4 sisi sama panjang, tetapi sudut persegi siku-siku, sudut belah ketupat tidak",
        f"{180-90-35}°, segitiga siku-siku", "sama kaki", f"{2*7} cm",
        "benar: persegi punya 4 sudut siku-siku dan sisi berhadapan sama panjang",
        "jawaban bebas (misalnya jam dinding, pintu, penggaris segitiga)"]
# Bab 11 keliling dan luas
pi = F(22, 7)
r7 = 28 // 2
ubin = (400 // 50) * (300 // 50)
J[11] = [f"keliling {4*9} cm, luas {9*9} cm²", f"keliling {2*(15+6)} cm, luas {15*6} cm²",
        f"{12*7//2} cm²", f"{14*5} cm²", f"{(8+12)*6//2} cm²", f"{20*30//2} cm²",
        f"keliling {pi*28} cm, luas {pi*r7*r7} cm²", f"{ubin} ubin (8 × 6)"]

# Bab 6 desimal (pakai Decimal agar tepat)
d = lambda x: str(x).replace(".", ",")
from decimal import Decimal as Dm
assert Dm("12.5") + Dm("3.75") == Dm("16.25") and Dm(8) - Dm("2.35") == Dm("5.65")
assert Dm("1.2") * Dm("0.3") == Dm("0.36") and 150000 * 20 // 100 == 30000
J[6] = ["0,7 dan 0,23", "0,04 (empat perseratus)",
        "; ".join(d(x) for x in sorted([Dm("0.6"), Dm("0.55"), Dm("0.605"), Dm("0.06")])),
        d(Dm("4.7") + Dm("2.85")), d(Dm(10) - Dm("3.46")), d((Dm("2.5") * Dm("0.4")).normalize()),
        "0,6 dan 60%", f"{80*25//100} soal"]
# Bab 7 pola
fib = [1, 1]
while len(fib) < 9: fib.append(fib[-1] + fib[-2])
warna = ["merah", "putih", "hijau", "kuning"]
assert 2 + 1 + 2 + 3 + 4 == 12 and 12 + 5 == 17
assert 4 + 19 * 3 == 61 and divmod(50, 3) == (16, 2)
J[7] = ["26, 31", "54, 45", "162, 486", "16, 22 (selisih +1, +2, +3, +4, +5, +6)",
        f"{fib[7]}, {fib[8]}", f"5 + 14 × 4 = {5 + 14*4}",
        f"38 : 4 = 9 sisa 2 → {warna[38 % 4 - 1]}", f"{sum(range(1, 12, 2))} (= 6 × 6)"]
# Bab 9 logika
J[9] = ["(a) benar, (c) salah; (b) bukan pernyataan", "salah (12 tidak habis dibagi 5)",
        "benar (12 genap)", "belum tentu", "lampu tidak menyala",
        f"misalnya 2, 6, atau 10 ({[x for x in range(2, 12, 2) if x % 4]})",
        f"genap: ganjil + ganjil = genap ({137 + 259})", "paling tua Gita, paling muda Hana (Gita, Eka, Fani, Hana)"]
assert (137 + 259) % 2 == 0

for b, js in sorted(J.items()):
    print(f"Bab {b}:")
    for i, j in enumerate(js, 1):
        print(f"  {i}. {j}")
