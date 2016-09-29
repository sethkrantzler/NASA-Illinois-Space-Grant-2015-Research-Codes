import numpy as np 
import matplotlib as plt 

def survivor_maker(run_directory, rangea, rangeb, rangec):
	for i,n,z in range(a), range(b), range(c):
		s=open("/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/Survivors.txt"%(i), "w")
		f=open("/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/RunP%r/PM%r.aei"%(i,n,z), "r")
		r=open("/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/RunP%r/INNER.aei"%(i,n), "r")
		if f.readlines()[-1].split()[0]==r.readlines()[-1].split()[0]:
			s.write(f.readlines()[1])
			
			