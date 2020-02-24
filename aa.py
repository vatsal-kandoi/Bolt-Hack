import RPi.GPIO as GPIO
import modules.buttons as button
import time

GPIO.setmode(GPIO.BCM)
a=14;
b=15
c=18
d=17
e=27
f=22
GPIO.setwarnings(False);
GPIO.setup(a, GPIO.OUT) 
GPIO.setup(b, GPIO.OUT) 
GPIO.setup(c, GPIO.OUT) 
GPIO.setup(d, GPIO.OUT) 
GPIO.setup(e, GPIO.OUT) 
GPIO.setup(f, GPIO.OUT) 
button.brailleOutput(a,b,c,d,e,f,"b");
time.sleep(2);
button.brailleOutput(a,b,c,d,e,f,"b");
time.sleep(2);
GPIO.cleanup();
