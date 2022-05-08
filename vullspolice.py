import discord
from discord.ext import commands
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
import random
import asyncio
import os
import requests
import datetime

prefix="."
intents = discord.Intents().all()
client=commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
	print(f"تم تشغيل بوت {client.user.name} بنجاح")
	activity = discord.Game(name=f"يراقبك الساعة 3 ليل")
	await client.change_presence(status=discord.Status.idle, activity=activity)

@client.command()
async def help(ctx):
 fun=discord.Embed(title="الأوامر الخاصة بالبوت", description=f"""**
{prefix}roll `نرد`
{prefix}simpcard `تعطي شخص بطاقة سيمب`
{prefix}love `نسبة الحب بين الطرفين`
{prefix}simp `نسبة السيمب`
{prefix}respect `تعطي شخص نقاط احترام`
{prefix}pixel `صورة الشخص لكن بيكسل وكانك بلعبة`
**""", color=ctx.author.color)
 fun.set_thumbnail(url=ctx.author.avatar_url)
 await ctx.send(embed=fun)
#{prefix}ping `سرعة الرد`
#{prefix}user `معلومات الشخص`
#{prefix}say `تتكلم بالبوت`
#{prefix}ban `تحظر عضو من السيرفر`
#وبس ، استمتع

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
 perms = '\n'.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
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
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None,*, reason="لا يوجد سبب"):
 if member == None:
  nomention=discord.Embed(title="خطأ", description="**نسيت ذكر أو وضع معرف أو وضع اسم المستخدم في الحظر**", color=discord.Color.red())
  await ctx.send(embed=nomention)
 confirmation = BotConfirmation(ctx)
 await confirmation.confirm(f"**هل انت متأكد، ستقوم بحظر {member.name} من السيرفر.**")
 if confirmation.confirmed:
  await member.ban(reason=reason)
  await confirmation.update(f"**تم حظر {member} بنجاح من {ctx.guild.name}**", hide_author=True)
  await ctx.send(embed=ban)
  sendmsg=discord.Embed(title="حصلت على حظر", description=f"**حصلت على حظر من {ctx.guild.name} بواسطة {ctx.author.name} حسب السبب: {reason}\nاذا كان سوء تفاهم ف تحدث معة: {ctx.author}**")
  await member.send(embed=sendmsg)
 else:
  await confirmation.update("**تم الألغاء**", hide_author=True)
 
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
 await ctx.channel.purge(limit=1)
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
 await ctx.send(embed=love)

@client.command()
async def simp(ctx,*, member=None):
 if member == None:
  member=ctx.author.name
 love=discord.Embed(description=f"**{member} سيمب بنسبة {random.randint(1, 100)}%**", color=ctx.author.color)
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
 id=member.id
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O {id}_pixel.png https://some-random-api.ml/canvas/pixelate/?avatar={avatar}")
 await ctx.reply(file=discord.File(f"{member.id}_pixel.png"), mention_author=False)
 os.system("rm -rf {id}_pixel.png")

client.run("OTYyMzY0MzQ0MjE2MTk5MjI4.YlGdow.FailWE_MSK5JG3aSqgeFG2GPEOU")