import discord
from discord.ext import commands
import random
import asyncio
import os

prefix="."
client=commands.Bot(command_prefix=prefix)
client.remove_command("help")

@client.event
async def on_ready():
	print(f"تم تشغيل بوت {client.user.name} بنجاح")
	activity = discord.Game(name=f"{prefix}help | Best Bot Forever")
	await client.change_presence(status=discord.Status.dnd, activity=activity)

@client.event
async def on_message(message):
	if message.content == "السلام عليكم":
		await message.channel.send(f"**وعليكم السلام نورت يا {message.author.name}**")
	elif message.content == "سلام عليكم":
		await message.channel.send(f"**وعليكم السلام ورحمة الله وبركاتة نورت سيرفر {message.guild.name}**")
	elif message.content == "باك":
		await message.channel.send(f"**ولكم نورت برجعتك**")
	elif message.content == "برب":
		await message.channel.send(f"**تيت لاتطول :)**")
	elif message.content == "اهلا":
		await message.channel.send(f"**اهلا بك في سيرفر {message.guild.name}**")
	elif message.content == "hello":
		await message.channel.send(f"**Hello {message.author.name} Welcome to {message.guild.name}**")
	elif message.content == "hi":
		await message.channel.send(f"**Hi {message.author.name}**")
	elif message.content == "back":
		await message.channel.send(f"**Welcome**")
	await client.process_commands(message)

@client.command()
@commands.guild_only()
async def help(ctx):
 help=discord.Embed(title="help Menu", description=f"""**
General commands
{prefix}help `Show this menu`
{prefix}ping `Bot speed`
{prefix}server `Getting server info`
{prefix}user `Getting user info`
{prefix}perms `Get user permissions`
{prefix}count `Timer to count down`
{prefix}ss `ScreenShot to any website`

Administrator commands
{prefix}ban `Ban a member form the server (send reason to the dm)`
{prefix}vote `Create vote to {ctx.guild.name} members`

Fun commands
{prefix}yt `Comment on youtube`
{prefix}roll `Roll dice`
{prefix}ben `Asking ben`

`bot replys`
hello, hi
back
اهلا، أهلا
السلام عليكم، السلام عليكم ورحمة الله وبركاتة، سلام عليكم
باك
برب
soon more
**""", color=ctx.author.color)
 help.set_thumbnail(url=ctx.author.avatar_url)
 help.set_footer(text=f"By user: {ctx.author}")
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
    embed.set_footer(text="⭐ • Bil")    
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
 user=discord.Embed(title=f"{user.name}'s info", description=f"""**
UserID: {user.id}
Created At: {user.created_at.strftime(date)}
Joined Server At: {user.joined_at.strftime(date)}
Roles: {roles}
**""", color=ctx.author.color)
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
async def ban(ctx, member: discord.Member = None, *, reason="No reason"):
  if not ctx.message.author.guild_permissions.ban_members:
  	await ctx.send(f"**Hey {ctx.author.name} It's looks like you don't have ban members permission to ban members from {ctx.guild.name}**")
  elif member == ctx.author:
    await ctx.send("**bro you can't ban yourself**")
  elif member == None:
    await ctx.send("**mention a user ** :x:")
  await member.send(f"**you have been banned from {ctx.message.guild.name} by {ctx.author.name} with reason: {reason}**")
  await member.ban(reason=reason)
  await ctx.send(f"**{member} sucessfully banned from {ctx.guild.name} with reason: {reason}**")

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
 ben=["yes", "no", "hohoho", "behhh", "(Closing Phone)"]
 await ctx.send(random.choice(ben))

@client.command()
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def vote(ctx,*, arg):
 vote=discord.Embed(title=arg, description="<:Bil_Yes:962545947571802142> Yes\n<:Bil_Neutral:962545988868931594> Neutral\n<:Bil_No:962546017318883481> No", color=ctx.author.color)
 vote.set_thumbnail(url=ctx.guild.icon_url)
 vote.set_footer(text=ctx.guild.name)
 react=await ctx.send(embed=vote)
 await react.add_reaction("<:Bil_Yes:962545947571802142>")
 await react.add_reaction("<:Bil_Neutral:962545988868931594>")
 await react.add_reaction("<:Bil_No:962546017318883481>")

@client.command()
@commands.guild_only()
async def ss(ctx, site):
 width = 1280
 crop = 720
 os.system(f"wget -O screenshot.png https://image.thum.io/get/width/{width}/crop/{crop}/https://{site}")
 await ctx.reply(f"**Took with {width}x{crop}Resolution**", file=discord.File("screenshot.png"), mention_author=False)
 os.system("rm -rf screenshot.png")

client.run("OTQ0ODU0MTY5MTQ2MjQ5MjU3.YhHqBA.fieLh-dY7KgmLw7BH60M6bPQpSQ")
