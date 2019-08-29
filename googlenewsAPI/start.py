import json
import requests
from datetime import datetime

api_key = 'fb7684264ad441cdbb693efdfa5eb742'

parametry = {'apiKey':api_key,'country':'pl'}

odpowiedz = requests.get('https://newsapi.org/v2/top-headlines',params=parametry)

json_data=json.loads(odpowiedz.text)

for i in json_data['articles']:
    data = datetime.strptime(i['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
    print('{0:%d}/{0:%m} {0:%H}:{0:%M}'.format(data))
    print(i['title']+'\n')
    try:
        print(i['description']+'\n\n')
    except:
        print('---\n\n')