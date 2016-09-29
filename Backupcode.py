import numpy as np
import matplotlib.pyplot as plt

myFileTerry="/Users/sethkrantzler/Documents/PythonCodes/mercury6/TERRY.aei"
#myFigurea="/Users/sethkrantzler/Documents/PythonCodes/mercury6/T&J1.25Oa.jpeg"
myFileJermaine="/Users/sethkrantzler/Documents/PythonCodes/mercury6/JERMAINE.aei" 
myFigureb="/Users/sethkrantzler/Documents/PythonCodes/mercury6/T&J1.25Ob.jpeg" 
#myFigureq="/Users/sethkrantzler/Documents/PythonCodes/mercury6/T&J1.25Oq.jpeg" 

#Orbital_SeperationMars = np.loadtxt(myFileJermaine, skiprows=4, usecols=(1,)) 
TimeMars = np.loadtxt(myFileJermaine, skiprows=4, usecols=(0,)) 
#PericentreJermaine = np.loadtxt(myFileTerry, skiprows=4, usecols=(3,)) 
ApericentreJermaine= np.loadtxt(myFileTerry, skiprows=4, usecols=(4,))

#Orbital_SeperationVenus= np.loadtxt(myFileTerry, skiprows=4, usecols=(1,)) 
TimeVenus= np.loadtxt (myFileTerry, skiprows=4,usecols=(0,))
#PericentreTerry = np.loadtxt(myFileTerry, skiprows=4, usecols=(3,)) 
ApericentreTerry=np.loadtxt(myFileTerry, skiprows=4, usecols=(4,))

fig=plt.figure(1)
axes=fig.add_subplot(111)

line1=axes.plot(TimeMars, Orbital_SeperationMars)
line2=axes.plot(TimeVenus, Orbital_SeperationVenus)

plt.setp(line1, color="r", linewidth=1)
plt.setp(line2, color="y", linewidth=1)
axes.set_title("Orbital Seperation(AU) vs. Time (Years)") 
axes.grid()
axes.set_xlabel("Time(Years)")
axes.set_ylabel("Orbital Seperation(AU)") 
plt.subplot(2, 2, 1)
labels = ('Jermaine', 'Terry')
legend = plt.legend(labels, loc=(0.75, 0.965), labelspacing=0.1)
plt.setp(legend.get_texts(), fontsize='small')
    
plt.savefig(myFigurea) 
plt.close() 

line3=axes.plot(TimeMars, PericentreJermaine)
line4=axes.plot(TimeVenus, PericentreTerry) 

fig=plt.figure()
axes=fig.add_subplot(111)

plt.setp(line3, color="r", linewidth=1)
plt.setp(line4, color="y", linewidth=1)
axes.set_title("Pericentre(AU) vs. Time(Years)") 
axes.grid()
axes.set_xlabel("Time(Years)")
axes.set_ylabel("Pericentre(AU)") 
plt.subplot(2, 2, 1)
labels = ('Jermaine', 'Terry')
legend = plt.legend(labels, loc=(0.75, 0.965), labelspacing=0.1)
plt.setp(legend.get_texts(), fontsize='small')
 
plt.savefig(myFigureb) 
plt.close()


fig=plt.figure()
axes=fig.add_subplot(111)

line5=axes.plot(TimeMars, ApericentreJermaine)
line6=axes.plot(TimeVenus, ApericentreTerry) 

plt.setp(line5, color="r", linewidth=1)
plt.setp(line6, color="y", linewidth=1)
axes.set_title("Apocentre(AU) vs. Time(Years)") 
axes.grid()
axes.set_xlabel("Time(Years)")
axes.set_ylabel("Apocentre(AU)") 
plt.subplot(2, 2, 1)
axes.axis([0,7.0260370, 0,.15])
labels = ('Jermaine', 'Terry')
legend = plt.legend(labels, loc=(0.75, 0.965), labelspacing=0.1)
plt.setp(legend.get_texts(), fontsize='small')
 
plt.savefig(myFigureb) 
plt.close() 

print myFigureb


