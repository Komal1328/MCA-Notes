#include<dht.h>
#define dataPin 8 // defines pin number to which sensor is connected
dht DHT;
int LED1=3; //green
int LED2=4; //red
int LED3=13; //yellow

void setup() {
  // put your setup code here, to run once:
  pinMode(LED1,OUTPUT);
  pinMode(LED2,OUTPUT);
  pinMode(LED3,OUTPUT);
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
  Serial.print("Humidity = ");
  Serial.print(h);
  Serial.print(" % ");
  Serial.println(" ");
  if(t>=22 && h>=75 && h<=80)
  {
    digitalWrite(LED1,HIGH);
    digitalWrite(LED2,LOW);
    digitalWrite(LED3,LOW);
  }
  else if(t>=22 && h>80 && h<=85)
  {
    digitalWrite(LED2,HIGH);
    digitalWrite(LED1,LOW);
    digitalWrite(LED3,LOW);
  }
  else if(t>=22 && h>85 && h<=90)
  {
    digitalWrite(LED3,HIGH);
    digitalWrite(LED1,LOW);
    digitalWrite(LED2,LOW);
  }
  delay(500);
}
