import numpy as np
import utils

class Source:
    def __init__(self, nTx, modOrd):
	    self.nTx = nTx
	    self.modOrd = modOrd
	    self.modSyms = utils.getModSym(modOrd)

    def step(self, precoding = 1):
        return np.dot(precoding, self.modSyms[np.random.randint(0, 2**self.modOrd, self.nTx)])


if __name__ == '__main__':
    src = Source(2, 2)
    print("First Tx symbols:")
    s = src.step()
    print(s)
    print("Second Tx symbols:")
    s = src.step()
    print(s)
