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
def q(ax,x,y,s,r=.13,fs=10):
    ax.add_patch(Circle((x,y),r,fc=H if s=='+' else B,ec='k',lw=.6,zorder=5)); ax.text(x,y,s if s=='+' else '−',color='w',ha='center',va='center',fontsize=fs,zorder=6,fontweight='bold')
# garis medan
f,axs=plt.subplots(1,2,figsize=(6.4,3)); Y,X=np.mgrid[-2:2:200j,-2:2:200j]
for ax,ch in zip(axs,[[(0,0,1)],[(-.8,0,1),(.8,0,-1)]]):
    Ex=sum(c*(X-x)/((X-x)**2+(Y-y)**2)**1.5 for x,y,c in ch); Ey=sum(c*(Y-y)/((X-x)**2+(Y-y)**2)**1.5 for x,y,c in ch)
    ax.streamplot(X,Y,Ex,Ey,color=T,linewidth=.8,density=.9,arrowsize=.8)
    for x,y,c in ch: q(ax,x,y,'+' if c>0 else '-',.16)
    ax.set_aspect('equal'); ax.axis('off')
sv(f,'garis.png')
# superposisi segitiga
f,ax=plt.subplots(figsize=(3.6,3.4)); ax.axis('off'); ax.set_aspect('equal')
q(ax,0,0,'+'); q(ax,3,0,'+'); q(ax,0,4,'-'); ax.text(-.3,-.35,'$q_1$'); ax.text(3.1,-.4,'$q_2$'); ax.text(-.5,4.1,'$q_3$')
ax.plot([0,3],[0,0],color='gray',lw=.8,ls=':'); ax.plot([0,0],[0,4],color='gray',lw=.8,ls=':'); ax.text(1.5,-.35,'0,30 m',ha='center',fontsize=8.5); ax.text(.12,2.6,'0,40 m',fontsize=8.5)
ar(ax,(0,0),(-1.6,0),B); ar(ax,(0,0),(0,1.2),B); ar(ax,(0,0),(-1.6,1.2),H,2); ax.text(-1.7,-.35,'$F_{12}$',color=B); ax.text(.1,1.2,'$F_{13}$',color=B); ax.text(-2.1,1.3,'$F$',color=H)
ax.set_xlim(-2.4,3.6); ax.set_ylim(-.7,4.5); sv(f,'super.png')
# pelat + lintasan
f,ax=plt.subplots(figsize=(4.6,2.6)); ax.axis('off')
ax.add_patch(Rectangle((0,1.5),4,.12,fc=H)); ax.add_patch(Rectangle((0,-.12),4,.12,fc=B))
for x in np.arange(.4,4,.6): ar(ax,(x,1.45),(x,.08),'gray',.8,8)
for x in np.arange(.3,4,.6): ax.text(x,1.72,'+',color=H,ha='center'); ax.text(x,-.42,'−',color=B,ha='center')
x=np.linspace(-1,4,50); y=.75+np.where(x>0,.04*x**2,0); ax.plot(x,y,color=G,lw=2); x2=np.linspace(4,5.3,5); ax.plot(x2,.75+.64+.32*(x2-4),color=G,lw=2); ar(ax,(5.2,1.774),(5.3,1.806),G,2)
ax.plot(-1,.75,'o',color=G,ms=5); ax.text(-1,.45,'elektron',ha='center',fontsize=8.5); ax.text(2.6,.5,r'$\vec E$',color='gray'); ax.set_xlim(-1.6,5.6); ax.set_ylim(-.6,2.1); sv(f,'pelat.png')
# gauss
f,ax=plt.subplots(figsize=(3.2,3.2)); ax.axis('off'); ax.set_aspect('equal')
ax.add_patch(Circle((0,0),1.5,fc=M,ec=B,ls='--',lw=1.4))
for a in np.arange(0,360,45): r=np.radians(a); ar(ax,(.25*np.cos(r),.25*np.sin(r)),(2.1*np.cos(r),2.1*np.sin(r)),T,1,9)
q(ax,0,0,'+',.2); ax.text(1.15,-1.45,'permukaan\nGauss',fontsize=8.5,color=B); ax.plot([0,1.06],[0,1.06],color='k',lw=.6); ax.text(.45,.72,'$r$'); ax.set_xlim(-2.3,2.6); ax.set_ylim(-2.3,2.3); sv(f,'gauss.png')
# potensial
f,ax=plt.subplots(figsize=(4.4,2.9)); sp(ax); r=np.linspace(.25,4,200); ax.plot(r,1/r,color=B,lw=2,label='$V \\propto 1/r$'); ax.plot(r,1/r**2,color=H,lw=2,label='$E \\propto 1/r^2$'); ax.set_ylim(0,4); ax.set_xlabel('jarak dari muatan, $r$'); ax.set_xticks([]); ax.set_yticks([]); ax.legend(frameon=False); sv(f,'potensial.png')
# kapasitor + dielektrik
f,axs=plt.subplots(1,2,figsize=(6,2.6))
for ax,d in zip(axs,[0,1]):
    ax.axis('off'); ax.add_patch(Rectangle((0,0),.15,2,fc=H)); ax.add_patch(Rectangle((1.85,0),.15,2,fc=B))
    for y in np.arange(.2,2,.3): ax.text(-.15,y,'+',color=H,ha='center',va='center'); ax.text(2.15,y,'−',color=B,ha='center',va='center')
    if d:
        ax.add_patch(Rectangle((.15,0),1.7,2,fc=M,ec='none'))
        for y in np.arange(.25,2,.38):
            for x in [.45,1,1.55]: ax.add_patch(matplotlib.patches.Ellipse((x,y),.42,.2,fc='w',ec=T,lw=.7)); ax.text(x-.13,y,'−',fontsize=7,ha='center',va='center',color=B); ax.text(x+.13,y,'+',fontsize=7,ha='center',va='center',color=H)
        ax.text(1,-.3,'dengan dielektrik',ha='center',fontsize=9)
    else:
        for y in np.arange(.25,2,.38): ar(ax,(.2,y),(1.8,y),'gray',.8,8)
        ax.text(1,-.3,'hampa',ha='center',fontsize=9)
    ax.set_xlim(-.4,2.4); ax.set_ylim(-.5,2.1)
sv(f,'kapasitor.png')
# seri paralel
def cap(ax,x,y,l):
    ax.plot([x-.08,x-.08],[y-.25,y+.25],color='k',lw=2); ax.plot([x+.08,x+.08],[y-.25,y+.25],color='k',lw=2); ax.text(x,y+.38,l,ha='center',fontsize=9)
f,axs=plt.subplots(1,2,figsize=(6,2)); 
ax=axs[0]; ax.axis('off'); ax.plot([0,.92],[0,0],'k',lw=1); ax.plot([1.08,1.92],[0,0],'k',lw=1); ax.plot([2.08,3],[0,0],'k',lw=1); cap(ax,1,0,'$C_1$'); cap(ax,2,0,'$C_2$'); ax.text(1.5,-.75,'seri',ha='center'); ax.set_xlim(-.2,3.2); ax.set_ylim(-1,1.2)
ax=axs[1]; ax.axis('off'); ax.plot([0,.6],[0,0],'k',lw=1); ax.plot([2.4,3],[0,0],'k',lw=1); ax.plot([.6,.6],[-.5,.5],'k',lw=1); ax.plot([2.4,2.4],[-.5,.5],'k',lw=1)
for y,l in [(.5,'$C_1$'),(-.5,'$C_2$')]: ax.plot([.6,1.42],[y,y],'k',lw=1); ax.plot([1.58,2.4],[y,y],'k',lw=1); cap(ax,1.5,y,l)
ax.text(1.5,-1.25,'paralel',ha='center'); ax.set_xlim(-.2,3.2); ax.set_ylim(-1.4,1.2); sv(f,'rangkaian.png')
# air & hidrasi
f,ax=plt.subplots(figsize=(5.4,2.8)); ax.axis('off'); ax.set_aspect('equal')
def air(ax,x,y,ang,sc=1):
    a=np.radians(ang); ax.add_patch(Circle((x,y),.3*sc,fc=B,ec='k',lw=.5))
    for d in [-52,52]: b=a+np.radians(d); ax.add_patch(Circle((x+.36*sc*np.cos(b),y+.36*sc*np.sin(b)),.17*sc,fc='w',ec='k',lw=.5))
air(ax,0,0,90,1.5); ax.text(0,-.75,'$\\delta-$',ha='center',color=B); ax.text(-.75,.75,'$\\delta+$',color=H,ha='center'); ax.text(.75,.75,'$\\delta+$',color=H,ha='center'); ar(ax,(0,-.35),(0,.95),G,1.6,10); ax.text(.1,1.05,'$\\vec p$',color=G)
q(ax,4,0,'+',.32)
for a in range(0,360,60): r=np.radians(a); air(ax,4+1.05*np.cos(r),1.05*np.sin(r),a)
ax.set_xlim(-1.3,5.8); ax.set_ylim(-1.7,1.7); sv(f,'air.png')
