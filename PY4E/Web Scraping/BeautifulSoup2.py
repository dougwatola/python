import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"


html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count_input = input("Enter Count:")
count = int(count_input)
#count = 4


p_input = input("Enter Position:")
position = int(p_input)
position = position - 1
#position = 2

print(f"Retrieving: {url}")

i = 0
#print(i)
#print(count)
while (i < count):
    #print("test")
    #tags = soup('a')
    #url = tags[position]
    #print(f"Retrieving: {url}")
    
    links = []

    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))
    
    
    url = links[position]
    print(f"Retrieving: {url}")
    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    i = i + 1