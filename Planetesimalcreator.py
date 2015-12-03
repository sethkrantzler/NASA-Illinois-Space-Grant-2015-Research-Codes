from scipy.stats import powerlaw
import matplotlib.pyplot as plt
import numpy as np
import math
import random


def generate_power(power_law, low, high):
    y = np.random.uniform(0., 1.)
    alpha = power_law+1.
    if power_law==0.:
        x = np.random.uniform(low, high)
    elif power_law==-1.:
        norm = np.log(high/low) 
        x = low * np.exp( y*np.log(high/low) ) 
    else:
        norm = (high/low)**alpha - 1.
        x = low * ( norm*y + 1. ) ** (1./alpha)
    return x 
    




def generate_uniform_cos(low, high):
	low_radian, high_radian = low*np.pi/180., high*np.pi/180.
	low_cos, high_cos = np.cos(low_radian), np.cos(high_radian)
	y = np.random.uniform(0., 1.)
	theta = math.acos( low_cos + y*(high_cos - low_cos) )
	sign = np.random.random_integers(0,1)
	if sign == 1:
		i = theta*180./np.pi
	else:
		i = - theta*180./np.pi
	return i
	

		
	
####File writing for small.in
def smallin_creator(RUNDIRECTORY, SMALLFILE, LineI, LineF):
		f=open("%s/small.in" %(RUNDIRECTORY), "w")
		r=open('%s'%SMALLFILE, "r")
		Smalllines=r.readlines()
		f.write(")O+_06 Small-body initial data  (WARNING: Do not delete this line!!)\n")
		f.write(")---------------------------------------------------------------------\n")
		f.write(" style (Cartesian, Asteroidal, Cometary) = Asteroidal\n")
		f.write(")---------------------------------------------------------------------\n")
		for value in range(LineI,LineF):
			f.write(Smalllines[value])			
		f.close()
		r.close()
			
			
	
	


def create_planetesimals(N=20000, SEED=100, MASS=1e-39, WRITEFILENAME='planetesimal_properties.txt', run=0):
	np.random.seed(SEED)
	writefile = open(WRITEFILENAME, 'w')
	biginput="/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupuniform/BigParam.txt"
	a=[]
	e=[]
	inc=[]
	LoAN=[]
	MA=[]
	AoP=[] 
	mass=MASS
	a0=np.loadtxt(biginput, skiprows=1, usecols=(2,)) 
	a1=np.loadtxt(biginput, skiprows=1, usecols=(3,)) 
	amin=a0[run]*((1./3.)**(2./3.))
	amax=a1[run]*((3.)**(2./3.))
	for i in range(N):
		a.append(generate_power(-2.5, amin, amax))
		e.append(np.random.rayleigh(scale=.05, size=1)[0])
		inc.append(generate_uniform_cos(0, .1))
		MA.append(random.uniform(0,360.0))
		LoAN.append(random.uniform(0,360.0))
		AoP.append(random.uniform(0,360.0))
		writefile.write("PM%r ep=0 m=%g\n%r %r %r %r %r %r 0 0 0\n"%(i, mass, a[i], e[i], inc[i], AoP[i], LoAN[i], MA[i]))
	writefile.close()
	
for i in range(50):
	create_planetesimals(N=20000, SEED=i, MASS=1e-39, WRITEFILENAME='/Users/sethkrantzler/Documents/PythonCodes/mercury6/10MOcleanup/Run%r/SmallParam.txt'%i, run=i)



def smallin_runs(RUNDIRECTORY, SMALLFILE):
	LineI=0
	LineF=400
	for z in range(100):
		smallin_creator("%s/RunP%r"%(RUNDIRECTORY,z),"%s" %SMALLFILE, LineI, LineF)
		LineI=LineI+400
		LineF=LineF+400
		if LineF>40000:
			break
		
for i in range(50):
	smallin_runs("/Users/sethkrantzler/Documents/PythonCodes/mercury6/10MOcleanup/Run%r"%i, '/Users/sethkrantzler/Documents/PythonCodes/mercury6/10MOcleanup/Run%r/SmallParam.txt'%i)
		









