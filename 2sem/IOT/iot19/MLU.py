import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
mq_thrhold = 100000

LIGHT_PIN= 3
MQ = 5
PIR = 22

GPIO.setup(LIGHT_PIN, GPIO.OUT)
GPIO.output(LIGHT_PIN, False)

GPIO_TRIG = 11 
GPIO_ECHO = 18
GPIO.setup(GPIO_TRIG, GPIO.OUT) 
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.output(GPIO_TRIG, GPIO.LOW)

def readPIR(PIR):
        GPIO.setup(PIR, GPIO.OUT)
        GPIO.output(PIR, False)
        time.sleep(0.1)
        GPIO.setup(PIR, GPIO.IN)
        return GPIO.input(PIR)
    
def readMQ(MQ):
    time.sleep(0.1)
    GPIO.setup(MQ, GPIO.IN)
    return GPIO.input(MQ)

def readUltra(GPIO_TRIG,GPIO_ECHO):
    time.sleep(2) 
    GPIO.output(GPIO_TRIG, GPIO.HIGH) 
    time.sleep(0.00001) 
    GPIO.output(GPIO_TRIG, GPIO.LOW)
    while GPIO.input(GPIO_ECHO)==0: 
        start_time = time.time() 
    while GPIO.input(GPIO_ECHO)==1: 
        Bounce_back_time = time.time()

    pulse_duration = Bounce_back_time - start_time 

    return round(pulse_duration * 17150, 2)

while True:
    i=readPIR(PIR);
    j=readMQ(MQ);
    distance=readUltra(GPIO_TRIG,GPIO_ECHO)
    
    if(i&j == 1 and distance < 10):
        GPIO.output(LIGHT_PIN, True)
        print("PIR:",i," MQ:",j,"Distance: ",distance);
    else:
        GPIO.output(LIGHT_PIN, False)
        print("PIR:",i," MQ:",j,"Distance: ",distance);

GPIO.cleanup()



