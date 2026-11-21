import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.ticker as mt
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle
plt.rcParams.update({"font.family":"Liberation Sans","font.size":9.5,"mathtext.fontset":"dejavusans","axes.linewidth":0.8})
K="black"; G="0.55"; L="0.85"
def save(fig,n): fig.savefig(n,dpi=220,bbox_inches="tight",facecolor="white"); plt.close(fig)
def arr(ax,p,q,lw=1.4,c=K,ms=10,style="-|>",ls="-"): ax.add_patch(FancyArrowPatch(p,q,arrowstyle=style,mutation_scale=ms,lw=lw,color=c,linestyle=ls,shrinkA=0,shrinkB=0))
def sp(ax):
    for s in ["top","right"]: ax.spines[s].set_visible(False)
def koma(ax,which="both",nd=None):
    f=mt.FuncFormatter(lambda v,p: (f"{v:g}" if nd is None else f"{v:.{nd}f}").replace(".",","))
    if which in("x","both"): ax.xaxis.set_major_formatter(f)
    if which in("y","both"): ax.yaxis.set_major_formatter(f)

# 1 sumbu posisi dan perpindahan
fig,ax=plt.subplots(figsize=(6.8,2.0)); ax.axis("off")
ax.plot([-45,55],[0,0],c=K,lw=1.2); arr(ax,(54,0),(57,0))
for x in range(-40,51,10):
    ax.plot([x,x],[-0.08,0.08],c=K,lw=0.8); ax.text(x,-0.3,str(x),ha="center",fontsize=8)
ax.text(58,-0.3,"$x$ (m)",fontsize=9)
ax.plot(0,0,"o",c=K,ms=5); ax.text(0,-0.62,"awal",ha="center",fontsize=8)
ax.plot(-30,0,"s",c=K,ms=5); ax.text(-30,-0.62,"akhir",ha="center",fontsize=8)
arr(ax,(0,0.45),(40,0.45),lw=1.1); ax.text(20,0.55,"40 m ke timur",ha="center",fontsize=8.5)
arr(ax,(40,0.95),(-30,0.95),lw=1.1); ax.text(5,1.05,"70 m ke barat",ha="center",fontsize=8.5)
arr(ax,(0,-1.05),(-30,-1.05),lw=2.2); ax.text(-15,-1.45,r"perpindahan $\Delta x=-30$ m",ha="center",fontsize=8.5)
ax.set_xlim(-48,66); ax.set_ylim(-1.6,1.4)
save(fig,"fig01_sumbu.png")

# 2 diagram gerak
fig,axs=plt.subplots(3,1,figsize=(6.6,2.9))
def md(ax,xs,ttl,a):
    ax.axis("off"); ax.set_xlim(-0.6,10.6); ax.set_ylim(-0.75,0.9)
    for i,x in enumerate(xs):
        ax.plot(x,0,"o",c=K,ms=6)
        if i<len(xs)-1: arr(ax,(x+0.12,0),(xs[i+1]-0.12,0),lw=1.0,ms=8)
    ax.text(-0.5,0.55,ttl,fontsize=8.8)
    if a==0: ax.text(9.2,-0.55,r"$\vec a=0$",fontsize=9)
    else:
        x0=7.6; arr(ax,(x0,-0.5),(x0+a*1.2,-0.5),lw=2.0); ax.text(x0+a*1.2+(0.15 if a>0 else -0.55),-0.6,r"$\vec a$",fontsize=10)
md(axs[0],[0,2,4,6,8,10],"(a) kecepatan tetap: jarak antartitik sama",0)
md(axs[1],[0,0.6,1.8,3.6,6.0,9.0],"(b) makin cepat: jarak antartitik membesar; $\\vec a$ searah $\\vec v$",1)
md(axs[2],[0,3.0,5.4,7.2,8.4,9.0],"(c) makin lambat: jarak antartitik mengecil; $\\vec a$ berlawanan $\\vec v$",-1)
save(fig,"fig02_diagramgerak.png")

# 3 tali busur menuju garis singgung
fig,ax=plt.subplots(figsize=(5.4,3.5))
t=np.linspace(0,3.3,200); ax.plot(t,3*t**2,c=K,lw=1.8)
for dt,ls,lab in [(1.0,":","$\\Delta t=1$ s: 15 m/s"),(0.5,"--","$\\Delta t=0{,}5$ s: 13,5 m/s")]:
    t2=2+dt; m=(3*t2**2-12)/dt; tt=np.array([1.3,3.3]); ax.plot(tt,12+m*(tt-2),c=K,lw=0.9,ls=ls,label="tali busur, "+lab); ax.plot(t2,3*t2**2,"o",c=K,ms=4)
tt=np.array([1.2,3.2]); ax.plot(tt,12+12*(tt-2),c=G,lw=2.2,label="garis singgung di $t=2$ s: 12 m/s",zorder=1)
ax.plot(2,12,"o",c=K,ms=6)
ax.set_xlabel("$t$ (s)"); ax.set_ylabel("$x$ (m)"); ax.set_xlim(0,3.4); ax.set_ylim(0,34); ax.legend(frameon=False,fontsize=8,loc="upper left"); sp(ax); koma(ax)
save(fig,"fig03_singgung.png")

# 4 tiga grafik x v a (kubik)
fig,axs=plt.subplots(3,1,figsize=(5.2,5.6),sharex=True)
t=np.linspace(0,3,300)
axs[0].plot(t,2*t**3-9*t**2+12*t,c=K,lw=1.6); axs[0].set_ylabel("$x$ (m)")
axs[1].plot(t,6*t**2-18*t+12,c=K,lw=1.6); axs[1].set_ylabel("$v$ (m/s)"); axs[1].axhline(0,c=K,lw=0.6)
axs[1].fill_between(t,6*t**2-18*t+12,0,where=(t>=1)&(t<=2),color=L)
axs[2].plot(t,12*t-18,c=K,lw=1.6); axs[2].set_ylabel("$a$ (m/s²)"); axs[2].axhline(0,c=K,lw=0.6); axs[2].set_xlabel("$t$ (s)")
for ax in axs:
    sp(ax); koma(ax)
    for tv in [1,2]: ax.axvline(tv,c=G,lw=0.7,ls=":")
    ax.axvline(1.5,c=G,lw=0.7,ls="--")
axs[0].plot([1,2],[5,4],"o",c=K,ms=4); axs[0].text(1.03,5.6,"puncak:\n$v=0$",fontsize=7.5); axs[0].text(2.03,2.2,"lembah:\n$v=0$",fontsize=7.5)
axs[1].text(0.45,1.2,"daerah kelabu:\nbergerak mundur",fontsize=7.5,ha="center"); axs[1].text(1.55,6.5,"$v$ paling negatif\nsaat $a=0$",fontsize=7.5)
fig.tight_layout(); save(fig,"fig04_xva.png")

# 5 v-t lift
fig,ax=plt.subplots(figsize=(5.4,2.7))
T=[0,4,10,12]; V=[0,2,2,0]; ax.plot(T,V,c=K,lw=1.8); ax.fill_between(T,V,color=L)
ax.plot([4,4],[0,2],c=K,lw=0.6,ls=":"); ax.plot([10,10],[0,2],c=K,lw=0.6,ls=":")
for x,s in [(2.7,"4 m"),(7,"12 m"),(10.65,"2 m")]: ax.text(x,0.55,s,ha="center",fontsize=9)
for x,s in [(1.4,"$a=+0{,}5$"),(7,"$a=0$"),(11.75,"$a=-1$")]: ax.text(x,2.15 if x!=1.4 else 1.3,s,ha="center",fontsize=8.5)
ax.set_xlabel("$t$ (s)"); ax.set_ylabel("$v$ (m/s)"); ax.set_ylim(0,2.6); ax.set_xlim(0,13); sp(ax); koma(ax)
save(fig,"fig05_lift.png")

# 6 luas pita v-t
fig,axs=plt.subplots(1,2,figsize=(6.8,2.6))
t=np.linspace(0,4,200); v=1+0.6*t**1.5
for ax,n in zip(axs,[4,16]):
    ax.plot(t,v,c=K,lw=1.6); w=4/n
    for i in range(n):
        ti=i*w; ax.add_patch(Rectangle((ti,0),w,1+0.6*(ti+w/2)**1.5,fc=L,ec=K,lw=0.5))
    ax.set_xlabel("$t$"); ax.set_ylabel("$v$"); ax.set_xticks([]); ax.set_yticks([]); sp(ax); ax.set_ylim(0,6.3)
    ax.set_title(f"{n} pita",fontsize=9)
axs[0].annotate(r"luas pita $=v\,\Delta t$"+"\n= perpindahan kecil",xy=(2.5,1.5),xytext=(0.2,4.6),arrowprops=dict(arrowstyle="->",lw=0.7),fontsize=8)
fig.tight_layout(); save(fig,"fig06_pita.png")

# 7 konstan a tiga grafik
fig,axs=plt.subplots(1,3,figsize=(7.0,2.3))
t=np.linspace(0,4,100)
axs[0].plot(t,1+1.0*t+0.5*0.8*t**2,c=K,lw=1.6); axs[0].set_title("posisi: parabola",fontsize=9); axs[0].set_ylabel("$x$")
axs[0].text(0.25,1.6,"$x_0$",fontsize=9)
axs[1].plot(t,1.0+0.8*t,c=K,lw=1.6); axs[1].set_title("kecepatan: garis lurus",fontsize=9); axs[1].set_ylabel("$v$"); axs[1].set_ylim(0,4.6)
axs[1].text(0.15,0.55,"$v_0$",fontsize=9); axs[1].text(2.0,1.7,"kemiringan $=a$",fontsize=8)
axs[2].plot(t,0*t+0.8,c=K,lw=1.6); axs[2].set_title("percepatan: tetap",fontsize=9); axs[2].set_ylabel("$a$"); axs[2].set_ylim(0,1.5)
for ax in axs: ax.set_xlabel("$t$"); ax.set_xticks([]); ax.set_yticks([]); sp(ax)
fig.tight_layout(); save(fig,"fig07_akonstan.png")

# 8 trapesium v-t penurunan
fig,ax=plt.subplots(figsize=(4.6,2.8))
ax.fill([0,3,3,0],[0,0,1,1],fc=L,ec=K,lw=0.8); ax.fill([0,3,3],[1,1,2.8],fc="0.7",ec=K,lw=0.8)
ax.plot([0,3],[1,2.8],c=K,lw=1.8)
ax.text(1.5,0.45,"persegi panjang\n$v_0t$",ha="center",fontsize=8.5); ax.text(2.15,1.45,r"segitiga" "\n" r"$\frac{1}{2}(at)\,t$",ha="center",fontsize=8.5)
ax.set_xticks([0,3]); ax.set_xticklabels(["0","$t$"]); ax.set_yticks([1,2.8]); ax.set_yticklabels(["$v_0$","$v_0+at$"])
ax.set_xlabel("waktu"); ax.set_ylabel("kecepatan"); ax.set_xlim(0,3.6); ax.set_ylim(0,3.2); sp(ax)
save(fig,"fig08_trapesium.png")

# 9 jatuh bebas strobo
fig,ax=plt.subplots(figsize=(3.0,4.6)); ax.axis("off")
g=9.8; ts=np.arange(0,5)*0.1; ys=-0.5*g*ts**2*100
ax.plot([0,0],[4,-84],c=K,lw=0.8)
for y in range(0,-81,-10):
    ax.plot([-0.06,0],[y,y],c=K,lw=0.7); ax.text(-0.1,y,str(-y),ha="right",va="center",fontsize=7.5)
ax.text(-0.1,8,"cm",fontsize=8,ha="right")
ax.plot([0.3]*5,ys,"o",c=L,mec=K,ms=11)
for t,y in zip(ts,ys): ax.text(0.5,y,f"$t={t:.1f}$ s".replace(".","{,}"),va="center",fontsize=8)
for i in range(4):
    ax.annotate("",xy=(1.45,ys[i+1]),xytext=(1.45,ys[i]),arrowprops=dict(arrowstyle="<->",lw=0.7))
    ax.text(1.55,(ys[i]+ys[i+1])/2,f"{abs(ys[i+1]-ys[i]):.1f} cm".replace(".",","),va="center",fontsize=7.5)
ax.set_xlim(-0.5,2.4); ax.set_ylim(-88,12)
save(fig,"fig09_strobo.png")

# 10 lempar ke atas y-t v-t
fig,axs=plt.subplots(2,1,figsize=(5.0,4.4),sharex=True)
tf=4.0653; t=np.linspace(0,tf,200)
axs[0].plot(t,20+15*t-4.9*t**2,c=K,lw=1.6); axs[0].set_ylabel("$y$ (m)"); axs[0].axhline(20,c=G,lw=0.6,ls=":")
axs[0].plot([1.531],[31.48],"o",c=K,ms=4); axs[0].text(1.6,32.2,"titik tertinggi: 31,5 m",fontsize=8)
axs[0].text(3.15,21,"tinggi atap",fontsize=7.5); axs[0].set_ylim(0,37)
axs[1].plot(t,15-9.8*t,c=K,lw=1.6); axs[1].axhline(0,c=K,lw=0.6); axs[1].set_ylabel("$v$ (m/s)"); axs[1].set_xlabel("$t$ (s)")
axs[1].plot([1.531],[0],"o",c=K,ms=4); axs[1].text(1.6,2.5,"$v=0$, tetapi $a=-9{,}8$ m/s²",fontsize=8)
axs[1].text(0.5,-19,"kemiringan tetap $=-g$",fontsize=8)
for ax in axs: sp(ax); koma(ax); ax.axvline(1.531,c=G,lw=0.6,ls=":")
fig.tight_layout(); save(fig,"fig10_lempar.png")

# 11 kejar
fig,ax=plt.subplots(figsize=(5.0,3.0))
t=np.linspace(0,24,200); ax.plot(t,30*t,c=K,lw=1.4,ls="--",label="pengebut: $x=30t$"); ax.plot(t,1.5*t**2,c=K,lw=1.8,label="polisi: $x=1{,}5t^2$")
ax.plot(20,600,"o",c=K,ms=5); ax.plot([20,20],[0,600],c=G,lw=0.6,ls=":"); ax.plot([0,20],[600,600],c=G,lw=0.6,ls=":")
ax.plot(10,150,"s",c=K,ms=4); ax.annotate("kecepatan sama ($t=10$ s):\njarak antara keduanya terbesar",xy=(10,150),xytext=(11.5,40),arrowprops=dict(arrowstyle="->",lw=0.7),fontsize=7.8)
ax.set_xlabel("$t$ (s)"); ax.set_ylabel("$x$ (m)"); ax.legend(frameon=False,fontsize=8.5); sp(ax); ax.set_xlim(0,24); ax.set_ylim(0,760)
save(fig,"fig11_kejar.png")

# 12 jarak berhenti
fig,ax=plt.subplots(figsize=(5.4,2.6))
vk=[40,60,80,100]; r=[v/3.6*0.75 for v in vk]; b=[(v/3.6)**2/12 for v in vk]
y=np.arange(4)
ax.barh(y,r,color="white",edgecolor=K,lw=0.9,label="jarak reaksi (0,75 s)"); ax.barh(y,b,left=r,color=G,edgecolor=K,lw=0.9,label="jarak pengereman ($a=-6$ m/s²)")
for i in range(4): ax.text(r[i]+b[i]+1.5,i,f"{r[i]+b[i]:.0f} m",va="center",fontsize=8.5)
ax.set_yticks(y); ax.set_yticklabels([f"{v} km/jam" for v in vk]); ax.set_xlabel("jarak berhenti (m)"); ax.legend(frameon=False,fontsize=8,loc="lower right"); sp(ax); ax.set_xlim(0,100)
save(fig,"fig12_berhenti.png")

# 13 hambatan udara
fig,ax=plt.subplots(figsize=(5.0,2.8))
t=np.linspace(0,22,200); ax.plot(t,55*np.tanh(9.8*t/55),c=K,lw=1.8,label="dengan hambatan udara"); ax.plot(t[:65],9.8*t[:65],c=K,lw=1.1,ls="--",label="tanpa hambatan: $v=gt$")
ax.axhline(55,c=G,lw=0.7,ls=":"); ax.text(13,57,"kecepatan terminal 55 m/s",fontsize=8)
ax.set_xlabel("$t$ (s)"); ax.set_ylabel("kelajuan (m/s)"); ax.set_ylim(0,72); ax.set_xlim(0,22); ax.set_xticks([0,5,10,15,20]); ax.legend(frameon=False,fontsize=8,loc="lower right"); sp(ax)
save(fig,"fig13_terminal.png")
print("ok")
