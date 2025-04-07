#include <Wire.h>

const int sensorPin = A0;
const int ledPin = 13;
int threshold = 50;
int received = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
  Wire.begin(0x08); // Set Arduino I2C address
  Wire.onRequest(sendData);
  Wire.onReceive(receiveData);
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(sensorPin);
  sensorValue = map(sensorValue, 0, 1023, 0, 100);
  Serial.print("Sensor Value: ");
  Serial.println(sensorValue);

  if (received == 1 && sensorValue > threshold) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }

  delay(1000);
}

void sendData() {
  int sensorValue = analogRead(sensorPin);
  sensorValue = map(sensorValue, 0, 1023, 0, 100);
  Wire.write(sensorValue);
}

void receiveData(int byteCount) {
  while (Wire.available()) {
    received = Wire.read();
  }
}
