#!/usr/bin/env python3
"""Angka Bab 10: Coulomb dalam pelarut, jarak Bjerrum, Born, Kw(T), CO2 superkritis."""
import numpy as np
NA, e, eps0, kB = 6.02214076e23, 1.602176634e-19, 8.8541878128e-12, 1.380649e-23
K = NA * e**2 / (4 * np.pi * eps0) * 1e12 / 1000  # kJ/mol pm
print('== energi pasangan Na+Cl- 282 pm')
for nm, eps in [('vakum', 1), ('heksana', 1.9), ('THF', 7.6), ('NH3 cair', 22.4), ('metanol', 32.7), ('asetonitril', 37.5), ('DMSO', 46.7), ('air', 78.4), ('HF cair', 84), ('H2SO4', 100)]:
    print(nm, eps, round(K / 282 / eps, 1))
print('kT 298 kJ/mol', round(kB * 298.15 * NA / 1000, 2))
for nm, eps, T in [('air', 78.4, 298.15), ('NH3', 22.4, 240), ('THF', 7.6, 298.15), ('heksana', 1.9, 298.15)]:
    q = e**2 / (8 * np.pi * eps0 * eps * kB * T) * 1e12; print('Bjerrum', nm, round(q), 'pm')
print('== Born: dG = -(K/2) z^2/r (1 - 1/eps), r = r_Shannon + 85 pm')
for nm, z, r, ex in [('Li+', 1, 76, -481), ('Na+', 1, 102, -375), ('K+', 1, 138, -304), ('Mg2+', 2, 72, -1838), ('Al3+', 3, 53.5, -4531)]:
    for eps, sv in [(78.4, 'air')]:
        print(nm, sv, round(-K / 2 * z * z / (r + 85) * (1 - 1 / eps)), 'eksp ΔhidG', ex)
print('Born Na+ dalam NH3 (eps 22.4) vs air', round(-K / 2 / 187 * (1 - 1 / 22.4)), round(-K / 2 / 187 * (1 - 1 / 78.4)))
print('== Kw terhadap suhu (data), pH netral')
for T, pKw in [(0, 14.94), (25, 14.00), (37, 13.62), (50, 13.26), (75, 12.70), (100, 12.26)]:
    print(T, pKw, 'pH netral', round(pKw / 2, 2))
# dH ionisasi dari van 't Hoff 25->50
R = 8.314; dH = -R * np.log(10**-13.26 / 10**-14.00) / (1 / 323.15 - 1 / 298.15); print('dH autoionisasi', round(dH / 1000, 1), 'kJ/mol')
print('== H2SO4 autoprotolisis K = 2.7e-4: [H3SO4+]=[HSO4-] =', '%.3f' % np.sqrt(2.7e-4) , 'mol/kg (molalitas ~ per kg)')
print('== NH3 cair: K ~ 1e-27 -> [NH4+] =', '%.1e' % np.sqrt(1e-27))
# elektron tersolvasi: serapan ~0,8 eV -> lambda
print('serapan e-(am) 0,8 eV ->', round(1239.84 / 0.8), 'nm')
# CO2 superkritis
print('CO2 kritis 31,0 C 73,8 bar; air 374 C 221 bar')
# HF leveling: HF sebagai pelarut, asam? Born dll selesai

# --- tambahan untuk contoh soal
import math
print('Fe3+ hidrolisis pKa 2,2, 0,10 M:')
Ka=10**-2.2; c=0.10; x=(-Ka+math.sqrt(Ka*Ka+4*Ka*c))/2; print(' [H+]',x,'pH',-math.log10(x))
print('AgCl Ksp 1,8e-10 s =',math.sqrt(1.8e-10),'; dalam NaCl 0,10 M s =',1.8e-10/0.1)
print('H2SO4 [H3SO4+] =',math.sqrt(2.7e-4))
Kf=6.12
for i in (1,2,4): print(' kriosk H2SO4 i',i,'dT',i*Kf*0.05)
print('DN DMSO kJ',29.8*4.184,'air',18.0*4.184,'MeCN',14.1*4.184)
print('rho ideal CO2 40C 100bar',100e5*0.04401/(8.314*313.15))
def kap(r): return 107900*2/r*(1-34.5/r)
print('Kapustinskii NaCl 283',kap(283),' BMIM BF4 330+232',kap(562), ' rasio',kap(562)/kap(283))
# NH3: elektron tersolvasi energi foton puncak
print('1550 nm ->',1239.84/1550,'eV')
# Bjerrum pada etanol 24.6 dan DMSO
for e in (24.6,46.7,37.5): print('Bjerrum',e,1.671e5/(e*298.15)*1e-0, 'pm (q=1)')

# --- soal akhir bab
import math
C=1.389e5/2
print('Born Cs+',-C/(167+85)*(1-1/78.4),' F-',-C/(133+10)*(1-1/78.4))
print('Born Na transfer air->heksana',C/187*((1-1/78.4)-(1-1/1.9)))
print('pasangan MgO air d=212',4*2*C/212/78.4)
print('Bjerrum MeCN',357*78.4/37.5)
print('eps agar E=4RT',492.7/(4*2.48))
print('Kw 60C',1e-14*math.exp(-55800/8.314*(1/333.15-1/298.15)), 'pKw',-math.log10(1e-14*math.exp(-55800/8.314*(1/333.15-1/298.15))))
print('CaF2 s',(3.5e-11/4)**(1/3),' dalam NaF 0,010',3.5e-11/1e-4)
print('BaSO4/SrSO4',1.1e-10/0.01,3.4e-7/0.01,1.1e-10/3.4e-5, 1.1e-10/3.4e-5/0.01*100,'%')
o=math.sqrt(5.6e-12/0.010); print('Mg(OH)2 pH',14+math.log10(o))
hb=3.81  # eV A^2 = hbar^2/2m
R=math.sqrt(hb*(4.4934**2-math.pi**2)/0.8); print('bola R (A)',R)
print('E foton 1550 nm kJ/mol',0.8*96.485)
print('KHSO4 0,10 -> [H3SO4+]',2.7e-4/0.10)
Q=3*96485*1000/26.98; print('Al 1 kg muatan',Q,'Ah',Q/3600,'kWh @4,2V',Q*4.2/3.6e6)
print('Na per 1000 Ah kg',3.6e6/96485*22.99/1000)
print('EMIM BF4 U',1.2025e5*2/532*(1-34.5/532))
print('DES fraksi massa ChCl',139.62/(139.62+2*60.06))
print('CO2 ideal 35C 80bar',80e5*0.04401/(8.314*308.15))
print('krio: 0,040 asetat i2',2*6.12*0.04,' B(OH)3 0,020',6*6.12*0.02)
print('foton dari pita 0,8 eV: kJ/mol',0.8*96.485)
