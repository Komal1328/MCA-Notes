// C++ code
//
const int trigger=3;
const int echo=2;
int LED1=12; //RED
int LED2=9;  //Green
int LED3=7;  //blue
int PIR=2;
long duration,inches,ft,cm;

void setup()
{
  pinMode(trigger, OUTPUT);
  pinMode(echo,INPUT);
  pinMode(PIR,INPUT);
  pinMode(LED1,OUTPUT);
  pinMode(LED2,OUTPUT);
  pinMode(LED3,OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(trigger, LOW);
  delayMicroseconds(100);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(100);
  digitalWrite(trigger, LOW);
  pinMode(echo,INPUT);
  duration=pulseIn(echo,HIGH);
  
  //The speed of sound is 343 m/s or 29.1 microsecond per cm
  //The ping travels out and back, so to find the distance of the 
  //object we take half of distance travelled
  
  //cm=(duration/2)/29.1;
  
  //According to Parallax's datasheet for PING))), there are 
  //73.746 microseconds per inch (i.e sound travels at 1130 feet 
  //per second ).this gives the distance travelled by the ping, 
  //outbound and return, so we divide by 2 to get the distance 
  //of obstacle.  
  
  inches=(duration/2)/74;
  ft=inches/12;
  Serial.print("Duration: ");
  Serial.print(ft);
  Serial.print(" Feet: ");
  //Serial.print(cm);
  //Serial.println("cm");
  
  if(ft < 3 && PIR == 1)
  {
    digitalWrite(LED2,LOW);
  	digitalWrite(LED3,LOW);
    digitalWrite(LED1,HIGH);
  }
  else if(ft > 3 && ft < 5 && PIR == 1)
  {
    digitalWrite(LED1,LOW);
    digitalWrite(LED3,LOW);
    digitalWrite(LED2,HIGH);
  }
  else 
  {
    digitalWrite(LED1,LOW);
    digitalWrite(LED2,LOW);
    digitalWrite(LED3,HIGH);
  }
  delay(100);
}