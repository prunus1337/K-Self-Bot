import random
import discord
from discord.ext import commands
import urllib
from src.utils import *
import os
from gtts import gTTS
import requests
import asyncio

class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hug(self, ctx, member: discord.User, user: discord.User = None):
        user = ctx.author if not user else user
        hugg = requests.get("https://nekos.life/api/v2/img/hug")
        res = hugg.json()
        await ctx.message.edit(content = f"""{user.mention} Hugs {member.mention}\n\n""" +
                        res["url"])


    @commands.command()
    async def kiss(self, ctx, member: discord.User, user: discord.User = None):
        user = ctx.author if not user else user
        kisss = requests.get("https://nekos.life/api/v2/img/kiss")
        res = kisss.json()
        await ctx.message.edit(content = f"""{user.mention} Kisses {member.mention}\n\n""" +
                        res["url"])

    @commands.command()
    async def ascii(self, ctx, *, message):
        ascii = requests.get(
            f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(message)}"
        ).text
        if len("```" + ascii + "```") > 2000:
            return
        await ctx.message.edit(content = f"```{ascii}```")


    @commands.command()
    async def wizz(self, ctx):
        msg = await ctx.message.edit(content = f"`WIZZING {ctx.guild.name}`")
        await asyncio.sleep(1)
        await msg.edit(
            content=
            f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.text_channels)} Text Channels**"
        )
        await asyncio.sleep(3)
        await msg.edit(
            content=
            f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.voice_channels)} Voice Channels**"
        )
        await asyncio.sleep(2)
        await msg.edit(
            content=
            f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.categories)} Categories**"
        )
        await asyncio.sleep(2)
        await msg.edit(
            content=
            f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.roles)} Roles**"
        )
        await asyncio.sleep(5)
        await msg.edit(
            content=f"`WIZZING {ctx.guild.name}`\n**Spamming Text Channels**")
        await asyncio.sleep(5)
        await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Spamming Webhooks**"
                    )
        await asyncio.sleep(2)
        await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Spamming Roles**")
        await asyncio.sleep(3)
        await msg.edit(
            content=f"`WIZZING {ctx.guild.name}`\n**Spamming Categories**")
        await asyncio.sleep(2)
        await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Sending Pings**")
        await asyncio.sleep(10)
        await msg.edit(
            content=
            f"`WIZZING {ctx.guild.name}`\n**Banning {len(ctx.guild.members)}**")
        await msg.edit(content=f"`WIZZED {ctx.guild.name}`")


    @commands.command()
    async def dmlist(self, ctx, *, x):
        for channel in commands.private_channels:
            try:
                await channel.send(x)
                print(f"DMd {channel}")
            except:
                print(f"Can't DM {channel}")
                continue


    @commands.command()
    async def level(self, ctx):
        responses = [
            'Cry about it', 'We love you KapT', 'Shut the up', 'We love you Weever', 'lol bro what are you doing with this bot?'
        ]
        answer = random.choice(responses)
        await ctx.message.edit(content = answer)
        await asyncio.sleep(5)


    @commands.command()
    async def dmfriends(self, ctx, *, x):
        for friend in commands.user.friends:
            try:
                await friend.send(x)
                print(f"DMd {friend.name}")
            except:
                print(f"Can't DM {friend.name}")
                continue


    @commands.command()
    async def deletedms(self, ctx, name='K Self-Bot'):
        removed=0
        for dm in self.bot.private_channels:
            if name.lower() in str(dm).lower():
                while True:
                    response=requests.delete(f"https://discord.com/api/v9/channels/{dm.id}", headers={'authorization': token})
                    if response!=401: break
                    asyncio.sleep(response.json()['retry_after'])
                removed+=1
        await ctx.message.edit(content = f"{title('Delete dms')}\nSuccessfully removed {removed} dms")



def setup(bot):
    bot.add_cog(MiscCog(bot))