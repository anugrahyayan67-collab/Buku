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
def fbd(ax,o,forces,dot=True):
    if dot: ax.add_patch(Circle(o,0.07,fc=K))
    for (dx,dy,lab,off) in forces:
        arr(ax,o,(o[0]+dx,o[1]+dy)); ax.text(o[0]+dx+off[0],o[1]+dy+off[1],lab,ha="center",va="center",fontsize=9.5)

# 1 Galileo bidang miring
fig,ax=plt.subplots(figsize=(6.6,2.2)); cl(ax,(-0.3,12.5),(-0.4,2.4))
for k,(xe,ls) in enumerate([(4.5,"-"),(7.5,"--"),(11.5,":")]):
    ax.plot([0,2,xe],[2,0,2],c=K,lw=1.3,ls=ls)
ax.plot([2,12.3],[0,0],c=G,lw=1.3,ls="-."); ax.plot([-0.2,12.3],[2,2],c=G,lw=0.5,ls=":")
ax.add_patch(Circle((0.12,2.12),0.13,fc=L,ec=K))
ax.text(6.2,2.12,"bola selalu naik sampai ketinggian semula",fontsize=8.5,ha="center")
ax.text(9.0,0.12,"lereng mendatar: bola tidak pernah berhenti",fontsize=8.5,ha="center",color="0.3")
save(fig,"fig01_galileo.png")

# 2 a vs F, a vs 1/m
fig,axs=plt.subplots(1,2,figsize=(6.6,2.5))
F=np.linspace(0,10,10); axs[0].plot(F,F/2,c=K,lw=1.6,label="$m$"); axs[0].plot(F,F/4,c=K,lw=1.6,ls="--",label="$2m$")
axs[0].set_xlabel("gaya total $F$"); axs[0].set_ylabel("percepatan $a$"); axs[0].legend(frameon=False,fontsize=8.5); axs[0].set_title("(a) massa tetap: $a\\propto F$",fontsize=9)
m=np.linspace(0.5,6,100); axs[1].plot(m,6/m,c=K,lw=1.6); axs[1].set_xlabel("massa $m$"); axs[1].set_ylabel("percepatan $a$"); axs[1].set_title("(b) gaya tetap: $a\\propto 1/m$",fontsize=9)
for ax in axs: ax.set_xticks([]); ax.set_yticks([]); sp(ax)
fig.tight_layout(); save(fig,"fig02_hukum2.png")

# 3 resultan dua gaya (perahu)
fig,ax=plt.subplots(figsize=(5.2,2.6)); cl(ax,(-0.6,5.4),(-1.9,1.9))
ax.add_patch(Polygon([(-0.5,-0.25),(0.3,-0.25),(0.6,0),(0.3,0.25),(-0.5,0.25)],fc=L,ec=K))
A=np.array([3*np.cos(np.radians(30)),3*np.sin(np.radians(30))]); B=np.array([2*np.cos(np.radians(-45)),2*np.sin(np.radians(-45))])
arr(ax,(0.6,0),(0.6+A[0],A[1])); arr(ax,(0.6,0),(0.6+B[0],B[1])); arr(ax,(0.6,0),(0.6+A[0]+B[0],A[1]+B[1]),lw=2.4,c=G)
ax.plot([0.6+A[0],0.6+A[0]+B[0]],[A[1],A[1]+B[1]],c=K,lw=0.6,ls="--"); ax.plot([0.6+B[0],0.6+A[0]+B[0]],[B[1],A[1]+B[1]],c=K,lw=0.6,ls="--")
ax.text(0.6,1.25,r"$\vec F_1$ (300 N, 30°)",fontsize=8.5); ax.text(-0.4,-1.3,r"$\vec F_2$ (200 N, 45°)",fontsize=8.5); ax.text(3.3,-0.45,r"$\sum\vec F$",fontsize=10)
ax.plot([0.6,5.2],[0,0],c=G,lw=0.5,ls=":")
save(fig,"fig03_resultan.png")

# 4 buku di meja: gaya dan pasangan
fig,axs=plt.subplots(1,2,figsize=(7.0,3.0))
ax=axs[0]; cl(ax,(-2.2,2.4),(-1.9,2.3)); ax.add_patch(Rectangle((-1.6,-0.5),3.2,0.25,fc=L,ec=K)); ax.add_patch(Rectangle((-0.6,-0.25),1.2,0.4,fc="white",ec=K,lw=1.2))
arr(ax,(0,-0.05),(0,1.5)); ax.text(0.35,1.35,r"$\vec n$",fontsize=11); arr(ax,(0,-0.05),(0,-1.6)); ax.text(0.45,-1.45,r"$\vec F_g$",fontsize=11)
ax.text(0,2.0,"(a) gaya-gaya pada BUKU:\nsaling menyeimbangkan, bukan pasangan aksi–reaksi",ha="center",fontsize=8)
ax=axs[1]; cl(ax,(-3.0,3.4),(-2.4,2.3)); ax.add_patch(Rectangle((-1.2,-0.5),2.4,0.25,fc=L,ec=K)); ax.add_patch(Rectangle((-0.6,-0.25),1.2,0.4,fc="white",ec=K,lw=1.2))
ax.add_patch(Arc((0,-5.4),7,7,theta1=62,theta2=118,lw=1.2)); ax.text(1.75,-2.35,"Bumi",fontsize=8.5)
arr(ax,(-0.3,0.15),(-0.3,1.15)); ax.text(-1.9,0.75,"meja pada buku",fontsize=7.8,ha="center")
arr(ax,(-0.3,-0.5),(-0.3,-1.45),c=G); ax.text(-1.9,-1.0,"buku pada meja",fontsize=7.8,ha="center",color="0.3")
arr(ax,(0.3,0.15),(0.3,1.15+0.0) if False else (0.3,-0.25+0.0),lw=0.01,ms=0.1)
arr(ax,(0.35,-0.5),(0.35,-1.15)); ax.text(2.1,-0.85,"Bumi pada buku\n(digambar di bawah meja)",fontsize=7.4,ha="center")
arr(ax,(0.35,-1.9),(0.35,-1.3),c=G); ax.text(2.1,-1.65,"buku pada Bumi",fontsize=7.8,ha="center",color="0.3")
ax.text(0,2.0,"(b) dua pasangan aksi–reaksi:\ntiap pasangan bekerja pada DUA benda berbeda",ha="center",fontsize=8)
save(fig,"fig04_pasangan.png")

# 5 lift tiga keadaan
fig,axs=plt.subplots(1,3,figsize=(6.8,2.9))
for ax,(ttl,n,acc) in zip(axs,[("mempercepat ke atas\n$n>mg$",1.9,1),("kecepatan tetap\n$n=mg$",1.4,0),("mempercepat ke bawah\n$n<mg$",0.9,-1)]):
    cl(ax,(-1.5,1.8),(-2.3,2.6)); ax.add_patch(Rectangle((-0.9,-0.4),1.8,2.3,fc="none",ec=K,lw=1.0)); ax.add_patch(Circle((0,0.6),0.09,fc=K))
    arr(ax,(0,0.6),(0,0.6+n)); ax.text(0.28,0.6+n-0.15,r"$\vec n$"); arr(ax,(0,0.6),(0,0.6-1.4)); ax.text(0.4,-0.65,r"$m\vec g$")
    if acc: arr(ax,(1.35,0.6-0.5*acc),(1.35,0.6+0.5*acc),lw=2.0,c=G); ax.text(1.5,0.5,r"$\vec a$",color="0.3")
    ax.text(0,-1.6,ttl,ha="center",va="top",fontsize=8.5)
save(fig,"fig05_lift.png")

# 6 lampu dua tali
fig,axs=plt.subplots(1,2,figsize=(6.6,2.8))
ax=axs[0]; cl(ax,(-2.6,2.2),(-1.4,1.9)); tanah(ax,-2.5,2.1,1.6)
a1,a2=np.radians(37),np.radians(53); P=(0,0); L1=1.6/np.sin(a1); L2=1.6/np.sin(a2)
ax.plot([0,-L1*np.cos(a1)],[0,1.6],c=K,lw=1.1); ax.plot([0,L2*np.cos(a2)],[0,1.6],c=K,lw=1.1); ax.plot([0,0],[0,-0.5],c=K,lw=1.1); ax.add_patch(Circle((0,-0.75),0.25,fc=L,ec=K))
ax.text(-1.55,1.3,"37°",fontsize=8.5); ax.text(0.72,1.3,"53°",fontsize=8.5); ax.text(0.35,-0.85,"5,0 kg",fontsize=8.5)
ax=axs[1]; cl(ax,(-2.2,2.2),(-1.9,1.7)); ax.plot([-2,2],[0,0],c=G,lw=0.5); ax.plot([0,0],[-1.8,1.6],c=G,lw=0.5)
fbd(ax,(0,0),[(-1.2*np.cos(a1),1.2*np.sin(a1),r"$\vec T_1$",(-0.2,0.15)),(1.6*np.cos(a2),1.6*np.sin(a2),r"$\vec T_2$",(0.2,0.15)),(0,-1.6,r"$m\vec g$",(0.35,0.1))])
ax.text(-0.75,0.12,"37°",fontsize=8); ax.text(0.45,0.12,"53°",fontsize=8); ax.text(0,-2.0+0.2,"diagram benda bebas simpul",ha="center",fontsize=8) if False else None
save(fig,"fig06_lampu.png")

# 7 bidang miring
fig,ax=plt.subplots(figsize=(5.2,3.0)); cl(ax,(-0.4,6.2),(-1.9,3.4))
th=np.radians(30); ax.add_patch(Polygon([(0,0),(5.2,0),(5.2,5.2*np.tan(th))],fc="0.95",ec=K,lw=1.1)); ax.add_patch(Arc((0,0),1.8,1.8,theta1=0,theta2=30,lw=0.8)); ax.text(1.05,0.2,r"$\theta$")
c=np.array([2.8,2.8*np.tan(th)]); n=np.array([-np.sin(th),np.cos(th)]); t=np.array([np.cos(th),np.sin(th)]); o=c+n*0.35
ax.add_patch(Polygon([c-t*0.5,c+t*0.5,c+t*0.5+n*0.7,c-t*0.5+n*0.7],fc=L,ec=K,lw=1.1))
arr(ax,o,o+n*1.5); ax.text(*(o+n*1.7),r"$\vec n$",ha="center"); arr(ax,o,o+np.array([0,-1.6])); ax.text(o[0]+0.15,o[1]-1.75,r"$m\vec g$")
arr(ax,o,o-t*0.8,lw=1.1,c=G); arr(ax,o,o-n*1.386,lw=1.1,c=G); ax.plot([o[0]-t[0]*0.8,o[0]],[o[1]-t[1]*0.8,o[1]-1.6],c=G,lw=0.5,ls=":"); ax.plot([o[0]-n[0]*1.386,o[0]],[o[1]-n[1]*1.386,o[1]-1.6],c=G,lw=0.5,ls=":")
ax.text(o[0]-1.55,o[1]-0.2,r"$mg\sin\theta$",fontsize=8.5,color="0.3",ha="center"); ax.text(o[0]+0.95,o[1]-0.85,r"$mg\cos\theta$",fontsize=8.5,color="0.3")
arr(ax,(4.6,3.0),(4.6-t[0]*0.8,3.0-t[1]*0.8),lw=0.8,ms=7); arr(ax,(4.6,3.0),(4.6+n[0]*0.8,3.0+n[1]*0.8),lw=0.8,ms=7); ax.text(3.75,2.45,"$x$",fontsize=9); ax.text(4.1,3.75,"$y$",fontsize=9)
save(fig,"fig07_miring.png")

# 8 Atwood dan meja-gantung
fig,axs=plt.subplots(1,2,figsize=(6.6,3.2))
ax=axs[0]; cl(ax,(-1.8,1.8),(-0.6,3.6)); tanah(ax,-0.8,0.8,3.4); ax.plot([0,0],[3.4,3.0],c=K,lw=1); ax.add_patch(Circle((0,2.75),0.3,fc="white",ec=K,lw=1.2))
ax.plot([-0.3,-0.3],[2.75,1.6],c=K,lw=1); ax.plot([0.3,0.3],[2.75,0.9],c=K,lw=1)
ax.add_patch(Rectangle((-0.6,1.1),0.6,0.5,fc=L,ec=K)); ax.text(-0.3,1.3,"$m_1$",ha="center",fontsize=8.5); ax.add_patch(Rectangle((-0.05,0.2),0.7,0.7,fc=L,ec=K)); ax.text(0.3,0.5,"$m_2$",ha="center",fontsize=8.5)
arr(ax,(-1.1,1.1),(-1.1,1.8),lw=1.6,c=G); ax.text(-1.45,1.4,r"$a$",color="0.3"); arr(ax,(1.1,0.9),(1.1,0.2),lw=1.6,c=G); ax.text(1.25,0.5,r"$a$",color="0.3")
ax.text(-0.75,2.2,r"$T$",fontsize=9); ax.text(0.45,2.0,r"$T$",fontsize=9); ax.set_title("(a) mesin Atwood",fontsize=9)
ax=axs[1]; cl(ax,(-0.4,4.6),(-0.6,3.6)); ax.add_patch(Rectangle((0,1.9),3.2,0.2,fc=L,ec=K)); ax.plot([3.0,3.0],[1.9,0],c=K,lw=1)
ax.add_patch(Rectangle((0.8,2.1),0.9,0.6,fc="white",ec=K,lw=1.2)); ax.text(1.25,2.3,"$M$",ha="center",fontsize=9); ax.add_patch(Circle((3.35,2.4),0.25,fc="white",ec=K,lw=1.2)); ax.plot([3.2,3.3],[2.1,2.2],c=K,lw=1)
ax.plot([1.7,3.35],[2.65,2.65],c=K,lw=1); ax.plot([3.6,3.6],[2.4,1.1],c=K,lw=1); ax.add_patch(Rectangle((3.3,0.5),0.6,0.6,fc=L,ec=K)); ax.text(3.6,0.72,"$m$",ha="center",fontsize=9)
arr(ax,(1.0,3.1),(1.8,3.1),lw=1.6,c=G); ax.text(1.3,3.25,"$a$",color="0.3"); arr(ax,(4.2,1.1),(4.2,0.4),lw=1.6,c=G); ax.text(4.3,0.7,"$a$",color="0.3"); ax.text(2.4,2.75,"$T$",fontsize=9); ax.text(3.7,1.6,"$T$",fontsize=9)
ax.set_title("(b) balok di meja licin dan beban gantung",fontsize=9)
save(fig,"fig08_atwood.png")

# 9 dua balok bersentuhan
fig,ax=plt.subplots(figsize=(6.4,2.3)); cl(ax,(-1.6,8.6),(-0.9,1.9)); tanah(ax,-1.4,3.4)
ax.add_patch(Rectangle((0,0),1.0,0.8,fc=L,ec=K)); ax.text(0.5,0.3,"3 kg",ha="center",fontsize=8.5); ax.add_patch(Rectangle((1.0,0),1.5,1.1,fc="white",ec=K)); ax.text(1.75,0.45,"5 kg",ha="center",fontsize=8.5)
arr(ax,(-1.2,0.4),(0,0.4),lw=2.0); ax.text(-0.7,0.6,"$F$",fontsize=10)
ax.text(1.0,1.5,"(a) keadaan",ha="center",fontsize=8.5)
for x0,w,lab,fs in [(4.6,1.0,"3 kg",[(-1.0,0,"$F$",1),(0.8,0,"$n_{21}$",-1)]),(7.0,1.2,"5 kg",[(-0.8,0,"$n_{12}$",1),])]:
    ax.add_patch(Rectangle((x0,0),w,0.8,fc=L if lab=="3 kg" else "white",ec=K)); ax.text(x0+w/2,0.3,lab,ha="center",fontsize=8.5)
arr(ax,(3.6,0.4),(4.6,0.4),lw=1.8); ax.text(4.0,0.6,"$F$",fontsize=9); arr(ax,(6.3,0.55),(5.6,0.55),lw=1.8); ax.text(6.05,0.75,"$n_{21}$",fontsize=9)
arr(ax,(6.3,0.25),(7.0,0.25),lw=1.8); ax.text(6.55,-0.15,"$n_{12}$",fontsize=9)
ax.text(6.0,1.5,"(b) gaya mendatar pada tiap balok",ha="center",fontsize=8.5)
save(fig,"fig09_kontak.png")

# 10 kuda gerobak
fig,ax=plt.subplots(figsize=(6.6,2.4)); cl(ax,(-0.5,9.5),(-1.0,2.0)); tanah(ax,-0.4,9.4)
ax.add_patch(Rectangle((0.8,0.35),2.2,0.9,fc=L,ec=K)); ax.add_patch(Circle((1.3,0.2),0.2,fc="white",ec=K)); ax.add_patch(Circle((2.5,0.2),0.2,fc="white",ec=K)); ax.text(1.9,0.7,"gerobak",ha="center",fontsize=8.5)
ax.add_patch(Rectangle((5.6,0.5),1.9,0.8,fc="white",ec=K)); ax.plot([5.9,5.9],[0.5,0],c=K,lw=1.5); ax.plot([7.2,7.2],[0.5,0],c=K,lw=1.5); ax.text(6.55,0.8,"kuda",ha="center",fontsize=8.5)
ax.plot([3.0,5.6],[0.85,0.85],c=K,lw=0.8)
arr(ax,(3.0,1.05),(4.1,1.05),lw=1.8); ax.text(3.5,1.3,"kuda pada\ngerobak",fontsize=7.5,ha="center")
arr(ax,(5.6,1.05),(4.5,1.05),lw=1.8,c=G); ax.text(5.1,1.3,"gerobak\npada kuda",fontsize=7.5,ha="center",color="0.3")
arr(ax,(6.55,-0.35),(8.3,-0.35),lw=2.2); ax.text(7.4,-0.75,"tanah pada kuda (ke depan)",fontsize=7.8,ha="center")
arr(ax,(2.2,-0.35),(1.4,-0.35),lw=1.2); ax.text(1.8,-0.75,"hambatan pada gerobak",fontsize=7.8,ha="center")
save(fig,"fig10_kuda.png")
print("ok5")
