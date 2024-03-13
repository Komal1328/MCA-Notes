
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
mq_thrhold = 100000
LIGHT_PIN= 3
MQ = 5
GPIO.setup(LIGHT_PIN, GPIO.OUT)
GPIO.output(LIGHT_PIN, False)
while True:
    
    time.sleep(0.1)
    GPIO.setup(MQ, GPIO.IN)
    i = GPIO.input(MQ)
    print("i=",i)
    if i == True:
        print("OODBATHI HOGE is THERE", i)
        GPIO.output(LIGHT_PIN, True)
    elif i == False:
        print(" OODBATHI HOGE IS not THERE", i)
        GPIO.output(LIGHT_PIN, False)

GPIO.cleanup()
exit()

