import numpy as np
import matplotlib.pyplot as plt

datos1 = np.genfromtxt("datos1.dat", skip_footer = 1)
datos2 = np.genfromtxt("datos2.dat", skip_footer = 1)

x1 = datos1[:,0]
y1 = datos1[:,1]

x2 = datos2[:,0]
y2 = datos2[:,1]


plt.figure()
plt.plot(x1,y1, 'ko')
plt.plot(x1,np.exp(-x1))
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title("Euler Method")
plt.savefig("Euler")

plt.figure()
plt.plot(x2,y2, 'ko')
plt.plot(x2,np.exp(-x2))
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title("RungeKutta Method")
plt.savefig("RungeKutta")