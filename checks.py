import discord
from discord.ext import commands
TOKEN = ''
bot = commands.Bot(command_prefix='+')

@bot.event
async def on_ready():
    print("Bot is ready (Checks)")
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
@bot.command(aliases=['me','ME'])
async def Me(ctx):
    await ctx.send(f'Hi You are  {ctx.author}')
bot.run(TOKEN)
