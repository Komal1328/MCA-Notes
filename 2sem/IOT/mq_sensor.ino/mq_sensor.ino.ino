int LED=13;
int MQ=A0;

void setup()
{
  pinMode(LED, OUTPUT);
  pinMode(MQ, INPUT);
  Serial.begin(9600);
}

void loop()
{
  int sensorval = analogRead(MQ);
  Serial.println(sensorval);
  delay(500);
  if(sensorval > 250)
  {
    digitalWrite(LED, HIGH);
    Serial.println("Somke detected");
  }
  else
  {
    digitalWrite(LED, LOW);
    Serial.println("Somke not detected");
  }
  delay(500);
}
