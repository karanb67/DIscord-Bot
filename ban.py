import discord
from discord.ext import commands
TOKEN = 'ODQ4NzkyNzMyMDIwMzc1NTky.YLRx1Q.KPPPD86FLfhedL2pCZsgOCgD-hw'
bot = commands.Bot(command_prefix='+')
@bot.event
async def on_ready():
    print('Bot is ready This is Ban')
@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked\n Reason:{reason}')
@bot.command()
async def ban(ctx, member:discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User {member.mention} has been banned\n Reason:{reason}')
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

bot.run(TOKEN)
