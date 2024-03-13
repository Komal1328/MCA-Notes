
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
PIR_pin=27
pin=17
LIGHT_PIN=3
GPIO.setup(LIGHT_PIN, GPIO.OUT)
GPIO.output(LIGHT_PIN, False)
def readLDR(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)
    time.sleep(0.1)
def readPIR(PIR_pin):
        GPIO.setup(PIR_pin, GPIO.OUT)
        GPIO.output(PIR_pin, False)
        time.sleep(0.1)
    
        GPIO.setup(pin, GPIO.IN)
        GPIO.setup(PIR_pin,GPIO.IN)
        i = GPIO.input(pin)
        j = GPIO.input(PIR_pin)
        if (i&j == False):
            print("NO INTRUDER", i,j)
            GPIO.output(LIGHT_PIN, False)
        elif (i&j == True):          
            print("LIGHT DETECTED", i,j)
            GPIO.output(LIGHT_PIN, True)
try:
    while True:
        readLDR(pin)
        readPIR(PIR_pin)
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()

