#!/usr/bin/env python3
# Angka Bab 11 Kimia Anorganik 1: senyawa koordinasi
import math
R=8.314; T=298.15; F=R*T*math.log(10)/1000
print('2,303RT kJ',F)
# Werner: AgCl dari 1,00 g CoCl3.nNH3
M={'Co':58.933,'Cl':35.453,'N':14.007,'H':1.008,'Ag':107.868}
NH3=M['N']+3*M['H']; AgCl=M['Ag']+M['Cl']
for n,free in [(6,3),(5,2),(4,1),(3,0)]:
    Mr=M['Co']+3*M['Cl']+n*NH3; print(f'CoCl3.{n}NH3 M={Mr:.2f} AgCl dari 1 g = {free*AgCl/Mr:.3f} g')
# CFSE (satuan Δo) dan P
def cfse_oct(n,ls):
    # isi t2g (-0.4) eg (+0.6)
    if ls: t=min(n,6); e=n-t
    else:
        t=min(n,3); e=min(n-t,2); r=n-t-e; t+=min(r,3); r-=min(r,3); e+=r
    pairs_ls=None
    return -0.4*t+0.6*e,t,e
def unp(t,e):
    up=lambda k,m: k if k<=m else 2*m-k
    return up(t,3)+up(e,2)
for n in range(11):
    h=cfse_oct(n,False); l=cfse_oct(n,True)
    tet_e=min(n,2) if n<=2 else (2 if n<=5 else min(n-3,4))
    # tetrahedral HS: e (-0.6Δt) dua orbital, t2 (+0.4Δt)
    e_=0;t2=0
    for k in range(n):
        if k<2: e_+=1
        elif k<5: t2+=1
        elif k<7: e_+=1
        else: t2+=1
    ct=-0.6*e_+0.4*t2
    print(f'd{n}: HS {h[0]:+.1f}Δo ({h[1]},{h[2]}) unp {unp(h[1],h[2])}; LS {l[0]:+.1f}Δo ({l[1]},{l[2]}) unp {unp(l[1],l[2])}; tet {ct:+.1f}Δt = {ct*4/9:+.2f}Δo')
# spin-only
for n in range(1,6): print('mu_so',n,math.sqrt(n*(n+2)))
# Ti3+
nu=20300; print('Ti3+ 20300 cm-1 ->',1e7/nu,'nm',nu*0.0119627,'kJ/mol')
# Spin tinggi/rendah
P={'Fe2+':19150,'Co3+':21000,'Fe3+':30000,'Mn2+':25500,'Co2+':22500}
for cx,ion,do in [('[Fe(H2O)6]2+','Fe2+',10400),('[Fe(CN)6]4-','Fe2+',32850),('[Co(NH3)6]3+','Co3+',22900),('[CoF6]3-','Co3+',13000),('[Fe(H2O)6]3+','Fe3+',13700),('[Mn(H2O)6]2+','Mn2+',7800)]:
    print(cx,do,'P',P[ion],'LS' if do>P[ion] else 'HS', 'kJ',do*0.0119627)
# CFSE kJ: [Fe(CN)6]4- LS d6: -2.4Δo+2P ; HS [Fe(H2O)6]2+: -0.4Δo
print('Fe(CN)6 4- CFSE -2,4Δo kJ',-2.4*32850*0.0119627,' net with 2P',(-2.4*32850+2*19150)*0.0119627)
print('Fe(H2O)6 2+ CFSE -0,4Δo kJ',-0.4*10400*0.0119627)
print('Co(NH3)6 3+ LS -2.4Δo+2P (cm-1)',-2.4*22900+2*21000,' vs HS -0.4Δo',-0.4*22900)
# Cr(III) deret spektrokimia
for L,v in [('Cl-',13600),('F-',15060),('H2O',17400),('NH3',21500),('en',21900),('CN-',26600)]: print('Cr',L,v,1e7/v,'nm')
# Irving-Williams log K1 en
# kelat Cd
for nm,lb,dH,dS in [('[Cd(NH2Me)4]',6.55,-57.3,-66.7),('[Cd(en)2]',10.62,-56.5,14.1)]:
    dG=dH-T*dS/1000; print(nm,'dG',dG,'logb dari dG',-dG/F,'(tabel',lb,') -TdS',-T*dS/1000)
print('Ni: log b6 NH3 8,61 dG',-8.61*F,' log b3 en 18,28 dG',-18.28*F,' selisih',(18.28-8.61)*F,'K',10**(18.28-8.61))
# CFSE oktahedral vs tetrahedral: preferensi situs oktahedral (OSPE) untuk spinel, Δt=4/9Δo
for n in (3,6,8):
    pass
# jari-jari M2+ Shannon KB6 spin tinggi

# --- OSPE spinel (satuan Δo; tetrahedral 4/9)
oct={4:-0.6,5:0,6:-0.4,8:-1.2,3:-1.2}; tet={4:-0.4*4/9,5:0,6:-0.6*4/9,8:-0.8*4/9,3:-0.8*4/9}
for nm,n in [('Fe2+ d6',6),('Fe3+ d5',5),('Mn2+ d5',5),('Mn3+ d4',4),('Ni2+ d8',8),('Cr3+ d3',3)]: print('OSPE',nm,oct[n]-tet[n])
# faktor statistik K_n/K_(n+1) untuk N=6
N=6; import math
for n in range(1,6):
    r=((N-n+1)/n)/((N-n)/(n+1)); print('K%d/K%d stat'%(n,n+1),r,'Δlog',math.log10(r))
# Ni(NH3)6 vs Ni(en)3 tukar
print('[Ni(NH3)6]+3en logK',18.28-8.61)
# Kontras konsentrasi efektif: en 0,1 M

# --- soal
c=0.0119627
print('Cr(H2O)6 EPMK kJ',-1.2*17400*c,' 575 nm')
print('[CoF6]3- HS EPMK kJ',-0.4*13000*c)
print('[Cr(NH3)6] lam',1e7/21500,'[Co(NH3)6]',1e7/22900)
for n in (1,3): print('mu',n,math.sqrt(n*(n+2)))
print('OSPE Co2+ d7', -0.8-(-1.2*4/9))
K=1.8e-10*10**7.21; print('AgCl+2NH3 K',K, 'sqrtK',math.sqrt(K)); s=math.sqrt(K)/(1+2*math.sqrt(K)); print('s di NH3 1 M',s)
n=12.5e-3*0.0100; cM=n/0.0500; print('kesadahan M',cM,'mg/L CaCO3',cM*100.09*1000)
print('Pb/Ca EDTA K',10**(18.04-10.65))
print('dG Ni(en)3',-18.28*F,' dG Cd en',-10.62*F)
print('Ag(NH3)2 dG',-7.21*F)
# AgCl dari 1 g [Cr(H2O)5Cl]Cl2.H2O : CrCl3.6H2O M
Mcr=51.996+3*35.453+6*18.015; print('CrCl3.6H2O M',Mcr,' AgCl 1 g, 2 Cl:',2*143.32/Mcr,' 3 Cl:',3*143.32/Mcr,' 1 Cl:',143.32/Mcr)
print('[Fe(H2O)6]3+ λ',1e7/13700)
print('Δo Co(NH3)6 kJ',22900*c)
