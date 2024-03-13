#include<dht.h>
#define dataPin 8 // defines pin number to which sensor is connected
dht DHT;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int readData = DHT.read11(dataPin);
  //int readData=DHT.read22(dataPin);

  float t = DHT.temperature;
  float h = DHT.humidity;

  Serial.print("Temperature = ");
  Serial.print(t);
  Serial.print(" ");
  Serial.print((char)176);
  Serial.print("C | ");
  Serial.print((t * 9.0)/5.0 +32.0);
  Serial.print(" ");
  Serial.print((char)176);
  Serial.print("F ");
  Serial.print("Humidity = ");
  Serial.print(h);
  Serial.print(" % ");
  Serial.print(" ");
  delay(2000);
}
