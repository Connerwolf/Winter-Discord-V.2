from os import name
import time
import json
import discord
from discord.ext import commands ,tasks
from datetime import date, timedelta
import sqlite3
from utility.reddit_api import praw_get
from utility.colors import randomcolor

# Config File

with open("./setup/bot_config.json") as c:
    config = json.load(c)

# Bot Setup

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=config["prefix"], id=config["owner_id"], intents=intents)
client.remove_command("help")
start_time = time.time()

# Functions

def ping():
    data = f"{round(client.latency*100)}ms"
    return data

def uptime():
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(timedelta(seconds=difference))
    return text

def version():
    v = config["version"]
    return v

def cur_activity(name,mode):
    if mode == "watching":
        watching = discord.ActivityType.watching
        activity = discord.Activity(name=name, type=watching)
        return activity

    elif mode == "playing":
        playing = discord.ActivityType.playing
        activity = discord.Activity(name=name, type=playing)
        return activity
    
    elif mode == "listening":
        listening = discord.ActivityType.listening
        activity = discord.Activity(name=name, type=listening)
        return activity

def guilds():
    data = len(client.guilds)
    return data

def report(content):
    async def send_report():
        user = await client.fetch_user(450223497021489163)
        await user.send(f"``Report: {content}``")

# Login

@client.event
async def on_ready():
    print(f"Client Booted | No Error | Ping: {ping()}")
    user = await client.fetch_user(450223497021489163) 
    activity = cur_activity(f"$help | {guilds()} Servers", "watching")
    await user.send(f"``Client Booted | No Error | Ping: {ping()}``")
    await client.change_presence(activity=activity)

    mainloop.start()

# Task Loop
@tasks.loop(minutes=5)
async def mainloop():
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    cur.execute("SELECT ID FROM MemeLoop")
    res = cur.fetchall()
    for r in res:
        channel = client.get_channel(r[0])
        meme = praw_get("memes")
        embed = discord.Embed(
            title = f":pencil: {meme.title}",
            description = f"[Open in browser]({meme.url})",
            color = randomcolor()
        )
        embed.set_image(url=meme.url)
        embed.set_footer(icon_url=client.user.avatar_url, text=f"Requested by {client.user.name}")
        await channel.send(embed=embed)
        con.close()

# Custom Activity

@commands.is_owner()
@client.command()
async def activity(ctx, mode, *, name=None):
    if mode == "default" and name == None:
        data = cur_activity(f"$help | {guilds()} Servers", "watching")
        await client.change_presence(activity=data)
    else:
        data = cur_activity(name, mode)
        await client.change_presence(activity=data)

# Cog Pre-Loader

initial_extensions = [
                        "cogs.Facts",
                        "cogs.Gif",
                        "cogs.Animals",
                        "cogs.Meme",
                        "cogs.Reddit",
                        "cogs.Wiki",
                        "cogs.Mod",
                        "cogs.Server",
                        "cogs.Errors",
                        "cogs.Help",
                        "cogs.AutoMeme"
                    ]

for extension in initial_extensions:
    client.load_extension(extension)
    print(f"Loaded: {extension}")

# Cog Manual Control

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    cog = f"cogs.{extension}"
    try:
        client.load_extension(cog)
        embed = discord.Embed(
            title = ":gear: Cog Control Panel",
            color = discord.Color.red()
        )
        embed.add_field(name=":file_folder: Name", value=extension, inline=True)
        embed.add_field(name=":pushpin: Result", value=f"Cog has been loaded", inline=False)
        embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    except Exception as e:
        if cog in initial_extensions:
            embed = discord.Embed(
            title = ":closed_book: Error",
            color = discord.Color.red()
            )
            embed.add_field(name=":file_folder:Name", value=extension, inline=True)
            embed.add_field(name=":pushpin: Issue", value=f"Cog is already loaded", inline=False)
            embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
            title = ":closed_book: Error",
            color = discord.Color.red()
            )
            embed.add_field(name=":file_folder: Name", value=extension, inline=True)
            embed.add_field(name=":pushpin: Issue", value=f"Cog not found", inline=False)
            embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    cog = f"cogs.{extension}"
    try:
        client.unload_extension(cog)
        embed = discord.Embed(
            title = ":gear: Cog Control Panel",
            color = discord.Color.red()
        )
        embed.add_field(name=":file_folder: Name", value=extension, inline=True)
        embed.add_field(name=":pushpin: Result", value=f"Cog has been unloaded", inline=False)
        embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    except Exception as e:
        if cog in initial_extensions:
            embed = discord.Embed(
            title = ":closed_book: Error",
            color = discord.Color.red()
            )
            embed.add_field(name=":file_folder: Name", value=extension, inline=True)
            embed.add_field(name=":pushpin: Issue", value=f"Cog is not loaded", inline=False)
            embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
            title = ":closed_book: Error",
            color = discord.Color.red()
            )
            embed.add_field(name=":file_folder: Name", value=extension, inline=True)
            embed.add_field(name=":pushpin: Issue", value=f"Cog not found", inline=False)
            embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    cog = f"cogs.{extension}"
    try:
        client.unload_extension(cog)
        client.load_extension(cog)
        embed = discord.Embed(
            title = ":gear: Cog Control Panel",
            color = discord.Color.red()
        )
        embed.add_field(name=":file_folder: Name", value=extension, inline=True)
        embed.add_field(name=":pushpin: Result", value=f"Cog has been reloaded", inline=False)
        embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    except Exception as e:
        if cog in initial_extensions:
            embed = discord.Embed(
            title = ":closed_book: Error",
            color = discord.Color.red()
            )
            embed.add_field(name=":file_folder: Name", value=extension, inline=True)
            embed.add_field(name=":pushpin: Issue", value=f"Cog failed to reloaded", inline=False)
            embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
            title = ":closed_book: Error",
            color = discord.Color.red()
            )
            embed.add_field(name=":file_folder: Name", value=extension, inline=True)
            embed.add_field(name=":pushpin: Issue", value=f"Cog not found", inline=False)
            embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def sleep(ctx, action:bool):
    if action == True: 
        try:
            for extension in initial_extensions:
                cog = f"cogs.{extension}"
                client.unload_extension(extension)

            embed = discord.Embed(
                title = ":gear: Cog Control Panel",
                color = discord.Color.magenta()
            )
            embed.add_field(name=":label: Cog State", value="Sleeping", inline=True)
            embed.add_field(name=":pushpin: Result", value=f"All Cogs turned off.", inline=False)
            embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
            activity = cur_activity(name="Sleep Mode",mode="watching")
            await client.change_presence(activity=activity)

        except Exception as e:
            report(e)

    elif action == False: 
        try:
            for extension in initial_extensions:
                cog = f"cogs.{extension}"
                client.load_extension(extension)

            embed = discord.Embed(
                title = ":gear: Cog Control Panel",
                color = discord.Color.magenta()
            )
            embed.add_field(name=":label: Cog State", value="Awake", inline=True)
            embed.add_field(name=":pushpin: Result", value=f"All Cogs turned on.", inline=False)
            embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
            data = cur_activity(f"$help | {guilds()} Servers", "watching")
            await client.change_presence(activity=data)

        except Exception as e:
            report(e)

client.run(config["token"]) 
