import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt("datos.dat")
d1 = datos[0:len(datos)/2]
d2 = datos[len(datos)/2+1:len(datos)]

x = np.linspace(0,1,len(d1))
y = np.linspace(0,1,len(d1))
plt.figure()
plt.plot(x, d1, label = "Funcion")
plt.plot(y, d2, label = "Derivada")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Funcion Coseno")
plt.legend()
plt.savefig("S5C1PLOT.pdf")