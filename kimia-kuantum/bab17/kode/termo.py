import numpy as np
h=6.62607015e-34; kB=1.380649e-23; NA=6.02214076e23; c=2.99792458e10; R=8.314462618; amu=1.66053906660e-27
def termo(masses, xyz_ang, freqs, sigma, T=298.15, P=1e5, scale=1.0):
    m=np.array(masses); x=np.array(xyz_ang)*1e-10; M=m.sum()*amu
    com=(m[:,None]*x).sum(0)/m.sum(); xc=x-com
    It=sum(mi*amu*(np.dot(r,r)*np.eye(3)-np.outer(r,r)) for mi,r in zip(m,xc)); Ip=np.linalg.eigvalsh(It)
    nu=np.array(freqs)*scale*c; th=h*nu/kB
    zpe=0.5*np.sum(h*nu)*NA
    Evib=R*np.sum(th/(np.exp(th/T)-1)); Svib=R*np.sum((th/T)/(np.exp(th/T)-1)-np.log(1-np.exp(-th/T))); Cvib=R*np.sum((th/T)**2*np.exp(th/T)/(np.exp(th/T)-1)**2)
    qt=(2*np.pi*M*kB*T/h**2)**1.5*kB*T/P; St=R*(np.log(qt)+2.5)
    thr=h**2/(8*np.pi**2*Ip*kB); qr=np.sqrt(np.pi)/sigma*T**1.5/np.sqrt(np.prod(thr)); Sr=R*(np.log(qr)+1.5)
    Hcorr=zpe+Evib+1.5*R*T+1.5*R*T+R*T  # trans + rot + PV
    S=St+Sr+Svib
    return dict(ZPE=zpe/1000, Evib=Evib/1000, H0_298=(Evib+4*R*T)/1000, Hcorr=Hcorr/1000, St=St, Sr=Sr, Svib=Svib, S=S, Cv=1.5*R+1.5*R+Cvib, Cp=4*R+Cvib, I=Ip/amu/1e-20, Gcorr=(Hcorr-T*S)/1000, thr=thr)
if __name__=='__main__':
    R0=0.9572; th=np.radians(104.52)/2
    xyz=[(0,0,0),(0,R0*np.sin(th),R0*np.cos(th)),(0,-R0*np.sin(th),R0*np.cos(th))]
    m=[15.99491462,1.00782503,1.00782503]
    d=termo(m,xyz,[1648.5,3832.2,3942.5],2); print('exp harmonic',{k:np.round(v,3) for k,v in d.items()})
    R1=0.9894093; th1=np.radians(100.02687)/2
    xyz1=[(0,0,0),(0,R1*np.sin(th1),R1*np.cos(th1)),(0,-R1*np.sin(th1),R1*np.cos(th1))]
    d=termo(m,xyz1,[2179.6,4145.4,4393.6],2); print('STO',{k:np.round(v,3) for k,v in d.items()})
