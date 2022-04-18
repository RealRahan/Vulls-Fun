
import discord
from discord.ext import commands
import random
import asyncio
import os
import requests

prefix="."
client=commands.Bot(command_prefix=prefix)
client.remove_command("help")
pics=["https://media.discordapp.net/attachments/963977936308936754/963978055154536468/1772-bill-cipher.gif", "https://media.discordapp.net/attachments/963977936308936754/963978054865141790/bill-cipher-gravity-falls.gif", "https://media.discordapp.net/attachments/963977936308936754/963978055536234567/daf4a9385f021eded8dbd0c66e96f0cf604be187_00.gif", "https://media.discordapp.net/attachments/963977936308936754/963978055771103262/190c13fcc842dae188d249889c37c522779db955_00.gif", "https://media.discordapp.net/attachments/963977936308936754/963978055985033216/3c6a9a590f495789c2959a2ff02b52d8.gif", "https://media.discordapp.net/attachments/963977936308936754/963978056291192902/giphy.gif", "https://media.discordapp.net/attachments/963977936308936754/963978056849064006/daobyco-76fe49e4-e57a-4c93-988e-fe7b1f7bd06e.gif", "https://media.discordapp.net/attachments/963977936308936754/963978057167806504/tumblr_nc4mjxKbGg1sntjsso1_400.gif", "https://media.discordapp.net/attachments/963977936308936754/963978057377525830/f77f56fa9662e7b7d8eec9c4392607fb_w200.gif"]

@client.event
async def on_ready():
	print(f"تم تشغيل بوت {client.user.name} بنجاح")
	activity = discord.Game(name=f"{prefix}help | يدعم اللغة العربية بالكامل")
	await client.change_presence(status=discord.Status.dnd, activity=activity)

@client.command()
@commands.guild_only()
async def help(ctx):
 y = 0
 for x in client.guilds:
  y += x.member_count
 await ctx.reply("<a:loading:964951108353159249>", delete_after=3, mention_author=False)
 await asyncio.sleep(3)
 help=discord.Embed(title=f"قائمة المساعدة ({len(client.commands)})", description=f"""**
الأوامر العامة
{prefix}help `هذة القائمة`
{prefix}ping `سرعة استجابة البوت`
{prefix}server `الحصول على معلومات الخادم`
{prefix}user `الحصول على معلومات المستخدم`
{prefix}perms `رؤية صلاحية المستخدم او صلاحياتك`
{prefix}count `عداد وقت، عندما ينتهي يقوم بمنشنتك`
{prefix}ss `لقطة شاشة لأي موقع`
{prefix}lyrics `كلمات الاغنية`

أوامر المشرفون
{prefix}ban `حظر مستخدم من السيرفر (لا تجربة على نفسك!)`

أوامر للمتعة
{prefix}meme `صور مضحكة مع تعليق نصي`
{prefix}roll `رمي النرد`
{prefix}simpcard `إعطاء شخص بطاقة مغفل`
{prefix}jail `سجن مستخدم`
تمت اضافتي في {len(client.guilds)} سيرفر
يتم استخدامي من {y} مستخدم
**""", color=ctx.author.color)
 help.set_thumbnail(url=random.choice(pics))
 help.set_footer(text=f"بواسطة: {ctx.author} | كافة حقوق رموز البوت محفوظة لسنة 2020-2022")
 await ctx.send(embed=help)

@client.command()
@commands.guild_only()
async def ping(ctx):
  await ctx.send(f"**{round(client.latency * 1000)}ميلي ثانية**")

@client.command()
@commands.guild_only()
async def server(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}")
    embed.add_field(name='🆔الرقم التعريفي للسيرفر', value=f"{ctx.guild.id}", inline=True)
    embed.add_field(name='📆انشئ بتاريخ', value=ctx.guild.created_at.strftime("%b %d %Y"), inline=True)
    embed.add_field(name='👑المالك', value=f"<@{ctx.guild.owner_id}>", inline=True)
    embed.add_field(name='👥الأعضاء', value=f'{ctx.guild.member_count} عضو', inline=True)
    embed.add_field(name='💬الرومات', value=f'{len(ctx.guild.text_channels)} كتابي | {len(ctx.guild.voice_channels)} صوتي', inline=True)
    embed.add_field(name='🌎موقع الاتصال', value=f'{ctx.guild.region}', inline=True)
    embed.set_thumbnail(url=ctx.guild.icon_url)   
    embed.set_author(name=f'{ctx.author.name}', icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
async def user(ctx, user: discord.Member = None):
 if user == None:
 	user=ctx.author
 avatar = user.avatar_url_as(static_format="png")
 date = "%b %d %Y"
 roles = ' '.join([r.mention for r in user.roles][1:])
 msg=await ctx.send("**اخذ الرقم التعريفي | <a:loading:964951108353159249>**")
 await asyncio.sleep(0.20)
 await msg.edit(content="**اخذ تاريخ الانشاء | <a:loading:964951108353159249>**")
 await asyncio.sleep(0.20)
 await msg.edit(content="**اخذ تاريخ الدخول | <a:loading:964951108353159249>**")
 await asyncio.sleep(0.20)
 await msg.edit(content="**اخذ معلومات الرتب | <a:loading:964951108353159249>**")
 await msg.delete()
 user=discord.Embed(title=f"{user.name}", description=f"""**
الرقم التعريفي: {user.id}
انشئ بتاريخ: {user.created_at.strftime(date)}
دخل {ctx.guild.name} بتاريخ: {user.joined_at.strftime(date)}
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
async def ban(ctx, member: discord.Member = None,*, reason="No reason"):
 if member == None:
  nomention=discord.Embed(title="خطأ", description="**نسيت ذكر أو وضع معرف أو وضع اسم المستخدم في الحظر**", color=discord.Color.red())
  await ctx.send(embed=nomention)
 await member.ban(reason=reason)
 ban=discord.Embed(title="تم", description=f"**تم حظر {member} بنجاح من {ctx.guild.name}**", color=discord.Color.green())
 ban.set_thumbnail(url=member.avatar_url)
 await ctx.send(embed=ban)
 sendmsg=discord.Embed(title="حصلت على حظر", description=f"**حصلت على حظر من {ctx.guild.name} بواسطة {ctx.author.name} حسب السبب: {reason}\nاذا كان سوء تفاهم ف تحدث معة: {ctx.author}**")
 await member.send(embed=sendmsg)

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
async def ss(ctx, site):
 width = 1280
 crop = 720
 os.system(f"wget -O screenshot.png https://image.thum.io/get/width/{width}/crop/{crop}/https://{site}")
 await ctx.reply(f"**{width}x{crop}**", file=discord.File("screenshot.png"), mention_author=False)
 os.system("rm -rf screenshot.png")

@client.command()
@commands.guild_only()
async def meme(ctx):
 r=requests.get("https://meme-api.herokuapp.com/gimme/armeme")
 meme=discord.Embed(title=r.json()["title"], color=ctx.author.color)
 meme.set_image(url=r.json()["url"])
 meme.set_footer(text=f'Ups: ({r.json()["ups"]})')
 await ctx.send(embed=meme)

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
async def lyrics(ctx,*, arg):
 r=requests.get(f"https://some-random-api.ml/lyrics/?title={arg}")
 if not r.status_code == 200:
 	await ctx.send(f"**لايمكنني العثور على الاغنية: {arg}**")
 if len(r.json()["lyrics"]) > 6000:
 	await ctx.send("**الأغنية تتعدى الـ6000 حرف وهذا هو العدد المسموح للديسكورد.**")
 l=discord.Embed(title=f"{r.json()['title']} ({r.json()['author']})", description=f"**{r.json()['lyrics']}**", color=ctx.author.color)
 l.set_thumbnail(url=r.json()['thumbnail']['genius'])
 await ctx.send(embed=l)

client.run("OTQ0ODU0MTY5MTQ2MjQ5MjU3.YhHqBA.jri3z5nkNJal6Z7yoKY2UrLOkus")
