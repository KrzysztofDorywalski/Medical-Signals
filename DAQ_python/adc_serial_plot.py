import serial
import time
import matplotlib.pyplot as plt

# 🔹 Ustawienia portu (dostosuj do swojego systemu)
PORT = 'COM6'  # Windows: np. 'COM3', Linux/macOS: '/dev/ttyUSB0'
BAUD_RATE = 9600  # Musi być taki sam jak w Arduino

# 🔹 Inicjalizacja list do przechowywania danych
timestamps = []
voltages = []

# 🔹 Inicjalizacja wykresu
plt.ion()  # Tryb interaktywny
fig, ax = plt.subplots()
ax.set_xlabel("Czas (s)")
ax.set_ylabel("Napięcie (V)")
ax.set_title("Pomiar napięcia w czasie rzeczywistym")

try:
    # 🔹 Połączenie z Arduino
    ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Poczekaj na stabilizację połączenia
    print("✅ Połączono z Arduino!")

    start_time = time.time()

    while True:
        try:
            # 🔹 Odczyt linii z portu szeregowego
            data = ser.readline().decode('utf-8').strip()
            if data:
                voltage = float(data)  # Konwersja na liczbę
                current_time = time.time() - start_time  # Czas od startu

                # 🔹 Dodanie danych do listy
                timestamps.append(current_time)
                voltages.append(voltage)

                # 🔹 Ograniczenie liczby próbek (dla wydajności)
                if len(timestamps) > 100:
                    timestamps.pop(0)
                    voltages.pop(0)

                # 🔹 Aktualizacja wykresu
                ax.clear()
                ax.plot(timestamps, voltages, color="red", label="Napięcie (V)")
                ax.set_xlabel("Czas (s)")
                ax.set_ylabel("Napięcie (V)")
                ax.set_title("Pomiar napięcia w czasie rzeczywistym")
                ax.legend()
                plt.pause(0.1)

                # 🔹 Wydruk wyniku na konsoli
                print(f"📟 Odczytane napięcie: {voltage:.2f} V")

        except ValueError:
            print("⚠️ Błąd konwersji danych - pominięto niepoprawny odczyt.")
        except KeyboardInterrupt:
            print("\n🛑 Zakończono program.")
            break

except serial.SerialException:
    print("❌ Błąd: Nie można otworzyć portu szeregowego.")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
