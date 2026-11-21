import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch as FA
plt.rcParams.update({'font.family':'Liberation Sans','font.size':10,'mathtext.fontset':'dejavusans','text.color':'#17355e'})
B='#1b75bc'; T='#17355e'; H='#b5541c'; W='#cfe3f5'
def sv(f,n): f.savefig(n,dpi=220,bbox_inches='tight'); plt.close(f)
f,axs=plt.subplots(1,2,figsize=(6.4,3.2))
for ax,(hl,hr,t) in zip(axs,[(2.0,2.0,'awal'),(1.55,2.45,'setimbang')]):
    ax.set_aspect('equal'); ax.axis('off')
    ax.plot([0,0,3,3],[3.2,0,0,3.2],color=T,lw=1.5); ax.plot([1.5,1.5],[0,3.0],color='#888',lw=2,ls=(0,(2,1.5)))
    ax.add_patch(Rectangle((0,0),1.5,hl,fc=W,ec='none')); ax.add_patch(Rectangle((1.5,0),1.5,hr,fc='#e9cdb8',ec='none'))
    rng=np.random.default_rng(2)
    for x,y in zip(rng.uniform(1.65,2.85,9),rng.uniform(0.2,hr-0.2,9)): ax.add_patch(Circle((x,y),0.07,fc=H))
    ax.text(0.75,-0.35,'pelarut\nmurni',ha='center',va='top',fontsize=8.5); ax.text(2.25,-0.35,'larutan',ha='center',va='top',fontsize=8.5)
    ax.text(1.5,3.35,t,ha='center',fontsize=9.5,fontweight='bold')
    if t=='setimbang':
        ax.annotate('',xy=(3.25,hr),xytext=(3.25,hl),arrowprops=dict(arrowstyle='<->',lw=.8)); ax.text(3.35,(hl+hr)/2,r'$h$: $\rho gh = \Pi$',va='center',fontsize=8.5)
        ax.add_patch(FA((0.9,1.0),(2.1,1.0),arrowstyle='-|>',mutation_scale=12,color=B,lw=1.6)); ax.text(1.5,1.15,'air',ha='center',fontsize=8,color=B)
    ax.set_xlim(-0.2,4.6); ax.set_ylim(-1.7,3.6)
axs[0].text(1.5,-1.5,'garis putus-putus: selaput semipermeabel',ha='center',fontsize=8,color='#666')
sv(f,'c_osmosis.png')
