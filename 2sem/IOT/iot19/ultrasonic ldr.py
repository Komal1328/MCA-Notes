import RPi.GPIO as GPIO 
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO_TRIG = 11 
GPIO_ECHO = 18
GPIO.setup(GPIO_TRIG, GPIO.OUT) 
GPIO.setup(GPIO_ECHO, GPIO.IN)

ldr_thrhold = 100000
LIGHT_PIN= 3
LDR = 5

GPIO.output(GPIO_TRIG, GPIO.LOW)
GPIO.setup(LIGHT_PIN, GPIO.OUT)
GPIO.output(LIGHT_PIN, False)

def readLDR(LDR):
    GPIO.setup(LDR, GPIO.OUT)
    GPIO.output(LDR, False)
    time.sleep(0.1)
    GPIO.setup(LDR, GPIO.IN)
    return GPIO.input(LDR)

while True:
    time.sleep(2) 
    GPIO.output(GPIO_TRIG, GPIO.HIGH) 
    time.sleep(0.00001) 
    GPIO.output(GPIO_TRIG, GPIO.LOW)
    while GPIO.input(GPIO_ECHO)==0: 
        start_time = time.time() 
    while GPIO.input(GPIO_ECHO)==1: 
        Bounce_back_time = time.time()
    
    i=readLDR(LDR)
    pulse_duration = Bounce_back_time - start_time 

    distance = round(pulse_duration * 17150, 2) 

    print ("Distance: ",distance, "cm","LIGHT", i) 
    
    if(distance<10 and i== True):
        GPIO.output(LIGHT_PIN, True)
    else:
        GPIO.output(LIGHT_PIN, False)       

GPIO.cleanup()

