#Ilustracja tw. o próbkowaniu
import numpy as np
import matplotlib.pyplot as plt

#próbkowanie sygnału harmonicznego
fsin = 10
Tokna = 0.8

#Próbkowanie sygnału analogowego
fs = 14   #częstotliwosc próbkowania
Ts = 1/fs
td = np.arange(0, Tokna, Ts)
xd = np.sin(2*np.pi*fsin*td)
plt.subplot(211)
plt.stem(td, xd)
#plt.step(td,xd)
#plt.show()

#Postać krzywej oryginalnej
t = np.arange(0,Tokna,0.001)
x = np.sin(2*np.pi*fsin*t)
plt.plot(t, x, 'red')

#Odtworzenie krzywej
z=0
for k in range(len(td)):
    #xr = xd[k]*np.sin((np.pi/Ts)*(t-k*Ts))/((np.pi/Ts)*(t-k*Ts))
    xr = xd[k]*np.sin((np.pi/Ts)*(t-(k-1)*Ts))/((np.pi/Ts)*(t-(k-1)*Ts))
    z += xr
plt.subplot(212)
plt.plot(t, z)