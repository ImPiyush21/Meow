import discord
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='kick', description='Kick a member')
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = 'No reason'):
        await member.kick(reason=reason)
        await interaction.response.send_message(f'Kicked {member.display_name}')

    @app_commands.command(name='ban', description='Ban a member')
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = 'No reason'):
        await member.ban(reason=reason)
        await interaction.response.send_message(f'Banned {member.display_name}')

    @app_commands.command(name='clear', description='Purge messages')
    @app_commands.checks.has_permissions(manage_messages=True)
    async def clear(self, interaction: discord.Interaction, amount: int):
        deleted = await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f'Deleted {len(deleted)} messages', ephemeral=True)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
