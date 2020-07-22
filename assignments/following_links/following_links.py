import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

position = input('Enter position: ')
count = input('Enter count: ')
positioni = int(position)
counti = int(count)

html = urllib.request.urlopen("http://py4e-data.dr-chuck.net/known_by_Saffi.html", context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
links = list()
for tag in tags:
    links.append(tag.get('href', None))

print(links[positioni - 1])

while counti > 1:
    html_requested = urllib.request.urlopen(links[positioni - 1], context=ctx).read()
    soup_requested = BeautifulSoup(html_requested, 'html.parser')

    links.clear()

    tags = soup_requested('a')
    for tag in tags:
        links.append(tag.get('href', None))

    print(links[positioni - 1])

    counti = counti - 1
