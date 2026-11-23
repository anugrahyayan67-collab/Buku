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
def res(ax,a,b,l='',off=.28):
    a=np.array(a,float); b=np.array(b,float); d=b-a; L=np.hypot(*d); u=d/L; n=np.array([-u[1],u[0]]); m=(a+b)/2; h=.35
    p0=m-u*h; pts=[a,p0]+[p0+u*(2*h)*(i+.5)/6+n*.1*(1 if i%2 else -1) for i in range(6)]+[m+u*h,b]; pts=np.array(pts); ax.plot(pts[:,0],pts[:,1],'k',lw=1.2)
    if l: ax.text(*(m+n*off),l,ha='center',va='center',fontsize=9)
def bat(ax,a,b,l='',off=.38):
    a=np.array(a,float); b=np.array(b,float); d=b-a; L=np.hypot(*d); u=d/L; n=np.array([-u[1],u[0]]); m=(a+b)/2
    ax.plot(*zip(a,m-u*.06),color='k',lw=1.2); ax.plot(*zip(m+u*.06,b),color='k',lw=1.2)
    ax.plot(*zip(m-u*.06-n*.1,m-u*.06+n*.1),color='k',lw=2.5); ax.plot(*zip(m+u*.06-n*.22,m+u*.06+n*.22),color='k',lw=1.2)
    if l: ax.text(*(m+n*off),l,ha='center',va='center',fontsize=9)
def w(ax,*pts): p=np.array(pts); ax.plot(p[:,0],p[:,1],'k',lw=1.2)
def fig(wd,h,xl,yl):
    f,ax=plt.subplots(figsize=(wd,h)); ax.axis('off'); ax.set_aspect('equal'); ax.set_xlim(*xl); ax.set_ylim(*yl); return f,ax
# hanyut
f,ax=fig(5,1.6,(-.3,5.3),(-.5,1.3)); ax.add_patch(Rectangle((0,0),5,.9,fc=M,ec=T)); rng=np.random.default_rng(1)
for x,y in zip(rng.uniform(.3,4.7,14),rng.uniform(.15,.75,14)): ax.add_patch(Circle((x,y),.06,fc=B)); ar(ax,(x,y),(x-.3,y),B,1,7)
ar(ax,(1.5,1.1),(3.5,1.1),H,1.6,10); ax.text(2.5,1.22,'arus $I$ (dan medan $E$)',ha='center',va='bottom',fontsize=9,color=H); ax.text(2.5,-.3,'elektron hanyut berlawanan arah arus',ha='center',fontsize=9,color=B); sv(f,'hanyut.png')
# V-I
f,ax=plt.subplots(figsize=(4.2,2.9)); sp(ax); V=np.linspace(0,1,100); ax.plot(V,V,color=B,lw=2,label='penghantar ohmik'); ax.plot(V,.9*V**.55,color=H,lw=2,label='lampu pijar'); ax.plot(V,.02*(np.exp(V*4.2)-1),color=G,lw=2,label='diode')
ax.set_xlabel('tegangan $V$'); ax.set_ylabel('arus $I$'); ax.set_xticks([]); ax.set_yticks([]); ax.set_ylim(0,1.15); ax.legend(frameon=False,fontsize=9); sv(f,'vi.png')
# seri paralel
f,ax=fig(6.2,2.2,(-.3,8.6),(-1.2,1.4))
w(ax,(0,0),(.3,0)); res(ax,(.3,0),(1.5,0),'$R_1$'); res(ax,(1.5,0),(2.7,0),'$R_2$'); w(ax,(2.7,0),(3,0)); ax.text(1.5,-.9,'seri: $R = R_1 + R_2$',ha='center',fontsize=9)
w(ax,(4.6,0),(5,0)); w(ax,(5,.6),(5,-.6)); w(ax,(7.6,.6),(7.6,-.6)); w(ax,(7.6,0),(8,0)); w(ax,(5,.6),(5.7,.6)); w(ax,(6.9,.6),(7.6,.6)); w(ax,(5,-.6),(5.7,-.6)); w(ax,(6.9,-.6),(7.6,-.6))
res(ax,(5.7,.6),(6.9,.6),'$R_1$'); res(ax,(5.7,-.6),(6.9,-.6),'$R_2$',.28); ax.text(6.3,-1.05,'paralel: $1/R = 1/R_1 + 1/R_2$',ha='center',fontsize=9); sv(f,'seripar.png')
# ggl
f,ax=fig(3.6,2.6,(-.9,3.6),(-.4,2.7)); bat(ax,(0,.3),(0,1.1),r'$\varepsilon$',.55); res(ax,(0,1.1),(0,2),'$r$',-.3); w(ax,(0,2),(3,2)); res(ax,(3,2),(3,0),'$R$',-.3); w(ax,(3,0),(0,0),(0,.3))
ax.add_patch(Rectangle((-.35,.15),1.15,1.95,fc='none',ec=B,ls='--')); ax.text(-.42,2.25,'baterai',color=B,fontsize=8.5); ar(ax,(1.2,2.15),(1.9,2.15),H,1.4,9); ax.text(1.55,2.3,'$I$',color=H,ha='center'); sv(f,'ggl.png')
# kirchhoff
f,ax=fig(4.6,2.8,(-.6,4.6),(-.5,2.6))
bat(ax,(0,.6),(0,1.4),r'$\varepsilon_1$',-.45); w(ax,(0,0),(0,.6)); w(ax,(0,1.4),(0,2)); res(ax,(0,2),(2,2),'$R_1$'); res(ax,(2,2),(4,2),'$R_2$'); bat(ax,(4,.6),(4,1.4),r'$\varepsilon_2$',.45); w(ax,(4,2),(4,1.4)); w(ax,(4,.6),(4,0),(0,0)); res(ax,(2,2),(2,0),'$R_3$',-.32)
ar(ax,(.6,1.75),(1.3,1.75),H,1.3,9); ax.text(.95,1.52,'$I_1$',color=H,ha='center'); ar(ax,(3.4,1.75),(2.7,1.75),H,1.3,9); ax.text(3.05,1.52,'$I_2$',color=H,ha='center'); ar(ax,(2.3,1.5),(2.3,.8),H,1.3,9); ax.text(2.5,1.15,'$I_3$',color=H)
ax.plot(2,2,'ko',ms=4); ax.plot(2,0,'ko',ms=4); sv(f,'kirchhoff.png')
# wheatstone
f,ax=fig(3.8,3.2,(-.8,4.8),(-1.9,2.3)); A=(0,0);Bp=(2,1.6);C=(4,0);D=(2,-1.6)
res(ax,A,Bp,'$R_1$',.32); res(ax,Bp,C,'$R_2$',.32); res(ax,A,D,'$R_3$',-.32); res(ax,D,C,'$R_x$',-.32); w(ax,Bp,(2,.35)); w(ax,D,(2,-.35)); ax.add_patch(Circle((2,0),.35,fc='w',ec='k')); ax.text(2,0,'G',ha='center',va='center',fontsize=9)
w(ax,A,(-.5,0),(-.5,-1.8),(1.6,-1.8)); w(ax,C,(4.5,0),(4.5,-1.8),(2.4,-1.8)); bat(ax,(1.6,-1.8),(2.4,-1.8)); sv(f,'wheatstone.png')
# RC
f,ax=plt.subplots(figsize=(4.6,2.9)); sp(ax); t=np.linspace(0,5,200); ax.plot(t,1-np.exp(-t),color=B,lw=2,label='mengisi'); ax.plot(t,np.exp(-t),color=H,lw=2,label='mengosongkan'); ax.axhline(.632,color='gray',ls=':',lw=.8); ax.axhline(.368,color='gray',ls=':',lw=.8); ax.axvline(1,color='gray',ls=':',lw=.8)
ax.set_xlabel(r'waktu ($t/\tau$)'); ax.set_ylabel('$V_C/V_0$'); ax.set_yticks([0,.368,.632,1]); ax.set_yticklabels(['0','0,37','0,63','1']); ax.legend(frameon=False,fontsize=9,loc='center right'); sv(f,'rc.png')
# sel Daniell
f,ax=fig(5,3,(-.5,6.5),(-.9,3.7))
for x0,c,l,ion in [(0,W,'Zn','Zn$^{2+}$'),(3.8,'#f3dccb','Cu','Cu$^{2+}$')]:
    ax.add_patch(Rectangle((x0,0),2.2,1.6,fc=c,ec='k')); ax.plot([x0,x0],[0,2.1],'k'); ax.plot([x0+2.2]*2,[0,2.1],'k'); ax.add_patch(Rectangle((x0+.9,.3),.4,2.3,fc='#999' if l=='Zn' else H,ec='k')); ax.text(x0+1.1,2.75,l,ha='center',fontsize=9); ax.text(x0+.45,.7,ion,ha='center',fontsize=8.5)
w(ax,(1.1,2.95),(1.1,3.3),(4.9,3.3),(4.9,2.95)); ar(ax,(2.4,3.3),(3.6,3.3),B,1.6,10); ax.text(3,3.42,'e$^-$',ha='center',color=B)
ax.plot([1.9,1.9,4.1,4.1],[.5,2.3,2.3,.5],color=G,lw=5,solid_joinstyle='round'); ax.text(3,2.5,'jembatan garam',ha='center',fontsize=8.5,color=G)
ax.text(1.1,-.5,'anode (−)\noksidasi',ha='center',fontsize=8.5); ax.text(4.9,-.5,'katode (+)\nreduksi',ha='center',fontsize=8.5); sv(f,'sel.png')
