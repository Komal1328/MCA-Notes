const int trigger=3;
const int echo = 2;
int LED1 = 7;
int LED2 = 8;
int LED3 = 13;
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
  digitalWrite(trigger,LOW);
  delayMicroseconds(100);
  digitalWrite(trigger,HIGH);
    delayMicroseconds(100);
	pinMode(echo,INPUT);
  duration=pulseIn(echo,HIGH);
  
//the speed of the sound is 343 m/s or 29.1 microseconds per centimeter.
  //The ping travel out and back so to find the distance of the object we can take half of the distance travelled
 cm = (duration/2)/29.1;
  
 //according to parallax datasheet for the PING)), there are 73.746 microseconds per inch(i.e sound travelled by the ping.
  //outbound and return, so we divided by 2 to get thedistance of the obstracle
  //see:http://www.parallax.com/d1/docs/prod/28015-PING-v1.3.pdf.
  
  inches=(duration/2)/74;
  Serial.print("Duration:");
  Serial.print(inches);
  Serial.print(" inches ");
  Serial.print(cm);
  Serial.println("cm");
  if(inches >= 0 && inches < 5 ){
    digitalWrite(LED1,HIGH);
  	digitalWrite(LED2,LOW);
    digitalWrite(LED3,LOW);
  }
  else if(inches >= 5 && inches < 10){
    digitalWrite(LED2,HIGH);
    digitalWrite(LED1,LOW);
  	digitalWrite(LED3,LOW);
  }
  else{
    digitalWrite(LED3,HIGH);
  	digitalWrite(LED1,LOW);
    digitalWrite(LED2,LOW);
  }
 delay(1000); // Wait for 1000 millisecond(s)
}