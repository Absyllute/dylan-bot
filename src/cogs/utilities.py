from discord.ext import commands
from discord import app_commands
import discord

class UtilitiesCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Test the bot. Replies with 'pong!'")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("🏓️ Pong! Bot online!")

async def setup(bot: commands.Bot):
    await bot.add_cog(UtilitiesCog(bot=bot))
