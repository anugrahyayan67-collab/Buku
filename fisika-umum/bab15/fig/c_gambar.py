import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family':'Liberation Sans','font.size':10,'mathtext.fontset':'dejavusans','text.color':'#17355e','axes.edgecolor':'#17355e'})
B='#1b75bc'; T='#17355e'; H='#b5541c'; W='#cfe3f5'; G='#1a8a6a'
KOMA=FuncFormatter(lambda x,p:('%g'%x).replace('.',','))
def sv(f,n): f.savefig(n,dpi=220,bbox_inches='tight'); plt.close(f)
def sp(ax):
    for s in ['top','right']: ax.spines[s].set_visible(False)
# kotak + penerobosan
f,axs=plt.subplots(1,2,figsize=(6.8,3.0),gridspec_kw={'width_ratios':[1,1.35]})
ax=axs[0]; ax.axis('off'); x=np.linspace(0,1,300)
ax.plot([0,0],[0,10.5],color=T,lw=2.5); ax.plot([1,1],[0,10.5],color=T,lw=2.5); ax.plot([0,1],[0,0],color=T,lw=1)
for n in [1,2,3]:
    E=n*n; ax.axhline(E,0.12,0.88,color='#aaa',lw=.6) if False else ax.plot([0,1],[E,E],color='#bbb',lw=.7,ls='--')
    ax.plot(x,E+0.75*np.sin(n*np.pi*x),color=[B,G,H][n-1],lw=2); ax.text(1.06,E,f'$n$ = {n}\n$E$ = {n*n}$E_1$',va='center',fontsize=8)
ax.set_xlim(-0.1,1.55); ax.set_ylim(-0.6,10.6); ax.text(0.5,-0.55,'$L$',ha='center'); ax.set_title('partikel dalam kotak',fontsize=9)
ax=axs[1]; ax.axis('off'); xx=np.linspace(-3,6,1200); k=4.0; kap=1.2; a=1.4; y0=0.75; y1=y0*np.exp(-kap*a)
f_=lambda u,yy: yy*np.cos(k*u)-(kap*yy/k)*np.sin(k*u)
y=np.where(xx<0,f_(xx,y0),np.where(xx<a,y0*np.exp(-kap*xx),f_(xx-a,y1)))
ax.add_patch(plt.Rectangle((0,-1.4),a,2.9,color=W)); ax.text(a/2,1.65,'penghalang\n$U > E$',ha='center',fontsize=8.5)
ax.plot(xx,y,color=B,lw=1.8); ax.axhline(0,color='#999',lw=.6)
ax.text(-1.5,-1.75,'gelombang datang',ha='center',fontsize=8.5); ax.text(4.2,-1.75,'gelombang yang lolos\n(kecil, tetapi tidak nol)',ha='center',fontsize=8.5)
ax.set_xlim(-3,6); ax.set_ylim(-2.3,2.3); ax.set_title('penerobosan',fontsize=9); sv(f,'c_kotak.png')
# LCAO
f,axs=plt.subplots(1,2,figsize=(6.6,2.5),sharey=True); x=np.linspace(-4,4,800); R=1.0
p1=np.exp(-abs(x+R)); p2=np.exp(-abs(x-R))
for ax,s,ttl,col in [(axs[0],1,'orbital ikatan: $\\psi_A + \\psi_B$',B),(axs[1],-1,'orbital antiikatan: $\\psi_A - \\psi_B$',H)]:
    sp(ax); ps=p1+s*p2; ax.plot(x,ps,color=col,lw=2,label='$\\psi$'); ax.fill_between(x,0,ps**2/2.2,color=col,alpha=.18,label='$|\\psi|^2$')
    ax.plot(x,p1,color='#999',lw=.8,ls=':'); ax.plot(x,s*p2,color='#999',lw=.8,ls=':')
    for xi in [-R,R]: ax.plot(xi,0,'o',color=T,ms=6)
    ax.axhline(0,color='#999',lw=.6); ax.set_title(ttl,fontsize=9); ax.set_xticks([]); ax.set_yticks([]); ax.legend(frameon=False,fontsize=8,loc='lower left' if s<0 else 'upper left')
axs[1].annotate('simpul',xy=(0,0),xytext=(1.6,0.9),fontsize=8.5,arrowprops=dict(arrowstyle='->',color='#777',lw=.8)); sv(f,'c_lcao.png')
# inti: energi ikat per nukleon + peluruhan
f,axs=plt.subplots(1,2,figsize=(6.8,2.9)); ax=axs[0]; sp(ax)
A=np.arange(4,240); Z=A/(1.98+0.0155*A**(2/3))
BE=15.8*A-18.3*A**(2/3)-0.714*Z*(Z-1)/A**(1/3)-23.2*(A-2*Z)**2/A
ax.plot(A,BE/A,color=B,lw=1.8)
pts=[(2,1.11,'²H'),(4,7.07,'⁴He'),(12,7.68,'¹²C'),(16,7.98,'¹⁶O'),(56,8.79,'⁵⁶Fe'),(238,7.57,'²³⁸U')]
off={'²H':(9,0.9),'⁴He':(9,6.3),'¹²C':(19,7.0),'¹⁶O':(3,8.55),'⁵⁶Fe':(50,9.2),'²³⁸U':(212,6.7)}
for a_,b_,n in pts: ax.plot(a_,b_,'o',color=H,ms=4); ax.text(*off[n],n,fontsize=8.5)
ax.set_xlabel('nomor massa $A$'); ax.set_ylabel('energi ikat tiap nukleon (MeV)'); ax.set_ylim(0,10); ax.set_xlim(0,250)
ax.annotate('',xy=(45,8.2),xytext=(12,4.5),arrowprops=dict(arrowstyle='->',color=G,lw=1.3)); ax.text(32,5.2,'fusi',color=G,fontsize=9)
ax.annotate('',xy=(120,8.0),xytext=(230,6.2),arrowprops=dict(arrowstyle='->',color=G,lw=1.3)); ax.text(165,6.0,'fisi',color=G,fontsize=9)
ax=axs[1]; sp(ax); t=np.linspace(0,5,300); ax.plot(t,100*0.5**t,color=B,lw=2)
for n in range(1,5): ax.plot([n,n,0],[0,100*0.5**n,100*0.5**n],color='#aaa',lw=.7,ls=':')
ax.set_xlabel('waktu (dalam waktu paruh)'); ax.set_ylabel('inti tersisa (%)'); ax.set_ylim(0,105); ax.set_xlim(0,5); ax.set_yticks([0,12.5,25,50,100]); ax.yaxis.set_major_formatter(KOMA)
plt.tight_layout(); sv(f,'c_inti.png')
