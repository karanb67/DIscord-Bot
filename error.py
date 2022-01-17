import discord
from discord.ext import commands
TOKEN = 'ODQ4NzkyNzMyMDIwMzc1NTky.YLRx1Q.KPPPD86FLfhedL2pCZsgOCgD-hw'
bot = commands.Bot(command_prefix='+')

@bot.event
async def on_ready():
    print("Bot is ready (Error )")
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invaild Command')
@bot.command()
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount)
@clear.error
async def clear_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Specify The Amount Of Messages To Clear')
bot.run(TOKEN)
