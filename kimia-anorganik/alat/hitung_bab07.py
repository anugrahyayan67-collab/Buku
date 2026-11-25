#!/usr/bin/env python3
"""Angka Bab 7: rantai Hückel -> pita, energi Fermi, pembawa intrinsik, doping, donor hidrogenik, celah -> warna, Hume-Rothery."""
import numpy as np
h, hbar, me, e, kB, NA = 6.62607e-34, 1.054572e-34, 9.10938e-31, 1.602177e-19, 1.380649e-23, 6.02214e23
print('== rantai N atom: E_k = 2 cos(k pi/(N+1)) (satuan beta), lebar pita')
for N in (2, 3, 4, 6, 10, 100, 10**6):
    k = np.arange(1, min(N, 2000) + 1); E = 2 * np.cos(k * np.pi / (N + 1))
    print(N, 'lebar', round(2 * np.cos(np.pi / (N + 1)) * 2, 4), 'jarak terdekat', '%.2e' % (2 * (np.cos(np.pi / (N + 1)) - np.cos(2 * np.pi / (N + 1)))))
print('== energi Fermi model elektron bebas')
for nm, z, Z, a in [('Na bcc', 1, 2, 429.1), ('K bcc', 1, 2, 532.8), ('Cu fcc', 1, 4, 361.5), ('Ag fcc', 1, 4, 408.6), ('Al fcc', 3, 4, 404.95), ('Mg hcp', 2, 2, None)]:
    if a is None: V = 2 * (np.sqrt(3) / 2 * 320.9**2 * 521.0) * 1e-36 / 2 * 2 / 2; n = 2 * 2 / (np.sqrt(3) / 2 * (320.9e-12)**2 * 521.0e-12)
    else: n = z * Z / (a * 1e-12)**3
    EF = hbar**2 / (2 * me) * (3 * np.pi**2 * n)**(2 / 3) / e; TF = EF * e / kB; vF = np.sqrt(2 * EF * e / me)
    print(nm, 'n=%.2e m-3' % n, 'EF=%.2f eV' % EF, 'TF=%.1e K' % TF, 'vF=%.2e m/s' % vF)
print('kT 300 K =', round(kB * 300 / e, 4), 'eV')
print('== Fermi-Dirac: f di E-EF = 0.1, 0.2, 0.5 eV pada 300 K')
for d in (0.05, 0.1, 0.2, 0.5): print(d, '%.2e' % (1 / (np.exp(d * e / (kB * 300)) + 1)))
print('== pembawa intrinsik n_i = sqrt(Nc Nv) exp(-Eg/2kT) (300 K)')
sem = {'Si': (1.12, 2.8e19, 1.04e19), 'Ge': (0.66, 1.04e19, 6.0e18), 'GaAs': (1.42, 4.7e17, 7.0e18), 'intan': (5.47, 1.0e19, 1.0e19)}
for s, (Eg, Nc, Nv) in sem.items():
    for T in (300,):
        ni = np.sqrt(Nc * Nv) * np.exp(-Eg * e / (2 * kB * T)); print(s, 'Eg', Eg, 'ni=%.1e cm-3' % ni)
Eg = 1.12
for T in (300, 350, 400, 500):
    print('Si T', T, 'ni ratio vs 300K', '%.1f' % (np.exp(-Eg * e / (2 * kB * T)) / np.exp(-Eg * e / (2 * kB * 300)) * (T / 300)**1.5))
print('== konduktivitas')
nSi = 8 / (5.431e-8)**3; print('atom Si per cm3 %.2e' % nSi)
ni = 1.0e10; mue, muh = 1400, 450
sig_i = ni * e * (mue + muh); print('sigma intrinsik Si %.2e S/cm' % sig_i, 'resistivitas %.2e ohm cm' % (1 / sig_i))
for ppm in (1, 0.01):
    nd = nSi * ppm * 1e-6; s = nd * e * mue; print('doping', ppm, 'ppm: n=%.1e' % nd, 'sigma %.2e S/cm' % s, 'faktor %.1e' % (s / sig_i), 'p=%.1e' % (ni**2 / nd))
print('Cu sigma 5.96e5 S/cm')
print('== donor hidrogenik di Si: m*=0.26, eps=11.7')
for nm, ms, eps in [('Si', 0.26, 11.7), ('Ge', 0.12, 16.0), ('GaAs', 0.067, 12.9)]:
    print(nm, 'E_ikat %.1f meV' % (13.606 * ms / eps**2 * 1000), 'jari-jari %.1f nm' % (0.0529 * eps / ms))
print('== celah -> lambda = 1239.84/Eg')
for nm, Eg in [('intan', 5.47), ('ZnS', 3.68), ('GaN', 3.4), ('ZnO', 3.37), ('TiO2 anatas', 3.2), ('TiO2 rutil', 3.0), ('InGaN biru', 2.7), ('CdS', 2.42), ('HgS', 2.0), ('GaP', 2.26), ('CdSe', 1.74), ('GaAs', 1.42), ('Si', 1.12), ('Ge', 0.66), ('PbS', 0.37)]:
    print(nm, Eg, round(1239.84 / Eg), 'nm')
print('== Hume-Rothery')
r = {'Cu': 128, 'Ni': 124, 'Ag': 144, 'Au': 144, 'Zn': 134, 'Fe': 126, 'C': 77, 'Pd': 137}
for a, b in [('Cu', 'Ni'), ('Cu', 'Ag'), ('Ag', 'Au'), ('Cu', 'Zn')]: print(a, b, '%.1f %%' % (100 * abs(r[a] - r[b]) / r[a]))
print('C/Fe', round(77 / 126, 2), 'rongga Oh fcc r/R 0.414 -> r maks', round(0.414 * 129, 1))
for nm, ea in [('CuZn beta', (1 + 2) / 2), ('Cu5Zn8 gamma', (5 + 16) / 13), ('CuZn3 epsilon', (1 + 6) / 4), ('Cu5Sn', (5 + 4) / 6), ('Cu31Sn8', (31 + 32) / 39), ('Cu3Sn', (3 + 4) / 4)]: print(nm, round(ea, 3))
