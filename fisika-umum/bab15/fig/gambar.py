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
# gamma
f,ax=plt.subplots(figsize=(4.4,2.9)); sp(ax); b=np.linspace(0,.995,400); ax.plot(b,1/np.sqrt(1-b**2),color=B,lw=2); ax.set_ylim(0,8); ax.set_xlabel('$v/c$'); ax.set_ylabel(r'$\gamma$'); ax.axhline(1,color='gray',ls=':',lw=.8); ax.set_xticks([0,.2,.4,.6,.8,1]); ax.set_xticklabels(['0','0,2','0,4','0,6','0,8','1']); sv(f,'gamma.png')
# jam cahaya
f,axs=plt.subplots(1,2,figsize=(5.6,2.4))
ax=axs[0]; ax.axis('off'); ax.set_xlim(-1,1); ax.set_ylim(-.5,2.4); ax.plot([-.4,.4],[0,0],color='k',lw=3); ax.plot([-.4,.4],[2,2],color='k',lw=3); ar(ax,(-.06,.05),(-.06,1.95),H,1.5,9); ar(ax,(.06,1.95),(.06,.05),H,1.5,9); ax.text(.5,1,'$d$'); ax.text(0,-.4,'jam diam',ha='center',fontsize=9)
ax=axs[1]; ax.axis('off'); ax.set_xlim(-.3,3.6); ax.set_ylim(-.5,2.4)
for x in [0,1.5,3]: ax.plot([x-.3,x+.3],[0,0],color='k',lw=3,alpha=.4 if x!=1.5 else 1); ax.plot([x-.3,x+.3],[2,2],color='k',lw=3,alpha=.4 if x!=1.5 else 1)
ar(ax,(0,.05),(1.5,1.95),H,1.5,9); ar(ax,(1.5,1.95),(3,.05),H,1.5,9); ar(ax,(.9,2.25),(2.1,2.25),G,1.3,9); ax.text(1.5,2.32,'$v$',color=G,ha='center',va='bottom'); ax.text(1.5,-.4,'jam bergerak: lintasan cahaya lebih panjang',ha='center',fontsize=9); sv(f,'jam.png')
# planck vs klasik
f,ax=plt.subplots(figsize=(4.6,3)); sp(ax); l=np.linspace(.1,4,400)*1e-6; h=6.626e-34;c=2.998e8;k=1.381e-23
pl=lambda T:(2*h*c**2/l**5)/(np.exp(h*c/(l*k*T))-1)
for T_,col in [(6000,B),(5000,G),(4000,H)]: ax.plot(l*1e6,pl(T_)/1e13,color=col,lw=2,label=f'{T_} K')
rj=2*c*k*5000/l**4/1e13; ax.plot(l*1e6,rj,color='k',ls='--',lw=1); ax.text(1.55,2.6,'ramalan klasik\n(5000 K)',fontsize=8.5); ax.set_ylim(0,3.4); ax.set_xlim(0,3)
ax.set_xlabel(r'panjang gelombang ($\mu$m)'); ax.set_ylabel('intensitas pancaran'); ax.set_yticks([]); ax.legend(frameon=False,fontsize=9); sv(f,'planck.png')
# fotolistrik
f,ax=plt.subplots(figsize=(4.6,3)); sp(ax); fr=np.linspace(0,15,10)
for phi,n,col in [(2.28,'Na',B),(4.08,'Al',G),(5.65,'Pt',H)]:
    f0=phi/.4136; x=np.linspace(f0,15,10); ax.plot(x,.4136*x-phi,color=col,lw=2,label=n)
ax.set_xlim(0,15.5); ax.set_ylim(0,4); ax.set_xlabel('frekuensi cahaya ($10^{14}$ Hz)'); ax.set_ylabel('$K_{maks}$ (eV)'); ax.legend(frameon=False,fontsize=9,loc='upper left'); ax.text(8.2,3.3,'kemiringan = $h$',fontsize=9); sv(f,'fotolistrik.png')
# tingkat energi H
f,ax=plt.subplots(figsize=(4.8,3.8)); sp(ax); ax.spines['bottom'].set_visible(False); ax.set_xticks([]); ax.set_ylabel('energi (eV)')
for n in [1,2,3,4,5,6]:
    E=-13.6/n**2; ax.plot([0,5],[E,E],color='k',lw=1)
    if n<=4: ax.text(5.1,E,f'$n={n}$',va='center',fontsize=8.5)
ax.plot([0,5],[0,0],color='gray',ls='--',lw=.8); ax.text(5.1,.35,r'$n=\infty$',va='center',fontsize=8.5)
for i,n in enumerate([2,3,4]): ar(ax,(.4+.35*i,-13.6/n**2),(.4+.35*i,-13.6),'#7a4fb3',1.2,8)
for i,n in enumerate([3,4,5]): ar(ax,(2+.35*i,-13.6/n**2),(2+.35*i,-3.4),H,1.2,8)
for i,n in enumerate([4,5]): ar(ax,(3.7+.35*i,-13.6/n**2),(3.7+.35*i,-1.51),G,1.2,8)
ax.text(.75,-9,'Lyman\n(UV)',ha='center',fontsize=8.5,color='#7a4fb3'); ax.text(2.35,-5.2,'Balmer\n(tampak)',ha='center',fontsize=8.5,color=H); ax.text(3.9,-2.9,'Paschen\n(IR)',ha='center',fontsize=8.5,color=G); ax.set_xlim(-.2,6); ax.set_ylim(-14.5,1); sv(f,'tingkat.png')
# Balmer
f,ax=plt.subplots(figsize=(5.4,1.3)); ax.set_facecolor('k'); ax.set_xlim(380,700); ax.set_yticks([])
for l_,col in [(656.3,'#ff2020'),(486.1,'#30d5ff'),(434.0,'#4a4aff'),(410.2,'#8a2be2'),(397.0,'#7a2bd0')]: ax.axvline(l_,color=col,lw=2.2)
ax.set_xlabel('panjang gelombang (nm)'); sv(f,'balmer.png')
# de Broglie orbit
f,axs=plt.subplots(1,2,figsize=(5.2,2.6)); th=np.linspace(0,2*np.pi,600)
for ax,n,t in zip(axs,[4,4.5],['$n = 4$: pas','tidak pas: saling menghapus']):
    ax.axis('off'); ax.set_aspect('equal'); ax.plot(np.cos(th),np.sin(th),color='gray',ls=':',lw=.8); r=1+.18*np.sin(n*th); ax.plot(r*np.cos(th),r*np.sin(th),color=B if n==4 else H,lw=1.8); ax.plot(0,0,'o',color=T,ms=5); ax.text(0,-1.5,t,ha='center',fontsize=9); ax.set_xlim(-1.4,1.4); ax.set_ylim(-1.7,1.4)
sv(f,'debroglie.png')
# sebaran radial
f,ax=plt.subplots(figsize=(4.6,2.9)); sp(ax); r=np.linspace(0,14,500); P1=4*r**2*np.exp(-2*r); P2=.125*r**2*(2-r)**2*np.exp(-r)
ax.plot(r,P1,color=B,lw=2,label='1s'); ax.plot(r,P2,color=H,lw=2,label='2s'); ax.axvline(1,color='gray',ls=':',lw=.8); ax.set_xlabel('jarak dari inti ($a_0$)'); ax.set_ylabel('peluang menemukan elektron'); ax.set_yticks([]); ax.legend(frameon=False,fontsize=9); sv(f,'radial.png')
