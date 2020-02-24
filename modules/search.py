import requests 
from bs4 import BeautifulSoup 
  
def search(content):
    URL = "https://google.com/search?channel=fs&q=" + "+".join(content.split(" "))+'+pdf';
    r = requests.get(URL); 
    soup = BeautifulSoup(r.content, 'html5lib') 
    links=[] 
    table = soup.findAll('div', attrs = {'class':'r'});
    for i in table:
        child = i.findAll("a", recursive=False);
        link = child["href"];
        details = child.findAll('h3', recursive=False);
        links.append([link, details]);
    return links;