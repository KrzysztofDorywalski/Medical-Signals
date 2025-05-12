import matplotlib.pyplot as plt
import numpy as np

#ograniczenie widma
B = 14
# częstotliwoć próbkowania
fs = 2*B
# okres próbkowania
Ts = 1.0/fs
To = 1.0
t = np.arange(0,To,Ts)

f = 1
x = 3*np.sin(2*np.pi*f*t)

f = 4
x += np.sin(2*np.pi*f*t)

f =  7  
x += 0.5* np.sin(2*np.pi*f*t)

plt.figure(figsize = (8, 6))
plt.plot(t, x, 'r')
plt.ylabel('Amplitude')

plt.show()

from numpy.fft import fft, ifft

X = fft(x)

N = len(X)
k = np.arange(N)
T = N/fs
freq = k/T 

plt.figure(figsize = (12, 6))
plt.subplot(121)

plt.stem(freq, (np.abs(X)/N), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
#plt.xlim(0, 10)

plt.subplot(122)
plt.plot(t, ifft(X), 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()


#obliczenie fft z scipy
import scipy.fftpack as fft

F = fft.fft(x)
freq = fft.fftfreq(N,1.0/fs)
mask = np.where(freq>=0)
plt.figure()
plt.stem(freq[mask],2*np.abs(F[mask])/N)

