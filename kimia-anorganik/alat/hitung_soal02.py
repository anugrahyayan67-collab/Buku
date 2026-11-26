#!/usr/bin/env python3
from math import cos, radians
D=3.33564e-30; e=1.602177e-19
print('q HBr', round(0.827*D/(e*141.4e-12),3), 'HI', round(0.448*D/(e*160.9e-12),3), 'CO', round(0.110*D/(e*112.8e-12),3))
print('mu dari q=1, d=100 pm (D):', round(e*100e-12/D,2))
print('mu NaCl gas jika ionik penuh d=236 pm:', round(e*236e-12/D,1), 'D; terukur 9.0 D ->', round(9.0/(e*236e-12/D)*100), '% ionik')
for nm, th in [('NH3',106.7),('H2S',92.1),('PH3',93.3),('120',120),('NF3',102.2),('OF2',103.1)]:
    c=-cos(radians(th)); a=c/(1+c); print(f'  {nm}: s = {100*a:.1f} %')
print('H2+F2', 436+159-2*570, '; H2+Cl2', 436+243-2*432, '; C2H4+H2', 614+436-(347+2*413), '(data -137)')
print('H2O2 -> H2O + 1/2 O2', 2*463+146 - (2*463 + 498/2))
print('N2H4 + O2 -> N2 + 2H2O', 160+4*391+498-(945+4*463))
print('2 H2 + O2 -> 2 H2O(g)', 2*436+498-4*463, '(data -484)')
print('CO2 C=O 799 vs C≡O 1072')
