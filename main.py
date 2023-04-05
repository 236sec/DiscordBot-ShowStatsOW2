import discord
import os

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)
TOKEN = os.environ['TOKEN']

@client.event
async def on_ready():
  print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
  print(message)
  if message.author == client.user:
      return

  if message.content.startswith('$ow'):
      channel = message.channel
      await channel.send('Im OW Stats Here')

client.run(TOKEN)
