import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq

# ----------- Parametry -------------
f_sig = 800          # Hz – częstotliwość sinusoidy
duration = 0.02      # s – długość analizowanego fragmentu
fs_ok   = 2000       # Hz – próbkowanie poprawne
fs_bad  = 1200       # Hz – próbkowanie z aliasingiem

def compute_spectrum(fs):
    N  = int(fs * duration)
    t  = np.arange(N) / fs
    x  = np.sin(2 * np.pi * f_sig * t)
    X  = fft(x)
    f  = fftfreq(N, 1 / fs)
    half = slice(0, N // 2)
    return f[half], 2 * np.abs(X[half]) / N

f1, spec1 = compute_spectrum(fs_ok)
f2, spec2 = compute_spectrum(fs_bad)

# ----------- Wykresy -------------
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.stem(f1, spec1, basefmt=" ")
plt.title(f"Poprawne próbkowanie\nfs = {fs_ok} Hz (Δf = {fs_ok/len(f1)*2:.1f} Hz)")
plt.xlabel("f [Hz]")
plt.ylabel("|X|")
plt.grid(True)
plt.xlim(0, fs_ok / 2)

plt.subplot(1, 2, 2)
plt.stem(f2, spec2, basefmt=" ")
plt.title(f"Aliasing\nfs = {fs_bad} Hz (Δf = {fs_bad/len(f2)*2:.1f} Hz)")
plt.xlabel("f [Hz]")
plt.grid(True)
plt.xlim(0, fs_bad / 2)

plt.tight_layout()
plt.show()
