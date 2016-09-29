import numpy as np
import matplotlib.pyplot as plt

def period_ratio_hist(run_directory):
	f=open("%s/RawDataTransEQ.txt"%(run_directory), "w")
	f.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" %("Time", "Orbital_SeperationInner", "Orbital_SeperationOuter", "EccenI", "EccenO", "MassInner","MassOuter", "Res1", "Res2", "Res3","Pr"))
	myFileInner="%s/INNER.aei" %run_directory
	myFileOuter="%s/OUTER.aei" %run_directory
	Res1=[]
	Res2=[]
	Res3=[]
	periodratio=[]
	Time=np.loadtxt(myFileInner, skiprows=4, usecols=(0,))
	EccenI=np.loadtxt(myFileInner, skiprows=4, usecols=(2,))
	EccenO=np.loadtxt(myFileOuter, skiprows=4, usecols=(2,))
	MAI=np.loadtxt(myFileInner, skiprows=4, usecols=(6,))
	MAO=np.loadtxt(myFileOuter, skiprows=4, usecols=(6,))
	LoANI=np.loadtxt(myFileInner, skiprows=4, usecols=(5,))
	LoANO=np.loadtxt(myFileOuter, skiprows=4, usecols=(5,))
	AoPI=np.loadtxt(myFileInner, skiprows=4, usecols=(4,))
	AoPO=np.loadtxt(myFileOuter, skiprows=4, usecols=(4,))
	for line in range(len(MAI)-1):
		theta1=(MAI[line]+LoANI[line]+AoPI[line])-2*(MAO[line]+LoANO[line]+AoPO[line])+(LoANI[line]+AoPI[line])
		theta2=(MAI[line]+LoANI[line]+AoPI[line])-2*(MAO[line]+LoANO[line]+AoPO[line])+(LoANO[line]+AoPO[line])
		theta3=theta1-theta2
		Res1.append(theta1)
		Res2.append(theta2)
		Res3.append(theta3)
	Orbital_SeperationInner = np.loadtxt(myFileInner, skiprows=4, usecols=(1,))
	Orbital_SeperationOuter= np.loadtxt(myFileOuter, skiprows=4, usecols=(1,))
	MassInner=np.loadtxt(myFileInner, skiprows=4, usecols=(7,))
	MassOuter=np.loadtxt(myFileOuter, skiprows=4, usecols=(7,))
	for i in range(len(MassOuter)-1):
	    MassI=MassInner[i]
	    MassO=MassOuter[i]
	    Mstar=1
	    TMI=Mstar+MassI
	    TMO=Mstar+MassO
	    aI=Orbital_SeperationInner[i]
	    aO=Orbital_SeperationOuter[i]
	    Pi=((aI**3.0)/TMI)**(1.0/2.0)
	    Po=((aO**3.0)/TMO)**(1.0/2.0)
	    Pr=Po/Pi
	    f.write("%r\t%r\t%r\t%r\t%r\t%r\t%r\t%r\t%r\t%r\t%r\n" %(Time[i], Orbital_SeperationInner[i], Orbital_SeperationOuter[i], EccenI[i], EccenO[i], MassInner[i], MassOuter[i], Res1[i], Res2[i], Res3[i], Pr)) 
	f.close()
        
        
period_ratio_hist("/Users/sethkrantzler/Documents/PythonCodes/mercury6/Transition_Real")      
        
        
        
        