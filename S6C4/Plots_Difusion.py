import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Z = np.genfromtxt("datos1.dat")
X, Y = np.meshgrid(np.linspace(0,1,100), np.linspace(0,1,100))
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z)
ax.set_zlim(0, 150)
ax.set_zlabel("Temperatura")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.title("Placa condicion inicial")
plt.savefig("Caso1(T = 0)")

Z1 = np.genfromtxt("datos2.dat")
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z1)
ax.set_zlabel("Temperatura")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.title("Placa t = 100")
plt.savefig("Caso1(t = 100)")

Z2 = np.genfromtxt("datos3.dat")
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z2)
ax.set_zlabel("Temperatura")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.title("Placa t = 2500")
plt.savefig("Caso1(t = 2500)")