import discord
from discord.ext import commands, tasks
import random
import asyncio
import os
import requests
import time
import sys

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
    if message.type == discord.MessageType.premium_guild_subscription:
        bost = discord.Embed(description=f"**[{message.author.mention}] بوست جديد بواسطة**\nعدد البوستات الان: {message.guild.premium_subscription_count}\n > ** \💙[ {message.author} ]  شكرا على البوست \💙**",color=0xf47fff)
        bost.set_author(name='بوست جديد',icon_url='https://cdn.discordapp.com/attachments/866399886881980427/959803265485254666/booster.gif?size=4096')
        await channel.send(embed=bost)

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
{prefix}amoi `هل انت تدعم الحزب الأموي الأسلامي؟`
{prefix}pet `جعوص`
{prefix}gay `الوان مشكوكة على صورة الشخص`
{prefix}hgay `نسبة الشيء ذاك`
{prefix}drip `بزنس مان`
{prefix}isis `امر يفضح الدواعش`
{prefix}ussr `يحط لوقو السوفيت على صورة احد`
**""", color=discord.Color.random())
 fun.set_thumbnail(url=ctx.author.avatar_url)
 edit=await ctx.send(embed=fun)

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
 chad.set_thumbnail(url="https://c.tenor.com/epNMHGvRyHcAAAAd/gigachad-chad.gif")
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
 if ctx.message.attachments:
  avatar = member.avatar_url_as(static_format="png")
  os.system(f"wget -O simpcard.png https://some-random-api.ml/canvas/simpcard/?avatar={ctx.message.attachments[0].url}")
  await ctx.reply(file=discord.File("simpcard.png"), mention_author=False)
  os.system("rm -rf simpcard.png")
  return
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
  return
 await ctx.message.delete()
 await ctx.send(f"**{arg}**")
 
@client.command()
@commands.guild_only()
async def love(ctx, name1=None,*, name2=None):
 love=discord.Embed(description=f"**نسبة الحب بين {name1} و {name2} هي {random.randint(-1, 100)}%**", color=ctx.author.color)
 love.set_thumbnail(url=ctx.guild.icon_url)
 await ctx.send(embed=love)

@client.command()
@commands.guild_only()
async def respect(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 if ctx.message.attachments:
  avatar = member.avatar_url_as(static_format="png")
  os.system(f"wget -O respect.png https://some-random-api.ml/canvas/passed/?avatar={ctx.message.attachments[0].url}")
  await ctx.reply(file=discord.File("respect.png"), mention_author=False)
  os.system("rm -rf respect.png")
  return
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O respect.png https://some-random-api.ml/canvas/passed/?avatar={avatar}")
 await ctx.reply(file=discord.File("respect.png"), mention_author=False)
 os.system("rm -rf respect.png")

@client.command()
@commands.guild_only()
async def pixel(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 if ctx.message.attachments:
  avatar = member.avatar_url_as(static_format="png")
  os.system(f"wget -O pixel.png https://some-random-api.ml/canvas/pixelate/?avatar={ctx.message.attachments[0].url}")
  await ctx.reply(file=discord.File(f"pixel.png"), mention_author=False)
  os.system("rm -rf pixel.png")
  return
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O user_pixel.png https://some-random-api.ml/canvas/pixelate/?avatar={avatar}")
 await ctx.reply(file=discord.File(f"user_pixel.png"), mention_author=False)
 os.system("rm -rf user_pixel.png")

@client.command()
@commands.guild_only()
async def fact(ctx):
 r=requests.get("https://api.popcat.xyz/fact")
 trans=requests.get(f"https://api.popcat.xyz/translate?to=ar&text={r.json()['fact']}")
 fact=discord.Embed(title="**حقيقة**", description=f"**{trans.json()['translated']}**", color=discord.Color.random())
 fact.set_thumbnail(url=ctx.guild.icon_url)
 await ctx.send(embed=fact)

@client.command()
@commands.guild_only()
async def wanted(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 if ctx.message.attachments:
  avatar = member.avatar_url_as(static_format="png")
  os.system(f"wget -O wanted.png https://api.popcat.xyz/wanted?image={ctx.message.attachments[0].url}")
  await ctx.reply(file=discord.File("wanted.png"), mention_author=False)
  os.system("rm -rf wanted.png")
  return
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O wanted.png https://api.popcat.xyz/wanted?image={avatar}")
 await ctx.reply(file=discord.File("wanted.png"), mention_author=False)
 os.system("rm -rf wanted.png")

@client.command()
@commands.guild_only()
async def gun(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
  if ctx.message.attachments:
   avatar = member.avatar_url_as(static_format="png")
   os.system(f"wget -O gun.png https://api.popcat.xyz/gun?image={ctx.message.attachments[0].url}")
   await ctx.reply(file=discord.File("gun.png"), mention_author=False)
 return
 os.system("rm -rf gun.png")
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O gun.png https://api.popcat.xyz/gun?image={avatar}")
 await ctx.reply(file=discord.File("gun.png"), mention_author=False)
 os.system("rm -rf gun.png")

@client.command()
@commands.guild_only()
async def trans(ctx,*, txt):
 trans=requests.get(f"https://translate-api.tk/translate?text={txt}&lang=ar").json()
 await ctx.send(f"**{trans['translated']['text']}**")

@client.command()
@commands.guild_only()
async def gay(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 if ctx.message.attachments:
  avatar = member.avatar_url_as(static_format="png")
  os.system(f"wget -O gay.png https://some-random-api.ml/canvas/gay/?avatar={ctx.message.attachments[0].url}")
  await ctx.reply(file=discord.File("gay.png"), mention_author=False)
  os.system("rm -rf gay.png")
  return
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O gay.png https://some-random-api.ml/canvas/gay/?avatar={avatar}")
 await ctx.reply(file=discord.File("gay.png"), mention_author=False)
 os.system("rm -rf gay.png")

@client.command()
@commands.guild_only()
async def pet(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 if ctx.message.attachments:
  avatar = member.avatar_url_as(static_format="png")
  os.system(f"wget -O pet.gif https://api.popcat.xyz/pet?image={ctx.message.attachments[0].url}")
  await ctx.reply(file=discord.File("pet.gif"), mention_author=False)
  os.system("rm -rf pet.gif")
  return
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O pet.gif https://api.popcat.xyz/pet?image={avatar}")
 await ctx.reply(file=discord.File("pet.gif"), mention_author=False)
 os.system("rm -rf pet.gif")
 
@client.command()
@commands.guild_only()
async def nazi(ctx, member: discord.Member=None):
 if member==None:
  member=ctx.author
 nazi=discord.Embed(title="**Nazi Germany**", description=f"**{member.name} نازي بنسبة {random.randint(-10, 100)}%**", color=ctx.author.color)
 nazi.set_thumbnail(url="https://www.gifcen.com/wp-content/uploads/2021/04/hitler-gif-1.gif")
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
 soviet.set_thumbnail(url="https://c.tenor.com/WJ1VMm3FtBMAAAAC/stalin-joseph-stalin.gif")
 await ctx.reply(embed=soviet, mention_author=False)

def restart_bot(): 
  os.execv(sys.executable, ['python3'] + sys.argv)

@client.command()
@commands.has_permissions(manage_messages=True)
async def reboot(ctx):
  await ctx.send("**تمت إعادة التشغيل**")
  restart_bot()

@client.command()
@commands.guild_only()
async def amoi(ctx, member=None):
 if member==None:
  member="انت"
 a=discord.Embed(title="**الدَّوْلَةُ الأُمَوِيَّةُ**", description=f"**{member} أموي بنسبة {random.randint(-10, 100)}%**" , color=ctx.author.color)
 a.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/d/de/Mohammad_adil_rais-Caliph_Umar%27s_empire_at_its_peak_644.PNG")
 await ctx.reply(embed=a, mention_author=False)

@client.command()
@commands.guild_only()
async def drip(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O drip.png https://api.popcat.xyz/drip?image={avatar}")
 await ctx.reply(file=discord.File("drip.png"), mention_author=False)
 os.system("rm -rf drip.png")

#https://normal-api.tk/image-search?query={q}
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

@client.command()
@commands.guild_only()
async def isis(ctx,*, member=None):
 if member==None:
  member="انت"
 isis=discord.Embed(title="**ISIS**", description=f"**{member} داعشي بنسبة {random.randint(-10, 100)}%**", color=ctx.author.color)
 isis.set_thumbnail(url="https://i.kym-cdn.com/photos/images/original/001/078/451/3c9.gif")
 await ctx.reply(embed=isis, mention_author=False)

@client.command()
@commands.guild_only()
async def ussr(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 if ctx.message.attachments:
  avatar = member.avatar_url_as(static_format="png")
  os.system(f"wget -O ussr.png https://api.popcat.xyz/communism?image={ctx.message.attachments[0].url}")
  await ctx.reply(file=discord.File("ussr.png"), mention_author=False)
  os.system("rm -rf ussr.png")
  return
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O ussr.png https://api.popcat.xyz/communism?image={avatar}")
 await ctx.reply(file=discord.File("ussr.png"), mention_author=False)
 os.system("rm -rf ussr.png")

client.run("OTk4ODg4MDAwNDUwNzQwMjM0.GMDCnt.x1UtD0TgujMWL2e0n_tZ8kqjNFXsPbSpUWNWBE")