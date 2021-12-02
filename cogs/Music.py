import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def play(self, ctx):
        try:
            file = ""
            location = ""
            voice = discord.utils.get(ctx.guild.voice_channels)
            channel = ctx.author.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(file,executable=location))

        except Exception as e:
            await ctx.send(f"Error: {e}")

    @commands.command()
    async def leave(self, ctx):
        try:
            vc = ctx.voice_client
            await vc.disconnect()
        except Exception as e:
            print(f"Error: {e}")

def setup(client):
    client.add_cog(Music(client))