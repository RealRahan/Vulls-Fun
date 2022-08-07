import discord
from discord.ext import commands, tasks
import random
import asyncio
import os
import requests
import time
import sys
import datetime

prefix="."
intents = discord.Intents().all()
client=commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
 print(f"تم تشغيل بوت {client.user.name} بنجاح")
 await client.change_presence(activity=discord.Game(name="إياس عم دريكس"))

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

@client.event
async def on_member_join(member):
 member.name = member.display_name
 channel = client.get_channel(995832723283390474)
 await channel.send(f"**دخل عضو جديد\nإسمه: {member.name}\nدخل السيرفر بتاريخ: <t:{int(ctx.member.joined_at.replace(tzinfo=datetime.timezone.utc).timestamp())}:R>\n و انشئ بتاريخ: <t:{int(ctx.member.created_at.replace(tzinfo=datetime.timezone.utc).timestamp())}:R>**")

client.run("MTAwMzUzMjE5NzQ1NTczMjc2Nw.GeYGxZ.oqX-CvEcALT9yin3x9bhAGIDvDA8f8xMQudQ54")