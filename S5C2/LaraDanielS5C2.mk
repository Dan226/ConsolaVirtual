Euler.png RungeKutta.png: datos1.dat datos2.dat plot.py
	python plot.py
datos1.dat datos2.dat: ./a.out
	./a.out
./a.out: LaraDanielS5C2.cpp
	g++ LaraDanielS5C2.cpp