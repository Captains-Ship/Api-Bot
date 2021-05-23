import urllib.request, json
import discord
import random
from random import *
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Member
from traceback import format_exception
import io
import contextlib
from io import BytesIO
from pprint import pprint
import os
from dotenv import load_dotenv
import textwrap
import asyncio
import json
import datetime
import random as r


client = commands.Bot(command_prefix ="c!", intents=discord.Intents.all())



@client.event
async def on_ready():
        print("ready")



@client.command()
async def joke(ctx):
        """get a chuck norris joke"""
        with urllib.request.urlopen("http://api.icndb.com/jokes/random") as url:
            data = json.loads(url.read().decode())
            value = data["value"]
            joke = uwu["joke"]
            await ctx.reply(joke)


@client.command()
async def bored(ctx):
        """Get an activity to do"""
        with urllib.request.urlopen("https://www.boredapi.com/api/activity") as url:
            data = json.loads(url.read().decode())
            activity = data["activity"]
            await ctx.reply(activity)





@client.command()
async def reddit(ctx, *, sub="memes"):
        """Reddit API integration"""
        with urllib.request.urlopen(f"https://www.reddit.com/r/{sub}/new.json") as url:
                    jsondata = json.loads(url.read().decode())
                    data = jsondata["data"]
                    children = data["children"]
                    postnum = r.randint(0, 24)
                    post = children[postnum]
                    postdata = post["data"]
                    nsfwcheck = postdata["over_18"]
                    if nsfwcheck == True:
                            await ctx.reply("post gathered was NSFW!")
                    else:
                            name = postdata["title"]
                            link = postdata["url"]
                            content = postdata["selftext"]
                            image = postdata["thumbnail"]
                            creator = postdata["author"]
                            embed = discord.Embed(
                                    title=f"{name}",
                                    description=f"{content}",
                                    url=link,
                                    colour=discord.Colour.blurple()
                            )
                            try:
                                    embed.set_image(url = postdata["url_overridden_by_dest"])
                            except:
                                    pass
                            embed.set_footer(text="Post by " + creator)
                            embed.set_author(name="Videos and galleries (multiple images 1 post) are NOT supported!")
                            await ctx.reply(embed=embed)




client.run("token")








