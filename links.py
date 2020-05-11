from bs4 import BeautifulSoup
import re
import urllib.request
import requests

WEBPAGE = 'target website here, i.e. https://aaaaa.com/the/website/path'
DOMAIN = "target domain here, i.e. https://aaaaa.com/"

r = requests.get(WEBPAGE)
text = r.text

soup = BeautifulSoup(text, features="lxml")
for link in soup.findAll('a', attrs={'href': re.compile("\.pdf")}): # Add other extensions here
    link = link.get('href')
    if link.find("/") < 0: link = DOMAIN + link
    fname = link[link.rindex("/")+1:]
    print(f"saving {fname}...")
    try:
        urllib.request.urlretrieve(link, fname)
    except Exception as e:
        print(e)
