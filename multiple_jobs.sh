for i in `ls -d Run*`
do
	cd $i
	pwd
	cd RunP0
	msub batch_real.sh
	cd ..
	cd RunP1
	msub batch_real.sh
	cd ..
	cd RunP2
	msub batch_real.sh	
	cd ..
	cd RunP3
	msub batch_real.sh
	cd .. 
	cd ..
done