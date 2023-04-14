import requests

def get_stats(player_name='',region='',platform=''):
  '''return the overwatch stats from https://ow-api.com parameter 
  player_name in format 'example-tag' , region example 'us' or     'eu' ,platform example pc'''
  response = requests.get(f'https://ow-api.com/v1/stats/{platform}/{region}/{player_name}/profile')
  if response.status_code == 200:
    print(response.text)
    return response.text


def main():
  platform = 'pc'
  region = 'us'
  player_name = 'ผมเบส#1466'
  player_name =  player_name.replace('#','-')
  get_stats(player_name,region,platform)

if __name__ == '__main__':
  main()