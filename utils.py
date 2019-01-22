#!/usr/bin/python3
import numpy as np

def getModSym(modOrd):
    if modOrd == 1:
        return np.array([-1, 1])

    if modOrd == 2:
        d1 = np.array([-1, 1])
        syms = np.add.outer(d1, 1j * d1)
        syms = syms / np.linalg.norm(syms, 'fro') * np.sqrt(2**modOrd)
        return syms.ravel()

    if modOrd == 4:
        d1 = np.array([-3, -1, 1, 3])
        syms = np.add.outer(d1, 1j * d1)
        syms = syms / np.linalg.norm(syms, 'fro') * np.sqrt(2**modOrd)
        return syms.ravel()

def cplxRandn(sz, var):
    """ generate complex random matrix """
    return np.random.randn(*sz) * np.sqrt(var / 2.) + \
        1.j * np.random.randn(*sz) * np.sqrt(var / 2.)

def hermitian(arr):
    return np.transpose(np.conj(arr))

def slice(est, modSyms):
    d = np.abs(np.subtract.outer(est, modSyms))
    #print(d)
    return modSyms[np.argmin(d, 1)]

if __name__ == '__main__':
    print("mod order = 1:")
    print(getModSym(1))
    print("mod order = 2:")
    print(getModSym(2))
    print("mod order = 4:")
    print(getModSym(4))
    print("generate 2x3 complex Gaussian of unit variance:")
    print(cplxRandn((2, 3), 1))
    print("Estimate variance from complex Gaussian:")
    print(np.linalg.norm(cplxRandn((1000, 2), 1), 'fro') ** 2 / 2000.)
    print("Hermitian of")
    H = cplxRandn((2, 3), 1.)
    print(H)
    print("is:")
    print(hermitian(H))

    modSyms = getModSym(2)
    print("mod syms:")
    print(modSyms)

    syms = cplxRandn((4,), 1)
    print("slice")
    print(syms)
    print(slice(syms, modSyms))
