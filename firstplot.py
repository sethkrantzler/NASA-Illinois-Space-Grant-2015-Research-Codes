import numpy as np
import matplotlib.pyplot as plt

myFileMars="/Users/sethkrantzler/Documents/PythonCodes/mercury6/MARS.aei"
myFigure="/Users/sethkrantzler/Documents/PythonCodes/mercury6/myFigure.ps"
myFileVenus="/Users/sethkrantzler/Documents/PythonCodes/mercury6/VENUS.aei" 

Orbital_SeperationMars = np.loadtxt(myFileMars, skiprows=4, usecols=(1,)) 
TimeMars = np.loadtxt(myFileMars, skiprows=4, usecols=(0,)) 

Orbital_SeperationVenus= np.loadtxt(myFileVenus, skiprows=4, usecols=(1,)) 
TimeVenus= np.loadtxt (myFileVenus, skiprows=4,usecols=(0,))

fig=plt.figure()
axes=fig.add_subplot(111)

line1=axes.plot(TimeMars, Orbital_SeperationMars)
line2=axes.plot(TimeVenus, Orbital_SeperationVenus)

plt.setp(line1, color="r", )
plt.setp(line2, color="y", )
axes.set_title("Orbital Seperation of the Solar System vs. Time (Years)") 
axes.grid()
axes.set_xlabel("Time(Years)")
axes.set_ylabel("Orbital Seperation") 
axes.axis([0,1220000.0,.3,1.6])
axes.text(1200000.0,.8, 'Venus',
        verticalalignment='bottom', horizontalalignment='right',
        color='yellow', fontsize=15) 
axes.text(1200000.0,1.2, 'Mars',
        verticalalignment='bottom', horizontalalignment='right',
        color='Red', fontsize=15)

 
plt.savefig(myFigure) 
plt.close()

print myFigure
