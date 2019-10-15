import discord
from discord.ext import commands
import json
import aiohttp
import random
import urllib.parse, urllib.request, re

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Server Bot", description="Worst bot ever", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="Bird")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="prefix", value="?")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Server ip", value="")

    await ctx.send(embed=embed)

@bot.command()
async def up(ctx):
    await bot.change_presence(activity=discord.Game(name='Server is Online | ?help'))

@bot.command()
async def down(ctx):
    await bot.change_presence(activity=discord.Game(name='Server is Offline | ?help'))
    await ctx.send(" <@275129399865769984> come fix it")


@bot.command()
async def hamachi(ctx):
    embed=discord.Embed(title="Download Hamachi", url="https://www.vpn.net/", description="You will need hamachi to join any of our servers", color=0xeee657)
    embed.set_thumbnail(url="https://dl1.cbsistatic.com/i/2019/03/27/a59bd109-031e-4e0e-ae14-55c8c2630d2d/f95bb8591c588d0c1d56e1749423e50d/imgingest-640041164592742636.png")

    embed.add_field(name="We currently have 3 hamachi servers", value="All 3 have been listed below", inline=False)
    embed.add_field(name="Server One:(5/5)", value="Server ID: aidanadamminecraft Password: peepee", inline=False)
    embed.add_field(name="Server Two:(5/5)", value="Server ID: minecraftserver484112211 Password: Aidan112211", inline=False)
    embed.add_field(name="Server Three(2/5)", value="Server ID :Minecraftgang112211 Password: Aidan112211", inline=False)
    embed.set_footer(text="Join Any open Server then to get the Server IP for any of our servers do ?help and find the server you want to join")

    await ctx.send(embed=embed)



@bot.command()
async def skyfactory(ctx):
    embed = discord.Embed(title="Skyfactory Download", url="https://www.feed-the-beast.com/projects/ftb-presents-skyfactory-3/files/2481283", description="Here you can download the modpack", color=0xeee657)

    # give info about you here
    embed.set_thumbnail(url="https://media.forgecdn.net/avatars/83/195/636186954657341781.png")



    embed.add_field(name="Server Ip", value="25.71.20.230:25565", inline=False)

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Bot Commands", description=" List of commands are:", color=0xeee657)

    embed.add_field(name="?add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="?multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="?greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="?cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="?invite", value="Gives an invite link for the bot", inline=False)
    embed.add_field(name="?help", value="Gives this message", inline=False)
    embed.add_field(name="?skyfactory", value="Gives info about skyfactory server", inline=False)
    embed.add_field(name="?up", value="Toggles the bot server status on", inline=False)
    embed.add_field(name="?down", value="toggles the bot server status off", inline=False)
    embed.add_field(name="?hamachi", value="Shows you where to download hamachi and our current servers", inline=False)
    embed.add_field(name="?[redacted]", value="[redacted]", inline=False)
    embed.add_field(name="?[redacted]", value="[redacted] ", inline=False)
    embed.add_field(name="?[redacted]", value="[redacted] ", inline=False)
    embed.add_field(name="?giphy", value="search giphy. example: ?giphy cat (Must include a space)", inline=False)
    embed.add_field(name="?youtube", value="search youtube. example: ?youtube minercaft (Must include a space)", inline=False)

    await ctx.send(embed=embed)

    

@bot.command()
async def birthday(ctx):
    embed=discord.Embed(title="Birthdays", description="All 5 of the gang members Birthdays ", color=0xeee657)
    embed.add_field(name="Jacob", value="May 28", inline=False)
    embed.add_field(name="John", value="April 28", inline=True)
    embed.add_field(name="Aidan", value="April 8", inline=True)
    embed.add_field(name="Adam" , value="January 15", inline=True)
    embed.add_field(name="Pepe", value="July 23", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def wifi(ctx):
    embed=discord.Embed(title="Wifi Passwords", description="All 5 of the gang members Wifi Passwords ", color=0xeee657)
    embed.add_field(name="Jacob", value="dftp2525", inline=False)
    embed.add_field(name="John", value="7116445358", inline=True)
    embed.add_field(name="Aidan", value="aidanrileyjack", inline=True)
    embed.add_field(name="Adam" , value="heavyshrub699", inline=True)
    embed.add_field(name="Pepe", value="Fair1035", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
    embed = discord.Embed(title="Invite Link", url="https://discordapp.com/api/oauth2/authorize?client_id=562970733781844008&permissions=8&scope=bot", description="Here you can invite me to your server", color=0xeee657)

    # give info about you here
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/f/f3/Erithacus_rubecula_with_cocked_head.jpg")



    embed.add_field(name="Requirements", value="jack shit, just let me send and read messages", inline=False)

    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def youtube(ctx, *search):
    searchTerm = ' '.join(search)
    query_string = urllib.parse.urlencode({'search_query': searchTerm})
    htm_content = urllib.request.urlopen('https://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])



@bot.command()
async def giphy(ctx, *, search):
    embed = discord.Embed(colour=discord.Colour.blue())
    session = aiohttp.ClientSession()

    if search == '':
        response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=API_KEY_GOES_HERE')
        embed.set_image(url=data['data']['images']['original']['url'])
    else:
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=API_KEY_GOES_HERE&limit=10')
        gif_choice = random.randint(0, 9)
        embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

    data = json.loads(await response.text())
    await session.close()

    await client.send_message(embed=embed)


bot.run('NTk0NjYxOTI3ODQyNzQyMzA0.XRgYCQ.jB6bqDs42S34l8GKgsSZc8O3Q0s')
