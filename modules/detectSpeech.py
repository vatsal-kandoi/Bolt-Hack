import speech_recognition as sr;
import RPi.GPIO as gpio 
from recorder import Recorder 



class ButtonRecorder(object): 
    def __init__(self, filename, pin): 
        self.filename = filename
        gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_UP) 
        self.pin = pin;
        self.rec = Recorder(channels=2) 

    def start(self):
        gpio.add_event_detect(self.pin, gpio.FALLING, callback=self.falling, bouncetime=10) 

    def rising(self, channel): 
        gpio.remove_event_detect(self.pin) 
        gpio.add_event_detect(self.pin, gpio.FALLING, callback=self.falling, bouncetime=10) 
        self.recfile.stop_recording() 
        self.recfile.close()
        global stop;
        stop = True;

    def falling(self, channel): 
        gpio.remove_event_detect(self.pin) 
        gpio.add_event_detect(self.pin, gpio.RISING, callback=self.rising, bouncetime=10) 
        self.recfile = self.rec.open(self.filename, 'wb')    
        self.recfile.start_recording();

def detectText(pin):
    stop = False;
    rec = ButtonRecorder('nonblocking.wav');
    rec.start();
    while ( stop == False ):
        pass
    r = sr.Recognizer() 
    with sr.AudioFile('nonblocking.wav') as source: 
        audio = r.record(source)   
        try: 
            text = r.recognize_google(audio);
        except sr.UnknownValueError: 
            text = 'Cannot decipher. Try again';
        except sr.RequestError as e:
            text = 'Cannot decipher. Try again';
    return text;
