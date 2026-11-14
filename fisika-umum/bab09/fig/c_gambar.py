import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch as FA, Arc, Polygon
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family':'Liberation Sans','font.size':10,'mathtext.fontset':'dejavusans','text.color':'#17355e','axes.edgecolor':'#17355e'})
B='#1b75bc'; T='#17355e'; H='#b5541c'; W='#cfe3f5'; G='#1a8a6a'
KOMA=FuncFormatter(lambda x,p:('%g'%x).replace('.',','))
def sv(f,n): f.savefig(n,dpi=220,bbox_inches='tight'); plt.close(f)
def ar(ax,a,b,c='k',lw=1.6,ms=12): ax.add_patch(FA(a,b,arrowstyle='-|>',mutation_scale=ms,color=c,lw=lw,shrinkA=0,shrinkB=0))
# 1 pembiasan & pemantulan total
f,axs=plt.subplots(1,2,figsize=(6.6,3.0))
for ax in axs: ax.set_aspect('equal'); ax.axis('off'); ax.add_patch(Rectangle((-2,-2),4,2,fc=W,ec='none')); ax.plot([-2,2],[0,0],color=T,lw=1); ax.plot([0,0],[-1.8,1.8],color='#999',ls=':',lw=.8); ax.set_xlim(-2,2); ax.set_ylim(-2,2)
ax=axs[0]; t1=np.radians(40); t2=np.arcsin(np.sin(t1)/1.333)
ar(ax,(-1.8*np.sin(t1),1.8*np.cos(t1)),(0,0),H,1.6); ar(ax,(0,0),(1.8*np.sin(t2),-1.8*np.cos(t2)),H,1.6); ar(ax,(0,0),(1.5*np.sin(t1),1.5*np.cos(t1)),'#d9a07a',1,9)
ax.add_patch(Arc((0,0),1.0,1.0,theta1=90,theta2=90+40,color=T,lw=.8)); ax.text(-0.35,0.62,r'$\theta_1$'); ax.add_patch(Arc((0,0),1.0,1.0,theta1=270,theta2=270+np.degrees(t2),color=T,lw=.8)); ax.text(0.12,-0.75,r'$\theta_2$')
ax.text(-1.9,1.7,'udara, $n_1$',fontsize=8.5); ax.text(-1.9,-1.85,'air, $n_2$',fontsize=8.5); ax.set_title('(a) pembiasan',fontsize=9)
ax=axs[1]
for th,col in [(30,B),(48.6,G),(65,H)]:
    t=np.radians(th); ar(ax,(-1.8*np.sin(t),-1.8*np.cos(t)),(0,0),col,1.4,9)
    if th<48: t2=np.arcsin(1.333*np.sin(t)); ar(ax,(0,0),(1.6*np.sin(t2),1.6*np.cos(t2)),col,1.4,9)
    elif th<50: ar(ax,(0,0),(1.8,0.02),col,1.4,9)
    else: ar(ax,(0,0),(1.8*np.sin(t),-1.8*np.cos(t)),col,1.4,9)
ax.text(-1.9,1.7,'udara',fontsize=8.5); ax.text(-1.9,-1.85,'air',fontsize=8.5); ax.text(0.5,-1.45,'dipantulkan\nseluruhnya',fontsize=8,color=H); ax.text(0.9,0.15,r'$\theta_c$',fontsize=8.5,color=G)
ax.set_title('(b) pemantulan total',fontsize=9); sv(f,'c_snell.png')
# 2 celah ganda dan pola
f,axs=plt.subplots(1,2,figsize=(6.6,2.8),gridspec_kw={'width_ratios':[1.3,1]})
ax=axs[0]; ax.axis('off'); ax.plot([0,0],[-1.5,-0.25],color=T,lw=3); ax.plot([0,0],[-0.15,0.15],color=T,lw=3); ax.plot([0,0],[0.25,1.5],color=T,lw=3)
ax.plot([3,3],[-1.5,1.5],color=T,lw=1.5); P=(3,0.9)
for y in [0.2,-0.2]: ax.plot([0,P[0]],[y,P[1]],color=B,lw=1)
ax.plot([0,3],[0,0],color='#999',ls=':',lw=.8); ax.text(1.4,0.55,r'$\theta$',fontsize=9); ax.text(-0.45,0.0,'$d$',va='center')
ax.plot([0,0.07],[-0.2,0.18],color=H,lw=1.5); ax.text(0.15,-0.45,r'$\Delta r = d\sin\theta$',fontsize=8.5,color=H)
ax.annotate('',xy=(3.25,0.9),xytext=(3.25,0),arrowprops=dict(arrowstyle='<->',lw=.7)); ax.text(3.32,0.45,'$y$',fontsize=9); ax.text(1.5,-1.75,'$L$ (jauh lebih besar dari $d$)',ha='center',fontsize=8.5); ax.set_xlim(-0.7,3.7); ax.set_ylim(-1.9,1.6)
ax=axs[1]; y=np.linspace(-3,3,800); I=np.cos(np.pi*y)**2*np.sinc(y/3.2)**2; ax.plot(I,y,color=B,lw=1.5); ax.set_xlabel('intensitas'); ax.set_ylabel(r'letak di layar ($y$ / jarak antarpita)'); ax.set_xticks([]); ax.yaxis.set_major_formatter(KOMA)
for s in ['top','right']: ax.spines[s].set_visible(False)
sv(f,'c_celah.png')
# 3 polarimeter
f,ax=plt.subplots(figsize=(6.4,1.9)); ax.set_aspect('equal'); ax.axis('off')
ax.add_patch(Circle((0,0),0.25,fc='#f0d24a',ec=T)); ax.text(0,-0.55,'sumber\ncahaya',ha='center',va='top',fontsize=8)
ax.add_patch(Rectangle((1.0,-0.45),0.1,0.9,fc=B)); ax.text(1.05,-0.55,'polarisator',ha='center',va='top',fontsize=8)
ax.add_patch(Rectangle((1.8,-0.3),2.2,0.6,fc=W,ec=T)); ax.text(2.9,-0.55,'tabung cuplikan\n(panjang $l$)',ha='center',va='top',fontsize=8)
ax.add_patch(Rectangle((4.7,-0.45),0.1,0.9,fc=B)); ax.text(4.75,-0.55,'analisator\n(diputar)',ha='center',va='top',fontsize=8)
ax.add_patch(Circle((5.6,0),0.18,fc=T)); ax.text(5.6,-0.55,'mata atau\ndetektor',ha='center',va='top',fontsize=8)
ax.plot([0.25,5.4],[0,0],color=H,lw=1,ls='--')
ax.plot([1.4,1.4],[-0.3,0.3],color=H,lw=2); ar(ax,(1.4,0),(1.4,0.3),H,1,7)
th=np.radians(30); ax.plot([4.35-0.3*np.sin(th),4.35+0.3*np.sin(th)],[-0.3*np.cos(th),0.3*np.cos(th)],color=H,lw=2); ax.text(4.35,0.42,r'diputar $\alpha$',ha='center',fontsize=8,color=H)
ax.set_xlim(-0.4,6.0); ax.set_ylim(-1.2,0.7); sv(f,'c_polarimeter.png')
