#!/usr/bin/env python3
# Kurva energi H2 (RHF, Heitler-London, GVB) basis minimal 1s Slater dengan zeta dioptimasi.
# Integral dihitung dengan ekspansi Gauss (14 fungsi). Menulis h2curves.json untuk gambar.py.
import numpy as np
from scipy.special import erf
from scipy.optimize import minimize_scalar
r=np.linspace(1e-4,20,6000); al=0.02*2.6**np.arange(14)
G=np.exp(-np.outer(r**2,al)); w=r
c,*_=np.linalg.lstsq(G*np.sqrt(w)[:,None]*r[:,None]**0.5,np.exp(-r)*np.sqrt(w)*r**0.5,rcond=None)
c=c/np.sqrt(np.pi)
def F0(t):
    out=np.ones_like(t); m=t>1e-12; out[m]=0.5*np.sqrt(np.pi/t[m])*erf(np.sqrt(t[m])); return out
def calc(R,z):
    cc=c*z**1.5; a=al*z*z
    # pasangan primitif: (i,j) untuk pusat (A,A),(A,B),(B,B); A=0, B=R di z
    ai,aj=np.meshgrid(a,a,indexing='ij'); ci,cj=np.meshgrid(cc,cc,indexing='ij')
    p=ai+aj; mu=ai*aj/p
    def pair(dA,dB):  # posisi pusat (skalar z)
        d2=(dA-dB)**2; K=np.exp(-mu*d2); P=(ai*dA+aj*dB)/p
        return (ci*cj*K).ravel(), p.ravel(), P.ravel(), d2
    out={}
    for nm,(dA,dB) in {'aa':(0,0),'ab':(0,R),'bb':(R,R)}.items():
        coef,pp,PP,d2=pair(dA,dB)
        s=np.sum(coef*(np.pi/pp)**1.5)
        t=np.sum((ci*cj*mu*(3-2*mu*d2)*(np.pi/p)**1.5*np.exp(-mu*d2)).ravel())
        v=-np.sum(coef*2*np.pi/pp*(F0(pp*PP**2)+F0(pp*(PP-R)**2)))
        out[nm]=(coef,pp,PP,s,t+v)
    def eri(x,y):
        c1,p1,P1,_,_=out[x]; c2,p2,P2,_,_=out[y]
        P,Q=np.meshgrid(p1,p2,indexing='ij'); X,Y=np.meshgrid(P1,P2,indexing='ij'); C=np.outer(c1,c2)
        return np.sum(C*2*np.pi**2.5/(P*Q*np.sqrt(P+Q))*F0(P*Q/(P+Q)*(X-Y)**2))
    S=out['ab'][3]; haa=out['aa'][4]; hab=out['ab'][4]
    J0=eri('aa','aa'); J1=eri('aa','bb'); K=eri('ab','ab'); L=eri('aa','ab')
    return S,haa,hab,J0,J1,K,L
def energies(R,z):
    S,haa,hab,J0,J1,K,L=calc(R,z)
    # fungsi ruang f1=ab+ba (kovalen), f2=aa+bb (ionik)
    # <pq|H|rs> = h_pr S_qs + S_pr h_qs + (pr|qs) ; basis indeks 0=a,1=b
    Sm=np.array([[1,S],[S,1]]); hm=np.array([[haa,hab],[hab,haa]])
    def g(p,r_,q,s):
        idx=tuple(sorted([tuple(sorted((p,r_))),tuple(sorted((q,s)))]))
        m={((0,0),(0,0)):J0,((1,1),(1,1)):J0,((0,0),(1,1)):J1,((0,1),(0,1)):K,((0,0),(0,1)):L,((0,1),(1,1)):L}
        return m[idx]
    def el(p,q,r_,s): return hm[p,r_]*Sm[q,s]+Sm[p,r_]*hm[q,s]+g(p,r_,q,s)+Sm[p,r_]*Sm[q,s]/R
    def ov(p,q,r_,s): return Sm[p,r_]*Sm[q,s]
    F=[[(0,1),(1,0)],[(0,0),(1,1)]]
    H=np.array([[sum(el(*u,*v) for u in A for v in B) for B in F] for A in F])
    O=np.array([[sum(ov(*u,*v) for u in A for v in B) for B in F] for A in F])
    eHL=H[0,0]/O[0,0]
    x=np.array([1,1.]); eHF=(x@H@x)/(x@O@x)
    from scipy.linalg import eigh
    e,v=eigh(H,O); 
    return eHF,eHL,e[0],v[:,0]
import json
eh=27.211386
Rs=np.concatenate([np.linspace(0.8,3,23),np.linspace(3.25,7,16)])
data={'R':list(Rs),'HF':[],'HL':[],'GVB':[]}
for R in Rs:
    for k,m in [('HF',0),('HL',1),('GVB',2)]:
        data[k].append(minimize_scalar(lambda z: energies(R,z)[m],bounds=(0.8,1.6),method='bounded').fun)
json.dump(data,open('h2curves.json','w'))
