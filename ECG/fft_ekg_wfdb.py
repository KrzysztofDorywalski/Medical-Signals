import wfdb
import numpy as np
import matplotlib.pyplot as plt

# 1) rekord 100 z bazy MIT-BIH Arrhythmia (pierwsze 10 s)
record = wfdb.rdrecord('100', pn_dir='mitdb', sampto=3600)  # 360 Hz * 10 s
x  = record.p_signal[:,0]      # kanał MLII
fs = record.fs                 # = 360 Hz
t  = np.arange(len(x))/fs

# 2) widmo
X   = np.fft.fft(x*np.hanning(len(x)))
freq= np.fft.fftfreq(len(x), 1/fs)
half= slice(0, len(x)//2)
mag = 2*np.abs(X[half])/len(x)

# 3) wykres
plt.figure(figsize=(12,4))
plt.subplot(1,2,1); plt.plot(t, x); plt.title("EKG 10 s (MIT-BIH #100)")
plt.subplot(1,2,2); plt.stem(freq[half], mag, basefmt=" "); plt.title("Widmo")
plt.tight_layout(); plt.show()
