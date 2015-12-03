import numpy as np 
import matplotlib.pyplot as plt 

	
def interactions_precise(run_directory, rangea):
	s=open("%s/InteractionTimes40.txt"%(run_directory), "w")
	s.write("Time\n")
	for n in range(rangea):
		f=open("%s/RunP%r/info.out"%(run_directory,n), "r")
		f.seek(0)
		for line in f:
			if line.rfind('INNER')>-1 or line.rfind('OUTER')>-1:
				a = line.split()
				yr, mo, da = a[6], a[7], a[8]
				s.write(str((int(yr)+4712)+(int(mo)*0.08333333333)+(float(da)*0.00273785078))+"\n")
		
	f.close()
	s.close()
	


def interaction_hist(file, run_directory):
	Time=np.loadtxt(file, skiprows=1, usecols=(0,))
	Histdest="%s/PlanestesimalInt40Hist.jpeg"%run_directory	
	
	fig=plt.figure()
	axes=fig.add_subplot(111)
	
	bins = 50
	
	axes.hist(Time, bins=bins, histtype='step', stacked=False, fill=True, color='indigo', alpha=0.8, normed=False)
	axes.set_title("$Histogram\,of\,Planetesimal\,Interaction\,Time$")
	axes.set_xlabel('$Time\,(Years)$')
	axes.set_yscale('linear')
	axes.set_xscale('linear') 
	plt.savefig(Histdest) 
	plt.close() 
	


def survivor_maker(run_directory, rangea):
	s=open("%s/Survivors40.txt"%(run_directory), "w")
	s.write("Time a e i AoP LoAN MA Mass\n")
	start=0
	finish=200
	for n in range(rangea):
		for z in range(start, finish):
			if z<(finish-1):
				f=open("%s/RunP%r/PM%r.aei"%(run_directory,n,z), "r")
				r=open("%s/RunP%r/INNER.aei"%(run_directory,n), "r")
				Plast=f.readlines()[-1]
				Ptime=Plast.split()[0]
				Baselast=r.readlines()[-1].split()[0]
				if Ptime==Baselast:
					s.write(Plast)
			elif z==finish-1:
				start=finish
				finish=finish+200
				f=open("%s/RunP%r/PM%r.aei"%(run_directory,n,z), "r")
				r=open("%s/RunP%r/INNER.aei"%(run_directory,n), "r")
				Plast=f.readlines()[-1]
				Ptime=Plast.split()[0]
				Baselast=r.readlines()[-1].split()[0]
				if Ptime==Baselast:
					s.write(Plast)
	
						
	s.close()
	f.close()
	r.close()



def survivor_histogram(file, run_directory, rangea):
	OrbitalSepinitial=[]
	OrbitalSepfin=np.loadtxt(file, skiprows=1, usecols=(1,)) 
	Histdest="%s/PlanestesimalSep40Hist.jpeg"%run_directory
	start=0
	finish=200
	for n in range(rangea):
		for z in range(start, finish):
			if z<(finish-1):
				f=open("%s/RunP%r/PM%r.aei"%(run_directory,n,z), "r")
				OrbitalSepinitial.append(float(f.readlines()[4].split()[1]))
			elif z==finish-1:
				start=finish
				finish=finish+200
				f=open("%s/RunP%r/PM%r.aei"%(run_directory,n,z), "r")
				OrbitalSepinitial.append(float(f.readlines()[4].split()[1]))
	
	f.close() 
	
	fig=plt.figure()
	axes=fig.add_subplot(111)
	bins = 250
	axes.hist(OrbitalSepinitial, bins=bins, range=[0.01,1], histtype='step', stacked=False, fill=False, color='teal', label="Initial", normed='True')
	axes.hist(OrbitalSepfin, bins=bins, range=[0.01,1], histtype='step', stacked=False, fill=True, color='indigo', facecolor='indigo', alpha=0.3, label="Final", normed='True')
	axes.set_title("Histogram of Planetesimal Distance")
	x1=[.1, .1]
	x2=[0.15293,0.15293]
	x3=[0.15290, 0.15290]
	y=[0,55]
	line1=plt.plot(x1,y) 
	line2=plt.plot(x2,y)
	line3=plt.plot(x3,y)
	plt.setp(line1, color='indigo', linewidth=1.0)
	plt.setp(line2, color='green', linewidth=1.0)
	plt.setp(line3, color='black', linewidth=1.0)
	axes.set_title('$Planetesimal\,Seperation\,after\,40\,Years$')
	axes.set_xlabel('$Distance\,(AU)$')
	axes.set_yscale('log')
	axes.set_xscale('log')
	axes.set_xlim([0.042,.32]) 
	axes.set_ylim([1,55])
	axes.legend(loc="best") 
	plt.savefig(Histdest) 
	plt.close()

for i in range(1,50):
	survivor_maker("/projects/b1011/sethk/cleanup/Run%r"%i, 100)
	survivor_histogram("/projects/b1011/sethk/cleanup/Run%r/Survivors40.txt"%i,"/projects/b1011/sethk/cleanup/Run%r"%i, 100)
	interactions_precise("/projects/b1011/sethk/cleanup/Run%r"%i, 100)
	interaction_hist("/projects/b1011/sethk/cleanup/Run%r/InteractionTimes40.txt"%i, "/projects/b1011/sethk/cleanup/Run%r"%i) 
	
	


