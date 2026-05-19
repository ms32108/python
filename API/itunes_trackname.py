import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()


response=requests.get("https://itunes.apple.com/search?entity=song&limit=10&term="+sys.argv[1])
data=response.json()



for count,name in enumerate(data["results"],start=1):
    print(f"{count} .",name["trackName"])



"""
import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()


response=requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o=response.json()

for count,result in enumerate(o["results"],start=1):
    print(count , result["trackName"])
"""