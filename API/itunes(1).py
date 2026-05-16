import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()


response=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(response.json())

"""
print(response.json()) is not reable so we 
import json library to format the json file more redable

"""