import asyncio
import discord
from discord.ext import commands
import requests
from src.utils import *

class GuildCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def servericon(self, ctx):
        await ctx.message.edit(content=f"{ctx.guild.icon_url}")


    @commands.command()
    async def serverbanner(self, ctx):
        await ctx.message.edit(content=f"{ctx.guild.banner_url}")


    @commands.command()
    async def servername(self, ctx):
        await ctx.message.edit(content=ctx.guild.name)


    @commands.command()
    async def serverinfo(self, ctx):
        await ctx.message.edit(content=f"""{title('Server Info')}
            
    **Server Name:**
    `{ctx.guild.name}`
    **Server ID:**
    `{ctx.guild.id}`
    **Server Owner:**
    `{ctx.guild.owner}`
    **Server Roles:**
    `{len(ctx.guild.roles)}`
    **Server Text Channels:**
    `{len(ctx.guild.text_channels)}`
    **Server Voice Channels:**
    `{len(ctx.guild.voice_channels)}`
    **Server Categories:**
    `{len(ctx.guild.categories)}`
    **Boosts:**
    `{ctx.guild.premium_subscription_count}`
    **Members:**
    `{ctx.guild.member_count}`""")


    @commands.command()
    async def serverroles(self, ctx):
        await ctx.message.edit(content=f"""{title('Roles')}\n""" +
                        "\n".join([role.name for role in ctx.guild.roles]))


    @commands.command()
    async def serverchannels(self, ctx):
        await ctx.message.edit(content=f"""{title('Channels')}\n""" +
                        "\n".join([channel.name for channel in ctx.guild.channels]))


    @commands.command()
    async def copy(self, ctx):
        await ctx.message.delete()
        await self.bot.create_guild(f'KSelfbot-Copy-{ctx.guild.name}')
        await asyncio.sleep(4)
        for g in self.bot.guilds:
            if f'KSelfbot-Copy-{ctx.guild.name}' in g.name:
                for c in g.channels:
                    await c.delete()
                for cate in ctx.guild.categories:
                    x = await g.create_category(f"{cate.name}")
                    for chann in cate.channels:
                        if isinstance(chann, discord.VoiceChannel):
                            await x.create_voice_channel(f"{chann}")
                        if isinstance(chann, discord.TextChannel):
                            await x.create_text_channel(f"{chann}")
                for role in ctx.guild.roles:
                    name = role.name
                    color = role.colour
                    perms = role.permissions
                    await g.create_role(name=name, permissions=perms, colour=color)

    @commands.command()
    async def clonechannel(self, ctx):
        await ctx.message.delete()
        new = await ctx.channel.clone()
        await new.edit(position=ctx.channel.position)
        await ctx.channel.delete()

    @commands.command()
    async def leave(self, ctx):
        await ctx.message.edit(content='GG')
        await ctx.guild.leave()


    @commands.command()
    async def leaveallservers(self, ctx):
        await ctx.message.delete()
        try:
            guilds = requests.get(
                'https://canary.discordapp.com/api/v8/users/@me/guilds',
                headers={
                    'authorization': token,
                    'user-agent': 'Mozilla/5.0'
                }).json()
            for guild in range(0, len(guilds)):
                guild_id = guilds[guild]['id']
                requests.delete(
                    f'https://canary.discordapp.com/api/v8/users/@me/guilds/{guild_id}',
                    headers={
                        'authorization': token,
                        'user-agent': 'Mozilla/5.0'
                    })
        except Exception:
            pass


    @commands.command()
    async def deleteallfriends(self, ctx):
        await ctx.message.delete()
        try:
            friends = requests.get(
                'https://canary.discordapp.com/api/v8/users/@me/relationships',
                headers={
                    'authorization': token,
                    'user-agent': 'Mozilla/5.0'
                }).json()
            for friend in range(0, len(friends)):
                friend_id = friends[friend]['id']
                requests.put(
                    f'https://canary.discordapp.com/api/v8/users/@me/relationships/{friend_id}',
                    json={'type': 2},
                    headers={
                        'authorization': token,
                        'user-agent': 'Mozilla/5.0'
                    })
                requests.delete(
                    f'https://canary.discordapp.com/api/v8/channels/{friend_id}',
                    headers={
                        'authorization': token,
                        'user-agent': 'Mozilla/5.0'
                    })
        except Exception:
            pass

def setup(bot):
    bot.add_cog(GuildCog(bot))