import numpy as np
import matplotlib.pyplot as plt

datos1 = np.genfromtxt("datos1.dat")

x1 = datos1[:,0]
y1 = datos1[:,1]
t = datos1[:,2]



plt.figure()
plt.plot(t,y1)
plt.plot(t,x1)
plt.xlabel('t (s)')
plt.ylabel('u')
plt.title("Ecuacion calor")
plt.savefig("PDEs")
