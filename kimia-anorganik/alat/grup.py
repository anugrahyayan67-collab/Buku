#!/usr/bin/env python3
"""Mesin teori grup kecil untuk Bab 3–4: tabel karakter, rumus reduksi, Γ3N, mode getaran."""
from fractions import Fraction as Fr
T = {}
# setiap tabel: kelas (nama, jumlah operasi, kontribusi xyz per atom tak berpindah), lalu baris irep
T['C2v'] = (['E', 'C2', 'sv(xz)', 'sv(yz)'], [1, 1, 1, 1], [3, -1, 1, 1],
            {'A1': [1, 1, 1, 1], 'A2': [1, 1, -1, -1], 'B1': [1, -1, 1, -1], 'B2': [1, -1, -1, 1]},
            {'IR': ['A1', 'B1', 'B2'], 'Raman': ['A1', 'A2', 'B1', 'B2'], 'rot': ['A2', 'B1', 'B2'], 'trans': ['A1', 'B1', 'B2']})
T['C3v'] = (['E', '2C3', '3sv'], [1, 2, 3], [3, 0, 1],
            {'A1': [1, 1, 1], 'A2': [1, 1, -1], 'E': [2, -1, 0]},
            {'IR': ['A1', 'E'], 'Raman': ['A1', 'E'], 'rot': ['A2', 'E'], 'trans': ['A1', 'E']})
T['D3h'] = (['E', '2C3', '3C2', 'sh', '2S3', '3sv'], [1, 2, 3, 1, 2, 3], [3, 0, -1, 1, -2, 1],
            {"A1'": [1, 1, 1, 1, 1, 1], "A2'": [1, 1, -1, 1, 1, -1], "E'": [2, -1, 0, 2, -1, 0],
             "A1''": [1, 1, 1, -1, -1, -1], "A2''": [1, 1, -1, -1, -1, 1], "E''": [2, -1, 0, -2, 1, 0]},
            {'IR': ["E'", "A2''"], 'Raman': ["A1'", "E'", "E''"], 'rot': ["A2'", "E''"], 'trans': ["E'", "A2''"]})
T['Td'] = (['E', '8C3', '3C2', '6S4', '6sd'], [1, 8, 3, 6, 6], [3, 0, -1, -1, 1],
           {'A1': [1, 1, 1, 1, 1], 'A2': [1, 1, 1, -1, -1], 'E': [2, -1, 2, 0, 0], 'T1': [3, 0, -1, 1, -1], 'T2': [3, 0, -1, -1, 1]},
           {'IR': ['T2'], 'Raman': ['A1', 'E', 'T2'], 'rot': ['T1'], 'trans': ['T2']})
T['D2h'] = (['E', 'C2(z)', 'C2(y)', 'C2(x)', 'i', 's(xy)', 's(xz)', 's(yz)'], [1] * 8, [3, -1, -1, -1, -3, 1, 1, 1],
            {'Ag': [1, 1, 1, 1, 1, 1, 1, 1], 'B1g': [1, 1, -1, -1, 1, 1, -1, -1], 'B2g': [1, -1, 1, -1, 1, -1, 1, -1], 'B3g': [1, -1, -1, 1, 1, -1, -1, 1],
             'Au': [1, 1, 1, 1, -1, -1, -1, -1], 'B1u': [1, 1, -1, -1, -1, -1, 1, 1], 'B2u': [1, -1, 1, -1, -1, 1, -1, 1], 'B3u': [1, -1, -1, 1, -1, 1, 1, -1]},
            {'IR': ['B1u', 'B2u', 'B3u'], 'Raman': ['Ag', 'B1g', 'B2g', 'B3g'], 'rot': ['B1g', 'B2g', 'B3g'], 'trans': ['B1u', 'B2u', 'B3u']})
T['D4h'] = (['E', '2C4', 'C2', "2C2'", "2C2''", 'i', '2S4', 'sh', '2sv', '2sd'], [1, 2, 1, 2, 2, 1, 2, 1, 2, 2], [3, 1, -1, -1, -1, -3, -1, 1, 1, 1],
            {'A1g': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'A2g': [1, 1, 1, -1, -1, 1, 1, 1, -1, -1], 'B1g': [1, -1, 1, 1, -1, 1, -1, 1, 1, -1], 'B2g': [1, -1, 1, -1, 1, 1, -1, 1, -1, 1],
             'Eg': [2, 0, -2, 0, 0, 2, 0, -2, 0, 0], 'A1u': [1, 1, 1, 1, 1, -1, -1, -1, -1, -1], 'A2u': [1, 1, 1, -1, -1, -1, -1, -1, 1, 1],
             'B1u': [1, -1, 1, 1, -1, -1, 1, -1, -1, 1], 'B2u': [1, -1, 1, -1, 1, -1, 1, -1, 1, -1], 'Eu': [2, 0, -2, 0, 0, -2, 0, 2, 0, 0]},
            {'IR': ['A2u', 'Eu'], 'Raman': ['A1g', 'B1g', 'B2g', 'Eg'], 'rot': ['A2g', 'Eg'], 'trans': ['A2u', 'Eu']})
T['Oh'] = (['E', '8C3', '6C2', '6C4', '3C2', 'i', '6S4', '8S6', '3sh', '6sd'], [1, 8, 6, 6, 3, 1, 6, 8, 3, 6], [3, 0, -1, 1, -1, -3, -1, 0, 1, 1],
           {'A1g': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'A2g': [1, 1, -1, -1, 1, 1, -1, 1, 1, -1], 'Eg': [2, -1, 0, 0, 2, 2, 0, -1, 2, 0],
            'T1g': [3, 0, -1, 1, -1, 3, 1, 0, -1, -1], 'T2g': [3, 0, 1, -1, -1, 3, -1, 0, -1, 1], 'A1u': [1, 1, 1, 1, 1, -1, -1, -1, -1, -1],
            'A2u': [1, 1, -1, -1, 1, -1, 1, -1, -1, 1], 'Eu': [2, -1, 0, 0, 2, -2, 0, 1, -2, 0], 'T1u': [3, 0, -1, 1, -1, -3, -1, 0, 1, 1],
            'T2u': [3, 0, 1, -1, -1, -3, 1, 0, 1, -1]},
           {'IR': ['T1u'], 'Raman': ['A1g', 'Eg', 'T2g'], 'rot': ['T1g'], 'trans': ['T1u']})
def reduksi(g, chi):
    kel, n, _, irep, _ = T[g]; h = sum(n)
    out = {}
    for r, c in irep.items():
        a = Fr(sum(ni * ci * xi for ni, ci, xi in zip(n, c, chi)), h)
        assert a.denominator == 1, (g, r, a)
        if a: out[r] = int(a)
    return out
def kurang(a, b):
    o = dict(a)
    for k in b: o[k] -= 1; assert o[k] >= 0
    return {k: v for k, v in o.items() if v}
def teks(d): return ' + '.join((f'{v}{k}' if v > 1 else k) for k, v in d.items())
def getaran(g, tak):
    kel, n, kontr, irep, sel = T[g]
    G3 = [a * c for a, c in zip(tak, kontr)]
    tot = reduksi(g, G3)
    vib = kurang(kurang(tot, [r for r in sel['trans'] for _ in range(irep[r][0] and 1)]), [])
    # kurangi translasi dan rotasi (tiap irep sekali, E/T sudah membawa dimensinya)
    vib = dict(tot)
    for r in sel['trans'] + sel['rot']: vib[r] -= 1
    vib = {k: v for k, v in vib.items() if v}
    ir = sum(v for k, v in vib.items() if k in sel['IR']); ra = sum(v for k, v in vib.items() if k in sel['Raman'])
    both = sum(v for k, v in vib.items() if k in sel['IR'] and k in sel['Raman'])
    return G3, tot, vib, ir, ra, both
if __name__ == '__main__':
    kasus = [('H2O', 'C2v', [3, 1, 3, 1]), ('NH3', 'C3v', [4, 1, 2]), ('BF3', 'D3h', [4, 1, 2, 4, 1, 2]), ('CH4', 'Td', [5, 2, 1, 1, 3]),
             ('SF6', 'Oh', [7, 1, 1, 3, 3, 1, 1, 1, 5, 3]), ('XeF4', 'D4h', [5, 1, 1, 3, 1, 1, 1, 5, 3, 1]), ('SF4', 'C2v', [5, 1, 3, 3]),
             ('trans-PtCl2N2 (D2h, atom berat)', 'D2h', [5, 1, 3, 3, 1, 5, 3, 3])]
    for nm, g, tak in kasus:
        G3, tot, vib, ir, ra, both = getaran(g, tak)
        print(f'{nm} ({g}): G3N = {G3}\n   total = {teks(tot)}\n   getaran = {teks(vib)}; aktif IR {ir}, Raman {ra}, keduanya {both}')
    # regangan M-Cl: cis C2v dan trans D2h
    print('regangan Pt-Cl cis (C2v):', teks(reduksi('C2v', [2, 0, 2, 0])), '| trans (D2h, Cl pada sumbu x):', teks(reduksi('D2h', [2, 0, 0, 2, 0, 2, 2, 0])))
    print('regangan C-O fac/mer? -> SALC H 1s H2O:', teks(reduksi('C2v', [2, 0, 2, 0])), '; NH3 H1s:', teks(reduksi('C3v', [3, 0, 1])),
          '; BF3 F sigma:', teks(reduksi('D3h', [3, 0, 1, 3, 0, 1])), '; CH4 H1s:', teks(reduksi('Td', [4, 1, 0, 0, 2])), '; SF6 sigma:', teks(reduksi('Oh', [6, 0, 0, 2, 2, 0, 0, 0, 4, 2])))
    print('derajat kebebasan klorofil C55H72MgN4O5 (77+... ) :', 3*(55+72+1+4+5), 'getaran', 3*(55+72+1+4+5)-6)
