#!/bin/python3
import discord
import os
import requests
import json
import random
import asyncio
import datetime
import time
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from dotenv import load_dotenv
from discord.utils import get 
from itertools import zip_longest
from discord import guild

client = commands.Bot(command_prefix="//")

client.remove_command('help')
rate=5
time=60
uptime = os.popen('uptime -p').read()[:-1]
target=datetime.time(0,0,0)
sad = ["cheerless","despondent","troubled","hurts","hurting","mirthless","mournful","saddened","teary","sorrow","sorrowful","sad", "depressed", "unhappy", "angry", "miserable", "depressing", "failed", "iam sad", "depress", "not happy"]
encourage = ["There you go!","Don’t give up", "Keep pushing.","Keep fighting!","Stay strong.","Never give up.","Never say ‘die’.","Come on! You can do it!","The sky is the limit", "Cheer up!", "Hang in there.", "You are a great person.", "Hey, dont worry, everything will be alright!", "You are a irreplacable person", "Dont worry, let me tell you a fact. you are really irreplacable person in this server.", "never better"] 
welcome = ["boo!","there!","mate","Howdy, howdy ,howdy!","partner!","sunshine!","It only takes a minute to say 'Hello', but it can make a big difference in someones day!","Saying hello doesn't have an ROI. It's about building relationships","If you're brave enough to say goodbye, life will reward you with a new hello.","I want to be your favorite hello and hardest goodbye","hi there","Whats up!","buddy!","how was your day!","buddy! Just felt like sharing a smile with you today","Whats special!","How are you?","Hope you are doing great!","A little note to say hello and let you know I care.","Just a note to say hello and wish that you have good times to come your way.","The two hardest things to say in life are hello for the first time and goodbye for the last","I know you are busy. It is good to be busy, but do say hello once in a while.","Are pigs flying? I haven't heard from you in a while. Hello!","Just to let you know that you can call from an iPhone to an Android. Hello!","When I stop thinking about you, I start missing you. When are we catching up?","Dont scold me my developer made me like this."]
arr=[] 
arr1=[] 

def randomquotes():
 response = requests.get("https://zenquotes.io/api/random")
 data = json.loads(response.text)
 quote = data[0]['q'] + "\t-" + data[0]['a']
 return quote

def todaysquotes():
 response = requests.get("https://zenquotes.io/api/today")
 data = json.loads(response.text)
 quote = data[0]['q'] + "\t-" + data[0]['a']
 return quote

@client.event
async def on_ready():
 print("Pepper On Fire")
 
"""
@client.event
async def on_message(message):
 if message.author == client.user:
  return
 
 lower = message.content.lower()
 channel = message.channel.send
 mention = message.author.mention 
 startswith = message.content.startswith
 content = message.content

 if lower == "//hello" or lower == "//hi" or lower == "//hai" or lower == "//haii" or lower == "//haiii": 
  
   if startswith ("//"):
    str = message.content.translate({ord(i): None for i in '//'})
   elif startswith ("~"):
    str = message.content.translate({ord(i): None for i in '~'})  
   else:
    await channel("Oh dear {} please recheck your command. If you are stuck check help menu.".format(mention))
   await channel(f'{mention} {str},{random.choice(welcome)}')
    
 
 elif message.content == '//' or message.content == '~':
  await channel("Oh dear {}. Use //help to to list commands.".format(mention))

 #if any(word in lower for word in sad):
 # await channel(f'{mention} {random.choice(encourage)}\n') 
 # await channel(f"{mention} {randomquotes()}")
 
 await client.process_commands(message)
"""

@client.event 
@commands.cooldown(2,60,commands.BucketType.user)
async def on_command_error(ctx,error):
 if isinstance(error,commands.CommandOnCooldown):
  msg = "*Slow it down bruh!\n{} Go get a coffee*\n**Command cooldown, releasing in {:.2f}s**".format(ctx.author.mention,error.retry_after)
  await ctx.reply(msg)

@client.command()
@commands.cooldown(7,60,commands.BucketType.user)

async def hello(ctx):
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return

 else :
  async with ctx.message.channel.typing():
   pass
  await ctx.send('{} hello,{}'.format(ctx.author.mention,random.choice(welcome)))

@client.command()
@commands.cooldown(7,60,commands.BucketType.user)
   
async def hi(ctx):
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return

 else :
  async with ctx.message.channel.typing():
   pass 
  await ctx.send('{} hi,{}'.format(ctx.author.mention,random.choice(welcome)))

@client.command()
@commands.cooldown(7,60,commands.BucketType.user)

async def hai(ctx):
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return
 
 else:
  async with ctx.message.channel.typing():
   pass
  await ctx.send('{} hai,{}'.format(ctx.author.mention,random.choice(welcome)))

@client.command()
@commands.cooldown(rate,time,commands.BucketType.user)

async def ping(ctx):
 latency = str(print (f"{round(client.latency * 1000)}"))
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return
 elif latency <= '50':
  msg="Fast as freik boi!!!"
 elif latency <= '100':
  msg="There is more to life than simply increasing it's speed!"
 elif latency <= '200':
  msg="Seems everything under control, but not fast."
 else:
  msg="Slow and steady wins the race."

 async with ctx.message.channel.typing():
  pass
 await ctx.send(f"pong!! {round(client.latency * 1000)}ms\n{msg}")
 
@client.command()
@commands.cooldown(rate,time,commands.BucketType.user)
 
async def inspire(ctx):
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return
 
 else:
  chn=ctx.message.channel
  async with chn.typing():
   pass
  await ctx.send(f"{ctx.message.author.mention} ***{randomquotes()}***")

@client.command()
@commands.cooldown(rate,time,commands.BucketType.user)

async def inspiretoday(ctx):
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return
 else:
  async with ctx.message.channel.typing():
   pass
  await ctx.send(f"{ctx.message.author.mention} ***{todaysquotes()}***")

"""
@client.command()
@commands.cooldown(rate,time,commands.BucketType.user)

async def mirror(ctx,*,args):
 #await ctx.message.delete()
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return

 else: 
  await ctx.send(args)
"""

@client.command()
@commands.cooldown(3,60,commands.BucketType.user)

async def weather(ctx,*,city):
  if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
   return
  else:
   loc = city
   api = ['61efa4b9e592ffa98d8df76ce0da3a4f','f34a1fb82c344f95c666479bea986884','bf5026fdfc56d95fc10c014435f6c45f']
   
   url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(loc,random.choice(api))
   response = requests.get(url)
   data = response.json()
   status = data['cod']
   
      
   if status == 200:
    #async with ctx.message.channel.typing(): 
     city_name = data['name']
     city_description = data['weather'][0]['description']
     city_temp = data['main']['temp']
     city_temp_cel = str(round(city_temp - 273.15))
     city_min_temp = data['main']['temp_min']
     city_max_temp = data['main']['temp_max']
     city_humidity = data['main']['humidity']
     city_lat = data['coord']['lat']
     city_lon = data['coord']['lon']
     city_visibility = data['visibility']
     city_wind = data['wind']['speed']
  
     embed = discord.Embed(title="Weather report of {}".format(city_name),color=discord.Colour.green())
     embed.add_field( name = "Description" , value = "**{}**".format(city_description)         , inline=False)
     embed.add_field( name = "Temperature (C)" , value = "**{}**".format(city_temp_cel)            , inline=False)
     embed.add_field( name = "Humidity (%)"    , value = "**{}**".format(city_humidity)            , inline=False)
     embed.add_field( name = "Coordinates" , value = "**{}**,**{}**".format(city_lat,city_lon) , inline=False)
     embed.add_field( name = "visibility"  , value = "**{}**".format(city_visibility)          , inline=False)
     embed.add_field( name = "Wind (km/h)"        , value = "**{}**".format(city_wind)                , inline=False)
     embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
     embed.set_footer(text="Requested by {}".format(ctx.author.name))
     #send = await ctx.send(embed=embed)
     async with ctx.message.channel.typing():
      pass
     await ctx.send(embed=embed) 
   
   elif status == '404':
     async with ctx.message.channel.typing():
      pass
     await ctx.reply("City not found")
   
   else:
     async with ctx.message.channel.typing():
      await ctx.reply("**{} Unknown error kindly report this to server developer.**".format(ctx.author.mention))

@client.command()
@commands.cooldown(rate,time,commands.BucketType.user)

async def heartbeat(ctx):
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return
 else:
  uptime = os.popen('uptime -p').read()[:-1]
  embed = discord.Embed( title = "Heartbeat **{}**".format(uptime),colour = discord.Colour.red())
  embed.set_footer(text="Requested by {}".format(ctx.author.name))
  
  await ctx.send(embed=embed)  

@client.command()
@commands.cooldown(rate,time,commands.BucketType.user)

async def joke(ctx):
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return
 else:
  async with ctx.message.channel.typing():
   api_url = ['http://official-joke-api.appspot.com/random_joke', 'http://official-joke-api.appspot.com/jokes/random']
   response = requests.get(random.choice(api_url))
   data = json.loads(response.text)
   setup = data['setup']
   punch = data['punchline']
   a=await ctx.send(setup)
   await asyncio.sleep(5)
   await a.reply(punch)

@client.group(invoke_without_command=True)
@commands.cooldown(rate,time,commands.BucketType.user)

async def help(ctx):
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return
 else:
  mention = ctx.message.author.mention 
  orange = discord.Colour.orange()
  red = discord.Colour.red()
  green = discord.Colour.green()
  emcon = discord.Embed( title="Help Menu", description="**Use //help <command> for extended help menu.**", colour = orange)
  
  emcon.add_field(name = "//ping"     , value = "Shows latency."                             , inline=False)
  emcon.add_field(name = "//inspire"  , value = "Get inspirational quotes."                  , inline=False)
  #emcon.add_field(name = "//mirror"   , value = "Makes tony to say what you wish. Try it!!!" , inline=False)
  emcon.add_field(name = "//hello"    , value = "wave hello"                                 , inline=False)
  emcon.add_field(name = "//inspiretoday" , value = "Get quote of the day."                    , inline=False)
  #emcon.add_field(name = "~image"     , value = "Get images."                                , inline=False)
  emcon.add_field(name = "//weather"  , value = "Weather report of a place"                             , inline=False)
  emcon.add_field(name = "//heartbeat", value = "Returns up time of server."                 , inline=False)
  emcon.add_field(name = "//joke"     , value = "Bored? Try me!"                             , inline=False)
  async with ctx.message.channel.typing():
   pass
  await ctx.send(embed = emcon)
 
@help.command()
@commands.cooldown(rate,time,commands.BucketType.user)
async def ping(ctx):
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return
 else:
  emcon = discord.Embed(title = "ping", description = "check latency of the server..", colour=discord.Colour.orange() )
  
  emcon.add_field(name = "**Syntax**", value = "**//ping**")
  await ctx.send(embed = emcon)
 
@help.command()
@commands.cooldown(rate,time,commands.BucketType.user)

async def inspire(ctx):
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return
 else:
  emcon = discord.Embed(title = "Inspirational Quotes", description = "Hear inspirational and motivational quotes", colour=discord.Colour.orange())
  emcon.add_field(name = "**Syntax**", value = "**//inspire**")
  await ctx.send(embed = emcon)
"""
@help.command()
@commands.cooldown(rate,time,commands.BucketType.user)

async def mirror(ctx):
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return
 else:
  emcon = discord.Embed(title = "mirror", description = "Sends text messages of your wish.", colour=discord.Colour.orange() )
  emcon.add_field(name = "**Syntax**", value = "**//mirror <text1,text2,...N**")
  await ctx.send(embed = emcon)
"""
@help.command()
@commands.cooldown(rate,time,commands.BucketType.user)

async def hello(ctx):
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return
 else:
  emcon = discord.Embed(title = "Hello Hai Hi", description = "Wish tony a hello.", colour=discord.Colour.orange() )
  emcon.add_field(name = "**Syntax**", value = "**//hello\n//hai\n//hi**")
  await ctx.send(embed=emcon)

@help.command()
@commands.cooldown(rate,time,commands.BucketType.user)

async def inspiretoday(ctx):
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return
 else:
  emcon = discord.Embed(title = "Today's Inspirational Quotes" , description = "Hear today's motivational/inspirtional quotes", colour=discord.Colour.orange())
  emcon.add_field(name = "**Syntax**", value = "**//inspiretoday**")
  await ctx.send(embed=emcon)

@help.command()
@commands.cooldown(rate,time,commands.BucketType.user)

async def image(ctx):
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return
 else:
  emcon = discord.Embed(title = "Image" , description = "get's images from google", colour=discord.Colour.orange())
  emcon.add_field(name = "**Syntax**", value = "**~image < image name >**")
  await ctx.send(embed=emcon)

@help.command()
@commands.cooldown(rate,time,commands.BucketType.user)

async def weather(ctx):
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return
 else:
  emcon = discord.Embed(title = "Weather Report" , description = "Check weather report of places.", colour=discord.Colour.orange())
  emcon.add_field(name = "**Syntax**", value = "**//weather < place name >**")
  await ctx.send(embed=emcon)

@help.command()
@commands.cooldown(rate,time,commands.BucketType.user)

async def heartbeat(ctx):
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return
 else:
  emcon = discord.Embed(title = "Heartbeat", description = "Shows uptime of server", colour=discord.Colour.orange())
  emcon.add_field(name = "**Syntax**", value = "**//heartbeat**")
  await ctx.send(embed=emcon)

@help.command()
@commands.cooldown(rate,time,commands.BucketType.user)

async def joke(ctx):
 if ctx.channel.id == 868391840079020064 or ctx.channel.id == 870332491087626250 or ctx.channel.id == 871054776811528232:
  return
 else:
  emcon = discord.Embed(title = "Jokes", description = "Ha Ha Ha", colour=discord.Colour.orange())
  emcon.add_field(name = "**SyntaxX**", value = "**//joke**")
  await ctx.send(embed=emcon)


async def dailyquotes():
  
 await client.wait_until_ready()
 f=open('channel.txt','r')
 channel_lines = f.readlines()
 channel_main = client.get_channel(871680070299844608)
 channel_murali = client.get_channel(872722629050638376)
 embed = discord.Embed(title = "Quote Of The Day!!!", description = f"{todaysquotes()}", colour=discord.Colour.blue())
 emcon = discord.Embed(title = "Quote Of The Day!!!", description = f"{todaysquotes()}", colour=discord.Colour.blue())
 await channel_main.send("<@&871748415179071579>",embed=embed)
 
 for x in channel_lines:
  channel_2 = client.get_channel(int(x))
  try:
    embed = discord.Embed(title = "Quote Of The Day!!!", description = f"{todaysquotes()}", colour=discord.Colour.blue())
    await asyncio.sleep(7)
    await channel_2.send(embed=embed)
    
  except:
   pass
 await asyncio.sleep(5) 
 await channel_murali.send("<@&872722625699389470>",embed=embed)

async def background_dailyquotes():
 now = datetime.datetime.utcnow()
 date = datetime.datetime.utcnow().date()
 if now.time() > target:
  tomm = datetime.datetime.combine(date + datetime.timedelta(days=1), datetime.time(0))
  sec = (tomm - now).total_seconds()
  await asyncio.sleep(sec)
 
 while True:
  now = datetime.datetime.utcnow()
  target_time = datetime.datetime.combine(now.date() , target)
  seconds_until_target_time = (target_time - now).total_seconds()
  await asyncio.sleep(seconds_until_target_time)
  await dailyquotes()
  tomm = datetime.datetime.combine(now.date() + datetime.timedelta(days=1), datetime.time(0))
  sec = (tomm - now).total_seconds()
  await asyncio.sleep(sec)


@client.event
async def on_guild_join(guild):
 create_role = await guild.create_role(name="Quodophile")
 role = get(guild.roles,name="Quodophile")
 overwrites = {
     guild.default_role: discord.PermissionOverwrite(read_messages=False),
     guild.me: discord.PermissionOverwrite(read_messages=True),
     role: discord.PermissionOverwrite(read_messages = True , add_reactions = True , send_messages = False , use_external_emojis = True)
 }
 channel = await guild.create_text_channel('📜Quote of the day', overwrites=overwrites)
 role_file = open('role.txt','a')
 role_file.write(str(role.id))
 role_file.write('\n')
 channel = client.get_channel(channel.id)
 channel_file = open('channel.txt','a')
 channel_file.write(str(channel.id))
 channel_file.write('\n')
 pin = await channel.send("***Invite me in your server***\n\n 'https://discord.com/api/oauth2/authorize?client_id=871808444502540379&permissions=8&scope=bot'") 
 await pin.pin()
 await channel.send(f"**Quote-Of-The-Day!**\n\n***{todaysquotes()}***")


client.loop.create_task(background_dailyquotes())
load_dotenv()
dingding=os.getenv('pepper')
client.run(dingding)


