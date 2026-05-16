import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
#the link downloads a json code in a .txt file
#run python itunes.py weezer(artist name)

response=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())