XY_met_dt.pdf VxVy_met_dt.pdf Ener_met_dt.pdf Mome_met_dt.pdf FFtIm.pdf ImProceso.pdf ImHybrid.pdf: datos1.dat datos2.dat datos3.dat datos4.dat datos5.dat datos6.dat datos7.dat datos8.dat datos9.dat cara_02_grisesMF.png cara_03_grisesMF.png Fourier.py Plots_hw2.py
	python Plots_hw2.py 
	python Fourier.py
datos1.dat datos2.dat datos3.dat datos4.dat datos5.dat datos6.dat datos7.dat datos8.dat datos9.dat: ./a.out
	./a.out
./a.out: ODEs.cpp
	g++ ODEs.cpp