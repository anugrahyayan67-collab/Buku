import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'Liberation Sans','font.size':10,'mathtext.fontset':'dejavusans','text.color':'#17355e','axes.edgecolor':'#17355e'})
B='#1b75bc'; T='#17355e'; H='#b5541c'; W='#cfe3f5'; G='#1a8a6a'
def sv(f,n): f.savefig(n,dpi=220,bbox_inches='tight'); plt.close(f)
from matplotlib.ticker import FuncFormatter
KOMA=FuncFormatter(lambda x,p:('%g'%x).replace('.',','))
def sp(ax):
    ax.xaxis.set_major_formatter(KOMA); ax.yaxis.set_major_formatter(KOMA)
    for s in ['top','right']: ax.spines[s].set_visible(False)
# 1 kurva potensial & parabola
f,ax=plt.subplots(figsize=(4.4,3.0)); sp(ax)
r=np.linspace(0.85,3.0,400); D=1; a=2.2; U=D*(1-np.exp(-a*(r-1.2)))**2-D
ax.plot(r,U,color=B,lw=2,label='energi potensial sebenarnya'); ax.plot(r,-D+D*a*a*(r-1.2)**2,color=H,lw=1.6,ls='--',label='hampiran parabola')
ax.set_ylim(-1.25,0.6); ax.set_xlabel('jarak $r$'); ax.set_ylabel('$U$'); ax.set_xticks([]); ax.set_yticks([]); ax.axhline(0,color='gray',lw=.6)
ax.text(1.2,-1.12,'$r_0$',ha='center',va='top'); ax.legend(frameon=False,fontsize=8.5,loc='upper right'); sv(f,'c_parabola.png')
# 2 deret Fourier gelombang kotak
f,axs=plt.subplots(1,2,figsize=(6.6,2.6),gridspec_kw={'width_ratios':[1.6,1]})
t=np.linspace(0,2,1000); sq=np.sign(np.sin(2*np.pi*t)); ax=axs[0]; sp(ax)
ax.plot(t,sq,color='#999',lw=1)
for n,col in [(1,G),(3,B),(15,H)]:
    s=sum(4/(np.pi*k)*np.sin(2*np.pi*k*t) for k in range(1,n+1,2)); ax.plot(t,s,color=col,lw=1.4,label=f'sampai harmonik ke-{n}')
ax.legend(frameon=False,fontsize=7.5,loc='lower center',ncol=2); ax.set_xlabel('waktu (periode)'); ax.set_yticks([]); ax.set_ylim(-2.5,1.5)
ax=axs[1]; sp(ax); k=np.arange(1,12,2); ax.bar(k,4/(np.pi*k),color=B,width=.6); ax.set_xlabel('harmonik ke-'); ax.set_ylabel('amplitudo'); ax.set_xticks(k)
sv(f,'c_fourier.png')
