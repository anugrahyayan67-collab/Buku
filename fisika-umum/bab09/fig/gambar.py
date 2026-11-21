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
# 1 jenis
f,axs=plt.subplots(2,1,figsize=(6,2.8)); x=np.linspace(0,10,400)
ax=axs[0]; ax.plot(x,.5*np.sin(2*np.pi*x/2.5),color=B,lw=2); ar(ax,(8.2,.85),(9.8,.85),H,1.6); ax.text(8.3,1.0,'arah rambat',color=H,fontsize=8.5); dar(ax,(.62,-.5),(.62,.5),T); ax.text(.75,.0,'getaran',fontsize=8.5,color=T)
ax.set_xlim(0,10); ax.set_ylim(-.8,1.3); ax.axis('off'); ax.set_title('transversal: getaran tegak lurus arah rambat',fontsize=9.5,loc='left')
ax=axs[1]; xs=np.linspace(0,10,90); xd=xs+.28*np.sin(2*np.pi*xs/2.5)
for xx in xd: ax.plot([xx,xx],[-.4,.4],color=B,lw=1)
dar(ax,(4.3,-.65),(5.1,-.65),T); ax.text(5.2,-.72,'getaran',fontsize=8.5,color=T); ax.text(1.55,.55,'rapatan',fontsize=8.5,ha='center'); ax.text(2.85,.55,'renggangan',fontsize=8.5,ha='center')
ax.set_xlim(0,10); ax.set_ylim(-.9,.9); ax.axis('off'); ax.set_title('longitudinal: getaran searah arah rambat',fontsize=9.5,loc='left'); sv(f,'jenis.png')
# 2 lambda
f,ax=plt.subplots(figsize=(5.4,2.3)); x=np.linspace(0,5,400); ax.plot(x,np.sin(2*np.pi*x/2),color=B,lw=2); ax.axhline(0,color='k',lw=.6)
dar(ax,(.5,1.25),(2.5,1.25)); ax.text(1.5,1.35,r'$\lambda$',ha='center'); dar(ax,(3.5,0),(3.5,-1)); ax.text(3.6,-.55,'$A$'); ax.plot(x,np.sin(2*np.pi*(x-.35)/2),color=B,lw=1,ls='--'); ar(ax,(4.2,.6),(4.9,.6),H,1.6); ax.text(4.3,.75,'$v$',color=H)
ax.set_xlabel('$x$'); ax.set_ylabel('$y$'); ax.set_xticks([]); ax.set_yticks([]); ax.set_ylim(-1.3,1.7); sp(ax); sv(f,'lambda.png')
# 3 kuadrat terbalik
f,ax=plt.subplots(figsize=(4.2,2.8)); clean(ax); ax.add_patch(Circle((0,0),.12,fc=H))
for r in (1,2,3): ax.add_patch(Arc((0,0),2*r,2*r,theta1=-28,theta2=28,color=B,lw=1.5)); ax.text(r*np.cos(.52)+.05,r*np.sin(.52)+.1,f'$r = {r}$',fontsize=8.5)
for a in (-.4,.4): ax.plot([0,3.4*np.cos(a)],[0,3.4*np.sin(a)],color='gray',lw=.8,ls='--')
ax.text(1.0,-.75,'$I$',fontsize=9); ax.text(2.0,-1.15,'$I/4$',fontsize=9); ax.text(3.0,-1.55,'$I/9$',fontsize=9); ax.set_xlim(-.3,3.8); ax.set_ylim(-1.8,1.9); sv(f,'kuadrat.png')
# 4 desibel
f,ax=plt.subplots(figsize=(5.6,2.9)); items=[(0,'ambang dengar'),(20,'bisikan'),(40,'perpustakaan'),(60,'percakapan'),(80,'jalan ramai'),(100,'konser, gergaji mesin'),(120,'ambang sakit'),(140,'mesin jet dekat')]
for L,n in items: ax.barh(n,L,color=B if L<85 else H,height=.6); ax.text(L+2,n,f'{L} dB',va='center',fontsize=8.5)
ax.axvline(85,color='k',ls=':',lw=1); ax.text(86,-.9,'batas aman\n8 jam',fontsize=7.5,va='top'); ax.set_xlim(0,165); ax.set_xlabel('taraf intensitas (dB)'); ax.tick_params(axis='y',labelsize=8.5); sp(ax); sv(f,'desibel.png')
# 5 doppler
f,ax=plt.subplots(figsize=(5,2.6)); clean(ax)
for i,r in enumerate([.35,.7,1.05,1.4,1.75]): ax.add_patch(Circle((1.6-.22*(i),0),r,fc='none',ec=B,lw=1.2))
ax.add_patch(Circle((1.6,0),.07,fc=H)); ar(ax,(1.7,0),(2.3,0),H,1.8); ax.text(1.75,.15,'$v_s$',color=H,fontsize=9)
ax.text(3.0,-.5,'di depan:\n$\\lambda$ memendek,\n$f$ naik',fontsize=8.5); ax.text(-2.9,-.5,'di belakang:\n$\\lambda$ memanjang,\n$f$ turun',fontsize=8.5); ax.set_xlim(-3,4.6); ax.set_ylim(-2,2); sv(f,'doppler.png')
# 6 superposisi
f,axs=plt.subplots(1,2,figsize=(6.2,2.6)); x=np.linspace(0,4*np.pi,300)
for ax,ph,t in zip(axs,[0,np.pi],['konstruktif: sefase','destruktif: berlawanan fase']):
    ax.plot(x,np.sin(x)+2.6,color=B,lw=1.3); ax.plot(x,np.sin(x+ph),color=G,lw=1.3); ax.plot(x,np.sin(x)+np.sin(x+ph)-3.4,color=H,lw=2); ax.axis('off'); ax.set_title(t,fontsize=9.5)
    ax.text(-.6,2.6,'1',fontsize=8.5); ax.text(-.6,0,'2',fontsize=8.5); ax.text(-1.6,-3.4,'jumlah',fontsize=8.5); ax.set_xlim(-1.8,13); ax.set_ylim(-5.8,3.9)
sv(f,'superposisi.png')
# 7 layangan
f,ax=plt.subplots(figsize=(5.6,2.2)); t=np.linspace(0,1,2000); y=np.cos(2*np.pi*40*t)+np.cos(2*np.pi*44*t); ax.plot(t,y,color=B,lw=.8); ax.plot(t,2*np.cos(2*np.pi*2*t),color=H,lw=1.3,ls='--'); ax.plot(t,-2*np.cos(2*np.pi*2*t),color=H,lw=1.3,ls='--')
dar(ax,(.125,2.4),(.375,2.4)); ax.text(.25,2.55,'$T_{layangan}$',ha='center',fontsize=9); ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel('waktu'); ax.set_ylim(-2.3,3.1); sp(ax); sv(f,'layangan.png')
# 8 senar
f,ax=plt.subplots(figsize=(5.4,3.3)); x=np.linspace(0,1,200)
for i,n in enumerate([1,2,3,4]):
    y0=-i*1.0; ax.plot(x,y0+.35*np.sin(n*np.pi*x),color=B,lw=1.6); ax.plot(x,y0-.35*np.sin(n*np.pi*x),color=B,lw=1,ls='--'); ax.plot([0,1],[y0,y0],color='gray',lw=.5)
    ax.text(1.05,y0,f'$n = {n}$:  $\\lambda = 2L'+('' if n==1 else f'/{n}')+f'$,  $f = {n if n>1 else ""}f_1$',va='center',fontsize=9)
ax.plot([0,0],[-3.5,.5],'k',lw=2); ax.plot([1,1],[-3.5,.5],'k',lw=2); ax.axis('off'); ax.set_xlim(-.05,2.0); sv(f,'senar.png')
# 9 pipa
f,ax=plt.subplots(figsize=(6,3)); x=np.linspace(0,1,100)
def pipe(x0,y0,closed,n,lab):
    ax.plot([x0,x0+1],[y0+.22,y0+.22],'k',lw=1.5); ax.plot([x0,x0+1],[y0-.22,y0-.22],'k',lw=1.5)
    if closed: ax.plot([x0,x0],[y0-.22,y0+.22],'k',lw=2.5); yy=.2*np.sin((2*n-1)*np.pi*x/2)
    else: yy=.2*np.cos(n*np.pi*x)
    ax.plot(x0+x,y0+yy,color=B,lw=1.4); ax.plot(x0+x,y0-yy,color=B,lw=1,ls='--'); ax.text(x0+.5,y0-.42,lab,ha='center',fontsize=8.5)
pipe(0,1.6,False,1,'$f_1 = v/2L$'); pipe(0,.6,False,2,'$f_2 = 2f_1$'); pipe(0,-.4,False,3,'$f_3 = 3f_1$')
pipe(1.5,1.6,True,1,'$f_1 = v/4L$'); pipe(1.5,.6,True,2,'$f_3 = 3f_1$'); pipe(1.5,-.4,True,3,'$f_5 = 5f_1$')
ax.text(.5,2.05,'terbuka di kedua ujung',ha='center',fontsize=9.5); ax.text(2.0,2.05,'tertutup di satu ujung',ha='center',fontsize=9.5); ax.axis('off'); ax.set_xlim(-.1,2.6); ax.set_ylim(-1,2.3); sv(f,'pipa.png')
# 10 interferensi dua sumber
f,ax=plt.subplots(figsize=(4.4,2.8)); clean(ax); ax.add_patch(Circle((0,.8),.1,fc=H)); ax.add_patch(Circle((0,-.8),.1,fc=H)); ax.plot([3.5],[.6],'o',color=T)
ax.plot([0,3.5],[.8,.6],color=B,lw=1.5); ax.plot([0,3.5],[-.8,.6],color=B,lw=1.5); ax.text(1.7,.95,'$r_1$'); ax.text(1.7,-.45,'$r_2$'); ax.text(3.6,.65,'P'); ax.text(-.75,.75,'$S_1$'); ax.text(-.75,-.85,'$S_2$')
ax.text(1.75,-1.6,r'$\Delta r = r_2 - r_1$',ha='center',fontsize=9); ax.set_xlim(-1,4.2); ax.set_ylim(-1.9,1.5); sv(f,'duasumber.png')
# 11 spektrum EM
f,ax=plt.subplots(figsize=(6.4,1.9)); names=[('radio',1e0,1e-1),('gel. mikro',1e-1,1e-3),('inframerah',1e-3,7e-7),('tampak',7e-7,4e-7),('ultraungu',4e-7,1e-8),('sinar X',1e-8,1e-11),('gama',1e-11,1e-13)]
cols=['#d9e6f2','#bcd4ea','#9cc0df',H,'#7fa9d1','#5b8fc2','#3f76ae']
for (n,a,b),c in zip(names,cols):
    ax.barh(0,np.log10(a)-np.log10(b),left=-np.log10(a),color=c,edgecolor='w'); ax.text(-(np.log10(a)+np.log10(b))/2,0,n,ha='center',va='center',fontsize=7.5,rotation=0 if n not in('tampak',) else 90,color='w' if n in ('tampak','sinar X','gama') else 'k')
ax.set_yticks([]); ax.set_xticks(range(0,14,2)); ax.set_xticklabels([f'$10^{{{-i}}}$' if i else '1' for i in range(0,14,2)]); ax.set_xlabel('panjang gelombang (m)'); ax.set_xlim(0,13)
for s in ('top','right','left'): ax.spines[s].set_visible(False)
sv(f,'spektrum.png')
# 12 kotak
f,ax=plt.subplots(figsize=(4.4,3)); x=np.linspace(0,1,200)
for n in (1,2,3): ax.plot(x,n*n+.9*np.sin(n*np.pi*x),color=B,lw=1.6); ax.plot([0,1],[n*n,n*n],color='gray',lw=.6,ls=':'); ax.text(1.06,n*n,f'$n = {n}$,  $E = {"" if n==1 else n*n}E_1$',va='center',fontsize=9)
ax.plot([0,0],[0,10.5],'k',lw=2.5); ax.plot([1,1],[0,10.5],'k',lw=2.5); ax.plot([0,1],[0,0],'k',lw=1); ax.text(.5,-.6,'$L$',ha='center'); ax.axis('off'); ax.set_xlim(-.1,2.0); ax.set_ylim(-1,10.8); sv(f,'kotak.png')
