import discord
import random
import os
import asyncio
import os, random
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
from pkg_resources import WorkingSet


client = commands.Bot(command_prefix=["send "])

@client.event
async def on_ready():
    print('hentai sender is ready') 


@client.command()
async def hentai(ctx):
        await randomSpam("uncanon", ctx)


async def randomSpam(name, ctx):
    stored = []
    for subdirs, dirs, files in os.walk(name):
        for file in files:
            filepath = subdirs + os.sep + file
            stored.append(os.path.abspath(filepath))
    list = random.sample(stored, 10) # change this number to change the number of hentai sent
    for i in list:
        await ctx.send(file=discord.File(i))
        await asyncio.sleep(0.8) # change the 0.8 value to change delay

client.run('token here')   