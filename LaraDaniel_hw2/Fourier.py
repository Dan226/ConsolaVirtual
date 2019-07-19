import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq, fft2, ifft2
import scipy.ndimage as im
from matplotlib.colors import LogNorm

#######Se leen las imagenes
imagen1 = plt.imread("cara_02_grisesMF.png")
imagen2 = plt.imread("cara_03_grisesMF.png")

########Transformada de Fourier usando el paquete de scipy
df21 = fft2(imagen1)
f21 = np.fft.fftshift(df21)
df22 = fft2(imagen2)
f22 = np.fft.fftshift(df22)

######## Se grafica el espectro de Fourier
plt.figure()
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
a = plt.imshow(abs(f21), norm = LogNorm())
cbar = plt.colorbar(a)
plt.xlabel("w")
plt.ylabel("F(w)")
plt.title("Espectro de Fourier imagen 1")
plt.subplot(1,2,2)
b = plt.imshow(abs(f22), norm = LogNorm())
cbar = plt.colorbar(b)
plt.xlabel("w")
plt.ylabel("F(w)")
plt.title("Espectro de Fourier imagen 2")
plt.savefig("FFtIm.pdf")

######## Se realizan filtros pasa-altos y pasa-bajos para realizar la imagen híbrida.
def filtro1(fc, amp):
    for i in range(np.shape(amp)[0]):
        for j in range(np.shape(amp)[1]):
            if(amp[i,j]>fc):
                amp[i,j] = 0
    return amp

def filtro2(fc, amp):
    for i in range(np.shape(amp)[0]):
        for j in range(np.shape(amp)[1]):
            if(amp[i,j]<fc):
                amp[i,j] = 0
    return amp

freqfiltro1 = filtro1(55,df21)  
freqfiltro2 = filtro2(4,df22)


plt.figure()
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
a = plt.imshow(abs(freqfiltro1), norm = LogNorm(), vmin = 100, vmax = 1200)
cbar = plt.colorbar(a)
plt.xlabel("w")
plt.ylabel("F(w)")
plt.title("Filtro imagen 1")  
plt.subplot(1,2,2)
b = plt.imshow(abs(freqfiltro2), norm = LogNorm(), vmin = 100, vmax = 1200)
cbar = plt.colorbar(b)
plt.xlabel("w")
plt.ylabel("F(w)")
plt.title("Filtro imagen 2")
plt.savefig("ImProceso.pdf")   
 
###########Transformada inversa
filtrototal = np.zeros([np.shape(df21)[0],np.shape(df21)[1]])

i1 = np.fft.ifftshift(freqfiltro1)
i2 = np.fft.ifftshift(freqfiltro2)

filtrototal = i1+i2

#for i in range(np.shape(df21)[1]):
#    for j in range(np.shape(df21)[0]):
#        filtrototal[j][i] = np.fft.ifftshift(freqfiltro1[j][i]) + np.fft.ifftshift(freqfiltro2[j][i])

if2 = ifft2(filtrototal)

plt.figure()
plt.figure(figsize=(20,10))
plt.imshow(abs(if2),cmap = "gray",  norm = LogNorm())
plt.savefig("ImHybrid.pdf")

