// C++ code
//
const int trigger=3;
const int echo=2;
int LED1=12;
int LED2=9;
int LED3=7;
long duration,inches,cm;

void setup()
{
  pinMode(trigger, OUTPUT);
  pinMode(echo,INPUT);
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
  
  cm=(duration/2)/29.1;
  
  //According to Parallax's datasheet for PING))), there are 
  //73.746 microseconds per inch (i.e sound travels at 1130 feet 
  //per second ).this gives the distance travelled by the ping, 
  //outbound and return, so we divide by 2 to get the distance 
  //of obstacle.  
  
  inches=(duration/2)/74;
  Serial.print("Duration: ");
  Serial.print(inches);
  Serial.print(" Inches: ");
  Serial.print(cm);
  Serial.println("cm");
  
  if(inches >= 0 && inches < 25 )
  {
    digitalWrite(LED2,LOW);
  	digitalWrite(LED3,LOW);
    digitalWrite(LED1,HIGH);
  }
  else if(inches >= 25 && inches < 50)
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