import discord
from discord.ext import commands

class Error(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
            title = ":closed_book: Syntax Error",
            color = discord.Color.red()
            )
            embed.add_field(name=":pushpin: Issue", value="A required argument was missing", inline=False)
            embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
            title = ":closed_book: Syntax Error",
            color = discord.Color.red()
            )
            embed.add_field(name=":pushpin: Issue", value="A bad required argument was provided", inline=False)
            embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        if isinstance(error, commands.NotOwner):
            embed = discord.Embed(
            title = ":closed_book: Permssion Error",
            color = discord.Color.red()
            )
            embed.add_field(name=":pushpin: Issue", value="Sorry, you are not the bot owner", inline=False)
            embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
            title = ":closed_book: Syntax Error",
            color = discord.Color.red()
            )
            embed.add_field(name=":pushpin: Issue", value="You are missing required permissions for this command", inline=False)
            embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
    
def setup(client):
    client.add_cog(Error(client))