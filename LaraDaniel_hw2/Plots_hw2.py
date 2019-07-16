import numpy as np
import matplotlib.pyplot as plt

d1 = np.genfromtxt("datos1.dat")
d2 = np.genfromtxt("datos2.dat")
d3 = np.genfromtxt("datos3.dat")

t = d1[:,0]
d1x = d1[:,1]
d1y = d1[:,2]
d1Vx = d1[:,3]
d1Vy = d1[:,4]

d2x = d2[:,1]
d2y = d2[:,2]
d2Vx = d2[:,3]
d2Vy = d2[:,4]

d3x = d3[:,1]
d3y = d3[:,2]
d3Vx = d3[:,3]
d3Vy = d3[:,4]

plt.figure()
plt.figure(figsize=(20,10))
plt.subplot(1,3,1)
plt.plot(d1x,d1y, label = "dt = 0.01")
plt.title("Runge Kutta")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(1,3,2)
plt.plot(d2x,d2y, label = "dt = 0.01")
plt.title("Euler")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(1,3,3)
plt.plot(d3x,d3y, label = "dt = 0.01")
plt.title("Leap Frog")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.savefig("Posicion")

plt.figure()
plt.figure(figsize=(20,10))
plt.subplot(1,3,1)
plt.scatter(d1Vx,d1Vy, label = "dt = 0.01")
plt.title("Runge Kutta")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(1,3,2)
plt.plot(d2Vx,d2Vy, label = "dt = 0.01")
plt.title("Euler")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(1,3,3)
plt.scatter(d3Vx,d3Vy, label = "dt = 0.01")
plt.title("Leap Frog")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.savefig("Velocidad")