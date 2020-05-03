import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

link = input('Enter location: ')
xmlf = urllib.request.urlopen(link).read().decode()
print('Retrieving', link)
print('Retrieved', len(xmlf), 'characters')

data = ET.fromstring(xmlf)
tags = data.findall('comments/comment')

print('Count: ', len(tags))
print('Sum: ', sum([int(tag.find('count').text) for tag in tags])) 