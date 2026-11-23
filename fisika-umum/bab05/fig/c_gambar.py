import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch as FA, Arc, Rectangle, Polygon
plt.rcParams.update({'font.family':'Liberation Sans','font.size':10,'mathtext.fontset':'dejavusans','text.color':'#17355e'})
B='#1b75bc'; T='#17355e'; H='#b5541c'; W='#cfe3f5'; G='#1a8a6a'
def sv(f,n): f.savefig(n,dpi=220,bbox_inches='tight'); plt.close(f)
def ar(ax,a,b,c='k',lw=1.6,ms=12): ax.add_patch(FA(a,b,arrowstyle='-|>',mutation_scale=ms,color=c,lw=lw,shrinkA=0,shrinkB=0))
# 1 benda tegar berputar
f,ax=plt.subplots(figsize=(3.6,3.4)); ax.set_aspect('equal'); ax.axis('off')
ax.add_patch(Circle((0,0),1.5,fc=W,ec=T,lw=1.2)); ax.plot(0,0,'o',color=T,ms=5)
for r,a in [(0.7,40),(1.4,40)]:
    x,y=r*np.cos(np.radians(a)),r*np.sin(np.radians(a)); ax.plot([0,x],[0,y],color=T,lw=.8); ax.plot(x,y,'o',color=H,ms=5)
    d=np.array([-np.sin(np.radians(a)),np.cos(np.radians(a))]); ar(ax,(x,y),(x+0.55*r*d[0],y+0.55*r*d[1]),B,1.5,10)
ax.text(0.85,1.35,r'$v = \omega r$',color=B); ax.add_patch(Arc((0,0),0.8,0.8,theta1=0,theta2=40,color=T,lw=.8)); ax.text(0.45,0.1,r'$\theta$')
ax.add_patch(Arc((0,0),3.5,3.5,theta1=200,theta2=250,color=G,lw=1.6)); ar(ax,(-1.0,-1.46),(-0.62,-1.64),G,1.6,10); ax.text(-1.85,-1.75,r'$\omega$',color=G,fontsize=12)
ax.set_xlim(-2,2); ax.set_ylim(-2,2); sv(f,'c_rotasi.png')
# 2 torsi kunci pas
f,ax=plt.subplots(figsize=(4.4,2.4)); ax.set_aspect('equal'); ax.axis('off')
ax.add_patch(Polygon([[-0.15,-0.12],[3,-0.08],[3,0.08],[-0.15,0.12]],fc='#bbb',ec=T)); ax.add_patch(Circle((0,0),0.32,fc='#ddd',ec=T)); ax.plot(0,0,'o',color=T,ms=4)
ar(ax,(2.8,0),(3.5,1.2),H,2,12); ax.text(3.5,1.25,r'$\vec F$',color=H); ax.add_patch(Arc((2.8,0),0.7,0.7,theta1=0,theta2=60,color=T,lw=.8)); ax.text(3.2,0.12,r'$\phi$',fontsize=9)
ax.annotate('',xy=(2.8,-0.45),xytext=(0,-0.45),arrowprops=dict(arrowstyle='<->',lw=.8)); ax.text(1.4,-0.75,'$r$ (lengan)',ha='center')
ax.plot([0,0.95],[0,-0.55*0+0],lw=0); ax.text(-0.2,0.45,'sumbu putar',fontsize=8.5)
ax.set_xlim(-0.6,4.1); ax.set_ylim(-1,1.5); sv(f,'c_torsi.png')
# 3 rotor molekul + spektrum
f,axs=plt.subplots(1,2,figsize=(6.6,2.6),gridspec_kw={'width_ratios':[1,1.6]})
ax=axs[0]; ax.set_aspect('equal'); ax.axis('off')
ax.add_patch(Circle((-0.55,0),0.28,fc='#555',ec=T)); ax.add_patch(Circle((0.65,0),0.33,fc=H,ec=T)); ax.plot([-0.55,0.65],[0,0],color=T,lw=2,zorder=0)
ax.text(-0.55,-0.6,'C',ha='center'); ax.text(0.65,-0.65,'O',ha='center'); ax.plot(0.06,0,'x',color=B,ms=8,mew=2); ax.text(0.0,0.35,'pusat massa',fontsize=8,ha='center',color=B)
ax.add_patch(Arc((0.06,0),2.3,0.9,theta1=200,theta2=340,color=G,lw=1.5)); ax.text(-0.1,-0.95,'berputar',fontsize=8.5,color=G,ha='center'); ax.set_xlim(-1.3,1.4); ax.set_ylim(-1.2,1)
ax=axs[1]; Bc=1.93; J=np.arange(0,25); kT=207.2
pop=(2*J+1)*np.exp(-Bc*J*(J+1)/kT); lines=2*Bc*(J+1); inten=pop*(1-np.exp(-lines/kT))*(J+1)
for x,y in zip(lines,inten/inten.max()): ax.plot([x,x],[0,y],color=B,lw=1.6)
ax.set_xlabel('bilangan gelombang (cm$^{-1}$)'); ax.set_yticks([]); ax.set_ylabel('serapan'); ax.set_title('spektrum rotasi CO (298 K)',fontsize=9)
for s in ['top','right']: ax.spines[s].set_visible(False)
sv(f,'c_rotor.png')
