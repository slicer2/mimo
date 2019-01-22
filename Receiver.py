#!/usr/bin/python3
import numpy as np

class Receiver:
    def __init__(self, nRx, N0, modOrd):
        self.nRx = nRx
        self.N0 = N0
        self.modOrd = modOrd
        self.modSyms = getModSym(modOrd)

    def step(self, rxSym, H = None, method = 'MMSE'):
        noise = cplxRandn(rxSym.shape, self.N0)
        rx = rxSym + noise

        if method == 'MMSE':
            assert (not H == None)
            M = hermitian(H) @ np.linalg.inv(H @ hermitian(H) + eye(H.shape[0]) * self.N0)
            est = M * y
            return slice(est, self.modSyms)

