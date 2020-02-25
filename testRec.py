import modules.detectSpeech as detectSpeech;
import modules.search as search;
import modules.detectOCR as OCR;
import wget

text = detectSpeech.detectText();
text = text.lower();
print(text);
#results = search.search(text);
#print(results);
wget.download("http://www.africau.edu/images/default/sample.pdf", 'response.pdf')
text2 = OCR.read("response.pdf");
print(text2);
