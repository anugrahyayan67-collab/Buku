import numpy as np
from scipy.linalg import eigh_tridiagonal
def pw92(rs, pol):
    A, a1, b1, b2, b3, b4 = (0.031091, 0.21370, 7.5957, 3.5876, 1.6382, 0.49294) if not pol else (0.015545, 0.20548, 14.1189, 6.1977, 3.3662, 0.62517)
    return -2 * A * (1 + a1 * rs) * np.log(1 + 1 / (2 * A * (b1 * rs ** 0.5 + b2 * rs + b3 * rs ** 1.5 + b4 * rs ** 2)))
def cumtrap(f, h):
    c = np.zeros_like(f); c[1:] = np.cumsum((f[1:] + f[:-1]) * h / 2); return c
def atom(Z, nel=2, korelasi=True, pol=False, h=0.0008, rmax=25.0, it=300):
    r = np.arange(1, int(rmax / h) + 1) * h; N = len(r)
    rho = Z ** 3 / np.pi * np.exp(-2 * Z * r) * nel
    for k in range(it):
        rho_ = np.maximum(rho, 1e-30); rs = (3 / (4 * np.pi * rho_)) ** (1 / 3)
        f = 6 if pol else 3
        vx = -(f / np.pi * rho_) ** (1 / 3); ex = 0.75 * vx
        if korelasi:
            ec = pw92(rs, pol); d = 1e-6; dec = (pw92(rs * (1 + d), pol) - pw92(rs * (1 - d), pol)) / (2 * rs * d); vc = ec - rs / 3 * dec
        else:
            ec = vc = 0 * rs
        q = cumtrap(4 * np.pi * r ** 2 * rho, h); g = 4 * np.pi * r * rho
        outer = cumtrap(g[::-1], h)[::-1]; vH = q / r + outer
        v = -Z / r + vH + vx + vc
        e, V = eigh_tridiagonal(1 / h ** 2 + v, -0.5 / h ** 2 * np.ones(N - 1), select='i', select_range=(0, 0))
        u = V[:, 0] / np.sqrt(np.sum(V[:, 0] ** 2) * h)
        rho_new = nel * u ** 2 / (4 * np.pi * r ** 2)
        if np.abs(rho_new - rho).max() < 1e-10 * Z ** 3: rho = rho_new; break
        rho = 0.5 * rho + 0.5 * rho_new
    eps = e[0]; dV = 4 * np.pi * r ** 2 * h
    EH = 0.5 * np.sum(vH * rho * dV); Ex = np.sum(ex * rho * dV); Ec = np.sum(ec * rho * dV); Vxc = np.sum((vx + vc) * rho * dV)
    E = nel * eps - EH - Vxc + Ex + Ec
    return dict(E=E, eps=eps, Ex=Ex, Ec=Ec, EH=EH, r=r, rho=rho, it=k)
if __name__ == '__main__':
    for nm, kw in [('He LDA', dict(Z=2, nel=2)), ('He x-only', dict(Z=2, nel=2, korelasi=False)), ('H LSDA', dict(Z=1, nel=1, pol=True)), ('H LSDA x-only', dict(Z=1, nel=1, pol=True, korelasi=False))]:
        d = atom(**kw); print(nm, 'E', round(d['E'], 5), 'eps', round(d['eps'], 5), 'Ex', round(d['Ex'], 5), 'Ec', round(d['Ec'], 5), 'EH', round(d['EH'], 5), d['it'])
