#!/usr/bin/env python3
"""Bab 4: energi orbital HF (teorema Koopmans) untuk molekul contoh, dan pindaian Walsh H2O."""
import numpy as np, json, sys
from pyscf import gto, scf
HA = 27.211386
def hit(atom, basis='cc-pvdz', spin=0, unit='Angstrom'):
    m = gto.M(atom=atom, basis=basis, spin=spin, symmetry=True, unit=unit, verbose=0)
    mf = (scf.ROHF(m) if spin else scf.RHF(m)); mf.kernel()
    lab = mf.get_orbsym() if hasattr(mf, 'get_orbsym') else None
    from pyscf import symm
    irr = symm.label_orb_symm(m, m.irrep_name, m.symm_orb, mf.mo_coeff)
    occ = mf.mo_occ
    return [(irr[i], round(mf.mo_energy[i] * HA, 2), float(occ[i])) for i in range(len(occ)) if mf.mo_energy[i] * HA < 15]
MOL = {
 'N2': 'N 0 0 0; N 0 0 1.098',
 'F2': 'F 0 0 0; F 0 0 1.412',
 'CO': 'C 0 0 0; O 0 0 1.128',
 'HF': 'H 0 0 0; F 0 0 0.917',
 'H2O': 'O 0 0 0; H 0 0.7572 0.5865; H 0 -0.7572 0.5865',
 'NH3': 'N 0 0 0.1173; H 0 0.9377 -0.2737; H 0.8121 -0.4689 -0.2737; H -0.8121 -0.4689 -0.2737',
 'CH4': 'C 0 0 0; H 0.6276 0.6276 0.6276; H -0.6276 -0.6276 0.6276; H -0.6276 0.6276 -0.6276; H 0.6276 -0.6276 -0.6276',
 'BeH2': 'Be 0 0 0; H 0 0 1.326; H 0 0 -1.326',
 'CO2': 'C 0 0 0; O 0 0 1.160; O 0 0 -1.160',
}
out = {}
for k, a in MOL.items():
    out[k] = hit(a); print(k, [x for x in out[k] if x[2] > 0][-6:], 'LUMO', [x for x in out[k] if x[2] == 0][:2])
out['O2'] = hit('O 0 0 0; O 0 0 1.208', spin=2); print('O2', out['O2'][-10:])
# B2H6: geometri eksperimen (D2h), B–B 1,763; B–Ht 1,19; B–Hb 1,33
bb = 1.763 / 2; hb = np.sqrt(1.33**2 - bb**2)
ang = np.radians(121.5 / 2); bht = 1.19
geo = f'B {bb} 0 0; B {-bb} 0 0; H 0 0 {hb}; H 0 0 {-hb}; ' + '; '.join(f'H {s*(bb+bht*np.cos(ang))} {t*bht*np.sin(ang)} 0' for s in (1, -1) for t in (1, -1))
out['B2H6'] = hit(geo); print('B2H6', [x for x in out['B2H6'] if x[2] > 0])
# pindaian Walsh H2O (O–H 0,958 Å)
w = {}
for th in range(90, 181, 5):
    t = np.radians(th / 2); r = 0.958
    m = gto.M(atom=f'O 0 0 0; H 0 {r*np.sin(t)} {-r*np.cos(t)}; H 0 {-r*np.sin(t)} {-r*np.cos(t)}', basis='cc-pvdz', verbose=0)
    mf = scf.RHF(m); e = mf.kernel()
    w[th] = {'E': e * HA, 'orb': [round(x * HA, 3) for x in mf.mo_energy[1:6]]}
emin = min(v['E'] for v in w.values())
for th in w: w[th]['Erel_kJ'] = round((w[th]['E'] - emin) * 96.485, 1)
print('Walsh', {k: (v['orb'], v['Erel_kJ']) for k, v in w.items() if k % 15 == 0})
# sudut optimum (parabola di sekitar minimum)
ths = np.array(sorted(w)); E = np.array([w[t]['E'] for t in ths]); i = E.argmin(); p = np.polyfit(ths[i-2:i+3], E[i-2:i+3], 2)
print('sudut optimum HF/cc-pVDZ', round(-p[1] / 2 / p[0], 1), 'penghalang linear kJ/mol', w[180]['Erel_kJ'])
json.dump({'orb': out, 'walsh': w}, open(sys.argv[1] if len(sys.argv) > 1 else '/tmp/bab04.json', 'w'))
