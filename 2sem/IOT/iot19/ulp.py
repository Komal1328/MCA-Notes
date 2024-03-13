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
LDR_PIN = 5
PIR_PIN=27

GPIO.output(GPIO_TRIG, GPIO.LOW)
GPIO.setup(LIGHT_PIN, GPIO.OUT)
GPIO.output(LIGHT_PIN, False)

def readLDR(LDR_PIN):
    GPIO.setup(LDR_PIN, GPIO.OUT)
    GPIO.output(LDR_PIN, False)
    time.sleep(0.1)
    GPIO.setup(LDR_PIN, GPIO.IN)
    return GPIO.input(LDR_PIN)

def readPIR(PIR_PIN):
        GPIO.setup(PIR_PIN, GPIO.OUT)
        GPIO.output(PIR_PIN, False)
        time.sleep(0.1)
        GPIO.setup(PIR_PIN, GPIO.IN)
        return GPIO.input(PIR_PIN)

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
    
    distance=readUltra(GPIO_TRIG,GPIO_ECHO)
    i=readLDR(LDR_PIN)
    j=readPIR(PIR_PIN)

    print ("Distance: ",distance, "cm","LIGHT", i,"Intruder",j) 
    
    if(distance<10 and i== True and j== True):
        GPIO.output(LIGHT_PIN, True)
    else:
        GPIO.output(LIGHT_PIN, False)       

GPIO.cleanup()


