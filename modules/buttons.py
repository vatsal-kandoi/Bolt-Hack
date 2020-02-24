import RPi.GPIO as GPIO        

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

def brailleInput(a,b,c,d,e,f)
    if(GPIO.input(a,0) and GPIO.input(b,1) and GPIO.input(c,1) and GPIO.input(d,1) and GPIO.input(e,1) and GPIO.input(f,1)):
        return "a"
    elif(GPIO.input(a,0) and GPIO.input(b,0) and GPIO.input(c,1) and GPIO.input(d,1) and GPIO.input(e,1) and GPIO.input(f,1)):      
        return "b"
    elif(GPIO.input(a,0) and GPIO.input(b,1) and GPIO.input(c,1) and GPIO.input(d,0) and GPIO.input(e,1) and GPIO.input(f,1)):
        return "c"
    elif(GPIO.input(a,0) and GPIO.input(b,1) and GPIO.input(c,1) and GPIO.input(d,0) and GPIO.input(e,0) and GPIO.input(f,1)):
        return "d"
    elif(GPIO.input(a,0) and GPIO.input(b,1) and GPIO.input(c,1) and GPIO.input(d,1) and GPIO.input(e,0) and GPIO.input(f,1)):
        return "e"
    elif(GPIO.input(a,0) and GPIO.input(b,0) and GPIO.input(c,1) and GPIO.input(d,0) and GPIO.input(e,1) and GPIO.input(f,1)):
        return "f"
    elif(GPIO.input(a,0) and GPIO.input(b,0) and GPIO.input(c,1) and GPIO.input(d,0) and GPIO.input(e,0) and GPIO.input(f,1)):
        return "g"
    elif(GPIO.input(a,0) and GPIO.input(b,0) and GPIO.input(c,1) and GPIO.input(d,1) and GPIO.input(e,0) and GPIO.input(f,1)):
        return "h"
    elif(GPIO.input(a,0) and GPIO.input(b,0) and GPIO.input(c,1) and GPIO.input(d,1) and GPIO.input(e,0) and GPIO.input(f,1)):
        return "i"
    elif(GPIO.input(a,1) and GPIO.input(b,0) and GPIO.input(c,1) and GPIO.input(d,0) and GPIO.input(e,0) and GPIO.input(f,1)):
        return "j"
    elif(GPIO.input(a,0) and GPIO.input(b,1) and GPIO.input(c,0) and GPIO.input(d,1) and GPIO.input(e,1) and GPIO.input(f,1)):
        return "k"
    elif(GPIO.input(a,0) and GPIO.input(b,0) and GPIO.input(c,0) and GPIO.input(d,1) and GPIO.input(e,1) and GPIO.input(f,1)):
        return "l"
    elif(GPIO.input(a,0) and GPIO.input(b,1) and GPIO.input(c,0) and GPIO.input(d,0) and GPIO.input(e,1) and GPIO.input(f,1)):
        return "m"
    elif(GPIO.input(a,0) and  GPIO.input(b,1) and GPIO.input(c,0) and GPIO.input(d,0) and GPIO.input(e,0) and GPIO.input(f,1)):
        return "n"
    elif(GPIO.input(a,0) and GPIO.input(b,1) and GPIO.input(c,0) and GPIO.input(d,1) and GPIO.input(e,0) and GPIO.input(f,1)):
        return "o"
    elif(GPIO.input(a,0) and GPIO.input(b,0) and GPIO.input(c,0) and GPIO.input(d,0) and GPIO.input(e,1) and GPIO.input(f,1)):
        return "p"
    elif(GPIO.input(a,0) and GPIO.input(b,0) and GPIO.input(c,0) and GPIO.input(d,0) and  GPIO.input(e,0) and GPIO.input(f,1)):
        return "q"
    elif(GPIO.input(a,0) and GPIO.input(b,0) and GPIO.input(c,0) and GPIO.input(d,1) and GPIO.input(e,0) and GPIO.input(f,1)):
        return "r"
    elif(GPIO.input(a,1) and GPIO.input(b,0) and GPIO.input(c,0) and GPIO.input(d,0) and GPIO.input(e,1) and GPIO.input(f,1)):
        return "s"
    elif(GPIO.input(a,1) and GPIO.input(b,0) and GPIO.input(c,0) and GPIO.input(d,0) and  GPIO.input(e,0) and  GPIO.input(f,1)):
        return "t"
    elif(GPIO.input(a,0) and GPIO.input(b,1) and GPIO.input(c,0) and GPIO.input(d,1) and GPIO.input(e,1) and GPIO.input(f,0)):
        return "u"
    elif(GPIO.input(a,0) and GPIO.input(b,0) and GPIO.input(c,0) and GPIO.input(d,1) and  GPIO.input(e,1) and GPIO.input(f,0)):
        return "v"
    elif(GPIO.input(a,1) and  GPIO.input(b,0) and  GPIO.input(c,1) and  GPIO.input(d,0) and GPIO.input(e,0) and  GPIO.input(f,0)):
        return "w"
    elif(GPIO.input(a,0) and GPIO.input(b,1) and GPIO.input(c,0) and GPIO.input(d,0) and GPIO.input(e,1) and GPIO.input(f,0)):
        return "x"
    elif(GPIO.input(a,0) and  GPIO.input(b,1) and  GPIO.input(c,0) and  GPIO.input(d,0) and   GPIO.input(e,0) and  GPIO.input(f,0)):
        return "y"
    elif(GPIO.input(a,0) and GPIO.input(b,1) and   GPIO.input(c,0) and  GPIO.input(d,1) and   GPIO.input(e,0) and  GPIO.input(f,0)):
        return "z"
    elif(GPIO.input(a,1) and GPIO.input(b,1) and GPIO.input(c,0) and   GPIO.input(d,1) and  GPIO.input(e,0) and   GPIO.input(f,0)):
        return "0"
    elif(GPIO.input(a,1) and  GPIO.input(b,0) and GPIO.input(c,1) and GPIO.input(d,1) and   GPIO.input(e,1) and GPIO.input(f,1) ):
        return "1"
    elif(GPIO.input(a,1) and GPIO.input(b,0) and GPIO.input(c,0) and GPIO.input(d,1) and GPIO.input(e,1) and GPIO.input(f,1) ):
        return "2"
    elif(GPIO.input(a,1) and GPIO.input(b,0) and GPIO.input(c,1) and  GPIO.input(d,1) and  GPIO.input(e,0) and   GPIO.input(f,1) ):
        return "3"
    elif(GPIO.input(a,1) and GPIO.input(b,0) and GPIO.input(c,1) and  GPIO.input(d,1) and  GPIO.input(e,0) and  GPIO.input(f,0) ):
        return "4"
    elif(GPIO.input(a,1) and GPIO.input(b,0) and  GPIO.input(c,1) and  GPIO.input(d,1) and  GPIO.input(e,1) and   GPIO.input(f,0)):
        return "5"
    elif(GPIO.input(a,1) and   GPIO.input(b,0) and GPIO.input(c,0) and    GPIO.input(d,1) and  GPIO.input(e,0) and  GPIO.input(f,1)):
        return "6"
    elif(GPIO.input(a,1) and  GPIO.input(b,0) and   GPIO.input(c,0) and  GPIO.input(d,1) and   GPIO.input(e,0) and   GPIO.input(f,0)):
        return "7"
    elif(GPIO.input(a,1) and  GPIO.input(b,0) and  GPIO.input(c,0) and  GPIO.input(d,1) and  GPIO.input(e,1) and  GPIO.input(f,0)):
        return "8"
    elif(GPIO.input(a,1) and GPIO.input(b,1) and GPIO.input(c,0) and  GPIO.input(d,1) and  GPIO.input(e,0) and  GPIO.input(f,1)):
        return "9"
    else:
        return None;