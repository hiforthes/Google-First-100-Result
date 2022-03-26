import requests
import json
params = {
  'api_key': 'YOUR valueserp.com API',
  'q': 'seo',
  'gl': 'us',
  'hl': 'en',
  'google_domain': 'google.com',
  'num': '100'
}
api_result = requests.get('https://api.valueserp.com/search', params)
x = 0
for y in api_result:
    x+=1
    results = json.dumps(api_result.json()['organic_results'][x]['title'])
    print(results)