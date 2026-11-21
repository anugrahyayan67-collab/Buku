# kq2.py - UHF, momen dipol, populasi, CCSD(T), dan CI determinan untuk sistem kecil.
from kq import *
import itertools

def mom1(a, l1, A, b, l2, B, C, k):  # <a|(r_k - C_k)|b>
    p = a + b; P = (a * A + b * B) / p; out = (np.pi / p) ** 1.5
    for d in range(3):
        e = Et(l1[d], l2[d], A[d] - B[d], a, b)
        if d == k:
            e1 = e[1] if len(e) > 1 else 0.0
            out *= e1 + (P[d] - C[d]) * e[0]
        else:
            out *= e[0]
    return out

def dipints(bfs, C=np.zeros(3)):
    n = len(bfs); M = np.zeros((3, n, n))
    for k in range(3):
        for i in range(n):
            for j in range(i + 1):
                A_, B_ = bfs[i], bfs[j]
                v = sum(A_.N[x] * B_.N[y] * A_.c[x] * B_.c[y] * mom1(A_.e[x], A_.l, A_.o, B_.e[y], B_.l, B_.o, C, k) for x in range(len(A_.e)) for y in range(len(B_.e)))
                M[k, i, j] = M[k, j, i] = v
    return M

def dipol(r, atoms):
    M = dipints(r['b']); D = r['D']
    el = -2 * np.array([np.sum(D * M[k]) for k in range(3)])
    nu = sum(Z[e] * np.array(x) for e, x in atoms)
    return el + nu  # a.u.

def mulliken(r, atoms):
    PS = 2 * r['D'] @ r['S']; q = []
    for k, (e, x) in enumerate(atoms):
        idx = [i for i, L in enumerate(r['lab']) if L[0] == k]
        q.append(Z[e] - sum(PS[i, i] for i in idx))
    return np.array(q)

def lowdin(r, atoms):
    s, U = np.linalg.eigh(r['S']); Sh = U @ np.diag(s ** 0.5) @ U.T
    M = Sh @ (2 * r['D']) @ Sh; q = []
    for k, (e, x) in enumerate(atoms):
        idx = [i for i, L in enumerate(r['lab']) if L[0] == k]
        q.append(Z[e] - sum(M[i, i] for i in idx))
    return np.array(q)

def uhf(S, T, V, I, na, nb, Enuc, maxit=300, tol=1e-10, guess_mix=0.0):
    H = T + V; s, U = np.linalg.eigh(S); X = U @ np.diag(s ** -0.5) @ U.T
    e, C = np.linalg.eigh(X.T @ H @ X); C = X @ C
    Ca = C.copy(); Cb = C.copy()
    if guess_mix and na > 0:
        h, l = na - 1, na; th = guess_mix
        ch, cl = Ca[:, h].copy(), Ca[:, l].copy(); Ca[:, h] = np.cos(th) * ch + np.sin(th) * cl; Ca[:, l] = -np.sin(th) * ch + np.cos(th) * cl
    Da = Ca[:, :na] @ Ca[:, :na].T; Db = Cb[:, :nb] @ Cb[:, :nb].T; Eold = 0
    for it in range(maxit):
        J = np.einsum('pqrs,rs->pq', I, Da + Db)
        Fa = H + J - np.einsum('prqs,rs->pq', I, Da); Fb = H + J - np.einsum('prqs,rs->pq', I, Db)
        Eel = 0.5 * (np.sum((Da + Db) * H) + np.sum(Da * Fa) + np.sum(Db * Fb))
        ea, Ca = np.linalg.eigh(X.T @ Fa @ X); Ca = X @ Ca; eb, Cb = np.linalg.eigh(X.T @ Fb @ X); Cb = X @ Cb
        Dan = Ca[:, :na] @ Ca[:, :na].T; Dbn = Cb[:, :nb] @ Cb[:, :nb].T
        Da = 0.5 * Da + 0.5 * Dan if it < 5 else Dan; Db = 0.5 * Db + 0.5 * Dbn if it < 5 else Dbn
        if abs(Eel - Eold) < tol and it > 5: break
        Eold = Eel
    # S^2
    Sab = Ca[:, :na].T @ S @ Cb[:, :nb]
    S2 = ((na - nb) / 2) * ((na - nb) / 2 + 1) + nb - np.sum(Sab ** 2)
    return dict(E=Eel + Enuc, ea=ea, eb=eb, Ca=Ca, Cb=Cb, S2=S2, it=it)

# ----- spin-orbital integrals
def so_ints(r):
    C, e, I, H = r['C'], r['e'], r['I'], r['H']; n = C.shape[1]
    mo = mo_eri(I, C)  # chemist (pq|rs)
    hmo = C.T @ H @ C
    nso = 2 * n; eps = np.repeat(e, 2)
    # antisymmetrized <pq||rs>
    sp = np.arange(nso) % 2; orb = np.arange(nso) // 2
    g = np.zeros((nso,) * 4)
    for p in range(nso):
        for q in range(nso):
            for rr in range(nso):
                for s in range(nso):
                    v1 = mo[orb[p], orb[rr], orb[q], orb[s]] * (sp[p] == sp[rr]) * (sp[q] == sp[s])
                    v2 = mo[orb[p], orb[s], orb[q], orb[rr]] * (sp[p] == sp[s]) * (sp[q] == sp[rr])
                    g[p, q, rr, s] = v1 - v2
    h = np.zeros((nso, nso))
    for p in range(nso):
        for q in range(nso):
            h[p, q] = hmo[orb[p], orb[q]] * (sp[p] == sp[q])
    return h, g, eps

def ccsd(r, maxit=100, tol=1e-10, triples=False):
    h, g, eps = so_ints(r); no = 2 * r['no']; nso = len(eps); nv = nso - no
    o = slice(0, no); v = slice(no, nso)
    F = h + np.einsum('pmqm->pq', g[:, o, :, o])
    Dai = eps[o, None] - eps[None, v]
    Dijab = eps[o, None, None, None] + eps[None, o, None, None] - eps[None, None, v, None] - eps[None, None, None, v]
    t1 = np.zeros((no, nv)); t2 = g[o, o, v, v] / Dijab
    Emp2 = 0.25 * np.sum(g[o, o, v, v] * t2)
    Eold = Emp2
    def tau_t(t1, t2): return t2 + np.einsum('ia,jb->ijab', t1, t1) - np.einsum('ib,ja->ijab', t1, t1)
    for it in range(maxit):
        tau = tau_t(t1, t2); taut = t2 + 0.5 * (np.einsum('ia,jb->ijab', t1, t1) - np.einsum('ib,ja->ijab', t1, t1))
        Fae = -0.5 * np.einsum('me,ma->ae', F[o, v], t1) + np.einsum('mf,mafe->ae', t1, g[o, v, v, v]) - 0.5 * np.einsum('mnaf,mnef->ae', taut, g[o, o, v, v])
        Fmi = 0.5 * np.einsum('ie,me->mi', t1, F[o, v]) + np.einsum('ne,mnie->mi', t1, g[o, o, o, v]) + 0.5 * np.einsum('inef,mnef->mi', taut, g[o, o, v, v])
        Fme = F[o, v] + np.einsum('nf,mnef->me', t1, g[o, o, v, v])
        Wmnij = g[o, o, o, o] + np.einsum('je,mnie->mnij', t1, g[o, o, o, v]) - np.einsum('ie,mnje->mnij', t1, g[o, o, o, v]) + 0.25 * np.einsum('ijef,mnef->mnij', tau, g[o, o, v, v])
        Wabef = g[v, v, v, v] - np.einsum('mb,amef->abef', t1, g[v, o, v, v]) + np.einsum('ma,bmef->abef', t1, g[v, o, v, v]) + 0.25 * np.einsum('mnab,mnef->abef', tau, g[o, o, v, v])
        Wmbej = g[o, v, v, o] + np.einsum('jf,mbef->mbej', t1, g[o, v, v, v]) - np.einsum('nb,mnej->mbej', t1, g[o, o, v, o]) - np.einsum('jnfb,mnef->mbej', 0.5 * t2 + np.einsum('jf,nb->jnfb', t1, t1), g[o, o, v, v])
        t1n = F[o, v] + np.einsum('ie,ae->ia', t1, Fae) - np.einsum('ma,mi->ia', t1, Fmi) + np.einsum('imae,me->ia', t2, Fme) - np.einsum('nf,naif->ia', t1, g[o, v, o, v]) - 0.5 * np.einsum('imef,maef->ia', t2, g[o, v, v, v]) - 0.5 * np.einsum('mnae,nmei->ia', t2, g[o, o, v, o])
        t1n = t1n / Dai
        Ft = Fae - 0.5 * np.einsum('mb,me->be', t1, Fme); Fm = Fmi + 0.5 * np.einsum('je,me->mj', t1, Fme)
        t2n = g[o, o, v, v].copy()
        P = np.einsum('ijae,be->ijab', t2, Ft); t2n += P - P.transpose(0, 1, 3, 2)
        P = np.einsum('imab,mj->ijab', t2, Fm); t2n -= P - P.transpose(1, 0, 2, 3)
        t2n += 0.5 * np.einsum('mnab,mnij->ijab', tau, Wmnij) + 0.5 * np.einsum('ijef,abef->ijab', tau, Wabef)
        P = np.einsum('imae,mbej->ijab', t2, Wmbej) - np.einsum('ie,ma,mbej->ijab', t1, t1, g[o, v, v, o])
        t2n += P - P.transpose(0, 1, 3, 2) - P.transpose(1, 0, 2, 3) + P.transpose(1, 0, 3, 2)
        P = np.einsum('ie,abej->ijab', t1, g[v, v, v, o]); t2n += P - P.transpose(1, 0, 2, 3)
        P = np.einsum('ma,mbij->ijab', t1, g[o, v, o, o]); t2n -= P - P.transpose(0, 1, 3, 2)
        t2n = t2n / Dijab
        t1, t2 = t1n, t2n
        Ecc = np.einsum('ia,ia', F[o, v], t1) + 0.25 * np.einsum('ijab,ijab', g[o, o, v, v], t2) + 0.5 * np.einsum('ijab,ia,jb', g[o, o, v, v], t1, t1)
        if abs(Ecc - Eold) < tol: break
        Eold = Ecc
    Et_ = 0.0  # untuk (T) pakai ccsd_t()
    return dict(Emp2=Emp2, Eccsd=Ecc, Et=Et_, it=it, t1=t1, t2=t2)

# ----- CI dalam basis determinan (spin-orbital), untuk sistem kecil
def ci(r, level=None, nfrozen=0):
    h, g, eps = so_ints(r); nso = len(eps); ne = 2 * r['no']
    ref = tuple(range(ne))
    dets = []
    for occ in itertools.combinations(range(nso), ne):
        na = sum(1 for x in occ if x % 2 == 0)
        if na != ne // 2: continue
        exc = len(set(occ) - set(ref))
        if level is not None and exc > level: continue
        dets.append(occ)
    n = len(dets); Hm = np.zeros((n, n))
    for I_, D1 in enumerate(dets):
        s1 = set(D1)
        for J_ in range(I_ + 1):
            D2 = dets[J_]; s2 = set(D2); diff = s1 - s2
            if len(diff) > 2: continue
            if len(diff) == 0:
                val = sum(h[p, p] for p in D1) + 0.5 * sum(g[p, q, p, q] for p in D1 for q in D1)
            else:
                # bawa D2 ke urutan maksimum kesamaan dengan D1, hitung tanda
                l1 = list(D1); l2 = list(D2)
                a_ = sorted(diff); b_ = sorted(s2 - s1)
                # tanda: permutasi untuk memindahkan elemen berbeda ke depan
                def sign_move(lst, items):
                    lst = list(lst); sgn = 1
                    for k, it in enumerate(items):
                        idx = lst.index(it); sgn *= (-1) ** (idx - k); lst.pop(idx); lst.insert(k, it)
                    return sgn, lst
                sa, la = sign_move(l1, a_); sb, lb = sign_move(l2, b_); sg = sa * sb
                if len(diff) == 1:
                    m, p = a_[0], b_[0]
                    val = sg * (h[m, p] + sum(g[m, q, p, q] for q in D1 if q != m))
                else:
                    m, n_ = a_; p, q = b_
                    val = sg * g[m, n_, p, q]
            Hm[I_, J_] = Hm[J_, I_] = val
    w, U = np.linalg.eigh(Hm)
    return w[0] + r["Enuc"], n, U[:, 0], dets

def ccsd_t(r, maxit=100):
    c = ccsd(r, maxit=maxit, triples=False); h, g, eps = so_ints(r); no = 2 * r['no']; nso = len(eps)
    o = slice(0, no); v = slice(no, nso); t1, t2 = c['t1'], c['t2']; eo, ev = eps[o], eps[v]
    def conn(i, j, k):
        return np.einsum('ae,ebc->abc', t2[j, k], g[v, i, v, v]) - np.einsum('mbc,ma->abc', t2[i], g[o, v, j, k])
    def disc(i, j, k):
        return np.einsum('a,bc->abc', t1[i], g[j, k, v, v])
    def Pabc(X): return X - X.transpose(1, 0, 2) - X.transpose(2, 1, 0)
    Et = 0.0
    for i in range(no):
        for j in range(no):
            for k in range(no):
                if i == j or j == k or i == k: continue
                W = Pabc(conn(i, j, k) - conn(j, i, k) - conn(k, j, i))
                Vd = Pabc(disc(i, j, k) - disc(j, i, k) - disc(k, j, i))
                D = eo[i] + eo[j] + eo[k] - ev[:, None, None] - ev[None, :, None] - ev[None, None, :]
                Et += np.sum(W * (W + Vd) / D) / 36
    c['Et'] = Et; return c
