import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq

# ---------------- Parametry ----------------
fs   = 1000           # Hz – próbkowanie
N    = 256            # liczba próbek (moc 2 = wygodna dla FFT)
t    = np.arange(N) / fs

f_sig = 40.3          # NIE-całkowita wielokrotność fs/N → przeciek
amp   = 1.0

# ---------------- Sygnał -------------------
x = amp * np.sin(2 * np.pi * f_sig * t)

# ---------------- FFT: brak okna -----------
X  = fft(x)
f  = fftfreq(N, 1 / fs)

# ---------------- FFT: okno Hann -----------
w     = np.hanning(N)
Xwin  = fft(x * w)
Xwin *= N / w.sum()          # korekta tłumienia okna

# ---------------- Wykresy ------------------
half = slice(0, N // 2) 

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.stem(f[half], 2 * np.abs(X[half]) / N, basefmt=" ")
plt.title("Bez okna – silny przeciek")
plt.xlabel("f [Hz]")
plt.ylabel("|X|")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.stem(f[half], 2 * np.abs(Xwin[half]) / N, basefmt=" ")
plt.title("Okno Hann – przeciek zredukowany")
plt.xlabel("f [Hz]")
plt.grid(True)

plt.tight_layout()
plt.show()
