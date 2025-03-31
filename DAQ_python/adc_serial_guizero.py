import serial
import time
import matplotlib.pyplot as plt
import csv
from guizero import App, PushButton, Text

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

# 🔹 Funkcja zapisująca dane do pliku CSV
def save_to_csv(timestamps, voltages):
    with open('dane_pomiarowe.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Czas (s)', 'Napięcie (V)'])  # Nagłówki kolumn
        for t, v in zip(timestamps, voltages):
            writer.writerow([t, v])
    print("✅ Dane zapisane do pliku dane_pomiarowe.csv")

# 🔹 Funkcja zatrzymująca pomiar
def stop_measurement():
    global running
    running = False  # Zatrzymanie pętli pomiaru
    save_to_csv(timestamps, voltages)  # Zapisz dane
    status_text.value = "Pomiar zakończony."  # Wyświetl status
    print("🛑 Zatrzymano pomiar.")

# 🔹 Funkcja rozpoczynająca pomiar
def start_measurement():
    global running
    running = True
    status_text.value = "Pomiar w trakcie..."  # Wyświetl status
    start_time = time.time()

    while running:
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

                # 🔹 Aktualizacja wyniku na GUI
                result_text.value = f"Napięcie: {voltage:.2f} V"

        except ValueError:
            print("⚠️ Błąd konwersji danych - pominięto niepoprawny odczyt.")
        except KeyboardInterrupt:
            print("\n🛑 Zakończono program.")
            break

# 🔹 Inicjalizacja GUI
app = App("Pomiar Napięcia", width=400, height=300)

# 🔹 Etykieta do wyświetlania statusu pomiaru
status_text = Text(app, text="Kliknij Start, aby rozpocząć pomiar.", size=12, color="blue", height=2)

# 🔹 Etykieta do wyświetlania wyniku pomiaru
result_text = Text(app, text="Napięcie: 0.00 V", size=14, color="red")

# 🔹 Przyciski do sterowania pomiarem
start_button = PushButton(app, command=start_measurement, text="Start", width=10, height=2)
stop_button = PushButton(app, command=stop_measurement, text="Stop", width=10, height=2)

# 🔹 Połączenie z Arduino
try:
    ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Poczekaj na stabilizację połączenia
    print("✅ Połączono z Arduino!")

    # Uruchomienie GUI
    app.display()

except serial.SerialException:
    print("❌ Błąd: Nie można otworzyć portu szeregowego.")
    status_text.value = "Błąd połączenia z Arduino."
except KeyboardInterrupt:
    print("\n🛑 Zakończono program.")
    save_to_csv(timestamps, voltages)  # Zapisz dane do pliku przy zakończeniu
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()

