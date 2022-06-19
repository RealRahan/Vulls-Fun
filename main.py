import disnake
from disnake.ext import commands
import random
import asyncio
import os
import requests
import time

prefix="."
intents = disnake.Intents().all()
client=commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
	print(f"تم تشغيل بوت {client.user.name} بنجاح")
	activity = disnake.Game(name=f"The Nigga Bot")
	await client.change_presence(status=disnake.Status.idle, activity=activity)

@client.command()
@commands.guild_only()
async def help(ctx):
 fun=disnake.Embed(title=f"**الأوامر**", description=f"""**
{prefix}roll `نرد`
{prefix}simpcard `تعطي شخص بطاقة سيمب`
{prefix}love `نسبة الحب بين الطرفين`
{prefix}respect `تعطي شخص نقاط احترام`
{prefix}pixel `صورة الشخص لكن بكسل`
{prefix}fact `حقائق منوعة`
{prefix}wanted `تكون مطلوب`
{prefix}hack `تهكر حساب شخص`
**""", color=ctx.author.color)
 fun.set_thumbnail(url=ctx.author.avatar_url)
 await ctx.send(embed=fun)

@client.command()
@commands.guild_only()
async def ping(ctx):
  await ctx.send(f"**{round(client.latency * 1000)}ms**")

@client.command()
@commands.guild_only()
async def roll(ctx):
  await ctx.send(f"**{random.randint(1,100)}**")

@client.command()
@commands.guild_only()
async def simpcard(ctx, member: disnake.Member=None):
 if member == None:
  member=ctx.author
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O simpcard.png https://some-random-api.ml/canvas/simpcard/?avatar={avatar}")
 await ctx.reply(file=disnake.File("simpcard.png"), mention_author=False)
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
 love=disnake.Embed(description=f"**نسبة الحب بين {name1} و {name2} هي {random.randint(1, 100)}%**", color=ctx.author.color)
 love.set_thumbnail(url=ctx.author.avatar_url)
 await ctx.send(embed=love)

@client.command()
async def respect(ctx, member: disnake.Member=None):
 if member == None:
  member=ctx.author
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O respect.png https://some-random-api.ml/canvas/passed/?avatar={avatar}")
 await ctx.reply(f"ريسبكت {member.name}", file=disnake.File("respect.png"), mention_author=False)
 os.system("rm -rf respect.png")

@client.command()
async def pixel(ctx, member: disnake.Member=None):
 if member == None:
  member=ctx.author
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O user_pixel.png https://some-random-api.ml/canvas/pixelate/?avatar={avatar}")
 await ctx.reply(file=disnake.File(f"user_pixel.png"), mention_author=False)
 os.system("rm -rf user_pixel.png")

@client.command()
@commands.guild_only()
async def fact(ctx):
 r=requests.get("https://api.popcat.xyz/fact")
 trans=requests.get(f"https://api.popcat.xyz/translate?to=ar&text={r.json()['fact']}")
 await ctx.send(f"**{trans.json()['translated']}**")

@client.command()
@commands.guild_only()
async def hack(ctx, member: disnake.Member=None):
 if member == None:
  await ctx.send(f"**{prefix}hack @user")
  return
 elif member == client.user:
  await ctx.send("**ليش تبغا تهكرني <:SAD0:978820847689146389>**")
  return
 msg=await ctx.send("**جارِ بدأ عملية الأختراق**")
 await msg.edit("**10% التحقق إذا كان الحساب صالح للأختراق**")
 time.sleep(1)
 await msg.edit("**20% تم التحقق ، محاولة تسجيل الدخول**")
 time.sleep(1)
 await msg.edit("**30% تم العثور على الايميل الخاص بالحساب**")
 time.sleep(1)
 await msg.edit("**40% تم العثور على كلمة مرور الحساب**")
 time.sleep(1)
 await msg.edit("**55% جارِ تسجيل الدخول**")
 time.sleep(1)
 await msg.edit("**67% تم تسجيل الدخول**")
 time.sleep(1)
 await msg.edit("**78% جارِ البحث عن التوكن**")
 time.sleep(1)
 await msg.edit("**89% تم العثور على التوكن**")
 time.sleep(1)
 await msg.edit("**99% تسجيل خروج من الحساب**")
 time.sleep(1)
 await msg.edit("**100% تم جمع المعلومات**")
 r=requests.get(f"https://some-random-api.ml/bottoken/?id={member.id}")
 await msg.delete()
 await ctx.send(f"**{r.json['token']} هو التوكن الخاص بـ{member.name}")

@client.command()
@commands.guild_only()
async def wanted(ctx, member: disnake.Member=None):
 if member == None:
  member=ctx.author
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O wanted.png https://some-random-api.ml/canvas/wanted/?avatar={avatar}")
 await ctx.reply(file=disnake.File("wanted.png"), mention_author=False)
 os.system("rm -rf wanted.png")

client.run("OTg3NDA4MTIzMDU4ODYwMDYz.GUOh9u.weUhj9iMormmgasobubiNjyOaQUJxR50g2-JC4")