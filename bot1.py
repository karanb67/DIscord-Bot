import discord
from discord.ext import commands
TOKEN = ''
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
bot = commands.Bot(command_prefix = '+', intents = intents)
@bot.event
async def on_ready():
    print('Bot1 is ready')
@bot.event
async def on_member_join(ctx, *, member):
    channel = member.server.get_channel("808296607493259295")
    fmt = 'Welcome to the {1.name} Discord server, {0.mention}'
    await ctx.send_message(channel, fmt.format(member, member.server))
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
