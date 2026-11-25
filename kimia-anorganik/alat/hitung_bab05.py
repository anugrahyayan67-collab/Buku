#!/usr/bin/env python3
"""Angka Bab 5: kemasan, rongga, massa jenis dari parameter kisi, rasio jari-jari, perovskit, Bragg, cacat."""
import numpy as np
NA = 6.02214076e23; kB = 8.617333e-5
print('== efisiensi kemasan')
for n, z, r in [('kubus sederhana', 1, .5), ('bcc', 2, np.sqrt(3) / 4), ('ccp/fcc', 4, np.sqrt(2) / 4), ('intan', 8, np.sqrt(3) / 8)]:
    print(n, round(100 * z * 4 / 3 * np.pi * r**3, 1), '%')
print('== rasio rongga r+/r-')
for n, v in [('segitiga', 2 / np.sqrt(3) - 1), ('tetrahedral', np.sqrt(1.5) - 1), ('oktahedral', np.sqrt(2) - 1), ('kubus', np.sqrt(3) - 1)]: print(n, round(v, 3))
print('== massa jenis dari parameter kisi')
def rho(Z, M, a, b=None, c=None, hex=False):
    V = (a * (b or a) * (c or a)) * (np.sqrt(3) / 2 if hex else 1) * 1e-30  # pm^3 -> cm^3 : 1 pm^3 = 1e-30 cm^3
    return Z * M / (NA * V)
data = [('NaCl', 4, 58.44, 564.0), ('KCl', 4, 74.55, 629.2), ('CsCl', 1, 168.36, 412.3), ('ZnS sfalerit', 4, 97.47, 541.0), ('CaF2', 4, 78.07, 546.3),
        ('MgO', 4, 40.30, 421.2), ('Cu', 4, 63.546, 361.5), ('Fe bcc', 2, 55.845, 286.7), ('intan', 8, 12.011, 356.7), ('Si', 8, 28.086, 543.1),
        ('SrTiO3', 1, 183.49, 390.5), ('Li2O', 4, 29.88, 461.4)]
for n, Z, M, a in data: print(n, 'Z', Z, 'rho', round(rho(Z, M, a), 3))
print('rutil TiO2', round(rho(2, 79.87, 459.4, 459.4, 295.9), 3))
print('grafit', round(rho(4, 12.011, 246.4, 246.4, 670.8, hex=True), 3))
print('== jarak dari a: NaCl d(Na-Cl)=a/2', 564.0 / 2, 'CsCl d=a√3/2', round(412.3 * np.sqrt(3) / 2, 1), 'ZnS a√3/4', round(541.0 * np.sqrt(3) / 4, 1), 'CaF2 Ca-F a√3/4', round(546.3 * np.sqrt(3) / 4, 1))
print('intan C-C', round(356.7 * np.sqrt(3) / 4, 1), 'Cu r', round(361.5 * np.sqrt(2) / 4, 1), 'Fe r', round(286.7 * np.sqrt(3) / 4, 1))
print('== rasio jari-jari halida alkali (Shannon, KB6)')
cat = {'Li': 76, 'Na': 102, 'K': 138, 'Rb': 152, 'Cs': 167}; an = {'F': 133, 'Cl': 181, 'Br': 196, 'I': 220}
for c in cat:
    print(c, {a: round(cat[c] / an[a], 2) if cat[c] < an[a] else round(an[a] / cat[c], 2) for a in an})
print('CsCl r+(KB8)=174:', round(174 / 181, 2), ' NaCl', round(102/181,3), ' MgO', round(72/140,3), ' ZnS Zn KB4 60/S 184', round(60/184,3), ' CaF2 Ca KB8 112/F 131?', round(112/133,3), ' TiO2', round(60.5/140,3), ' SiO2 Si KB4 26/140', round(26/140,3))
print('== faktor toleransi perovskit t=(rA+rO)/(√2(rB+rO))')
for n, rA, rB in [('SrTiO3', 144, 60.5), ('CaTiO3', 134, 60.5), ('BaTiO3', 161, 60.5), ('KNbO3', 164, 64)]:
    print(n, round((rA + 140) / (np.sqrt(2) * (rB + 140)), 3))
print('== Bragg Cu Ka 154.06 pm')
lam = 154.06
def pola(a, fA, fB, nm):
    out = []
    for h in range(0, 5):
        for k in range(0, h + 1):
            for l in range(0, k + 1):
                if h + k + l == 0: continue
                if len({h % 2, k % 2, l % 2}) > 1: continue  # fcc: semua genap atau semua ganjil
                d = a / np.sqrt(h * h + k * k + l * l); s = lam / (2 * d)
                if s >= 1: continue
                F = fA + fB if h % 2 == 0 else fA - fB
                m = len({(x, y, z) for x in (h, -h) for y in (k, -k) for z in (l, -l)}) * len(set(__import__('itertools').permutations((h, k, l))))
                out.append(((h, k, l), round(d, 1), round(2 * np.degrees(np.arcsin(s)), 2), F * F))
    print(nm, [(x[0], x[1], x[2], x[3]) for x in sorted(out, key=lambda t: t[2])][:7])
pola(564.0, 18, 10, 'NaCl (f≈jumlah elektron Cl- 18, Na+ 10)'); pola(629.2, 18, 18, 'KCl (K+ 18, Cl- 18)')
print('== cacat Schottky NaCl, ΔH ~ 2,3 eV (per pasangan), n/N = exp(-ΔH/2kT)')
for T in (300, 600, 1000, 1073):
    print(T, '%.2e' % np.exp(-2.3 / (2 * kB * T)))
print('Frenkel AgCl ΔH ~ 1,4 eV:', {T: '%.1e' % np.exp(-1.4 / (2 * kB * T)) for T in (300, 700)})
print('== wustit Fe0,95O: y Fe3+ =', round(2 * (1 - 0.95), 3), ' Fe2+ =', round(0.95 - 2 * 0.05, 3), ' kekosongan per O = 0.05')
