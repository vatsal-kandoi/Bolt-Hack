import RPi.GPIO as GPIO
import modules.buttons as button
import time

GPIO.setmode(GPIO.BCM)
a=26;
b=19
c=13
d=6
e=5
f=11
GPIO.setwarnings(False);
GPIO.setup(a, GPIO.IN) 
GPIO.setup(b, GPIO.IN) 
GPIO.setup(c, GPIO.IN) 
GPIO.setup(d, GPIO.IN) 
GPIO.setup(e, GPIO.IN) 
GPIO.setup(f, GPIO.IN) 
print(button.brailleInput(a,b,c,d,e,f));
GPIO.cleanup();
