import requests
import json
import discord
from discord.ext import commands
from utility.colors import randomcolor

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def facts(self, ctx):
        data = requests.get(url="https://uselessfacts.jsph.pl/today.json?language=en")
        x = json.loads(data.content)
        y = x["text"]
        data = requests.get(url="https://uselessfacts.jsph.pl/random.json?language=en")
        a = json.loads(data.content)
        b = a["text"]
        embed = discord.Embed(
            title = f":scroll: Facts",
            color = discord.Color.gold()
        )
        embed.add_field(name=":page_facing_up: Daily Fact", value=f"{y}", inline=False)
        embed.add_field(name=":page_facing_up: Random Fact", value=f"{b}", inline=False)
        embed.set_thumbnail(url="https://media0.giphy.com/media/L2ft4vPJ3ZBfgk26Se/giphy.gif")
        embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fun(client))