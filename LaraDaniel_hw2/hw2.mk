Posicion.pdf Velocidad.pdf EnergiaTotal.pdf MomentumAngular.pdf: datos1.dat datos2.dat datos3.dat datos4.dat datos5.dat datos6.dat datos7.dat datos8.dat datos9.dat Plots_hw2.py
	python Plots_hw2.py
datos1.dat datos2.dat datos3.dat datos4.dat datos5.dat datos6.dat datos7.dat datos8.dat datos9.dat: ./a.out
	./a.out
./a.out: ODEs.cpp
	g++ ODEs.cpp