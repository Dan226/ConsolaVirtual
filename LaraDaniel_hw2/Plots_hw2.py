import numpy as np
import matplotlib.pyplot as plt
import math

d1 = np.genfromtxt("datos1.dat")
d2 = np.genfromtxt("datos2.dat")
d3 = np.genfromtxt("datos3.dat")
d4 = np.genfromtxt("datos4.dat")
d5 = np.genfromtxt("datos5.dat")
d6 = np.genfromtxt("datos6.dat")
d7 = np.genfromtxt("datos7.dat")
d8 = np.genfromtxt("datos8.dat")
d9 = np.genfromtxt("datos9.dat")

def energia(Vx,Vy,x,y):
    G1 = 6.67e-11
    UA = 149597870700.0
    M = 1.99e30
    yr = 31536000.0
    m = 5.972e24
    G = G1*(1.0/(UA*UA*UA))*(M)*(yr*yr)
    E = np.zeros(len(Vx))
    for i in range(len(Vx)):
        a = float(math.pow((x[i]*x[i]+y[i]*y[i]),0.5))
        b = float(G*M*m)
        if(a!=0.0):
            E[i] = 0.5*m*(Vx[i]*Vx[i] + Vy[i]*Vy[i])- b/a
        else:
            E[i] = 0.5*m*(Vx[i]*Vx[i] + Vy[i]*Vy[i]) 
    return E

def momento(Vx,Vy,x,y):
    m = 5.972e24
    #momento angular: L = r x m*v
    L = np.zeros(len(x))
    
    for i in range(len(x)):
        Vx[i] = m*Vx[i]
        Vy[i] = m*Vy[i]
        L[i] = np.cross([x[i],y[i]],[Vx[i],Vy[i]])
    return L    


t1 = d1[:,0]
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

t2 = d4[:,0]
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

t3 = d7[:,0]
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
#Calculo energia
E1 = energia(d1Vx,d1Vy,d1x,d1y)
E2 = energia(d2Vx,d2Vy,d2x,d2y)
E3 = energia(d3Vx,d3Vy,d3x,d3y)
E4 = energia(d4Vx,d4Vy,d4x,d4y)
E5 = energia(d5Vx,d5Vy,d5x,d5y)
E6 = energia(d6Vx,d6Vy,d6x,d6y)
E7 = energia(d7Vx,d7Vy,d7x,d7y)
E8 = energia(d8Vx,d8Vy,d8x,d8y)
E9 = energia(d9Vx,d9Vy,d9x,d9y)

#Calculo momento angular
m1 = momento(d1Vx,d1Vy,d1x,d1y)
m2 = momento(d2Vx,d2Vy,d2x,d2y)
m3 = momento(d3Vx,d3Vy,d3x,d3y)
m4 = momento(d4Vx,d4Vy,d4x,d4y)
m5 = momento(d5Vx,d5Vy,d5x,d5y)
m6 = momento(d6Vx,d6Vy,d6x,d6y)
m7 = momento(d7Vx,d7Vy,d7x,d7y)
m8 = momento(d8Vx,d8Vy,d8x,d8y)
m9 = momento(d9Vx,d9Vy,d9x,d9y)


#Graficas posicion
plt.figure()
plt.figure(figsize=(15,15))
plt.subplot(3,3,1)
plt.plot(d1x,d1y, label = "dt = 0.01", color = "black")
plt.title("Runge Kutta")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,2)
plt.plot(d2x,d2y, label = "dt = 0.01", color = "red")
plt.title("Euler")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,3)
plt.plot(d3x,d3y, label = "dt = 0.01", color = "green")
plt.title("Leap Frog")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,4)
plt.plot(d4x,d4y, label = "dt = 0.0001", color = "black")
plt.title("Runge Kutta")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,5)
plt.plot(d5x,d5y, label = "dt = 0.0001", color = "red")
plt.title("Euler")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,6)
plt.plot(d6x,d6y, label = "dt = 0.0001", color = "green")
plt.title("Leap Frog")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,7)
plt.plot(d7x,d7y, label = "dt = 0.001", color = "black")
plt.title("Runge Kutta")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,8)
plt.plot(d8x,d8y, label = "dt = 0.001", color = "red")
plt.title("Euler")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.subplot(3,3,9)
plt.plot(d9x,d9y, label = "dt = 0.001", color = "green")
plt.title("Leap Frog")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.savefig("Posicion.pdf")
#Graficas velocidades
plt.figure()
plt.figure(figsize=(15,15))
plt.subplot(3,3,1)
plt.plot(d1Vx,d1Vy, label = "dt = 0.01", color = "black")
plt.title("Runge Kutta")
plt.xlabel("Vx")
plt.ylabel("Vy")
plt.legend()
plt.subplot(3,3,2)
plt.plot(d2Vx,d2Vy, label = "dt = 0.01", color = "red")
plt.title("Euler")
plt.xlabel("Vx")
plt.ylabel("Vy")
plt.legend()
plt.subplot(3,3,3)
plt.plot(d3Vx,d3Vy, label = "dt = 0.01", color = "green")
plt.title("Leap Frog")
plt.xlabel("Vx")
plt.ylabel("Vy")
plt.legend()
plt.subplot(3,3,4)
plt.plot(d4Vx,d4Vy, label = "dt = 0.0001", color = "black")
plt.title("Runge Kutta")
plt.xlabel("Vx")
plt.ylabel("Vy")
plt.legend()
plt.subplot(3,3,5)
plt.plot(d5Vx,d5Vy, label = "dt = 0.0001", color = "red")
plt.title("Euler")
plt.xlabel("Vx")
plt.ylabel("Vy")
plt.legend()
plt.subplot(3,3,6)
plt.plot(d6Vx,d6Vy, label = "dt = 0.0001", color = "green")
plt.title("Leap Frog")
plt.xlabel("Vx")
plt.ylabel("Vy")
plt.legend()
plt.subplot(3,3,7)
plt.plot(d7Vx,d7Vy, label = "dt = 0.001", color = "black")
plt.title("Runge Kutta")
plt.xlabel("Vx")
plt.ylabel("Vy")
plt.legend()
plt.subplot(3,3,8)
plt.plot(d8Vx,d8Vy, label = "dt = 0.001", color = "red")
plt.title("Euler")
plt.xlabel("Vx")
plt.ylabel("Vy")
plt.legend()
plt.subplot(3,3,9)
plt.plot(d9Vx,d9Vy, label = "dt = 0.001", color = "green")
plt.title("Leap Frog")
plt.xlabel("Vx")
plt.ylabel("Vy")
plt.legend()
plt.savefig("Velocidad.pdf")
#Graficas energias
plt.figure()
plt.figure(figsize=(15,15))
plt.subplot(3,3,1)
plt.plot(t1,E1, label = "dt = 0.01", color = "black")
plt.title("Runge Kutta")
plt.ylabel("E (J)")
plt.xlabel("t (s)")
plt.legend()
plt.subplot(3,3,2)
plt.plot(t1,E2, label = "dt = 0.01", color = "red")
plt.title("Euler")
plt.ylabel("E (J)")
plt.xlabel("t (s)")
plt.legend()
plt.subplot(3,3,3)
plt.plot(t1,E3, label = "dt = 0.01", color = "green")
plt.title("Leap Frog")
plt.ylabel("E (J)")
plt.xlabel("t (s)")
plt.legend()
plt.subplot(3,3,4)
plt.plot(t2,E4, label = "dt = 0.0001", color = "black")
plt.title("Runge Kutta")
plt.ylabel("E (J)")
plt.xlabel("t (s)")
plt.legend()
plt.subplot(3,3,5)
plt.plot(t2,E5, label = "dt = 0.0001", color = "red")
plt.title("Euler")
plt.ylabel("E (J)")
plt.xlabel("t (s)")
plt.legend()
plt.subplot(3,3,6)
plt.plot(t2,E6, label = "dt = 0.0001", color = "green")
plt.title("Leap Frog")
plt.ylabel("E (J)")
plt.xlabel("t (s)")
plt.legend()
plt.subplot(3,3,7)
plt.plot(t3,E7, label = "dt = 0.001", color = "black")
plt.title("Runge Kutta")
plt.ylabel("E (J)")
plt.xlabel("t (s)")
plt.legend()
plt.subplot(3,3,8)
plt.plot(t3,E8, label = "dt = 0.001", color = "red")
plt.title("Euler")
plt.ylabel("E (J)")
plt.xlabel("t (s)")
plt.legend()
plt.subplot(3,3,9)
plt.plot(t3,E9, label = "dt = 0.001", color = "green")
plt.title("Leap Frog")
plt.ylabel("E (J)")
plt.xlabel("t (s)")
plt.legend()
plt.savefig("EnergiaTotal.pdf")

#Graficas momentos
plt.figure()
plt.figure(figsize=(15,15))
plt.subplot(3,3,1)
plt.plot(t1,m1, label = "dt = 0.01", color = "black")
plt.title("Runge Kutta")
plt.ylabel("P (v)")
plt.xlabel("t (s)")
plt.legend()
plt.subplot(3,3,2)
plt.plot(t1,m2, label = "dt = 0.01", color = "red")
plt.title("Euler")
plt.ylabel("P (v)")
plt.xlabel("t (s)")
plt.legend()
plt.subplot(3,3,3)
plt.plot(t1,m3, label = "dt = 0.01", color = "green")
plt.title("Leap Frog")
plt.ylabel("P (v)")
plt.xlabel("t (s)")
plt.legend()
plt.subplot(3,3,4)
plt.plot(t2,m4, label = "dt = 0.0001", color = "black")
plt.title("Runge Kutta")
plt.ylabel("P (v)")
plt.xlabel("t (s)")
plt.legend()
plt.subplot(3,3,5)
plt.plot(t2,m5, label = "dt = 0.0001", color = "red")
plt.title("Euler")
plt.ylabel("P (v)")
plt.xlabel("t (s)")
plt.legend()
plt.subplot(3,3,6)
plt.plot(t2,m6, label = "dt = 0.0001", color = "green")
plt.title("Leap Frog")
plt.ylabel("P (v)")
plt.xlabel("t (s)")
plt.legend()
plt.subplot(3,3,7)
plt.plot(t3,m7, label = "dt = 0.001", color = "black")
plt.title("Runge Kutta")
plt.ylabel("P (v)")
plt.xlabel("t (s)")
plt.legend()
plt.subplot(3,3,8)
plt.plot(t3,m8, label = "dt = 0.001", color = "red")
plt.title("Euler")
plt.ylabel("P (v)")
plt.xlabel("t (s)")
plt.legend()
plt.subplot(3,3,9)
plt.plot(t3,m9, label = "dt = 0.001", color = "green")
plt.title("Leap Frog")
plt.ylabel("P (v)")
plt.xlabel("t (s)")
plt.legend()
plt.savefig("MomentumAngular.pdf")