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
f21 = np.fft.fftshift(imagen1)
df22 = fft2(imagen2)
f22 = np.fft.fftshift(imagen2)

######## Se grafica el espectro de Fourier
plt.figure()
a = plt.imshow(abs(df21), norm = LogNorm())
cbar = plt.colorbar(a)
plt.xlabel("w")
plt.ylabel("F(w)")
plt.title("Espectro de Fourier imagen 1")
plt.savefig("FFT-2D-Imagen1")

plt.figure()
b = plt.imshow(abs(df22), norm = LogNorm())
cbar = plt.colorbar(a)
plt.xlabel("w")
plt.ylabel("F(w)")
plt.title("Espectro de Fourier imagen 2")
plt.savefig("FFT-2D-Imagen2")

######## Se realizan filtros pasa-altos y pasa-bajos para realizar la imagen híbrida.
def filtro1(fc, amp):
    for i in range(np.shape(amp)[1]):
        for j in range(np.shape(amp)[0]):
            if(amp[j,i]>fc):
                amp[j,i] = 0
    return amp

def filtro2(fc, amp):
    for i in range(np.shape(amp)[1]):
        for j in range(np.shape(amp)[0]):
            if(amp[j,i]<fc):
                amp[j,i] = 0
    return amp

fc = 100
freqfiltro1 = filtro1(fc,df21)  
freqfiltro2 = filtro2(100,df22)

plt.figure()
a = plt.imshow(abs(freqfiltro1), norm = LogNorm(), vmin = 100, vmax = 1200)
cbar = plt.colorbar(a)
plt.xlabel("w")
plt.ylabel("F(w)")
plt.title("Filtro imagen 1")
plt.savefig("FFT2Dfiltro1")   

plt.figure()
b = plt.imshow(abs(freqfiltro2), norm = LogNorm(), vmin = 100, vmax = 1200)
cbar = plt.colorbar(b)
plt.xlabel("w")
plt.ylabel("F(w)")
plt.title("Filtro imagen 2")
plt.savefig("FFT2Dfiltro2")   
 
###########Transformada inversa
filtrototal = np.zeros([np.shape(df21)[0],np.shape(df21)[1]])

for i in range(np.shape(df21)[1]):
    for j in range(np.shape(df21)[0]):
        filtrototal[j][i] = abs(freqfiltro1[j][i] + freqfiltro2[j][i])

if2 = ifft2(filtrototal)

plt.figure()
plt.imshow(abs(if2), cmap = "gist_gray", interpolation = "bessel")
plt.savefig("ImFiltrada")

