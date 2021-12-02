import discord
from discord.ext import commands

class Server(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        for channel in member.guild.text_channels:
            if channel.name == "join-leave":
                embed = discord.Embed(
                    title = ":inbox_tray: Member Joined",
                    color = discord.Color.green()
                )
                embed.add_field(name=":spy: User", value=member, inline=False)
                embed.add_field(name=":id: ID", value=member.id, inline=False)
                embed.add_field(name=":calendar: Joined at", value=member.joined_at, inline=False)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(icon_url=self.client.user.avatar_url,text=f"{self.client.user.name} | {member.guild.id}")
                await channel.send(embed=embed)

        if member.guild.id == 555787450765541387:
            role = discord.utils.get(member.guild.roles, name="Members")
            await member.add_roles(role)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        for channel in member.guild.text_channels:
            if channel.name == "join-leave":
                embed = discord.Embed(
                    title = ":outbox_tray: Member Left",
                    color = discord.Color.red()
                )
                embed.add_field(name=":spy: User", value=member, inline=False)
                embed.add_field(name=":id: ID", value=member.id, inline=False)
                embed.add_field(name=":calendar: Joined at", value=member.joined_at, inline=False)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(icon_url=self.client.user.avatar_url,text=f"{self.client.user.name} | {member.guild.id}")
                await channel.send(embed=embed)

    @commands.command()
    async def logs(self ,ctx, mode:str=None, is_private:str=None):
        if mode == None:
            embed = discord.Embed(
            title = ":closed_book: Log Error",
            color = discord.Color.red()
            )
            embed.add_field(name=":pushpin: Issue", value="mode [enable/disable] required", inline=False)
            embed.add_field(name=":pushpin: Syntax", value="$logs [enable/disable] p [optional]")
            embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        else:
            if mode == "enable" and is_private == None:
                guild = ctx.guild
                await guild.create_text_channel("join-leave")
                for channel in guild.text_channels:
                    if channel.name == "join-leave":
                        await channel.set_permissions(ctx.guild.default_role, read_messages=True, send_messages=False)
                
                embed = discord.Embed(
                title = ":pencil: Server Logs",
                color = discord.Color.green()
                )
                embed.add_field(name=":wrench: Mode", value="Enabled", inline=False)
                embed.add_field(name=":pushpin: Result", value="Member Join/Leave log are enabled now", inline=False)
                embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
                embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)
            
            if mode == "enable" and is_private == "private":
                guild = ctx.guild
                await guild.create_text_channel("join-leave")
                for channel in guild.text_channels:
                    if channel.name == "join-leave":
                        await channel.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)

                embed = discord.Embed(
                title = ":pencil: Server Logs",
                color = discord.Color.green()
                )
                embed.add_field(name=":wrench: Mode", value="Enabled", inline=False)
                embed.add_field(name=":pushpin: Result", value="Member Join/Leave log are enabled now in private mode", inline=False)
                embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
                embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)

            if mode == "disable":
                guild = ctx.guild
                for channel in guild.text_channels:
                    if channel.name == "join-leave":
                        await channel.delete()

                embed = discord.Embed(
                title = ":pencil: Server Logs",
                color = discord.Color.red()
                )
                embed.add_field(name=":wrench: Mode", value="Disabled", inline=False)
                embed.add_field(name=":pushpin: Result", value="Member Join/Leave log are disabled now", inline=False)
                embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
                embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Server(client))