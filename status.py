import discord
from discord.ext import commands
TOKEN = ''
bot = commands.Bot(command_prefix='+')
@bot.event
async def on_ready():
   await bot.change_presence(status=discord.Status.online, activity=discord.Game('BattleGrounds-(CharId:-5104046940)'))
   print('Bot is ready(status)')

bot.run(TOKEN)
