#!/usr/bin/env python3
"""Angka Bab 2 Kimia Anorganik 1."""
from math import cos, acos, radians, degrees, sqrt
D = 3.33564e-30; e = 1.602177e-19
print('== muatan parsial dari momen dipol: q/e = mu/(e d)')
for m, mu, d in [('HF', 1.826, 91.7), ('HCl', 1.109, 127.4), ('HBr', 0.827, 141.4), ('HI', 0.448, 160.9), ('CO', 0.110, 112.8)]:
    print(f'  {m}: {mu*D/(e*d*1e-12):.3f}')
print('== hibrida setara: cos(theta) = -1/n -> karakter s = 1/(1+n)')
for m, th in [('CH4', 109.47), ('NH3', 106.7), ('H2O', 104.5), ('PH3', 93.3), ('H2S', 92.1)]:
    n = -1 / cos(radians(th)); print(f'  {m}: sudut {th}°, n = {n:.2f}, karakter s ikatan = {100/(1+n):.1f} %')
print('  sp2 120 ->', round(degrees(acos(-1/2)), 1), '; sp 180; sp3', round(degrees(acos(-1/3)), 2))
print('== entalpi reaksi dari energi ikatan')
nh3 = 945 + 3*436 - 6*391; print('  N2 + 3H2 -> 2NH3:', nh3, 'kJ (data -92)')
h2o2 = (2*463 + 146) ; print('  H2O2 -> H2O + 1/2 O2: putus', 2*463+146, 'bentuk', 2*463 + 498/2, '->', 2*463+146 - (2*463 + 498/2), 'kJ (data -98)')
n2h4 = 160 + 4*391 + 498 - (945 + 4*463); print('  N2H4 + O2 -> N2 + 2H2O(g):', n2h4, 'kJ (data -534)')
ch4 = 4*413 + 2*498 - (2*799 + 4*463); print('  CH4 + 2O2 -> CO2 + 2H2O(g):', ch4, 'kJ (data -802)')
print('== kuat ikatan rangkap: C=C - C-C', 614-347, '; C≡C - C=C', 839-614, '; N=N - N-N', 418-160, '; N≡N - N=N', 945-418)
print('== oksidasi: S dalam S2O3(2-) rata-rata', (2*1 - 0)/1 if False else (0+2*1)/1)
for sp, ox in [('S2O3 2-', (-2 + 3*2)/2), ('S4O6 2-', (-2 + 6*2)/4), ('N3-', -1/3), ('Fe3O4', 8/3), ('C3O2', 4/3)]:
    print(f'  {sp}: rata-rata {ox:.3f}')
print('== titik didih hidrida (°C) dan anomali')
bp = {'14': [-161.5, -111.9, -88.5, -51.8], '15': [-33.3, -87.7, -62.5, -17.0], '16': [100.0, -60.3, -41.3, -2.2], '17': [19.5, -85.1, -66.8, -35.4]}
for g, v in bp.items():
    # ekstrapolasi linear dari periode 3-5 ke periode 2
    x = [3, 4, 5]; y = v[1:]; n = 3; mx = sum(x)/n; my = sum(y)/n
    b = sum((a-mx)*(c-my) for a, c in zip(x, y)) / sum((a-mx)**2 for a in x); a0 = my - b*mx
    print(f'  gol {g}: periode 2 terukur {v[0]}, ekstrapolasi {a0 + 2*b:.0f}, selisih {v[0] - (a0 + 2*b):.0f}')
print('== gas mulia: tl (K) vs polarisabilitas (A^3)')
for g, T, a in [('He', 4.2, .205), ('Ne', 27.1, .396), ('Ar', 87.3, 1.64), ('Kr', 119.8, 2.48), ('Xe', 165.0, 4.04), ('Rn', 211.5, 5.3)]:
    print(f'  {g}: {T} K, alpha {a}')
print('== energi interaksi relatif dipol (1/r^3 ion-dipol, 1/r^6 dispersi): gandakan r ->', 1/2**3, 1/2**6)
print('== muatan formal SCN- tiga struktur: [S=C=N]- : S 0, C 0, N -1 ; [S-C≡N]-: S -1, C 0, N 0 ; [S≡C-N]-: S +1, C 0, N -2')
print('== N2O: N=N=O : N(-1) N(+1) O(0); N≡N-O : N(0) N(+1) O(-1)')
print('== ClO4-: semua tunggal: Cl +3, O -1; 3 rangkap+1 tunggal: Cl 0')
