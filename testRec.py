import modules.detectSpeech as detectSpeech;

text = detectSpeech.detectText(enterPin);
text = text.lower();
print(text);