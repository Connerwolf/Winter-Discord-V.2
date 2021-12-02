import discord
from discord.ext import commands
from utility.reddit_api import praw_get
from utility.colors import randomcolor

class Reddit(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def reddit(self, ctx, *, search):
        try:
            reddit = praw_get(search)
            print(praw_get)
            embed = discord.Embed(
                title = f":pencil: {reddit.title})",
                description = f"[Open in browser]({reddit.url})",
                color = randomcolor()
            )
            embed.set_image(url=reddit.url)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
        
        except:
            embed = discord.Embed(
                title = f":closed_book: {reddit.title})",
                color = randomcolor()
            )
            embed.add_field(name=":pushpin: Issue", value="Winter failed to find something relevant", inline=False)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Reddit(client))