import discord
from discord.ext import commands
TOKEN = 'ODQ4NzkyNzMyMDIwMzc1NTky.YLRx1Q.KPPPD86FLfhedL2pCZsgOCgD-hw'
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
bot = commands.Bot(command_prefix = '+', intents = intents)
@bot.event
async def on_ready():
    print('Bot is ready')
@bot.event
async def on_member_join(member):
    print(f'{member}has joined the server')
@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('+hello'):
        await message.channel.send('Teri jrurt nhi thi be!')

bot.run(TOKEN)
