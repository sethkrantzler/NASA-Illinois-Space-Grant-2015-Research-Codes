import numpy as np 
import random 
import subprocess 

def bigin_creator(run_directory, cleanup_directory, rangea, number_runs):
	for i in range(rangea):
		p1=open("%s/Run%r/RunP0/INNER.aei" %(cleanup_directory, i), "r")
		p2=open("%s/Run%r/RunP0/OUTER.aei" %(cleanup_directory, i), "r")
		lastline1=p1.readlines()[-1]
		lastline2=p2.readlines()[-1]
		mass1=lastline1.split()[7]
		mass2=lastline2.split()[7]
		a1=lastline1.split()[1]
		a2=lastline2.split()[1]
		e1=lastline1.split()[2]
		e2=lastline2.split()[2]
		i1=lastline1.split()[3]
		i2=lastline2.split()[3]
		AoP1=lastline1.split()[4]
		AoP2=lastline2.split()[4]
		LoAN1=lastline1.split()[5]
		LoAN2=lastline2.split()[5]
		MA1=lastline1.split()[6]
		MA2=lastline2.split()[6]
		for n in range(number_runs):
			f=open("%s/Run%r/RunP%r/big.in" %(run_directory, i, n), "w")
			f.write(")O+_06 Big-body initial data  (WARNING: Do not delete this line!!)\n")
			f.write(")---------------------------------------------------------------------\n")
			f.write(" style (Cartesian, Asteroidal, Cometary) = Asteroidal\n")
			f.write(" epoch (in days) = 0.0\n")
			f.write(")---------------------------------------------------------------------\n")
			f.write("INNER m=%r r=3.D0 d=1.33\n"%(mass1))
			f.write("%r %r %r %r %r %r\n"%(a1, e1, i1, AoP1, LoAN1, MA1))
			f.write("0.0 0.0 0.0\n")
			f.write("OUTER m=%r r=3.D0 d=1.33\n"%(mass2))
			f.write("%r %r %r %r %r %r\n"%(a2, e2, i2, AoP2, LoAN2, MA2))
			f.write("0.0 0.0 0.0\n")
			f.close()
		

def smallin_creator(run_directory, cleanup_directory, smallfile, rangea, samplesize, mass, number_runs):
	np.random.seed(35)
	for i in range(rangea):
		r=open('%s/Run%r/%s'%(cleanup_directory, i, smallfile), "r")
		All_ptsmals=r.readlines()
		for z in range(numbers_runs):
			f=open("%s/Run%r/RunP%r/small.in" %(run_directory,i, z), "w")
			random_2000=random.sample((len(All_ptsmals)-1),samplesize)
			f.write(")O+_06 Small-body initial data  (WARNING: Do not delete this line!!)\n")
			f.write(")---------------------------------------------------------------------\n")
			f.write(" style (Cartesian, Asteroidal, Cometary) = Asteroidal\n")
			f.write(")---------------------------------------------------------------------\n")	
			for n in range(samplesize):
				mass=mass
				a=All_ptsmals[random_2000[n]].split()[1]
				e=All_ptsmals[random_2000[n]].split()[2]
				i=All_ptsmals[random_2000[n]].split()[3]
				AoP=All_ptsmals[random_2000[n]].split()[4]
				LoAN=All_ptsmals[random_2000[n]].split()[5]
				MA=All_ptsmals[random_2000[n]].split()[6]
				f.write ("PM%r ep=0 m=%g\n%r %r %r %r %r %r 0 0 0\n"(n, mass, a, e, i, AoP, LoAN, MA))
		f.close()
	r.close()

def delete_files(sourcefile):
	print "deleting file", sourcefile
	dataout,dataerr=subprocess.Popen([r"rm",sourcefile],stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	print "dataout", dataout
	print "dataerr", dataerr	 



def copy_files(sourcefile, destfile):
	print "copying file", sourcefile, "to", destfile
	dataout,dataerr=subprocess.Popen([r"cp",sourcefile,destfile],stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	print "dataout", dataout
	print "dataerr", dataerr


def directory_maker(path,number):
	subprocess.call("mkdir %s" %(path), shell=True) 
	for i in range(number):
		subprocess.call("mkdir %s/RunP%r" %(path,i), shell=True) 
		
directory_maker("/projects/b1011/sethk/Real_runs", 0)
for i in range(50):
	directory_maker("/projects/b1011/sethk/Real_runs/Run%r", 4)
	
for i in range(50):
	for n in range(4):
		copy_files("/projects/b1011/sethk/source/SourceFiles/param.in", "/projects/b1011/sethk/Real_runs/Run%r/RunP%r"%(i,n))
		copy_files("/projects/b1011/sethk/source/SourceFiles/element.in", "/projects/b1011/sethk/Real_runs/Run%r/RunP%r"%(i,n))
		copy_files("/projects/b1011/sethk/source/SourceFiles/files.in", "/projects/b1011/sethk/Real_runs/Run%r/RunP%r"%(i,n))
		copy_files("/projects/b1011/sethk/source/SourceFiles/message.in", "/projects/b1011/sethk/Real_runs/Run%r/RunP%r"%(i,n))
		copy_files("/projects/b1011/sethk/source/SourceFiles/mercury6", "/projects/b1011/sethk/Real_runs/Run%r/RunP%r"%(i,n))
		copy_files("/projects/b1011/sethk/source/SourceFiles/element6", "/projects/b1011/sethk/Real_runs/Run%r/RunP%r"%(i,n))

bigin_creator("/projects/b1011/sethk/Real_runs", "/projects/b1011/sethk/cleanup", 50, 4)
smallin_creator("/projects/b1011/sethk/Real_runs", "/projects/b1011/sethk/cleanup", "Survivors40.txt", 50, 2000, .00000005, 4)
		
	


	
















	