import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
ldr_thrhold = 100000
mq_thrhold = 100000
LIGHT_PIN= 3
MQ = 5
LDR = 22
GPIO.setup(LIGHT_PIN, GPIO.OUT)
GPIO.output(LIGHT_PIN, False)

def readLDR(LDR):
    GPIO.setup(LDR, GPIO.OUT)
    GPIO.output(LDR, False)
    time.sleep(0.1)
    GPIO.setup(LDR, GPIO.IN)
    return GPIO.input(LDR)
    
def readMQ(MQ):
    time.sleep(0.1)
    GPIO.setup(MQ, GPIO.IN)
    return GPIO.input(MQ)

while True:
    i=readLDR(LDR);
    j=readMQ(MQ);
    if(i&j == 1):
        GPIO.output(LIGHT_PIN, True)
        print("LDR:",i," MQ:",j);
    else:
        GPIO.output(LIGHT_PIN, False)
        print("LDR:",i," MQ:",j);

GPIO.cleanup()


