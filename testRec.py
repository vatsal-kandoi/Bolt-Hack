import modules.detectSpeech as detectSpeech;
import modules.search as search;
import modules.detectOCR as OCR;
import wget

text = detectSpeech.detectText(enterPin);
text = text.lower();
print(text);
results = search.search(text);
wget.download(results[keyboardInput-1][0], 'response.pdf')
text2 = OCR.read("response.pdf");
print(text2);