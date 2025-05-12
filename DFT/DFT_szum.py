# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:05:10 2023

@author: krzysztof
"""

from numpy import*
from matplotlib.pyplot import*

#Użycie DFT do odszukania częstotliwości sygnału ukrytego w szumie

fs = 1000      #częstotliwość próbkowania
Ts = 1/fs      #okres próbkowania
N = 150       #liczba próbek
t = arange(0,N,Ts) #wektor czasu

#sygnał sinusoidalny o częstotliwości 50 Hz i amplitudzie 0.7 oraz 120 Hz
#sinusoida o amplitudzie 1
signal = 0.7*sin(2*pi*50*t) + sin(2*pi*120*t)

#dodanie szumu białego o wartości średniej 0 i wariancji 4
X = signal + 2*random.normal(scale=4 ,size=len(signal))

#sygnał w dziedzinie czasu
plot(1000*t[:150],X[:150]);
title('Sygnał zaszumiony');
xlabel('t / ms'), ylabel('x(t)');


#DFT + widmo amplitudowe (pierwsza połówka)
Y = fft.fft(X);
k = arange(len(X))
fk = (k*fs)/N

figure()
stem(fk, (abs(Y)/N))

'''
P2 = abs(Y/N);
P1 = P2[1:N/2+1]
P1[2:len(P2)-1] = 2*P1[2:len(P2)-1];

f = fs*(0:(N/2))/N;

figure()
plot(f,P1);
title('widmo amplitudowe'), xlabel('f / Hz'), ylabel('abs(Y)');
'''