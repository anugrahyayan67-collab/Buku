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
def fig(wd,h,xl,yl):
    f,ax=plt.subplots(figsize=(wd,h)); ax.axis('off'); ax.set_aspect('equal'); ax.set_xlim(*xl); ax.set_ylim(*yl); return f,ax
def silang(ax,xs,ys,c='#8aa'):
    for x in xs:
        for y in ys: ax.text(x,y,'×',color=c,ha='center',va='center',fontsize=9)
# magnet batang
f,ax=fig(4.4,3.2,(-3,3),(-2.2,2.2)); Y,X=np.mgrid[-2.2:2.2:200j,-3:3:200j]
Bx=0*X; By=0*X
for x0,c in [(-.9,1),(.9,-1)]:
    r3=((X-x0)**2+Y**2+.01)**1.5; Bx+=c*(X-x0)/r3; By+=c*Y/r3
ax.streamplot(X,Y,Bx,By,color=T,linewidth=.8,density=.9,arrowsize=.8)
ax.add_patch(Rectangle((-1,-.25),1,.5,fc=H,ec='k',zorder=5)); ax.add_patch(Rectangle((0,-.25),1,.5,fc=B,ec='k',zorder=5)); ax.text(-.5,0,'U',color='w',ha='center',va='center',zorder=6,fontweight='bold'); ax.text(.5,0,'S',color='w',ha='center',va='center',zorder=6,fontweight='bold'); sv(f,'batang.png')
# lorentz: lingkaran dalam B
f,ax=fig(3.6,3.2,(-2.2,2.6),(-2.1,2.1)); silang(ax,np.arange(-2,2.4,.5),np.arange(-1.9,2,.5))
ax.add_patch(Circle((0,0),1.3,fc='none',ec=B,lw=1.8)); ax.add_patch(Circle((1.3,0),.1,fc=H,zorder=5)); ar(ax,(1.3,0),(1.3,1.0),G,1.8,11); ar(ax,(1.3,0),(.45,0),H,1.8,11)
ax.text(1.42,.9,r'$\vec v$',color=G); ax.text(.65,.12,r'$\vec F$',color=H); ax.text(1.45,-.3,'$+q$',fontsize=9); ax.plot([0,-.92],[0,-.92],color='k',lw=.6); ax.text(-.4,-.72,'$r$'); ax.text(2.0,1.8,r'$\vec B$ masuk',fontsize=8.5,ha='center'); sv(f,'lingkaran.png')
# spektrometer massa
f,ax=fig(5,3,(-.5,6.3),(-.4,3.3)); silang(ax,np.arange(2.6,6.2,.45),np.arange(.1,2.6,.45))
ax.add_patch(Rectangle((2.3,2.75),3.9,.12,fc='#555')); ax.add_patch(Rectangle((0,1.9),1.6,.1,fc=H)); ax.add_patch(Rectangle((0,3.0),1.6,.1,fc=B)); ax.text(.8,1.45,'pemilih\nkecepatan',ha='center',va='center',fontsize=8.5)
ar(ax,(-.4,2.5),(2.6,2.5),'k',1.2,9); ax.plot([2.6,2.6],[2.5,2.75],color='k',lw=0)
for r,c,l in [(.75,B,'$m_1$'),(1.1,H,'$m_2$')]:
    th=np.linspace(np.pi,0,60); ax.plot(2.9+r+r*np.cos(th),2.75-r*np.sin(th),color=c,lw=1.8); ax.text(2.9+2*r,2.95,l,color=c,ha='center',fontsize=9)
ax.plot([2.6,2.9],[2.5,2.75],color='k',lw=1.2); ax.text(4.2,3.15,'detektor',fontsize=8.5,ha='center'); ax.text(-.4,2.65,'ion',fontsize=8.5); sv(f,'spektro.png')
# kawat lurus & solenoide
f,axs=plt.subplots(1,2,figsize=(6.2,2.8))
ax=axs[0]; ax.axis('off'); ax.set_aspect('equal'); ax.set_xlim(-2,2); ax.set_ylim(-1.8,1.8)
for r in [.5,.95,1.45]:
    ax.add_patch(Circle((0,0),r,fc='none',ec=T,lw=.9)); ar(ax,(r,-.02),(r,.08),T,.9,9)
ax.add_patch(Circle((0,0),.14,fc='w',ec=H,lw=1.5)); ax.plot(0,0,'o',color=H,ms=3); ax.text(.2,-.3,'$I$ keluar',fontsize=8.5,color=H); ax.text(1.1,1.25,r'$\vec B$',color=T)
ax=axs[1]; ax.axis('off'); ax.set_xlim(-.5,5); ax.set_ylim(-1.3,1.3)
for x in np.arange(.3,4,.33): ax.add_patch(Circle((x,.6),.1,fc='w',ec=H)); ax.plot(x,.6,'o',color=H,ms=2); ax.add_patch(Circle((x,-.6),.1,fc='w',ec=H)); ax.text(x,-.6,'×',color=H,ha='center',va='center',fontsize=6)
for y in [-.3,0,.3]: ar(ax,(.1,y),(4.2,y),T,1,9)
ax.text(4.35,0,r'$\vec B$',color=T,va='center'); sv(f,'medanarus.png')
# torsi simpal / momen
f,ax=fig(3.8,2.6,(-2.4,2.6),(-1.5,1.6))
for y in [-1.1,-.4,.3,1.0]: ar(ax,(-2.2,y),(2.2,y),'#bbb',.8,8)
ax.plot([-1,1],[-.7,.7],color=H,lw=4,solid_capstyle='round'); ar(ax,(0,0),(-.75,1.07),G,1.8,11); ax.text(-1.0,1.15,r'$\vec\mu$',color=G); ax.text(2.25,1.0,r'$\vec B$',color='gray',va='center'); ax.add_patch(Arc((0,0),1.1,1.1,theta1=0,theta2=125,color='k',lw=.7)); ax.text(.35,.55,r'$\theta$'); ax.text(.3,-.75,'simpal arus\n(tampak samping)',fontsize=8,ha='left'); sv(f,'torsi.png')
# zeeman
f,ax=plt.subplots(figsize=(4.2,2.8)); sp(ax); b=np.linspace(0,1,10); ax.plot(b,.5*b,color=H,lw=2); ax.plot(b,-.5*b,color=B,lw=2); ax.set_xlabel('medan magnet $B$'); ax.set_ylabel('energi'); ax.set_xticks([]); ax.set_yticks([])
ax.text(.55,.38,'spin berlawanan medan',fontsize=8.5,color=H,rotation=20); ax.text(.55,-.2,'spin searah medan',fontsize=8.5,color=B,rotation=-20); ax.annotate('',xy=(.9,.45),xytext=(.9,-.45),arrowprops=dict(arrowstyle='<->',color='k')); ax.text(.92,0,r'$\Delta E = hf$',fontsize=9,va='center'); ax.set_xlim(0,1.25); sv(f,'zeeman.png')
# batang pada rel
f,ax=fig(4.6,2.6,(-.6,5),(-.6,2.4)); silang(ax,np.arange(.3,4.6,.5),np.arange(.25,1.8,.5))
ax.plot([0,4.5],[0,0],color='k',lw=2); ax.plot([0,4.5],[2,2],color='k',lw=2); ax.plot([0,0],[0,2],color='k',lw=1.2); ax.add_patch(Rectangle((-.12,.7),.24,.6,fc='w',ec='k')); ax.text(-.45,1,'$R$',ha='center',va='center')
ax.add_patch(Rectangle((2.9,-.15),.18,2.3,fc=H,ec='k')); ar(ax,(3.1,1),(4.1,1),G,1.8,11); ax.text(4.15,1,r'$\vec v$',color=G,va='center'); ar(ax,(1.2,2.15),(.5,2.15),B,1.3,9); ax.text(.85,2.28,'$I$',color=B,ha='center'); ax.annotate('',xy=(3.35,0),xytext=(3.35,2),arrowprops=dict(arrowstyle='<->',color='k',lw=.7)); ax.text(3.45,.4,'$L$'); sv(f,'rel.png')
# generator sinus
f,ax=plt.subplots(figsize=(4.6,2.6)); sp(ax); t=np.linspace(0,2,300); ax.plot(t,np.sin(2*np.pi*t),color=B,lw=2); ax.axhline(0,color='k',lw=.6); ax.plot([0,2],[.707,.707],color=H,ls='--',lw=1); ax.text(2.05,.6,'nilai rms',color=H,fontsize=8.5,va='center'); ax.text(2.05,1,'puncak',fontsize=8.5,va='center')
ax.set_xlabel('waktu (periode)'); ax.set_ylabel('tegangan'); ax.set_yticks([]); ax.set_xlim(0,2.5); sv(f,'ac.png')
# trafo
f,ax=fig(4.2,2.6,(-1.6,5.6),(-.4,3))
ax.add_patch(Rectangle((0,0),4,2.6,fc='#bbb',ec='k')); ax.add_patch(Rectangle((.7,.6),2.6,1.4,fc='w',ec='k'))
for y in np.arange(.75,1.95,.2): ax.plot([-.1,.8],[y,y+.08],color=H,lw=2)
for y in np.arange(.75,1.95,.4): ax.plot([3.2,4.1],[y,y+.08],color=B,lw=2)
ax.text(-.9,1.3,'primer\n$N_p$',ha='center',va='center',fontsize=9,color=H); ax.text(4.9,1.3,'sekunder\n$N_s$',ha='center',va='center',fontsize=9,color=B); ax.text(2,2.3,'inti besi',ha='center',va='center',fontsize=8.5); sv(f,'trafo.png')
# spektrum EM
f,ax=plt.subplots(figsize=(6.2,1.5)); ax.set_xlim(4,21); ax.set_ylim(0,1); ax.set_yticks([])
bd=[(4,9,'radio','#dfe9f5'),(9,11.5,'gelombang\nmikro','#c3d8ee'),(11.5,14.6,'inframerah','#f3dccb'),(14.6,14.9,'','#f0d24a'),(14.9,16.5,'ultraviolet','#d9cfee'),(16.5,19,'sinar-X','#cfe3f5'),(19,21,'sinar\ngama','#b9cde3')]
for a,b,l,c in bd: ax.add_patch(Rectangle((a,0),b-a,1,fc=c,ec='k',lw=.5)); ax.text((a+b)/2,.5,l,ha='center',va='center',fontsize=8)
ax.annotate('tampak',xy=(14.75,1),xytext=(14.75,1.25),ha='center',fontsize=8,arrowprops=dict(arrowstyle='-',lw=.6),annotation_clip=False)
ax.set_xticks(range(4,22,2)); ax.set_xticklabels([f'$10^{{{i}}}$' for i in range(4,22,2)]); ax.set_xlabel('frekuensi (Hz)'); sv(f,'spektrum.png')
