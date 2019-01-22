#!/usr/bin/python3
import numpy as np
import utils


class Receiver:
    def __init__(self, nRx, modOrd, N0):
        self.nRx = nRx
        self.N0 = N0
        self.modOrd = modOrd
        self.modSyms = utils.getModSym(modOrd)

    def step(self, rxSym, H = None, method = 'MMSE'):
        noise = utils.cplxRandn(rxSym.shape, self.N0)
        rx = rxSym + noise

        if method == 'MMSE':
            assert (H != None)
            M = np.dot(utils.hermitian(H), np.linalg.inv(np.dot(H, utils.hermitian(H)) + np.eye(H.shape[0]) * self.N0))
            est = np.dot(M, rx)
            return utils.slice(est, self.modSyms)

if __name__ == '__main__':
    rcv = Receiver(3, 2, 1e-7)
    import source
    import chan
    src = source.Source(2, 2)
    chan = chan.Channel(2, 3)
    txSyms = src.step()
    rxSyms = chan.step(txSyms)
    demapped = rcv.step(rxSyms, chan.H, 'MMSE')
    print("Tx symbols:")
    print(txSyms)
    print("demapped symbols:")
    print(demapped)
