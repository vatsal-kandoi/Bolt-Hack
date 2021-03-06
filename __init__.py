import modules.detectSpeech as detectSpeech;
import modules.search as search;
import requests;
import modules.buttons as button
import modules.detectOCR as OCR;
#from picamera import Picamera;
from PIL import Image
from gtts import gTTS 
import simpleaudio as sa
import wget
import re
import RPi.GPIO as GPIO
import serial
import json
import urllib
import time;
import pytesseract

GPIO.setmode(GPIO.BOARD)

'''
    2. Search for new
    3. In search for new, read out links to options available, and take input for which link to go to
    4. In existing files, read out avaiable and take input for which file to open
    5. Once file / article opened, read out text till cancel button pressed. 
    6. Output type to be determined by option, either speech or braille
    7. If braille, next letter if next pressed, prev if prev
    8. Option to take image instead of upload pdf (If time, optimum position)
    9. Learn Braille course
'''

keyboardInput = False; # Default is microphone
keyboardOutput = True; # Default if microphone

outputStream = '';
inputStream = '';
currentLetter = 0;
play = False;

searchStatus = 0;
options = [];

sessionMode = 0; 
'''
    Modes:
    0 : Main menu
    // Choosing settings
    1 : Input menu
    2 : Output menu
    3 : Reading out the pdf from output stream
    4 : Reading out loud

    5 : Search result output
    5 : Learning Mode
    6 : Searching
'''

# Defining GPIO Pins
a = 11


pausePin = 26;
playPin = 25;
enterPin = 24;
exitPin = 23;

def format(response):
    output = '';
    for i in range(len(response)):
        output += 'Link ' + i+1 + " ";
        output += "".join(response[i][1].split(" "));
    return output;

def download():
    wget.download(options[0][0], 'response.pdf')
    
if __name__=='__main__':
    # Set LED output high to signify switch on
    ser = serial.Serial('/dev/ttyACM0',9600)


    while True: # Looping indefinitel
        read = ser.readline().decode();
       	read = read[0:2];
        time.sleep(1);
        print(read);
        print(len(read));
        if(read == "au"):
            print("Detecting");
            text = detectSpeech.detectText();
            text = text.split(" ")[0];
            print(text);
            response = requests.get("https://api.duckduckgo.com/?q="+text+"&format=json")
            text = response.json()
            try:
                text = text["RelatedTopics"][0]["Text"]
            except:
                text = "Error"
            print(text);
            text = text.lower();
            #text = OCR.read('image.jpg');
            #myobj = gTTS(text=text, lang='en', slow=False);
            #myobj.save("response.wav");
            #wave_obj = sa.WaveObject.from_wave_file("response.wav")
            #play_obj = wave_obj.play()
            ser.write(str.encode(text));
            while(ser.readline().decode()[0:2] != 'ok'):
                pass;
            print("Entered");
        elif(read == 'ca'):
            #camera = PiCamera()
            #camera.start_preview()
            #time.sleep(5)
            #camera.capture('/home/pi/Desktop/image.jpg')
            #amera.stop_preview()
            text = pytesseract.image_to_string(Image.open('image.jpg'))
            print(text)
            ser.write(str.encode(text));
            while(ser.readline().decode()[0:2] != 'ok'):
                pass;
            print("Entered");
        else:
            pass;
       	# Check play pin press
        # inputChar = button.brailleInput(p,q,r,s,t,u);
        # if ( inputChar != None):
        #     inputStream += inputChar;
        #     print(inputStream) 

        # if (sessionMode == 3 and currentLetter != len(outputStream)-1):
        #     # button.brailleOutput(a,b,c,d,e,f,outputStream[currentLetter])
        #     ser.write(outputStream[currentLetter]);

        # if (playPin == 1):
        #     if (sessionMode == 0):
        #         sessionMode = 1;
        #     elif (sessionMode == 1):
        #         keyboardInput = True;
        #         sessionMode=0;
        #     elif (sessionMode == 2):
        #         keyboardOutput = True;
        #         sessionMode=0;
        #     elif (sessionMode == 3):
        #         currentLetter += 1;
        
        # if (pausePin == 1):
        #     if (sessionMode == 0):
        #         sessionMode = 2;
        #     elif (sessionMode == 1):
        #         keyboardInput = False;
        #         sessionMode=0;
        #     elif (sessionMode == 2):
        #         keyboardOutput = False;
        #         sessionMode=0;
        #     elif (sessionMode == 4 and play_obj != None):
        #         if (play_obj.is_playing()):
        #             play_obj.stop();

        # if (enterPin == 1):
        #     if (keyboardInput):
        #         if (searchStatus == 1):
        #             # Open and read pdf
        #             download();
        #             text = OCR.read('response.pdf');
        #             if (keyboardOutput):
        #                 outputStream = "".join(text.split(" "));
        #                 outputStream = re.sub('[\W]+','',outputStream);
        #                 outputStream = outputStream.lower();
        #                 sessionMode = 3;
        #             else:
        #                 myobj = gTTS(text=outputStream, lang='en', slow=False);
        #                 myobj.save("response.wav");
        #                 wave_obj = sa.WaveObject.from_wave_file("response.wav")
        #                 play_obj = wave_obj.play()
        #             searchStatus = 0;
        #         else:
        #             results = search.search(inputStream);
        #             outputStream = format(results);
        #             options = results;
        #             searchStatus = 1;
        #             if (keyboardOutput):
        #                 outputStream = "".join(text.split(" "));
        #                 outputStream = re.sub('[\W]+','',outputStream);
        #                 outputStream = outputStream.lower();
        #                 sessionMode = 3;
        #             else:
        #                 myobj = gTTS(text=outputStream, lang='en', slow=False);
        #                 myobj.save("response.wav");
        #                 wave_obj = sa.WaveObject.from_wave_file("response.wav")
        #                 play_obj = wave_obj.play()

        #     else:
        #         text = detectSpeech.detectText();
        #         text = text.lower();
        #         if (text == 'cannot decipher try again'):
        #             outputStream = text;
        #         elif (text == 'learn braille'):
        #             print("Learn braille");
        #         elif (searchStatus == 1):
        #             # Open and read pdf
        #             wget.download(options[text-1][0], 'response.pdf')
        #             text = OCR.read("response.pdf");
        #             outputStream = text;
        #             if (keyboardOutput):
        #                 outputStream = "".join(text.split(" "));
        #                 outputStream = re.sub('[\W]+','',outputStream);
        #                 outputStream = outputStream.lower();
        #                 sessionMode = 3;
        #             else:
        #                 myobj = gTTS(text=outputStream, lang='en', slow=False);
        #                 myobj.save("response.wav");
        #                 wave_obj = sa.WaveObject.from_wave_file("response.wav")
        #                 play_obj = wave_obj.play()
        #             searchStatus = 0;
        #         else:
        #             results = search.search(text);
        #             outputStream = format(results);
        #             options = results;
        #             searchStatus = 1;
        #         if (keyboardOutput):
        #             outputStream = "".join(text.split(" "));
        #             outputStream = re.sub('[\W]+','',outputStream);
        #             outputStream = outputStream.lower();
        #             sessionMode = 3;
        #         else:
        #             myobj = gTTS(text=outputStream, lang='en', slow=False);
        #             myobj.save("response.wav");
        #             wave_obj = sa.WaveObject.from_wave_file("response.wav")
        #             sessionMode = 4;
        #             play_obj = wave_obj.play();

        # if (exitPin == 1):
        #     sessionMode = 0;
        #     currentLetter = 0;
        #     inputStream = '';
        #     outputStream = '';
        #     if (play_obj != None):
        #         play_obj.stop();
