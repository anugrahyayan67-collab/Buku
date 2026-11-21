#!/usr/bin/env python3
# Modul Hückel diperluas (parameter Hoffmann) dan PPP-SCF + CIS untuk gambar Bab 13.
# Hückel diperluas (Hoffmann) dengan orbital Slater yang diuraikan ke Gauss
import numpy as np
from math import factorial, sqrt, pi
r=np.linspace(1e-4,25,8000)
al=0.01*2.2**np.arange(16)
def fit(f,w):
    G=np.exp(-np.outer(r**2,al)); sw=np.sqrt(w)
    c,*_=np.linalg.lstsq(G*sw[:,None],f*sw,rcond=None); return c
# radial STO zeta=1 ternormalisasi: R_n = N r^(n-1) e^-r
N1=2.0; N2=(2**2.5)/sqrt(24)
# 1s: R=2e^-r ; Y00 -> psi = 2e^-r/sqrt(4pi) ~ sum c exp(-a r^2)
c1=fit(2*np.exp(-r)/sqrt(4*pi), r**2)
# 2s: R=N2 r e^-r
c2s=fit(N2*r*np.exp(-r)/sqrt(4*pi), r**2)
# 2p: psi = N2 r e^-r sqrt(3/4pi) cos -> x * [N2 e^-r sqrt(3/4pi)] ~ x * sum c exp(-a r^2)
c2p=fit(N2*np.exp(-r)*sqrt(3/(4*pi)), r**4)
PAR={'H':[('1s',-13.6,1.3)],'C':[('2s',-21.4,1.625),('2p',-11.4,1.625)],'N':[('2s',-26.0,1.95),('2p',-13.4,1.95)],
     'O':[('2s',-32.3,2.275),('2p',-14.8,2.275)],'B':[('2s',-15.2,1.3),('2p',-8.5,1.3)],'Be':[('2s',-10.0,0.975),('2p',-6.0,0.975)]}
def basis(atoms):
    bf=[]  # (atom idx, type, H_ii, coefs, exps, center, l, comp)
    for ia,(el,pos) in enumerate(atoms):
        for nm,Hii,z in PAR[el]:
            if nm=='1s': bf.append((ia,'s',Hii,c1*z**1.5,al*z*z,np.array(pos,float),0,None,el+' 1s'))
            elif nm=='2s': bf.append((ia,'s',Hii,c2s*z**1.5,al*z*z,np.array(pos,float),0,None,el+' 2s'))
            else:
                for k,ax in enumerate('xyz'): bf.append((ia,'p',Hii,c2p*z**2.5,al*z*z,np.array(pos,float),1,k,el+' 2p'+ax))
    return bf
def ovl(f,g):
    _,_,_,ca,aa,A,la,ka,_=f; _,_,_,cb,ab,B,lb,kb,_=g
    s=0.0
    for ci,a in zip(ca,aa):
        p=a+ab; mu=a*ab/p; AB=A-B; P=(a*A+ab[:,None]*B)/p[:,None]
        S0=(pi/p)**1.5*np.exp(-mu*(AB@AB))
        if la==0 and lb==0: t=S0
        elif la==1 and lb==0: t=(P[:,ka]-A[ka])*S0
        elif la==0 and lb==1: t=(P[:,kb]-B[kb])*S0
        else: t=((P[:,ka]-A[ka])*(P[:,kb]-B[kb])+(1/(2*p) if ka==kb else 0))*S0
        s+=ci*np.sum(cb*t)
    return s
def eht(atoms,K=1.75,ret_S=False):
    A0=0.529177
    at=[(el,np.array(p)/A0) for el,p in atoms]   # Å -> bohr
    bf=basis(at); n=len(bf)
    S=np.array([[ovl(bf[i],bf[j]) for j in range(n)] for i in range(n)])
    Hd=np.array([b[2] for b in bf])
    H=K*S*(Hd[:,None]+Hd[None,:])/2; np.fill_diagonal(H,Hd)
    from scipy.linalg import eigh
    e,C=eigh(H,S)
    return e,C,S,bf
E2=14.397  # e^2/(4 pi eps0) dalam eV Å
def ppp(xyz, bonds, beta=-2.39, gamma0=11.13, nel=None, betas=None, verbose=False):
    xyz=np.array(xyz,float); n=len(xyz); nel=n if nel is None else nel
    a=E2/gamma0
    R=np.linalg.norm(xyz[:,None]-xyz[None],axis=2)
    G=E2/(R+a)  # Mataga-Nishimoto; diagonal = gamma0
    Hc=np.zeros((n,n))
    for k,(i,j) in enumerate(bonds):
        b=beta if betas is None else betas[k]; Hc[i,j]=Hc[j,i]=b
    # alpha = 0 (rujukan); inti: tiap atom Z=1
    P=np.eye(n)*nel/n
    nocc=nel//2
    for it in range(200):
        F=Hc.copy()
        q=np.diag(P)
        for m in range(n):
            F[m,m]+=0.5*P[m,m]*G[m,m]+sum((q[v]-1)*G[m,v] for v in range(n) if v!=m)
        F-=0.5*P*G*(1-np.eye(n))
        e,C=np.linalg.eigh(F)
        Pn=2*C[:,:nocc]@C[:,:nocc].T
        if np.abs(Pn-P).max()<1e-10: P=Pn; break
        P=0.5*P+0.5*Pn
    # CIS
    occ=range(nocc); vir=range(nocc,n)
    # integral (ia|jb) dalam basis MO dengan pendekatan ZDO: (pq|rs)=sum_mn C_mp C_mq G_mn C_nr C_ns
    def eri(p,q,r,s): return (C[:,p]*C[:,q])@G@(C[:,r]*C[:,s])
    ex=[(i,a_) for i in occ for a_ in vir]
    A1=np.zeros((len(ex),len(ex))); A3=np.zeros_like(A1)
    for I,(i,a_) in enumerate(ex):
        for J,(j,b) in enumerate(ex):
            d=(e[a_]-e[i]) if (i==j and a_==b) else 0
            A1[I,J]=d+2*eri(i,a_,j,b)-eri(i,j,a_,b)
            A3[I,J]=d-eri(i,j,a_,b)
    s1,v1=np.linalg.eigh(A1); s3,v3=np.linalg.eigh(A3)
    # kekuatan osilator relatif: momen transisi sqrt2 * sum c <i|r|a>
    mu=[]
    for k in range(len(s1)):
        m=np.zeros(3)
        for I,(i,a_) in enumerate(ex): m+=np.sqrt(2)*v1[I,k]*(C[:,i]*C[:,a_])@xyz
        mu.append(m)
    f=[2/3*s*(np.dot(m,m))/E2*0.0 for s,m in zip(s1,mu)]
    fosc=[ (2/3)*(s/27.2114)*(np.dot(m,m)/0.529177**2) for s,m in zip(s1,mu)]
    return e,C,P,s1,s3,np.array(fosc)
