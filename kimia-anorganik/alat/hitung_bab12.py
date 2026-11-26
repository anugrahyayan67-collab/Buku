#!/usr/bin/env python3
# Angka Bab 12 Kimia Anorganik 1: hidrogen dan gas mulia
import math
R=8.314; h=6.62607e-34; c=2.99792e10; kB=1.380649e-23; NA=6.02214e23
cm=h*c*NA/1000  # kJ/mol per cm-1
print('1 cm-1 = kJ/mol',cm)
# ZPE H2, D2
for nm,w in [('H2',4401.2),('HD',3813.1),('D2',3115.5)]: print(nm,'ZPE kJ',0.5*w*cm)
print('D0 H2 432,07 D2 439,6 selisih',439.6-432.07)
# KIE C-H vs C-D (regang 2900 / 2100)
dz=0.5*(2900-2900/math.sqrt(2))*cm; print('ΔZPE C-H/C-D kJ',dz,' kH/kD 298 K',math.exp(dz*1000/(R*298.15)))
# orto/para
B=60.853
def fpara(T):
    pa=sum((2*J+1)*math.exp(-B*J*(J+1)*1.4388/T) for J in range(0,30,2))
    o=3*sum((2*J+1)*math.exp(-B*J*(J+1)*1.4388/T) for J in range(1,30,2))
    return pa/(pa+o)
for T in (20.3,50,77,100,150,200,298.15,500): print('para',T,fpara(T))
print('energi orto->para per mol (J=1->0) kJ',2*B*cm,' kalor uap H2 0,90 kJ/mol')
# Massa isotop dan kelimpahan
print('D/H 156 ppm; T paruh 12,32 th')
# Produksi
print('SMR stoikiometri CH4+2H2O->CO2+4H2: kg CO2/kg H2',44.01/(4*2.016))
for V in (1.23,1.48,1.9): print('elektrolisis',V,'V kWh/kg',(1000/2.016)*2*96485*V/3.6e6)
print('HHV kWh/kg',285.83/2.016,'MJ/kg -> ',285.83/2.016*1000/3600,'kWh'); print('LHV MJ/kg',241.83/2.016)
# kerapatan energi
LHV=241.83/2.016  # MJ/kg
for nm,rho in [('700 bar',40.2),('cair',70.8)]: print(nm,'MJ/L',LHV*rho/1000)
print('bensin MJ/L',44.4*0.745,'metanol',19.9*0.792)
Mla=138.905+5*58.693; MH=Mla+6*1.008; wt=6*1.008/MH; print('LaNi5H6 %massa H',wt*100,'MJ/kg',wt*LHV)
rhoLa=8.3/Mla*6*1.008*1000; print('LaNi5H6 kg H/m3 (anggap volume paduan)',rhoLa,'MJ/L',rhoLa*LHV/1000)
# Pd menyerap H
Pd=12.02/106.42; nH=0.7*Pd; V=nH/2*22.414e3; print('Pd H/Pd 0,7: mol Pd/cm3',Pd,'mL H2(STP) per cm3',V)
# Hidrat metana
M=16.043+5.75*18.015; n=910000/M; print('hidrat CH4 penuh: mol/m3',n,'m3 CH4 STP',n*22.414e-3)
# Es
dV=18.015*(1/0.9998-1/0.9167)*1e-6; print('dV leleh m3/mol',dV,'dT/dp K/bar',273.15*dV/6010*1e5,' tekanan untuk -1 C (bar)',-1/(273.15*dV/6010*1e5))
print('ekspansi beku %',(0.9998/0.9167-1)*100)
print('entropi sisa es R ln 1.5',R*math.log(1.5))
# Rayleigh
x=(1.2572-1.2505)/(1.7837-1.2505); print('fraksi Ar dalam N2 atmosfer',x,' nyata',0.934/(78.084+0.934))
# XeF2 dari energi ikatan
for De in (133,):
    print('XeF2 ΔH ≈',158.7-2*De,' XeF4',2*158.7-4*131,' XeF6',3*158.7-6*126)
# IE O2 vs Xe
print('IE O2 1165, Xe 1170 kJ/mol')
# Rn
print('Rn-222 sisa setelah 30 hari',0.5**(30/3.8235))
# He cair untuk MRI

# --- soal
print('T2 sisa setelah 24,6 th',0.5**(24.64/12.32))
print('ZPE HD',0.5*3813.1*cm)
print('KIE O-H/O-D 3600 cm-1',math.exp(0.5*(3600-3600/math.sqrt(2))*cm*1000/(R*298.15)))
print('H2 per kg 700 bar volume tangki untuk 5 kg L',5/40.2*1000,' cair',5/70.8*1000)
# CaH2 + 2H2O -> Ca(OH)2 + 2H2 : air per g CaH2
print('CaH2 menyerap air g per g',2*18.015/42.094)
print('NaBH4 %H',4*1.008/37.83*100,'NH3BH3 %H',6*1.008/30.87*100)
# Pd volume H/Pd 0,6
print('Pd 0,6 mL',0.6*Pd/2*22414)
# es: Δp untuk -2 C
print('dp -2 C bar',2/0.0074237)
# Rayleigh dengan massa jenis Ar
# Xe: massa Xe dalam 1 m3 udara
print('Xe g/m3 udara',0.087e-6*1000/22.414*131.29)
print('He g/m3 udara',5.24e-6*1000/22.414*4.0026)
print('Rn 222 setelah 7 hari',0.5**(7/3.8235),' 3 hari',0.5**(3/3.8235))
print('XeF2 mol F per g',2/169.29)
# Grotthuss
print('rasio λ H+/Na+',349.6/50.1)
# energi orto-para D2 B=30.44 J 1->0 =2B
print('D2 B 30,44: 2B kJ',2*30.44*cm)
# kerapatan es -> volume per molekul
print('Vm es cm3',18.015/0.9167,' air',18.015/0.9998)
