#Dub's Meme Bot by Dub

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import random

bot = commands.Bot(command_prefix='^')

@bot.event
async def on_ready():
    print ("All Systems ONLINE x)")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def urmomgay(ctx):
    await bot.say("https://orig00.deviantart.net/8dfa/f/2017/039/1/0/beep_boop_your_mom_gay_by_spartans3m-dayamxu.gif")


@bot.command(pass_context=True)
async def robloxdab(ctx):
    await bot.say("https://t7.rbxcdn.com/447a533760df28dd2760e56a1e2ad580")

@bot.command()
async def info(member:discord.Member):
    """Tells you some info about the member."""
    fmt = '{0} joined on {0.joined_at} and has {1} roles.'.format(member, len(member.roles))

@bot.command(pass_context=True)
async def insult(ctx):
    await bot.say("You're Gay :stuck_out_tongue_winking_eye:")

@bot.command(pass_context=True)
async def credits(ctx):
    embed = discord.Embed(name="Lonely-Bot Credits", description="Lonely-Bot's Creator", color=0x6D00CC)
    embed.add_field(name="CopypasteMasta", value="Dub", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def wc(ctx, user:discord.Member):
    embed = discord.Embed(name="Wall Checks", description= "Used to check if walls are clear", color=0x6D00CC)
    embed.add_field(name="Wall Status", value="Clear", inline=True)
    embed.add_field(name="Checked By", value= user.name, inline=True)
    await bot.say(embed=embed) 

@bot.command(pass_context=True)
async def owner(ctx):
    await bot.say("After hours of nonstop copy-paste, this is the best Dub could manage.")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("NO")

@bot.command(pass_context=True)
async def shrug(ctx):
    await bot.say(" ¯\_(ツ)_/¯ ")

@bot.command(name='8ball', pass_context=True)
async def eight_ball(context):       
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
        'Isnt it obvious?',
        'How about no?',
        'Its a possiblilty to consider',
    ]
    await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@bot.command(name='slap', pass_context=True)
async def slap(context):
    possible_responses = [
        'https://i.pinimg.com/originals/fc/e1/2d/fce12d3716f05d56549cc5e05eed5a50.gif',
        'https://i.pinimg.com/originals/fc/e1/2d/fce12d3716f05d56549cc5e05eed5a50.gif',
        'https://media.giphy.com/media/AkKEOnHxc4IU0/giphy.gif',
        'https://reallifeanime.files.wordpress.com/2014/06/akari-slap.gif',
        'https://media.giphy.com/media/VEmm8ngZxwJ9K/giphy.gif',
        'https://media1.giphy.com/media/127h8dMHnk5H5C/giphy.gif',
    ]
    await bot.say(random.choice(possible_responses) + " ")
    
@bot.command(pass_context=True)
async def wink(ctx):
    await bot.say("wInK woNk :wink:")    
    
     

bot.run("Mjc1NzExNDY2NjkzMTk3ODI2.DXh_wg.ujMgs2XvRvwPZiqKk8L3hnyD-gE")