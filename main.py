import discord
import os

myToken = os.getenv('TOKEN')
client = discord.Client()

@client.event
async def on_ready():
  print(f'Nou konekte ak {client.user}')

@client.event
# msj = msg = message
async def on_message(msj):
  if msj.author == client.user:
    return
  
  if msj.content.startswith('$hello'):
    await  msj.channel.send('Byen vini!!!')


client.run(myToken)