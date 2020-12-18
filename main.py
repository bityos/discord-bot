import discord
import os
from word import one,respe
import random

myToken = os.getenv('TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == f'{one[0]}':
            await message.channel.send('%s:  %s' %(self.user, random.choice(respe)))

    

myToken = os.getenv('TOKEN')
client = discord.Client()