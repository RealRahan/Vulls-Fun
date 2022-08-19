import discord
from discord.ext import commands, tasks
import random
import asyncio
import os
import requests
import time
import sys
import datetime
import DiscordUtils
from seconds import Secs

prefix="."
intents = discord.Intents().all()
intents.members = True
client=commands.Bot(command_prefix=prefix, intents=intents)
tracker = DiscordUtils.InviteTracker(client)
client.remove_command("help")

@client.event
async def on_ready():
 print(f"تم تشغيل بوت {client.user.name} بنجاح")

def restart_bot(): 
  os.execv(sys.executable, ['python3'] + sys.argv)

@client.command()
@commands.has_permissions(manage_messages=True)
async def reboot(ctx):
  await ctx.send("**تمت إعادة التشغيل**")
  restart_bot()

@client.command()
async def ping(ctx):
    await ctx.reply(f"**{round(client.latency * 1000)}MS**")

@client.command(aliases=["ver"])
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def verify(ctx, user: discord.Member=None,*, r="مافي سبب"):
 if ctx.channel.id == 995832723283390474:
  if user == None:
   await ctx.send(f"**{prefix}ver, verify @{ctx.author.name}**")
   return
  await user.add_roles(discord.utils.get(user.guild.roles, name="عبدو"))
  await user.remove_roles(discord.utils.get(user.guild.roles, name="Unverified"))
  channel = client.get_channel(1007545972785676338)
  await channel.send("**توثيق ↓**")
  txt=f"**توثق من طرف: {ctx.author}\nسبب التوثيق: {r}**"
  embed=discord.Embed(title=f"**لوق {user}**", description=txt, color=discord.Color.random())
  embed.set_thumbnail(url=user.avatar)
  await channel.send(embed=embed)
  await ctx.send(f"**تم توثيق {user.name} ✅**")
 else:
  return

@client.command(aliases=["unver"])
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def unverify(ctx, user: discord.Member=None,*, reason="مافي سبب"):
 if user == None:
   await ctx.send(f"**{prefix}unver, unverify @{ctx.author.name}**")
   return
 await user.add_roles(discord.utils.get(user.guild.roles, name="Unverified"))
 await user.remove_roles(discord.utils.get(user.guild.roles, name="عبدو"))
 await ctx.message.add_reaction("✅")
 channel = client.get_channel(1007545972785676338)
 await channel.send("**إزالة التوثيق ↓**")
 txt=f"**انشال من طرف: {ctx.author}\nالسبب: {reason}**"
 embed=discord.Embed(title=f"**لوق {user}**", description=txt, color=discord.Color.random())
 embed.set_thumbnail(url=user.avatar)
 await channel.send(embed=embed)

@client.event
async def on_member_join(member):
 channel = client.get_channel(995832723283390474)
 inviter = await tracker.fetch_inviter(member)
 if inviter == None:
  await channel.send(f"**دخل عضو جديد\nإسمه: {member.name}\nانشئ قبل: <t:{int(member.created_at.replace(tzinfo=datetime.timezone.utc).timestamp())}:R>\nالإنفايتر: مستخدم رابط مخصص ل{member.guild.name}.\nإذا جاوب على الأسئلة تقدر توثقه بالأمر:**")
  await channel.send(f"**{prefix}verify {member.id}**")
  return
 else:
  await channel.send(f"**دخل عضو جديد\nإسمه: {member.name}\nانشئ قبل: <t:{int(member.created_at.replace(tzinfo=datetime.timezone.utc).timestamp())}:R>\nالإنفايتر: {inviter}\nإذا جاوب على الأسئلة تقدر توثقه بالأمر:**")
 await channel.send(f"**{prefix}verify {member.id}**")

@client.command()
async def timer(ctx, n=None,*, r=None):
 if n == None:
  await ctx.send(f"**الإستخدام:\n{prefix}timer 5m/5h/5mo/5y**")
 tosec=Secs(n)
 number=int(tosec)
 message = await ctx.send(f"**{number} متبقي**")
 while number != 0:
  number -= 1
  await message.edit(content=f"**{number} متبقي**")
  await asyncio.sleep(1)
 await message.edit(content=f"**إنتهى عداد ال{number} ثانيه!**")
 if r != None:
  await ctx.send(f"ملاحظتك: {r}")
 await ctx.send(ctx.author.mention)

client.run("MTAwMzUzMjE5NzQ1NTczMjc2Nw.GeYGxZ.oqX-CvEcALT9yin3x9bhAGIDvDA8f8xMQudQ54")
