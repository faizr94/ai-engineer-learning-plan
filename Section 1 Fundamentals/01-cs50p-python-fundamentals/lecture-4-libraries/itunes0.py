"""
APIs - Application Programming Interface
JSON - Javascript Object Notation (commonly used as a language agnostic format for exchanging data between computers)
"""
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
    
# Making a HTTP request to the server    
response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1]
)


# Lets try to get the track name from the response results
# print(json.dumps(response.json(), indent=2))

o = response.json()

# Loop goes through each dictionary inside o["results"] which is a list of dictionaries
# result['trackName'] pulls the "trackName" value from the dictionary
for result in o["results"]:
    print(result['trackName'])


# This only works if the current limit is set to 1. Once the limit increases beyond, the print statement below would only return the first result
# hence we still need the loop
# print(o['results'][0]['trackName'])
