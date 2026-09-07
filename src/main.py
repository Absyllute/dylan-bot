import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

load_dotenv()

CLANKER_TOKEN = getenv("BOT_TOKEN")
DEV_GUILD_ID  = getenv("DEV_GUILD")

DEV_GUILD = discord.Object(id=str(DEV_GUILD_ID))

custom_intents = discord.Intents.default()

class BotClient(commands.Bot):

    async def setup_hook(self) -> None:
        await self.load_extension("cogs.economy")

        self.tree.copy_global_to(guild=DEV_GUILD)
        synced_cmds = await self.tree.sync(guild=DEV_GUILD)

        print(f"Synced {len(synced_cmds)} slash commands")

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}")

client = BotClient(command_prefix="d.", intents=custom_intents)
client.run(str(CLANKER_TOKEN))