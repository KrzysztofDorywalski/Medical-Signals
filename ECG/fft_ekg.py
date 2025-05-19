import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ---------------- 1. EKG z SciPy ----------------
ekg = signal.electrocardiogram()   # ~10 h zapisu
fs  = 360                          # [Hz] – stałe w dataset-cie SciPy

# bierzemy pierwszy, 10-sekundowy wycinek
duration = 10          # [s]
N = int(fs * duration)
x = ekg[:N]
t = np.arange(N) / fs

# ---------------- 2. FFT ----------------
X   = np.fft.fft(x * np.hanning(N))   # okno Hann, by ograniczyć przeciek
freq = np.fft.fftfreq(N, 1/fs)
half = slice(0, N//2)                 # tylko dodatnie f
mag  = 2 * np.abs(X[half]) / N        # skala amplitudowa

# ---------------- 3. Wykresy ----------------
plt.figure(figsize=(12,4))

# sygnał w czasie
plt.subplot(1,2,1)
plt.plot(t, x)
plt.title("EKG – 10 s")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [mV]")
plt.xlim(0, 10)
plt.grid(True)

# widmo
plt.subplot(1,2,2)
plt.stem(freq[half], mag, basefmt=" ")
plt.title("Widmo amplitudowe (okno Hann)")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("|X|")
plt.xlim(0, fs/2)          # 0 – 180 Hz
plt.grid(True)

plt.tight_layout()
plt.show()
