from PIL import Image, ImageFilter
import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        try:
            file = ctx.author.avatar_url
            img = Image.open(file)
            img.filter(ImageFilter.GaussianBlur).save("test.png")
            await ctx.send(file=discord.file("test.png"))

        except Exception as e:
            print(e)

def setup(client):
    client.add_cog(Test(client))        