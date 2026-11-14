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
R=8.314
# 1 skala
f,ax=plt.subplots(figsize=(5.2,3)); ax.axis('off')
cols=[('Kelvin',[0,77,273.15,310.15,373.15],'K'),('Celsius',[-273.15,-196,0,37,100],'°C'),('Fahrenheit',[-459.67,-321,32,98.6,212],'°F')]
ys=[0,.21,.73,.80,.92]; labs=['nol mutlak','nitrogen cair mendidih','air membeku','suhu tubuh','air mendidih']
for i,(n,v,un) in enumerate(cols):
    x=1.6+i*1.3; ax.plot([x,x],[0,1],color=B,lw=4); ax.text(x,1.08,n,ha='center',fontsize=9.5,fontweight='bold',color=T)
    for y,val in zip(ys,v): ax.plot([x-.08,x+.08],[y,y],'k',lw=1); ax.text(x+.14,y,f'{val:g}'.replace('.',','),va='center',fontsize=8.5)
for y,l in zip(ys,labs): ax.text(1.35,y,l,ha='right',va='center',fontsize=8.5)
ax.set_xlim(-.6,5.2); ax.set_ylim(-.08,1.15); sv(f,'skala.png')
# 2 air
f,ax=plt.subplots(figsize=(4.8,2.9)); Tc=np.linspace(0,12,100); rho=999.84+0.0679*Tc-0.00909*Tc**2+0.0001*Tc**3
ax.plot(Tc,rho,color=B,lw=2.2); ax.plot([4],[rho[np.argmin(abs(Tc-4))]],'o',color=H); ax.text(4.3,999.985,'paling rapat pada 4 °C',fontsize=9,color=H)
ax.set_xlabel('suhu (°C)'); ax.set_ylabel('massa jenis air (kg/m³)'); ax.ticklabel_format(useOffset=False); sp(ax); sv(f,'air.png')
# 3 isoterm
f,ax=plt.subplots(figsize=(4.8,3)); V=np.linspace(4,50,200)
for Tk,c in [(200,B),(300,G),(450,H)]: ax.plot(V,R*Tk/V,color=c,lw=2,label=f'{Tk} K')
ax.set_xlabel('volume (L), untuk 1 mol'); ax.set_ylabel('tekanan (kPa)'); ax.set_ylim(0,700); ax.legend(frameon=False,fontsize=9,title='isoterm'); sp(ax); sv(f,'isoterm.png')
# 4 kurva pemanasan
f,ax=plt.subplots(figsize=(5.6,3)); Q=[0,2.1,35.5,77.4,303,307]; Tm=[-10,0,0,100,100,120]
ax.plot(Q,Tm,color=B,lw=2.2); ax.set_xlabel('kalor yang diberikan (kJ), untuk 100 g'); ax.set_ylabel('suhu (°C)')
for x,y,t in [(19,6,'es melebur'),(52,58,'air memanas'),(190,106,'air mendidih')]: ax.text(x,y,t,fontsize=8.5,color=T,ha='center')
ax.text(-2,-22,'es',fontsize=8.5,color=T); ax.text(300,126,'uap',fontsize=8.5,color=T); ax.set_ylim(-28,135); sp(ax); sv(f,'pemanasan.png')
# 5 konduksi
f,ax=plt.subplots(figsize=(4.4,2.6)); clean(ax); ax.add_patch(Rectangle((1.5,0),1.2,2,fc='#ccc',ec='k')); ax.text(.7,1,'panas\n$T_1$',ha='center',color=H,fontsize=10); ax.text(3.5,1,'dingin\n$T_2$',ha='center',color=B,fontsize=10)
for y in (.5,1,1.5): ar(ax,(1.6,y),(2.6,y),H,1.8)
dar(ax,(1.5,-.25),(2.7,-.25)); ax.text(2.1,-.6,'$d$',ha='center'); ax.text(2.1,2.15,'luas $A$',ha='center',fontsize=9); ax.set_xlim(0,4.2); ax.set_ylim(-.8,2.4); sv(f,'konduksi.png')
# 6 planck
f,ax=plt.subplots(figsize=(5,3)); lam=np.linspace(.1,3,400)*1e-6; h=6.626e-34;c=3e8;k=1.381e-23
for Tk,col in [(3000,B),(4000,G),(5800,H)]:
    Bl=2*h*c**2/lam**5/(np.exp(h*c/(lam*k*Tk))-1); ax.plot(lam*1e6,Bl/1e13,color=col,lw=2,label=f'{Tk} K')
ax.axvspan(.4,.7,color='#eee'); ax.text(.55,2.45,'tampak',ha='center',fontsize=8); ax.set_xlabel('panjang gelombang (μm)'); ax.set_ylabel('pancaran (satuan sembarang)'); ax.set_yticks([]); ax.legend(frameon=False,fontsize=9); ax.set_xlim(0,3); sp(ax); sv(f,'planck.png')
# 7 kotak
f,ax=plt.subplots(figsize=(4,2.8)); clean(ax); ax.add_patch(Rectangle((0,0),3,2,fc=M,ec='k',lw=1.5)); rng=np.random.default_rng(4)
for i in range(14):
    x,y=rng.uniform(.2,2.8),rng.uniform(.2,1.8); a=rng.uniform(0,6.28); ax.add_patch(Circle((x,y),.05,fc=B)); ar(ax,(x,y),(x+.3*np.cos(a),y+.3*np.sin(a)),B,1,7)
ax.add_patch(Circle((2.7,1.0),.06,fc=H)); ar(ax,(2.3,1.25),(2.68,1.02),H,1.6,9); ar(ax,(2.68,.98),(2.3,.75),H,1.6,9); ax.text(3.1,1,r'$\Delta p = 2mv_x$',fontsize=9,va='center'); dar(ax,(0,-.2),(3,-.2)); ax.text(1.5,-.5,'$L$',ha='center'); ax.set_xlim(-.2,4.6); ax.set_ylim(-.7,2.2); sv(f,'kotak.png')
# 8 MB suhu
def mb(v,Mm,Tk): m=Mm/6.022e23; return 4*np.pi*(m/(2*np.pi*k*Tk))**1.5*v**2*np.exp(-m*v**2/(2*k*Tk))
f,ax=plt.subplots(figsize=(5,3)); v=np.linspace(0,2500,500)
for Tk,col in [(300,B),(1000,H)]: ax.plot(v,mb(v,.028,Tk)*1e3,color=col,lw=2,label=f'N$_2$, {Tk} K')
for vv,n in [(421,'$v_p$'),(475,r'$\bar v$'),(515,'$v_{rms}$')]: ax.plot([vv,vv],[0,mb(vv,.028,300)*1e3],color='gray',lw=.8,ls=':')
ax.text(300,2.15,r'$v_p$   $\bar v$   $v_{rms}$',fontsize=8.5); ax.set_xlabel('kelajuan (m/s)'); ax.set_ylabel('bagian molekul'); ax.set_yticks([]); ax.legend(frameon=False,fontsize=9); ax.set_xlim(0,2500); ax.set_ylim(0,2.4); sp(ax); sv(f,'mbsuhu.png')
# 9 MB massa
f,ax=plt.subplots(figsize=(5,3)); v=np.linspace(0,4000,600)
for Mm,n,col in [(.032,'O$_2$',B),(.004,'He',G),(.002016,'H$_2$',H)]: ax.plot(v,mb(v,Mm,300)*1e3,color=col,lw=2,label=n)
ax.set_xlabel('kelajuan (m/s)'); ax.set_ylabel('bagian molekul'); ax.set_yticks([]); ax.legend(frameon=False,fontsize=9,title='300 K'); ax.set_xlim(0,4000); sp(ax); sv(f,'mbmassa.png')
# 10 fraksi Ea
f,ax=plt.subplots(figsize=(5,3)); E=np.linspace(0,12,400)
def fe(E,t): return 2/np.sqrt(np.pi)*np.sqrt(E)/t**1.5*np.exp(-E/t)
ax.plot(E,fe(E,1),color=B,lw=2,label='$T$ rendah'); ax.plot(E,fe(E,1.6),color=H,lw=2,label='$T$ tinggi')
ax.fill_between(E,fe(E,1.6),where=E>6,color=H,alpha=.35); ax.fill_between(E,fe(E,1),where=E>6,color=B,alpha=.6); ax.axvline(6,color='k',ls='--',lw=1); ax.text(6.15,.42,'$E_a$')
ax.set_xlabel('energi kinetik molekul'); ax.set_ylabel('bagian molekul'); ax.set_xticks([]); ax.set_yticks([]); ax.legend(frameon=False,fontsize=9); sp(ax); sv(f,'fraksi.png')
# 11 Cv H2
f,ax=plt.subplots(figsize=(5,3)); Tl=np.logspace(1.3,4,300)
def step(T,T0,w): return 1/(1+np.exp(-(np.log10(T)-np.log10(T0))/w))
Cv=1.5+step(Tl,90,.13)+step(Tl,2200,.16); ax.semilogx(Tl,Cv,color=B,lw=2.2)
for y,t in [(1.5,'translasi saja: $\\frac{3}{2}R$'),(2.5,'+ rotasi: $\\frac{5}{2}R$'),(3.5,'+ getaran: $\\frac{7}{2}R$')]: ax.axhline(y,color='gray',ls=':',lw=.8); ax.text(22,y+.07,t,fontsize=8.5)
ax.set_xlabel('suhu (K)'); ax.set_ylabel('$C_V/R$ untuk H$_2$'); ax.set_ylim(1,4); ax.set_yticks([1.5,2.5,3.5]); ax.set_yticklabels(['1,5','2,5','3,5']); sp(ax); sv(f,'cv.png')
# 12 jalan bebas
f,ax=plt.subplots(figsize=(4,2.8)); clean(ax); rng=np.random.default_rng(11); pts=[(0,0)]
for i in range(9): a=rng.uniform(0,6.28); l=rng.exponential(.6)+.15; pts.append((pts[-1][0]+l*np.cos(a),pts[-1][1]+l*np.sin(a)))
xs,ys=zip(*pts); ax.plot(xs,ys,color=B,lw=1.5)
for x,y in pts[1:-1]: ax.add_patch(Circle((x,y),.07,fc='#999',ec='k',lw=.5))
ax.add_patch(Circle(pts[0],.07,fc=H)); ax.add_patch(Circle(pts[-1],.07,fc=H)); ax.text(pts[0][0]+.1,pts[0][1]+.12,'awal',fontsize=8.5); ax.text(pts[-1][0]+.1,pts[-1][1]+.12,'akhir',fontsize=8.5)
ax.set_xlim(min(xs)-.4,max(xs)+.6); ax.set_ylim(min(ys)-.4,max(ys)+.4); sv(f,'jalan.png')
# 13 vdw
f,ax=plt.subplots(figsize=(5,3)); a=.3640;b=4.267e-5; V=np.linspace(6e-5,6e-4,400)
for Tk,col in [(280,B),(304,G),(340,H)]: ax.plot(V*1e3,(R*Tk/(V-b)-a/V**2)/1e6,color=col,lw=2,label=f'{Tk} K')
ax.plot(V*1e3,R*340/V/1e6,color=H,lw=1,ls='--'); ax.text(.36,9.2,'gas ideal, 340 K',fontsize=8,color=H)
ax.set_ylim(2,14); ax.set_xlim(.05,.6); ax.set_xlabel('volume molar (L/mol)'); ax.set_ylabel('tekanan (MPa)'); ax.legend(frameon=False,fontsize=9,title='CO$_2$'); sp(ax); sv(f,'vdw.png')
