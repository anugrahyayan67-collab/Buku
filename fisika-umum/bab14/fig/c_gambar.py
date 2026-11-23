import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch as FA
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family':'Liberation Sans','font.size':10,'mathtext.fontset':'dejavusans','text.color':'#17355e','axes.edgecolor':'#17355e'})
B='#1b75bc'; T='#17355e'; H='#b5541c'; W='#cfe3f5'; G='#1a8a6a'
KOMA=FuncFormatter(lambda x,p:('%g'%x).replace('.',','))
def sv(f,n): f.savefig(n,dpi=220,bbox_inches='tight'); plt.close(f)
def ar(ax,a,b,c='k',lw=1.8,ms=12): ax.add_patch(FA(a,b,arrowstyle='-|>',mutation_scale=ms,color=c,lw=lw,shrinkA=0,shrinkB=0))
f,axs=plt.subplots(1,2,figsize=(6.6,2.9),gridspec_kw={'width_ratios':[1,1.3]})
ax=axs[0]; ax.set_aspect('equal'); ax.axis('off')
ar(ax,(0,0),(1.6,0),B); ax.text(0.8,-0.25,'$V_R$',color=B,ha='center')
ar(ax,(0,0),(0,1.9),G); ax.text(-0.3,1.6,'$V_L$',color=G); ar(ax,(0,0),(0,-1.2),H); ax.text(-0.35,-1.1,'$V_C$',color=H)
ar(ax,(0,0),(1.6,0.7),T,2.2); ax.text(1.65,0.75,'$V$',fontsize=11); ax.plot([1.6,1.6],[0,0.7],color='#999',ls=':',lw=.8); ax.text(0.45,0.08,r'$\phi$',fontsize=9)
ax.text(0.2,-1.6,'arus sefase dengan $V_R$',fontsize=8); ax.set_xlim(-0.7,2.3); ax.set_ylim(-1.8,2.1); ax.set_title('diagram fasor',fontsize=9)
ax=axs[1]; fr=np.linspace(20,120,400); L=.5;C=10e-6
for R,col in [(30,H),(100,B)]:
    Z=np.sqrt(R**2+(2*np.pi*fr*L-1/(2*np.pi*fr*C))**2); ax.plot(fr,220/Z,color=col,lw=2,label=f'$R$ = {R} Ω')
ax.set_xlabel('frekuensi (Hz)'); ax.set_ylabel('arus rms (A)'); ax.legend(frameon=False,fontsize=8.5); ax.yaxis.set_major_formatter(KOMA)
for s in ['top','right']: ax.spines[s].set_visible(False)
ax.set_title('resonansi rangkaian RLC',fontsize=9); sv(f,'c_ac.png')
# NMR etanol
f,ax=plt.subplots(figsize=(6.0,2.6)); x=np.linspace(0.6,4.2,4000)
def lor(x0,a,w=0.0025): return a*w**2/((x-x0)**2+w**2)
J=7/400; y=np.zeros_like(x)
for k,a in enumerate([1,2,1]): y+=lor(1.2+(k-1)*J,a*1.0)
for k,a in enumerate([1,3,3,1]): y+=lor(3.7+(k-1.5)*J,a*0.6667)
y+=lor(2.6,1.0,0.01)*1.0
ax.plot(x,y,color=B,lw=1.2); ax.set_xlim(4.2,0.6); ax.set_yticks([]); ax.set_xlabel(r'geseran kimia $\delta$ (ppm)'); ax.xaxis.set_major_formatter(KOMA)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.text(3.7,2.2,'CH$_2$\nkuartet (2 H)',ha='center',fontsize=8.5); ax.text(1.2,2.2,'CH$_3$\ntriplet (3 H)',ha='center',fontsize=8.5); ax.text(2.6,1.15,'OH (1 H)',ha='center',fontsize=8.5)
ax.set_ylim(0,2.8); sv(f,'c_nmr.png')
