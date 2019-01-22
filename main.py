from source import Source
from chan import Channel
from receiver import Receiver
from errorcounter import ErrorCounter

nTx = 1
nRx = 1
modOrd = 2
N0 = 1e-1
nSym = 100

src = Source(nTx, modOrd)
chan = Channel(nTx, nRx)
rcv = Receiver(nRx, modOrd, N0)
errCounter = ErrorCounter()

for iSym in range(nSym):
    txSym = src.step()
    #print(txSym)
    rxSym = chan.step(txSym)
    #print(rxSym)
    #print(chan.H)
    demapped = rcv.step(rxSym, chan.H, 'MMSE')
    errCounter.step(txSym, demapped)

errCounter.print()
