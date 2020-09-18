import urllib.request, urllib.parse, urllib.error
import json

data = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_753851.json').read()
sum = 0

info = json.loads(data)
for item in info["comments"]:
    sum = sum + item["count"]
print(sum)
