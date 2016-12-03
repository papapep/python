import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
#html = urllib.urlopen(url).read()
url = "http://python-data.dr-chuck.net/comments_339406.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
suma = 0
for tag in tags:
    suma = suma + int(tag.contents[0])

print suma


