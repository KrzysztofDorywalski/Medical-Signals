import serial
import numpy as np
import matplotlib.pyplot as plt

port = 'COM6'  # Sprawdź w Arduino IDE
baud = 9600
samples = 100

ser = serial.Serial(port, baud, timeout=1)
data = []

for _ in range(samples):
    try:
        value = int(ser.readline().decode().strip())
        data.append(value)
    except:
        continue

ser.close()

# Tworzenie wykresu
plt.plot(data, marker='o', linestyle='-')
plt.xlabel("Numer próbki")
plt.ylabel("Napięcie ADC")
plt.title("Aliasing w próbkowaniu")
plt.show()
