import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq

# ---------------- Parametry ----------------
fs = 1000               # [Hz] – częstotliwość próbkowania
f1 = 200                # [Hz] – pierwsza sinusoida
f2 = 220                # [Hz] – druga sinusoida (blisko)
A1 = 1.0
A2 = 0.8
Ns = [128, 512, 2048]   # Długości okna pomiarowego

# ---------------- Wykres ----------------
plt.figure(figsize=(15, 4))

for i, N in enumerate(Ns, 1):
    t = np.arange(N) / fs
    x = A1 * np.sin(2*np.pi*f1*t) + A2 * np.sin(2*np.pi*f2*t)

    # FFT
    X = fft(x)
    f = fftfreq(N, 1/fs)
    half = slice(0, N//2)
    mag = 2 * np.abs(X[half]) / N

    # Δf = fs / N
    delta_f = fs / N

    # Wykres
    plt.subplot(1, len(Ns), i)
    plt.stem(f[half], mag, basefmt=" ")
    plt.title(f"N = {N}, Δf = {delta_f:.2f} Hz")
    plt.xlabel("f [Hz]")
    if i == 1:
        plt.ylabel("|X|")
    plt.xlim(100, 300)
    plt.grid(True)

plt.tight_layout()
plt.show()
