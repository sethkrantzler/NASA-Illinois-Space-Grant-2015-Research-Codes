import numpy as np
import matplotlib.pyplot as plt

myFile="/Users/sethkrantzler/Documents/PythonCodes/mercury6/Anomaly_Runs/anomalydata.txt"
myFigureall="/Users/sethkrantzler/Documents/PythonCodes/mercury6/Anomaly_Runs/anomalycrash.jpeg"

Anomaly = np.loadtxt(myFile, usecols=(0,)) 
Time = np.loadtxt(myFile, usecols=(1,)) 

fig=plt.figure()
axes=fig.add_subplot(111)

plt.scatter(Time, Anomaly, marker="o")
axes.set_title("Anomaly(Degrees) Vs. Time of Binary System(Years) for Jermaine at .125 AU ") 
axes.grid()
axes.set_xlabel("Time(Years)")
axes.set_ylabel("Anomaly(Degrees)") 
plt.savefig(myFigureall) 
plt.close()  

print myFigureall