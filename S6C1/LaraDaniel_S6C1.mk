PDEs.png: datos1.dat LaraDaniel_S6C1_plots.py
	python LaraDaniel_S6C1_plots.py
datos1.dat: ./a.out
	./a.out
./a.out: LaraDaniel_S6C1_PDEs.cpp
	g++ LaraDaniel_S6C1_PDEs.cpp