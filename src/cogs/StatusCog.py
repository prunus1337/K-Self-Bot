import discord
from discord.ext import commands
import urllib
from src.utils import *
import os
from gtts import gTTS

class UtilCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def status(self, ctx):
        # if ctx.invoked_subcommand is None or ctx.invoked_subcommand.name == 'clear':
        #     await ctx.message.delete()
        #     await self.bot.change_presence(status=discord.Status.dnd)
        ...

    @status.command()
    async def game(self, ctx, *, x = "K Self-Bot"):
        await ctx.message.delete()
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.playing, 
                application_id = application_id, 
                name='K Self-Bot', details=f"{x}", 
                assets={
                    'large_image': str(large_image_id), 
                    'large_text': 'https://t.me/kapt_self_bot'
                }
            )
        )

    @status.command()
    async def stream(self, ctx, *, x = "K Self-Bot"):
        await ctx.message.delete()
        await self.bot.change_presence(
            activity = discord.Activity(
                type=discord.ActivityType.streaming,
                application_id = application_id,
                name = "K Self-Bot",
                details = f"{x}",
                assets = {
                'large_image' : str(large_image_id),
                'large_text':f'https://t.me/kapt_self_bot'
                },
                url = "https://twitch.tv/kapt"
                )
            )

    @status.command()
    async def listen(self, ctx):
        await ctx.message.delete()
        await self.bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listen, name='K Self-Bot'))


    @status.command()
    async def watch(self, ctx):
        await ctx.message.delete()
        await self.bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watch, name='K Self-Bot'))


def setup(bot):
    bot.add_cog(UtilCog(bot))