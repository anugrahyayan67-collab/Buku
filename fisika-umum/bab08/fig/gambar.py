import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch as FA, Rectangle, Circle, Arc, Polygon
plt.rcParams.update({'font.family':'Liberation Sans','font.size':10,'mathtext.fontset':'dejavusans'})
B='#1b75bc'; T='#17355e'; M='#e9f2fa'; H='#b5541c'; W='#cfe3f5'; G='#1a8a6a'
def ar(ax,a,b,c='k',lw=1.6,ms=13,ls='-'): ax.add_patch(FA(a,b,arrowstyle='-|>',mutation_scale=ms,color=c,lw=lw,ls=ls,shrinkA=0,shrinkB=0))
def dar(ax,a,b,c='k'): ar(ax,a,b,c,1,8); ar(ax,b,a,c,1,8)
def sv(f,n): f.savefig(n,dpi=220,bbox_inches='tight'); plt.close(f)
def clean(ax): ax.set_aspect('equal'); ax.axis('off')
def sp(ax):
    for s in ('top','right'): ax.spines[s].set_visible(False)
def spring(ax,x0,x1,y,n=8,a=.18):
    xs=np.linspace(x0,x1,2*n+1); ys=y+np.array([0]+[(-1)**i*a for i in range(1,2*n)]+[0]); ax.plot(xs,ys,'k',lw=1.2)
# 1 ghs
f,axs=plt.subplots(3,1,figsize=(5.4,4.2),sharex=True); t=np.linspace(0,2,400)
for ax,y,lab,c in zip(axs,[np.cos(2*np.pi*t),-np.sin(2*np.pi*t),-np.cos(2*np.pi*t)],['$x$','$v$','$a$'],[B,H,G]):
    ax.plot(t,y,color=c,lw=2); ax.axhline(0,color='k',lw=.6); ax.set_ylabel(lab,rotation=0,labelpad=10); ax.set_yticks([-1,0,1]); sp(ax)
axs[0].set_yticklabels(['$-A$','0','$A$']); axs[1].set_yticklabels([r'$-\omega A$','0',r'$\omega A$']); axs[2].set_yticklabels([r'$-\omega^2A$','0',r'$\omega^2A$'])
axs[2].set_xticks([0,.5,1,1.5,2]); axs[2].set_xticklabels(['0','$T/2$','$T$','$3T/2$','$2T$']); axs[2].set_xlabel('waktu'); sv(f,'ghs.png')
# 2 pegas massa
f,ax=plt.subplots(figsize=(5.6,2.6)); clean(ax)
for y,xb,lab in [(1.6,3.0,'setimbang: $F = 0$'),(.8,4.0,'diregangkan: gaya ke kiri'),(0,2.0,'ditekan: gaya ke kanan')]:
    ax.plot([0,0],[y-.3,y+.3],'k',lw=2.5); spring(ax,0,xb,y,8,.12); ax.add_patch(Rectangle((xb,y-.22),.6,.44,fc=B,ec=T)); ax.plot([0,5.4],[y-.24,y-.24],'k',lw=.8); ax.text(5.6,y,lab,fontsize=8.5,va='center')
ar(ax,(4.0,.8),(3.2,.8),H,2); ar(ax,(2.6,0),(3.4,0),H,2); ax.plot([3.3,3.3],[-.4,2.0],color='gray',ls=':'); ax.text(3.3,-.6,'$x = 0$',ha='center',fontsize=9)
ax.set_xlim(-.2,8.6); ax.set_ylim(-.8,2.1); sv(f,'pegasmassa.png')
# 3 lingkar
f,ax=plt.subplots(figsize=(4.6,3)); clean(ax); th=np.radians(50)
ax.add_patch(Circle((0,0),1.2,fc='none',ec='gray',ls='--')); ax.plot([-1.5,1.5],[0,0],'k',lw=.8); ax.plot([0,0],[-1.4,1.4],'k',lw=.4)
ax.plot([0,1.2*np.cos(th)],[0,1.2*np.sin(th)],color=T,lw=1.5); ax.add_patch(Circle((1.2*np.cos(th),1.2*np.sin(th)),.07,fc=H)); ax.plot([1.2*np.cos(th)]*2,[1.2*np.sin(th),0],color=H,ls=':'); ax.add_patch(Circle((1.2*np.cos(th),0),.07,fc=B))
ax.add_patch(Arc((0,0),.6,.6,theta1=0,theta2=50,color='k')); ax.text(.36,.12,r'$\omega t$',fontsize=9); ax.text(.3,.62,'$A$'); ax.text(.45,-.25,r'$x = A\cos\omega t$',color=B,fontsize=9)
ar(ax,(1.2*np.cos(th),1.2*np.sin(th)),(1.2*np.cos(th)-.5*np.sin(th),1.2*np.sin(th)+.5*np.cos(th)),H,1.5); ax.set_xlim(-1.6,2.2); ax.set_ylim(-1.5,1.5); sv(f,'lingkar.png')
# 4 energi vs x
f,ax=plt.subplots(figsize=(4.6,2.9)); x=np.linspace(-1.15,1.15,200); ax.plot(x,x**2,color=B,lw=2.2,label='$U = \\frac{1}{2}kx^2$'); ax.plot([-1,1],[1,1],color=H,lw=1.6); ax.text(1.03,1,'$E$',color=H,va='center')
ax.plot(x[(abs(x)<=1)],1-x[(abs(x)<=1)]**2,color=G,lw=1.6,ls='--'); ax.text(0,.82,'$K$',color=G,ha='center'); ax.text(.72,.3,'$U$',color=B)
xx=.6; ax.plot([xx,xx],[0,xx**2],color=B,lw=3,alpha=.5); ax.plot([xx,xx],[xx**2,1],color=G,lw=3,alpha=.5)
ax.set_xticks([-1,0,1]); ax.set_xticklabels(['$-A$','0','$A$']); ax.set_yticks([]); ax.set_xlabel('$x$'); ax.set_ylabel('energi'); ax.set_ylim(0,1.35); sp(ax); sv(f,'energix.png')
# 5 energi vs t
f,ax=plt.subplots(figsize=(4.8,2.6)); t=np.linspace(0,1,300); ax.plot(t,np.cos(2*np.pi*t)**2,color=B,lw=2,label='$U$'); ax.plot(t,np.sin(2*np.pi*t)**2,color=G,lw=2,ls='--',label='$K$'); ax.axhline(1,color=H,lw=1.5); ax.text(1.02,1,'$E$',color=H,va='center'); ax.axhline(.5,color='gray',ls=':',lw=.8)
ax.set_xticks([0,.25,.5,.75,1]); ax.set_xticklabels(['0','$T/4$','$T/2$','$3T/4$','$T$']); ax.set_yticks([0,.5,1]); ax.set_yticklabels(['0','$E/2$','$E$']); ax.legend(frameon=False,loc='upper center',ncol=2,bbox_to_anchor=(.5,.95),fontsize=9); ax.set_ylim(0,1.3); sp(ax); sv(f,'energit.png')
# 6 bandul
f,ax=plt.subplots(figsize=(3.4,3.2)); clean(ax); L=3; th=np.radians(28); x,y=L*np.sin(th),-L*np.cos(th)
ax.plot([-1,1],[0,0],'k',lw=2); ax.plot([0,0],[0,-L],color='gray',ls='--'); ax.plot([0,x],[0,y],'k',lw=1.3); ax.add_patch(Circle((x,y),.16,fc=B,ec=T))
ar(ax,(x,y),(x,y-1.1),T,2); ax.text(x+.1,y-1.0,'$mg$',color=T); ar(ax,(x,y),(x-.52*np.cos(th),y-.52*np.sin(th)),H,2); ax.text(x-1.55,y-.5,r'$mg\sin\theta$',color=H,fontsize=9)
ax.add_patch(Arc((0,0),1.5,1.5,theta1=270,theta2=298,color='k')); ax.text(.16,-1.05,r'$\theta$'); ax.text(.85,-1.2,'$L$'); a=np.linspace(-.6,.6,40); ax.plot(L*np.sin(a),-L*np.cos(a),color='gray',ls=':',lw=.8); ax.text(.3,-3.3,'$s = L\\theta$',fontsize=9)
ax.set_xlim(-2,2.6); ax.set_ylim(-4.3,.3); sv(f,'bandul.png')
# 7 tingkat energi getaran
f,ax=plt.subplots(figsize=(4.6,3.1)); x=np.linspace(-2.6,2.6,200); ax.plot(x,.5*x**2,color=B,lw=2)
for n in range(5):
    E=n+.5; xa=np.sqrt(2*E); ax.plot([-xa,xa],[E,E],color=H,lw=1.5); ax.text(xa+.1,E,f'$n = {n}$',va='center',fontsize=8.5)
dar(ax,(-.3,1.5),(-.3,2.5)); ax.text(-.25,1.95,r' $hf$',fontsize=9); ax.text(0,.18,r'$\frac{1}{2}hf$',ha='center',fontsize=8.5)
ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel('regangan ikatan'); ax.set_ylabel('energi'); ax.set_ylim(0,5.2); ax.set_xlim(-3,3.9); sp(ax); sv(f,'tingkat.png')
# 8 peta IR
f,ax=plt.subplots(figsize=(6.2,2.3)); 
items=[(3600,'O–H'),(3300,'N–H'),(2950,'C–H'),(2200,'C≡C, C≡N'),(1715,'C=O'),(1650,'C=C'),(1100,'C–O, C–C'),(700,'C–Cl')]
for i,(w,n) in enumerate(items):
    ax.plot([w,w],[0,1],color=B,lw=3); ax.text(w,1.08+.28*(i%2),n,ha='center',fontsize=8.5)
ax.set_xlim(4000,400); ax.set_ylim(0,1.9); ax.set_yticks([]); ax.set_xlabel('bilangan gelombang (cm$^{-1}$)')
for s in ('top','right','left'): ax.spines[s].set_visible(False)
ax.annotate('',xy=(3900,1.75),xytext=(600,1.75),arrowprops=dict(arrowstyle='->',color=H)); ax.text(2250,1.8,'ikatan makin kaku atau atom makin ringan',color=H,ha='center',fontsize=8.5); sv(f,'petair.png')
# 9 redam
f,ax=plt.subplots(figsize=(5,2.9)); t=np.linspace(0,6,500)
ax.plot(t,np.exp(-.25*t)*np.cos(2*np.pi*t),color=B,lw=1.6,label='teredam ringan'); ax.plot(t,np.exp(-.25*t),color=B,ls=':',lw=1); ax.plot(t,-np.exp(-.25*t),color=B,ls=':',lw=1)
ax.plot(t,(1+3*t)*np.exp(-3*t),color=H,lw=2,label='teredam kritis'); ax.plot(t,1.07*np.exp(-.9*t)-.07*np.exp(-12*t),color=G,lw=2,ls='--',label='teredam lebih')
ax.axhline(0,color='k',lw=.6); ax.set_xlabel('waktu'); ax.set_ylabel('simpangan'); ax.set_xticks([]); ax.set_yticks([0]); ax.legend(frameon=False,fontsize=8.5); sp(ax); sv(f,'redam.png')
# 10 resonansi
f,ax=plt.subplots(figsize=(4.8,3)); r=np.linspace(.2,2,400)
for Q,c in [(2,G),(5,B),(15,H)]: ax.plot(r,1/np.sqrt((1-r**2)**2+(r/Q)**2),color=c,lw=1.8,label=f'$Q = {Q}$')
ax.set_xlabel('frekuensi pendorong / frekuensi alami'); ax.set_ylabel('amplitudo / simpangan statis'); ax.set_xticks([.5,1,1.5,2]); ax.set_xticklabels(['0,5','1','1,5','2']); ax.legend(frameon=False,fontsize=9); ax.set_ylim(0,16); sp(ax); sv(f,'resonansi.png')
# 11 CO2
f,ax=plt.subplots(figsize=(5.8,2.8)); clean(ax)
def mol(y,arrows,lab):
    for x,c,r in [(-1.2,H,.2),(0,'#444',.17),(1.2,H,.2)]: ax.add_patch(Circle((x,y),r,fc=c,ec='k'))
    ax.plot([-1,-.17],[y,y],'k',lw=1.5); ax.plot([.17,1],[y,y],'k',lw=1.5)
    for (x,dx,dy) in arrows: ar(ax,(x,y+np.sign(dy)*.22 if dy else y+.3),(x+dx,y+dy+(np.sign(dy)*.22 if dy else .3)),B,1.6,10)
    ax.text(2.0,y,lab,fontsize=8.5,va='center')
mol(2,[(-1.2,-.5,0),(1.2,.5,0)],'ulur simetris, 1388 cm$^{-1}$\n(tidak menyerap inframerah)')
mol(1,[(-1.2,.45,0),(0,-.5,0),(1.2,.45,0)],'ulur asimetris, 2349 cm$^{-1}$')
mol(0,[(-1.2,0,.4),(0,0,-.45),(1.2,0,.4)],'tekuk, 667 cm$^{-1}$')
ax.set_xlim(-2,5.6); ax.set_ylim(-.8,2.6); sv(f,'co2.png')
