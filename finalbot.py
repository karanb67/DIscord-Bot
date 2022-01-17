import discord
import os
import random
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
bot = commands.Bot(command_prefix = '+', intents = intents)
status=cycle(['BattleGrounds-(CharId:-5104046940)','BattleGrounds','ClashOfClans','JungleHeat'])
#change_status
@bot.event
async def on_ready():
    change_status.start()
    print('Bot is ready')
@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))
#kick
@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked\n Reason:{reason}')
    #ban
@bot.command()
async def ban(ctx, member:discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User {member.mention} has been banned\n Reason:{reason}')
#unban
@bot.command()
async def unban(ctx, *, member):
    banned_users= await ctx.guild.bans()
    member_name, member_discriminator= member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.name ,user.discriminator)==(member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned{user.mention}')
            return
#clear
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount)
    #clearerrorhandling
@clear.error
async def clear_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Specify The Amount Of Messages To Clear')
#me
@bot.command(aliases=['me','ME'])
async def Me(ctx):
    await ctx.send(f'Hi You are  {ctx.author}')
#ping
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong!!! {round(bot.latency * 1000)}ms')
#cf
@bot.command(aliases=['cf'])
async def coinflip(ctx):
    responses  = ['Heads','Tails']
    await ctx.send(f'{random.choice(responses)} ')
#hello
@bot.command(aliases=['hello'])
async def Hello(ctx):
    responses  = ['Hey Bruh!','Heya!','How you doin!','Sup? bro!','Or chikne ky haaal']
    await ctx.send(f'{random.choice(responses)} ')
#tempban

bot.run('TOKEN')
