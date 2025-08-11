API_KEY = "rcXa7aiPh5Dyv2GvH1GxUg==o6KRWNL4YcGFyQLI"

import requests

city = 'Tashkent'
api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)