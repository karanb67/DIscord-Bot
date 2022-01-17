import discord
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
TOKEN = 'ODQ4NzkyNzMyMDIwMzc1NTky.YLRx1Q.KPPPD86FLfhedL2pCZsgOCgD-hw'
bot = commands.Bot(command_prefix='+')
status=cycle(['BattleGrounds-(CharId:-5104046940)','BattleGrounds'])
@bot.event
async def on_ready():
    change_status.start()
    print('Bot is ready This is bg task')
@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))
bot.run(TOKEN)
