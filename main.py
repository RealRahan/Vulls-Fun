import discord
from discord.ext import commands, tasks
import random
import asyncio
import os
import requests
import time
import sys
import DiscordUtils

prefix="."
intents = discord.Intents().all()
client=commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
 print(f"تم تشغيل بوت {client.user.name} بنجاح")
 await client.change_presence(activity=discord.Game(name="إياس عم دريكس"))

@client.listen('on_message')
async def bost_stuf(message):
    channel = discord.utils.get(message.guild.channels, id=979008775207940147)
    footer=["https://c.tenor.com/lJFPnQNrMoEAAAAC/kfc-man.gif", "https://c.tenor.com/epNMHGvRyHcAAAAd/gigachad-chad.gif"]
    if message.type == discord.MessageType.premium_guild_subscription:
        bost = discord.Embed(description=f"**{message.author.mention} بوست جديد بواسطة الزنجي**\nعدد البوستات الان: {message.guild.premium_subscription_count}\n**<:creepyzenj:991237327227723806> [ {message.author.name} ]  شكرا على البوست <:creepyzenj:991237327227723806>**",color=0xf47fff)
        bost.set_author(name='بوست جديد',icon_url='https://cdn.discordapp.com/attachments/866399886881980427/959803265485254666/booster.gif?size=4096')
        bost.set_footer(text=message.guild.name, icon_url=random.choice(footer))
        await channel.send(embed=bost)


def restart_bot(): 
  os.execv(sys.executable, ['python3'] + sys.argv)

@client.command()
@commands.has_permissions(manage_messages=True)
async def reboot(ctx):
  await ctx.send("**تمت إعادة التشغيل**")
  restart_bot()

@client.command(aliases=["ver"])
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def verify(ctx, user: discord.Member=None):
 if ctx.channel.id == 995832723283390474:
  if user == None:
   await ctx.send(f"**{prefix}ver, verify @{ctx.author.name}**")
   return
  await user.add_roles(discord.utils.get(user.guild.roles, name="عبدو"))
  await user.remove_roles(discord.utils.get(user.guild.roles, name="Unverified"))
  await ctx.send(f"**تم توثيق {user.name} ✅**")
 else:
  return

@client.command(aliases=["unver"])
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def unverify(ctx, user: discord.Member=None,*, reason=None):
 if user == None:
   await ctx.send(f"**{prefix}unver, unverify @{ctx.author.name}**")
   return
 await user.add_roles(discord.utils.get(user.guild.roles, name="Unverified"))
 await user.remove_roles(discord.utils.get(user.guild.roles, name="عبدو"))
 await ctx.send(f"**تمت إزالة {user.name} من التوثيق ✅**")
 channel = client.get_channel(995832723283390474)
 await channel.send(f"**للاسف تمت إزالتك من التوثيق {user.mention} :x:**")
 if reason != None:
  await channel.send(f"**السبب: {reason}**")
  return

client.run("MTAwMzUzMjE5NzQ1NTczMjc2Nw.GeYGxZ.oqX-CvEcALT9yin3x9bhAGIDvDA8f8xMQudQ54")