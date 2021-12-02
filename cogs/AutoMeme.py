import discord
from discord.ext import commands
import sqlite3


class AutoMeme(commands.Cog):
    def __init__(self, client):
        self.client = client

    try:
        with sqlite3.connect("main.db") as con:
            cur = con.cursor()
            cur.execute("CREATE TABLE MemeLoop (ID int)")
            con.commit()
    
    except Exception as e:
        pass

    @commands.command()
    async def automeme(self, ctx, mode):
        try:
            print("test 1")
            print(mode)
            if mode == "on":
                print("test 2")
                with sqlite3.connect("main.db") as con:
                    channel = ctx.channel.id
                    cur = con.cursor()
                    cur.execute("SELECT ID FROM MemeLoop WHERE ID = {}".format(channel))
                    res = cur.fetchone()
                    
                    if res == None:
                        print("test 3")
                        cur.execute("INSERT INTO MemeLoop (ID) VALUES ({})".format(channel))
                        con.commit()
                        embed = discord.Embed(
                        title = f":computer: AutoMeme",
                        color = discord.Color.from_rgb(210,60,60)
                        )
                        embed.add_field(name=":gear: Status :", value="ON | Turned on for this channel.",inline=False)
                        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
                        await ctx.send(embed=embed)

                    else:
                        embed = discord.Embed(
                        title = f":closed_book: Error",
                        color = discord.Color.from_rgb(210,60,60)
                        )
                        embed.add_field(name=":gear: Issue:", value="AutoMeme already Running in this channel",inline=False)
                        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
                        await ctx.send(embed=embed)

            elif mode == "off":
                print("test 4")
                with sqlite3.connect("main.db") as con:
                    channel = ctx.channel.id
                    cur = con.cursor()
                    cur.execute("SELECT ID FROM MemeLoop WHERE ID = {}".format(channel))
                    res = cur.fetchone()

                    if res == None:
                        embed = discord.Embed(
                        title = f":closed_book: Error",
                        color = discord.Color.from_rgb(210,60,60)
                        )
                        embed.add_field(name=":gear: Issue:", value="AutoMeme not currently Running in this channel",inline=False)
                        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
                        await ctx.send(embed=embed)

                    else:
                        cur.execute("DELETE FROM MemeLoop WHERE ID = {}".format(channel))
                        con.commit()
                        embed = discord.Embed(
                        title = f":computer: AutoMeme",
                        color = discord.Color.from_rgb(210,60,60)
                        )
                        embed.add_field(name=":gear: Status :", value="OFF | Turned off for this channel.",inline=False)
                        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
                        await ctx.send(embed=embed)
        
        except Exception as e:
            print(f"Error: {e}")

def setup(client):
    client.add_cog(AutoMeme(client))