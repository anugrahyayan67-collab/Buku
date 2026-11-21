import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({'font.family':'Liberation Sans','font.size':10,'mathtext.fontset':'dejavusans','text.color':'#17355e','axes.edgecolor':'#17355e'})
B='#1b75bc'; T='#17355e'; H='#b5541c'; W='#cfe3f5'; G='#1a8a6a'
def sv(f,n): f.savefig(n,dpi=220,bbox_inches='tight'); plt.close(f)
f,ax=plt.subplots(figsize=(6.2,2.9)); ax.axis('off')
for x0,gap,lab,fill in [(0,0,'logam',0.6),(2.3,0.8,'semikonduktor',1),(4.6,2.6,'isolator',1)]:
    ax.add_patch(Rectangle((x0,0),1.5,1.4,fc=B,ec=T)); top=1.4+gap
    ax.add_patch(Rectangle((x0,top),1.5,1.4,fc='w',ec=T))
    if x0==0: ax.add_patch(Rectangle((x0,top),1.5,0.5,fc=B,ec='none')); ax.add_patch(Rectangle((x0,top),1.5,1.4,fc='none',ec=T))
    ax.text(x0+0.75,-0.35,lab,ha='center',va='top',fontsize=9)
    if gap>0:
        ax.annotate('',xy=(x0+1.7,top),xytext=(x0+1.7,1.4),arrowprops=dict(arrowstyle='<->',lw=.8)); ax.text(x0+1.78,1.4+gap/2,'$E_g$',va='center',fontsize=9)
ax.text(0.75,0.7,'terisi',ha='center',va='center',color='w',fontsize=8.5); ax.text(3.05,0.7,'pita\nvalensi',ha='center',va='center',color='w',fontsize=8); ax.text(3.05,2.9,'pita\nkonduksi',ha='center',va='center',fontsize=8)
ax.plot([2.6,2.75,3.3],[2.35,2.4,2.32],'o',color=H,ms=3.5); ax.plot([2.65,2.9,3.35],[1.25,1.3,1.22],'o',mfc='w',mec=H,ms=3.5)
ax.text(-0.4,2.0,'energi',rotation=90,va='center',fontsize=9); ax.set_xlim(-0.6,6.6); ax.set_ylim(-0.8,5.5); sv(f,'c_pita.png')
