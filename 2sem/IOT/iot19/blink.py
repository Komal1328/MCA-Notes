[Desktop Entry]
Type=Link
Name=blink.py
Icon=text-x-python
URL=smb://172.1.26.10/users/IoT/RPi%20Programs/blink.py
import RPi.GPIO as GPIO
import time
pin =2

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
GPIO.setup(pin,False)
while True:
    try:
        GPIO.output(pin,True)
        time.sleep(0.1)
        GPIO.output(pin,False)
        time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
