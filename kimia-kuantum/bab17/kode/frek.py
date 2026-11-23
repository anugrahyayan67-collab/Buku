from kq import *
import sys, json
MASS = {'H': 1.00782503, 'O': 15.99491462, 'C': 12.0, 'N': 14.00307401}
def E_at(els, x, bas, nel):
    at = [(e, tuple(x[3 * k:3 * k + 3])) for k, e in enumerate(els)]
    S, T, V, I, b, l = ints(at, bas); return rhf(S, T, V, I, nel, enuc(at))['E']
def hessian(els, x0, bas, nel, h=0.005):
    n = len(x0); Hs = np.zeros((n, n)); E0 = E_at(els, x0, bas, nel); cache = {}
    def E(dv):
        key = tuple(np.round(dv / h).astype(int))
        if key not in cache: cache[key] = E_at(els, x0 + dv, bas, nel)
        return cache[key]
    for i in range(n):
        ei = np.zeros(n); ei[i] = h
        Hs[i, i] = (E(ei) - 2 * E0 + E(-ei)) / h ** 2
        for j in range(i):
            ej = np.zeros(n); ej[j] = h
            Hs[i, j] = Hs[j, i] = (E(ei + ej) - E(ei - ej) - E(-ei + ej) + E(-ei - ej)) / (4 * h * h)
    return E0, Hs
def frekuensi(els, Hs):
    m = np.repeat([MASS[e] for e in els], 3); Hm = Hs / np.sqrt(np.outer(m, m))
    lam, vec = np.linalg.eigh(Hm)
    Eh = 4.3597447222071e-18; a0 = 5.29177210903e-11; amu = 1.66053906660e-27; c = 2.99792458e10
    w = np.sign(lam) * np.sqrt(np.abs(lam) * Eh / (a0 ** 2 * amu)) / (2 * np.pi * c)
    return w, vec
if __name__ == '__main__':
    basn = sys.argv[1]; R = float(sys.argv[2]); th = float(sys.argv[3])
    bas = {'sto': STO3G, '631gs': B631Gs}[basn]
    at = h2o(R, th); els = [a[0] for a in at]; x0 = np.array([c for a in at for c in a[1]], float)
    E0, Hs = hessian(els, x0, bas, 10); w, v = frekuensi(els, Hs)
    json.dump(dict(E0=E0, H=Hs.tolist(), w=w.tolist()), open(f'frek_{basn}.json', 'w'))
    print(E0, np.round(w, 1))

def proyeksi(els, x0, Hs):
    m = np.array([MASS[e] for e in els]); n = len(els); x = x0.reshape(n, 3)
    com = (m[:, None] * x).sum(0) / m.sum(); xc = x - com; sm = np.sqrt(np.repeat(m, 3))
    vecs = []
    for k in range(3):
        v = np.zeros((n, 3)); v[:, k] = 1; vecs.append((v.ravel() * sm))
    for k in range(3):
        ax = np.zeros(3); ax[k] = 1; v = np.cross(ax, xc); vecs.append(v.ravel() * sm)
    Q, _ = np.linalg.qr(np.array(vecs).T); keep = [i for i in range(Q.shape[1]) if np.linalg.norm(np.array(vecs).T[:, i]) > 1e-8]
    Q = Q[:, keep]; P = np.eye(3 * n) - Q @ Q.T
    Hm = Hs / np.outer(sm, sm); Hp = P @ Hm @ P
    lam, vec = np.linalg.eigh(Hp)
    Eh = 4.3597447222071e-18; a0 = 5.29177210903e-11; amu = 1.66053906660e-27; c = 2.99792458e10
    return np.sign(lam) * np.sqrt(np.abs(lam) * Eh / (a0 ** 2 * amu)) / (2 * np.pi * c), vec
