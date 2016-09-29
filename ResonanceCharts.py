import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
"""
def period_ratio_hist(run_directory, rangea, rangeb):
        for i in range(rangea):
                for z in range(rangeb):
                        myFileInner="%s/Run%r/RunP%r/INNER.aei"%(run_directory, i, z)
                        myFileOuter="%s/Run%r/RunP%r/OUTER.aei"%(run_directory, i, z)
                        ResPlot="%s/Run%r/RunP%r/ResonanceAngles_Run%rP%r.pdf"%(run_directory, i, z, i, z)
                        Res1=[]
                        Res2=[]
                        Time=np.loadtxt(myFileInner, skiprows=4, usecols=(0,))
                        MAI=np.loadtxt(myFileInner, skiprows=4, usecols=(6,))
                        MAO=np.loadtxt(myFileOuter, skiprows=4, usecols=(6,))
                        LoANI=np.loadtxt(myFileInner, skiprows=4, usecols=(5,))
                        LoANO=np.loadtxt(myFileOuter, skiprows=4, usecols=(5,))
                        AoPI=np.loadtxt(myFileInner, skiprows=4, usecols=(4,))
                        AoPO=np.loadtxt(myFileOuter, skiprows=4, usecols=(4,))
                        for line in range(len(MAI)-1):
							theta1=(MAI[line]+LoANI[line]+AoPI[line])-2*(MAO[line]+LoANO[line]+AoPO[line])+(LoANI[line]+AoPI[line])
							theta2=(MAI[line]+LoANI[line]+AoPI[line])-2*(MAO[line]+LoANO[line]+AoPO[line])+(LoANO[line]+AoPO[line])
							Res1.append(theta1)
							Res2.append(theta2)
							
						fig=plt.figure()
        				axes=fig.add_subplot(111)
        				axes.scatter(Time, Res1, color="indigo", markersize=.5, label="$\Theta$1")
        				axes.scatter(Time, Res2, color="red", markersize=.5, label="$\Theta$2")
        				axes.set_title("Resonance Angles for Run %r P%r"%(i,z))
        				axes.set_xlabel("Time (Years)")
        				axes.set_ylabel("Degrees")
						plt.savefig(ResPlot)
						plt.close()"""


myOrbits="/Users/sethkrantzler/Documents/PythonCodes/mercury6/Transition_10MO/OrbitalResClarity.pdf"
myFileInner="/Users/sethkrantzler/Documents/PythonCodes/mercury6/Transition_10MO/INNER.aei"
myFileOuter="/Users/sethkrantzler/Documents/PythonCodes/mercury6/Transition_10MO/OUTER.aei"
ResPlot="/Users/sethkrantzler/Documents/PythonCodes/mercury6/Transition_10MO/ResAnglesClarity10MO.pdf"
Res1=[]
Res2=[]
TimeI=np.loadtxt(myFileInner, skiprows=4, usecols=(0,))
MAI=np.loadtxt(myFileInner, skiprows=4, usecols=(6,))
MAO=np.loadtxt(myFileOuter, skiprows=4, usecols=(6,))
LoANI=np.loadtxt(myFileInner, skiprows=4, usecols=(5,))
LoANO=np.loadtxt(myFileOuter, skiprows=4, usecols=(5,))
AoPI=np.loadtxt(myFileInner, skiprows=4, usecols=(4,))
AoPO=np.loadtxt(myFileOuter, skiprows=4, usecols=(4,))

for line in range(len(MAI)):
	thetaone=(MAI[line]+LoANI[line]+AoPI[line])-2*(MAO[line]+LoANO[line]+AoPO[line])+(LoANI[line]+AoPI[line])
	thetatwo=(MAI[line]+LoANI[line]+AoPI[line])-2*(MAO[line]+LoANO[line]+AoPO[line])+(LoANO[line]+AoPO[line])
	theta1=np.mod(thetaone,360) - 180
	theta2=np.mod(thetatwo,360) - 180
	Res1.append(theta1)
	Res2.append(theta2)
	
	
							
fig=plt.figure()
axes=fig.add_subplot(111)
ax=fig.add_subplot(111)
axes.plot(TimeI, Res1, color="indigo", linewidth=.5, linestyle="none", marker='.', markersize=1, label="$\Theta$1")
axes.plot(TimeI, Res2, color="red", linewidth=.25, linestyle="none", label="$\Theta$2", marker='.', markersize=1, alpha=1)
axes.set_title("Resonance Angles for Clarity Run 10MO")
axes.set_xlabel("Time (Years)")
axes.set_ylabel("Degrees")
plt.savefig(ResPlot)
plt.close()