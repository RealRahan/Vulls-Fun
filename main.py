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
	activity = discord.Game(name=f"فولز > ميمر")
	await client.change_presence(status=discord.Status.idle, activity=activity)

@client.command()
async def help(ctx):
 await ctx.reply("<a:loading:964951108353159249>", delete_after=3, mention_author=False)
 await asyncio.sleep(3)
 embeds = [
 discord.Embed(title="الأوامر العامة", description=f"""**
{prefix}help `هذي القائمة`
{prefix}ping `سرعة الرد`
{prefix}user `معلومات الشخص`
{prefix}say `تتكلم بالبوت`
**"""),
 discord.Embed(title=f"الأوامر الأشرافية", description=f"""**
{prefix}ban `تبند عضو (والله لو تجربة على نفسك الله يرحمك)`
قريبا اوامر زيادة.
**"""),
 discord.Embed(title="الأوامر الممتعة", description=f"""**
{prefix}meme `غني عن التعريف`
{prefix}roll `نرد`
{prefix}simpcard `تعطي شخص بطاقة سيمب`
{prefix}jail `تسجن شخص`
**""")
]
 paginator = BotEmbedPaginator(ctx, embeds)
 await paginator.run()

@client.command()
@commands.guild_only()
async def ping(ctx):
  await ctx.send(f"**{round(client.latency * 1000)}ms**")

@client.command()
@commands.guild_only()
async def user(ctx, user: discord.Member = None):
 if user == None:
 	user=ctx.author
 avatar = user.avatar_url_as(static_format="png")
 date = "%b %d %Y"
 roles = ' و '.join([r.mention for r in user.roles][1:])
 msg=await ctx.send("**اخذ الرقم التعريفي | <a:loading:964951108353159249>**")
 await asyncio.sleep(0.30)
 await msg.edit(content="**اخذ تاريخ الانشاء | <a:loading:964951108353159249>**")
 await asyncio.sleep(0.30)
 await msg.edit(content="**اخذ تاريخ الدخول | <a:loading:964951108353159249>**")
 await asyncio.sleep(0.30)
 await msg.edit(content="**اخذ معلومات الحالة | <a:loading:964951108353159249>**")
 await asyncio.sleep(0.30)
 await msg.edit(content="**اخذ معلومات الرتب | <a:loading:964951108353159249>**")
 await msg.delete()
 user=discord.Embed(title=f"{user.name}", description=f"""**
الرقم التعريفي: {user.id}
انشئ بتاريخ: {user.created_at.strftime(date)}
دخل {ctx.guild.name} بتاريخ: {user.joined_at.strftime(date)}
الحالة: {user.status}
الرتب: {roles}
**""", color=user.color)
 user.set_thumbnail(url=avatar)
 user.set_footer(text=f"بطلب من: {ctx.author} | {prefix}perms لرؤية صلاحيات المستخدم")
 await ctx.send(embed=user)

@client.command()
@commands.guild_only()
async def perms(ctx, user: discord.Member=None):
  if user == None:
  	user=ctx.author
  perms = '\n'.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
  perm=discord.Embed(description=f"**{perms}**")
  await ctx.send(embed=perm)

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
async def count(ctx, t:int):
    message=await ctx.send(f"**{t}**")
    while t > 0:
        t -=1
        await message.edit(content=f"**{t}**")
        await asyncio.sleep(1)
    await message.edit(content=f"**انتهى بواسطة {ctx.author.name}**")
    mention=await ctx.send(ctx.author.mention)
    await mention.delete()

@client.command()
@commands.guild_only()
async def meme(ctx):
 r=requests.get("https://meme-api.herokuapp.com/gimme/armeme")
 os.system(f"wget -O meme.png {r.json()['url']}")
 await ctx.send(f"{r.json()['title']}\nUps: ({r.json()['ups']})", file=discord.File("meme.png"))
 os.system("rm -rf meme.png")

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
async def jail(ctx, member: discord.Member=None):
 if member == None:
  member=ctx.author
 avatar = member.avatar_url_as(static_format="png")
 os.system(f"wget -O jail.png https://some-random-api.ml/canvas/jail/?avatar={avatar}")
 await ctx.reply(file=discord.File("jail.png"), mention_author=False)
 os.system("rm -rf jail.png")

@client.command()
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def say(ctx,*, arg=None):
 if arg == None:
  await ctx.send("**اكتب نص.**")
 await ctx.channel.purge(limit=1)
 await ctx.send(arg)

client.run("OTYyMzY0MzQ0MjE2MTk5MjI4.YlGdow.FailWE_MSK5JG3aSqgeFG2GPEOU")
