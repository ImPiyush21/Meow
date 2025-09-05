import discord
from discord.ext import commands
from discord import app_commands
import aiohttp
from config import EMBED_COLOR

class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def fetch_gif(self, endpoint: str):
        url = f'https://api.waifu.pics/sfw/{endpoint}'
        try:
            async with aiohttp.ClientSession() as s:
                async with s.get(url, timeout=10) as r:
                    if r.status == 200:
                        data = await r.json()
                        return data.get('url')
        except Exception:
            return None

    @app_commands.command(name='hug', description='Hug someone')
    async def hug(self, interaction: discord.Interaction, member: discord.Member = None):
        await interaction.response.defer()
        gif = await self.fetch_gif('hug')
        if member:
            desc = f"**{interaction.user.mention} hugs {member.mention}!**"
        else:
            desc = f"**{interaction.user.mention} hugs!**"
        embed = discord.Embed(description=desc, color=EMBED_COLOR)
        if gif:
            embed.set_image(url=gif)
        await interaction.followup.send(embed=embed)

    @app_commands.command(name='kiss', description='Kiss someone')
    async def kiss(self, interaction: discord.Interaction, member: discord.Member = None):
        await interaction.response.defer()
        gif = await self.fetch_gif('kiss')
        if member:
            desc = f"**{interaction.user.mention} kisss {member.mention}!**"
        else:
            desc = f"**{interaction.user.mention} kisss!**"
        embed = discord.Embed(description=desc, color=EMBED_COLOR)
        if gif:
            embed.set_image(url=gif)
        await interaction.followup.send(embed=embed)

    @app_commands.command(name='pat', description='Pat someone')
    async def pat(self, interaction: discord.Interaction, member: discord.Member = None):
        await interaction.response.defer()
        gif = await self.fetch_gif('pat')
        if member:
            desc = f"**{interaction.user.mention} pats {member.mention}!**"
        else:
            desc = f"**{interaction.user.mention} pats!**"
        embed = discord.Embed(description=desc, color=EMBED_COLOR)
        if gif:
            embed.set_image(url=gif)
        await interaction.followup.send(embed=embed)

    @app_commands.command(name='slap', description='Slap someone')
    async def slap(self, interaction: discord.Interaction, member: discord.Member = None):
        await interaction.response.defer()
        gif = await self.fetch_gif('slap')
        if member:
            desc = f"**{interaction.user.mention} slaps {member.mention}!**"
        else:
            desc = f"**{interaction.user.mention} slaps!**"
        embed = discord.Embed(description=desc, color=EMBED_COLOR)
        if gif:
            embed.set_image(url=gif)
        await interaction.followup.send(embed=embed)

    @app_commands.command(name='poke', description='Poke someone')
    async def poke(self, interaction: discord.Interaction, member: discord.Member = None):
        await interaction.response.defer()
        gif = await self.fetch_gif('poke')
        if member:
            desc = f"**{interaction.user.mention} pokes {member.mention}!**"
        else:
            desc = f"**{interaction.user.mention} pokes!**"
        embed = discord.Embed(description=desc, color=EMBED_COLOR)
        if gif:
            embed.set_image(url=gif)
        await interaction.followup.send(embed=embed)

    @app_commands.command(name='wink', description='Wink someone')
    async def wink(self, interaction: discord.Interaction):
        await interaction.response.defer()
        gif = await self.fetch_gif('wink')
        desc = f"**{interaction.user.mention} winks!**"
        embed = discord.Embed(description=desc, color=EMBED_COLOR)
        if gif:
            embed.set_image(url=gif)
        await interaction.followup.send(embed=embed)

    @app_commands.command(name='dance', description='Dance someone')
    async def dance(self, interaction: discord.Interaction):
        await interaction.response.defer()
        gif = await self.fetch_gif('dance')
        desc = f"**{interaction.user.mention} dances!**"
        embed = discord.Embed(description=desc, color=EMBED_COLOR)
        if gif:
            embed.set_image(url=gif)
        await interaction.followup.send(embed=embed)

    @app_commands.command(name='cry', description='Cry someone')
    async def cry(self, interaction: discord.Interaction):
        await interaction.response.defer()
        gif = await self.fetch_gif('cry')
        desc = f"**{interaction.user.mention} crys!**"
        embed = discord.Embed(description=desc, color=EMBED_COLOR)
        if gif:
            embed.set_image(url=gif)
        await interaction.followup.send(embed=embed)

    @app_commands.command(name='kill', description='Kill someone')
    async def kill(self, interaction: discord.Interaction, member: discord.Member = None):
        await interaction.response.defer()
        gif = await self.fetch_gif('kill')
        if member:
            desc = f"**{interaction.user.mention} kills {member.mention}!**"
        else:
            desc = f"**{interaction.user.mention} kills!**"
        embed = discord.Embed(description=desc, color=EMBED_COLOR)
        if gif:
            embed.set_image(url=gif)
        await interaction.followup.send(embed=embed)

    @app_commands.command(name='bite', description='Bite someone')
    async def bite(self, interaction: discord.Interaction, member: discord.Member = None):
        await interaction.response.defer()
        gif = await self.fetch_gif('bite')
        if member:
            desc = f"**{interaction.user.mention} bites {member.mention}!**"
        else:
            desc = f"**{interaction.user.mention} bites!**"
        embed = discord.Embed(description=desc, color=EMBED_COLOR)
        if gif:
            embed.set_image(url=gif)
        await interaction.followup.send(embed=embed)

    @app_commands.command(name='smile', description='Smile someone')
    async def smile(self, interaction: discord.Interaction):
        await interaction.response.defer()
        gif = await self.fetch_gif('smile')
        desc = f"**{interaction.user.mention} smiles!**"
        embed = discord.Embed(description=desc, color=EMBED_COLOR)
        if gif:
            embed.set_image(url=gif)
        await interaction.followup.send(embed=embed)

    @app_commands.command(name='blush', description='Blush someone')
    async def blush(self, interaction: discord.Interaction):
        await interaction.response.defer()
        gif = await self.fetch_gif('blush')
        desc = f"**{interaction.user.mention} blushs!**"
        embed = discord.Embed(description=desc, color=EMBED_COLOR)
        if gif:
            embed.set_image(url=gif)
        await interaction.followup.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Actions(bot))
