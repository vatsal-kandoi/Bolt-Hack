import RPi.GPIO as GPIO
import modules.buttons as button

GPIO.setmode(GPIO.BOARD)
a=14;
b=15
c=18
d=2
e=3
f=4
GPIO.setup(a, GPIO.OUT) 
GPIO.setup(b, GPIO.OUT) 
GPIO.setup(c, GPIO.OUT) 
GPIO.setup(d, GPIO.OUT) 
GPIO.setup(e, GPIO.OUT) 
GPIO.setup(f, GPIO.OUT) 

button.brailleOutput(a,b,c,d,e,f,"a");
