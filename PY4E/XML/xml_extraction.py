#Import relevant libraries
from urllib.request import urlopen
import urllib.request, urllib.parse, urllib.error
#import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Actual Data
#Prompt for URL for xml file and parse the XML

link = input('Enter - ')
url = urlopen(link)
#url = urlopen('http://py4e-data.dr-chuck.net/comments_42.xml')
xmldoc = parse(url)

print("Retrieving ", link)

#Determine the number of count entries in xml tree
counts = xmldoc.findall('.//count')
#counts = xml_tree.findall('./comments/comment/count')
print("Count: ",(len(counts)))

#This will be a runninng tally of numbers extracted from xml
count_list=[]


for item in xmldoc.iterfind('comments/comment'):
    count_number = int(item.findtext('count'))
    count_list.append(count_number)

print('Sum: ',(sum(count_list)))