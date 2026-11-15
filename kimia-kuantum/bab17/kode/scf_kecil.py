import numpy as np
from scipy.special import erf

# STO-3G untuk 1s dengan zeta = 1; eksponen dipersekalakan dengan zeta**2
d0 = np.array([0.444635, 0.535328, 0.154329])
a0 = np.array([0.109818, 0.405771, 2.227660])

def F0(t):                                    # fungsi Boys orde nol
    return 1.0 if t < 1e-10 else 0.5 * np.sqrt(np.pi / t) * erf(np.sqrt(t))

def scf(Z, zeta, R, nel=2, siklus=30):
    X = np.array([0.0, R])                    # inti di sumbu z
    prim = [[(zt**2 * a0[k], d0[k] * (2 * zt**2 * a0[k] / np.pi)**0.75) for k in range(3)]
            for zt in zeta]                   # (eksponen, koefisien ternormalisasi)
    n = len(X)
    S, T, V = np.zeros((n, n)), np.zeros((n, n)), np.zeros((n, n))
    G = np.zeros((n, n, n, n))
    for i in range(n):
        for j in range(n):
            for a, ca in prim[i]:
                for b, cb in prim[j]:
                    p = a + b; P = (a * X[i] + b * X[j]) / p
                    K = ca * cb * np.exp(-a * b / p * (X[i] - X[j])**2)
                    S[i, j] += K * (np.pi / p)**1.5
                    T[i, j] += K * (np.pi / p)**1.5 * a * b / p * (3 - 2 * a * b / p * (X[i] - X[j])**2)
                    for C in range(n):
                        V[i, j] -= K * 2 * np.pi / p * Z[C] * F0(p * (P - X[C])**2)
                    for k in range(n):
                        for l in range(n):
                            for c, cc in prim[k]:
                                for d, cd in prim[l]:
                                    q = c + d; Q = (c * X[k] + d * X[l]) / q
                                    L = cc * cd * np.exp(-c * d / q * (X[k] - X[l])**2)
                                    G[i, j, k, l] += K * L * 2 * np.pi**2.5 / (p * q * np.sqrt(p + q)) \
                                                     * F0(p * q / (p + q) * (P - Q)**2)
    H = T + V
    s, U = np.linalg.eigh(S); Xm = U @ np.diag(s**-0.5) @ U.T      # ortogonalisasi simetris
    P = np.zeros((n, n))                                            # tebakan awal: Hcore
    for it in range(siklus):
        F = H + np.einsum('kl,ijkl->ij', P, G) - 0.5 * np.einsum('kl,ilkj->ij', P, G)
        e, Cp = np.linalg.eigh(Xm.T @ F @ Xm); C = Xm @ Cp
        Pbaru = 2 * C[:, :nel // 2] @ C[:, :nel // 2].T
        if np.abs(Pbaru - P).max() < 1e-8: break
        P = Pbaru
    Eel = 0.5 * np.sum(P * (H + F))
    return Eel + Z[0] * Z[1] / R, e, C, S, P

for nama, Z, zeta, R in [('H2', [1, 1], [1.24, 1.24], 1.4), ('HeH+', [2, 1], [1.69, 1.24], 1.4632)]:
    E, e, C, S, P = scf(Z, zeta, R)
    print(f'{nama}: E = {E:.6f} hartree, energi orbital = {np.round(e, 4)}')
