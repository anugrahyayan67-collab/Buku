import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle, Arc
plt.rcParams.update({"font.family":"Liberation Sans","font.size":10,"mathtext.fontset":"dejavusans"})
K="black"; G="0.55"; L="0.85"
def save(fig,n): fig.savefig(n,dpi=220,bbox_inches="tight",facecolor="white"); plt.close(fig)

# 1 skala panjang
fig,ax=plt.subplots(figsize=(7.2,2.9))
items=[(-15,"proton"),(-10,"atom"),(-7,"virus"),(-5,"sel darah\nmerah"),(-3,"butir\npasir"),(0,"manusia"),(4,"gunung"),(7,"Bumi"),(11,"jarak\nBumi–Matahari"),(16,"tahun\ncahaya"),(21,"galaksi\nBima Sakti"),(26,"alam semesta\nteramati")]
ax.plot([-17,28],[0,0],c=K,lw=1.4)
for i,(e,lab) in enumerate(items):
    up = i%2==0
    ax.plot([e,e],[0,0.55 if up else -0.55],c=K,lw=0.8); ax.plot(e,0,"o",c=K,ms=4)
    ax.text(e,0.65 if up else -0.65,lab,ha="center",va="bottom" if up else "top",fontsize=8)
for e in range(-15,28,3):
    ax.text(e,-0.12 if (e in [-15,-3,0]) else -0.12,"",fontsize=6)
for e in [-15,-10,-5,0,5,10,15,20,25]:
    ax.plot([e,e],[-1.72,-1.6],c=K,lw=0.8)
    ax.text(e,-1.78,f"$10^{{{e}}}$",fontsize=8,ha="center",va="top")
ax.plot([-17,28],[-1.6,-1.6],c=K,lw=0.7); ax.text(28.4,-1.85,"m",fontsize=9)
ax.set_xlim(-18,30); ax.set_ylim(-2.2,1.6); ax.axis("off")
save(fig,"fig01_skala.png")

# 2 akurasi presisi
fig,axs=plt.subplots(1,4,figsize=(7.4,2.3))
rng=np.random.default_rng(3)
cases=[((0,0),0.12,"akurat dan presis"),((0,0),0.55,"akurat, tidak presis"),((0.55,0.4),0.12,"presis, tidak akurat\n(galat sistematik)"),((0.5,-0.45),0.5,"tidak akurat,\ntidak presis")]
for ax,(c,s,t) in zip(axs,cases):
    ax.set_aspect("equal"); ax.axis("off")
    for r in [1.0,0.66,0.33]: ax.add_patch(Circle((0,0),r,fc="none",ec=K,lw=0.8))
    ax.add_patch(Circle((0,0),0.06,fc=K))
    p=rng.normal(0,s,(7,2))+np.array(c); ax.plot(p[:,0],p[:,1],"x",c=K,ms=6,mew=1.6)
    ax.text(0,-1.25,t,ha="center",va="top",fontsize=8.5); ax.set_xlim(-1.3,1.3); ax.set_ylim(-1.9,1.2)
save(fig,"fig02_akurasi.png")

# 3 penggaris
fig,ax=plt.subplots(figsize=(6.6,1.9)); ax.axis("off")
ax.add_patch(Rectangle((0,0),7.2,0.9,fc="white",ec=K,lw=1.1))
for i in range(0,71):
    x=0.2+i*0.1; h=0.42 if i%10==0 else (0.3 if i%5==0 else 0.18)
    ax.plot([x,x],[0.9,0.9-h],c=K,lw=0.7)
    if i%10==0 and i<70: ax.text(x,0.22,str(i//10),ha="center",fontsize=9)
ax.text(6.9,0.22,"cm",fontsize=8)
ax.add_patch(Rectangle((0.2,1.0),4.37,0.42,fc=L,ec=K,lw=1.0))
ax.plot([4.57,4.57],[0.9,1.75],c=K,lw=0.7,ls="--")
ax.text(4.57,1.82,"ujung benda: di antara 4,3 dan 4,4 cm",ha="center",fontsize=8.5)
ax.text(2.3,1.14,"benda",ha="center",fontsize=8.5)
ax.set_xlim(-0.1,7.4); ax.set_ylim(-0.1,2.1)
save(fig,"fig03_penggaris.png")

# 4 histogram pengukuran (data simulasi: 200 pengukuran periode, rata-rata 2,007 s, simpangan baku 0,05 s)
rng=np.random.default_rng(11); d=rng.normal(2.007,0.05,200)
fig,ax=plt.subplots(figsize=(5.6,2.9))
ax.hist(d,bins=17,color=L,edgecolor=K,lw=0.8)
m,s=d.mean(),d.std(ddof=1)
ax.axvline(m,c=K,lw=1.6); 
for xx in [m-s,m+s]: ax.axvline(xx,c=K,lw=1.0,ls="--")
ymax=ax.get_ylim()[1]
ax.text(m,ymax*1.03,r"rata-rata $\bar x$",ha="center",fontsize=8.5)
import matplotlib.ticker as mt
ax.xaxis.set_major_formatter(mt.FuncFormatter(lambda v,p: f"{v:.2f}".replace(".",",")))
ax.annotate("",xy=(m-s,ymax*0.86),xytext=(m+s,ymax*0.86),arrowprops=dict(arrowstyle="<->",lw=0.9))
ax.text(m+s+0.004,ymax*0.84,r"$\pm s$ (sekitar 68% data)",fontsize=8.5)
ax.set_xlabel("hasil pengukuran periode (s)"); ax.set_ylabel("banyaknya pengukuran")
for sp in ["top","right"]: ax.spines[sp].set_visible(False)
ax.set_ylim(0,ymax*1.12)
save(fig,"fig04_histogram.png"); print("hist",m,s)

# 5 kubus dibelah (tampak depan)
fig,axs=plt.subplots(1,3,figsize=(6.6,2.5))
for ax,n,t in zip(axs,[1,2,4],["1 kubus\nluas total $6a^2$","8 kubus\nluas total $12a^2$","64 kubus\nluas total $24a^2$"]):
    ax.set_aspect("equal"); ax.axis("off")
    s=1.0/n; gap=0.06 if n>1 else 0
    for i in range(n):
        for j in range(n):
            ax.add_patch(Rectangle((i*(s+gap),j*(s+gap)),s,s,fc=L,ec=K,lw=0.9))
    w=n*s+(n-1)*gap
    ax.text(w/2,-0.12,t,ha="center",va="top",fontsize=8.5); ax.set_xlim(-0.1,1.35); ax.set_ylim(-0.6,1.3)
save(fig,"fig05_kubus.png")

# 6 tangga awalan
fig,ax=plt.subplots(figsize=(7.2,1.7)); ax.axis("off")
pre=[(-15,"femto","f"),(-12,"piko","p"),(-9,"nano","n"),(-6,"mikro","µ"),(-3,"mili","m"),(0,"(satuan\ndasar)",""),(3,"kilo","k"),(6,"mega","M"),(9,"giga","G"),(12,"tera","T")]
ax.plot([-16.5,13.5],[0,0],c=K,lw=1.2)
for e,nm,sy in pre:
    ax.plot([e,e],[-0.1,0.1],c=K,lw=1.0)
    ax.text(e,0.2,f"$10^{{{e}}}$" if e!=0 else "$1$",ha="center",fontsize=8.5)
    ax.text(e,-0.25,nm,ha="center",va="top",fontsize=8.5)
    if sy: ax.text(e,-0.62,sy,ha="center",va="top",fontsize=10,weight="bold")
ax.add_patch(FancyArrowPatch((-3,0.62),(9,0.62),arrowstyle="-|>",mutation_scale=10,lw=1,color=K)); ax.text(3,0.7,"tiap anak tangga ke kanan: 1000 kali lebih besar",ha="center",fontsize=8)
ax.set_xlim(-17,14); ax.set_ylim(-0.95,0.95)
save(fig,"fig06_awalan.png")

# 7 bandul
fig,ax=plt.subplots(figsize=(2.9,2.9)); ax.set_aspect("equal"); ax.axis("off")
ax.plot([-0.7,0.7],[0,0],c=K,lw=1.6)
for xx in np.arange(-0.65,0.7,0.14): ax.plot([xx,xx+0.09],[0,0.09],c=K,lw=0.5)
a=np.radians(22); Lb=2.0; P=(Lb*np.sin(a),-Lb*np.cos(a))
ax.plot([0,P[0]],[0,P[1]],c=K,lw=1.1); ax.add_patch(Circle(P,0.13,fc=L,ec=K))
ax.plot([0,0],[0,-Lb],c=K,lw=0.6,ls=":"); ax.add_patch(Circle((-P[0],P[1]),0.13,fc="none",ec=K,ls="--",lw=0.7))
ax.text(P[0]/2+0.1,P[1]/2,"$L$",fontsize=11); ax.text(P[0]+0.2,P[1]-0.05,"$m$",fontsize=11)
ax.add_patch(FancyArrowPatch((1.3,-0.6),(1.3,-1.3),arrowstyle="-|>",mutation_scale=10,lw=1.2,color=K)); ax.text(1.38,-1.0,"$g$",fontsize=11)
ax.set_xlim(-1.2,1.8); ax.set_ylim(-2.4,0.3)
save(fig,"fig07_bandul.png")
