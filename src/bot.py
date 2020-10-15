import discord
import os
from dotenv import load_dotenv

load_dotenv()

class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = DiscordClient()
client.run(os.environ['DISCORD_TOKEN'])
