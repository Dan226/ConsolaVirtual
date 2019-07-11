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
plt.imshow(abs(df21), norm = LogNorm())
plt.savefig("FFT-2D-Imagen1")
plt.figure()
plt.imshow(abs(df22), norm = LogNorm())
plt.savefig("FFT-2D-Imagen2")

######## Se realizan filtros pasa-altos y pasa-bajos para realizar la imagen híbrida.
