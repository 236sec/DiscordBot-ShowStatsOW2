import requests

platform = 'pc'
region = 'us'
player_name = 'ผมเบส#1466'
player_name = player_name.replace('#','-')
response = requests.get(f'https://ow-api.com/v1/stats/{platform}/{region}/{player_name}/profile')

print(response.status_code)  # prints the response status code (e.g. 200 for success)
print(response.text)  # prints the response body as text