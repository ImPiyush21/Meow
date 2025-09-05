import discord
from discord.ext import commands
from discord import app_commands
from config import EMBED_COLOR, BOT_NAME
import os

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='ping', description='Check bot latency')
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Pong! {round(self.bot.latency*1000)}ms')

    @app_commands.command(name='info', description='Bot info')
    async def info(self, interaction: discord.Interaction):
        embed = discord.Embed(title=BOT_NAME, description='Premium Discord Bot', color=EMBED_COLOR)
        embed.add_field(name='Developer', value='Piyush')
        embed.add_field(name='Guilds', value=str(len(self.bot.guilds)))
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name='invite', description='Invite link')
    async def invite(self, interaction: discord.Interaction):
        app_id = os.getenv('APPLICATION_ID') or (self.bot.user.id if self.bot.user else '')
        url = f'https://discord.com/oauth2/authorize?client_id={app_id}&permissions=8&scope=bot%20applications.commands'
        await interaction.response.send_message(url)

async def setup(bot):
    await bot.add_cog(Utility(bot))
