import subprocess

def move_files(sourcefile, destfile):
	print "copying file", sourcefile, "to", destfile
	dataout,dataerr=subprocess.Popen([r"mv",sourcefile,destfile],stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	print "dataout", dataout
	print "dataerr", dataerr


def symbolic_link(sourcefile, destfile):
	print "linking file", sourcefile, "to", destfile
	dataout,dataerr=subprocess.Popen([r"ln","-s",sourcefile,destfile],stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	print "dataout", dataout
	print "dataerr", dataerr
	
def delete_files(sourcefile):
	print "deleting file", sourcefile
	dataout,dataerr=subprocess.Popen([r"rm",sourcefile],stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	print "dataout", dataout
	print "dataerr", dataerr	 

def create_directory(directory_name):
	print "creating directory:", directory_name
	dataout,dataerr=subprocess.Popen([r"mkdir","-p",directory_name],stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	print "dataout", dataout
	print "dataerr", dataerr


def copy_files(sourcefile, destfile):
	print "copying file", sourcefile, "to", destfile
	dataout,dataerr=subprocess.Popen([r"cp",sourcefile,destfile],stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	print "dataout", dataout
	print "dataerr", dataerr

for i in range(1,50):
	copy_files("/Users/sethkrantzler/Documents/batch_cleanup.sh", "/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r"%i)
	#copy_files("/Users/sethkrantzler/Documents/PythonCodes/mercury6/element.in", "/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r"%i)
	#copy_files("/Users/sethkrantzler/Documents/PythonCodes/mercury6/message.in", "/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r"%i)
	#copy_files("/Users/sethkrantzler/Documents/PythonCodes/mercury6/files.in", "/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r"%i)
	"""for n in range(100):
		symbolic_link("/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/param.in"%i,"/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/RunP%r"%(i,n))
		symbolic_link("/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/element.in"%i,"/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/RunP%r"%(i,n))
		symbolic_link("/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/message.in"%i,"/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/RunP%r"%(i,n))
		symbolic_link("/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/files.in"%i,"/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/RunP%r"%(i,n))
		symbolic_link("/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/big.in"%i,"/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/RunP%r"%(i,n))
		symbolic_link("/Users/sethkrantzler/Documents/PythonCodes/mercury6/mercury6","/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/RunP%r"%(i,n))
		symbolic_link("/Users/sethkrantzler/Documents/PythonCodes/mercury6/mercury.inc","/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/RunP%r"%(i,n))
		symbolic_link("/Users/sethkrantzler/Documents/PythonCodes/mercury6/element.in","/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/RunP%r"%(i,n))
		symbolic_link("/Users/sethkrantzler/Documents/PythonCodes/mercury6/element6","/Users/sethkrantzler/Documents/PythonCodes/mercury6/cleanupruns1/Run%r/RunP%r"%(i,n))"""
		
