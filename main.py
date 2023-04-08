import discord
import os
import json
from ow_api import get_stats
from textformatting import text_format

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
        output_message = text_format(respond)
        await message.channel.send(output_message)
        print("SEND SUCESS")
    else:
      print("Message :",content)
      # Define the output message
      output_message = "__**{Name}**__ :video_game:\n\nHere is some additional information:\n\n**Important information:** This text is highlighted in bold.\n\n**TANK**: This text is highlighted in red.\n\n:warning: Be careful when using this command!\n\n![Image description](https://static.playoverwatch.com/img/pages/career/icons/endorsement/2-8b9f0faa25.svg#icon)"
      output_message = text_format(content)

      # Send the message to the Discord channel
      await message.channel.send(output_message)


client.run(os.environ['TOKEN'])
