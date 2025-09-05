import discord
from discord.ext import commands
from discord import app_commands
import json, os, random

DATA_FILE = 'data/economy.json'
os.makedirs('data', exist_ok=True)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({}, f)

def load():
    with open(DATA_FILE,'r') as f:
        return json.load(f)

def save(d):
    with open(DATA_FILE,'w') as f:
        json.dump(d,f,indent=2)

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.data = load()

    def ensure(self, uid):
        s = str(uid)
        if s not in self.data:
            self.data[s] = {'wallet':0,'inventory':[]}
        return self.data[s]

    @app_commands.command(name='balance', description='Check your balance')
    async def balance(self, interaction: discord.Interaction):
        user = self.ensure(interaction.user.id)
        await interaction.response.send_message(f"💰 You have **{user['wallet']}** coins")

    @app_commands.command(name='daily', description='Claim daily reward')
    async def daily(self, interaction: discord.Interaction):
        u = self.ensure(interaction.user.id)
        amt = random.randint(100,300)
        u['wallet'] += amt
        save(self.data)
        await interaction.response.send_message(f"🎁 You received {amt} coins")

    @app_commands.command(name='work', description='Work to earn coins')
    async def work(self, interaction: discord.Interaction):
        u = self.ensure(interaction.user.id)
        amt = random.randint(50,200)
        u['wallet'] += amt
        save(self.data)
        await interaction.response.send_message(f"💼 You earned {amt} coins")

    @app_commands.command(name='gamble', description='Gamble coins')
    async def gamble(self, interaction: discord.Interaction, amount: int):
        u = self.ensure(interaction.user.id)
        if amount <=0 or amount>u['wallet']:
            await interaction.response.send_message('Invalid amount')
            return
        win = random.choice([True,False])
        if win:
            u['wallet'] += amount
            res = f'You won {amount} coins!'
        else:
            u['wallet'] -= amount
            res = f'You lost {amount} coins.'
        save(self.data)
        await interaction.response.send_message(res)

    @app_commands.command(name='shop', description='View shop')
    async def shop(self, interaction: discord.Interaction):
        await interaction.response.send_message('Shop: VIP (500), ELITE (1000)')

    @app_commands.command(name='buy', description='Buy an item from shop')
    async def buy(self, interaction: discord.Interaction, item: str):
        items = {'vip':500,'elite':1000}
        i = item.lower()
        if i not in items:
            await interaction.response.send_message('Unknown item')
            return
        u = self.ensure(interaction.user.id)
        if u['wallet'] < items[i]:
            await interaction.response.send_message('Not enough coins')
            return
        u['wallet'] -= items[i]
        u['inventory'].append(i)
        save(self.data)
        await interaction.response.send_message(f'Purchased {i} for {items[i]} coins')

async def setup(bot):
    await bot.add_cog(Economy(bot))
