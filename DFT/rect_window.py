#widmo okna prostokątnego
import numpy as np
import matplotlib.pyplot as plt

#impuls ciągły
t = np.arange(-0.5,2,0.01)
rect = np.zeros(len(t))
for i in range(len(t)):
    if t[i] >= 0 and t[i] <=1:
        rect[i] = 1
plt.subplot(211), plt.plot(t,rect), plt.title('Impuls prostokątny ciągły')

#impuls dyskretny
N = 20
Ts = 0.1
To = N*Ts
td = np.arange(-0.5, To, Ts)
rectd = np.zeros(len(td))
for i in range(len(td)):
    if td[i] >= -Ts and td[i] <=1:
        rectd[i] = 1
plt.subplots_adjust(hspace=0.6)
plt.subplot(212), plt.stem(td,rectd), plt.title('Impuls prostokątny ciągły')

#DFT N próbek
W = np.exp(-1j*2*np.pi/N)
X = [0+1j]*(N+1)
X[0] = 1
X0 = 0
for k in range(1,N+1):
    X0 = 0
    for n in range(1,N+1):
        X[k] = rectd[n]*W**((k-1)*(n-1))+X0
        X0=X[k]
modul = np.absolute(X) 
km = np.arange(0, len(X))
plt.figure(), plt.stem(km, modul), plt.xlabel('k'), plt.ylabel('X(k)')
plt.title('DFT dla 20 próbek')

