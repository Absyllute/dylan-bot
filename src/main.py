import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

load_dotenv()

CLANKER_TOKEN = getenv("BOT_TOKEN")

custom_intents = discord.Intents.default()

class BotClient(commands.Bot):
    async def on_ready(self):
        print(f"Logged in as {self.user}")

client = BotClient(command_prefix="d.", intents=custom_intents)
client.run(str(CLANKER_TOKEN))