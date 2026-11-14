import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch as FA
plt.rcParams.update({'font.family':'Liberation Sans','font.size':10,'mathtext.fontset':'dejavusans','text.color':'#17355e'})
B='#1b75bc'; T='#17355e'; H='#b5541c'; W='#cfe3f5'
def sv(f,n): f.savefig(n,dpi=220,bbox_inches='tight'); plt.close(f)
# meriam Newton
f,ax=plt.subplots(figsize=(4.4,4.0)); ax.set_aspect('equal'); ax.axis('off')
ax.add_patch(Circle((0,0),1,fc=W,ec=T,lw=1.2)); ax.plot([0,0],[1,1.12],color=T,lw=2)
x0,y0=0,1.12
for v,c,l in [(0.55,'#9aa',''),(0.75,'#9aa',''),(0.9,'#7a9',''),(1/np.sqrt(1.12),B,'orbit lingkaran'),(1.05,H,'orbit elips')]:
    r=np.array([x0,y0],float); vv=np.array([v,0.]); pts=[r.copy()]
    for _ in range(8000):
        a=-r/np.linalg.norm(r)**3; vv+=a*0.002; r+=vv*0.002; pts.append(r.copy())
        if np.linalg.norm(r)<1: break
        if len(pts)>400 and np.linalg.norm(r-np.array([x0,y0]))<0.01: break
    P=np.array(pts); ax.plot(P[:,0],P[:,1],color=c,lw=1.5 if l else 1)
ax.text(0.05,1.2,'puncak gunung',fontsize=8.5); ax.text(-0.18,-0.05,'Bumi',fontsize=9)
ax.text(1.32,-0.15,'orbit\nlingkaran',fontsize=8.5,color=B,bbox=dict(fc='white',ec='none',pad=1)); ax.text(-1.68,-1.75,'orbit elips',fontsize=8.5,color=H)
ax.set_xlim(-1.7,2.0); ax.set_ylim(-2.0,1.45); sv(f,'c_orbit.png')
