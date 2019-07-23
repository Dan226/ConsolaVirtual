import numpy as np
import matplotlib.pyplot as plt
import random

datos = np.genfromtxt("Canal_ionico.txt")
xold = datos[:,0]
yold = datos[:,1]

def radio(x, y):
    return (x**2+y**2)


def MC(xo,yo,pasos,sigma):
    x = []
    y = []
    radios = np.zeros(len(xo))
    r = []
    for i in range(len(xo)):
        radios[i] = radio(xo[i], yo[i])
        
    r_min = min(radios)
    xold = xo[0]
    yold = yo[0]
    
    for i in range(pasos):
        xnew = np.random.normal(xold, sigma,1)
        ynew = np.random.normal(yold, sigma,1)
        rnew = (xnew**2+ynew**2)**0.5
        alfa = radio(xnew,ynew)/radio(xold,yold)
        if(rnew<=r_min): 
            if(alfa>1):
                x.append(xnew)
                y.append(ynew)
                r.append(rnew)
            else:
                beta = np.random.uniform(1,1,0)
                if(beta>alfa):
                    x.append(xold)
                    y.append(yold)
                    r.append(rold)

                else:
                    x.append(xnew)
                    y.append(ynew)
                    r.append(rnew)
                    xold = xnew
                    yold = ynew
                    rold = rnew
                    
                
    return x,y,r_min
        
    
xnew, ynew, r = MC(xold,yold,100,0.1)    
 
    
fig, ax = plt.subplots()
plt.axis('equal')
circle1 = plt.Circle((5,5),  r, color='r',fill=False)
plt.scatter(xold,yold,color = "black", s = 1)
ax.add_artist(circle1)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Canal")
plt.savefig("Canal.png")
plt.close()



