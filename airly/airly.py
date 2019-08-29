import requests
import json

parametry = {'apikey':'65eb5a888844453baf8314a8c209aae4','indextype':'AIRLY_CAQI','installationId':'810'}
zapytanie = requests.get("https://airapi.airly.eu/v2/measurements/installation",params=parametry)

json_data = json.loads(zapytanie.text)

timeStamp = json_data['current']['fromDateTime']
pm1= json_data['current']['values'][0]['value']
pm25= json_data['current']['values'][1]['value']
pm10= json_data['current']['values'][2]['value']
temp = json_data['current']['values'][5]['value']
humid = json_data['current']['values'][4]['value']
pres = json_data['current']['values'][3]['value']

print(timeStamp,pm1,pm25,pm10,temp,humid,pres, sep=",", end=';\n')