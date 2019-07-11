import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Z = np.genfromtxt("datos1.dat")
X, Y = np.meshgrid(np.linspace(0,1,99), np.linspace(0,1,99))
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z)
ax.set_zlim(0, 150)
ax.set_zlabel("Temperatura")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.title("Placa condicion inicial")
plt.savefig("Condicion inicial")