import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Select, View
from config import EMBED_COLOR

class PremiumHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='help', description='Show the interactive premium help menu')
    async def help_command(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title='🤖 Premium Bot Help Menu',
            description='Select a **category** from the dropdown below to explore commands!',
            color=EMBED_COLOR
        )
        embed.set_footer(text=f'Requested by {interaction.user}', icon_url=interaction.user.display_avatar.url)
        select = Select(
            placeholder='📂 Choose a command category',
            options=[
                discord.SelectOption(label='🎵 Music', description='Play and manage songs', emoji='🎵'),
                discord.SelectOption(label='💰 Economy', description='Earn, spend, and manage coins', emoji='💰'),
                discord.SelectOption(label='⚡ Actions', description='Fun anime GIF interaction commands', emoji='⚡'),
                discord.SelectOption(label='🔨 Moderation', description='Kick, ban, and manage users', emoji='🔨'),
                discord.SelectOption(label='😂 Fun', description='Memes, jokes, and entertainment', emoji='😂'),
                discord.SelectOption(label='🛠 Utility', description='Info, ping, invite, etc.', emoji='🛠'),
                discord.SelectOption(label='🎮 Games', description='Play mini-games', emoji='🎮'),
            ]
        )

        async def callback(interaction2: discord.Interaction):
            sel = select.values[0]
            mapping = {
                '🎵 Music': '**🎵 Music Commands**\n`/play <url>` `/pause` `/resume` `/skip` `/stop` `/queue` `/nowplaying`',
                '💰 Economy': '**💰 Economy Commands**\n`/balance` `/daily` `/work` `/gamble` `/shop` `/buy`',
                '⚡ Actions': '**⚡ Action GIFs**\n`/hug` `/kiss` `/pat` `/slap` `/poke` `/cuddle` `/highfive` `/wave` `/punch` `/dance`',
                '🔨 Moderation': '**🔨 Moderation**\n`/kick` `/ban` `/unban` `/mute` `/clear`',
                '😂 Fun': '**😂 Fun**\n`/meme` `/joke` `/8ball` `/roll` `/quote`',
                '🛠 Utility': '**🛠 Utility**\n`/ping` `/info` `/invite` `/help`',
                '🎮 Games': '**🎮 Games**\n`/rps` `/tictactoe` `/guess`'
            }
            desc = mapping.get(sel, 'No commands')
            embed2 = discord.Embed(title=f'{sel} Commands', description=desc, color=EMBED_COLOR)
            await interaction2.response.edit_message(embed=embed2, view=None)

        select.callback = callback
        view = View()
        view.add_item(select)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=False)

async def setup(bot):
    await bot.add_cog(PremiumHelp(bot))
