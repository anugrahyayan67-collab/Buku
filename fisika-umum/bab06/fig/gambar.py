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
# 1 kolom
f,ax=plt.subplots(figsize=(3.6,3.2)); clean(ax)
ax.add_patch(Rectangle((0,0),4,3,fc=W,ec='none')); ax.plot([0,0,4,4],[3.4,0,0,3.4],'k',lw=1.5); ax.plot([0,4],[3,3],color=B,lw=1)
ax.add_patch(Rectangle((1.5,.8),1,2.2,fc='#9cc6ea',ec=T,ls='--'))
ar(ax,(2,3.9),(2,3.05),H,2); ax.text(2.15,3.55,'$p_0A$',color=H); ar(ax,(2,.1),(2,.78),H,2); ax.text(2.15,.3,'$pA$',color=H); ar(ax,(2,2.1),(2,1.4),T,2); ax.text(2.1,1.7,'$mg$',color=T,fontsize=9)
dar(ax,(3.3,.8),(3.3,3)); ax.text(3.4,1.9,'$h$'); ax.set_xlim(-.3,4.3); ax.set_ylim(-.2,4.1); sv(f,'kolom.png')
# 2 bejana
f,ax=plt.subplots(figsize=(6,2.4)); clean(ax)
shapes=[[(0,0),(0,2),(1.2,2),(1.2,0)],[(2.2,0),(1.7,2),(3.9,2),(3.4,0)],[(4.9,0),(5.3,2),(5.7,2),(6.1,0)]]
for s in shapes: ax.add_patch(Polygon(s,fc=W,ec='k',lw=1.4))
ax.plot([-.3,6.4],[2,2],color=B,ls=':'); dar(ax,(6.6,0),(6.6,2)); ax.text(6.7,1,'$h$')
for x in (.6,2.8,5.5): ax.text(x,-.35,r'$p = p_0 + \rho gh$',ha='center',fontsize=8.5)
ax.set_xlim(-.4,7.1); ax.set_ylim(-.6,2.3); sv(f,'bejana.png')
# 3 tabung U
f,ax=plt.subplots(figsize=(3.4,3)); clean(ax)
ax.add_patch(Rectangle((0,.5),.6,1.7,fc=W,ec='none')); ax.add_patch(Rectangle((1.8,.5),.6,1.2,fc=W,ec='none')); ax.add_patch(Rectangle((0,0),2.4,.5,fc=W,ec='none'))
ax.add_patch(Rectangle((1.8,1.7),.6,1.0,fc='#f0d9a8',ec='none'))
ax.plot([0,0,2.4,2.4],[3,0,0,3],'k',lw=1.5); ax.plot([.6,.6,1.8,1.8],[3,.5,.5,3],'k',lw=1.5)
ax.plot([-.2,2.6],[1.7,1.7],color='gray',ls=':'); dar(ax,(-.25,1.7),(-.25,2.2)); ax.text(-.75,1.9,'$h_1$'); dar(ax,(2.65,1.7),(2.65,2.7)); ax.text(2.75,2.15,'$h_2$')
ax.text(.3,1.1,'air',ha='center',fontsize=8.5); ax.text(2.1,2.2,'minyak',ha='center',fontsize=8,rotation=90)
ax.set_xlim(-.9,3.2); ax.set_ylim(-.2,3.1); sv(f,'tabungu.png')
# 4 bendungan
f,ax=plt.subplots(figsize=(4.6,2.8)); clean(ax)
ax.add_patch(Rectangle((0,0),3,2.4,fc=W,ec='none')); ax.add_patch(Polygon([(3,0),(3,2.8),(3.5,2.8),(4.3,0)],fc='#bbb',ec='k'))
for y in np.linspace(.2,2.2,6): ar(ax,(3-(2.4-y)*.8,y),(3,y),H,1.4,9)
ax.plot([3-2.4*.8,3],[0,2.4],color=H,lw=1); dar(ax,(-.2,0),(-.2,2.4)); ax.text(-.6,1.2,'$H$'); ax.plot([3],[.8],'o',color=T); ax.text(3.2,.75,r'$F$',color='w',fontsize=10,fontweight='bold'); ax.text(1.5,2.6,r'tekanan bertambah ke bawah',color=H,fontsize=8.5,ha='center')
ax.plot([-.4,4.5],[0,0],'k',lw=1.5); ax.set_xlim(-.8,4.6); ax.set_ylim(-.2,3); sv(f,'bendungan.png')
# 5 barometer + manometer
f,axs=plt.subplots(1,2,figsize=(6,3.2))
ax=axs[0]; clean(ax); ax.add_patch(Rectangle((0,0),2.4,.6,fc='#b9c0c9',ec='k')); ax.add_patch(Rectangle((1,.3),.4,2.5,fc='#b9c0c9',ec='none')); ax.plot([1,1,1.4,1.4],[.3,3.4,3.4,.3],'k',lw=1.3); ax.plot([1,1.4],[3.4,3.4],'k',lw=1.3)
ax.text(1.2,3.1,'vakum',ha='center',fontsize=7.5); dar(ax,(1.9,.6),(1.9,2.8)); ax.text(2.0,1.7,'$h$ = 760 mm'); ar(ax,(.4,1.5),(.4,.65),H,1.6); ax.text(.05,1.6,'$p_0$',color=H); ax.set_xlim(-.2,3.7); ax.set_ylim(-.2,3.6); ax.set_title('barometer',fontsize=9.5)
ax=axs[1]; clean(ax); ax.add_patch(Circle((.5,2.6),.5,fc=M,ec='k')); ax.text(.5,2.6,'gas\n$p$',ha='center',va='center',fontsize=8.5)
ax.add_patch(Rectangle((1.2,.4),.4,1.0,fc='#b9c0c9',ec='none')); ax.add_patch(Rectangle((2.4,.4),.4,2.0,fc='#b9c0c9',ec='none')); ax.add_patch(Rectangle((1.2,0),1.6,.4,fc='#b9c0c9',ec='none'))
ax.plot([1.0,1.2,1.2,2.8,2.8],[2.6,2.6,0,0,3.3],'k',lw=1.3); ax.plot([1.0,1.6,1.6,2.4,2.4],[2.9,2.9,.4,.4,3.3],'k',lw=1.3)
ax.plot([1.0,3.2],[1.4,1.4],color='gray',ls=':'); dar(ax,(3.05,1.4),(3.05,2.4)); ax.text(3.15,1.85,'$h$'); ar(ax,(2.6,3.6),(2.6,3.0),H,1.6); ax.text(2.75,3.4,'$p_0$',color=H)
ax.set_xlim(-.1,3.6); ax.set_ylim(-.2,3.8); ax.set_title('manometer terbuka',fontsize=9.5); sv(f,'ukur.png')
# 6 hidraulik
f,ax=plt.subplots(figsize=(5.2,2.6)); clean(ax)
ax.add_patch(Polygon([(0,0),(0,1.6),(.6,1.6),(.6,.6),(3,.6),(3,1.6),(5,1.6),(5,0)],fc=W,ec='k',lw=1.4))
ax.add_patch(Rectangle((0,1.6),.6,.18,fc=T)); ax.add_patch(Rectangle((3,1.6),2,.18,fc=T))
ar(ax,(.3,2.7),(.3,1.85),H,2); ax.text(.45,2.4,'$F_1$',color=H); ar(ax,(4,1.85),(4,2.9),B,2.6); ax.text(4.15,2.4,'$F_2$',color=B)
ax.text(.3,1.2,'$A_1$',ha='center',fontsize=9); ax.text(4,1.0,'$A_2$',ha='center'); ax.text(2,.25,'tekanan sama di mana-mana',ha='center',fontsize=8.5)
ax.set_xlim(-.2,5.2); ax.set_ylim(-.1,3); sv(f,'hidraulik.png')
# 7 atmosfer
f,ax=plt.subplots(figsize=(4.8,3)); h=np.linspace(0,20,200); ax.plot(h,101.3*np.exp(-h/8.44),color=B,lw=2.2)
for hh,n in [(3.676,'Semeru'),(8.849,'Everest'),(11,'pesawat jet')]: ax.plot([hh],[101.3*np.exp(-hh/8.44)],'o',color=H); ax.text(hh+.4,101.3*np.exp(-hh/8.44)+3,n,fontsize=8.5)
ax.set_xlabel('ketinggian (km)'); ax.set_ylabel('tekanan (kPa)'); ax.set_xlim(0,20); ax.set_ylim(0,110); sp(ax); sv(f,'atmosfer.png')
# 8 apung
f,ax=plt.subplots(figsize=(3.6,3.2)); clean(ax)
ax.add_patch(Rectangle((0,0),4,3.2,fc=W,ec='none')); ax.plot([0,0,4,4],[3.6,0,0,3.6],'k',lw=1.5); ax.add_patch(Rectangle((1.3,.9),1.4,1.4,fc='#c9a26b',ec='k'))
for x in (1.5,2,2.5): ar(ax,(x,2.9),(x,2.33),H,1.3,9); ar(ax,(x,0.05),(x,.87),H,1.9,11)
for y in (1.2,1.6,2.0): ar(ax,(.7,y),(1.27,y),'gray',1,8); ar(ax,(3.3,y),(2.73,y),'gray',1,8)
ax.text(2.85,2.7,'$p_{atas}$ kecil',color=H,fontsize=8.5); ax.text(2.85,.35,'$p_{bawah}$ besar',color=H,fontsize=8.5)
ax.set_xlim(-.2,5.6); ax.set_ylim(-.2,3.7); sv(f,'apung.png')
# 9 terapung
f,ax=plt.subplots(figsize=(6,2.4)); clean(ax)
for x0,y,lab,c in [(0,1.55,r'$\rho < \rho_f$'+'\nterapung','#e8cf9f'),(2.3,.8,r'$\rho = \rho_f$'+'\nmelayang','#c9a26b'),(4.6,0,r'$\rho > \rho_f$'+'\ntenggelam','#8a6a3a')]:
    ax.add_patch(Rectangle((x0,0),1.8,2,fc=W,ec='none')); ax.plot([x0,x0,x0+1.8,x0+1.8],[2.3,0,0,2.3],'k',lw=1.3); ax.add_patch(Rectangle((x0+.55,y),.7,.7,fc=c,ec='k')); ax.text(x0+.9,-.55,lab,ha='center',fontsize=8.5)
ax.set_xlim(-.2,6.6); ax.set_ylim(-.9,2.4); sv(f,'terapung.png')
# 10 permukaan
f,ax=plt.subplots(figsize=(4.6,2.4)); clean(ax); ax.add_patch(Rectangle((0,0),5,1.8,fc=W,ec='none')); ax.plot([0,5],[1.8,1.8],color=B,lw=1.5)
for (x,y),dirs in [((1.3,.8),[(0,1),(0,-1),(1,0),(-1,0),(.7,.7),(-.7,.7),(.7,-.7),(-.7,-.7)]),((3.6,1.72),[(0,-1),(1,0),(-1,0),(.7,-.7),(-.7,-.7)])]:
    ax.add_patch(Circle((x,y),.1,fc=T))
    for dx,dy in dirs: ar(ax,(x,y),(x+.5*dx,y+.5*dy),H,1.2,8)
ax.text(1.3,-.3,'di dalam: gaya total nol',ha='center',fontsize=8.5); ax.text(3.6,-.3,'di permukaan: ditarik ke dalam',ha='center',fontsize=8.5)
ax.set_xlim(-.1,5.1); ax.set_ylim(-.5,2.2); sv(f,'permukaan.png')
# 11 kontak
f,ax=plt.subplots(figsize=(5.2,1.8)); clean(ax)
ax.plot([0,5.4],[0,0],'k',lw=1.5); t=np.linspace(0,np.pi,60); ax.fill(1.2+1.0*np.cos(t),.35*np.sin(t),fc=W,ec=B); 
t=np.linspace(-.9,np.pi+.9,80); xx=4.0+.55*np.cos(t); yy=.43+.55*np.sin(t); ax.fill(xx,yy,fc='#b9c0c9',ec='k')
ax.text(1.2,-.4,r'air pada kaca bersih: $\theta < 90°$'+'\n(membasahi)',ha='center',fontsize=8.5,va='top'); ax.text(4.0,-.4,r'raksa pada kaca: $\theta > 90°$'+'\n(tidak membasahi)',ha='center',fontsize=8.5,va='top')
ax.set_xlim(-.2,5.6); ax.set_ylim(-1.2,1.1); sv(f,'kontak.png')
# 12 kapiler
f,ax=plt.subplots(figsize=(5.2,3)); clean(ax)
for x0,col,rise,lab in [(0,W,1.2,'air'),(3,'#b9c0c9',-.5,'raksa')]:
    ax.add_patch(Rectangle((x0,0),2.2,1.2,fc=col,ec='none')); ax.plot([x0,x0,x0+2.2,x0+2.2],[1.6,0,0,1.6],'k',lw=1.3)
    ax.add_patch(Rectangle((x0+.95,.3),.3,.9+rise,fc=col,ec='none')); ax.add_patch(Rectangle((x0+.95,1.2+min(rise,0)),.3,abs(min(rise,0)),fc='w',ec='none'))
    ax.plot([x0+.95,x0+.95],[.3,3],'k',lw=1.3); ax.plot([x0+1.25,x0+1.25],[.3,3],'k',lw=1.3); ax.text(x0+1.1,-.35,lab,ha='center',fontsize=9)
    dar(ax,(x0+1.6,1.2),(x0+1.6,1.2+rise)); ax.text(x0+1.7,1.2+rise/2,'$h$',va='center')
ax.set_xlim(-.2,5.5); ax.set_ylim(-.6,3.1); sv(f,'kapiler.png')
# 13 putar
f,axs=plt.subplots(1,2,figsize=(6,2.4))
ax=axs[0]; clean(ax); ax.add_patch(Polygon([(0,0),(0,1.6),(3,.8),(3,0)],fc=W,ec='none')); ax.plot([0,0,3,3],[2,0,0,2],'k',lw=1.4); ax.plot([0,3],[1.6,.8],color=B,lw=1.5)
ar(ax,(3.3,.6),(4.2,.6),H,2); ax.text(3.6,.8,r'$\vec a$',color=H); ax.add_patch(Arc((3,.8),1.6,1.6,theta1=165,theta2=180,color='k')); ax.text(1.75,.86,r'$\theta$',fontsize=9); ax.plot([1.5,3],[.8,.8],color='gray',ls=':')
ax.set_xlim(-.2,4.4); ax.set_ylim(-.2,2.1); ax.set_title(r'dipercepat: $\tan\theta = a/g$',fontsize=9.5)
ax=axs[1]; clean(ax); x=np.linspace(-1.2,1.2,60); y=.6+.7*x**2; ax.fill_between(x,0,y,color=W); ax.plot(x,y,color=B,lw=1.5); ax.plot([-1.2,-1.2,1.2,1.2],[2,0,0,2],'k',lw=1.4)
ax.plot([0,0],[-.2,2.2],color='gray',ls='-.'); ax.add_patch(Arc((0,2.15),.7,.25,theta1=200,theta2=520,color=H)); ax.text(.45,2.1,r'$\omega$',color=H)
ax.set_xlim(-1.5,1.5); ax.set_ylim(-.3,2.4); ax.set_title(r'berputar: $z = \omega^2r^2/2g$',fontsize=9.5); sv(f,'putar.png')
# 14 tetes laplace
f,ax=plt.subplots(figsize=(4.6,2.2)); clean(ax)
ax.add_patch(Circle((1,1),.8,fc=W,ec=B,lw=1.6)); ax.text(1,1,r'$p_0 + \dfrac{2\gamma}{r}$',ha='center',va='center',fontsize=9); ax.text(1,-.15,'tetes zat cair\n(satu permukaan)',ha='center',fontsize=8.5,va='top')
ax.add_patch(Circle((3.6,1),.8,fc='w',ec=B,lw=3.2)); ax.text(3.6,1,r'$p_0 + \dfrac{4\gamma}{r}$',ha='center',va='center',fontsize=9); ax.text(3.6,-.15,'gelembung sabun\n(dua permukaan)',ha='center',fontsize=8.5,va='top')
ax.set_xlim(0,4.6); ax.set_ylim(-.9,2); sv(f,'laplace.png')
