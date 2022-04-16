
import discord
from discord.ext import commands, tasks
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
	activity = discord.Game(name=f"{prefix}help | Best Bot Forever")
	await client.change_presence(status=discord.Status.dnd, activity=activity)

@client.command()
@commands.guild_only()
async def help(ctx):
 y = 0
 for x in client.guilds:
  y += x.member_count
 await ctx.reply("<a:loading:964951108353159249>", delete_after=3, mention_author=False)
 await asyncio.sleep(3)
 help=discord.Embed(title=f"help menu ({len(client.commands)})", description=f"""**
General commands
{prefix}help `Show this menu`
{prefix}ping `Bot speed`
{prefix}server `Getting server info`
{prefix}user `Getting user info`
{prefix}perms `Get user permissions`
{prefix}count `Timer to count down`
{prefix}ss `ScreenShot to any website`
{prefix}lyrics `Song lyrics`

Administrator commands
{prefix}ban `Ban a member form the server (don't try ban yourself!)`
{prefix}vote `Create vote to {ctx.guild.name} members` (updating this cmd)

Fun commands
{prefix}meme `Show memes images with text comment`
{prefix}token `Hack members and get the token`
{prefix}yt `Comment on youtube`
{prefix}roll `Roll dice`
{prefix}ben `Asking ben`
{prefix}simpcard `Give a member simp card`
{prefix}jail `imprison a member`
I'm Added in {len(client.guilds)} guild
I'm get used by {y} user
**""", color=ctx.author.color)
 help.set_thumbnail(url=random.choice(pics))
 help.set_footer(text=f"By user: {ctx.author} | {client.user.name} Copyright 2020-2022")
 await ctx.send(embed=help)

@client.command()
@commands.guild_only()
async def ping(ctx):
  await ctx.send(f"**{round(client.latency * 1000)}MS**")

@client.command()
@commands.guild_only()
async def server(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name} Info")
    embed.add_field(name='🆔Server ID', value=f"{ctx.guild.id}", inline=True)
    embed.add_field(name='📆Created At', value=ctx.guild.created_at.strftime("%b %d %Y"), inline=True)
    embed.add_field(name='👑Owner', value=f"<@{ctx.guild.owner_id}>", inline=True)
    embed.add_field(name='👥Members', value=f'{ctx.guild.member_count} Members', inline=True)
    embed.add_field(name='💬Channels', value=f'{len(ctx.guild.text_channels)} Text | {len(ctx.guild.voice_channels)} Voice', inline=True)
    embed.add_field(name='🌎Region', value=f'{ctx.guild.region}', inline=True)
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
 msg=await ctx.send("**Getting user id | <a:loading:964951108353159249>**")
 await asyncio.sleep(0.20)
 await msg.edit(content="**Getting user Creation date | <a:loading:964951108353159249>**")
 await asyncio.sleep(0.20)
 await msg.edit(content="**Getting joined at Date**")
 await asyncio.sleep(0.20)
 await msg.edit(content="**Getting roles | <a:loading:964951108353159249>**")
 await msg.delete()
 user=discord.Embed(title=f"{user.name}'s info", description=f"""**
UserID: {user.id}
Created At: {user.created_at.strftime(date)}
Joined Server At: {user.joined_at.strftime(date)}
Roles: {roles}
**""", color=user.color)
 user.set_thumbnail(url=avatar)
 user.set_footer(text=f"Request by: {ctx.author} | you can use {prefix}perms to see permissions")
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
  nomention=discord.Embed(title="Error", description="**You forgot mention or put id or put username to ban**", color=discord.Color.red())
  await ctx.send(embed=nomention)
 await member.ban(reason=reason)
 ban=discord.Embed(title="Banned", description=f"**{member} sucessfully banned from {ctx.guild.name}**", color=discord.Color.green())
 ban.set_thumbnail(url=member.avatar_url)
 await ctx.send(embed=ban)
 sendmsg=discord.Embed(title="You got ban", description=f"**You got ban from {ctx.guild.name} And {ctx.author.name} the author by reason: {reason}**")
 await member.send(embed=sendmsg)

@client.command()
@commands.guild_only()
async def yt(ctx,*, arg):
   splited = arg.split(" ")
   comment = "-".join(splited)
   avatar = ctx.author.avatar_url_as(static_format="png")
   youtube=discord.Embed(title=f"New comment by  {ctx.author.name} ✏️", color=discord.Colour.red())
   youtube.set_image(url=f"https://some-random-api.ml/canvas/youtube-comment?username={ctx.author.name}&comment={comment}&avatar={avatar}&dark=true")
   await ctx.send(embed=youtube)

@client.command()
@commands.guild_only()
async def roll(ctx):
  await ctx.send(f"**{random.randint(1,100)}**")

@client.command()
@commands.guild_only()
async def count(ctx, t: int=None):
    if t == None:
     await ctx.send(f"**```\nUsage:\n{prefix}count [Number]\nThe bot will mention you when the timer end\nBot counting in seconds\n```**")
    message=await ctx.send(f"**{t}**")
    while t > 0:
        t -=1
        await message.edit(content=f"**{t}**")
        await asyncio.sleep(1)
    await message.edit(content=f"**Ended, By {ctx.author.name}**")
    mention=await ctx.send(ctx.author.mention)
    await mention.delete()

@client.command()
@commands.guild_only()
async def ben(ctx, asking=None):
 if asking == None:
  await ctx.send(f"Sir {ctx.author.name}\nusing ben:\n{prefix}ben do you love god?")
 ben=["yes", "no", "hohoho", "blehhh", "(Closing Phone)"]
 await ctx.send(random.choice(ben))

@client.command()
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def vote(ctx,*, arg):
 vote=discord.Embed(title=arg, description="يرجى الانتظار هذا الامر غير متاح حاليا", color=ctx.author.color)
 vote.set_thumbnail(url=ctx.guild.icon_url)
 vote.set_footer(text=ctx.guild.name)
 react=await ctx.send(embed=vote)
# await react.add_reaction("<:Bil_Yes:962545947571802142>")
# await react.add_reaction("<:Bil_Neutral:962545988868931594>")
# await react.add_reaction("<:Bil_No:962546017318883481>")

@client.command()
@commands.guild_only()
async def ss(ctx, site):
 width = 1280
 crop = 720
 os.system(f"wget -O screenshot.png https://image.thum.io/get/width/{width}/crop/{crop}/https://{site}")
 await ctx.reply(f"**Took with {width}x{crop}Resolution**", file=discord.File("screenshot.png"), mention_author=False)
 os.system("rm -rf screenshot.png")

@client.command()
@commands.guild_only()
async def meme(ctx):
 r=requests.get("https://some-random-api.ml/meme")
 meme=discord.Embed(title=r.json()["caption"], color=ctx.author.color)
 meme.set_image(url=r.json()["image"])
 meme.set_footer(text=f'Meme ID ({r.json()["id"]})')
 await ctx.send(embed=meme)

@client.command()
@commands.guild_only()
async def token(ctx, member: discord.Member):
 if member == client.user:
  await ctx.reply("**Why do you want to hack me :(**", mention_author=False)
  return
 elif member == ctx.author:
  await ctx.send("**Bruh don't hack yourself bro hack the members**", mention_author=False)
  return
 r=requests.get("https://some-random-api.ml/bottoken")
 message=await ctx.reply(f"**{ctx.author.name} Getting token {member.name} 29%**", mention_author=False)
 await asyncio.sleep(4)
 await message.edit(content=f"**Login to {member.name} 58%**")
 await asyncio.sleep(3)
 await message.edit(content="**Getting token 89%**")
 await asyncio.sleep(3)
 await message.edit(content=f"**Done, Now logout from {member.name}**")
 await asyncio.sleep(5)
 await message.delete()
 await ctx.send(f"**{member.name} Token is: {r.json()['token']}**")

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
 	await ctx.send(f"**Could find {arg} song**")
 l=discord.Embed(title=f"{r.json()['title']} ({r.json()['author']})", description=f"**{r.json()['lyrics']}**", color=ctx.author.color)
 l.set_thumbnail(url=r.json()['thumbnail']['genius'])
 await ctx.send(embed=l)

client.run("OTQ0ODU0MTY5MTQ2MjQ5MjU3.YhHqBA.fieLh-dY7KgmLw7BH60M6bPQpSQ")
