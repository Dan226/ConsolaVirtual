PDEs.png: datos1.dat Plots_cuerdayTambor.py
	python Plots_cuerdayTambor.py
datos1.dat: ./a.out
	./a.out
./a.out: LaraDaniel_cuerdayTambor.cpp
	g++ LaraDaniel_cuerdayTambor.cpp
