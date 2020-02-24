import RPi.GPIO as GPIO
import time;

def brailleOutput(a,b,c,d,e,f,char):
    if(char=="a"):
        GPIO.output(a,0)
        GPIO.output(b,1)
        GPIO.output(c,1)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,1)
    elif(char=="b"):
        GPIO.output(a,0)
        GPIO.output(b,0)
        GPIO.output(c,1)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,1)
    elif(char=="c"):
        GPIO.output(a,0)
        GPIO.output(b,1)
        GPIO.output(c,1)
        GPIO.output(d,0)
        GPIO.output(e,1)
        GPIO.output(f,1)
    elif(char=="d"):
        GPIO.output(a,0)
        GPIO.output(b,1)
        GPIO.output(c,1)
        GPIO.output(d,0)
        GPIO.output(e,0)
        GPIO.output(f,1)
    elif(char=="e"):
        GPIO.output(a,0)
        GPIO.output(b,1)
        GPIO.output(c,1)
        GPIO.output(d,1)
        GPIO.output(e,0)
        GPIO.output(f,1)
    elif(char=="f"):
        GPIO.output(a,0)
        GPIO.output(b,0)
        GPIO.output(c,1)
        GPIO.output(d,0)
        GPIO.output(e,1)
        GPIO.output(f,1)
    elif(char=="g"):
        GPIO.output(a,0)
        GPIO.output(b,0)
        GPIO.output(c,1)
        GPIO.output(d,0)
        GPIO.output(e,0)
        GPIO.output(f,1)
    elif(char=="h"):
        GPIO.output(a,0)
        GPIO.output(b,0)
        GPIO.output(c,1)
        GPIO.output(d,1)
        GPIO.output(e,0)
        GPIO.output(f,1)
    elif(char=="i"):
        GPIO.output(a,0)
        GPIO.output(b,0)
        GPIO.output(c,1)
        GPIO.output(d,1)
        GPIO.output(e,0)
        GPIO.output(f,1)
    elif(char=="j"):
        GPIO.output(a,1)
        GPIO.output(b,0)
        GPIO.output(c,1)
        GPIO.output(d,0)
        GPIO.output(e,0)
        GPIO.output(f,1)
    elif(char=="k"):
        GPIO.output(a,0)
        GPIO.output(b,1)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,1)
    elif(char=="l"):
        GPIO.output(a,0)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,1)
    elif(char=="m"):
        GPIO.output(a,0)
        GPIO.output(b,1)
        GPIO.output(c,0)
        GPIO.output(d,0)
        GPIO.output(e,1)
        GPIO.output(f,1)
    elif(char=="n"):
        GPIO.output(a,0)
        GPIO.output(b,1)
        GPIO.output(c,0)
        GPIO.output(d,0)
        GPIO.output(e,0)
        GPIO.output(f,1)
    elif(char=="o"):
        GPIO.output(a,0)
        GPIO.output(b,1)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,0)
        GPIO.output(f,1)
    elif(char=="p"):
        GPIO.output(a,0)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,0)
        GPIO.output(e,1)
        GPIO.output(f,1)
    elif(char=="q"):
        GPIO.output(a,0)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,0)
        GPIO.output(e,0)
        GPIO.output(f,1)
    elif(char=="r"):
        GPIO.output(a,0)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,0)
        GPIO.output(f,1)
    elif(char=="s"):
        GPIO.output(a,1)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,0)
        GPIO.output(e,1)
        GPIO.output(f,1)
    elif(char=="t"):
        GPIO.output(a,1)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,0)
        GPIO.output(e,0)
        GPIO.output(f,1)
    elif(char=="u"):
        GPIO.output(a,0)
        GPIO.output(b,1)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,0)
    elif(char=="v"):
        GPIO.output(a,0)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,0)
    elif(char=="w"):
        GPIO.output(a,1)
        GPIO.output(b,0)
        GPIO.output(c,1)
        GPIO.output(d,0)
        GPIO.output(e,0)
        GPIO.output(f,0)
    elif(char=="x"):
        GPIO.output(a,0)
        GPIO.output(b,1)
        GPIO.output(c,0)
        GPIO.output(d,0)
        GPIO.output(e,1)
        GPIO.output(f,0)
    elif(char=="y"):
        GPIO.output(a,0)
        GPIO.output(b,1)
        GPIO.output(c,0)
        GPIO.output(d,0)
        GPIO.output(e,0)
        GPIO.output(f,0)
    elif(char=="z"):
        GPIO.output(a,0)
        GPIO.output(b,1)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,0)
        GPIO.output(f,0)
    elif(char=="#"):
        GPIO.output(a,1)
        GPIO.output(b,1)
        GPIO.output(c,0)
        GPIO.output(d,0)
        GPIO.output(e,0)
        GPIO.output(f,0)
    elif(char=="0"):
        GPIO.output(a,1)
        GPIO.output(b,1)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,0)
        GPIO.output(f,0)
    elif(char=="1"):
        GPIO.output(a,1)
        GPIO.output(b,0)
        GPIO.output(c,1)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,1)
    elif(char=="2"):
        GPIO.output(a,1)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,1)
    elif(char=="3"):
        GPIO.output(a,1)
        GPIO.output(b,0)
        GPIO.output(c,1)
        GPIO.output(d,1)
        GPIO.output(e,0)
        GPIO.output(f,1)
    elif(char=="4"):
        GPIO.output(a,1)
        GPIO.output(b,0)
        GPIO.output(c,1)
        GPIO.output(d,1)
        GPIO.output(e,0)
        GPIO.output(f,0)
    elif(char=="5"):
        GPIO.output(a,1)
        GPIO.output(b,0)
        GPIO.output(c,1)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,0)
    elif(char=="6"):
        GPIO.output(a,1)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,0)
        GPIO.output(f,1)
    elif(char=="7"):
        GPIO.output(a,1)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,0)
        GPIO.output(f,0)
    elif(char=="8"):
        GPIO.output(a,1)
        GPIO.output(b,0)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,0)
    elif(char=="9"):
        GPIO.output(a,1)
        GPIO.output(b,1)
        GPIO.output(c,0)
        GPIO.output(d,1)
        GPIO.output(e,0)
        GPIO.output(f,1)
    else:
        GPIO.output(a,1)
        GPIO.output(b,1)
        GPIO.output(c,1)
        GPIO.output(d,1)
        GPIO.output(e,1)
        GPIO.output(f,1)

def brailleInput(a,b,c,d,e,f):
    time.sleep(0.5);
    if(GPIO.input(a)==GPIO.HIGH and GPIO.input(b)==GPIO.LOW and GPIO.input(c)==GPIO.LOW and GPIO.input(d)==GPIO.LOW and GPIO.input(e)==GPIO.LOW and GPIO.input(f)==GPIO.LOW):
        return "a"
    elif(GPIO.input(a)==GPIO.HIGH and GPIO.input(b)==GPIO.HIGH and GPIO.input(c)==GPIO.LOW and GPIO.input(d)==GPIO.LOW and GPIO.input(e)==GPIO.LOW and GPIO.input(f)==GPIO.LOW):      
        return "b"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "c"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "d"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "e"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "f"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "g"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "h"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "i"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "j"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "k"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "l"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "m"
    elif(GPIO.input(a) and  GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "n"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "o"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "p"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and  GPIO.input(e) and GPIO.input(f)):
        return "q"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "r"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "s"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and  GPIO.input(e) and  GPIO.input(f)):
        return "t"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "u"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and  GPIO.input(e) and GPIO.input(f)):
        return "v"
    elif(GPIO.input(a) and  GPIO.input(b) and  GPIO.input(c) and  GPIO.input(d) and GPIO.input(e) and  GPIO.input(f)):
        return "w"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f)):
        return "x"
    elif(GPIO.input(a) and  GPIO.input(b) and  GPIO.input(c) and  GPIO.input(d) and   GPIO.input(e) and  GPIO.input(f)):
        return "y"
    elif(GPIO.input(a) and GPIO.input(b) and   GPIO.input(c) and  GPIO.input(d) and   GPIO.input(e) and  GPIO.input(f)):
        return "z"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and   GPIO.input(d) and  GPIO.input(e) and   GPIO.input(f)):
        return "0"
    elif(GPIO.input(a) and  GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and   GPIO.input(e) and GPIO.input(f) ):
        return "1"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and GPIO.input(d) and GPIO.input(e) and GPIO.input(f) ):
        return "2"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and  GPIO.input(d) and  GPIO.input(e) and   GPIO.input(f) ):
        return "3"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and  GPIO.input(d) and  GPIO.input(e) and  GPIO.input(f) ):
        return "4"
    elif(GPIO.input(a) and GPIO.input(b) and  GPIO.input(c) and  GPIO.input(d) and  GPIO.input(e) and   GPIO.input(f)):
        return "5"
    elif(GPIO.input(a) and   GPIO.input(b) and GPIO.input(c) and    GPIO.input(d) and  GPIO.input(e) and  GPIO.input(f)):
        return "6"
    elif(GPIO.input(a) and  GPIO.input(b) and   GPIO.input(c) and  GPIO.input(d) and   GPIO.input(e) and   GPIO.input(f)):
        return "7"
    elif(GPIO.input(a) and  GPIO.input(b) and  GPIO.input(c) and  GPIO.input(d) and  GPIO.input(e) and  GPIO.input(f)):
        return "8"
    elif(GPIO.input(a) and GPIO.input(b) and GPIO.input(c) and  GPIO.input(d) and  GPIO.input(e) and  GPIO.input(f)):
        return "9"
    else:
        return None;