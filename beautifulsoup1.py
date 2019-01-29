import urllib.request
from bs4 import BeautifulSoup

url = input("Enter a url: ")
with urllib.request.urlopen(url) as url:
    html=url.read()
    soup=BeautifulSoup(html,"html.parser")
    
    tags = soup('a')
    for tag in tags:
        print (tag.get('href', None))
