# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:50:57 2024

@author: KD

Przykład DFT sygnału harmonicznego i niedopasowanie okna
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy.fftpack as fft


A=50; fsin=100; fi=np.pi/4
#To = 4/fsin
To=3.73/fsin
N=64
Ts = To/N
fs = 1/Ts
t = np.arange(0,To,Ts)
tbis=t[1:len(t)-1]

x = 10 + A*np.cos(2*np.pi*fsin*t+fi)
n = np.arange(N); k=n

plt.subplot(211); plt.stem(n,x); plt.title('Wykres próbek czasowych sygnału')

y = fft.fft(x)
plt.subplot(212), plt.stem(k, np.abs(y)/N)
plt.title('Unormowane widmo apmplitudowe'); plt.xlabel('k')

