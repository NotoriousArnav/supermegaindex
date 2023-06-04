"""
This is an Example Script to upload Mega.nz Links stored in a JSON file in this Stucture

```
[
  {
    "link": "https://mega.nz/file/7TRUCZCZ#ZPFmeFnccvR4ltf_2lwTdi8PqHIArRx_bkqRP9wwq4k",
    "title": "Wireshark For Professionals",
    "description": "Wireshark For Professionals"
  },
  ...
]
```

Uses:
- requests
To Handle HTTP requests
- time
For the sleep function to make sure, the server doesn't get overloaded
- json
For Parsing the JSON contents of the File
- pprint
To Print Data in a Readable way

"""

import requests, time, json, pprint, os

apiKey = os.getenv('smikey', input('Input your API key (if smikey is not set): '))
Base_URL = "https://arnv2004.pythonanywhere.com/api/records"

waitTime = 5

headers = {"Authorization": f"Token {apiKey}"}

with open(input("Enter Path to Mega Links JSON file: ")) as f:
    links = json.load(f)

for data in links:
    pprint.pprint(data)
    data = requests.post(Base_URL, json=data, headers=headers)
    print(data)

    #    for x in range(waitTime):
    #        print(f"Next Request in {waitTime-x}")
    #       time.sleep(1)
 
