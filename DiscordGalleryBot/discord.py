import discord
import setting
from discord import Webhook, RequestsWebhookAdapter

client = discord.Client()
r = requests.head(url="https://discord.com/api/v1")
try:
    print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
except:
    print("No rate limit")

@client.event
async def on_ready():
  print('Bot logged in as {0.user}'.format(client))

##READ MESSAGES##
@client.event
async def on_message(message):
  
  ##CHECK VALIDATION##
  if message.author == client.user:
    return

  if message.channel.id == setting.galleryId:
    return

  if not setting.isAllowBot:
    return

  for user in setting.blackListUsers:
    if user == message.author.memberId: #check again how to get member id
      return

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
  webhook = Webhook.from_url(setting.webhookURL, adapter=RequestsWebhookAdapter())
  webhook.send('FROM: {}\n{}: \n{}'.format(channelName, author, content))

client.run(setting.token)