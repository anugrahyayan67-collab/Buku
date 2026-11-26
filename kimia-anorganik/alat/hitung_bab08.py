#!/usr/bin/env python3
"""Angka Bab 8: ΔG–T NH4Cl, Ka, aturan Pauling, asam aqua, kekerasan Pearson, Drago–Wayland."""
import numpy as np
R = 8.314
print('== NH3(g) + HCl(g) -> NH4Cl(s)')
dH = -314.4 - (-45.9) - (-92.3); dS = 94.6 - 192.8 - 186.9
print('dH', round(dH, 1), 'dS', round(dS, 1), 'T(dG=0)', round(dH * 1000 / dS, 0), 'K', round(dH * 1000 / dS - 273.15), 'C', ' dG298', round(dH - 298.15 * dS / 1000, 1))
print('RT ln10 pada 298 K =', round(R * 298.15 * np.log(10) / 1000, 2), 'kJ/mol')
print('== disosiasi 0,10 M HF (pKa 3,17) dan HOCl (7,53)')
for nm, pKa in [('HF', 3.17), ('HOCl', 7.53), ('CH3COOH', 4.76)]:
    Ka = 10**-pKa; c = 0.10; x = (-Ka + np.sqrt(Ka**2 + 4 * Ka * c)) / 2
    print(nm, 'pH', round(-np.log10(x), 2), 'alfa %', round(100 * x / c, 2))
print('== aturan Pauling pKa1 = 8 - 5p')
ok = [('HOCl', 0, 7.53), ('HClO2', 1, 1.96), ('HClO3', 2, -1.0), ('HClO4', 3, -10), ('H3PO4', 1, 2.15), ('H3PO3', 1, 1.3), ('H3PO2', 1, 1.2), ('H2SO4', 2, -3), ('H2SO3', 1, 1.86), ('HNO3', 2, -1.4), ('HNO2', 1, 3.25), ('H3BO3', 0, 9.24), ('H4SiO4', 0, 9.8), ('H3AsO4', 1, 2.26), ('H5IO6', 1, 3.29), ('HOI', 0, 10.6), ('HOBr', 0, 8.65), ('H2SeO4', 2, -2), ('H2CO3*', 1, 3.6)]
for nm, p, pk in ok: print(nm, p, 8 - 5 * p, pk)
print('== asam aqua: pKa vs z^2/r (r Shannon KB6, pm)')
aq = [('Na+', 1, 102, 14.8), ('Ca2+', 2, 100, 12.8), ('Mg2+', 2, 72, 11.4), ('Zn2+', 2, 74, 9.0), ('Fe2+', 2, 78, 9.5), ('Cu2+', 2, 73, 7.5), ('Al3+', 3, 53.5, 5.0), ('Cr3+', 3, 61.5, 4.0), ('Fe3+', 3, 64.5, 2.2), ('Hg2+', 2, 102, 3.4), ('Sc3+', 3, 74.5, 4.3), ('Be2+', 2, 45, 5.7)]
for nm, z, r, pk in aq: print(nm, round(100 * z * z / r, 2), pk)
print('== kekerasan absolut eta = (I - A)/2 (eV)')
# kation M^z+: (I_{z+1} - I_z)/2 ; anion X-: (I(X) - A(X))/2
IE = {'Li': (5.392, 75.640), 'Na': (5.139, 47.286), 'K': (4.341, 31.63), 'Mg': (7.646, 15.035, 80.144), 'Ca': (6.113, 11.872, 50.91), 'Al': (5.986, 18.829, 28.448, 119.99),
      'Ag': (7.576, 21.48), 'Cu': (7.726, 20.292), 'Hg': (10.438, 18.757, 34.2), 'Fe': (7.902, 16.199, 30.651, 54.91), 'Zn': (9.394, 17.964, 39.72), 'Au': (9.226, 20.20), 'Tl': (6.108, 20.428), 'Pb': (7.417, 15.032, 31.94), 'Cd': (8.994, 16.908, 37.48)}
eta = {}
for m, z in [('Li', 1), ('Na', 1), ('K', 1), ('Mg', 2), ('Ca', 2), ('Al', 3), ('Fe', 3), ('Fe', 2), ('Zn', 2), ('Cd', 2), ('Hg', 2), ('Pb', 2), ('Cu', 1), ('Ag', 1), ('Au', 1), ('Tl', 1)]:
    I = IE[m]; eta[f'{m}{z}+'] = round((I[z] - I[z - 1]) / 2, 1)
for x, (I, A) in {'F': (17.423, 3.401), 'Cl': (12.968, 3.613), 'Br': (11.814, 3.364), 'I': (10.451, 3.059), 'OH': (13.02, 1.83), 'H': (13.598, 0.754), 'SH': (10.42, 2.32), 'CN': (14.0, 3.86)}.items():
    eta[x + '-'] = round((I - A) / 2, 1)
print(eta)
print('== Drago–Wayland -dH = EA EB + CA CB (kkal/mol)')
A = {'I2': (1.00, 1.00), 'fenol': (4.33, 0.442), 'BF3': (9.88, 1.62)}
B = {'NH3': (1.36, 3.46), 'piridina': (1.17, 6.40), 'Me3N': (0.808, 11.54), 'Et2O': (0.963, 3.25), 'aseton': (0.987, 2.33), 'DMSO': (1.34, 2.85), 'etil asetat': (0.975, 1.74)}
for a, (EA, CA) in A.items():
    print(a, {b: round(EA * EB + CA * CB, 2) for b, (EB, CB) in B.items()})
print('kkal->kJ 4.184; I2-piridina', round((1.17 + 6.40) * 4.184, 1), 'kJ')

# === pendalaman (revisi 2) ===
import math
F=5.708
print('== siklus HX(aq) -> H+(aq) + X-(aq), entalpi (kJ/mol)')
dat={'HF':(48,570,328,504,3.17),'HCl':(18,432,349,361,-6),'HBr':(21,366,325,330,-9),'HI':(23,298,295,285,-10)}
for k,(dh,D,EA,hx,pka) in dat.items():
    H=dh+D+1312-EA-1091-hx; G=F*pka
    print(k,'dehid',dh,'D',D,'IE 1312','-EA',-EA,'hidH+ -1091','hidX',-hx,'=> dH',H,' dG(pKa)',round(G,1),' -TdS',round(G-H,1))
print('== spesiasi H3PO4 pada pH 7,4')
pk=[2.15,7.20,12.35]
def frac(pH):
    h=10**-pH; K=[10**-p for p in pk]
    t=[h**3,h**2*K[0],h*K[0]*K[1],K[0]*K[1]*K[2]]; s=sum(t); return [x/s for x in t]
for pH in (2.15,4.7,7.2,7.4,9.8,12.35): print(pH,[round(x,4) for x in frac(pH)])
print('rasio HPO4/H2PO4 pH 7,4',10**(7.4-7.2))
print('== pH air hujan murni (CO2 420 ppm)')
KH=0.033; p=420e-6; Ka1=10**-6.35; h=math.sqrt(KH*p*Ka1); print('[H+]',h,'pH',-math.log10(h))
print('== pengendapan selektif Fe(OH)3/Mg(OH)2, 0,010 M')
for nm,ksp,n in [('Fe(OH)3',2.8e-39,3),('Mg(OH)2',5.6e-12,2)]:
    oh=(ksp/0.010)**(1/n); print(nm,'pH mulai',14+math.log10(oh)); oh2=(ksp/1e-5)**(1/n); print('  pH 99,9 % mengendap',14+math.log10(oh2))
print('== Hammett: indikator pK -10,1, rasio BH+/B = 10 ->',-10.1-1)
print('== zeolit ZSM-5 Si/Al 15: situs mmol/g',1/16/ (60.08*15/16+ (26.98+2*16+1.008)/16 )*1000)
print('ZSM-5 sel satuan 96 T: Al per sel', 96/16)
print('== buffer asetat 0,10/0,10 + 0,010 HCl')
pKa=4.76; print('pH',pKa+math.log10(0.09/0.11))
print('== pKa H3O+: -log(55,5)',-math.log10(55.5))
