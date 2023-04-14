import json
info = '{"competitiveStats":{"awards":{"cards":0,"medals":0,"medalsBronze":0,"medalsSilver":0,"medalsGold":0},\
"games":{"played":244,"won":128},"season":null},"endorsement":2,\
"endorsementIcon":"https://static.playoverwatch.com/img/pages/career/icons/endorsement/2-8b9f0faa25.svg#icon",\
"gamesLost":645,"gamesPlayed":1360,"gamesWon":715,"icon":"https://d15f34w2p8l1cc.cloudfront.net/overwatch/17042e76e79bafa3d5fb93207ccf4799722d5ea93ec3588107ee2f8d598db4fe.png",\
"name":"ผมเบส","private":false,"quickPlayStats":{"awards":{"cards":340,"medals":0,"medalsBronze":0,"medalsSilver":0,"medalsGold":0},"games":{"played":1116,"won":587}},\
"rating":0,"ratingIcon":"","ratings":[{"group":"Diamond","tier":5,"role":"tank","roleIcon":"https://static.playoverwatch.com/img/pages/career/icons/role/tank-f64702b684.svg#icon",\
"rankIcon":"https://static.playoverwatch.com/img/pages/career/icons/rank/DiamondTier-5-cccbb1eb8c.png"},{"group":"Diamond","tier":4,"role":"offense","roleIcon":"https://static.playoverwatch.com/img/pages/career/icons/role/offense-ab1756f419.svg#icon","rankIcon":"https://static.playoverwatch.com/img/pages/career/icons/rank/DiamondTier-4-c11a83dff7.png"},{"group":"Diamond","tier":3,"role":"support","roleIcon":"https://static.playoverwatch.com/img/pages/career/icons/role/support-0258e13d85.svg#icon","rankIcon":"https://static.playoverwatch.com/img/pages/career/icons/rank/DiamondTier-3-5808b1a384.png"}]}'
forma = json.loads(info)
name = forma['name']
gameplayed = int(forma['competitiveStats']['games']['played'])
winrate = (forma['competitiveStats']['games']['won']/gameplayed) *100
winrate = f'{winrate:.2f}'
isprivate = forma['private']
endorsement = forma['endorsement']
tankrole = forma['ratings'][0]
dpsrole = forma['ratings'][1]
supportrole = forma['ratings'][2]
print(isprivate)
print(gameplayed)
print(winrate)
print("Endorsement Level:",endorsement)
print(tankrole['role'])
print(dpsrole['role'])
print(supportrole['role'])
print(name)