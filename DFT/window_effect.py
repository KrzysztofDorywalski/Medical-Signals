import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy.fftpack as fft

# Generacja sygnału
#K=99 # Okno o całkowitej wielokrotności okresu sinusoidy
K=125 # Okno o niecałkowitej wielokrotności okresu sinusoidy
t = np.arange(0,K)*0.02
x = np.sin(2*np.pi*t+np.pi/2)

# Generacja okien funkcyjnych
wt=signal.triang(K)
wh=signal.hamming(K)
wb=signal.blackman(K)
xt=x*wt
xh=x*wh
xb=x*wb

#f=((1:K)-(K+1)/2)/K*50;
plt.subplot(5,1,1), plt.plot(t,x), plt.grid(), plt.xlabel('t'), plt.title('Postać czasowa sygnału')

y=fft.fft(x) 
f = fft.fftfreq(K,0.02)
plt.subplot(5,1,2), plt.stem(f,abs(y)/K), plt.grid(), plt.xlim([-5,5]), plt.xlabel('f')

y=fft.fft(xt) 
f = fft.fftfreq(K,0.02)
plt.subplot(5,1,3), plt.stem(f,abs(y)/K), plt.grid(), plt.xlim([-5,5]), plt.xlabel('f')

y=fft.fft(xh) 
f = fft.fftfreq(K,0.02)
plt.subplot(5,1,4), plt.stem(f,abs(y)/K), plt.grid(), plt.xlim([-5,5]), plt.xlabel('f')

y=fft.fft(xb) 
f = fft.fftfreq(K,0.02)
plt.subplot(5,1,5), plt.stem(f,abs(y)/K), plt.grid(), plt.xlim([-5,5]), plt.xlabel('f')
