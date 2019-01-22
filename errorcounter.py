import numpy as np

class ErrorCounter:
    def __init__(self):
        self.symErrCount = 0
        self.symCount = 0

    def step(self, txSym, rxSym):
        self.symCount += len(txSym)
        self.symErrCount += np.sum(txSym != rxSym)

    def print(self):
        print("syms received : ", self.symCount)
        print("errs          : ", self.symErrCount)
        print("sym error rate: ", float(self.symErrCount) / self.symCount)

if __name__ == '__main__':
    errCounter = ErrorCounter()
    txSym = np.array([1., -1.])
    rxSym = np.array([1., 1.])
    errCounter.step(txSym, rxSym)
    errCounter.print()
