
#RUN--> python "itunes(1).py" ksi 


import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()


response=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

json_data = response.json()
clean_data=json.dumps(json_data,indent=2)

print(clean_data)





"""
print(response.json()) is not reable so we 
import json library to format the json file more redable

!!!!!"json.dumps(json txt , indent= size)"!!!

"""

"""
O/P-->

{
  "resultCount": 1,
  "results": [
    {
      "wrapperType": "track",
      "kind": "song",
      "artistId": 489704062,
      "collectionId": 1769091225,
      "trackId": 1769091226,
      "artistName": "KSI",
      "collectionName": "Thick Of It / Low", 
      "trackName": "Thick Of It (feat. Trippie Redd)", (we only need this track name here)
      "collectionCensoredName": "Thick Of It / Low",
      "trackCensoredName": "Thick Of It (feat. Trippie Redd)",
      "artistViewUrl": "https://music.apple.com/us/artist/ksi/489704062?uo=4",
      "collectionViewUrl": "https://music.apple.com/us/album/thick-of-it-feat-trippie-redd/1769091225?i=1769091226&uo=4",
      "trackViewUrl": "https://music.apple.com/us/album/thick-of-it-feat-trippie-redd/1769091225?i=1769091226&uo=4",
      "previewUrl": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/b7/ef/2b/b7ef2b15-5abc-781c-a41d-5e2e0643a8c1/mzaf_12851188655861085853.plus.aac.p.m4a",
      "artworkUrl30": "https://is1-ssl.mzstatic.com/image/thumb/Music211/v4/f1/b2/ef/f1b2ef27-7fc6-e325-3b0c-1458524febbb/5021732495983.jpg/30x30bb.jpg",
      "artworkUrl60": "https://is1-ssl.mzstatic.com/image/thumb/Music211/v4/f1/b2/ef/f1b2ef27-7fc6-e325-3b0c-1458524febbb/5021732495983.jpg/60x60bb.jpg",
      "artworkUrl100": "https://is1-ssl.mzstatic.com/image/thumb/Music211/v4/f1/b2/ef/f1b2ef27-7fc6-e325-3b0c-1458524febbb/5021732495983.jpg/100x100bb.jpg",
      "collectionPrice": 1.99,
      "trackPrice": 1.29,
      "releaseDate": "2024-08-31T12:00:00Z",
      "collectionExplicitness": "notExplicit",
      "trackExplicitness": "notExplicit",
      "discCount": 1,
      "discNumber": 1,
      "trackCount": 2,
      "trackNumber": 1,
      "trackTimeMillis": 160842,
      "country": "USA",
      "currency": "USD",
      "primaryGenreName": "Pop",
      "isStreamable": true
    }
  ]
}

"""