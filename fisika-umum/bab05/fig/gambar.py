import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch as FA, Rectangle, Circle, Arc, Polygon
plt.rcParams.update({'font.family':'Liberation Sans','font.size':10,'mathtext.fontset':'dejavusans'})
B='#1b75bc'; T='#17355e'; M='#e9f2fa'; H='#b5541c'
def ar(ax,a,b,c='k',lw=1.6,ms=13,ls='-'): ax.add_patch(FA(a,b,arrowstyle='-|>',mutation_scale=ms,color=c,lw=lw,ls=ls,shrinkA=0,shrinkB=0))
def sv(f,n): f.savefig(n,dpi=220,bbox_inches='tight'); plt.close(f)
def clean(ax): ax.set_aspect('equal'); ax.axis('off')
def ball(ax,x,y,r=.3,c=B,t=None): 
    ax.add_patch(Circle((x,y),r,fc=c,ec=T,lw=1.2))
    if t: ax.text(x,y,t,ha='center',va='center',color='w',fontsize=8.5,fontweight='bold')
def sp(ax):
    for s in ('top','right'): ax.spines[s].set_visible(False)
# 1 impuls
f,ax=plt.subplots(figsize=(4.8,2.8)); t=np.linspace(0,4,200); F=1200*np.sin(np.pi*t/4)**2
ax.fill_between(t,F,color=M); ax.plot(t,F,color=B,lw=2.2); ax.plot([0,4],[600,600],color=H,ls='--',lw=1.5); ax.text(4.08,600,'$F_{rata}$',color=H,va='center')
ax.text(2,250,'luas = impuls $J$',ha='center',color=T,fontweight='bold'); ax.set_xlabel('$t$ (ms)'); ax.set_ylabel('$F$ (N)'); ax.set_xlim(0,4.7); ax.set_ylim(0,1350); sp(ax); sv(f,'impuls.png')
# 2 pantul
f,ax=plt.subplots(figsize=(5.6,2.2)); clean(ax)
for x0,lab,vs in [(0,'sebelum',(1.3,H)),(4.4,'sesudah',(-1.0,B))]:
    ax.add_patch(Rectangle((x0+2.2,-.9),.25,1.8,fc='#bbb',ec='k')); ball(ax,x0+1.2,0,.25)
    ar(ax,(x0+1.2,0.5),(x0+1.2+vs[0],0.5),vs[1],2); ax.text(x0+1.2,-1.2,lab,ha='center',fontsize=9)
ax.text(1.8,.72,r'$\vec p_i$',color=H); ax.text(5.0,.72,r'$\vec p_f$',color=B)
ar(ax,(8.6,-.3),(6.3+0.0,-.3),T,2.2); ax.text(7.4,-.75,r'$\Delta\vec p = \vec p_f - \vec p_i$',color=T,ha='center',fontsize=9)
ax.set_xlim(-.3,9); ax.set_ylim(-1.5,1.2); sv(f,'pantul.png')
# 3 sistem
f,ax=plt.subplots(figsize=(4.6,2.4)); clean(ax)
ax.add_patch(plt.matplotlib.patches.Ellipse((2.5,0),5.6,2.4,fc='none',ec='gray',ls='--')); ax.text(2.5,1.35,'sistem',ha='center',color='gray',fontsize=9)
ball(ax,1,0,.38,B,'1'); ball(ax,4,0,.38,T,'2')
ar(ax,(1.4,.12),(2.3,.12),H,2); ar(ax,(3.6,-.12),(2.7,-.12),H,2); ax.text(1.85,.32,r'$\vec F_{2\,pada\,1}$',color=H,fontsize=8.5,ha='center'); ax.text(3.15,-.5,r'$\vec F_{1\,pada\,2}$',color=H,fontsize=8.5,ha='center')
ar(ax,(4,-.4),(4.9,-1.7),'k',1.3); ax.text(5,-1.75,r'$\vec F_{luar}$',fontsize=9)
ax.set_xlim(-.6,5.9); ax.set_ylim(-2,1.6); sv(f,'sistem.png')
# 4 rekoil
f,ax=plt.subplots(figsize=(5.8,2)); clean(ax)
for y0,lab in [(1.3,'sebelum: $p = 0$'),(0,'sesudah: $p$ tetap $0$')]:
    ax.add_patch(Rectangle((1,y0-.12),2.2,.24,fc=T,ec='k')); ax.add_patch(Rectangle((1,y0-.5),.35,.45,fc=T,ec='k')); ax.text(-.9,y0,lab,fontsize=9,va='center')
ax.add_patch(Rectangle((4.6,-.07),.3,.14,fc=H,ec='k')); ar(ax,(5,0),(6.6,0),H,2); ax.text(5.6,.2,r'$m\vec v$',color=H)
ar(ax,(.9,0),(.2,0),B,2); ax.text(.3,.22,r'$M\vec V$',color=B); ax.set_xlim(-1,6.8); ax.set_ylim(-.8,1.8); sv(f,'rekoil.png')
# 5 perahu
f,ax=plt.subplots(figsize=(5.8,2.6)); clean(ax)
for y0,xb,xp,lab in [(1.6,0,2.6,'awal'),(0,-1,.6,'akhir')]:
    ax.fill_between([-2,5],[y0-.5,y0-.5],[y0-.2,y0-.2],color=M); ax.add_patch(Polygon([(xb,y0),(xb+3.2,y0),(xb+2.9,y0-.35),(xb+.3,y0-.35)],fc='#c9a26b',ec='k'))
    ax.add_patch(Circle((xp,y0+.62),.13,fc=B,ec=T)); ax.plot([xp,xp],[y0+.5,y0+.05],color=T,lw=2); ax.text(-2.6,y0,lab,fontsize=9)
    ax.plot([xb+1.6],[y0-.17],'x',color='k',ms=5)
ax.plot([1.53,1.53],[-.6,2.5],color=H,ls=':'); ax.text(1.6,2.45,'pusat massa sistem\n(tidak bergeser)',color=H,fontsize=8,va='top')
ax.plot([1.53],[1.6+.2],'o',color=H,ms=4); ax.plot([1.53],[.2],'o',color=H,ms=4)
ax.set_xlim(-2.8,5.2); ax.set_ylim(-.7,2.7); sv(f,'perahu.png')
# 6 balistik
f,ax=plt.subplots(figsize=(5,2.8)); clean(ax)
ax.plot([1.5,4.5],[3,3],'k',lw=2); ax.plot([3,3],[3,.6],'k',lw=1); ax.add_patch(Rectangle((2.6,0),.8,.6,fc='#c9a26b',ec='k'))
th=np.radians(28); x1=3+2.7*np.sin(th); y1=3-2.7*np.cos(th); ax.plot([3,x1],[3,y1+.25],'k',lw=1,ls='--'); ax.add_patch(Rectangle((x1-.4,y1-.3),.8,.6,fc='#c9a26b',ec='k',alpha=.5,angle=28))
ax.add_patch(Rectangle((.2,.24),.3,.12,fc=H,ec='k')); ar(ax,(.6,.3),(1.9,.3),H,2); ax.text(1,.5,r'$m,\ \vec v$',color=H); ax.text(3,.28,'$M$',ha='center',va='center')
ax.plot([3.4,5.2],[.3,.3],color='gray',ls=':'); ax.plot([4.3,5.2],[y1,y1],color='gray',ls=':'); ar(ax,(5,.3),(5,y1),'k',1,8); ar(ax,(5,y1),(5,.3),'k',1,8); ax.text(5.1,(y1+.3)/2,'$h$')
ax.set_xlim(0,5.5); ax.set_ylim(-.3,3.3); sv(f,'balistik.png')
# 7 lenting
f,ax=plt.subplots(figsize=(6.6,3)); clean(ax)
rows=[(2.2,.3,.3,'massa sama: bertukar kecepatan',(1.2,0),(0,1.2)),(1.1,.45,.2,'berat menumbuk ringan',(1.2,0),(1.0,1.9)),(0,.2,.45,'ringan menumbuk berat',(1.2,0),(-.9,.25))]
for y,r1,r2,lab,(a1,a2),(b1,b2) in rows:
    ball(ax,0,y,r1,B); ball(ax,1.8,y,r2,T); ar(ax,(r1,y),(r1+a1*.6,y),H,1.8)
    ball(ax,5,y,r1,B); ball(ax,6.8,y,r2,T)
    if abs(b1)>.01: ar(ax,(5+np.sign(b1)*r1,y),(5+np.sign(b1)*r1+b1*.6,y),H,1.8)
    if abs(b2)>.01: ar(ax,(6.8+r2,y),(6.8+r2+b2*.6,y),H,1.8)
    ax.text(3.4,y,lab,ha='center',va='center',fontsize=8.5)
ax.text(.9,2.85,'sebelum',ha='center',fontsize=9,color='gray'); ax.text(6,2.85,'sesudah',ha='center',fontsize=9,color='gray')
ax.set_xlim(-1.6,8.6); ax.set_ylim(-.6,3.1); sv(f,'lenting.png')
# 8 moderator
f,ax=plt.subplots(figsize=(4.8,2.9)); A=np.logspace(0,2.4,200); ax.semilogx(A,4*A/(1+A)**2,color=B,lw=2.2)
for a,n in [(1,'H'),(2,'D'),(12,'C'),(207,'Pb')]: ax.plot([a],[4*a/(1+a)**2],'o',color=H); ax.text(a*1.12,4*a/(1+a)**2+.03,n,fontsize=9)
ax.set_xlabel('massa inti sasaran / massa neutron'); ax.set_ylabel('bagian energi yang dipindahkan'); ax.set_ylim(0,1.12); ax.set_yticks([0,.5,1]); ax.set_yticklabels(['0','0,5','1']); sp(ax); sv(f,'moderator.png')
# 9 simpang
f,ax=plt.subplots(figsize=(3.8,3.4)); clean(ax)
ax.add_patch(Rectangle((-2.6,-.25),.9,.5,fc=B,ec=T)); ar(ax,(-1.6,0),(-.4,0),B,2); ax.text(-1.2,.2,r'$\vec p_1$',color=B)
ax.add_patch(Rectangle((-.25,-2.6),.5,.9,fc=T,ec='k')); ar(ax,(0,-1.6),(0,-.4),T,2); ax.text(.15,-1.2,r'$\vec p_2$',color=T)
ar(ax,(0,0),(1.6,1.6),H,2.4); ax.text(1.7,1.6,r'$\vec p_1 + \vec p_2$',color=H); ax.add_patch(Arc((0,0),1.2,1.2,theta1=0,theta2=45,color='k')); ax.text(.75,.22,r'$\theta$')
ax.plot([0,2],[0,0],color='gray',ls=':'); ax.set_xlim(-2.8,3); ax.set_ylim(-2.8,2.2); sv(f,'simpang.png')
# 10 biliar
f,ax=plt.subplots(figsize=(5,2.6)); clean(ax)
ball(ax,-2.2,0,.28,'w'); ar(ax,(-1.9,0),(-.9,0),H,2); ball(ax,0,0,.28,T)
a1=np.radians(30); a2=np.radians(-60)
ar(ax,(0.1,.2),(2.2*np.cos(a1),2.2*np.sin(a1)+.2),B,2); ar(ax,(.15,-.1),(1.3*np.cos(a2)+.15,1.3*np.sin(a2)-.1),T,2)
ax.plot([0,2.6],[0,0],color='gray',ls=':'); ax.text(1.0,.27,'30°',fontsize=9); ax.text(.75,-.5,'60°',fontsize=9); ax.text(2.1,1.35,r'$\vec v_1^{\,\prime}$',color=B); ax.text(.95,-1.25,r'$\vec v_2^{\,\prime}$',color=T)
ax.add_patch(Rectangle((.18,-.02),.16,.16,fc='none',ec='k',lw=.8,angle=-60+0)); ax.set_xlim(-2.7,2.9); ax.set_ylim(-1.5,1.6); sv(f,'biliar.png')
# 11 pm
f,ax=plt.subplots(figsize=(5.6,1.9)); clean(ax)
ax.plot([0,4],[0,0],'k',lw=1.2); ball(ax,0,0,.22,B); ball(ax,4,0,.38,T); ax.plot([3],[0],'x',color=H,ms=9,mew=2.2); ax.text(3,.42,'PM',color=H,ha='center',fontsize=9)
ax.text(0,-.6,'2,0 kg\n$x = 0$',ha='center',fontsize=8.5); ax.text(4,-.75,'6,0 kg\n$x = 4{,}0$ m',ha='center',fontsize=8.5); ax.text(3,-.45,'3,0 m',ha='center',fontsize=8.5,color=H)
ax.set_xlim(-.8,4.9); ax.set_ylim(-1.1,.8); sv(f,'pm.png')
# 12 pecah
f,ax=plt.subplots(figsize=(6,2.6)); x=np.linspace(0,200,200); y=4*40*x/200*(1-x/200)
ax.plot(x[:100],y[:100],color='k',lw=1.6); ax.plot(x[100:],y[100:],color=H,ls='--',lw=1.4); ax.plot([100],[40],'*',color=H,ms=14)
ax.plot([100,100],[40,0],color=B,lw=1.6); xx=np.linspace(100,300,100); ax.plot(xx,40*(1-((xx-100)/200)**2),color=B,lw=1.6)
ax.plot([100,200,300],[0,0,0],'o',color=T); ax.text(100,-9,'keping 1',ha='center',fontsize=8.5); ax.text(200,-9,'pusat massa',ha='center',fontsize=8.5,color=H); ax.text(300,-9,'keping 2',ha='center',fontsize=8.5)
ax.set_xlim(0,320); ax.set_ylim(-14,48); ax.set_xlabel('$x$ (m)'); ax.set_yticks([]); sp(ax); ax.spines['left'].set_visible(False); sv(f,'pecah.png')
# 13 roket
f,ax=plt.subplots(figsize=(5.4,1.9)); clean(ax)
ax.add_patch(Polygon([(2,-.3),(4.2,-.3),(4.9,0),(4.2,.3),(2,.3)],fc=M,ec=T,lw=1.3)); ax.add_patch(Polygon([(2,-.2),(1.6,-.35),(1.6,.35),(2,.2)],fc=T,ec='k'))
for yy in (-.15,0,.15): ar(ax,(1.5,yy),(.3,yy*1.8),H,1.3,9)
ax.text(.2,.55,r'gas buang, $v_e$',color=H,fontsize=9); ar(ax,(5.1,0),(6.3,0),B,2.2); ax.text(5.4,.22,'gaya dorong',color=B,fontsize=9); ax.text(3.2,0,'$m$',ha='center',va='center')
ax.set_xlim(0,6.6); ax.set_ylim(-.7,.9); sv(f,'roket.png')
# 14 gas
f,ax=plt.subplots(figsize=(4,2.4)); clean(ax)
ax.add_patch(Rectangle((3,-1.1),.25,2.2,fc='#bbb',ec='k')); ball(ax,1.2,.45,.14); ar(ax,(1.4,.45),(2.6,.45),H,1.8); ax.text(1.8,.65,r'$+mv_x$',color=H,fontsize=9)
ball(ax,1.2,-.45,.14); ar(ax,(2.6,-.45),(1.4,-.45),B,1.8); ax.text(1.8,-.8,r'$-mv_x$',color=B,fontsize=9); ax.text(.2,.45,'datang',fontsize=8.5,va='center'); ax.text(.2,-.45,'pergi',fontsize=8.5,va='center')
ax.text(3.4,0,r'$\Delta p = 2mv_x$'+'\npada dinding',fontsize=9,va='center'); ax.set_xlim(0,5.2); ax.set_ylim(-1.3,1.3); sv(f,'gas.png')
# ---- perbaikan
f,ax=plt.subplots(figsize=(6.4,2.2)); clean(ax)
for x0,lab,vs in [(0,'sebelum',(1.3,H)),(4.2,'sesudah',(-1.0,B))]:
    ax.add_patch(Rectangle((x0+2.2,-.9),.25,1.8,fc='#bbb',ec='k')); ball(ax,x0+1.2,0,.25)
    ar(ax,(x0+1.2,0.5),(x0+1.2+vs[0],0.5),vs[1],2); ax.text(x0+1.2,-1.2,lab,ha='center',fontsize=9)
ax.text(1.8,.72,r'$\vec p_i$',color=H); ax.text(4.8,.72,r'$\vec p_f$',color=B)
ar(ax,(10.3,0),(8.0,0),T,2.2); ax.text(9.15,-.5,r'$\Delta\vec p = \vec p_f - \vec p_i$',color=T,ha='center',fontsize=9)
ax.set_xlim(-.3,10.6); ax.set_ylim(-1.5,1.2); sv(f,'pantul.png')
f,ax=plt.subplots(figsize=(6.4,2)); clean(ax)
for y0,lab in [(1.3,'sebelum: $p = 0$'),(0,'sesudah: $p$ tetap $0$')]:
    ax.add_patch(Rectangle((1,y0-.12),2.2,.24,fc=T,ec='k')); ax.add_patch(Rectangle((1,y0-.5),.35,.45,fc=T,ec='k')); ax.text(-3.2,y0,lab,fontsize=9,va='center')
ax.add_patch(Rectangle((4.6,-.07),.3,.14,fc=H,ec='k')); ar(ax,(5,0),(6.6,0),H,2); ax.text(5.6,.2,r'$m\vec v$',color=H)
ar(ax,(.9,0),(.2,0),B,2); ax.text(.3,.22,r'$M\vec V$',color=B); ax.set_xlim(-3.3,6.8); ax.set_ylim(-.8,1.8); sv(f,'rekoil.png')
f,ax=plt.subplots(figsize=(5.8,2.6)); clean(ax)
for y0,xb,xp,lab in [(1.6,0,3.1,'awal'),(0,1.0,1.1,'akhir')]:
    ax.fill_between([-1,5.4],[y0-.5,y0-.5],[y0-.2,y0-.2],color=M); ax.add_patch(Polygon([(xb,y0),(xb+3.2,y0),(xb+2.9,y0-.35),(xb+.3,y0-.35)],fc='#c9a26b',ec='k'))
    ax.add_patch(Circle((xp,y0+.62),.13,fc=B,ec=T)); ax.plot([xp,xp],[y0+.5,y0+.05],color=T,lw=2); ax.text(-1.7,y0,lab,fontsize=9)
    ax.plot([xb+1.6],[y0-.17],'x',color='k',ms=5)
ax.plot([2.1,2.1],[-.6,2.9],color=H,ls=':'); ax.text(2.2,2.9,'pusat massa sistem (tidak bergeser)',color=H,fontsize=8,va='top')
ax.set_xlim(-1.9,5.6); ax.set_ylim(-.7,3.0); sv(f,'perahu.png')
f,ax=plt.subplots(figsize=(7,3.3)); clean(ax)
rows=[(2.6,.3,.3,'massa sama: bertukar kecepatan',(0,1.2)),(1.3,.45,.2,'berat menumbuk ringan',(1.0,1.9)),(0,.2,.45,'ringan menumbuk berat',(-.9,.25))]
for y,r1,r2,lab,(b1,b2) in rows:
    ball(ax,0,y,r1,B); ball(ax,1.8,y,r2,T); ar(ax,(r1,y),(r1+.72,y),H,1.8)
    ball(ax,6.2,y,r1,B); ball(ax,8.0,y,r2,T)
    if abs(b1)>.01: ar(ax,(6.2+np.sign(b1)*r1,y),(6.2+np.sign(b1)*r1+b1*.6,y),H,1.8)
    if abs(b2)>.01: ar(ax,(8.0+r2,y),(8.0+r2+b2*.6,y),H,1.8)
    ax.text(4.0,y+.62,lab,ha='center',va='center',fontsize=8.5,color=T)
ax.text(.9,3.5,'sebelum',ha='center',fontsize=9,color='gray'); ax.text(7.1,3.5,'sesudah',ha='center',fontsize=9,color='gray')
ax.plot([4.0,4.0],[-.5,3.0],color='#ccc',lw=.8); ax.set_xlim(-1.6,9.8); ax.set_ylim(-.6,3.7); sv(f,'lenting.png')
