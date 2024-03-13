int LED=13;
int LDR=A0;

void setup()
{
  pinMode(LED, OUTPUT);
  pinMode(LDR, INPUT);
  Serial.begin(9600);
}

void loop()
{
  int sensorval = analogRead(LDR);
  Serial.println(sensorval);
  delay(500);
  if(sensorval < 600)
    digitalWrite(LED, HIGH);
  else
    digitalWrite(LED, LOW);
  delay(500);
}
