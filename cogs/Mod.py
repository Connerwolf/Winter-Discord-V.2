import asyncio
import discord
from discord import embeds
from discord import guild
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["k"])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member=None, *, reason=None):
        if not member:
            embed = discord.Embed(
                title = ':closed_book: Kick Error',
                color = discord.Color.green()
            )
            embed.add_field(name=":pushpin: Issue", value="A member was not defined")
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f"{ctx.author.name} | Winter Error Handler")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
            title = f':boot: Kicked',
            color = discord.Color.green()
            )
            embed.add_field(name=":spy: User", value=member, inline=False)
            embed.add_field(name=":id: ID", value=member.id, inline=False)
            embed.add_field(name=":bookmark_tabs: Reason", value=reason, inline=False) 
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Performed by {ctx.author.name}")
            await member.kick(reason=reason)
            await ctx.send(embed=embed)

    @commands.command(aliases=["b"])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member=None, *, reason=None):
        if not member:
            embed = discord.Embed(
                title = ':closed_book: Ban Error',
                color = discord.Color.green()
            )
            embed.add_field(name=":pushpin: Issue", value="A member was not defined")
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f"{ctx.author.name} | Winter Error Handler")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
            title = f':tools: Banned',
            color = discord.Color.green()
            )
            embed.add_field(name=":spy: User", value=member, inline=False)
            embed.add_field(name=":id: ID", value=member.id, inline=False)
            embed.add_field(name=":bookmark_tabs: Reason", value=reason, inline=False) 
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Performed by {ctx.author.name}")
            await member.ban(reason=reason)
            await ctx.send(embed=embed)

    @commands.command(aliases=["ub"])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id:int=None, *, reason=None):
        if not id:
            embed = discord.Embed(
                title = ':closed_book: Unban Error',
                color = discord.Color.green()
            )
            embed.add_field(name=":pushpin: Issue", value="User ID required to unban")
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f"{ctx.author.name} | Winter Error Handler")
            await ctx.send(embed=embed)
        else:
            member = await self.client.fetch_user(id)
            embed = discord.Embed(
            title = f':tools: Unbanned',
            color = discord.Color.green()
            )
            embed.add_field(name=":spy: User", value=member, inline=False)
            embed.add_field(name=":id: ID", value=member.id, inline=False)
            embed.add_field(name=":bookmark_tabs: Reason", value=reason, inline=False) 
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Performed by {ctx.author.name}")
            await ctx.guild.unban(member,reason=reason)
            await ctx.send(embed=embed)

    @commands.command(aliases=['m'])
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member=None, mute_minutes:int=0, *,reason=None):
        if not member:
            embed = discord.Embed(
            title = ":closed_book: Mute Error",
            color = discord.Color.red()
            )
            embed.add_field(name=":pushpin: Issue", value="A member was not defined", inline=False)
            embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        else:
            role = discord.utils.get(ctx.guild.roles, name='Muted')
            guild = ctx.guild
            if role not in guild.roles:
                await guild.create_role(name="Muted")
                for channel in guild.text_channels:
                    await channel.set_permissions(role, send_messages=False)

            else:
                embed = discord.Embed(
                    title = ":mute: Muted",
                    color = discord.Color.green()
                )
                embed.add_field(name=":spy: User", value=member, inline=False)
                embed.add_field(name=":id: ID", value=member.id, inline=False)
                embed.add_field(name=":alarm_clock: Time",value=f"{mute_minutes} mins",inline=False)
                embed.add_field(name=":bookmark_tabs: Reason", value=reason, inline=False) 
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Performed by {ctx.author.name}")
                await member.add_roles(role,reason=reason)
                await ctx.send(embed=embed)

                if mute_minutes > 0:
                    new_time = mute_minutes * 60
                    await asyncio.sleep(new_time)
                    embed = discord.Embed(
                    title = ":speaker: Unmuted",
                    color = discord.Color.green()
                    )
                    embed.add_field(name=":spy: User", value=member, inline=False)
                    embed.add_field(name=":id: ID", value=member.id, inline=False)
                    embed.add_field(name=":alarm_clock: Time",value=f"{mute_minutes} mins",inline=False)
                    embed.add_field(name=":bookmark_tabs: Reason", value="Auto Unmute", inline=False) 
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.set_footer(icon_url=self.client.user.avatar_url,text=f"Performed by {self.client.user.name}")
                    await ctx.send(embed=embed)
                    await member.remove_roles(role,reason='Auto Unmute')

    @commands.command(aliases=['um'])
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member=None, *,reason=None):
        if not member:
            embed = discord.Embed(
            title = "Mute Error",
            color = discord.Color.red()
            )
            embed.add_field(name="Issue", value="A member was not defined", inline=False)
            embed.set_thumbnail(url="https://miro.medium.com/max/1600/1*e_Loq49BI4WmN7o9ItTADg.gif")
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        else:
            role = discord.utils.get(ctx.guild.roles, name='Muted')
            embed = discord.Embed(
            title = ":speaker: Unmuted",
            color = discord.Color.green()
            )
            embed.add_field(name=":spy: User", value=member, inline=False)
            embed.add_field(name=":id: ID", value=member.id, inline=False)
            embed.add_field(name=":bookmark_tabs: Reason", value=reason, inline=False) 
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Performed by {ctx.author.name}")
            await ctx.send(embed=embed)
            await member.remove_roles(role,reason='Auto Unmute')

    @commands.command(aliases=['c', 'purge'])
    async def clear(self, ctx, limit=5):
        embed = discord.Embed(
        title = ":broom: Cleared",
        color = discord.Color.green()
        )
        embed.add_field(name=":round_pushpin: Amount", value=limit, inline=False) 
        embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Performed by {ctx.author.name}")
        await ctx.channel.purge(limit=limit)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Moderation(client))