# kq.py - program kimia kuantum kecil untuk Bab 17 Kimia Kuantum.
# Integral Gauss Kartesius (s, p, d) dengan skema McMurchie-Davidson, basis STO-3G, 6-31G, 6-31G*, 6-31G**,
# dan RHF dengan DIIS. Semua besaran dalam satuan atom. Ditulis untuk belajar, bukan untuk kecepatan.
import numpy as np
from math import factorial
from scipy.special import hyp1f1, gammainc, gamma
from itertools import product

def dfact(n):
    return 1 if n <= 0 else n * dfact(n - 2)

def boys(n, T):
    if T < 1e-12: return 1.0 / (2 * n + 1)
    return gamma(n + 0.5) * gammainc(n + 0.5, T) / (2 * T ** (n + 0.5))

def E(i, j, t, Qx, a, b):
    p = a + b; q = a * b / p
    if t < 0 or t > i + j: return 0.0
    if i == j == t == 0: return np.exp(-q * Qx * Qx)
    if j == 0:
        return (1 / (2 * p)) * E(i - 1, j, t - 1, Qx, a, b) - (q * Qx / a) * E(i - 1, j, t, Qx, a, b) + (t + 1) * E(i - 1, j, t + 1, Qx, a, b)
    return (1 / (2 * p)) * E(i, j - 1, t - 1, Qx, a, b) + (q * Qx / b) * E(i, j - 1, t, Qx, a, b) + (t + 1) * E(i, j - 1, t + 1, Qx, a, b)

class BF:  # fungsi basis terkontraksi Kartesius
    def __init__(s, origin, shell, exps, coefs):
        s.o = np.array(origin, float); s.l = shell; s.e = np.array(exps, float); s.c = np.array(coefs, float)
        l, m, n = shell; L = l + m + n
        s.N = np.array([(2 / np.pi) ** 0.75 * 2 ** L * a ** ((2 * L + 3) / 4) / np.sqrt(dfact(2 * l - 1) * dfact(2 * m - 1) * dfact(2 * n - 1)) for a in s.e])
        # normalisasi kontraksi
        pf = np.pi ** 1.5 * dfact(2 * l - 1) * dfact(2 * m - 1) * dfact(2 * n - 1) / 2 ** L
        tot = 0.0
        for i in range(len(s.e)):
            for j in range(len(s.e)):
                tot += s.N[i] * s.N[j] * s.c[i] * s.c[j] / (s.e[i] + s.e[j]) ** (L + 1.5)
        s.c = s.c / np.sqrt(tot * pf)

def ov(a, l1, A, b, l2, B):
    S1 = E(l1[0], l2[0], 0, A[0] - B[0], a, b); S2 = E(l1[1], l2[1], 0, A[1] - B[1], a, b); S3 = E(l1[2], l2[2], 0, A[2] - B[2], a, b)
    return S1 * S2 * S3 * (np.pi / (a + b)) ** 1.5

def kin(a, l1, A, b, l2, B):
    l, m, n = l2
    t0 = b * (2 * (l + m + n) + 3) * ov(a, l1, A, b, l2, B)
    t1 = -2 * b * b * (ov(a, l1, A, b, (l + 2, m, n), B) + ov(a, l1, A, b, (l, m + 2, n), B) + ov(a, l1, A, b, (l, m, n + 2), B))
    t2 = -0.5 * (l * (l - 1) * ov(a, l1, A, b, (l - 2, m, n), B) + m * (m - 1) * ov(a, l1, A, b, (l, m - 2, n), B) + n * (n - 1) * ov(a, l1, A, b, (l, m, n - 2), B))
    return t0 + t1 + t2

def S_(A_, B_):
    return sum(A_.N[i] * B_.N[j] * A_.c[i] * B_.c[j] * ov(A_.e[i], A_.l, A_.o, B_.e[j], B_.l, B_.o) for i in range(len(A_.e)) for j in range(len(B_.e)))
def T_(A_, B_):
    return sum(A_.N[i] * B_.N[j] * A_.c[i] * B_.c[j] * kin(A_.e[i], A_.l, A_.o, B_.e[j], B_.l, B_.o) for i in range(len(A_.e)) for j in range(len(B_.e)))
def V_(A_, B_, C):
    return sum(A_.N[i] * B_.N[j] * A_.c[i] * B_.c[j] * nuc(A_.e[i], A_.l, A_.o, B_.e[j], B_.l, B_.o, C) for i in range(len(A_.e)) for j in range(len(B_.e)))
def ERI_(A_, B_, C_, D_):
    s = 0.0
    for i in range(len(A_.e)):
        for j in range(len(B_.e)):
            for k in range(len(C_.e)):
                for l in range(len(D_.e)):
                    s += A_.N[i] * B_.N[j] * C_.N[k] * D_.N[l] * A_.c[i] * B_.c[j] * C_.c[k] * D_.c[l] * eri(A_.e[i], A_.l, A_.o, B_.e[j], B_.l, B_.o, C_.e[k], C_.l, C_.o, D_.e[l], D_.l, D_.o)
    return s

# --- data basis
def cart(L):
    return [(i, j, L - i - j) for i in range(L, -1, -1) for j in range(L - i, -1, -1)]

STO3G = {
 'H': [('S', [3.42525091, 0.62391373, 0.16885540], [0.15432897, 0.53532814, 0.44463454])],
 'He': [('S', [6.36242139, 1.15892300, 0.31364979], [0.15432897, 0.53532814, 0.44463454])],
 'C': [('S', [71.6168370, 13.0450960, 3.5305122], [0.15432897, 0.53532814, 0.44463454]),
       ('SP', [2.9412494, 0.6834831, 0.2222899], [-0.09996723, 0.39951283, 0.70011547], [0.15591627, 0.60768372, 0.39195739])],
 'N': [('S', [99.1061690, 18.0523120, 4.8856602], [0.15432897, 0.53532814, 0.44463454]),
       ('SP', [3.7804559, 0.8784966, 0.2857144], [-0.09996723, 0.39951283, 0.70011547], [0.15591627, 0.60768372, 0.39195739])],
 'O': [('S', [130.7093200, 23.8088610, 6.4436083], [0.15432897, 0.53532814, 0.44463454]),
       ('SP', [5.0331513, 1.1695961, 0.3803890], [-0.09996723, 0.39951283, 0.70011547], [0.15591627, 0.60768372, 0.39195739])],
 'F': [('S', [166.6791300, 30.3608120, 8.2168207], [0.15432897, 0.53532814, 0.44463454]),
       ('SP', [6.4648032, 1.5022812, 0.4885885], [-0.09996723, 0.39951283, 0.70011547], [0.15591627, 0.60768372, 0.39195739])],
}
B631G = {
 'H': [('S', [18.7311370, 2.8253937, 0.6401217], [0.03349460, 0.23472695, 0.81375733]), ('S', [0.1612778], [1.0])],
 'C': [('S', [3047.52490, 457.369510, 103.948690, 29.2101550, 9.28666300, 3.16392700], [0.0018347, 0.0140373, 0.0688426, 0.2321844, 0.4679413, 0.3623120]),
       ('SP', [7.86827240, 1.88128850, 0.54424930], [-0.1193324, -0.1608542, 1.1434564], [0.0689991, 0.3164240, 0.7443083]),
       ('SP', [0.16871440], [1.0], [1.0])],
 'N': [('S', [4173.51100, 627.457900, 142.902100, 40.2343300, 12.8202100, 4.39043700], [0.0018348, 0.0139950, 0.0685870, 0.2322410, 0.4690700, 0.3604550]),
       ('SP', [11.6263580, 2.71628000, 0.77221800], [-0.1149610, -0.1691180, 1.1458520], [0.0675800, 0.3239070, 0.7408950]),
       ('SP', [0.21203130], [1.0], [1.0])],
 'O': [('S', [5484.67166, 825.234946, 188.046958, 52.9645000, 16.8975704, 5.79963534], [0.00183107, 0.0139501, 0.0684451, 0.232714, 0.470193, 0.358520]),
       ('SP', [15.5396162, 3.59993359, 1.01376175], [-0.110778, -0.148026, 1.130767], [0.0708743, 0.339753, 0.727159]),
       ('SP', [0.270005822], [1.0], [1.0])],
}
def polar(bas, dexp, pexpH=None):
    b = {k: list(v) for k, v in bas.items()}
    for el in b:
        if el in dexp: b[el] = b[el] + [('D', [dexp[el]], [1.0])]
    if pexpH: b['H'] = b['H'] + [('P', [pexpH], [1.0])]
    return b
B631Gs = polar(B631G, {'C': 0.8, 'N': 0.8, 'O': 0.8})
B631Gss = polar(B631G, {'C': 0.8, 'N': 0.8, 'O': 0.8}, 1.1)
Z = {'H': 1, 'He': 2, 'C': 6, 'N': 7, 'O': 8, 'F': 9}

def basis(atoms, bas):
    bfs = []; lab = []
    for k, (el, xyz) in enumerate(atoms):
        for sh in bas[el]:
            if sh[0] == 'S': bfs.append(BF(xyz, (0, 0, 0), sh[1], sh[2])); lab.append((k, el, 's'))
            elif sh[0] == 'SP':
                bfs.append(BF(xyz, (0, 0, 0), sh[1], sh[2])); lab.append((k, el, 's'))
                for l in cart(1): bfs.append(BF(xyz, l, sh[1], sh[3])); lab.append((k, el, 'p'))
            elif sh[0] == 'P':
                for l in cart(1): bfs.append(BF(xyz, l, sh[1], sh[2])); lab.append((k, el, 'p'))
            elif sh[0] == 'D':
                for l in cart(2): bfs.append(BF(xyz, l, sh[1], sh[2])); lab.append((k, el, 'd'))
    return bfs, lab

def ints(atoms, bas):
    bfs, lab = basis(atoms, bas); n = len(bfs)
    S = np.zeros((n, n)); T = np.zeros((n, n)); V = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1):
            S[i, j] = S[j, i] = S_(bfs[i], bfs[j]); T[i, j] = T[j, i] = T_(bfs[i], bfs[j])
            V[i, j] = V[j, i] = sum(-Z[el] * V_(bfs[i], bfs[j], np.array(xyz)) for el, xyz in atoms)
    I = np.zeros((n, n, n, n))
    for i in range(n):
        for j in range(i + 1):
            ij = i * (i + 1) // 2 + j
            for k in range(n):
                for l in range(k + 1):
                    kl = k * (k + 1) // 2 + l
                    if ij < kl: continue
                    v = ERI_(bfs[i], bfs[j], bfs[k], bfs[l])
                    for (a, b, c, d) in [(i, j, k, l), (j, i, k, l), (i, j, l, k), (j, i, l, k), (k, l, i, j), (l, k, i, j), (k, l, j, i), (l, k, j, i)]:
                        I[a, b, c, d] = v
    return S, T, V, I, bfs, lab

def enuc(atoms):
    e = 0.0
    for i in range(len(atoms)):
        for j in range(i):
            e += Z[atoms[i][0]] * Z[atoms[j][0]] / np.linalg.norm(np.array(atoms[i][1]) - np.array(atoms[j][1]))
    return e

def rhf(S, T, V, I, nel, Enuc, maxit=100, tol=1e-10, verbose=False, diis=True):
    H = T + V; s, U = np.linalg.eigh(S); X = U @ np.diag(s ** -0.5) @ U.T
    no = nel // 2; e, C = np.linalg.eigh(X.T @ H @ X); C = X @ C; D = C[:, :no] @ C[:, :no].T
    Eold = 0; Fs = []; Es = []; hist = []
    for it in range(maxit):
        J = np.einsum('pqrs,rs->pq', I, D); K = np.einsum('prqs,rs->pq', I, D); F = H + 2 * J - K
        Eel = np.sum(D * (H + F)); err = F @ D @ S - S @ D @ F
        hist.append((it, Eel + Enuc))
        if diis:
            Fs.append(F); Es.append(err)
            if len(Fs) > 8: Fs.pop(0); Es.pop(0)
            if len(Fs) > 2:
                m = len(Fs); Bm = -np.ones((m + 1, m + 1)); Bm[-1, -1] = 0
                for i in range(m):
                    for j in range(m): Bm[i, j] = np.sum(Es[i] * Es[j])
                rhs = np.zeros(m + 1); rhs[-1] = -1
                cc = np.linalg.solve(Bm, rhs); F = sum(cc[i] * Fs[i] for i in range(m))
        e, Cp = np.linalg.eigh(X.T @ F @ X); C = X @ Cp; D = C[:, :no] @ C[:, :no].T
        if abs(Eel - Eold) < tol and np.abs(err).max() < 1e-7: break
        Eold = Eel
    J = np.einsum('pqrs,rs->pq', I, D); K = np.einsum('prqs,rs->pq', I, D); F = H + 2 * J - K
    e, Cp = np.linalg.eigh(X.T @ F @ X); C = X @ Cp; D = C[:, :no] @ C[:, :no].T
    Eel = np.sum(D * (H + F))
    return dict(E=Eel + Enuc, e=e, C=C, D=D, F=F, H=H, X=X, it=it, hist=hist, no=no)

def mo_eri(I, C):
    return np.einsum('pqrs,pi,qj,rk,sl->ijkl', I, C, C, C, C, optimize=True)

def mp2(res, I):
    C, e, no = res['C'], res['e'], res['no']; mo = mo_eri(I, C)
    o = slice(0, no); v = slice(no, None)
    iajb = mo[o, v, o, v]; eo = e[:no]; ev = e[no:]
    d = eo[:, None, None, None] - ev[None, :, None, None] + eo[None, None, :, None] - ev[None, None, None, :]
    return np.sum(iajb * (2 * iajb - iajb.transpose(0, 3, 2, 1)) / d)

# ---- tabel koefisien Hermite E dan integral Hermite R
from functools import lru_cache
@lru_cache(maxsize=None)
def Et(i, j, Qx, a, b):
    return tuple(E(i, j, t, Qx, a, b) for t in range(i + j + 1))

def Rtab(L, p, PC):
    RPC2 = PC @ PC; T = p * RPC2
    Fn = [boys(n, T) for n in range(L + 1)]
    # R[n][t][u][v]
    Rn = {}
    for n in range(L + 1): Rn[(n, 0, 0, 0)] = (-2 * p) ** n * Fn[n]
    for tot in range(1, L + 1):
        for n in range(L - tot + 1):
            for t in range(tot + 1):
                for u in range(tot - t + 1):
                    v = tot - t - u
                    if t > 0:
                        val = PC[0] * Rn[(n + 1, t - 1, u, v)] + ((t - 1) * Rn[(n + 1, t - 2, u, v)] if t > 1 else 0)
                    elif u > 0:
                        val = PC[1] * Rn[(n + 1, t, u - 1, v)] + ((u - 1) * Rn[(n + 1, t, u - 2, v)] if u > 1 else 0)
                    else:
                        val = PC[2] * Rn[(n + 1, t, u, v - 1)] + ((v - 1) * Rn[(n + 1, t, u, v - 2)] if v > 1 else 0)
                    Rn[(n, t, u, v)] = val
    return Rn

def nuc(a, l1, A, b, l2, B, C):
    p = a + b; P = (a * A + b * B) / p
    ex = Et(l1[0], l2[0], A[0] - B[0], a, b); ey = Et(l1[1], l2[1], A[1] - B[1], a, b); ez = Et(l1[2], l2[2], A[2] - B[2], a, b)
    Rn = Rtab(sum(l1) + sum(l2), p, P - C); val = 0.0
    for t, x in enumerate(ex):
        for u, y in enumerate(ey):
            for v, z in enumerate(ez):
                val += x * y * z * Rn[(0, t, u, v)]
    return 2 * np.pi / p * val

def eri(a, l1, A, b, l2, B, c, l3, C, d, l4, D):
    p = a + b; q = c + d; al = p * q / (p + q); P = (a * A + b * B) / p; Q = (c * C + d * D) / q
    e1 = [Et(l1[k], l2[k], A[k] - B[k], a, b) for k in range(3)]; e2 = [Et(l3[k], l4[k], C[k] - D[k], c, d) for k in range(3)]
    Rn = Rtab(sum(l1) + sum(l2) + sum(l3) + sum(l4), al, P - Q); val = 0.0
    for t, x1 in enumerate(e1[0]):
        for u, y1 in enumerate(e1[1]):
            for v, z1 in enumerate(e1[2]):
                f1 = x1 * y1 * z1
                if f1 == 0: continue
                for tau, x2 in enumerate(e2[0]):
                    for nu, y2 in enumerate(e2[1]):
                        for phi, z2 in enumerate(e2[2]):
                            val += f1 * x2 * y2 * z2 * (-1) ** (tau + nu + phi) * Rn[(0, t + tau, u + nu, v + phi)]
    return 2 * np.pi ** 2.5 / (p * q * np.sqrt(p + q)) * val

ANG = 1.8897261246
def h2o(R, th):  # R dalam Å, sudut dalam derajat; bidang xz, sumbu C2 = z
    R *= ANG; h = np.radians(th) / 2
    return [('O', (0.0, 0.0, 0.0)), ('H', (R * np.sin(h), 0.0, R * np.cos(h))), ('H', (-R * np.sin(h), 0.0, R * np.cos(h)))]
def energi(atoms, bas, nel, **kw):
    S, T, V, I, b, l = ints(atoms, bas); r = rhf(S, T, V, I, nel, enuc(atoms), **kw); r.update(S=S, T=T, V=V, I=I, b=b, lab=l, Enuc=enuc(atoms)); return r
