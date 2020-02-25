from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 

def read(path):
    output = '';
    if (path[-4:] == '.pdf'):
        pages = convert_from_path(path, 500) 
        for page in pages: 
            text = str(((pytesseract.image_to_string(page))));
            text = text.replace('-\n', '');
            output += output;
    else:
        text = str(((pytesseract.image_to_string(path))));
        text = text.replace('-\n', '');
        output += output;
    return output;
