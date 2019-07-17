import numpy as np
import matplotlib.pyplot as plt

d1 = np.genfromtxt("datos1.dat")
d2 = np.genfromtxt("datos2.dat")
d3 = np.genfromtxt("datos3.dat")
d4 = np.genfromtxt("datos4.dat")
d5 = np.genfromtxt("datos5.dat")
d6 = np.genfromtxt("datos6.dat")
d7 = np.genfromtxt("datos7.dat")
d8 = np.genfromtxt("datos8.dat")
d9 = np.genfromtxt("datos9.dat")

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

d4x = d4[:,1]
d4y = d4[:,2]
d4Vx = d4[:,3]
d4Vy = d4[:,4]

d5x = d5[:,1]
d5y = d5[:,2]
d5Vx = d5[:,3]
d5Vy = d5[:,4]

d6x = d6[:,1]
d6y = d6[:,2]
d6Vx = d6[:,3]
d6Vy = d6[:,4]

d7x = d7[:,1]
d7y = d7[:,2]
d7Vx = d7[:,3]
d7Vy = d7[:,4]

d8x = d8[:,1]
d8y = d8[:,2]
d8Vx = d8[:,3]
d8Vy = d8[:,4]

d9x = d9[:,1]
d9y = d9[:,2]
d9Vx = d9[:,3]
d9Vy = d9[:,4]

plt.figure()
plt.figure(figsize=(10,10))
plt.subplot(3,3,1)
plt.plot(d1x,d1y, label = "dt = 0.01")
plt.title("Runge Kutta")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,2)
plt.plot(d2x,d2y, label = "dt = 0.01")
plt.title("Euler")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,3)
plt.plot(d3x,d3y, label = "dt = 0.01")
plt.title("Leap Frog")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,4)
plt.plot(d4x,d4y, label = "dt = 0.1")
plt.title("Runge Kutta")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,5)
plt.plot(d5x,d5y, label = "dt = 0.1")
plt.title("Euler")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,6)
plt.plot(d6x,d6y, label = "dt = 0.1")
plt.title("Leap Frog")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,7)
plt.plot(d7x,d7y, label = "dt = 0.001")
plt.title("Runge Kutta")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,8)
plt.plot(d8x,d8y, label = "dt = 0.001")
plt.title("Euler")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,9)
plt.plot(d9x,d9y, label = "dt = 0.001")
plt.title("Leap Frog")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.savefig("Posicion")

plt.figure()
plt.figure(figsize=(10,10))
plt.subplot(3,3,1)
plt.scatter(d1Vx,d1Vy, label = "dt = 0.01")
plt.title("Runge Kutta")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,2)
plt.plot(d2Vx,d2Vy, label = "dt = 0.01")
plt.title("Euler")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,3)
plt.scatter(d3Vx,d3Vy, label = "dt = 0.01")
plt.title("Leap Frog")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,4)
plt.scatter(d4Vx,d4Vy, label = "dt = 0.1")
plt.title("Runge Kutta")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,5)
plt.plot(d5Vx,d5Vy, label = "dt = 0.1")
plt.title("Euler")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,6)
plt.scatter(d6Vx,d6Vy, label = "dt = 0.1")
plt.title("Leap Frog")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,7)
plt.scatter(d7Vx,d7Vy, label = "dt = 0.001")
plt.title("Runge Kutta")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,8)
plt.plot(d8Vx,d8Vy, label = "dt = 0.001")
plt.title("Euler")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,9)
plt.scatter(d9Vx,d9Vy, label = "dt = 0.001")
plt.title("Leap Frog")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.savefig("Velocidad")