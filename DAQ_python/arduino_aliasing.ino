const int analogPin = A0;  
const int samplingRate = 5000;  // Częstotliwość próbkowania w Hz (zmieniaj, aby zobaczyć aliasing)
const int numSamples = 100;  // Liczba próbek do pobrania

void setup() {
    Serial.begin(9600);  // Komunikacja z komputerem
}

void loop() {
    for (int i = 0; i < numSamples; i++) {
        int value = analogRead(analogPin);  // Pobranie wartości z A0
        Serial.println(value);  // Wysłanie wartości do komputera
        delayMicroseconds(1000000 / samplingRate);  // Ustalony czas próbkowania
    }
}
