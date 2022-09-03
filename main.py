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
tracker = DiscordUtils.InviteTracker(client)
client.remove_command("help")

@client.event
async def on_ready():
 print(f"تم تشغيل بوت {client.user.name} بنجاح")
 await client.change_presence(activity=discord.Game(name="What"))

@client.event
async def on_message(m):
 if m.channel.id == 1004159791574294528:
   await m.content.delete()
  e=discord.Embed(title=f"إقتراح بواسطة {m.author.name}", description=f"**{m.content}**", color=discord.Color.random())
  e.set_thumbnail(url=m.author.avatar)
  await ctx.send(embed=e)

@client.command()
@commands.guild_only()
async def help(ctx):
    embed1 = discord.Embed(title="**1/5**", description=f"""**
{prefix}roll `نرد`
{prefix}simpcard `تعطي شخص بطاقة سيمب`
{prefix}love `نسبة الحب بين الطرفين`
{prefix}respect `تعطي شخص نقاط احترام`
**""", color=ctx.author.color)
    embed1.set_thumbnail(url=ctx.guild.icon)
    embed2 = discord.Embed(title="**2/5**", description=f"""**
{prefix}pixel `صورة الشخص لكن بكسل`
{prefix}trans `ترجمة الكلام`
{prefix}fact `معلومات عن كل شيء`
{prefix}wanted `تكون مطلوب`
**""", color=ctx.author.color)
    embed2.set_thumbnail(url=ctx.guild.icon)
    embed3 = discord.Embed(title="**3/5**", description=f"""**
{prefix}chad `نسبة التشاد عند الشخص`
{prefix}nazi `هل انت نازي او لا؟`
{prefix}soviet `هل انت سوفيتي او نازي؟`
{prefix}drip `بزنس مان`
**""", color=ctx.author.color)
    embed3.set_thumbnail(url=ctx.guild.icon)
    embed4 = discord.Embed(title="**4/5**", description=f"""**
{prefix}amoi `هل انت تدعم الحزب الأموي الأسلامي؟`
{prefix}pet `جعوص`
{prefix}gay `الوان مشكوكة على صورة الشخص`
{prefix}hgay `نسبة الشيء ذاك`
**""", color=ctx.author.color)
    embed4.set_thumbnail(url=ctx.guild.icon)
    embed5 = discord.Embed(title="**5/5**", description=f"""**
{prefix}isis `امر يفضح الدواعش`
{prefix}ussr `يحط لوقو السوفيت على صورة احد`
{prefix}shiite `نشوفك اذا شيعي`
{prefix}sunni `او ممكن تقول انك شيعي وتطلع سني`
**""", color=ctx.author.color)
    embed5.set_thumbnail(url=ctx.guild.icon)
    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
    paginator.add_reaction('⏮️', "first")
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('🔐', "lock")
    paginator.add_reaction('⏩', "next")
    paginator.add_reaction('⏭️', "last")
    embeds = [embed1, embed2, embed3, embed4, embed5]
    await paginator.run(embeds)

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
  avatar = member.avatar.replace(static_format="png")
  os.system(f"wget -O simpcard.png https://some-random-api.ml/canvas/simpcard/?avatar={ctx.message.attachments[0].url}")
  await ctx.reply(file=discord.File("simpcard.png"), mention_author=False)
  os.system("rm -rf simpcard.png")
  return
 avatar = member.avatar.replace(static_format="png")
 os.system(f"wget -O simpcard.png https://some-random-api.ml/canvas/simpcard/?avatar={avatar}")
 await ctx.reply(file=discord.File("simpcard.png"), mention_author=False)
 os.system("rm -rf simpcard.png")

@client.command()
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def say(ctx,*, arg=""):
 if ctx.message.attachments:
  os.system(f"wget -O image.png {ctx.message.attachments[0].url}")
  await ctx.reply(arg, file=discord.File("image.png"), mention_author=False)
  os.system("rm -rf image.png")
  return
 await ctx.message.delete()
 await ctx.send(f"**{arg}**")
 
@client.command()
@commands.guild_only()
async def love(ctx, name1, name2):
 love=discord.Embed(description=f"**نسبة الحب بين {name1} و {name2} هي {random.randint(-1, 100)}%**", color=ctx.author.color)
 love.set_thumbnail(url=ctx.guild.icon_url)
 await ctx.reply(embed=love, mention_author=False)

@client.command()
@commands.guild_only()
async def respect(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 if ctx.message.attachments:
  avatar = member.avatar.replace(static_format="png")
  os.system(f"wget -O respect.png https://some-random-api.ml/canvas/passed/?avatar={ctx.message.attachments[0].url}")
  await ctx.reply(file=discord.File("respect.png"), mention_author=False)
  os.system("rm -rf respect.png")
  return
 avatar = member.avatar.replace(static_format="png")
 os.system(f"wget -O respect.png https://some-random-api.ml/canvas/passed/?avatar={avatar}")
 await ctx.reply(file=discord.File("respect.png"), mention_author=False)
 os.system("rm -rf respect.png")

@client.command()
@commands.guild_only()
async def pixel(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 if ctx.message.attachments:
  avatar = member.avatar.replace(static_format="png")
  os.system(f"wget -O pixel.png https://some-random-api.ml/canvas/pixelate/?avatar={ctx.message.attachments[0].url}")
  await ctx.reply(file=discord.File(f"pixel.png"), mention_author=False)
  os.system("rm -rf pixel.png")
  return
 avatar = member.avatar.replace(static_format="png")
 os.system(f"wget -O user_pixel.png https://some-random-api.ml/canvas/pixelate/?avatar={avatar}")
 await ctx.reply(file=discord.File(f"user_pixel.png"), mention_author=False)
 os.system("rm -rf user_pixel.png")

@client.command()
@commands.guild_only()
async def fact(ctx):
 r=requests.get("https://api.popcat.xyz/fact")
 trans=requests.get(f"https://api.popcat.xyz/translate?to=ar&text={r.json()['fact']}")
 await ctx.send(f"```\nحقيقة\n{trans.json()['translated']}\n```")

@client.command()
@commands.guild_only()
async def wanted(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 if ctx.message.attachments:
  avatar = member.avatar.replace(static_format="png")
  os.system(f"wget -O wanted.png https://api.popcat.xyz/wanted?image={ctx.message.attachments[0].url}")
  await ctx.reply(file=discord.File("wanted.png"), mention_author=False)
  os.system("rm -rf wanted.png")
  return
 avatar = member.avatar.replace(static_format="png")
 os.system(f"wget -O wanted.png https://api.popcat.xyz/wanted?image={avatar}")
 await ctx.reply(file=discord.File("wanted.png"), mention_author=False)
 os.system("rm -rf wanted.png")

@client.command()
@commands.guild_only()
async def trans(ctx,*, txt):
 trans=requests.get(f"https://api.popcat.xyz/translate?to=ar&text={txt}").json()
 await ctx.send(f"**{trans['translated']}**")

@client.command()
@commands.guild_only()
async def gay(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 if ctx.message.attachments:
  avatar = member.avatar.replace(static_format="png")
  os.system(f"wget -O gay.png https://some-random-api.ml/canvas/gay/?avatar={ctx.message.attachments[0].url}")
  await ctx.reply(file=discord.File("gay.png"), mention_author=False)
  os.system("rm -rf gay.png")
  return
 avatar = member.avatar.replace(static_format="png")
 os.system(f"wget -O gay.png https://some-random-api.ml/canvas/gay/?avatar={avatar}")
 await ctx.reply(file=discord.File("gay.png"), mention_author=False)
 os.system("rm -rf gay.png")

@client.command()
@commands.guild_only()
async def pet(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 if ctx.message.attachments:
  avatar = member.avatar.replace(static_format="png")
  os.system(f"wget -O pet.gif https://api.popcat.xyz/pet?image={ctx.message.attachments[0].url}")
  await ctx.reply(file=discord.File("pet.gif"), mention_author=False)
  os.system("rm -rf pet.gif")
  return
 avatar = member.avatar.replace(static_format="png")
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
async def sunni(ctx,*, member=None):
 if member==None:
  member="انت"
 sunni=discord.Embed(title="**السنه**", description=f"**{member} سني بنسبة {random.randint(-1, 100)}%**", color=ctx.author.color)
 sunni.set_thumbnail(url="https://pbs.twimg.com/media/FLA8dhDXsAkK6FI?format=jpg&name=large")
 await ctx.reply(embed=sunni, mention_author=False)

@client.command()
@commands.guild_only()
async def shiite(ctx,*, member=None):
 if member==None:
  member="انت"
 shia=discord.Embed(title="**الشيعة**", description=f"**{member} شيعي بنسبة {random.randint(-1, 100)}%**", color=ctx.author.color)
 shia.set_thumbnail(url="https://c.tenor.com/dkxTibEsGZoAAAAS/%D9%84%D8%B7%D9%85-%D9%84%D8%B7%D9%85%D9%8A%D8%A9.gif")
 await ctx.reply(embed=shia, mention_author=False)

@client.command()
@commands.guild_only()
async def ussr(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 if ctx.message.attachments:
  avatar = member.avatar.replace(static_format="png")
  os.system(f"wget -O ussr.png https://api.popcat.xyz/communism?image={ctx.message.attachments[0].url}")
  await ctx.reply(file=discord.File("ussr.png"), mention_author=False)
  os.system("rm -rf ussr.png")
  return
 avatar = member.avatar.replace(static_format="png")
 os.system(f"wget -O ussr.png https://api.popcat.xyz/communism?image={avatar}")
 await ctx.reply(file=discord.File("ussr.png"), mention_author=False)
 os.system("rm -rf ussr.png")

@client.command()
@commands.guild_only()
async def بوت(ctx,*, txt):
 tr=requests.get(f"https://api.popcat.xyz/translate?to=en&text={txt}").json()
 r=requests.get(f"https://api.popcat.xyz/chatbot?msg={tr['translated']}&owner=سليم&botname=ترولر").json()
 trans=requests.get(f"https://api.popcat.xyz/translate?to=ar&text={r['response']}").json()
 await ctx.reply(f"**{trans['translated']}**", mention_author=False)

client.run("MTAwNjc0NTQ1Mzc4Nzg4NTYxOQ.GG6_rX.tj_jSCEAaIKYfKJGozfUVDmvSbP-EjR6pfsThM")
