S5C1PLOT.pdf: datos.dat plotsS5C1.py
    python plotsS5C1.py
                           
datos.dat: ./a.out
    ./a.out > datos.dat
    
./a.out: S5C1Deriv.cpp
    g++ S5C1Deriv.cpp