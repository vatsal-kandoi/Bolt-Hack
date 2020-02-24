import speech_recognition as sr;
import RPi.GPIO as gpio 
import pyaudio
import wave
import sys

def detectText(pin):
    CHUNK = 512
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 2
    WAVE_OUTPUT_FILENAME = "output.wav"

    if sys.platform == 'darwin':
        CHANNELS = 1

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    r = sr.Recognizer() 
    with sr.AudioFile('output.wav') as source: 
        audio = r.record(source)   
        try: 
            text = r.recognize_google(audio);
        except sr.UnknownValueError: 
            text = 'Cannot decipher. Try again';
        except sr.RequestError as e:
            text = 'Cannot decipher. Try again';
    return text;
