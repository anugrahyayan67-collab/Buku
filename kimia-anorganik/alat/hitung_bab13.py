#!/usr/bin/env python3
# Angka Bab 13 Kimia Anorganik 1: kimia inti (massa atom AME, u)
import math
u=931.494; mH=1.007825032; mn=1.008664916; me=0.000548580
M={'1H':1.007825032,'2H':2.014101778,'3H':3.016049281,'3He':3.016029322,'4He':4.002603254,'6Li':6.015122887,'7Li':7.016003437,'9Be':9.012183065,'12C':12.0,'14C':14.003241989,'14N':14.003074004,'16O':15.994914620,'18O':17.999159613,'18F':18.000937324,
   '20Ne':19.992440176,'40Ca':39.962590866,'40K':39.963998166,'40Ar':39.962383122,'56Fe':55.934936326,'62Ni':61.928345115,'90Zr':89.904698,'120Sn':119.902202,'197Au':196.966570,'208Pb':207.976653,'235U':235.043930,'238U':238.050788,'234Th':234.043601,'141Ba':140.914411,'92Kr':91.926156,'226Ra':226.025410,'222Rn':222.017578,'99Tc':98.906250}
Z={'1H':1,'2H':1,'3H':1,'3He':2,'4He':2,'6Li':3,'7Li':3,'9Be':4,'12C':6,'14C':6,'14N':7,'16O':8,'18O':8,'18F':9,'20Ne':10,'40Ca':20,'40K':19,'40Ar':18,'56Fe':26,'62Ni':28,'90Zr':40,'120Sn':50,'197Au':79,'208Pb':82,'235U':92,'238U':92,'234Th':90,'141Ba':56,'92Kr':36,'226Ra':88,'222Rn':86}
def A(k): return int(''.join(c for c in k if c.isdigit()))
def BE(k):
    a=A(k); z=Z[k]; return (z*mH+(a-z)*mn-M[k])*u
for k in ['2H','4He','6Li','12C','16O','56Fe','62Ni','90Zr','120Sn','197Au','208Pb','235U','238U']:
    print(f'{k}: B = {BE(k):.2f} MeV, B/A = {BE(k)/A(k):.3f}')
print('defek massa 4He u',2*mH+2*mn-M['4He'])
# Q
print('Q alfa 238U',(M['238U']-M['234Th']-M['4He'])*u)
print('Q alfa 226Ra',(M['226Ra']-M['222Rn']-M['4He'])*u)
print('Q beta- 14C',(M['14C']-M['14N'])*u)
print('Q beta- 40K',(M['40K']-M['40Ca'])*u,' EC',(M['40K']-M['40Ar'])*u,' beta+',(M['40K']-M['40Ar'])*u-2*me*u)
print('Q beta+ 18F',(M['18F']-M['18O'])*u-2*me*u)
print('Q beta- 3H',(M['3H']-M['3He'])*u)
# energi kinetik alfa (rekoil)
Q=(M['238U']-M['234Th']-M['4He'])*u; print('Ealfa 238U',Q*234/238)
# fisi & fusi
Qf=(M['235U']+mn-M['141Ba']-M['92Kr']-3*mn)*u; print('Q fisi 235U->141Ba+92Kr+3n',Qf)
print('energi per kg 235U (200 MeV) J',200e6*1.602177e-19*6.02214e23/0.235,' batu bara 29 MJ/kg rasio',200e6*1.602177e-19*6.02214e23/0.235/29e6)
print('Q fusi D+T',(M['2H']+M['3H']-M['4He']-mn)*u)
print('Q 4 1H -> 4He (atom)',(4*mH-M['4He'])*u)
print('fusi D-T per kg bahan J',17.59e6*1.602177e-19*6.02214e23/(0.005030))
# kinetika
L=math.log(2)
def act(g,M_,th_s): return g/M_*6.02214e23*L/th_s
yr=365.25*24*3600
print('aktivitas 1 g Ra-226 Bq',act(1,226.0254,1600*yr))
print('aktivitas 1 g C (14C/12C 1.2e-12) Bq/g',1.2e-12*6.02214e23/12.011*L/(5730*yr),' per menit',1.2e-12*6.02214e23/12.011*L/(5730*yr)*60)
print('Otzi fraksi 5300 th',0.5**(5300/5730),' umur dari 0,53:',math.log(1/0.53)*5730/L)
print('umur 14C dari 25 %',2*5730,' dari 10 %',math.log(10)*5730/L)
for r in (0.1,0.5,1.0): print('U-Pb Pb/U',r,'umur Gth',math.log(1+r)/(L/4.468e9)/1e9)
print('Tc-99m sisa 24 jam',0.5**(24/6.01),' Mo-99 66 jam')
print('F-18 sisa 2 jam',0.5**(120/109.8))
print('I-131 8,02 hari: sisa 80 hari',0.5**(80/8.02))
print('Rn sisa 10 hari',0.5**(10/3.8235))
print('K-40 dalam tubuh: 140 g K, kelimpahan 0,0117 %, t1/2 1,248e9 th; Bq',140/39.098*1.17e-4*6.02214e23*L/(1.248e9*yr))
print('pisang 0,42 g K? Bq',0.42/39.098*1.17e-4*6.02214e23*L/(1.248e9*yr))
# semi-empiris
def semf(Z_,A_):
    aV,aS,aC,aA,aP=15.75,17.8,0.711,23.7,11.18
    N_=A_-Z_; d=0
    if Z_%2==0 and N_%2==0: d=aP/A_**0.5
    elif Z_%2==1 and N_%2==1: d=-aP/A_**0.5
    return aV*A_-aS*A_**(2/3)-aC*Z_*(Z_-1)/A_**(1/3)-aA*(A_-2*Z_)**2/A_+d
for k in ['56Fe','238U','4He','16O','208Pb']: print('SEMF',k,semf(Z[k],A(k))/A(k),'data',BE(k)/A(k))
# rincian suku untuk 56Fe
a=56;z=26
print('suku 56Fe vol',15.75*a,'perm',-17.8*a**(2/3),'coul',-0.711*z*(z-1)/a**(1/3),'asim',-23.7*(a-2*z)**2/a,'pair',11.18/a**0.5)
# Z optimum
for a in (56,120,208,238): print('Z0',a, a/(2+0.0154*a**(2/3)) if False else (a/2)/(1+0.0077*a**(2/3)))

# --- soal & contoh tambahan
print('Tc: 740*2^(3/6.01)',740*2**(3/6.01))
print('dosis 2 m',80*(0.5/2)**2,' r',0.5*math.sqrt(80/20))
print('Am-241 0,3 ug Bq',0.3e-6/241.06*6.022e23*L/(432.2*yr))
print('aktivitas 1 mg I-131 Bq',1e-3/130.906*6.022e23*L/(8.02*86400))
print('tritium 1 g Bq',1/3.016*6.022e23*L/(12.32*yr))
print('K-Ar: 40Ar*/40K=0,1 umur (λ total 5,543e-10/th, cabang EC 0,1072)',math.log(1+0.1/0.1072)/5.543e-10/1e9,'Gth')
print('14C: 0,10 Bq/g umur',math.log(0.23/0.10)*5730/L)
print('Pb/U 0,8 umur', math.log(1.8)/(L/4.468e9)/1e9)
print('U235 2 Gy lalu %', 0.720*2**(2e9/7.04e8)/ (0.720*2**(2e9/7.04e8)+99.274*2**(2e9/4.468e9))*100)
print('U235 saat Bumi terbentuk %', 0.720*2**(4.55e9/7.04e8)/ (0.720*2**(4.55e9/7.04e8)+99.274*2**(4.55e9/4.468e9))*100)
print('B/A 2H dll ok; deuteron energi ikat',(mH+mn-M['2H'])*u)
print('energi foton anihilasi keV',me*u*1000)
print('Q 3H beta keV',(M['3H']-M['3He'])*u*1000)
print('radius 238U fm',1.2*238**(1/3),' 4He',1.2*4**(1/3))
print('Coulomb barrier alfa-Th (r sum) MeV',1.44*2*90/(1.2*(234**(1/3)+4**(1/3))))
print('energi kimia 1 kg C bakar 32,8 MJ; fusion/fisi ratios done')
print('mol He dari 1 g U-238 per tahun',1/238.05*L/4.468e9*8)
