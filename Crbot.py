#import things
import discord
from discord.ext import commands
import random
import asyncio
from discord.utils import get
from discord import Game

bot = commands.Bot(command_prefix='.')


maps = ["940-9970-7913 – CizzorzDeathRun Challenge, parkour challenge",
        "3624-9134-2626 – MW2 Rust, classic COD map", "0213-4672-2099 – Janky Jail, fun multiplayer map",
        "6352-8048-2222 – Snipers Vs Runners, inventive mini game",
        "0632-6317-2480 – Tinker’s Toystore",
        "4264-02210-9408 – Merls Battle Arena",
        "4203-6925-0108 – Shipment COD 4, ideal for a frantic FFA",
        "1743-0750-4752 - New Aircraft Mode! 2 Ships and 2 Teams / Explosive Weapons / Legendary Weapons / Check out Island-Codes.com for all Creatives maps! ",
        "0036-5652-3629 - An oil company has come across a big Discovery! Grab your diving gear and find it before others do! FFA Map by Senix & Dfault_skin / Island-Codes.com ",
        "2201-4498-7425 - Shotgun Arena for 4 Teams / All Shotguns / Respawn / Full life + Full shield / Map by Senix",
        "0551-6888-0933 - AIM Deagle from CSS. Only Deagle / 2 Teams / Fulllife + Fullshield / Respawn / Map by Senix ",
        "3847-9331-2064 - Elevate or Practice your Edits in your choice of 3 Courses!",
        " 0940-9970-7913 - Good Luck... You'll need it. Check YouTube Video Description for FULL LIST of Rules!! Submit Best Runs before 2019. Make sure you have video proof. ",
        "8335-1484-3001 - literally just the words Code and LazarBeam",
        "6561-6398-2653 - QUICK WARMUP COURSE TO DO BEFORE YOU PLAY. Use Code: CanDook",
        "2713-8534-8732 - Escape the big house",
        "3719-3214-8173 - Visual Escape Maze 2",
        "0643-0361-6954 - Mongraal Edit course",
        "9723-1485-5757 - Parkour school for noobs ",]


@bot.event
async def on_ready():
    print("Starting up")
    await bot.change_presence(activity=Game(".randcode"))
   


@bot.command()
async def addcode(ctx, *, map):
    if ctx.message.author.id == 427841299920453634:
        maps.append(map)
        print(maps)
        await ctx.send(f"The map {map} has append to maps list")
    else:
        await ctx.send("only the owner of the bot can use this command")




@bot.command()
async def randcode(ctx):
    await ctx.send(random.choice(maps))
    


@bot.command()
async def allcode(ctx):
    await ctx.send(maps)




@bot.command()
async def removecode(ctx, map):
    author = ctx.message.author
    if author.id == 427841299920453634:
       maps.remove(map)
    await ctx.send(f"The map {map} is removed from maps list")



bot.run("NTcwMTcwNjY5ODc5NTI1Mzg2.XL7S_w.z1eh36akqLgSHXVk02on1Ek3mf8")
