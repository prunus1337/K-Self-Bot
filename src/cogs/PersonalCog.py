import discord
from discord.ext import commands
import urllib

import requests
from src.utils import *
import os
from gtts import gTTS

class PersonalCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def guilds(self, ctx):
        await ctx.message.edit(content = f"{title('Guilds')}\n{len(self.bot.guilds)} \nGuild:\n" + "\n".join([guild.name for guild in self.bot.guilds]))

    @commands.command()
    async def prefix(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"""**__PREFIX__**\n`""" + j["prefix"] + "`")


    @commands.command()
    async def myroles(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"""**Roles:**\n`{len(ctx.author.roles)}`
    **Role Names:**\n""" + "\n".join([role.name for role in ctx.guild.roles]))


    @commands.command()
    async def nick(self, ctx, *, x):
        await ctx.message.delete()
        await ctx.author.edit(nick=x)

    @commands.command()
    async def nickreset(self, ctx):
        await ctx.message.delete()
        await ctx.author.edit(nick=ctx.author.name)


    @commands.command(aliases=['friendexport'])
    async def friendbackup(self, ctx):
        friends = requests.get(
            'https://discordapp.com/api/v8/users/@me/relationships',
            headers={
                'authorization': token,
                'user-agent': 'Mozilla/5.0'
            }).json()
        await ctx.message.delete()
        for friend in range(0, len(friends)):
            friend_id = friends[friend]['id']
            friend_name = friends[friend]['user']['username']
            friend_discriminator = friends[friend]['user']['discriminator']
            friendinfo = f'{friend_name}#{friend_discriminator} ({friend_id})'
            with open('Friends.txt', 'a+') as f:
                f.write(friendinfo + "\n")

    @commands.command()
    async def invite(self, ctx, *, link):
        if "discord.gg/" in link:
            link2 = (link.split("https://discord.gg/")[1])[:10]
            response = requests.get(
                f'https://discord.com/api/v6/invite/{link2}').json()
            if 'Unknown Invite' in response:
                await ctx.message.edit(
                    content="**Wrong invitation link!**",
                    delete_after=3)
            else:
                try:
                    embed = f"**Server Name: `{response['guild']['name']}`\nServer id: `{response['guild']['id']}`\nInvitation Maker Name: `{response['inviter']['username']}`\nInvitation Creator Tag: `{response['inviter']['discriminator']}`\nid of the creator of the invitation: `{response['inviter']['id']}`\nChannel Name: `{response['channel']['name']}`\nChannel id: `{response['channel']['id']}`**"
                except:
                    await ctx.message.edit(
                        content="**Wrong invitation link!**",
                        delete_after=3)
                    return

                await ctx.message.edit(content=embed)
        else:
            await ctx.message.edit(
                content=
                "**Please provide the invitation link in the format\n```<https://discord.gg/link>```**",
                delete_after=5)

    @commands.command()
    async def delguild(self, ctx):
        try:
            await ctx.guild.delete()
        except Exception as e:
            await ctx.send(f'An error occurred while deleting the server | `{e}`')

    @commands.command()
    async def create_guild(self, ctx, *, nameg='Guild by K-SelfBot'):
        new = await self.bot.create_guild(name=nameg)
        listc = await new.fetch_channels()
        for c in listc:
            await c.delete()
        await new.create_text_channel('made-by-kapt-selfbot'),
        await ctx.send(f'Server has been created {nameg}')

    @commands.command()
    async def reactionall(self, ctx, amount: int):
        await ctx.message.delete()
        messages = await ctx.channel.history(limit=amount).flatten()
        reactioned=0
        for message in messages:
            await message.add_reaction("🐱")
            await message.add_reaction("✅")
            reactioned+=1
        await ctx.send(f"**:white_check_mark: Successfully set reactions to {reactioned} messages!**")

def setup(bot):
    bot.add_cog(PersonalCog(bot))