import discord
from discord.ext import commands
from discord import app_commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='meme', description='Get a random meme')
    async def meme(self, interaction: discord.Interaction):
        await interaction.response.send_message('https://i.imgflip.com/30b1gx.jpg')

    @app_commands.command(name='joke', description='Tell a joke')
    async def joke(self, interaction: discord.Interaction):
        jokes = ['Why did the chicken cross the road? To get to the other side!', 'I told my computer I needed a break, and it said No problem - it froze.']
        await interaction.response.send_message(random.choice(jokes))

    @app_commands.command(name='8ball', description='Ask the magic 8ball')
    async def eightball(self, interaction: discord.Interaction, question: str):
        answers = ['Yes','No','Maybe','Ask again later','Definitely']
        await interaction.response.send_message(random.choice(answers))

    @app_commands.command(name='roll', description='Roll a dice 1-100')
    async def roll(self, interaction: discord.Interaction):
        await interaction.response.send_message(str(random.randint(1,100)))

    @app_commands.command(name='quote', description='Motivational quote')
    async def quote(self, interaction: discord.Interaction):
        await interaction.response.send_message('Believe in yourself!')

async def setup(bot):
    await bot.add_cog(Fun(bot))
