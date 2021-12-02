import discord
from discord.ext import commands
from utility.reddit_api import praw_get
from utility.colors import randomcolor

class Animals(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cat(self, ctx):
        data = praw_get("catpictures")
        embed = discord.Embed(
            title = f":pencil: {data.title}",
            description = f"[Open in browser]({data.url})",
            color = randomcolor()
        )
        embed.set_image(url=data.url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command()
    async def dog(self, ctx):
        data = praw_get("dogpictures")
        embed = discord.Embed(
            title = f":pencil: {data.title}",
            description = f"[Open in browser]({data.url})",
            color = randomcolor()
        )
        embed.set_image(url=data.url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Animals(client))