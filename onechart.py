import numpy as np
import matplotlib.pyplot as plt

myFileInner="/projects/b1011/sethk/Hybrid_mid/Hybrid_runs/Run45/RunP3/INNER.aei"
myFigureall="/projects/b1011/sethk/Hybrid_mid/Hybrid_runs/Run45/RunP3/OrbitalProperties.jpeg"
myFileOuter="/projects/b1011/sethk/Hybrid_mid/Hybrid_runs/Run45/RunP3/OUTER.aei" 

Orbital_SeperationMars = np.loadtxt(myFileOuter, skiprows=4, usecols=(1,)) 
TimeMars = np.loadtxt(myFileOuter, skiprows=4, usecols=(0,)) 
EccentricityOuter=(myFileOuter, skiprows=4, usecols=(2,))
PericentreJermaine = Orbital_SeperationMars*(1-EccentricityOuter)
ApericentreJermaine= Orbital_SeperationMars*(1+EccentricityOuter)

Orbital_SeperationVenus= np.loadtxt(myFileInner, skiprows=4, usecols=(1,)) 
TimeVenus= np.loadtxt (myFileInner, skiprows=4,usecols=(0,))
EccentricityInner=(myFileInner, skiprows=4, usecols=(2,))
PericentreTerry = Orbital_SeperationVenus*(1-EccentricityInner) 
ApericentreTerry= Orbital_SeperationVenus*(1+EccentricityInner) 

fig=plt.figure()
axes=fig.add_subplot(111)

line1=ax.plot(TimeMars, Orbital_SeperationMars,label="a")
line2=ax.plot(TimeVenus, Orbital_SeperationVenus, label="a")
line3=ax.plot(TimeMars, PericentreJermaine,label="q")
line4=ax.plot(TimeVenus, PericentreTerry,label="q")
line5=ax.plot(TimeMars, ApericentreJermaine, label="Q")
line6=ax.plot(TimeVenus, ApericentreTerry, label="Q")

plt.setp(line1, color="r", linewidth=.7)
plt.setp(line2, color="b", linewidth=.7)
plt.setp(line3, color="r", linewidth=.3)
plt.setp(line4, color="b", linewidth=.3) 
plt.setp(line5, color="r", linewidth=.5)
plt.setp(line6, color="b", linewidth=.5) 


plt.savefig(myFigureall) 
plt.close() 

print myFigureall
