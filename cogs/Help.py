from enum import Flag
import json
from os import name
import discord
from discord.ext import commands
from winter import ping

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, category=None):
        if category == None:
            embed = discord.Embed(
                title = ":file_folder: Help Commands",
                color = discord.Color.green()
            )
            embed.add_field(name=":desktop: $help media",value="This command provides all the media related commands",inline=False)
            embed.add_field(name=":tada: $help fun",value="This command provides all the fun related commands",inline=False)
            embed.add_field(name=":tools: $help moderation",value="This command provides all the moderation related commands",inline=False)
            embed.add_field(name=":wrench: $help utility",value="This command provides all the utility related commands",inline=False)
            embed.add_field(name=":postal_horn: $invite",value="[Click Here](https://discord.com/oauth2/authorize?client_id=586553956843388942&scope=bot&permissions=8)",inline=True)
            embed.add_field(name=":shield: $support",value="[Click Here](https://discord.gg/zAhDxAVTXu)",inline=True)
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        elif category == "media":
            embed = discord.Embed(
                title = ":desktop: Media Commands",
                color = discord.Color.green()
            )
            embed.add_field(name="$cat",value="This command provides a cat image.",inline=False)
            embed.add_field(name="$dog",value="This command provides a dog image.",inline=False)
            embed.add_field(name="$gif <search_term>",value="This command provides a gif.",inline=False)
            embed.add_field(name="$reddit <search_term>",value="This command provides a search result from reddit.",inline=False)
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        elif category == "fun":
            embed = discord.Embed(
                title = ":tada: Fun Commands",
                color = discord.Color.green()
            )
            embed.add_field(name="$slap <user=optional>",value="This command helps u slaps some peeps.",inline=False)
            embed.add_field(name="$facts",value="This command gets u some kind of facts.",inline=False)
            embed.add_field(name="$wiki <search_term>",value="This command finds u stuff from wikipedia.",inline=False)
            embed.add_field(name="$meme", value="This commands sends you a Meme .... maybe", inline=False)
            embed.add_field(name="$automeme <on/off>",value="This commands sends a meme every 5 mins.",inline=False)
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
        
        elif category == "moderation":
            embed = discord.Embed(
                title = ":tools: Moderation Commands",
                color = discord.Color.green()
            )
            embed.add_field(name="$kick <user> <reason=optional>",value="This command kicks the mentioned user",inline=False)
            embed.add_field(name="$ban <user> <reason=optional>",value="This command bans the mentioned user",inline=False)
            embed.add_field(name="$unban <user_id> <reason=optional>",value="This command unbans the mentioned user",inline=False)
            embed.add_field(name="$mute <search_term> <reason=optional>",value="This command mutes the mentioned user",inline=False)
            embed.add_field(name="$unmute <search_term> <reason=optional>",value="This command unmutes the mentioned user",inline=False)
            embed.add_field(name="$clear <limit=5 by default>",value="This command clears a limited number of messages from the channel",inline=False)
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        elif category == "utility":
            embed = discord.Embed(
                title = ":wrench: Utility Commands",
                color = discord.Color.green()
            )
            embed.add_field(name="$winter",value="This command provides bot data",inline=False)
            embed.add_field(name="$logs <enable/disable> <private=optional>",value="This command provides user join/leave logs in a bot created custom channel",inline=False)
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

    @commands.command()
    async def winter(self, ctx):
        with open("setup/bot_config.json") as file:
            config = json.load(file)

        me = await self.client.fetch_user(450223497021489163)
        embed = discord.Embed(
            title = ":wolf: Winter Data",
            color = discord.Color.magenta()
        )
        embed.add_field(name=":satellite_orbital: Ping",value=f"{ping()}",inline=False),
        embed.add_field(name=":notepad_spiral: Version",value=f"{config['version']}",inline=False),
        embed.add_field(name=":floppy_disk: Prefix",value=f"{config['prefix']}",inline=False),
        embed.add_field(name=":keyboard: Developer",value=f"{me.name}",inline=False)
        embed.add_field(name=":tada: Latest Update", value="1.Added Automeme \n2.Fixed some stuff \n3. Better Bot Maintainance",inline=False)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))