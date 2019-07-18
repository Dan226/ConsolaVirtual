#Ejercicio 1 Terminar lo que hizo en clase + dos preguntas adicionales (en mayusculas en el texto)

import numpy as np
import matplotlib.pylab as plt


# 1) lea los datos de resorte.dat y almacenelos.
# 
datos = np.genfromtxt("resorte.dat")
t = datos[:,0]
x = datos[:,1]


# Los datos corresponden a las posiciones en x de un oscilador (masa resorte) en funcion del tiempo. La ecuacion de movimiento esta dada por

# xt=a*np.exp(-gamma*t)*np.cos(omega*t)
# Donde a, gamma, y omega son parametros.
def f(a, gamma, omega, t):
    return a*np.exp(-gamma*t)*np.cos(omega*t)

# 2) Implemente un algoritmo que le permita, por medio de estimacion bayesiana de parametros, encontrar los parametros correspondientes a los datos d. Para esto debe:

# 2a.) definir una funcion que reciba los parametros que se busca estimar y los datos de tiempo y retorne el modelo  

def likelihood(chi):
    return np.exp(-0.5*chi)

def bayes(aini,gini,oini,tiempo,obs,s1,s2,s3,pasos):
    an = []
    a = []
    av = []
    gn = []
    gv = []
    g = []
    on = []
    ov = []
    o = []
    Lm = []
    ymodn = np.zeros(len(tiempo))
    ymodv = np.zeros(len(tiempo))
    alfa = 0.0
    chin= 0.0 
    chiv= 0.0 
    Ln= 0.0
    Lv = 0.0
    av =aini 
    gv=gini 
    ov=oini
    a.append(aini), g.append(gini), o.append(oini)
    
    
    #Montecarlo Hasting
    for i in range(pasos-1):
        an=np.random.normal(0,s1,1)
        gn=np.random.normal(0,s2,1) 
        on=np.random.normal(0,s3,1)
        for i in range(len(tiempo)):
            ymodn[i] = f(an,gn,on,t[i])
            ymodv[i] = f(av,gv,ov,t[i])

        #chi cuadrado    
        chiv = np.sum((obs-ymodv)**2)
        chin = np.sum((obs-ymodn)**2)
         

        #Likelihood
        Ln = likelihood(chin)
        Lv = likelihood(chiv)
        
        if(Lv != 0.0):
            alfa = (Ln/Lv)
            if(alfa > 1):
                a.append(an), g.append(gn), o.append(on), Lm.append(Ln)
                av =an
                gv = gn
                ov = on
            else:
                beta = np.random.uniform(0,1,1)
                if(beta < alfa):
                    a.append(av), g.append(gv), o.append(ov), Lm.append(Lv)
                    av =an 
                    gv = gn 
                    ov = on
                else:
                    a.append(an), g.append(gn), o.append(on), Lm.append(Ln)
                    av =an 
                    gv = gn 
                    ov = on
        
               
          
    L = np.max(Lm)
    s = np.where(Lm == L)
    for i in range(pasos-1):
        if(Lm[i] == L):
            alfa = a[i] 
            gamma = g[i] 
            omega = o[i]

    print("Los mejores parametros son a:",alfa,",gamma:", gamma, ",omega:",omega )        
    modelo = f(alfa,gamma,omega,tiempo)
    plt.figure()
    plt.plot(tiempo,obs, label = "datos")
    plt.plot(tiempo,modelo, label = "modelo")
    plt.title("distribucion uniforme")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Elongacion (m)")
    plt.legend()
    plt.savefig("Resorte")           
    

bayes(7.5,0.6,18.2,t,x,1,1,1,100000)
    

# 2b.) Definir una funcion que retorne la funcion de verosimilitud

# 2c.) Caminata

#condiciones iniciales
aini=7.5
gammaini=0.6
omegaini=18.2

#numero de pasos
iteraciones=100000


# 2d.) Seleccione los mejores parametros E IMPRIMA UN MENSAJE QUE DIGA: "LOS MEJORES PARAMETROS SON a=... gamma=... Y omgega=..."

# 2f.) Grafique sus datos originales y su modelo con los mejores parametros. Guarde su grafica sin mostrarla en Resorte.pdf

# 3) SABIENDO QUE omega=np.sqrt(k/m), IMPRIMA UN MENSAJE DONDE EXPLIQUE SI PUEDE O NO DETERMINAR k Y m DE MANERA INDIVIDUAL USANDO EL METODO ANTERIOR. JUSTIFIQUE BIEN SU RESPUESTA (PUEDE ADEMAS HACER PRUEBAS CON EL CODIGO PARA RESPONDER ESTA PREGUNTA).



