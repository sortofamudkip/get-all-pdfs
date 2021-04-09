from bs4 import BeautifulSoup
import re
import urllib.request
import requests
from sys import argv
import argparse
from urllib.parse import urlparse

parser = argparse.ArgumentParser(description='Downloads all PDFs from a website.')
parser.add_argument("url", help="A valid URL, e.g. https://aaaaa.com/the/website/path")
parser.add_argument("-f", "--force", action="store_true", help="Force download (without asking).")
args = parser.parse_args()

URL = args.url
url_object = urlparse(URL)
DOMAIN = f"//{url_object.netloc}"

try:
	r = requests.get(URL)
except requests.exceptions.ConnectionError as e:
	print("Could not connect to:", URL)
	print("Exception:")
	print(e)
	exit()

text = r.text


	

soup = BeautifulSoup(text, features="html.parser")
for link in soup.findAll('a', attrs={'href': re.compile("\.pdf")}): # Add other extensions here
    link = link.get('href')
    if link.find("/") < 0: link = DOMAIN + link
    fname = link[link.rindex("/")+1:]

    if not args.force:
    	ans = ""
    	while ans not in ["yes", "no"]:
    		ans = input(f"Download '{fname}'? ")
    	if ans == "no": continue
    try:
        urllib.request.urlretrieve(link, fname)
    except Exception as e:
        print(e)
