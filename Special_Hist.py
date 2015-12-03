import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
    
def get_weights(Pratioarray, BINNO=50):
	RANGE = [np.min(Pratioarray), np.max(Pratioarray)]
	hist, binedges = np.histogram(Pratioarray, range=RANGE, bins=BINNO, density=True)
	return hist, binedges

def get_normalized_histograms(run_directory, rangea, rangeb, RANGE=[1.7, 2.2], BINNO=50, PLOTFILENAME='test.pdf'):
	Finalpratio=[]
	Initialpratio=[]
	PercentChange=[]
	for i in range(rangea):
    		for z in range(rangeb):
        	myFileInner="%s/Run%r/RunP%r/INNER.aei"%(run_directory, i, z)
			myFileOuter="%s/Run%r/RunP%r/OUTER.aei"%(run_directory, i, z)
			Orbital_SeperationInner = np.loadtxt(myFileInner, skiprows=4, usecols=(1,))
			Orbital_SeperationOuter= np.loadtxt(myFileOuter, skiprows=4, usecols=(1,))
			MassInner=np.loadtxt(myFileInner, skiprows=4, usecols=(7,))
			MassOuter=np.loadtxt(myFileOuter, skiprows=4, usecols=(7,))
			MassIi=MassInner[0]
			MassOi=MassOuter[0]
            MassIf=MassInner[len(MassInner)-1]
            MassOf=MassOuter[len(MassOuter)-1]
            Mstar=1
            TMII=Mstar+MassIi
            TMOI=Mstar+MassOi
            TMIF=Mstar+MassIf
            TMOF=Mstar+MassOf
            aIi=Orbital_SeperationInner[0]
            aOi=Orbital_SeperationOuter[0]
            aIf=Orbital_SeperationInner[len(Orbital_SeperationInner)-1]
        	aOf=Orbital_SeperationOuter[len(Orbital_SeperationOuter)-1]
       		InitialPi=((aIi**3.0)/TMII)**(1.0/2.0)
     		InitialPo=((aOi**3.0)/TMOI)**(1.0/2.0)
        	InitialPr=InitialPo/InitialPi
            FinalPi=((aIf**3.0)/TMIF)**(1.0/2.0)
        	FinalPo=((aOf**3.0)/TMOF)**(1.0/2.0)
        	FinalPr=FinalPo/FinalPi
        	PercentC=(FinalPr-InitialPr)/InitialPr
            if FinalPr>0:
                Initialpratio.append(InitialPr)
                Finalpratio.append(FinalPr)
                PercentChange.append(PercentC)

	hist, binedges = get_weights(Initialpratio, BINNO=50)
	w = []
	Ratioini, Ratiofin = [], []
	for i in range(len(Initialpratio)):
		try:
			for j in range(len(binedges)-1):
				if Initialpratio[i] <= binedges[j+1] and Initialpratio[i] > binedges[j]:
					w.append(1./hist[j])
					Ratioini.append(Initialpratio[i])
					Ratiofin.append(Finalpratio[i])
					raise StopIteration()
		except StopIteration:
			print 'Found Pini', i, 'weight', hist[j]
			pass
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.hist(Ratioini, range=[1.7, 2.2], bins=50, weights=w, normed=True, histtype='step', color='red', fill=False, lw=1)
	ax.hist(Ratiofin, range=[1.7, 2.2], bins=50, weights=w, normed=True, histtype='step', color='blue', fill=True, alpha=.6, lw=1)
	ax.set_xlabel(r'$P_2/P_1$', size=16)
	ax.set_ylabel(r'$\rm{pdf}$', size=16)
	plt.savefig(PLOTFILENAME)
	plt.show()


get_normalized_histograms(PLOTFILENAME="/projects/b1011/sethk/Hybrid_mid/Hybrid_runs/PeriodRatioHist.jpeg", run_directory="/projects/b1011/sethk/Hybrid_mid/Hybrid_runs",rangea=50, rangeb=4)	
