while True: # Looping indefinitely
    text = detectSpeech.detectText();
    print(text);
    text = json.load(requests.get("https://api.duckduckgo.com/?q="+text[0]+"&format=json"))
    text = OCR.read('image.jpg');
    myobj = gTTS(text=text, lang='en', slow=False);
    myobj.save("response.wav");
    wave_obj = sa.WaveObject.from_wave_file("response.wav")
    play_obj = wave_obj.play()
