#zad 1.1 z Bio sign process
#Tworzenie sygnału i jego reprezentacji dyskretnej

import numpy as np
import matplotlib.pyplot as plt

#Sygnał ciągły
t = np.arange(0,10,0.01)
x = np.exp(-2*t)

plt.subplot(211)
plt.plot(t,x, color='red')
plt.xlabel('t / s')
plt.ylabel('exp(-2t)')
plt.title('Sygnał ciągły')

#Sygnał dyskretny
Ts = 0.1
td = np.arange(0,10,Ts)
xd = np.exp(-2*td)

plt.subplot(212)
plt.plot(td,xd, 'o')
