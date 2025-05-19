import numpy as np
import matplotlib.pyplot as plt

# --- 1. Parametry sygnału ---
fs   = 1000          # częstotliwość próbkowania [Hz]
T    = 1.0           # długość sygnału [s]
N    = int(fs*T)     # liczba próbek
t    = np.arange(N) / fs

# --- 2. Sygnał testowy ---
sig  = 0.7*np.sin(2*np.pi*50*t) + 1.0*np.sin(2*np.pi*120*t)
sig += 0.5*np.random.randn(N)   # biały szum

# --- 3. FFT ---
X    = np.fft.fft(sig)
freq = np.fft.fftfreq(N, d=1/fs)

# interesuje nas tylko dodatnia połowa widma
half = slice(0, N//2)

# --- 4. Wykres ---
plt.figure(figsize=(8,4))
plt.plot(freq[half], np.abs(X[half]) * 2 / N)   # skala amplitudowa
plt.title("Widmo amplitudowe sygnału")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("|X(f)|")
plt.grid(True)
plt.tight_layout()
plt.show()
