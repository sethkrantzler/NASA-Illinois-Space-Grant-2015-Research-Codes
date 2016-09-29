import numpy as np
import matplotlib.pyplot as plt

myFileTerry="/Users/sethkrantzler/Documents/PythonCodes/mercury6/TERRY.aei"
myFigurea="/Users/sethkrantzler/Documents/PythonCodes/mercury6/TJ.13a.jpeg"
myFileJermaine="/Users/sethkrantzler/Documents/PythonCodes/mercury6/JERMAINE.aei" 

Orbital_SeperationMars = np.loadtxt(myFileJermaine, skiprows=4, usecols=(1,)) 
TimeMars = np.loadtxt(myFileJermaine, skiprows=4, usecols=(0,)) 
PericentreJermaine = np.loadtxt(myFileTerry, skiprows=4, usecols=(3,)) 
ApericentreJermaine= np.loadtxt(myFileTerry, skiprows=4, usecols=(4,))

Orbital_SeperationVenus= np.loadtxt(myFileTerry, skiprows=4, usecols=(1,)) 
TimeVenus= np.loadtxt (myFileTerry, skiprows=4,usecols=(0,))
PericentreTerry = np.loadtxt(myFileTerry, skiprows=4, usecols=(3,)) 
ApericentreTerry=np.loadtxt(myFileTerry, skiprows=4, usecols=(4,))

fig=plt.figure()
axes=fig.add_subplot(111)

line1=axes.plot(TimeMars, Orbital_SeperationMars)
line2=axes.plot(TimeVenus, Orbital_SeperationVenus)

plt.setp(line1, color="r", linewidth=1)
plt.setp(line2, color="y", linewidth=1)
axes.set_title("Orbital Seperation(AU) vs. Time (Years) for Jermaine at .13 AU") 
axes.grid()
axes.set_xlabel("Time(Years)")
axes.set_ylabel("Orbital Seperation(AU)") 
axes.axis 
labels=('Jermaine','Terry')
plt.legend(labels)

plt.savefig(myFigurea) 
plt.close() 

print myFigurea 

myFileTerry="/Users/sethkrantzler/Documents/PythonCodes/mercury6/TERRY.aei"
myFigureq="/Users/sethkrantzler/Documents/PythonCodes/mercury6/TJ.13q.jpeg"
myFileJermaine="/Users/sethkrantzler/Documents/PythonCodes/mercury6/JERMAINE.aei" 

Orbital_SeperationMars = np.loadtxt(myFileJermaine, skiprows=4, usecols=(1,)) 
TimeMars = np.loadtxt(myFileJermaine, skiprows=4, usecols=(0,)) 
PericentreJermaine = np.loadtxt(myFileJermaine, skiprows=4, usecols=(3,)) 
ApericentreJermaine= np.loadtxt(myFileJermaine, skiprows=4, usecols=(4,))

Orbital_SeperationVenus= np.loadtxt(myFileTerry, skiprows=4, usecols=(1,)) 
TimeVenus= np.loadtxt (myFileTerry, skiprows=4,usecols=(0,))
PericentreTerry = np.loadtxt(myFileTerry, skiprows=4, usecols=(3,)) 
ApericentreTerry=np.loadtxt(myFileTerry, skiprows=4, usecols=(4,))

fig=plt.figure()
axes=fig.add_subplot(111)

line1=axes.plot(TimeMars, PericentreJermaine)
line2=axes.plot(TimeVenus, PericentreTerry)

plt.setp(line1, color="r", linewidth=1)
plt.setp(line2, color="y", linewidth=1)
axes.set_title("Pericentre(AU) vs. Time (Years) for Jermaine at .13 AU") 
axes.grid()
axes.set_xlabel("Time(Years)")
axes.set_ylabel("Pericentre(AU)") 
axes.axis 
labels=('Jermaine','Terry')
plt.legend(labels)

plt.savefig(myFigureq) 
plt.close() 

print myFigureq  

myFileTerry="/Users/sethkrantzler/Documents/PythonCodes/mercury6/TERRY.aei"
myFigureb="/Users/sethkrantzler/Documents/PythonCodes/mercury6/TJ.13b.jpeg"
myFileJermaine="/Users/sethkrantzler/Documents/PythonCodes/mercury6/JERMAINE.aei" 

Orbital_SeperationMars = np.loadtxt(myFileJermaine, skiprows=4, usecols=(1,)) 
TimeMars = np.loadtxt(myFileJermaine, skiprows=4, usecols=(0,)) 
PericentreJermaine = np.loadtxt(myFileJermaine, skiprows=4, usecols=(3,)) 
ApericentreJermaine= np.loadtxt(myFileJermaine, skiprows=4, usecols=(4,))

Orbital_SeperationVenus= np.loadtxt(myFileTerry, skiprows=4, usecols=(1,)) 
TimeVenus= np.loadtxt (myFileTerry, skiprows=4,usecols=(0,))
PericentreTerry = np.loadtxt(myFileTerry, skiprows=4, usecols=(3,)) 
ApericentreTerry=np.loadtxt(myFileTerry, skiprows=4, usecols=(4,))

fig=plt.figure()
axes=fig.add_subplot(111)

line1=axes.plot(TimeMars, ApericentreJermaine)
line2=axes.plot(TimeVenus, ApericentreTerry)

plt.setp(line1, color="r", linewidth=1)
plt.setp(line2, color="y", linewidth=1)
axes.set_title("Apocentre(AU) vs. Time (Years) for Jermaine at .13 AU") 
axes.grid()
axes.set_xlabel("Time(Years)")
axes.set_ylabel("Apocentre(AU)") 
labels=('Jermaine','Terry')
plt.legend(labels)

plt.savefig(myFigureb) 
plt.close()  
print myFigureb

