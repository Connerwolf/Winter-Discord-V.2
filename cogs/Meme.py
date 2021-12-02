import random
import discord
from discord.ext import commands
from utility.reddit_api import praw_get
from utility.colors import randomcolor

class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx):
        meme = praw_get("memes")
        embed = discord.Embed(
            title = f":pencil: {meme.title}",
            description = f"[Open in browser]({meme.url})",
            color = randomcolor()
        )
        embed.set_image(url=meme.url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Meme(client))