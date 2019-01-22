#!/usr/bin/python3
import numpy as np

class Channel:
    def __init__(self, nTx, nRx):
        self.nRx = nRx
        self.nTx = nTx
        self.generateH()

    def step(self, txSym):
        self.generateH()
        return np.dot(self.H, txSym)

    def generateH(self):
        self.H = np.random.randn(self.nRx, self.nTx) * np.sqrt(0.5) + \
            1.j * np.random.randn(self.nRx, self.nTx) * np.sqrt(0.5)

        return self.H


if __name__ == '__main__':
    chan = Channel(2, 3)
    print("First set of channel matrix:")
    H = chan.generateH()
    print(H)
    print("Second set of channel matrix:")
    H = chan.generateH()
    print(H)

    sym = np.array([1. + 1.j, -1. + 1.j]) / np.sqrt(2.)
    print("Input sym:")
    print(sym)
    print("Channel output:")
    print(chan.step(sym))
    print("channel:")
    print(chan.H)
