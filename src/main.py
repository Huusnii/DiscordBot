import discord
import os
import requests
from keep_alive import keep_alive

client = discord.Client()
r = requests.head(url="https://discord.com/api/v1")
try:
    print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
except:
    print("No rate limit")

@client.event
async def on_ready():
  print('Bot logged in as {0.user}'.format(client))

##channel list##
gallery = 000000


##read messages##
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.channel.id == gallery:
    return

  if message.author.bot: return
  
  ##message contains##
  if "https://www.youtube" in message.content:
    channel = client.get_channel(gallery)
    await channel.send('{}: {}'.format(message.author, message.content))

  if "https://youtu.be" in message.content:
    channel = client.get_channel(gallery)
    await channel.send('{}: {}'.format(message.author, message.content))

  if "https://outplayed.tv" in message.content:
    channel = client.get_channel(gallery)
    await channel.send('{}: {}'.format(message.author, message.content))

  ###read attachment###
  try:
    print(message.attachments[0].url)
    img = message.attachments[0].url
    channel = client.get_channel(gallery)
    await channel.send('{}: {}'.format(message.author, img))
  except IndexError:
    pass

keep_alive()
client.run(os.environ['TOKEN'])