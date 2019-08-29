import json
import requests

response = requests.get('https://airapi.airly.eu/v2/measurements/point?indexType=AIRLY_CAQI&lat=50.014&lng=20.162&apikey=65eb5a888844453baf8314a8c209aae4')
json_data = json.loads(response.text)

print(json_data['current']['values'][1]['value'])