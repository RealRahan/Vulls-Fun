import discord
from discord.ext import commands, tasks
import random
import asyncio
import os
import requests
import time

prefix="."
intents = discord.Intents().all()
client=commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
	print(f"تم تشغيل بوت {client.user.name} بنجاح")
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Vulls Channel"))
	azkar.start()

@tasks.loop(seconds = 900) # repeat after every 15 mins
async def azkar():
 r=requests.get("https://azkar-api.nawafhq.repl.co/zekr?e&m&t&pd&json").json()
 channel = client.get_channel(988834703299739688)
 a=discord.Embed(title=f"**{r['category']}**", description=f"**{r['content']}\n\n{r['description']}**")
 a.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZDS14K7-oXuLkcdwdi8F7khg4rOSEBMNo8w&usqp=CAU")
 a.set_footer(text=r["reference"])
 await channel.send(embed=a)

@client.command()
@commands.guild_only()
async def help(ctx):
 fun=discord.Embed(title=f"**الأوامر ({len(client.commands)})**", description=f"""**
{prefix}roll `نرد`
{prefix}simpcard `تعطي شخص بطاقة سيمب`
{prefix}love `نسبة الحب بين الطرفين`
{prefix}respect `تعطي شخص نقاط احترام`
{prefix}pixel `صورة الشخص لكن بكسل`
{prefix}trans `ترجمة الكلام`
{prefix}fact `معلومات عن كل شيء`
{prefix}wanted `تكون مطلوب`
{prefix}gun `تحط مسدس بصورتك`
{prefix}chad `نسبة التشاد عند الشخص`
{prefix}nazi `هل انت نازي او لا؟`
{prefix}soviet `هل انت سوفيتي او نازي؟`
{prefix}pet `جعوص`
{prefix}gay `الوان مشكوكة على صورة الشخص`
{prefix}hgay نسبة الشيء ذاك للشخص
**""", color=discord.Color.random())
 fun.set_thumbnail(url=ctx.author.avatar_url)
 msg=await ctx.send(embed=fun)
 while True:
  time.sleep(1)
  fun=discord.Embed(title=f"**الأوامر ({len(client.commands)})**", description=f"""**
{prefix}roll `نرد`
{prefix}simpcard `تعطي شخص بطاقة سيمب`
{prefix}love `نسبة الحب بين الطرفين`
{prefix}respect `تعطي شخص نقاط احترام`
{prefix}pixel `صورة الشخص لكن بكسل`
{prefix}trans `ترجمة الكلام`
{prefix}fact `معلومات عن كل شيء`
{prefix}wanted `تكون مطلوب`
{prefix}gun `تحط مسدس بصورتك`
{prefix}chad `نسبة التشاد عند الشخص`
{prefix}nazi `هل انت نازي او لا؟`
{prefix}soviet `هل انت سوفيتي او نازي؟`
{prefix}pet `جعوص`
{prefix}gay `الوان مشكوكة على صورة الشخص`
{prefix}hgay نسبة الشيء ذاك للشخص
**""", color=discord.Color.random())
 fun.set_thumbnail(url=ctx.author.avatar_url)
  await msg.edit(embed=fun)

@client.command()
@commands.guild_only()
async def ping(ctx):
  await ctx.send(f"**{round(client.latency * 1000)}ms**")

@client.command()
@commands.guild_only()
async def chad(ctx, member: discord.Member=None):
 if member==None:
  member=ctx.author
 chad=discord.Embed(title="**Chad Rate**", description=f"**{member.name} تشاد بنسبة {random.randint(0, 100)}%**", color=ctx.author.color)
 chad.set_thumbnail(url=member.avatar_url)
 await ctx.reply(embed=chad, mention_author=False)

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
  await ctx.send(f"**اكتب كلام\nمثال: {prefix}say أهلا جميعاً.**")
 await ctx.message.delete()
 await ctx.send(f"**{arg}**")
 
@client.command()
async def love(ctx, name1=None,*, name2=None):
 love=discord.Embed(description=f"**نسبة الحب بين {name1} و {name2} هي {random.randint(-1, 100)}%**", color=ctx.author.color)
 love.set_thumbnail(url=ctx.guild.icon_url)
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
@commands.guild_only()
async def wanted(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O wanted.png https://api.popcat.xyz/wanted?image={avatar}")
 await ctx.reply(file=discord.File("wanted.png"), mention_author=False)
 os.system("rm -rf wanted.png")

@client.command()
@commands.guild_only()
async def gun(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O gun.png https://api.popcat.xyz/gun?image={avatar}")
 await ctx.reply(file=discord.File("gun.png"), mention_author=False)
 os.system("rm -rf gun.png")

@client.command()
@commands.guild_only()
async def trans(ctx,*, txt):
 trans=requests.get(f"https://api.popcat.xyz/translate?to=ar&text={txt}")
 await ctx.send(f"**{trans.json()['translated']}**")

@client.command()
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def verify(ctx, user: discord.Member=None):
 if ctx.channel.id == 987012780102123540:
  if user == None:
   await ctx.send(f"**{prefix}verify @{ctx.author.name}**")
   return
  await user.add_roles(discord.utils.get(user.guild.roles, name="عبدو"))
  await user.remove_roles(discord.utils.get(user.guild.roles, name="Non-verified"))
  await ctx.send(f"**تم توثيق {user.name} ✅**")
 else:
  return

@client.command()
@commands.guild_only()
async def ques(ctx):
 if ctx.channel.id == 987012780102123540:
  await ctx.channel.trigger_typing()
  await ctx.send("""**
1-كم عمرك

2-من فين عرفت السيرفر

3-هل بتتحمل الترولز اللي هنا

4-بتكون عاقل وتلتزم بالقوانين

5-هل انت من داعمين الشواذ
**""")
 else:
  return

@client.command()
@commands.guild_only()
async def gay(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O gay.png https://some-random-api.ml/canvas/gay/?avatar={avatar}")
 await ctx.reply(file=discord.File("gay.png"), mention_author=False)
 os.system("rm -rf gay.png")

@client.command()
@commands.guild_only()
async def pet(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O pet.gif https://api.popcat.xyz/pet?image={avatar}")
 await ctx.reply(file=discord.File("pet.gif"), mention_author=False)
 os.system("rm -rf pet.gif")
 
@client.command()
@commands.guild_only()
async def nazi(ctx, member: discord.Member=None):
 if member==None:
  member=ctx.author
 nazi=discord.Embed(title="**Nazi Rate**", description=f"**{member.name} نازي بنسبة {random.randint(-10, 100)}%**", color=ctx.author.color)
 nazi.set_thumbnail(url="https://thumbs.gfycat.com/ThirstyMadeupIchthyostega-size_restricted.gif")
 await ctx.reply(embed=nazi, mention_author=False)

@client.command()
@commands.guild_only()
async def hgay(ctx, member: discord.Member=None):
 if member==None:
  member=ctx.author
 grate=discord.Embed(title="**grate**", description=f"**{member.name} :rainbow_flag: بنسبة {random.randint(-1, 100)}%**", color=ctx.author.color)
 grate.set_thumbnail(url="https://i.imgflip.com/6c3qh2.jpg")
 await ctx.reply(embed=grate, mention_author=False)

@client.command()
@commands.guild_only()
async def soviet(ctx, member: discord.Member=None):
 if member==None:
  member=ctx.author
 soviet=discord.Embed(title="**Soviet Union**", description=f"**{member.name} سوفيتي بنسبة {random.randint(-1, 100)}%**", color=ctx.author.color)
 soviet.set_thumbnail(url="https://i.imgflip.com/4y8rea.gif")
 await ctx.reply(embed=soviet, mention_author=False)

client.run("OTg5MDc1MTY1NjI5NTMwMTMz.GdNKA5.h570v2YUML9hcB19odruQDXOC8G6yYCWwef3tY")