#!/usr/bin/env python3
"""Angka Bab 1 Kimia Anorganik 1 (dihitung sebelum ditulis)."""
from math import sqrt
R = 13.606  # eV
def slater(Z, conf, target):
    """conf: list (grup, jumlah) urut; grup: '1s','2sp','3sp','3d','4sp','4d'. target: grup elektron yang ditinjau."""
    order = [g for g, _ in conf]; t = order.index(target); S = 0.0
    n = lambda g: int(g[0])
    for i, (g, k) in enumerate(conf):
        if i > t: continue
        kk = k - 1 if g == target else k
        if g == target: S += kk * (0.30 if g == '1s' else 0.35)
        elif target.endswith('d') or target.endswith('f'): S += kk * 1.00
        elif n(g) == n(target) - 1: S += kk * 0.85
        elif n(g) < n(target) - 1: S += kk * 1.00
        else: S += kk * 0.35  # sama n tetapi grup d lebih dalam? tidak terjadi untuk target sp
    return S, Z - S
print('== Slater')
cases = {
 'Li 2s': (3, [('1s',2),('2sp',1)], '2sp'), 'C 2p': (6, [('1s',2),('2sp',4)], '2sp'), 'N 2p': (7, [('1s',2),('2sp',5)], '2sp'),
 'O 2p': (8, [('1s',2),('2sp',6)], '2sp'), 'F 2p': (9, [('1s',2),('2sp',7)], '2sp'), 'Ne 2p': (10, [('1s',2),('2sp',8)], '2sp'),
 'Na 3s': (11, [('1s',2),('2sp',8),('3sp',1)], '3sp'), 'Cl 3p': (17, [('1s',2),('2sp',8),('3sp',7)], '3sp'),
 'K 4s': (19, [('1s',2),('2sp',8),('3sp',8),('4sp',1)], '4sp'), 'K 3d (hipotetis)': (19, [('1s',2),('2sp',8),('3sp',8),('3d',1)], '3d'),
 'Zn 4s': (30, [('1s',2),('2sp',8),('3sp',8),('3d',10),('4sp',2)], '4sp'), 'Zn 3d': (30, [('1s',2),('2sp',8),('3sp',8),('3d',10),('4sp',2)], '3d'),
 'Fe 4s': (26, [('1s',2),('2sp',8),('3sp',8),('3d',6),('4sp',2)], '4sp'), 'Fe 3d': (26, [('1s',2),('2sp',8),('3sp',8),('3d',6),('4sp',2)], '3d'),
}
for k, (Z, c, t) in cases.items():
    S, Ze = slater(Z, c, t); print(f'  {k}: S = {S:.2f}, Zeff = {Ze:.2f}')
# Zn 4s: grup 3d dihitung 0,85 (n-1) -> periksa manual
print('  Zn 4s manual: S = 0.35 + 18*0.85 + 10*1 =', 0.35 + 18*0.85 + 10, '-> Zeff', 30 - (0.35 + 18*0.85 + 10))
print('  periode 2 Zeff(2p) C..Ne:', [round(Z - (1.70 + (Z - 3) * 0.35), 2) for Z in range(6, 11)])
print('  periode 3 Zeff(3p) Al..Ar:', [round(Z - (2 + 6.8 + (Z - 11) * 0.35), 2) for Z in range(13, 19)])
print('== Zeff dari spektrum: Zeff = n*sqrt(IE/R)')
for nama, n, IE in [('Li 2s', 2, 5.392), ('Li 2p', 2, 5.392 - 1.848), ('Na 3s', 3, 5.139), ('Na 3p', 3, 5.139 - 2.104), ('Na 3d', 3, 5.139 - 3.617)]:
    print(f'  {nama}: energi ikat {IE:.3f} eV, Zeff = {n*sqrt(IE/R):.2f}')
print('  Li 2p eksitasi 670.8 nm ->', round(1239.84/670.8, 3), 'eV; Na 589.0 nm ->', round(1239.84/589.0, 3), 'eV; Na 3d 29172.8 cm-1 ->', round(29172.8/8065.54, 3), 'eV')
print('== hidrogenik: He+ IE =', round(R*4, 1), 'eV; Li2+ =', round(R*9, 1), 'eV; H n=2 ->', round(R/4, 2))
print('== Pauling HCl: D(HH)=436, D(ClCl)=242, D(HCl)=432')
Dg = sqrt(436*242); d = 432 - Dg; print(f'  rata geometrik {Dg:.1f}, Delta {d:.1f}, dchi = {0.102*sqrt(d):.2f} (tabel 0.96)')
Da = (436+242)/2; d2 = 432 - Da; print(f'  rata aritmetik {Da:.1f}, Delta {d2:.1f}, dchi = {0.102*sqrt(d2):.2f}')
print('  HF: D(HH)=436,D(FF)=159,D(HF)=570:', end=' '); Dg = sqrt(436*159); print(f'Delta {570-Dg:.1f}, dchi {0.102*sqrt(570-Dg):.2f} (tabel {3.98-2.20:.2f})')
print('== Mulliken chi_P ~ 0.187(IE+EA)+0.17')
for e, I, A, P in [('F', 17.423, 3.401, 3.98), ('Cl', 12.968, 3.613, 3.16), ('Br', 11.814, 3.364, 2.96), ('I', 10.451, 3.059, 2.66), ('O', 13.618, 1.461, 3.44), ('C', 11.260, 1.262, 2.55), ('Na', 5.139, 0.548, 0.93), ('H', 13.598, 0.754, 2.20)]:
    m = (I + A)/2; print(f'  {e}: chi_M = {m:.2f} eV -> {0.187*(I+A)+0.17:.2f} (Pauling {P})')
print('== Allred-Rochow chi = 0.744 + 3590 Zeff/r^2 (Zeff = Z - S dengan semua elektron valensi)')
for e, Z, S, r, ar in [('C', 6, 1.70 + 4*0.35, 77, 2.50), ('N', 7, 1.70 + 5*0.35, 75, 3.07), ('O', 8, 1.70 + 6*0.35, 73, 3.50), ('F', 9, 1.70 + 7*0.35, 72, 4.10),
                       ('Si', 14, 2 + 6.8 + 4*0.35, 117, 1.74), ('Cl', 17, 2 + 6.8 + 7*0.35, 99, 2.83)]:
    Ze = Z - S; print(f'  {e}: Zeff {Ze:.2f}, r {r} pm -> chi {0.744 + 3590*Ze/r**2:.2f} (tabel A-R {ar})')
print('== kerapatan muatan / daya mempolarisasi z/r^2 (Shannon KB6, pm)')
for ion, z, r in [('Li+', 1, 76), ('Na+', 1, 102), ('K+', 1, 138), ('Cs+', 1, 167), ('Be2+ (KB4)', 2, 27), ('Mg2+', 2, 72), ('Ca2+', 2, 100), ('Al3+', 3, 53.5), ('Ag+', 1, 115)]:
    print(f'  {ion}: z/r = {1000*z/r:.1f} x10^-3 pm^-1, z/r^2 = {1e4*z/r**2:.2f} x10^-4')
print('== isoelektronik Ne (pm):', {'O2-': 140, 'F-': 133, 'Na+': 102, 'Mg2+': 72, 'Al3+': 53.5})
print('   rasio jari-jari Na+/F-:', round(102/133, 2))
print('== kenaikan energi ionisasi berurutan Mg (eV): 7.646, 15.035, 80.144 -> rasio I3/I2 =', round(80.144/15.035, 2))
print('   Al: 5.986, 18.829, 28.448, 119.99 -> I4/I3 =', round(119.99/28.448, 2))
print('   eV -> kJ/mol: 1 eV =', 96.485, '; IE1 Na', round(5.139*96.485), 'kJ/mol; Cl EA', round(3.613*96.485), 'kJ/mol')
print('   Na + Cl -> Na+ + Cl- (gas):', round((5.139 - 3.613)*96.485), 'kJ/mol (positif)')
print('== efek pasangan inert: jumlah IE (eV) untuk melepas ns2 (I2+I3):')
for e, I2, I3 in [('Al', 18.829, 28.448), ('Ga', 20.515, 30.726), ('In', 18.870, 28.044), ('Tl', 20.428, 29.852)]:
    print(f'  {e}: {I2 + I3:.2f} eV = {round((I2+I3)*96.485)} kJ/mol')
print('== kelimpahan kerak (massa %): O 46.1, Si 28.2, Al 8.23, Fe 5.63, Ca 4.15, Na 2.36, Mg 2.33, K 2.09 -> total', round(46.1+28.2+8.23+5.63+4.15+2.36+2.33+2.09, 2))
print('== energi ikatan X-X (kJ/mol): F2 159, Cl2 243, Br2 193, I2 151; N≡N 945 lawan 3x N-N 160 =', 3*160, '; P≡P 490? lawan 3x P-P 201 =', 3*201)
