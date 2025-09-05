import discord
from discord.ext import commands
from discord import app_commands
import random

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='rps', description='Play rock paper scissors')
    async def rps(self, interaction: discord.Interaction, choice: str):
        opts = ['rock','paper','scissors']
        c = choice.lower()
        if c not in opts:
            await interaction.response.send_message('Choose rock/paper/scissors')
            return
        botc = random.choice(opts)
        if c==botc:
            res='Tie'
        elif (c=='rock' and botc=='scissors') or (c=='paper' and botc=='rock') or (c=='scissors' and botc=='paper'):
            res='You win'
        else:
            res='You lose'
        await interaction.response.send_message(f'You: {c} — Bot: {botc} — {res}')

    @app_commands.command(name='guess', description='Guess number 1-10')
    async def guess(self, interaction: discord.Interaction, number: int):
        secret = random.randint(1,10)
        if number==secret:
            await interaction.response.send_message('🎉 Correct!')
        else:
            await interaction.response.send_message(f'Wrong — I picked {secret}')

    @app_commands.command(name='tictactoe', description='Play tictactoe (placeholder)')
    async def ttt(self, interaction: discord.Interaction, opponent: discord.Member):
        await interaction.response.send_message(f'TicTacToe vs {opponent.display_name} (not implemented fully)')

async def setup(bot):
    await bot.add_cog(Games(bot))
