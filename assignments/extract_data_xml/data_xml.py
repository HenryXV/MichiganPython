import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_753850.xml", context=ctx).read()

tree = ET.fromstring(html)
list = tree.findall('comments/comment')
total = 0
print('Total comments: ', len(list))

for item in list:
    count = item.find('count').text
    total = int(count) + total

print('Total sum:', total)
