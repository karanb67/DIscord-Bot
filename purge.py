import discord
from discord.ext import commands
TOKEN = 'ODQ4NzkyNzMyMDIwMzc1NTky.YLRx1Q.KPPPD86FLfhedL2pCZsgOCgD-hw'
bot = commands.Bot(command_prefix='+')

@bot.event
async def on_ready():
    print("Bot is ready (Purge)")

@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

bot.run(TOKEN)
