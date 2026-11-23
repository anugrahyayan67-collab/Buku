import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.ticker as mt
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle, Arc, Polygon
plt.rcParams.update({"font.family":"Liberation Sans","font.size":9.5,"mathtext.fontset":"dejavusans","axes.linewidth":0.8})
K="black"; G="0.55"; L="0.85"; g=9.8
def save(fig,n): fig.savefig(n,dpi=220,bbox_inches="tight",facecolor="white"); plt.close(fig)
def arr(ax,p,q,lw=1.5,c=K,ms=10,ls="-"): ax.add_patch(FancyArrowPatch(p,q,arrowstyle="-|>",mutation_scale=ms,lw=lw,color=c,linestyle=ls,shrinkA=0,shrinkB=0))
def cl(ax,xl,yl): ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(*xl); ax.set_ylim(*yl)
def sp(ax):
    for s in ["top","right"]: ax.spines[s].set_visible(False)
V=lambda s: r"$\vec{%s}$"%s

# 1 r, delta r, v
fig,ax=plt.subplots(figsize=(4.6,3.0)); cl(ax,(-0.5,5.6),(-0.5,3.8))
arr(ax,(-0.3,0),(5.4,0),lw=0.7,ms=7); arr(ax,(0,-0.3),(0,3.6),lw=0.7,ms=7); ax.text(5.4,-0.3,"$x$"); ax.text(-0.3,3.5,"$y$")
t=np.linspace(0.3,2.6,100); X=1.9*t; Y=0.6+2.4*t-0.75*t**2; ax.plot(X,Y,c=G,lw=1.2,ls="--")
P1=(1.9*0.7,0.6+2.4*0.7-0.75*0.49); P2=(1.9*1.9,0.6+2.4*1.9-0.75*3.61)
arr(ax,(0,0),P1); arr(ax,(0,0),P2); arr(ax,P1,P2,lw=2.0)
ax.text(0.35,1.05,r"$\vec r_1$"); ax.text(2.2,0.95,r"$\vec r_2$"); ax.text(2.2,2.75,r"$\Delta\vec r$")
vt=np.array([1.9,2.4-1.5*0.7]); vt=vt/np.linalg.norm(vt)*1.3; arr(ax,P1,(P1[0]+vt[0],P1[1]+vt[1]),lw=1.2,c="0.3"); ax.text(P1[0]+0.2,P1[1]+1.25,r"$\vec v$ (menyinggung lintasan)",fontsize=8,color="0.3")
ax.plot(*P1,"o",c=K,ms=4); ax.plot(*P2,"o",c=K,ms=4)
save(fig,"fig01_posisi.png")

# 2 dua bola: dijatuhkan vs dilempar mendatar
fig,ax=plt.subplots(figsize=(4.6,3.6)); ax.axis("off")
ts=np.arange(0,6)*0.09
for t in ts:
    y=-0.5*g*t*t; ax.plot([-0.08,2.5*0.5],[y,y],c=G,lw=0.5,ls=":")
    ax.plot(0,y,"o",c="white",mec=K,ms=8); ax.plot(2.5*t,y,"o",c=L,mec=K,ms=8)
tt=np.linspace(0,0.45,50); ax.plot(2.5*tt,-0.5*g*tt**2,c=K,lw=0.7,ls="--")
ax.text(0,0.09,"dijatuhkan",ha="center",fontsize=8.5); ax.text(0.75,0.09,"dilempar mendatar",ha="center",fontsize=8.5)
ax.text(1.28,-0.5,"pada saat yang sama,\nkeduanya selalu\nsama tinggi",fontsize=8)
ax.set_xlim(-0.2,2.0); ax.set_ylim(-1.05,0.2)
save(fig,"fig02_duabola.png")

# 3 lintasan berbagai sudut
fig,ax=plt.subplots(figsize=(6.0,3.0))
v0=20
for th,ls in [(15,":"),(30,"--"),(45,"-"),(60,"--"),(75,":")]:
    a=np.radians(th); T=2*v0*np.sin(a)/g; t=np.linspace(0,T,100); ax.plot(v0*np.cos(a)*t,v0*np.sin(a)*t-0.5*g*t*t,c=K,lw=1.8 if th==45 else 1.0,ls=ls)
    tm=T/2; ax.text(v0*np.cos(a)*tm,v0*np.sin(a)*tm-0.5*g*tm*tm+0.5,f"{th}°",ha="center",fontsize=8.5)
ax.set_xlabel("$x$ (m)"); ax.set_ylabel("$y$ (m)"); ax.set_aspect("equal"); ax.set_xlim(0,43); ax.set_ylim(0,21.5); sp(ax)
save(fig,"fig03_sudut.png")

# 4 vektor kecepatan sepanjang lintasan
fig,ax=plt.subplots(figsize=(6.2,2.9)); ax.set_aspect("equal"); ax.axis("off")
v0=20; a=np.radians(55); vx=v0*np.cos(a); vy0=v0*np.sin(a); T=2*vy0/g
t=np.linspace(0,T,100); ax.plot(vx*t,vy0*t-0.5*g*t*t,c=G,lw=1.0,ls="--"); ax.plot([-2,vx*T+4],[0,0],c=K,lw=0.8)
s=0.42
for tt in np.linspace(0,T,5):
    x=vx*tt; y=vy0*tt-0.5*g*tt*tt; vy=vy0-g*tt
    ax.plot(x,y,"o",c=K,ms=4); arr(ax,(x,y),(x+vx*s,y),lw=1.1,c="0.4",ms=8)
    if abs(vy)>0.5: arr(ax,(x,y),(x,y+vy*s),lw=1.1,c="0.4",ms=8)
    arr(ax,(x,y),(x+vx*s,y+vy*s),lw=1.8)
ax.text(vx*T/2,vy0**2/(2*g)+1.6,"di titik tertinggi $v_y=0$,\ntetapi $v_x$ tetap",ha="center",fontsize=8)
ax.text(1.0,-2.2,"$v_x$ sama di setiap titik; $v_y$ berkurang $9{,}8$ m/s tiap sekon",fontsize=8)
ax.set_xlim(-3,vx*T+8); ax.set_ylim(-9,vy0**2/(2*g)+5)
save(fig,"fig04_komponen.png")

# 5 monyet
fig,ax=plt.subplots(figsize=(5.2,2.9)); ax.set_aspect("equal"); ax.axis("off")
ax.plot([-1,44],[0,0],c=K,lw=0.8); ax.plot([0,40],[0,15],c=G,lw=0.8,ls=":")
v0=25; D=np.hypot(40,15); vx=v0*40/D; vy=v0*15/D; T=40/vx; t=np.linspace(0,T,60)
ax.plot(vx*t,vy*t-0.5*g*t*t,c=K,lw=1.5); ax.plot([40,40],[15,15-0.5*g*T*T],c=K,lw=1.0,ls="--")
ax.plot(40,15,"o",c="white",mec=K,ms=9); ax.plot(40,15-0.5*g*T*T,"o",c=L,mec=K,ms=9); ax.plot(0,0,"s",c=K,ms=5)
ax.text(20,9.3,"garis bidik",fontsize=8,rotation=20.5,color="0.35"); ax.text(41.2,14.5,"monyet\nsemula",fontsize=8); ax.text(41.2,1.8,"bertemu",fontsize=8)
ax.annotate("",xy=(37.5,15-0.5*g*T*T),xytext=(37.5,15),arrowprops=dict(arrowstyle="<->",lw=0.7)); ax.text(31.5,8,r"$\frac{1}{2}gt^2$",fontsize=10)
ax.text(18,2.0,"lintasan peluru",fontsize=8)
ax.set_xlim(-2,50); ax.set_ylim(-2,18)
save(fig,"fig05_monyet.png")

# 6 melingkar
fig,axs=plt.subplots(1,2,figsize=(6.4,2.9))
ax=axs[0]; cl(ax,(-1.6,1.9),(-1.5,1.7)); th=np.linspace(0,2*np.pi,200); ax.plot(np.cos(th),np.sin(th),c=G,lw=1.0)
a1,a2=np.radians(50),np.radians(95)
for a,lab in [(a1,"1"),(a2,"2")]:
    p=np.array([np.cos(a),np.sin(a)]); ax.plot([0,p[0]],[0,p[1]],c=K,lw=0.8); ax.plot(*p,"o",c=K,ms=4)
    tv=np.array([-np.sin(a),np.cos(a)])*0.8; arr(ax,p,p+tv,lw=1.6); ax.text(*(p+tv+np.array([0.02,0.08])),r"$\vec v_%s$"%lab)
ax.add_patch(Arc((0,0),0.6,0.6,theta1=50,theta2=95,lw=0.8)); ax.text(0.1,0.38,r"$\Delta\theta$",fontsize=8.5); ax.text(0.5,0.25,"$r$")
ax.set_title("(a) kecepatan selalu menyinggung",fontsize=9)
ax=axs[1]; cl(ax,(-1.4,1.2),(-0.5,1.4))
v1=np.array([-np.sin(a1),np.cos(a1)])*1.2; v2=np.array([-np.sin(a2),np.cos(a2)])*1.2; o=np.array([0.6,0.0])
arr(ax,o,o+v1,lw=1.6); arr(ax,o,o+v2,lw=1.6); arr(ax,o+v1,o+v2,lw=2.0,c=G)
ax.text(*(o+v1/2+np.array([0.08,0])),r"$\vec v_1$"); ax.text(*(o+v2/2+np.array([-0.3,-0.1])),r"$\vec v_2$"); ax.text(*(o+(v1+v2)/2+np.array([-0.15,0.42])),r"$\Delta\vec v$")
ax.add_patch(Arc(o,0.7,0.7,theta1=140,theta2=185,lw=0.8)); ax.text(o[0]-0.5,o[1]+0.12,r"$\Delta\theta$",fontsize=8.5)
ax.set_title(r"(b) $\Delta\vec v$ mengarah ke pusat",fontsize=9)
save(fig,"fig06_melingkar.png")

# 7 radial dan tangensial
fig,ax=plt.subplots(figsize=(3.6,3.0)); cl(ax,(-1.5,1.9),(-1.3,1.6)); th=np.linspace(np.radians(-20),np.radians(140),100); ax.plot(np.cos(th),np.sin(th),c=G,lw=1.0)
a=np.radians(55); p=np.array([np.cos(a),np.sin(a)]); ax.plot(*p,"o",c=K,ms=5); ax.plot(0,0,"o",c=K,ms=3); ax.plot([0,p[0]],[0,p[1]],c=K,lw=0.5,ls=":")
ar=-p*0.75; at=np.array([-np.sin(a),np.cos(a)])*0.5
arr(ax,p,p+ar,lw=1.3,c="0.35"); arr(ax,p,p+at,lw=1.3,c="0.35"); arr(ax,p,p+ar+at,lw=2.0)
ax.text(*(p+ar+np.array([0.06,-0.02])),r"$\vec a_r$",fontsize=9); ax.text(*(p+at+np.array([-0.3,0.05])),r"$\vec a_t$",fontsize=9); ax.text(*(p+ar+at+np.array([-0.3,-0.1])),r"$\vec a$",fontsize=11)
ax.text(1.05,0.2,"lintasan",fontsize=8,color="0.4")
save(fig,"fig07_radial.png")

# 8 perahu
fig,axs=plt.subplots(1,2,figsize=(6.6,3.0))
for ax,case in zip(axs,[0,1]):
    cl(ax,(-1.6,3.4),(-0.5,3.5)); ax.plot([-1.6,3.4],[0,0],c=K,lw=1.2); ax.plot([-1.6,3.4],[3,3],c=K,lw=1.2)
    for yy in [0.8,1.6,2.4]: arr(ax,(-1.4,yy),(-0.8,yy),lw=0.6,c=G,ms=6)
    if case==0:
        arr(ax,(0,0),(0,2.5),lw=1.4); arr(ax,(0,2.5),(1.5,2.5),lw=1.4,c="0.4"); arr(ax,(0,0),(1.5,2.5),lw=2.2)
        ax.text(-0.75,1.2,r"$\vec v_{pa}$"); ax.text(0.45,2.65,r"$\vec v_{at}$"); ax.text(1.0,1.1,r"$\vec v_{pt}$"); ax.set_title("(a) haluan lurus: perahu hanyut",fontsize=9)
    else:
        arr(ax,(0,0),(-1.5,2.0),lw=1.4); arr(ax,(-1.5,2.0),(0,2.0),lw=1.4,c="0.4"); arr(ax,(0,0),(0,2.0),lw=2.2)
        ax.text(-1.35,0.9,r"$\vec v_{pa}$"); ax.text(-0.95,2.15,r"$\vec v_{at}$"); ax.text(0.1,1.0,r"$\vec v_{pt}$"); ax.set_title("(b) haluan ke hulu: tiba tepat di seberang",fontsize=9)
    ax.text(2.3,0.5,"arus →",fontsize=8,color="0.4")
save(fig,"fig08_perahu.png")

# 9 hambatan udara
fig,ax=plt.subplots(figsize=(5.6,2.6))
def traj(th,k):
    a=np.radians(th); x=y=0; vx=30*np.cos(a); vy=30*np.sin(a); dt=0.002; X=[0];Y=[0]
    while y>=0:
        v=np.hypot(vx,vy); vx+=-k*v*vx*dt; vy+=(-g-k*v*vy)*dt; x+=vx*dt; y+=vy*dt; X.append(x);Y.append(y)
    return X,Y
X,Y=traj(45,0); ax.plot(X,Y,c=K,lw=1.0,ls="--",label="tanpa udara, 45°")
X,Y=traj(45,0.02); ax.plot(X,Y,c=K,lw=1.8,label="dengan hambatan udara, 45°")
X,Y=traj(38,0.02); ax.plot(X,Y,c=G,lw=1.4,label="dengan hambatan udara, 38°")
ax.set_xlabel("$x$ (m)"); ax.set_ylabel("$y$ (m)"); ax.set_aspect("equal"); ax.legend(frameon=False,fontsize=8); sp(ax); ax.set_ylim(0,34); ax.set_xlim(0,95)
save(fig,"fig09_udara.png")
print("ok4")
