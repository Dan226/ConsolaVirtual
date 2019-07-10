PDEs.png: datos1.dat Plots_cuerda.py
	python Plots_cuerda.py
datos1.dat: ./a.out
	./a.out
./a.out: LaraDaniel_cuerda.cpp
	g++ LaraDaniel_cuerda.cpp
