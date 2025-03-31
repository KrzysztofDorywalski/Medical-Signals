#Tworzenie sygnału eksponencjalny+harmoniczny trwający 6s i jego reprezentacja dyskretna

import numpy as np
import matplotlib.pyplot as plt

fig,axes = plt.subplots(2,1)
fig.subplots_adjust(hspace=1, wspace=0.3)

#Sygnał analogowy
t = np.arange(0,6,0.001)
x=2*np.exp(-0.5*t)*np.sin(3*t)
#plt.subplot(211)
axes[0].plot(t,x)
axes[0].set_title('Sygnal ciagly')
axes[0].set_xlabel('t / s')

#Sygnał dyskretny
fs = 10
Ts = 1/fs
td = np.arange(0,6,Ts)
xd=2*np.exp(-0.5*td)*np.sin(3*td)
#plt.subplot(212)
axes[1].stem(td,xd)
axes[1].set_title('Sygnał dyskretny')
axes[1].set_xlabel('t / s')
axes[1].step(td,xd, color='red')
