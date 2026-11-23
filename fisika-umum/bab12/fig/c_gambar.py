import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch as FA
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family':'Liberation Sans','font.size':10,'mathtext.fontset':'dejavusans','text.color':'#17355e','axes.edgecolor':'#17355e'})
B='#1b75bc'; T='#17355e'; H='#b5541c'; W='#cfe3f5'; G='#1a8a6a'
KOMA=FuncFormatter(lambda x,p:('%g'%x).replace('.',','))
def sv(f,n): f.savefig(n,dpi=220,bbox_inches='tight'); plt.close(f)
def ar(ax,a,b,c='k',lw=1.6,ms=12): ax.add_patch(FA(a,b,arrowstyle='-|>',mutation_scale=ms,color=c,lw=lw,shrinkA=0,shrinkB=0))
# cincin
f,ax=plt.subplots(figsize=(4.2,3.0)); ax.set_aspect('equal'); ax.axis('off')
ax.add_patch(Ellipse((0,0),0.8,2.4,fc='none',ec=H,lw=2.2)); ax.plot([-0.2,3.2],[0,0],color='#999',ls=':',lw=.8)
P=(2.4,0); ax.plot(*P,'o',color=T,ms=5); ax.text(2.4,-0.3,'P',ha='center')
for y,s in [(1.2,1),(-1.2,-1)]:
    ax.plot([0,P[0]],[y,0],color=B,lw=.9); d=np.array([2.4,-y]); d=d/np.linalg.norm(d); ar(ax,P,(P[0]+0.7*d[0],0.7*d[1]),B,1.2,9)
ar(ax,P,(P[0]+0.95,0),T,2,11); ax.text(3.4,0.15,r'$\vec E$ (sumbu)',fontsize=8.5)
ax.text(-0.35,1.4,'$dq$',color=H); ax.text(1.2,0.15,'$z$',fontsize=9); ax.annotate('',xy=(0,1.2),xytext=(0,0),arrowprops=dict(arrowstyle='<->',lw=.7)); ax.text(0.08,0.55,'$R$',fontsize=9)
ax.text(1.45,0.95,'komponen tegak\nsaling meniadakan',fontsize=7.5,color=B)
ax.set_xlim(-0.6,4.3); ax.set_ylim(-1.5,1.6); sv(f,'c_cincin.png')
# atmosfer ion
f,axs=plt.subplots(1,2,figsize=(6.6,2.9),gridspec_kw={'width_ratios':[1,1.3]})
ax=axs[0]; ax.set_aspect('equal'); ax.axis('off'); rng=np.random.default_rng(4)
ax.add_patch(Circle((0,0),1.5,fc='#eef4fb',ec=B,ls='--')); ax.add_patch(Circle((0,0),0.22,fc=H,ec=T)); ax.text(0,0,'+',color='w',ha='center',va='center',fontweight='bold')
for i in range(40):
    r=abs(rng.normal(0,1.0))+0.35; a=rng.uniform(0,2*np.pi); neg=rng.random()<0.5+0.4*np.exp(-r/0.7)
    if r>2.1: continue
    ax.add_patch(Circle((r*np.cos(a),r*np.sin(a)),0.09,fc=B if neg else '#e9a77c',ec='none'))
ax.text(0,-1.85,r'jari-jari $\approx \lambda_D$',ha='center',fontsize=8.5,color=B); ax.set_xlim(-2.1,2.1); ax.set_ylim(-2.1,2.0)
ax.set_title('awan ion bermuatan lawan',fontsize=9)
ax=axs[1]; r=np.linspace(0.3,5,300); ax.plot(r,1/r,color=H,lw=2,label='tanpa perisai ($1/r$)'); ax.plot(r,np.exp(-r)/r,color=B,lw=2,label=r'dengan perisai ($e^{-r/\lambda_D}/r$)')
ax.set_xlabel(r'jarak ($r/\lambda_D$)'); ax.set_ylabel('potensial'); ax.set_yticks([]); ax.set_ylim(0,3); ax.legend(frameon=False,fontsize=8); ax.xaxis.set_major_formatter(KOMA)
for s in ['top','right']: ax.spines[s].set_visible(False)
sv(f,'c_debye.png')
