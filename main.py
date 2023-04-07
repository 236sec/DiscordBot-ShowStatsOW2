import discord
import os
import json
from ow_api import get_stats

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return 0
    fetch_message = await message.channel.fetch_message(message.id)
    content = fetch_message.content
    if content.startswith('$ow'):
        await message.channel.send('Hello!')
        inputPlayername = content.split(' ')[1]
        respond = get_stats(player_name = inputPlayername,region='us',platform = 'pc')
        respond = json.loads(respond)
        print(type(respond))
        print(respond)
        #await message.channel.send(respond)
    else:
      print("Message :",content)

client.run(os.environ['TOKEN'])
