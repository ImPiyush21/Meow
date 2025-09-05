import os, asyncio
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

async def load_cogs():
    for filename in sorted(os.listdir('./cogs')):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user} ({bot.user.id})')
    try:
        await bot.tree.sync()
        print('🌐 Slash commands synced.')
    except Exception as e:
        print('⚠️ Sync failed:', e)

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

if __name__ == '__main__':
    if not TOKEN:
        print('ERROR: DISCORD_TOKEN not set. Copy .env.example to .env and add your token.')
    else:
        asyncio.run(main())
