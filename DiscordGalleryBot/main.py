import discord
import os
import requests
from keep_alive import keep_alive
from discord import Webhook, RequestsWebhookAdapter

client = discord.Client()
r = requests.head(url="https://discord.com/api/v1")
try:
    print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
except:
    print("No rate limit")

##SECRET##
galleryId = os.environ['GALLERY_ID']
token = os.environ['TOKEN']
webhookURL = os.environ['WEBHOOK']

##URL WHITELISH##
URLs = ["https://www.youtube",
        "https://youtu.be", 
        "https://outplayed.tv"]

@client.event
async def on_ready():
  print('Bot logged in as {0.user}'.format(client))

##READ MESSAGES##
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.channel.id == galleryId:
    return

  if message.author.bot: return

  ##READ MESSAGES STRING##
  for url in URLs: 
    if url in message.content:
      await sendMessage(message.channel, message.author, message.content)

  ###READ ATTACHMENT###
  try:
    img = message.attachments[0].url
    await sendMessage(message.channel, message.author, img)
  except IndexError:
    pass

async def sendMessage(channelName, author, content):
  webhook = Webhook.from_url(webhookURL, adapter=RequestsWebhookAdapter())
  webhook.send('FROM: {}\n{}: \n{}'.format(channelName, author, content))

keep_alive()
client.run(token)