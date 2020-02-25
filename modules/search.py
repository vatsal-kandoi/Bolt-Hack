import requests 
from bs4 import BeautifulSoup 
import googlesearch
def search(content):
    response = googlesearch.search(content+" pdf", stop=20)
    for result in response:
        print(result)
    return response;
