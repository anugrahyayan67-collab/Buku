#!/usr/bin/env python3
"""Angka Bab 6: tetapan Madelung (penjumlahan Evjen), Born–Landé, Born–Mayer, Kapustinskii, Born–Haber, senyawa hipotetis, kelarutan, karbonat."""
import numpy as np, json, sys
NA, e, eps0 = 6.02214076e23, 1.602176634e-19, 8.8541878128e-12
K = NA * e**2 / (4 * np.pi * eps0) * 1e12 / 1000   # kJ mol^-1 pm  (bila r dalam pm)
print('N_A e^2/(4 pi eps0) =', round(K, 0), 'kJ mol-1 pm')
# --- Madelung NaCl dengan kubus Evjen
def evjen(N):
    s = 0.0
    r = np.arange(-N, N + 1)
    X, Y, Z = np.meshgrid(r, r, r, indexing='ij')
    q = (-1.0) ** (np.abs(X) + np.abs(Y) + np.abs(Z))
    w = np.ones_like(X, dtype=float)
    for A in (X, Y, Z): w *= np.where(np.abs(A) == N, .5, 1.)
    d = np.sqrt(X**2 + Y**2 + Z**2); m = d > 0
    return -(q[m] * w[m] / d[m]).sum()
mad = {N: round(evjen(N), 5) for N in (1, 2, 3, 4, 6, 10, 20)}
print('Madelung NaCl (Evjen):', mad)
# deret satu dimensi: rantai bergantian 2 ln 2
print('rantai 1D: 2 ln 2 =', round(2 * np.log(2), 4))
print('tiga suku pertama NaCl:', round(6 - 12 / np.sqrt(2) + 8 / np.sqrt(3), 3), ' ... +6/2:', round(6 - 12 / np.sqrt(2) + 8 / np.sqrt(3) - 6 / 2, 3))
# --- Born-Lande
A = {'NaCl': 1.74756, 'CsCl': 1.76267, 'ZnS': 1.63806, 'wurtzit': 1.64132, 'CaF2': 2.51939, 'TiO2': 2.408, 'Al2O3': 4.1719}
nB = {'He': 5, 'Ne': 7, 'Ar': 9, 'Kr': 10, 'Xe': 12}
def BL(Am, z1, z2, r0, n): return -K * Am * z1 * z2 / r0 * (1 - 1 / n)
def BM(Am, z1, z2, r0, rho=34.5): return -K * Am * z1 * z2 / r0 * (1 - rho / r0)
def kap(nu, z1, z2, rs): return -1.2025e5 * nu * z1 * z2 / rs * (1 - 34.5 / rs)
dat = [  # nama, struktur, z1, z2, r0 (pm, dari parameter kisi), n, U siklus (kJ/mol, entalpi kisi termokimia)
 ('LiF', 'NaCl', 1, 1, 201.4, (5 + 7) / 2, 1049), ('NaF', 'NaCl', 1, 1, 231.7, 7, 930), ('NaCl', 'NaCl', 1, 1, 282.0, 8, 787),
 ('NaBr', 'NaCl', 1, 1, 298.7, 8.5, 751), ('NaI', 'NaCl', 1, 1, 323.7, 9.5, 705), ('KCl', 'NaCl', 1, 1, 314.6, 9, 717),
 ('KI', 'NaCl', 1, 1, 352.9, 10.5, 649), ('CsCl', 'CsCl', 1, 1, 357.1, 10.5, 659), ('CsI', 'CsCl', 1, 1, 395.6, 12, 604),
 ('MgO', 'NaCl', 2, 2, 210.6, 7, 3795), ('CaO', 'NaCl', 2, 2, 240.5, 8, 3414), ('BaO', 'NaCl', 2, 2, 276.2, 10.5, 3029),
 ('CaF2', 'CaF2', 2, 1, 236.6, 8, 2651),
 ('AgF', 'NaCl', 1, 1, 246.0, 8.5, 974), ('AgCl', 'NaCl', 1, 1, 277.5, 9.5, 918), ('AgBr', 'NaCl', 1, 1, 288.4, 10, 905), ('AgI', 'ZnS', 1, 1, 281.4, 11, 892)]
rows = []
for nm, st, z1, z2, r0, n, Uc in dat:
    u1 = BL(A[st], z1, z2, r0, n); u2 = BM(A[st], z1, z2, r0)
    rows.append((nm, round(u1), round(u2), Uc, round(100 * (Uc + u1) / Uc, 1)))
for r in rows: print('%-5s BL %6d  BM %6d  siklus %5d  selisih(%%) %5.1f' % r)
# --- Kapustinskii dengan jari-jari Shannon (KB 6)
rS = {'Li': 76, 'Na': 102, 'K': 138, 'Rb': 152, 'Cs': 167, 'Mg': 72, 'Ca': 100, 'Sr': 118, 'Ba': 135, 'F': 133, 'Cl': 181, 'Br': 196, 'I': 220, 'O': 140, 'CO3': 178, 'SO4': 258, 'NO3': 179, 'O2': 173, 'OH': 133}
for nm, c, a, nu, z1, z2 in [('NaCl', 'Na', 'Cl', 2, 1, 1), ('KCl', 'K', 'Cl', 2, 1, 1), ('MgO', 'Mg', 'O', 2, 2, 2), ('CaF2', 'Ca', 'F', 3, 2, 1), ('Na2O', 'Na', 'O', 3, 1, 2)]:
    print('Kapustinskii', nm, round(kap(nu, z1, z2, rS[c] + rS[a])))
# --- Born-Haber NaCl
NaCl = dict(sub=107.5, IE=495.8, halfD=121.7, EA=-348.6, f=-411.2)
UL = NaCl['sub'] + NaCl['IE'] + NaCl['halfD'] + NaCl['EA'] - NaCl['f']
print('Born-Haber NaCl entalpi kisi =', round(UL, 1))
# KCl
KCl = dict(sub=89.0, IE=418.8, halfD=121.7, EA=-348.6, f=-436.5)
print('Born-Haber KCl =', round(sum(KCl[k] for k in ('sub', 'IE', 'halfD', 'EA')) - KCl['f'], 1))
# MgO: hitung afinitas elektron total O -> O2- dari siklus dengan U = 3795
MgO = dict(sub=147.1, IE=737.7 + 1450.7, halfD=249.2, f=-601.6, U=3795)
EA_tot = MgO['f'] - MgO['sub'] - MgO['IE'] - MgO['halfD'] + MgO['U']
print('MgO: EA1+EA2 (O->O2-) =', round(EA_tot, 1), ' EA2 =', round(EA_tot + 141.0, 1))
# CaF2 Born-Haber
CaF2 = dict(sub=177.8, IE=589.8 + 1145.4, D=158.8, EA=2 * -328.2, f=-1228.0)
print('Born-Haber CaF2 =', round(CaF2['sub'] + CaF2['IE'] + CaF2['D'] + CaF2['EA'] - CaF2['f'], 1))
# --- senyawa hipotetis (Kapustinskii; jari-jari kation monovalen dianggap mirip ion tetangga)
hal = dict(halfD=121.7, EA=-348.6)
def dfH(sub, IE, U): return sub + IE + hal['halfD'] + hal['EA'] + U
U_MgCl = kap(2, 1, 1, 102 + 181)     # Mg+ dianggap seukuran Na+
U_CaCl = kap(2, 1, 1, 138 + 181)     # Ca+ ~ K+
U_NeCl = kap(2, 1, 1, 102 + 181)
U_MgCl2 = kap(3, 2, 1, 72 + 181)
U_MgCl3 = kap(4, 3, 1, 60 + 181)     # Mg3+ dianggap ~ 60 pm
print('U MgCl', round(U_MgCl), 'CaCl', round(U_CaCl), 'MgCl2 (Kap)', round(U_MgCl2), 'MgCl3', round(U_MgCl3))
f_MgCl = dfH(147.1, 737.7, U_MgCl); f_CaCl = dfH(177.8, 589.8, U_CaCl); f_NeCl = dfH(0, 2080.7, U_NeCl)
f_MgCl2_calc = 147.1 + 737.7 + 1450.7 + 2 * (121.7 - 348.6) + U_MgCl2
f_MgCl3 = 147.1 + 737.7 + 1450.7 + 7732.7 + 3 * (121.7 - 348.6) + U_MgCl3
print('dfH MgCl', round(f_MgCl), 'CaCl', round(f_CaCl), 'NeCl', round(f_NeCl), 'MgCl2 hitung', round(f_MgCl2_calc), '(ukur -641,3)', 'MgCl3', round(f_MgCl3))
print('2MgCl -> Mg + MgCl2 dH =', round(-641.3 - 2 * f_MgCl), ' 2CaCl -> Ca + CaCl2 dH =', round(-795.4 - 2 * f_CaCl))
# --- kelarutan: dH_lar = U(+) + hidrasi
hyd = {'Li': -519, 'Na': -404, 'K': -321, 'Rb': -296, 'Cs': -271, 'Ag': -464, 'F': -504, 'Cl': -361, 'Br': -330, 'I': -285}
Ul = {'LiF': 1049, 'NaF': 930, 'NaCl': 787, 'KCl': 717, 'NaI': 705, 'KI': 649, 'CsI': 604, 'LiI': 759, 'CsF': 744, 'AgCl': 918, 'AgF': 974, 'LiCl': 864}
for s in ['LiF', 'LiCl', 'LiI', 'NaF', 'NaCl', 'KCl', 'KI', 'CsF', 'CsI', 'AgF', 'AgCl']:
    c = s[:2] if s[:2] in hyd else s[:1]; a = s[len(c):]
    print('larut', s, Ul[s] + hyd[c] + hyd[a])
# --- karbonat: T dekomposisi dari dH, dS (1 bar CO2)
D = {'MgCO3': (-1095.8, 65.7), 'MgO': (-601.6, 26.9), 'CaCO3': (-1206.9, 92.9), 'CaO': (-635.1, 39.8), 'SrCO3': (-1220.1, 97.1), 'SrO': (-592.0, 54.4),
     'BaCO3': (-1216.3, 112.1), 'BaO': (-553.5, 70.4), 'CO2': (-393.5, 213.8)}
for m in ('Mg', 'Ca', 'Sr', 'Ba'):
    dH = D[m + 'O'][0] + D['CO2'][0] - D[m + 'CO3'][0]; dS = D[m + 'O'][1] + D['CO2'][1] - D[m + 'CO3'][1]
    print('karbonat', m, 'dH', round(dH, 1), 'dS', round(dS, 1), 'T', round(dH * 1000 / dS - 273.15), 'C')
for m in ('Mg', 'Ca', 'Sr', 'Ba'):
    dU = kap(2, 2, 2, rS[m] + 140) - kap(2, 2, 2, rS[m] + 178)
    print('selisih U(MO)-U(MCO3) Kapustinskii', m, round(dU))
