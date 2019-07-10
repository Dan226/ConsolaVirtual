import numpy as np
import matplotlib.pyplot as plt

datos1 = np.genfromtxt("datos1.dat")

x11 = datos1[:,0]
x21 = datos1[:,1]
x31 = datos1[:,2]
x41 = datos1[:,3]
x51 = datos1[:,4]
x61 = datos1[:,5]
y11 = datos1[:,6]
t = datos1[:,7]



plt.figure()
plt.figure(figsize=(20,10))
plt.subplot(2,3,1)
plt.plot(t,y11, label = "inicial")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.ylim((0.000, 0.010));
plt.title("Cuerda")
plt.legend()
plt.subplot(2,3,2)
plt.plot(t,x11, label = "tiempo1")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.ylim((0.000, 0.010));
plt.title("Cuerda")
plt.legend()
plt.subplot(2,3,3)
plt.plot(t,x21, label = "tiempo2")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.ylim((0.000, 0.010));
plt.title("Cuerda")
plt.legend()
plt.subplot(2,3,4)
plt.plot(t,x31, label = "tiempo3")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.ylim((0.000, 0.010));
plt.title("Cuerda")
plt.legend()
plt.subplot(2,3,5)
plt.plot(t,x41, label = "tiempo4")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.ylim((0.000, 0.010));
plt.title("Cuerda")
plt.legend()
plt.subplot(2,3,6)
plt.plot(t,x51, label = "tiempo5")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.ylim((0.000, 0.010));
plt.title("Cuerda")
plt.legend()
plt.savefig("PDEs")

datos2 = np.genfromtxt("datos2.dat")

x12 = datos2[:,0]
x22 = datos2[:,1]
x32 = datos2[:,2]
x42 = datos2[:,3]
x52 = datos2[:,4]
x62 = datos1[:,5]
y12 = datos1[:,6]
t = datos1[:,7]

plt.figure()
plt.figure(figsize=(20,10))
plt.subplot(2,3,1)
plt.plot(t,y12, label = "inicial")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.ylim((0.000, 0.010));
plt.title("Cuerda")
plt.legend()
plt.subplot(2,3,2)
plt.plot(t,x12, label = "tiempo1")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.ylim((0.000, 0.010));
plt.title("Cuerda")
plt.legend()
plt.subplot(2,3,3)
plt.plot(t,x22, label = "tiempo2")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.ylim((0.000, 0.010));
plt.title("Cuerda")
plt.legend()
plt.subplot(2,3,4)
plt.plot(t,x32, label = "tiempo3")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.ylim((0.000, 0.010));
plt.title("Cuerda")
plt.legend()
plt.subplot(2,3,5)
plt.plot(t,x42, label = "tiempo4")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.ylim((0.000, 0.010));
plt.title("Cuerda")
plt.legend()
plt.subplot(2,3,6)
plt.plot(t,x52, label = "tiempo5")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.ylim((0.000, 0.010));
plt.title("Cuerda")
plt.legend()
plt.savefig("PDECaso2")



datos3 = np.genfromtxt("datos3.dat")

x13 = datos3[:,0]
x23 = datos3[:,1]
x33 = datos3[:,2]
x43 = datos3[:,3]
x53 = datos3[:,4]
x63 = datos3[:,5]
y13 = datos3[:,6]
t = datos3[:,7]



plt.figure()
plt.figure(figsize=(20,10))
plt.subplot(2,3,1)
plt.plot(t,y13, label = "inicial")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.title("Cuerda")
plt.legend()
plt.subplot(2,3,2)
plt.plot(t,x13, label = "tiempo1")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.title("Cuerda")
plt.legend()
plt.subplot(2,3,3)
plt.plot(t,x23, label = "tiempo2")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.title("Cuerda")
plt.legend()
plt.subplot(2,3,4)
plt.plot(t,x33, label = "tiempo3")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.title("Cuerda")
plt.legend()
plt.subplot(2,3,5)
plt.plot(t,x43, label = "tiempo4")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.title("Cuerda")
plt.legend()
plt.subplot(2,3,6)
plt.plot(t,x53, label = "tiempo5")
plt.xlabel('t (s)')
plt.ylabel('u')
plt.title("Cuerda")
plt.legend()
plt.savefig("PDECaso3")
