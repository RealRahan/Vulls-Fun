import discord
from discord.ext import commands
import random
import asyncio
import os
import requests

prefix="."
intents = discord.Intents().all()
client=commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
	print(f"تم تشغيل بوت {client.user.name} بنجاح")
	activity = discord.Game(name=f"can you feel my heart")
	await client.change_presence(status=discord.Status.online, activity=activity)

@client.command()
async def help(ctx):
 fun=discord.Embed(title="الأوامر الخاصة بالبوت", description=f"""**
{prefix}roll `نرد`
{prefix}user `معلومات الشخص`
{prefix}simpcard `تعطي شخص بطاقة سيمب`
{prefix}love `نسبة الحب بين الطرفين`
{prefix}respect `تعطي شخص نقاط احترام`
{prefix}pixel `صورة الشخص لكن بكسل`
{prefix}fact `حقائق منوعة`
{prefix}img `تبحث على صور`
**""", color=ctx.author.color)
 fun.set_thumbnail(url=ctx.author.avatar_url)
 await ctx.send(embed=fun)

@client.command()
@commands.guild_only()
async def ping(ctx):
  await ctx.send(f"**{round(client.latency * 1000)}ms**")

@client.command()
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def user(ctx, user: discord.Member = None):
 if user == None:
 	user=ctx.author
 avatar = user.avatar_url_as(static_format="png")
 date = "%b %d %Y"
 roles = ' و '.join([r.mention for r in user.roles][1:])
 perms = '  /  '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
 user=discord.Embed(title=f"{user.name}", description=f"""**
الرقم التعريفي: {user.id}
انشئ بتاريخ: {user.created_at.strftime(date)}
دخل {ctx.guild.name} بتاريخ: {user.joined_at.strftime(date)}
الحالة: {user.status}
الرتب: {roles}
الصلاحيات:
{perms}
**""", color=user.color)
 user.set_thumbnail(url=avatar)
 user.set_footer(text=f"بطلب من: {ctx.author}")
 await ctx.send(embed=user)

@client.command()
@commands.guild_only()
async def roll(ctx):
  await ctx.send(f"**{random.randint(1,100)}**")

@client.command()
@commands.guild_only()
async def simpcard(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O simpcard.png https://some-random-api.ml/canvas/simpcard/?avatar={avatar}")
 await ctx.reply(file=discord.File("simpcard.png"), mention_author=False)
 os.system("rm -rf simpcard.png")

@client.command()
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def say(ctx,*, arg=None):
 if arg == None:
  await ctx.send("**اكتب نص.**")
 await ctx.message.delete()
 await ctx.send(arg)
 
@client.command()
async def love(ctx,name1=None,*, name2=None):
 if name1 == None:
  await ctx.send("**اسم الطرف الأول مطلوب**")
  return
 if name2 == None:
  await ctx.send("**اسم الطرف الثاني مطلوب**")
  return
 love=discord.Embed(description=f"**نسبة الحب بين {name1} و {name2} هي {random.randint(1, 100)}%**", color=ctx.author.color)
 love.set_thumbnail(url=ctx.author.avatar_url)
 await ctx.send(embed=love)

@client.command()
async def respect(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O respect.png https://some-random-api.ml/canvas/passed/?avatar={avatar}")
 await ctx.reply(f"ريسبكت {member.name}", file=discord.File("respect.png"), mention_author=False)
 os.system("rm -rf respect.png")

@client.command()
async def pixel(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O user_pixel.png https://some-random-api.ml/canvas/pixelate/?avatar={avatar}")
 await ctx.reply(file=discord.File(f"user_pixel.png"), mention_author=False)
 os.system("rm -rf user_pixel.png")

@client.command()
@commands.guild_only()
async def fact(ctx):
 r=requests.get("https://api.popcat.xyz/fact")
 trans=requests.get(f"https://api.popcat.xyz/translate?to=ar&text={r.json()['fact']}")
 await ctx.send(f"**{trans.json()['translated']}**")

@client.command()
async def img(ctx,*, search=None):
 if search == None:
  await ctx.send(f"**الاستخدام:\n{prefix}img trollface**")
  return
 r=requests.get(f"https://normal-api.tk/image-search?query={search}")
 if r.json()["status"] == 400:
  await ctx.send("**مالقيتها للأسف.**")
 image=discord.Embed(description=f"**{search}**", color=ctx.author.color)
 image.set_image(url=r.json()["image"])
 image.set_footer(text="محرك بحث جوجل ©2022", icon_url="https://freesvg.org/img/1534129544.png")
 await ctx.reply(embed=image, mention_author=False)

client.run("OTg3NDA4MTIzMDU4ODYwMDYz.GeOw-a.pYlrzLwMVph2qTe6_zWz63KkgRuy-udOleRCrA")
