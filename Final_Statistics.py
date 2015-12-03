import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def period_ratio_hist(run_directory, rangea, rangeb):
        Finalpratio=[]
        Initialpratio=[]
        PercentChange=[]
        myHistp="%s/PeriodRatioHist.jpeg"%run_directory
        myHistc="%s/PeriodRatioHistCumulative.jpeg"%run_directory
        myHistperc="%s/PeriodPercent.jpeg"%run_directory
        myScat="%s/PeriodScatter.jpeg"%run_directory
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
#			print InitialPr, FinalPr, PercentC
   	
	fig=plt.figure()
        axes=fig.add_subplot(111)
        axes.hist(Initialpratio, bins=200, range=[1.78, 2.08], histtype='step', stacked=False, fill=True, cumulative=True, color='red', alpha=0.5,label='P Ratio I')
        axes.hist(Finalpratio, bins=200, range=[1.78, 2.08], histtype='step', stacked=False, fill=False, cumulative=True, color='blue',label='P Ratio F')
        axes.set_title("Cumulative Histogram of Initial and Final Period Ratios Hybrid Runs")
        axes.legend(loc='upper left')
        axes.set_yscale('linear')
        axes.set_xscale('linear')
        plt.savefig(myHistc)
        plt.close()

	fig=plt.figure()
	axes=fig.add_subplot(111)
        axes.hist(Initialpratio, bins=30, range=[1.75, 2.05], histtype='step', stacked=False, fill=False, cumulative=False, color='red', alpha=1,label='P Ratio I')
        axes.hist(Finalpratio, bins=30, range=[1.75, 2.05], histtype='step', stacked=False, fill=True, cumulative=False, color='blue', alpha=0.4,label='P Ratio F')
        axes.set_title("Histogram of Initial and Final Period Ratios Hybrid Runs")
        axes.legend(loc='best')
        axes.set_yscale('linear')
        axes.set_xscale('linear')
	axes.set_ylim([0,20])
        plt.savefig(myHistp)
        plt.close()

""" fig=plt.figure()
        axes=fig.add_subplot(111)
        axes.hist(PercentChange, bins=100, histtype='step', stacked=False, fill=True, color='red', alpha=0.5)
        axes.set_title("Histogram of Difference of Final and Initial Period Ratio\n as a Percentage of Initial Period Ratio Hybrid Runs", fontsize=10)
        axes.set_yscale('linear')
        axes.set_xscale('linear')
        plt.savefig(myHistperc)
        plt.close()

        fig=plt.figure()
        axes=fig.add_subplot(111)
        axes.scatter(Initialpratio, Finalpratio, color="indigo")
        axes.set_title("Scatterplot of Initial Period Ratio vs. Final Period Ratio Hybrid Runs", fontsize=11)
        x=range(1,4)
        y=range(1,4)
        axes.plot(x,y)
        axes.plot((1.75,2.0),(2.0,2.0), color="red")
        axes.plot((2.0,2.0),(1.75,2.05), color="red")
        axes.set_xlim([1.75,2.08])
        axes.set_ylim([1.75,2.08])
        axes.set_xlabel("Initial Period Ratio")
        axes.set_ylabel("Final Period Ratio")
        plt.savefig(myScat)
        plt.close()
"""

period_ratio_hist("/projects/b1011/sethk/Hybrid_mid/Hybrid_runs", 50, 4)
period_ratio_hist("/projects/b1011/sethk/Real_Runs", 50, 4)
