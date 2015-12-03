import numpy as np
import matplotlib.pyplot as plt


for i in range(50):
	myFileInner="/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/INNER.aei"%i
	myFigureall="/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/StabilityCheck/Run%rStability.jpeg"%i
	myFileOuter="/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/OUTER.aei"%i
	Orbital_SeperationMars = np.loadtxt(myFileInner, skiprows=4, usecols=(1,)) 
	TimeMars = np.loadtxt(myFileInner, skiprows=4, usecols=(0,)) 
	PericentreJermaine = np.loadtxt(myFileInner, skiprows=4, usecols=(4,)) 
	EccentricityInner= np.loadtxt(myFileInner, skiprows=4, usecols=(2,)) 
	ApericentreInner=(1+EccentricityInner)*Orbital_SeperationMars
	
	Orbital_SeperationVenus= np.loadtxt(myFileOuter, skiprows=4, usecols=(1,)) 
	TimeVenus= np.loadtxt (myFileOuter, skiprows=4,usecols=(0,))
	PericentreTerry = np.loadtxt(myFileOuter, skiprows=4, usecols=(4,)) 
	EccentricityOuter= np.loadtxt(myFileOuter, skiprows=4, usecols=(2,)) 
	ApericentreOuter=(1+EccentricityOuter)*Orbital_SeperationVenus
	
	fig=plt.figure()
	axes=fig.add_subplot(111)

	line1=axes.plot(TimeMars, Orbital_SeperationMars,label="Inner a")
	line2=axes.plot(TimeVenus, Orbital_SeperationVenus, label="Outer a")
	line3=axes.plot(TimeMars, PericentreJermaine,label="Inner q")
	line4=axes.plot(TimeVenus, PericentreTerry,label="Outer q")
	line5=axes.plot(TimeMars, ApericentreInner, label="Inner Q")
	line6=axes.plot(TimeVenus, ApericentreOuter, label="Outer Q")

	plt.setp(line1, color="r", linewidth=.7)
	plt.setp(line2, color="b", linewidth=.7)
	plt.setp(line3, color="r", linewidth=.5)
	plt.setp(line4, color="b", linewidth=.5) 
	plt.setp(line5, color="r", linewidth=.3)
	plt.setp(line6, color="b", linewidth=.3) 
	

	axes.set_title("Distance(AU) Vs. Time(Years) for Run %r"%i) 
	axes.grid()
	axes.legend(loc='best')
	axes.set_xlabel("Time(Years)")
	axes.set_ylabel("Distance(AU)") 
	plt.savefig(myFigureall) 
	plt.close() 
	
Initialpratio=[]
Finalpratio=[] 
ei=[]
ef=[]
myHiste="/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/StabilityCheck/EccentricityStability.jpeg"
myHistp="/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/StabilityCheck/PratioStability.jpeg"

for n in range(50):
	myFileInner="/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/INNER.aei"%n
	myFileOuter="/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/OUTER.aei"%n
	EccentricityInner= np.loadtxt(myFileInner, skiprows=4, usecols=(2,)) 
	EccentricityOuter= np.loadtxt(myFileOuter, skiprows=4, usecols=(2,))
	Orbital_SeperationInner = np.loadtxt(myFileInner, skiprows=4, usecols=(1,)) 
	Orbital_SeperationOuter= np.loadtxt(myFileOuter, skiprows=4, usecols=(1,))
	Initialpratio.append((Orbital_SeperationOuter[0]**(3.0/2.0))/(Orbital_SeperationInner[0]**(3.0/2.0)))
	Finalpratio.append((Orbital_SeperationOuter[len(Orbital_SeperationOuter)-1]**(3.0/2.))/(Orbital_SeperationInner[len(Orbital_SeperationInner)-1]**(3.0/2.0)))
	ei.append(EccentricityInner[0])
	ei.append(EccentricityOuter[0])
	ef.append(EccentricityInner[len(EccentricityInner)-1])
	ef.append(EccentricityOuter[len(EccentricityOuter)-1])

fig=plt.figure()
axes=fig.add_subplot(111)


bins = 20
axes.hist([ei,ef], bins=bins, range=[0, .015], histtype='bar', stacked=False, fill=True, color=['burlywood', 'blue'],
                            label=['Eccen. I', 'Eccen. F'])
axes.set_title("Histogram of Initial and Final Eccentricities") 
axes.legend(loc='best')
axes.set_yscale('linear')
axes.set_xscale('linear') 
plt.savefig(myHiste) 
plt.close() 

fig=plt.figure()
axes=fig.add_subplot(111)
MIN=1.8
MAX=2

bins = 20
axes.hist([Initialpratio,Finalpratio], bins=bins, range=[1.8, 2.0], histtype='bar', stacked=False, fill=True, color=['burlywood', 'blue'],
                            label=['P Ratio I', 'P Ratio F'])
axes.set_title("Histogram of Initial and Final Period Ratios") 
axes.legend(loc='best')
axes.set_yscale('linear')
axes.set_xscale('linear') 
plt.savefig(myHistp) 
plt.close()