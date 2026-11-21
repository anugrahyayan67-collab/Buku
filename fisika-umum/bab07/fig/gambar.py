import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch as FA, Rectangle, Circle, Arc, Polygon
plt.rcParams.update({'font.family':'Liberation Sans','font.size':10,'mathtext.fontset':'dejavusans'})
B='#1b75bc'; T='#17355e'; M='#e9f2fa'; H='#b5541c'; W='#cfe3f5'
def ar(ax,a,b,c='k',lw=1.6,ms=13,ls='-'): ax.add_patch(FA(a,b,arrowstyle='-|>',mutation_scale=ms,color=c,lw=lw,ls=ls,shrinkA=0,shrinkB=0))
def dar(ax,a,b,c='k'): ar(ax,a,b,c,1,8); ar(ax,b,a,c,1,8)
def sv(f,n): f.savefig(n,dpi=220,bbox_inches='tight'); plt.close(f)
def clean(ax): ax.set_aspect('equal'); ax.axis('off')
def sp(ax):
    for s in ('top','right'): ax.spines[s].set_visible(False)
# 1 garis arus
f,axs=plt.subplots(1,2,figsize=(6.4,1.9)); x=np.linspace(0,4,200)
ax=axs[0]; clean(ax)
for y in np.linspace(.15,1.05,6): ax.plot(x,y+0*x,color=B,lw=1.2); ar(ax,(3.7,y),(4,y),B,1.2,8)
ax.plot([0,4],[0,0],'k',lw=1.5); ax.plot([0,4],[1.2,1.2],'k',lw=1.5); ax.set_title('laminar',fontsize=9.5); ax.set_ylim(-.1,1.3)
ax=axs[1]; clean(ax); rng=np.random.default_rng(3)
for y in np.linspace(.15,1.05,6):
    yy=y+np.where(x>1,.13*np.sin(6*x+rng.uniform(0,6))*np.sin(2.3*x+rng.uniform(0,6))*(x-1)/1.5,0); ax.plot(x,np.clip(yy,.03,1.17),color=B,lw=1.2)
ax.plot([0,4],[0,0],'k',lw=1.5); ax.plot([0,4],[1.2,1.2],'k',lw=1.5); ax.set_title('turbulen',fontsize=9.5); ax.set_ylim(-.1,1.3); sv(f,'garisarus.png')
# 2 kontinuitas
def pipe(ax,y0=0,fill=W):
    xs=[0,2,3,5]; top=[1,1,.4,.4]; bot=[-1,-1,-.4,-.4]
    ax.fill_between(xs,[b+y0 for b in bot],[t+y0 for t in top],color=fill); ax.plot(xs,[t+y0 for t in top],'k',lw=1.5); ax.plot(xs,[b+y0 for b in bot],'k',lw=1.5)
f,ax=plt.subplots(figsize=(5.2,2.2)); clean(ax); pipe(ax)
ar(ax,(.5,0),(1.3,0),H,2); ax.text(.7,.2,'$v_1$',color=H); ar(ax,(3.3,0),(4.8,0),H,2); ax.text(3.9,.12,'$v_2$',color=H)
ax.text(1,-.65,'$A_1$'); ax.text(4,-.3,'$A_2$',fontsize=9); ax.text(2.5,-1.4,'$A_1v_1 = A_2v_2$',ha='center'); ax.set_xlim(-.2,5.2); ax.set_ylim(-1.7,1.2); sv(f,'kontinu.png')
# 3 bernoulli
f,ax=plt.subplots(figsize=(5.6,3)); clean(ax)
xs=np.linspace(0,6,100); c=.4+1.6/(1+np.exp(-(xs-3)*2.5)); hw=.55-.3/(1+np.exp(-(xs-3)*2.5))
ax.fill_between(xs,c-hw,c+hw,color=W); ax.plot(xs,c+hw,'k',lw=1.5); ax.plot(xs,c-hw,'k',lw=1.5)
ar(ax,(.3,.4),(1.1,.4),H,2); ax.text(.5,.55,'$v_1$',color=H); ar(ax,(4.7,2.0),(5.8,2.0),H,2); ax.text(5.1,2.1,'$v_2$',color=H,fontsize=9)
ax.text(.2,1.1,'$p_1$'); ax.text(4.8,2.45,'$p_2$'); ax.plot([-.3,6.3],[-.5,-.5],color='gray',ls='--')
dar(ax,(1.5,-.5),(1.5,.4)); ax.text(1.6,-.2,'$y_1$'); dar(ax,(4.3,-.5),(4.3,2.0)); ax.text(4.4,.6,'$y_2$')
ax.set_xlim(-.4,6.4); ax.set_ylim(-.7,2.8); sv(f,'bernoulli.png')
# 4 torricelli
f,ax=plt.subplots(figsize=(4.8,2.8)); clean(ax)
ax.add_patch(Rectangle((0,0),1.6,2.4,fc=W,ec='none')); ax.plot([0,0,1.6],[2.8,0,0],'k',lw=1.5); ax.plot([1.6,1.6],[2.8,1.1],'k',lw=1.5); ax.plot([1.6,1.6],[.9,0],'k',lw=1.5)
x=np.linspace(0,2.4,50); ax.plot(1.6+x,1.0-.17*x**2,color=B,lw=2.5); ax.plot([-.3,4.5],[0,0],'k',lw=1.2)
dar(ax,(-.25,1.0),(-.25,2.4)); ax.text(-.6,1.65,'$h$'); ar(ax,(1.7,1.0),(2.4,1.0),H,1.8); ax.text(1.9,1.15,r'$v = \sqrt{2gh}$',color=H,fontsize=9)
ax.set_xlim(-.8,4.6); ax.set_ylim(-.2,2.9); sv(f,'torricelli.png')
# 5 venturi
f,ax=plt.subplots(figsize=(5.4,2.8)); clean(ax)
xs=[0,1.6,2.4,3.2,4,5.6]; top=[.6,.6,.25,.25,.6,.6]; ax.fill_between(xs,[-t for t in top],top,color=W); ax.plot(xs,top,'k',lw=1.5); ax.plot(xs,[-t for t in top],'k',lw=1.5)
for x0,hh in [(.8,1.5),(2.8,.75)]:
    ax.add_patch(Rectangle((x0-.08,.6 if x0<2 else .25),.16,hh,fc=W,ec='none')); ax.plot([x0-.08,x0-.08],[.6 if x0<2 else .25,2.4],'k',lw=1); ax.plot([x0+.08,x0+.08],[.6 if x0<2 else .25,2.4],'k',lw=1)
ax.plot([.5,3.3],[2.1,2.1],color='gray',ls=':'); ax.plot([2.5,3.3],[1.0,1.0],color='gray',ls=':'); dar(ax,(3.2,1.0),(3.2,2.1)); ax.text(3.3,1.5,'$h$')
ar(ax,(.2,0),(1.0,0),H,1.8); ar(ax,(2.45,0),(3.4,0),H,1.8); ax.text(.3,-.4,'lambat, $p$ besar',fontsize=8.5); ax.text(2.2,-.55,'cepat, $p$ kecil',fontsize=8.5)
ax.set_xlim(-.1,5.7); ax.set_ylim(-.9,2.5); sv(f,'venturi.png')
# 6 sifon
f,ax=plt.subplots(figsize=(4.4,3)); clean(ax)
ax.add_patch(Rectangle((0,1.2),1.6,1.0,fc=W,ec='none')); ax.plot([0,0,1.6,1.6],[2.6,1.2,1.2,2.6],'k',lw=1.5)
ax.plot([1.0,1.0,2.6,2.6],[1.5,3.0,3.0,.2],color=B,lw=4,solid_joinstyle='round'); ar(ax,(2.6,.15),(2.6,-.35),H,1.8)
ax.plot([-.2,3.4],[2.2,2.2],color='gray',ls=':'); dar(ax,(3.1,.2),(3.1,2.2)); ax.text(3.2,1.2,'$h$'); dar(ax,(.5,2.2),(.5,3.0)); ax.text(.1,2.55,'$H$')
ax.set_xlim(-.3,3.6); ax.set_ylim(-.5,3.3); sv(f,'sifon.png')
# 7 sayap
f,ax=plt.subplots(figsize=(5.6,2.4)); clean(ax); x=np.linspace(-2.5,3.5,200)
t=np.linspace(0,1,80); xu=2.4*t-.6; yu=.42*np.sqrt(t)*(1-t)**.8+.05; yl=-.1*np.sqrt(t)*(1-t)+.02*0
ax.fill(np.r_[xu,xu[::-1]],np.r_[yu,yl[::-1]],fc='#bbb',ec='k')
for y0 in (.25,.5,.8,1.15): ax.plot(x,y0+.33*np.exp(-((x-.3)/.9)**2)*np.exp(-(y0-.25))-.1*(x>1)*(1-np.exp(-(x-1)))*np.exp(-(y0-.25)),color=B,lw=1.1)
for y0 in (-.2,-.5,-.85): ax.plot(x,y0-.06*np.exp(-((x-.2)/1.0)**2)-.1*(x>1)*(1-np.exp(-(x-1)))*np.exp(y0+.2),color=B,lw=1.1)
ar(ax,(.4,.5),(.4,1.75),H,2.4); ax.text(.52,1.6,'gaya angkat',color=H,fontsize=9); ax.text(-2.4,1.45,'cepat, tekanan rendah',fontsize=8.5); ax.text(-2.4,-1.15,'lambat, tekanan tinggi',fontsize=8.5)
ax.text(2.2,-.75,'udara dibelokkan\nke bawah',fontsize=8,color=T); ax.set_xlim(-2.6,3.6); ax.set_ylim(-1.3,1.9); sv(f,'sayap.png')
# 8 viskos
f,ax=plt.subplots(figsize=(4.8,2.2)); clean(ax)
ax.add_patch(Rectangle((0,0),4,1.2,fc=W,ec='none')); ax.add_patch(Rectangle((0,1.2),4,.15,fc=T)); ax.add_patch(Rectangle((0,-.15),4,.15,fc='#888'))
for y in np.linspace(.2,1.1,5): ar(ax,(.8,y),(.8+1.6*y/1.2,y),H,1.3,9)
ax.plot([.8,.8+1.6],[0,1.2],color=H,lw=.8,ls='--'); ar(ax,(4.1,1.27),(4.9,1.27),B,2); ax.text(4.3,1.45,'$F$, $v$',color=B); dar(ax,(3.6,0),(3.6,1.2)); ax.text(3.7,.55,'$d$'); ax.text(.1,-.5,'pelat diam',fontsize=8.5)
ax.set_xlim(-.1,5.1); ax.set_ylim(-.7,1.8); sv(f,'viskos.png')
# 9 poiseuille
f,ax=plt.subplots(figsize=(5,2)); clean(ax); ax.add_patch(Rectangle((0,-1),5,2,fc=W,ec='none')); ax.plot([0,5],[1,1],'k',lw=1.5); ax.plot([0,5],[-1,-1],'k',lw=1.5)
ys=np.linspace(-.9,.9,9)
for y in ys: ar(ax,(1.5,y),(1.5+2.2*(1-y*y),y),H,1.2,8)
yy=np.linspace(-1,1,50); ax.plot(1.5+2.2*(1-yy**2),yy,color=H,lw=1); ax.text(3.8,.1,r'$v_{maks}$',color=H,fontsize=9); ax.text(.15,.6,'$p_1$'); ax.text(4.6,.6,'$p_2$'); ax.plot([0,5],[0,0],color='gray',ls='-.',lw=.6)
ax.set_xlim(-.1,5.1); ax.set_ylim(-1.2,1.2); sv(f,'poiseuille.png')
# 10 r4
f,ax=plt.subplots(figsize=(4.6,2.8)); r=np.linspace(.4,1.2,100); ax.plot(r,r**4,color=B,lw=2.2)
for rr in (.5,.8,1.0): ax.plot([rr],[rr**4],'o',color=H); ax.text(rr+.02,rr**4-.12,f'{rr**4*100:.0f}%'.replace('.',','),fontsize=9)
ax.set_xlabel('jari-jari / jari-jari semula'); ax.set_ylabel('debit / debit semula'); ax.set_xlim(.4,1.2); ax.set_ylim(0,2.1)
ax.set_xticks([.4,.6,.8,1,1.2]); ax.set_xticklabels(['0,4','0,6','0,8','1,0','1,2']); ax.set_yticks([0,.5,1,1.5,2]); ax.set_yticklabels(['0','0,5','1,0','1,5','2,0']); sp(ax); sv(f,'r4.png')
# 11 stokes
f,ax=plt.subplots(figsize=(3,3)); clean(ax); ax.add_patch(Rectangle((-1.5,-1.9),3,3.8,fc=W,ec='none')); ax.add_patch(Circle((0,0),.4,fc='#888',ec='k'))
ar(ax,(0,0),(0,-1.4),T,2.2); ax.text(.12,-1.3,'$mg$',color=T); ar(ax,(-.12,.3),(-.12,1.0),B,2); ax.text(-1.25,.75,'$F_{apung}$',color=B,fontsize=9); ar(ax,(.12,.3),(.12,1.35),H,2); ax.text(.25,1.1,r'$6\pi\eta rv$',color=H,fontsize=9)
ar(ax,(1.0,.3),(1.0,-.5),'k',1.2); ax.text(1.08,-.2,'$v$'); ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.9,1.9); sv(f,'stokes.png')
# 12 difusi
f,ax=plt.subplots(figsize=(4.8,3)); x=np.logspace(-9,0,100); ax.loglog(x,x**2/2e-9,color=B,lw=2.2)
for xx,n in [(1e-8,'tebal membran'),(1e-5,'ukuran sel'),(1e-3,'1 mm'),(1e-1,'10 cm')]: ax.plot([xx],[xx**2/2e-9],'o',color=H); ax.text(xx*1.8,xx**2/2e-9*.25,n,fontsize=8.5)
for tt,n in [(1,'1 s'),(3600,'1 jam'),(3.15e7,'1 tahun')]: ax.axhline(tt,color='gray',ls=':',lw=.8); ax.text(1.3e-9,tt*1.4,n,fontsize=8,color='gray')
ax.set_xlabel('jarak (m)'); ax.set_ylabel('waktu difusi (s)'); ax.set_xlim(1e-9,1); sp(ax); sv(f,'difusi.png')
# 13 aspirator
f,ax=plt.subplots(figsize=(3.2,3.2)); clean(ax)
ax.fill([.7,1.3,1.1,1.1,1.5,1.5,.5,.5,.9,.9],[3,3,2,1.6,.6,0,0,.6,1.6,2],fc=W,ec='k',lw=1.3)
ax.fill([1.1,2.4,2.4,1.1],[1.9,1.9,1.7,1.7],fc='w',ec='k',lw=1.3); ar(ax,(1,3.5),(1,3.05),B,2); ax.text(1.15,3.3,'air masuk',fontsize=8.5); ar(ax,(1,0),(1,-.5),B,2); ax.text(1.15,-.35,'air + udara',fontsize=8.5)
ar(ax,(2.9,1.8),(2.45,1.8),H,1.8); ax.text(2.0,2.05,'udara terisap\ndari labu',fontsize=8,color=H); ax.text(-.9,1.75,'leher sempit:\ncepat, $p$ rendah',fontsize=8)
ax.set_xlim(-1,3.3); ax.set_ylim(-.7,3.7); sv(f,'aspirator.png')
