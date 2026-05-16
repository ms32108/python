import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
#the link downloads a json code in a .txt file
#run python itunes.py weezer(artist name)

response=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())


"""
if "print(response)" use it simply 
prints "Response [200]" that means  request sucessfull(404/500 means failed)
but to print the json text 

we use "print(response.json())"

Takes the raw response text and runs json.loads() under the hood.

Output is a usable Python dictionary containing the iTunes data.

"""