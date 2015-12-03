import random 
import numpy as np
import subprocess
import math

###initial condition lists###
a1=[.1 for i in range (50)] 
a2=[] 
MeanAnomaly1=[] 
Long1=[] 
AoP1=[]
MeanAnomaly2=[] 
Long2=[] 
AoP2=[]
Mass1=[.000005 for i in range (50)]
Mass2=[.00005 for i in range (50)]

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
	

i1=[]
i2=[]
for i in range (50): 
	i1.append(generate_uniform_cos(0, .1))
for i in range (50): 
	i2.append(generate_uniform_cos(0, .1))
Eccentricity1=[] 
for i in range (50):
    Eccentricity1.append(np.random.rayleigh(scale=.005, size=1)[0])

Eccentricity2=[]
for i in range (50):
    Eccentricity2.append(np.random.rayleigh(scale=.005, size=1)[0])

def calculate_period(m1, m2, a):
	P=((a**3.0)/(m1+m2))**(1.0/2.0)
	return P
	
def calculate_semimajor_axes(m1, m2, P):
	acubed=(P**2.0)*(m1+m2)
	a=acubed**(1.0/3.0)
	return a

#Pr=calculate_period(5.36000000E-05, 1, 1.56382711E-01)/calculate_period(5.75000000E-05, 1, 9.88615227E-02)
#print Pr,0

Pr=calculate_period(5.7000000E-05, 1, 1.46029631E-01)/calculate_period(2.02500000E-05, 1, 8.90363606E-02 )
print Pr,3000
	

for i in range (50):

    MeanAnomaly1.append(random.uniform(0,360.0)) 
    
for i in range (50):

    Long1.append(random.uniform(0,360.0))

for i in range (50):

    AoP1.append(random.uniform(0,360.0))
    

for i in range (50):

    MeanAnomaly2.append(random.uniform(0,360.0)) 
    
for i in range (50):

    Long2.append(random.uniform(0,360.0))

for i in range (50):

    AoP2.append(random.uniform(0,360.0))



def directory_maker(path,number):
	subprocess.call("mkdir %s" %(path), shell=True) 
	for i in range(number):
		subprocess.call("mkdir %s/RunP%r" %(path,i), shell=True) 


	
####File writing for Big.in
def bigin_creator(path, mass1, mass2, a1, a2, e1, e2, i1, i2, AoP1, LoAN1, MA1, AoP2, LoAN2, MA2):
	for i in range(50):
		f=open("%s/Run%r/big.in" %(path, i), "w")
		f.write(")O+_06 Big-body initial data  (WARNING: Do not delete this line!!)\n")
		f.write(")---------------------------------------------------------------------\n")
		f.write(" style (Cartesian, Asteroidal, Cometary) = Asteroidal\n")
		f.write(" epoch (in days) = 0.0\n")
		f.write(")---------------------------------------------------------------------\n")
		f.write("INNER m=%r r=3.D0 d=1.33\n"%(mass1[i]))
		f.write("%r %r %r %r %r %r\n"%(a1[i], e1[i], i1[i], AoP1[i], LoAN1[i], MA1[i]))
		f.write("0.0 0.0 0.0\n")
		f.write("OUTER m=%r r=3.D0 d=1.33\n"%(mass2[i]))
		f.write("%r %r %r %r %r %r\n"%(a2[i], e2[i], i2[i], AoP2[i], LoAN2[i], MA2[i]))
		f.write("0.0 0.0 0.0\n")
		f.close()
		print f

def table(run_directory,Mass1, Mass2, a1, a2, Eccentricity1, Eccentricity2, i1, i2, AoP1, Long1, MeanAnomaly1, AoP2, Long2, MeanAnomaly2): 
	r=open("%s/BigParam.txt"%run_directory, "w")
	r.write("Mass1\tMass2\ta1\ta2\tEccentricity1\tEccentricity2\ti1\ti2\tAoP1\tLong1\tMeanAnomaly1\tAoP2\tLong2\tMeanAnomaly2\n")
	for i in range(50):
		r.write("%r\t%r\t%r\t%r\t%r\t%r\t%r\t%r\t%r\t%r\t%r\t%r\t%r\t%r\t\n" %(Mass1[i], Mass2[i], a1[i], a2[i], Eccentricity1[i], Eccentricity2[i], i1[i], i2[i], AoP1[i], Long1[i], MeanAnomaly1[i], AoP2[i], Long2[i], MeanAnomaly2[i]))
	r.close()
"""	
for i in range(50):
	directory_maker("/Users/sethkrantzler/Documents/PythonCodes/mercury6/10MOcleanup/Run%r"%i, 100)
	
table("/Users/sethkrantzler/Documents/PythonCodes/mercury6/10MOcleanup", Mass1, Mass2, a1, a2, Eccentricity1, Eccentricity2, i1, i2, AoP1, Long1, MeanAnomaly1, AoP2, Long2, MeanAnomaly2)
bigin_creator('/Users/sethkrantzler/Documents/PythonCodes/mercury6/10MOcleanup', Mass1, Mass2, a1, a2, Eccentricity1, Eccentricity2, i1, i2, AoP1, Long1, MeanAnomaly1, AoP2, Long2, MeanAnomaly2)"""
