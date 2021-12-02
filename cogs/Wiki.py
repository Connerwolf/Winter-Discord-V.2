import discord
from discord.ext import commands
from utility.wiki_api import wiki, wiki_suggest
from utility.colors import randomcolor

class Wiki(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def wiki(self, ctx, *, search):
        data = wiki(search, lenght=4)
        if data != None:
            embed = discord.Embed(
                title = ":newspaper: Wikipedia",
                color = randomcolor()
            )
            embed.set_thumbnail(url="https://wallsheaven.com/photos/A043227933/220/minimal-elegant-monogram-art-logo.-outstanding-professional-trendy-awesome-artistic-w-wv-vw-initial-based-alphabet-icon-logo.-premium-business-logo-white-color-on-black-background.webp")
            embed.add_field(name=f":pushpin: {search}", value=data)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        else:
            data = wiki_suggest(search)
            embed = discord.Embed(
                title = ":newspaper: Wikipedia",
                color = randomcolor()
            )
            embed.set_thumbnail(url="https://wallsheaven.com/photos/A043227933/220/minimal-elegant-monogram-art-logo.-outstanding-professional-trendy-awesome-artistic-w-wv-vw-initial-based-alphabet-icon-logo.-premium-business-logo-white-color-on-black-background.webp")
            embed.add_field(name=f":pushpin: No Match Found", value=f"Try: {data}")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Wiki(client))