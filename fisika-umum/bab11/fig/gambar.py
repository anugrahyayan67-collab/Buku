import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch as FA, Rectangle, Circle, Arc, Polygon
plt.rcParams.update({'font.family':'Liberation Sans','font.size':10,'mathtext.fontset':'dejavusans'})
B='#1b75bc'; T='#17355e'; M='#e9f2fa'; H='#b5541c'; W='#cfe3f5'; G='#1a8a6a'
def ar(ax,a,b,c='k',lw=1.6,ms=13,ls='-'): ax.add_patch(FA(a,b,arrowstyle='-|>',mutation_scale=ms,color=c,lw=lw,ls=ls,shrinkA=0,shrinkB=0))
def dar(ax,a,b,c='k'): ar(ax,a,b,c,1,8); ar(ax,b,a,c,1,8)
def sv(f,n): f.savefig(n,dpi=220,bbox_inches='tight'); plt.close(f)
def sp(ax):
    for s in ['top','right']: ax.spines[s].set_visible(False)
def pv(w=4.2,h=3.0):
    f,ax=plt.subplots(figsize=(w,h)); sp(ax); ax.set_xlabel('$V$'); ax.set_ylabel('$p$'); ax.set_xticks([]); ax.set_yticks([]); return f,ax
# usaha: luas di bawah kurva
f,ax=pv(); V=np.linspace(1,3,100); p=3/V
ax.plot(V,p,color=B,lw=2); ax.fill_between(V,p,color=W); ax.text(1.9,.6,'$W$ = luas',ha='center'); ar(ax,(1.75,1.9),(2.1,1.55),B,1.4,10)
ax.plot([1,3],[3,1],'o',color=T,ms=5); ax.text(.95,3.1,'1',ha='right'); ax.text(3.05,1.05,'2'); ax.set_xlim(.5,3.5); ax.set_ylim(0,3.6); sv(f,'usaha.png')
# dua jalur
f,ax=pv(); ax.plot([1,1,3],[1,3,3],color=B,lw=2); ax.plot([1,3,3],[1,1,3],color=H,lw=2); ax.fill_between([1,3],[1,1],color='#f3dccb',alpha=.7)
ax.plot([1,3],[1,3],'o',color=T,ms=5); ax.text(.9,.85,'A',ha='right'); ax.text(3.08,3.05,'C'); ax.text(.9,3,'B',ha='right'); ax.text(3.08,.9,'D')
ax.text(1.9,3.15,'jalur 1',color=B); ax.text(1.8,1.12,'jalur 2',color=H); ax.set_xlim(.4,3.6); ax.set_ylim(0,3.7); sv(f,'jalur.png')
# empat proses
f,ax=pv(4.6,3.3); V=np.linspace(1,3,100)
ax.plot([1,3],[3,3],color=G,lw=2); ax.text(3.05,3,'isobarik',color=G,va='center')
ax.plot(V,3/V,color=B,lw=2); ax.text(3.05,1.02,'isotermal',color=B,va='center')
ax.plot(V,3/V**1.67,color=H,lw=2); ax.text(3.05,.45,'adiabatik',color=H,va='center')
ax.plot([1,1],[3,.5],color='gray',lw=2); ax.text(.95,1.2,'isokhorik',color='gray',ha='right')
ax.plot(1,3,'o',color=T,ms=6); ax.set_xlim(.2,4); ax.set_ylim(0,3.5); sv(f,'proses.png')
# skema mesin & kulkas
def skema(n,mesin):
    f,ax=plt.subplots(figsize=(3.2,3.6)); ax.axis('off')
    ax.add_patch(Rectangle((0,3.2),3,.6,fc='#f3dccb',ec=H)); ax.text(1.5,3.5,'tandon panas $T_h$',ha='center',va='center')
    ax.add_patch(Rectangle((0,0),3,.6,fc=W,ec=B)); ax.text(1.5,.3,'tandon dingin $T_c$',ha='center',va='center')
    ax.add_patch(Circle((1.5,1.9),.5,fc=M,ec=T,lw=1.5)); ax.text(1.5,1.9,'mesin' if mesin else 'pompa',ha='center',va='center',fontsize=9)
    if mesin:
        ar(ax,(1.5,3.2),(1.5,2.4),H,3); ar(ax,(1.5,1.4),(1.5,.6),B,2); ar(ax,(2,1.9),(3,1.9),T,1.6); ax.text(1.62,2.8,'$Q_h$'); ax.text(1.62,1,'$Q_c$'); ax.text(3.05,1.9,'$W$',va='center')
    else:
        ar(ax,(1.5,2.4),(1.5,3.2),H,3); ar(ax,(1.5,.6),(1.5,1.4),B,2); ar(ax,(3,1.9),(2,1.9),T,1.6); ax.text(1.62,2.8,'$Q_h$'); ax.text(1.62,1,'$Q_c$'); ax.text(3.05,1.9,'$W$',va='center')
    ax.set_xlim(-.1,3.5); ax.set_ylim(-.1,3.9); sv(f,n)
skema('mesin.png',1); skema('kulkas.png',0)
# carnot
f,ax=pv(4.4,3.2); g=1.4
V1,V2=1,2; Th,Tc=3,1.9; V3=V2*(Th/Tc)**(1/(g-1)); V4=V1*(Th/Tc)**(1/(g-1))
a=np.linspace(V1,V2,50); ax.plot(a,Th/a,color=H,lw=2); b=np.linspace(V2,V3,50); ax.plot(b,Th*V2**(g-1)/b**g,color='gray',lw=2)
c=np.linspace(V4,V3,50); ax.plot(c,Tc/c,color=B,lw=2); d=np.linspace(V1,V4,50); ax.plot(d,Th*V1**(g-1)/d**g,color='gray',lw=2)
Va=np.linspace(V1,V3,300); up=np.where(Va<V2,Th/Va,Th*V2**(g-1)/Va**g); lo=np.where(Va<V4,Th*V1**(g-1)/Va**g,Tc/Va); ax.fill_between(Va,lo,up,color=W,alpha=.8)
for (x,y,t,dx,dy) in [(V1,Th/V1,'1',-.15,.05),(V2,Th/V2,'2',.08,.08),(V3,Tc/V3,'3',.1,0),(V4,Tc/V4,'4',-.2,-.2)]: ax.plot(x,y,'o',color=T,ms=5); ax.text(x+dx,y+dy,t)
ax.text(1.45,2.35,'$T_h$',color=H); ax.text(4.2,.62,'$T_c$',color=B); ax.text(2.6,.95,'$W$'); ax.set_xlim(.5,7); ax.set_ylim(0,3.4); sv(f,'carnot.png')
# otto
f,ax=pv(4.2,3.1); V=np.linspace(1,4,80); ax.plot(V,5/V**g,color=H,lw=2); ax.plot(V,1.8/V**g,color=B,lw=2); ax.plot([1,1],[1.8,5],color='gray',lw=2); ax.plot([4,4],[1.8/4**g,5/4**g],color='gray',lw=2)
ax.fill_between(V,1.8/V**g,5/V**g,color=W,alpha=.8); ax.text(.95,3.4,'pembakaran',ha='right',fontsize=8.5,rotation=90,va='center'); ax.text(2.3,1.9,'langkah usaha',fontsize=8.5,color=H); ax.text(1.6,.35,'pemampatan',fontsize=8.5,color=B); ax.text(4.08,.5,'buang',fontsize=8.5)
ax.set_xlim(.3,4.8); ax.set_ylim(0,5.4); sv(f,'otto.png')
# multiplicity
from math import comb
f,ax=plt.subplots(figsize=(4.6,2.8)); sp(ax); N=100; k=np.arange(0,101); w=np.array([comb(N,i) for i in k],float); ax.bar(k,w/w.max(),color=B,width=1)
ax.set_xlabel('banyaknya molekul di paruh kiri (dari 100)'); ax.set_ylabel('banyaknya cara (relatif)'); ax.set_yticks([]); sv(f,'cara.png')
# pemuaian bebas
f,ax=plt.subplots(figsize=(5,1.9)); ax.axis('off'); rng=np.random.default_rng(3)
for x0,full in [(0,0),(3.4,1)]:
    ax.add_patch(Rectangle((x0,0),2.6,1.3,fc='w',ec='k',lw=1.2)); ax.plot([x0+1.3]*2,[0,1.3] if not full else [0,.45],color='k',lw=1.2)
    if full: ax.plot([x0+1.3]*2,[.85,1.3],color='k',lw=1.2)
    xs=rng.uniform(x0+.08,x0+(2.52 if full else 1.22),40); ys=rng.uniform(.08,1.22,40); ax.plot(xs,ys,'o',color=B,ms=3)
ar(ax,(2.75,.65),(3.25,.65),'k',1.4,10); ax.text(.65,-.25,'awal',ha='center'); ax.text(4.7,-.25,'akhir',ha='center'); ax.set_xlim(-.1,6.1); ax.set_ylim(-.4,1.4); sv(f,'bebas.png')
# gibbs
f,ax=plt.subplots(figsize=(4.4,3)); sp(ax); Tt=np.linspace(233,313,10); ax.plot(Tt-273.15,(6010-Tt*22.0)/1000,color=B,lw=2); ax.axhline(0,color='k',lw=.8); ax.axvline(0,color='gray',ls=':',lw=.8)
ax.set_xlabel('suhu (°C)'); ax.set_ylabel(r'$\Delta G$ peleburan es (kJ/mol)'); ax.text(-38,.25,'es mantap\n($\\Delta G > 0$)',fontsize=9); ax.text(8,-.55,'air mantap\n($\\Delta G < 0$)',fontsize=9); sv(f,'gibbs.png')
