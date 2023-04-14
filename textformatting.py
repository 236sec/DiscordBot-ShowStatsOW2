def endorsementNumToText(endorsementNum):
  if endorsementNum == 0:
    return 'zero'
  elif endorsementNum == 1:
    return 'one'
  elif endorsementNum == 2:
    return 'two'
  elif endorsementNum == 3:
    return 'three'


def text_format(api_respond):
  '''api_respond must be json type'''
  name = api_respond['name']
  if api_respond['private'] :
    return f"__**{name}**__ :video_game:\n:lock: **This Account Is Private**"
  elif not(api_respond['private']):
    endorsementNum = api_respond['endorsement']
    endorsementText = endorsementNumToText(endorsementNum)
    gameplayed = int(api_respond['competitiveStats']['games']['played'])
    winrate = (api_respond['competitiveStats']['games']['won']/gameplayed) *100
    winrate = f'{winrate:.2f}'
    return f"__**{name}**__ :video_game:\n\nEndorsement Level : :{endorsementText}:\n\nGAMEPLAYED:**{gameplayed}**  WINRATE:**{winrate}**\n\n**Warning:** This text is highlighted in red.\n\n:warning: Be careful when using this command!\n"


def test():
  api_re = {'name':'ผมเบส','private':False,'endorsement':2}
  print(text_format(api_re))
