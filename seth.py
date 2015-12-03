import numpy as np
import matplotlib.pyplot as plt

def get_weights(Pratioarray, BINNO=50):
	RANGE = (np.min(Pratioarray), np.max(Pratioarray))
	hist, binedges = np.histogram(Pratioarray, range=RANGE, bins=BINNO, density=False)
	return hist, binedges

def get_normalized_histograms(Pratioinitial, Pratiofinal, BINNO=10, PLOTFILENAME='test.pdf'):
	hist, binedges = get_weights(Pratioinitial, BINNO=BINNO)
	RANGE = (np.min(Pratioinitial), np.max(Pratioinitial))
	w = []
	Ratioini, Ratiofin = [], []
	for i in range(len(Pratioinitial)):
		try:
			for j in range(len(binedges)-1):
				if Pratioinitial[i] <= binedges[j+1] and Pratioinitial[i] > binedges[j]:
					w.append(1./hist[j])
					Ratioini.append(Pratioinitial[i])
					Ratiofin.append(Pratiofinal[i])
					raise StopIteration()
		except StopIteration:
			print 'Found Pini', i, 'weight', hist[j]
			pass
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.hist(Ratioini, range=RANGE, bins=BINNO, weights=w, normed=True, histtype='step', color='red', ls='dotted', lw=1)
	ax.hist(Ratiofin, range=RANGE, bins=BINNO, weights=w, normed=True, histtype='step', color='blue', ls='solid', lw=1)
	ax.set_xlabel(r'$P_2/P_1$', size=16)
	ax.set_ylabel(r'$\rm{pdf}$', size=16)
	plt.savefig(PLOTFILENAME)
	plt.show()
	
def get_diff(Pratioinitial, Pratiofinal, BINNO=15, PLOTFILENAME='test1.pdf'):
	RANGE = (np.min(Pratioinitial), np.max(Pratioinitial))
	histini, binedgesini = np.histogram(Pratioinitial, bins=BINNO, range=RANGE)
	histfin, binedgesfin = np.histogram(Pratiofinal, bins=BINNO, range=RANGE)
	binmids = []
	for i in range(len(binedgesini)-1):
		binmids.append((binedgesini[i+1]+binedgesini[i])/2.)
	histdiff = histfin - histini
	plt.plot(binmids, histdiff)
	plt.show()
			
