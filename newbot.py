import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='+')
@bot.event
async def on_ready():
    print('Bot is ready')
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong!!! {(bot.latency * 1000)}ms')
@bot.command(aliases=['8ball','eightball'])
async def _8ball(ctx, *,question):
    responses=['hey','hello','sdjhtfgiusd']
            await ctx.send(f'Ques:{question}\nAnswer:{random.choice(responses)}')
            
bot.run('')
