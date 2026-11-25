#!/usr/bin/env python3
"""Angka Bab 9: Daniell, Nernst, kompleksasi, Latimer, Frost Mn, Pourbaix Fe, Ellingham, biologi."""
import numpy as np, json
F, R, T = 96485.3, 8.314, 298.15
k = R * T * np.log(10) / F
print('0,0592 =', round(k, 5))
E = 0.340 + 0.762; dG = -2 * F * E / 1000; K = 10 ** (2 * E / k)
print('Daniell E', E, 'dG', round(dG, 1), 'K %.1e' % K)
print('Nernst Daniell [Zn2+]=1, [Cu2+]=0.01 ->', round(E - k / 2 * np.log10(1 / 0.01), 3))
for pH in (0, 7, 14): print('O2/H2O pH', pH, round(1.229 - k * pH, 3), 'H+/H2', round(-k * pH, 3))
print('MnO4-/Mn2+ pH 7', round(1.507 - 8 * k / 5 * 7, 3), ' pH 3', round(1.507 - 8 * k / 5 * 3, 3))
print('Cr2O7/Cr3+ pH 7', round(1.36 - 14 * k / 6 * 7, 3))
print('Ag(NH3)2+/Ag', round(0.7996 - k * np.log10(1.7e7), 3), 'AgCl/Ag', round(0.7996 + k * np.log10(1.77e-10), 3), 'AgI/Ag', round(0.7996 + k * np.log10(8.5e-17), 3))
# Fe(CN)6: beta6 Fe3+ 1e42, Fe2+ 1e35 -> E = 0.771 - k log(1e42/1e35)
print('Fe(CN)6 3-/4- dari beta', round(0.771 - k * 7, 3))
# Latimer
print('Cu2+/Cu dari Latimer', round((0.153 + 0.521) / 2, 3), 'disprop Cu+ E', round(0.521 - 0.153, 3), 'K %.1e' % 10 ** ((0.521 - 0.153) / k))
mnA = {'MnO4-': (7, 0.56), 'MnO4 2-': (6, 2.26), 'MnO2': (4, 0.95), 'Mn3+': (3, 1.51), 'Mn2+': (2, -1.18)}
print('MnO4-/MnO2', round((0.56 + 2 * 2.26) / 3, 3), 'MnO2/Mn2+', round((0.95 + 1.51) / 2, 3), 'MnO4-/Mn2+', round((0.56 + 2 * 2.26 + 0.95 + 1.51) / 5, 3))
# Frost pH0
nE = {0: 0}; nE[2] = 2 * -1.18; nE[3] = nE[2] + 1.51; nE[4] = nE[3] + 0.95; nE[6] = nE[4] + 2 * 2.26; nE[7] = nE[6] + 0.56
nEb = {0: 0}; nEb[2] = 2 * -1.56; nEb[3] = nEb[2] + 0.10; nEb[4] = nEb[3] - 0.20; nEb[6] = nEb[4] + 2 * 0.60; nEb[7] = nEb[6] + 0.56
print('Frost Mn pH0', {k_: round(v, 2) for k_, v in nE.items()}); print('Frost Mn pH14', {k_: round(v, 2) for k_, v in nEb.items()})
# Mn3+ disprop: 2Mn3+ -> Mn2+ + MnO2 E = 1.51 - 0.95
print('Mn3+ disprop E', round(1.51 - 0.95, 2), 'MnO4 2- disprop asam E', round(2.26 - 0.56, 2))
# komproporsionasi MnO4- + Mn2+ -> MnO2 : E = E(MnO4-/MnO2) - E(MnO2/Mn2+)
print('komprop MnO4-+Mn2+ E', round(1.693 - 1.23, 3))
# Pourbaix Fe, c = 1e-6
c = 1e-6; Ksp3 = 2.8e-39; Ksp2 = 4.87e-17; Kw = 1e-14
pH3 = 14 + np.log10((Ksp3 / c) ** (1 / 3)); pH2 = 14 + np.log10((Ksp2 / c) ** 0.5)
print('pH endapan Fe(OH)3', round(pH3, 2), 'Fe(OH)2', round(pH2, 2), 'Fe2+/Fe E', round(-0.447 + k / 2 * np.log10(c), 3))
# Fe(OH)3 + 3H+ + e -> Fe2+ + 3H2O : E = E°' - 3k pH - k log[Fe2+]; E°' = 0.771 + k log(Ksp3/Kw^3)
E0a = 0.771 + k * np.log10(Ksp3 / Kw**3); print("E° Fe(OH)3/Fe2+", round(E0a, 3))
# Fe(OH)3 + H+ + e -> Fe(OH)2 + H2O: E°'' = E0a + k log(Ksp2 / Kw^2) ... at pH: E = E0b - k pH
E0b = E0a - k * np.log10(Ksp2 / Kw**2) * 1  # derive: combine
print("E° Fe(OH)3/Fe(OH)2 (pH 0 ekstrapolasi)", round(E0b, 3))
# Fe(OH)2 + 2H+ + 2e -> Fe + 2H2O: E = -0.447 + k/2 log(Ksp2/Kw^2) - k pH
E0c = -0.447 + k / 2 * np.log10(Ksp2 / Kw**2); print('E° Fe(OH)2/Fe', round(E0c, 3))
json.dump({'pH3': pH3, 'pH2': pH2, 'E0a': E0a, 'E0b': E0b, 'E0c': E0c, 'k': k}, open('/home/user/Buku/kimia-anorganik/bab09/_pourbaix.json', 'w'))
# Ellingham (per mol O2): dG = dH - T dS (kJ)
ell = {'4Ag+O2→2Ag2O': (-62.2, -132.8), '4Cu+O2→2Cu2O': (-337.2, -151.6), '2Fe+O2→2FeO': (-544.0, -138.3), '2Zn+O2→2ZnO': (-701.0, -201.1),
       '4/3Al+O2→2/3Al2O3': (-1117.1, -209.0), '2Mg+O2→2MgO': (-1203.2, -216.8), '2C+O2→2CO': (-221.0, 178.7), 'C+O2→CO2': (-393.5, 2.86), '2CO+O2→2CO2': (-566.0, -173.0)}
for nm, (h, s) in ell.items(): print(nm, 'dG 298', round(h - 298.15 * s / 1000, 1), 'dG 1500', round(h - 1500 * s / 1000, 1))
def silang(a, b):
    (h1, s1), (h2, s2) = ell[a], ell[b]; return (h1 - h2) / ((s1 - s2) / 1000)
for m in ('2Fe+O2→2FeO', '2Zn+O2→2ZnO', '4/3Al+O2→2/3Al2O3', '2Mg+O2→2MgO', '4Cu+O2→2Cu2O'):
    print('C/CO memotong', m, round(silang(m, '2C+O2→2CO')), 'K')
print('Ag2O terurai di', round(-62.2 / -0.1328), 'K')
json.dump(ell, open('/home/user/Buku/kimia-anorganik/bab09/_ellingham.json', 'w'), ensure_ascii=False)
# biologi
dE = 0.816 - (-0.320); print('NADH->O2 dE', round(dE, 3), 'dG', round(-2 * F * dE / 1000, 1), 'kJ; ATP ~ 30,5 kJ ->', round(2 * F * dE / 1000 / 30.5, 1))
print('korosi Fe pH7 E', round(0.816 - (-0.447), 3))
print('Zn/Fe galvanis E', round(-0.447 - (-0.762), 3))
