import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'Liberation Sans','font.size':10,'mathtext.fontset':'dejavusans','text.color':'#17355e','axes.edgecolor':'#17355e'})
B='#1b75bc'; T='#17355e'; H='#b5541c'; W='#cfe3f5'; G='#1a8a6a'
def sv(f,n): f.savefig(n,dpi=220,bbox_inches='tight'); plt.close(f)
R=8.314
f,axs=plt.subplots(1,2,figsize=(6.8,3.2))
def diagram(ax,Tt,pt,Hs,Hv,Tc,pc,slope_m,title,lab1,mark):
    T1=np.linspace(Tt-60,Tt,100); ps=pt*np.exp(-Hs/R*(1/T1-1/Tt))
    T2=np.linspace(Tt,Tc,200); pv=pt*np.exp(-Hv/R*(1/T2-1/Tt))
    P3=np.logspace(np.log10(pt),np.log10(pc*4),50); T3=Tt+(P3-pt)/slope_m
    ax.semilogy(T1,ps,color=B,lw=2); ax.semilogy(T2,pv,color=H,lw=2); ax.semilogy(T3,P3,color=G,lw=2)
    ax.plot(Tt,pt,'o',color=T,ms=5); ax.plot(Tc,pv[-1],'o',color=T,ms=5)
    ax.text(Tt+3,pt*0.45,'titik tripel',fontsize=8); ax.text(Tc-30,pv[-1]*2.2,'titik kritis',fontsize=8)
    ax.axhline(101325,color='gray',ls=':',lw=.8); ax.text(Tc-25,101325*1.3,'1 atm',fontsize=7.5,color='gray')
    for (x,y,t) in lab1: ax.text(x,y,t,fontsize=9,fontweight='bold',ha='center')
    ax.set_xlabel('suhu (K)'); ax.set_ylabel('tekanan (Pa)'); ax.set_title(title,fontsize=9.5)
    for s in ['top','right']: ax.spines[s].set_visible(False)
diagram(axs[0],273.16,611.7,51000,45000,647,2.2e7,-1.35e7,'air (skematis)',[(232,1e6,'padat'),(420,3e6,'cair'),(450,300,'gas')],None)
axs[0].set_ylim(10,1e8)
diagram(axs[1],216.6,5.18e5,26000,16000,304.1,7.38e6,2.0e6,'karbon dioksida (skematis)',[(190,3e6,'padat'),(250,1e7,'cair'),(260,2e4,'gas')],None)
axs[1].set_ylim(1e3,1e8)
sv(f,'c_fasa.png')
