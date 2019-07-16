#Ejercicio 0
#Lean el capitulo 5 del Landau (ver el programa del curso).

#Ejercicio 1
# Usando los generadores de numeros aleatorios de numpy (https://docs.scipy.org/doc/numpy-1.15.1/reference/routines.random.html):
# a) Genere 1000 numeros aleatorios que sigan una distribucion uniforme y esten entre -10 y 10. Haga un histograma y guardelo sin mostrarlo en un archivo llamado uniforme.pdf
# a) Genere 1000 numeros aleatorios que sigan una distribucion gausiana centrada en 17 y de sigma 5. Haga un histograma y guardelo sin mostrarlo en un archivo llamado gausiana.pdf

import numpy as np
import matplotlib.pyplot as plt
import random
import time

s = np.random.uniform(-10,10,1000)
plt.figure()
count, bins, ignored = plt.hist(s, 30, density=True)
plt.title("distribucion uniforme")
plt.xlabel("X")
plt.ylabel("Cantidad")
plt.savefig("uniforme.pdf")

plt.figure()
s = np.random.normal(17,5,1000)
plt.figure()
count, bins, ignored = plt.hist(s, 30, density=True)
plt.title("distribucion gausiana")
plt.xlabel("X")
plt.ylabel("Cantidad")
plt.savefig("gausiana.pdf")

# Ejercicio 2
# Escriba un programa en Python que: 
# Genere puntos aleatorios distribuidos uniformemente dentro de un cuadrado de lado 30.5. Grafique sus puntos y guarde la grafica sin mostrarla en un archivo llamado cuadrado.pdf. 
# Genere puntos aleatorios distribuidos uniformemente dentro de circulo de radio 23. Grafique sus puntos y guarde la grafica sin mostrarla en un archivo llamado circulo.pdf. 

x = np.random.uniform(0,30.5,1000)
y = np.random.uniform(0,30.5,1000)
plt.figure()
plt.figure(figsize = (10,10))
plt.scatter(x,y, label = "distribucion", s = 2, color = "black")
plt.title("distribucion uniforme en cuadrado")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("cuadrado.pdf")

plt.figure()
a = []
b = []
c= np.random.uniform(0,30.5,1000)
d = np.random.uniform(0,30.5,1000)

for i in range(d.size):
    if(((c[i]**2 + d[i]**2)**0.5)<23):
        a.append(c[i])
        b.append(d[i])
plt.figure(figsize = (10,10))
plt.scatter(a,b, label = "distribucion", s = 2, color = "black")
plt.title("distribucion uniforme en circulo")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("circulo")        

# Ejercicio 3 
# Lean sobre caminatas aleatorias.

# Ejercicio 4
# Tome los puntos distribuidos aleatoriamente dentro del cuadrado y haga que cada punto siga una caminata aleatoria de 100 pasos. 
# La magnitud de los pasos de esta caminata debe seguir una distribucion gaussiana centrada en el punto y de sigma igual a 0.25
# Implemente condiciones de frontera periodicas: si un punto se "sale" de cuadrado por un lado, "entra" por el otro  

plt.figure()
random.random()
for j in range(len(x)):
    for i in range(0, 100):
        x[j] += (np.random.normal(x[j],0.25,1))*0.1
        y[j] += (np.random.normal(y[j],0.25,1))*0.1
        if (x[j]>30.5):
            x[j] -= 30.5
        elif (x[j] < 0):
            x[j] += 30.5
        if(y[j]>30.5):
            y[j] -= 30.5
        elif(y[j]<0):
            y[j] += 30.5
            
plt.scatter(x, y, s = 2, color = "black")
plt.title("Caminata aleatoria")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("DistCaminata.pdf")


# Grafique la distribucion final de puntos y guarde dicha grafica sin mostrarla en un archivo llamado DistCaminata.pdf
# Grafique la caminata de UNO de sus puntos y guarde dicha grafica sin mostrarla en un archivo llamado puntoCaminata.pdf

plt.figure()
a = []
b = []
c = x[1]
d = y[1]
for i in range(0, 100):
        xin = (np.random.normal(0,0.25,1))
        yin = (np.random.normal(0,0.25,1))
        c += xin[0]
        d += yin[0]
        if (c>30.5):
            c -= 30.5
        elif (c < 0):
            c += 30.5
        if(d>30.5):
            d -= 30.5
        elif(d<0):
            d += 30.5
        a.append(c)
        b.append(d)

plt.plot(a, b, color = "black")
plt.title("Caminata aleatoria")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("puntoCaminata.pdf")
# Repita el proceso para sigma = 0.00025 y sigma= 2.5. Grafique la caminata de UNO de sus puntos para los distintos sigmas y guardela sin mostrarla en sigmaCaminata.pdf
plt.figure()
a = []
b = []
m = []
h = []
c = x[1]
d = y[1]
e = x[1]
f = y[1]
for i in range(0, 100):
        xin1 = (np.random.normal(0,0.00025,1))
        yin1 = (np.random.normal(0,0.00025,1))
        xin2 = (np.random.normal(0,2.5,1))
        yin2 = (np.random.normal(0,2.5,1))
        c += xin1[0]
        d += yin1[0]
        e += xin2[0]
        f += yin2[0]
        if (c>30.5):
            c -= 30.5
        elif (c < 0):
            c += 30.5
        if (e>30.5):
            e -= 30.5
        elif (e < 0):
            e += 30.5
        if(d>30.5):
            d -= 30.5
        elif(d<0):
            d += 30.5
        if(f>30.5):
            f -= 30.5
        elif(f<0):
            f += 30.5    
        a.append(c)
        b.append(d)
        m.append(e)
        h.append(f)

        
plt.plot(a, b, color = "black", label = "Sigma = 0.00025")
plt.plot(m,h, color = "red", label = "Sigma = 2.5")
plt.title("Caminata aleatoria")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.savefig("sigmaCaminata")

# Repita el proceso para condiciones abiertas: si un punto se "sale" del cuadrado deja de ser considerado en la simulacion.

# Si le queda tiempo puede:

##################################################################################################################################################################
############################################################ Ejercicio  ##########################################################################
##################################################################################################################################################################

#difusion: una gota de crema en un Cafe.
#
#Condiciones iniciales:
#Cafe: 10000 particulas distribuidas uniformemente dentro de un circulo de radio igual a raiz de 230
#Crema: 100 particulas distribuidas uniformemente dentro de un circulo de radio igual a raiz de 2
#
#Nota: si su codigo se esta demorando mucho en correr, puede usar 1000 particulas de cafe en vez de 10000.
#
# 1) Haga una grafica de las condiciones iniciales donde los dos tipos de particulas tengan distintos colores. Guarde dicha grafica sin mostrarla en CafeLecheIni.pdf
#
#2) Todas las particulas deben hacer una caminata aleatoria de 1000 pasos. Los pasos en las coordenadas x y deben seguir una distribucion gausiana de sigma 2.5. Si va a usar coordenadas polares elija un sigma apropiado.
#
#3) Condiciones de frontera: implemente unas condiciones tales que si la particulas "sale" del circulo, usted vuelva a dar el paso. Si no puede implementar solo las condiciones antes descritas, debe al menos escribir comentarios explicando que hace cada linea de codigo de las condiciones propuestas (comentado abajo)
#
# 4) Haga una grafica de las posiciones finales de las particulas despues de la caminata donde los dos tipos de particulas tengan distintos colores. Guarde dicha grafica sin mostrarla en CafeLecheFin.pdf
#

import numpy as np
import matplotlib.pylab as plt


#Una posible implementacion de condiciones de frontera. Trate de hacer la suya propia sin usar esta. 
#Si usa esta (obtiene menos puntos) debe comentar cada una de las lineas explicando en palabras que hace el codigo. Debe tambien naturalmente usar los nombres de variables que uso en el resto de su codigo propio.
#indexcafe=np.where((xcafenuevo*xcafenuevo+ycafenuevo*ycafenuevo)>230)
#indexcrema=np.where((xcremanuevo*xcremanuevo+ycremanuevo*ycremanuevo)>230)
#while(len(indexcafe[0])>1):
#	xcafenuevo[indexcafe]=xcafe[indexcafe] + np.random.normal(0,sigma)
#	ycafenuevo[indexcafe]=ycafe[indexcafe] + np.random.normal(0,sigma)
#	indexcafe=np.where((xcafenuevo*xcafenuevo+ycafenuevo*ycafenuevo)>=230)
#while(len(indexcrema[0])>1):
#	xcremanuevo[indexcrema]=xcrema[indexcrema] + np.random.normal(0,sigma)
#	ycremanuevo[indexcrema]=ycrema[indexcrema] + np.random.normal(0,sigma)
#	indexcrema=np.where((xcremanuevo*xcremanuevo+ycremanuevo*ycremanuevo)>=230) 



	
