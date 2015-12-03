#!/bin/bash

#MSUB -N Seth 
#MSUB -m abe SethKrantzler2017@u.northwestern.edu
#MSUB -e error.out
#MSUB -o output.out
#MSUB -l nodes=1:ppn=1
#MSUB -l walltime=23:59:59
#MSUB -A b1011
#MSUB -q ligo



# Go to working directory
cd $PBS_O_WORKDIR

echo ------------------------------------------------------
echo -n 'Job is running on node '; cat $PBS_NODEFILE
echo ------------------------------------------------------
echo MOAB: qsub is running on $PBS_O_HOST
echo MOAB: originating queue is $PBS_O_QUEUE
echo MOAB: executing queue is $PBS_QUEUE
echo MOAB: working directory is $PBS_O_WORKDIR
echo MOAB: execution mode is $PBS_ENVIRONMENT
echo MOAB: job identifier is $PBS_JOBID
echo MOAB: job name is $PBS_JOBNAME
echo MOAB: node file is $PBS_NODEFILE
echo MOAB: current home directory is $PBS_O_HOME
echo MOAB: PATH = $PBS_O_PATH
echo ----------------------------------------------
echo ------------------------------------------------------
echo -n 'Job is running on node '; cat $PBS_NODEFILE
echo ------------------------------------------------------
echo ' '
echo ' '


for i in `ls -d RunP*`
do
	cd $i
	pwd
	./mercury6 && ./element6
	rm ce.out
	cd ..
done
