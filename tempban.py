import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='+')
@bot.event
async def on_ready():
    print('Bot is ready')

class DurationConverter(commands.Converter):
    async def convert(self, ctx, argument):
        amount = argument[:-1]
        unit=argument[-1]

        if amount.isdigit() and unit in['s','m']:
            return (int(amount),unit)
        raise commands.BadArgument(message)

bot.run('ODQ4NzkyNzMyMDIwMzc1NTky.YLRx1Q.KPPPD86FLfhedL2pCZsgOCgD-hw')
