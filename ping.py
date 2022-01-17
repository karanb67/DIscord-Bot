import discord
import random
from discord.ext import commands
bot = commands.Bot(command_prefix='+')
@bot.event
async def on_ready():
    print('Bot is ready This is pong')
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong!!! {round(bot.latency * 1000)}ms')
@bot.command(aliases=['cf'])
async def coinflip(ctx):
    responses  = ['Heads','Tails']
    await ctx.send(f'{random.choice(responses)} ')
bot.run('ODQ4NzkyNzMyMDIwMzc1NTky.YLRx1Q.KPPPD86FLfhedL2pCZsgOCgD-hw')
