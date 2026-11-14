import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle, Arc, Polygon
plt.rcParams.update({"font.family":"Liberation Sans","font.size":9.5,"mathtext.fontset":"dejavusans","axes.linewidth":0.8})
K="black"; G="0.55"; L="0.85"
def save(fig,n): fig.savefig(n,dpi=220,bbox_inches="tight",facecolor="white"); plt.close(fig)
def arr(ax,p,q,lw=1.6,c=K,ms=11,ls="-"): ax.add_patch(FancyArrowPatch(p,q,arrowstyle="-|>",mutation_scale=ms,lw=lw,color=c,linestyle=ls,shrinkA=0,shrinkB=0))
def cl(ax,xl,yl): ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(*xl); ax.set_ylim(*yl)
V=lambda s: r"$\vec{%s}$"%s

# 1 penjumlahan
fig,axs=plt.subplots(1,3,figsize=(7.2,2.4))
ax=axs[0]; cl(ax,(-0.4,4.6),(-0.5,3.3)); arr(ax,(0,0),(3,0.6)); arr(ax,(3,0.6),(4,2.8)); arr(ax,(0,0),(4,2.8),lw=2.2,c=G)
ax.text(1.5,-0.1,V("A")); ax.text(3.75,1.5,V("B")); ax.text(1.5,1.6,V("A")+"$+$"+V("B")); ax.set_title("(a) ujung ke pangkal",fontsize=9)
ax=axs[1]; cl(ax,(-0.4,4.6),(-0.5,3.3)); arr(ax,(0,0),(1,2.2)); arr(ax,(1,2.2),(4,2.8)); arr(ax,(0,0),(4,2.8),lw=2.2,c=G)
ax.text(0.05,1.2,V("B")); ax.text(2.2,2.75,V("A")); ax.text(2.2,1.0,V("B")+"$+$"+V("A")); ax.set_title("(b) urutan dibalik: hasil sama",fontsize=9)
ax=axs[2]; cl(ax,(-0.4,4.6),(-0.5,3.3)); arr(ax,(0,0),(3,0.6)); arr(ax,(0,0),(1,2.2)); ax.plot([3,4],[0.6,2.8],c=K,lw=0.7,ls="--"); ax.plot([1,4],[2.2,2.8],c=K,lw=0.7,ls="--"); arr(ax,(0,0),(4,2.8),lw=2.2,c=G)
ax.text(1.5,-0.1,V("A")); ax.text(0.05,1.2,V("B")); ax.set_title("(c) jajargenjang",fontsize=9)
save(fig,"fig01_jumlah.png")

# 2 pengurangan dan skalar
fig,axs=plt.subplots(1,2,figsize=(6.6,2.3))
ax=axs[0]; cl(ax,(-1.6,4.4),(-2.6,1.4)); arr(ax,(0,0),(3,0.6)); arr(ax,(3,0.6),(2,-1.6)); arr(ax,(0,0),(2,-1.6),lw=2.2,c=G); arr(ax,(3.3,0.6),(4.3,2.8-1.5+0.9-0.9),lw=0.9,ls="--")
ax.text(1.4,0.5,V("A")); ax.text(2.7,-0.7,"$-$"+V("B")); ax.text(0.1,-1.3,V("A")+"$-$"+V("B")); ax.text(4.0,0.9,V("B"),color="0.3"); ax.set_title(r"(a) $\vec A-\vec B=\vec A+(-\vec B)$",fontsize=9)
ax=axs[1]; cl(ax,(-3.2,4.6),(-1.2,1.6)); arr(ax,(0,1),(1.5,1)); ax.text(0.6,1.15,V("A")); arr(ax,(0,0.2),(3,0.2)); ax.text(1.3,0.35,"$2$"+V("A")); arr(ax,(0,-0.6),(-2.25,-0.6)); ax.text(-1.5,-0.45,"$-1{,}5$"+V("A")); ax.set_title("(b) perkalian dengan skalar",fontsize=9)
save(fig,"fig02_kurang.png")

# 3 komponen
fig,ax=plt.subplots(figsize=(4.4,3.0)); cl(ax,(-0.6,5.2),(-0.7,3.6))
arr(ax,(-0.4,0),(5,0),lw=0.8,ms=8); arr(ax,(0,-0.4),(0,3.4),lw=0.8,ms=8); ax.text(5.05,-0.1,"$x$"); ax.text(-0.1,3.45,"$y$",ha="right")
a=np.radians(35); A=4.6; P=(A*np.cos(a),A*np.sin(a)); arr(ax,(0,0),P,lw=2.2)
arr(ax,(0,0),(P[0],0),lw=1.3,c=G); arr(ax,(P[0],0),P,lw=1.3,c=G)
ax.text(P[0]/2-0.3,P[1]/2+0.35,V("A"),fontsize=11); ax.text(P[0]/2,-0.45,r"$A_x=A\cos\theta$",ha="center"); ax.text(P[0]+0.1,P[1]/2,r"$A_y=A\sin\theta$")
ax.add_patch(Arc((0,0),1.5,1.5,theta1=0,theta2=35,lw=0.8)); ax.text(0.95,0.2,r"$\theta$")
ax.set_xlim(-0.6,6.6)
save(fig,"fig03_komponen.png")

# 4 kuadran
fig,ax=plt.subplots(figsize=(4.2,3.4)); cl(ax,(-4.6,4.6),(-3.6,3.9))
arr(ax,(-4.4,0),(4.4,0),lw=0.8,ms=8); arr(ax,(0,-3.4),(0,3.6),lw=0.8,ms=8); ax.text(4.45,-0.1,"$x$"); ax.text(0.1,3.6,"$y$")
arr(ax,(0,0),(-3,4*0.75*1.0),lw=2.0); arr(ax,(0,0),(3,-3),lw=1.2,ls="--",c=G)
ax.text(-3.3,3.1,r"$\vec A=(-3;\,4)$",fontsize=9); ax.text(1.4,-2.9,"arah yang diberikan\nkalkulator: $-53{,}1^\\circ$",fontsize=7.8)
ax.add_patch(Arc((0,0),1.6,1.6,theta1=0,theta2=126.87,lw=0.8)); ax.text(0.5,0.9,r"$126{,}9^\circ$",fontsize=8.5)
for (x,y,s) in [(2.6,2.4,"I\n$(+,+)$"),(-3.0,1.2,"II\n$(-,+)$"),(-2.8,-2.3,"III\n$(-,-)$"),(3.2,-1.2,"IV\n$(+,-)$")]: ax.text(x,y,s,ha="center",fontsize=8,color="0.35")
save(fig,"fig04_kuadran.png")

# 5 pendaki
fig,ax=plt.subplots(figsize=(3.6,4.0)); cl(ax,(-1.0,2.6),(-0.5,4.4))
arr(ax,(-0.8,0),(2.4,0),lw=0.7,ms=7); arr(ax,(0,-0.3),(0,4.3),lw=0.7,ms=7); ax.text(2.4,-0.25,"timur",fontsize=8); ax.text(0.08,4.2,"utara",fontsize=8)
A=np.array([1.732,1.0]); B=A+np.array([0,3.0]); C=B+np.array([-1.061,-1.061])
arr(ax,(0,0),A); arr(ax,A,B); arr(ax,B,C); arr(ax,(0,0),C,lw=2.2,c=G)
ax.text(0.9,0.25,V("A")); ax.text(1.85,2.4,V("B")); ax.text(1.3,3.65,V("C")); ax.text(0.0,1.8,V("R"),fontsize=11)
save(fig,"fig05_pendaki.png")

# 6 titik (proyeksi)
fig,ax=plt.subplots(figsize=(4.4,2.4)); cl(ax,(-0.4,5.2),(-0.7,2.8))
arr(ax,(0,0),(4.8,0),lw=1.8); a=np.radians(40); A=3.4; P=(A*np.cos(a),A*np.sin(a)); arr(ax,(0,0),P,lw=1.8)
ax.plot([P[0],P[0]],[0,P[1]],c=K,lw=0.7,ls="--"); ax.plot([0,P[0]],[-0.25,-0.25],c=G,lw=2.5)
ax.text(P[0]/2,-0.6,r"$A\cos\theta$ (bayangan $\vec A$ pada $\vec B$)",ha="center",fontsize=8.5); ax.text(1.0,1.3,V("A"),fontsize=11); ax.text(4.5,0.15,V("B"),fontsize=11)
ax.add_patch(Arc((0,0),1.4,1.4,theta1=0,theta2=40,lw=0.8)); ax.text(0.85,0.22,r"$\theta$")
save(fig,"fig06_titik.png")

# 7 silang
fig,ax=plt.subplots(figsize=(4.6,2.6)); cl(ax,(-0.5,6.2),(-0.5,2.8))
A=np.array([3.6,0.0]); B=np.array([1.6,2.0])
ax.add_patch(Polygon([(0,0),A,A+B,B],fc=L,ec=K,lw=0.6,ls="--")); arr(ax,(0,0),A,lw=1.8); arr(ax,(0,0),B,lw=1.8)
ax.text(1.8,-0.35,V("A"),fontsize=11); ax.text(0.45,1.2,V("B"),fontsize=11); ax.text(2.6,1.0,r"luas $=AB\sin\theta$",ha="center",fontsize=8.5)
ax.add_patch(Arc((0,0),1.3,1.3,theta1=0,theta2=51.3,lw=0.8)); ax.text(0.75,0.25,r"$\theta$")
ax.add_patch(Circle((5.6,2.0),0.22,fc="white",ec=K,lw=1.2)); ax.add_patch(Circle((5.6,2.0),0.05,fc=K)); ax.text(5.6,1.45,r"$\vec A\times\vec B$"+"\nkeluar bidang",ha="center",va="top",fontsize=8)
save(fig,"fig07_silang.png")

# 8 tetrahedral
fig,ax=plt.subplots(figsize=(3.4,3.4)); cl(ax,(-1.9,2.1),(-1.9,2.1))
def pr(p): x,y,z=p; return np.array([x-0.45*y, z-0.3*y])
cube=[(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]
for i,j in [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]:
    p,q=pr(cube[i]),pr(cube[j]); ax.plot([p[0],q[0]],[p[1],q[1]],c=G,lw=0.6,ls=":")
H=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
for h in H:
    q=pr(h); ax.plot([0,q[0]],[0,q[1]],c=K,lw=1.6); ax.add_patch(Circle(q,0.13,fc="white",ec=K,lw=1.0,zorder=3))
ax.add_patch(Circle((0,0),0.2,fc=G,ec=K,zorder=4)); ax.text(0.25,-0.12,"C",fontsize=9); ax.text(pr(H[0])[0]+0.18,pr(H[0])[1],"H",fontsize=9)
save(fig,"fig08_tetrahedral.png")
print("ok3")
