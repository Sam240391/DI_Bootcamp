import requests
import json
from pprint import pprint

url = 'https://opentdb.com/api.php?amount=20&category=18'
response = requests.get(url)
print(response)
data = response.json()
pprint(data)

with open('trivia.json', 'w') as f:
    json.dump(response.json(), f, indent=4)
