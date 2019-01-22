nTx = 1
nRx = 1
nSym = 10

src = Source(nTx)
chan = Channel(nTx, nRx)
rcv = Receiver(nRx)

for iSym in range(nSym):
	txSym = src.step
	rxSym = chan.step(txSym)
	demapped = rcv.step(rxSym)
	errCounter.step(txSym, demapped)

errCounter.print
