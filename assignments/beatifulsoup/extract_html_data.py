import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

html = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_753848.html").read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
sum = 0
for tag in tags:
    number = re.findall('[0-9]', str(tag))
    sum = sum + int(''.join(number))
print(sum)
