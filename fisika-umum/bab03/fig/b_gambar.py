import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle, Arc, Polygon
plt.rcParams.update({"font.family":"Liberation Sans","font.size":9.5,"mathtext.fontset":"dejavusans","axes.linewidth":0.8})
K="black"; G="0.55"; L="0.85"
def save(fig,n): fig.savefig(n,dpi=220,bbox_inches="tight",facecolor="white"); plt.close(fig)
def arr(ax,p,q,lw=1.6,c=K,ms=11,ls="-"): ax.add_patch(FancyArrowPatch(p,q,arrowstyle="-|>",mutation_scale=ms,lw=lw,color=c,linestyle=ls,shrinkA=0,shrinkB=0))
def cl(ax,xl,yl): ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(*xl); ax.set_ylim(*yl)
def tanah(ax,x0,x1,y=0):
    ax.plot([x0,x1],[y,y],c=K,lw=1.1)
    for x in np.arange(x0+0.1,x1,0.25): ax.plot([x,x-0.12],[y,y-0.12],c=K,lw=0.5)
def sp(ax):
    for s in ["top","right"]: ax.spines[s].set_visible(False)
def F(ax,o,dx,dy,lab,off=(0,0),**kw):
    arr(ax,o,(o[0]+dx,o[1]+dy),**kw); ax.text(o[0]+dx+off[0],o[1]+dy+off[1],lab,ha="center",va="center",fontsize=9.5)

# 1 grafik gesekan
fig,ax=plt.subplots(figsize=(5.4,3.0))
ax.plot([0,196],[0,196],c=K,lw=1.8); ax.plot([196,196],[196,157],c=K,lw=0.8,ls=":"); ax.plot([196,330],[157,157],c=K,lw=1.8)
ax.plot([0,196],[196,196],c=G,lw=0.6,ls=":"); ax.plot([0,196],[157,157],c=G,lw=0.6,ls=":")
ax.set_yticks([157,196]); ax.set_yticklabels([r"$\mu_kn$",r"$\mu_sn$"]); ax.set_xticks([196]); ax.set_xticklabels([r"$\mu_sn$"])
ax.text(60,100,"diam:\n$f_s=F$",fontsize=9); ax.text(230,170,"meluncur: $f_k=\\mu_kn$",fontsize=9)
ax.set_xlabel("gaya dorong $F$"); ax.set_ylabel("gaya gesek $f$"); ax.set_xlim(0,340); ax.set_ylim(0,240); sp(ax)
save(fig,"fig01_grafik.png")

# 2 permukaan mikroskopik
fig,ax=plt.subplots(figsize=(5.2,1.9)); ax.axis("off")
rng=np.random.default_rng(5); x=np.linspace(0,10,160)
y1=0.25*np.sin(3.1*x)+0.18*np.sin(7.7*x+1)+0.1*rng.normal(size=x.size).cumsum()*0.08
y2=0.52+0.25*np.sin(2.7*x+2)+0.18*np.sin(8.3*x)+0.1*rng.normal(size=x.size).cumsum()*0.08
y2=np.maximum(y2,y1+0.02)
ax.fill_between(x,y1,-1.2,color=L); ax.plot(x,y1,c=K,lw=1.0); ax.fill_between(x,y2,2.3,color="0.7"); ax.plot(x,y2,c=K,lw=1.0)
idx=np.where(y2-y1<0.06)[0]
ax.plot(x[idx],y1[idx]+0.02,"o",c=K,ms=3)
ax.text(5,-0.75,"permukaan bawah",ha="center",fontsize=8.5); ax.text(5,1.8,"permukaan atas",ha="center",fontsize=8.5)
ax.set_ylim(-1.2,2.3)
save(fig,"fig02_mikro.png")

# 3 tarik bersudut
fig,ax=plt.subplots(figsize=(4.8,2.8)); cl(ax,(-2.6,3.4),(-2.0,2.4)); tanah(ax,-2.4,3.2,-0.4)
ax.add_patch(Rectangle((-0.7,-0.4),1.4,0.8,fc=L,ec=K)); o=(0,0)
a=np.radians(30); F(ax,o,2.0*np.cos(a),2.0*np.sin(a),r"$\vec T$",(0.2,0.12)); F(ax,o,0,1.5,r"$\vec n$",(0.25,0)); F(ax,o,0,-1.6,r"$m\vec g$",(0.35,0.05)); F(ax,o,-1.2,0,r"$\vec f_k$",(-0.05,0.25))
ax.add_patch(Arc(o,1.3,1.3,theta1=0,theta2=30,lw=0.8)); ax.text(0.9,0.13,"30°",fontsize=8); ax.plot([0,1.9],[0,0],c=G,lw=0.5,ls=":")
save(fig,"fig03_tarik.png")

# 4 bidang miring kasar naik/turun
fig,axs=plt.subplots(1,2,figsize=(6.8,2.8))
for ax,up in zip(axs,[True,False]):
    cl(ax,(-0.4,5.8),(-1.2,3.9)); th=np.radians(30); ax.add_patch(Polygon([(0,0),(5.0,0),(5.0,5.0*np.tan(th))],fc="0.95",ec=K,lw=1.1))
    c=np.array([2.6,2.6*np.tan(th)]); n=np.array([-np.sin(th),np.cos(th)]); t=np.array([np.cos(th),np.sin(th)]); o=c+n*0.3
    ax.add_patch(Polygon([c-t*0.45,c+t*0.45,c+t*0.45+n*0.6,c-t*0.45+n*0.6],fc=L,ec=K,lw=1.0))
    arr(ax,o,o+n*1.3); ax.text(*(o+n*1.5),r"$\vec n$",ha="center"); arr(ax,o,o+np.array([0,-1.4])); ax.text(o[0]+0.3,o[1]-1.35,r"$m\vec g$")
    fd=-t if up else t; arr(ax,o,o+fd*1.0); ax.text(*(o+fd*1.25+n*0.1),r"$\vec f_k$",ha="center")
    vd=t if up else -t; arr(ax,c+n*1.9-vd*0.5,c+n*1.9+vd*0.5,lw=1.0,c=G); ax.text(*(c+n*2.15),"$v$",ha="center",fontsize=9,color="0.3")
    ax.set_title("(a) bergerak naik: $a=g(\\sin\\theta+\\mu_k\\cos\\theta)$" if up else "(b) bergerak turun: $a=g(\\sin\\theta-\\mu_k\\cos\\theta)$",fontsize=8.5)
save(fig,"fig04_miring.png")

# 5 balok bertumpuk
fig,ax=plt.subplots(figsize=(6.4,2.4)); cl(ax,(-1.4,8.8),(-0.8,2.4)); tanah(ax,-1.2,3.6)
ax.add_patch(Rectangle((0,0),2.4,0.8,fc="white",ec=K)); ax.text(1.2,0.3,"3 kg",ha="center",fontsize=8.5); ax.add_patch(Rectangle((0.6,0.8),1.2,0.6,fc=L,ec=K)); ax.text(1.2,1.0,"1 kg",ha="center",fontsize=8.5)
arr(ax,(2.4,0.4),(3.5,0.4),lw=2.0); ax.text(3.0,0.65,"$F$",fontsize=10)
ax.add_patch(Rectangle((5.4,1.2),1.2,0.6,fc=L,ec=K)); arr(ax,(6.0,1.2),(7.0,1.2)); ax.text(7.6,1.2,r"$f_s$ (maju)",fontsize=8.5,va="center")
ax.add_patch(Rectangle((4.8,0.0),2.4,0.8,fc="white",ec=K)); arr(ax,(6.0,0.8),(5.0,0.8),c=G); ax.text(4.3,0.9,r"$f_s$",fontsize=8.5,color="0.3"); arr(ax,(7.2,0.4),(8.2,0.4),lw=2.0); ax.text(8.45,0.4,"$F$",va="center")
ax.text(6.0,2.15,"gaya mendatar pada tiap balok",ha="center",fontsize=8.5)
save(fig,"fig05_tumpuk.png")

# 6 tikungan datar dan miring
fig,axs=plt.subplots(1,2,figsize=(6.8,2.9))
ax=axs[0]; cl(ax,(-2.6,2.6),(-1.9,2.4)); tanah(ax,-2.2,2.2,-0.5); ax.add_patch(Rectangle((-0.7,-0.5),1.4,0.8,fc=L,ec=K)); o=(0,-0.1)
F(ax,o,0,1.6,r"$\vec n$",(0.25,0)); F(ax,o,0,-1.5,r"$m\vec g$",(0.4,0.05)); F(ax,o,-1.5,0,r"$\vec f_s$",(-0.1,0.25))
ax.text(-2.5,-0.1,"ke pusat\ntikungan",fontsize=7.5,ha="center",va="center",color="0.3"); ax.set_title("(a) tikungan datar: gesekan statis",fontsize=9)
ax=axs[1]; cl(ax,(-2.6,2.6),(-1.9,2.4)); th=np.radians(20); ax.add_patch(Polygon([(-2.2,-0.9),(2.2,-0.9),(2.2,-0.9+4.4*np.tan(th))],fc="0.95",ec=K,lw=1.0))
c=np.array([0.0,-0.9+2.2*np.tan(th)]); n=np.array([-np.sin(th),np.cos(th)]); t=np.array([np.cos(th),np.sin(th)]); o=c+n*0.35
ax.add_patch(Polygon([c-t*0.6,c+t*0.6,c+t*0.6+n*0.7,c-t*0.6+n*0.7],fc=L,ec=K))
arr(ax,o,o+n*1.9); ax.text(*(o+n*2.1),r"$\vec n$",ha="center"); arr(ax,o,o+np.array([0,-1.5])); ax.text(o[0]+0.4,o[1]-1.4,r"$m\vec g$")
arr(ax,o,o+np.array([n[0]*1.9,0]),lw=1.0,c=G); ax.plot([o[0]+n[0]*1.9]*2,[o[1],o[1]+n[1]*1.9],c=G,lw=0.5,ls=":"); ax.text(o[0]-1.25,o[1]+0.05,r"$n\sin\theta$",fontsize=8,color="0.3",ha="center")
ax.add_patch(Arc((-2.2,-0.9),1.6,1.6,theta1=0,theta2=20,lw=0.8)); ax.text(-1.2,-0.78,r"$\theta$",fontsize=9); ax.set_title("(b) tikungan miring: komponen gaya normal",fontsize=9)
save(fig,"fig06_tikungan.png")

# 7 bandul kerucut
fig,ax=plt.subplots(figsize=(3.4,3.2)); cl(ax,(-1.8,2.2),(-3.0,0.5)); tanah(ax,-0.8,0.8,0.2)
a=np.radians(30); Lb=2.0; P=np.array([Lb*np.sin(a),-Lb*np.cos(a)]); ax.plot([0,P[0]],[0.2,P[1]],c=K,lw=1.0); ax.plot([0,0],[0.2,P[1]],c=G,lw=0.6,ls=":")
th=np.linspace(0,2*np.pi,100); ax.plot(P[0]*np.cos(th),P[1]+0.22*np.sin(th),c=G,lw=0.7,ls="--"); ax.add_patch(Circle(P,0.1,fc=L,ec=K,zorder=3))
T=np.array([-np.sin(a),np.cos(a)]); arr(ax,P,P+T*1.1); ax.text(*(P+T*1.25+np.array([0.2,0])),r"$\vec T$"); arr(ax,P,P+np.array([0,-0.95])); ax.text(P[0]+0.35,P[1]-0.9,r"$m\vec g$")
ax.add_patch(Arc((0,0.2),0.9,0.9,theta1=270,theta2=300,lw=0.8)); ax.text(0.13,-0.55,r"$\theta$"); ax.text(0.28,-1.0,"$L$"); ax.text(P[0]/2,P[1]-0.42,"$r=L\\sin\\theta$",ha="center",fontsize=8)
save(fig,"fig07_kerucut.png")

# 8 lingkaran vertikal
fig,ax=plt.subplots(figsize=(3.8,3.6)); cl(ax,(-2.3,2.6),(-2.4,2.4)); th=np.linspace(0,2*np.pi,200); ax.plot(1.5*np.cos(th),1.5*np.sin(th),c=G,lw=0.9,ls="--"); ax.plot(0,0,"o",c=K,ms=3)
for P,up in [((0,1.5),True),((0,-1.5),False)]:
    ax.add_patch(Circle(P,0.12,fc=L,ec=K,zorder=3))
    if up:
        arr(ax,(-0.12,1.5),(-0.12,0.75)); ax.text(-0.45,1.0,r"$\vec T$"); arr(ax,(0.12,1.5),(0.12,0.65)); ax.text(0.5,0.95,r"$m\vec g$")
        ax.text(0.3,1.95,"puncak: $T+mg=mv^2/r$",fontsize=8.5,ha="center")
    else:
        arr(ax,(0,-1.5),(0,-0.5)); ax.text(0.3,-0.8,r"$\vec T$"); arr(ax,(0,-1.5),(0,-2.2)); ax.text(0.4,-2.1,r"$m\vec g$")
        ax.text(1.35,-1.75,"dasar:\n$T-mg=mv^2/r$",fontsize=8.5,ha="left")
save(fig,"fig08_vertikal.png")

# 9 terminal tiga tahap
fig,axs=plt.subplots(1,3,figsize=(6.2,2.6))
for ax,(D,ttl) in zip(axs,[(0.25,"baru jatuh:\n$a\\approx g$"),(0.8,"makin cepat:\n$a<g$"),(1.3,"kecepatan terminal:\n$a=0$")]):
    cl(ax,(-1.3,1.3),(-2.5,1.8)); ax.add_patch(Circle((0,0),0.14,fc=L,ec=K,zorder=3)); arr(ax,(0,0),(0,-1.3)); ax.text(0.4,-1.2,r"$m\vec g$")
    arr(ax,(0,0),(0,D),c="0.35"); ax.text(0.35,D-0.05,r"$\vec D$",color="0.3"); ax.text(0,-1.75,ttl,ha="center",va="top",fontsize=8.5)
save(fig,"fig09_terminal.png")
print("ok6")
