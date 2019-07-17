# Ejercicio 1

import numpy as np
import matplotlib.pylab as plt
import random
import time


# Use esta funcion que recibe un valor x y retorna un valor f(x) donde f es la forma funcional que debe seguir su distribucion. 
def mifun(x):
    x_0 = 3.0
    a = 0.01
    return np.exp(-(x**2))/((x-x_0)**2 + a**2)

# Dentro de una funcion que reciba como parametros el numero de pasos y el sigma de la distribucion gausiana que va a usar para calcular el paso de su caminata, implemente el algortimo de Metropolis-Hastings. Finalmente, haga un histograma de los datos obtenidos y grafique en la misma grafica, la funcion de distribucion de probabilidad fx (Ojo, aca debe normalizar). Guarde la grafica sin mostrarla en un pdf. Use plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf"), donde sigma y pasos son los parametros que recibe la funcion. 
x = np.linspace(-10,10,1000)
plt.figure()
plt.plot(x, mifun(x))
plt.savefig("funcion")


def MCMC(sigma, pasos):
    x = np.linspace(0,1,pasos)
    z = np.linspace(0,1,pasos)
    x[0] = np.random.uniform(-10,10,1)
    alfa = 0
    for i in range(pasos-1):
        s = np.random.normal(0,sigma,1)
        alfa = (mifun(s)/mifun(x[i]))
        if(alfa > 1):
            x[i+1] = s
        else:
            beta = np.random.uniform(0,1,1)
            if(beta < alfa):
                x[i+1] = s
            else:
                x[i+1] = x[i]
                
    plt.figure()
    count, bins, ignored = plt.hist(x, 100, density = True)
    plt.title("distribucion uniforme")
    plt.xlabel("X")
    plt.ylabel("Cantidad")
    plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf")

    
MCMC(5, 100000 )        
MCMC(0.2, 100000 )    
MCMC(0.01, 100000 )    
MCMC(0.1, 1000)    
MCMC(0.1, 100000 )  
 
    
    
   # 

# Cuando haya verificado que su codigo funciona, use los siguientes parametros:
# sigma = 5, pasos =100000 
# sigma = 0.2, pasos =100000 
# sigma = 0.01, pasos =100000 
# sigma = 0.1, pasos =1000 
# sigma = 0.1, pasos =100000 
# este puede ser muy demorado dependiendo del computador: sigma = 0.1, pasos =500000 

# Al ejecutar el codigo, este debe generar 6 (o 5) graficas .pdf una para cada vez que se llama a la funcion.
