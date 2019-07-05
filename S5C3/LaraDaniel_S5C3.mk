RungeKutta.png: datos1.dat LaraDaniel_S5C3_plots.py
	python LaraDaniel_S5C3_plots.py
datos1.dat: ./a.out
	./a.out
./a.out: LaraDaniel_S5C3_ODEs.cpp
	g++ LaraDaniel_S5C3_ODEs.cpp