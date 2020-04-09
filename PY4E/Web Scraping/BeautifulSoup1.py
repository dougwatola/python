from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = "http://www.py4e.com/code3/urllink2.py"
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

comments = soup('span')

numbers = []
for comment in comments:
    number = int(comment.getText().split('\n')[0])
    numbers.append(number)
#print(numbers)
total = sum(numbers)
print(total)