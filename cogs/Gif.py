import discord
from discord.ext import commands
from utility.tenor_api import tenor
from utility.colors import randomcolor

class Gif(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gif(self, ctx, *,search):
        data = tenor(search)
        embed = discord.Embed(
            title = f":pencil: {search}",
            description = f"[Open in browser]({data})",
            color = randomcolor(),
        )
        embed.set_image(url=data)
        embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, *,member: discord.Member=None):
        data = tenor("animeslap")
        if member == None:
            embed = discord.Embed(
                title = f":hand_splayed: U got slapped by a stranger lol",
                description = f"[Open in browser]({data})",
                color = randomcolor(),
            )
            embed.set_image(url=data)
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title = f":hand_splayed: You slapped {member}",
                description = f"[Open in browser]({data})",
                color = randomcolor(),
            )
            embed.set_image(url=data)
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Gif(client))