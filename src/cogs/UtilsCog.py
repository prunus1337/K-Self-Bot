import discord
from discord.ext import commands
import urllib
from src.utils import *
import os
from gtts import gTTS

class UtilCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def avatar(self, ctx: commands.Context, user: discord.User):
        await ctx.message.edit(content=f"{title('Avatar')}\n{user.avatar_url}")

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.message.edit(content=f"{title('Ping')}\n`{round(self.bot.latency * 1000)}ms`")

    @commands.command()
    async def info(self, ctx: commands.Context):
        await ctx.message.edit(content=f"{title('Info')}\nUsername: `{self.bot.user.name}`\nID: `{self.bot.user.id}`\nGuilds: `{len(self.bot.guilds)}`\n[Avatar URL]({self.bot.user.avatar_url})")

    @commands.command()
    async def tts(self, ctx, lang: str = "ru", *, message):
        await ctx.message.delete()
        tts = gTTS(message, lang=lang)
        filename = f'K Self-Bot-{lang}-tts.mp3'
        tts.save(filename)
        await ctx.send(file=discord.File(fp=filename, filename=filename))
        if os.path.exists(filename):
            os.remove(filename)

    @commands.command()
    async def dumpemojis(self, ctx, server_id: int = None):
        await ctx.message.delete()
        try:
            if server_id is None:
                server = ctx.guild
            else:
                server = discord.utils.get(ctx.bot.guilds, id=server_id)
            emojiNum = len(server.emojis)
            folderName = 'Emojis/' + server.name.translate(
                {ord(c): None
                for c in '/<>:"\\|?*'})
            if emojiNum > 0:
                if not os.path.exists(folderName):
                    os.makedirs(folderName)
            for emoji in server.emojis:
                if emoji.animated:
                    fileName = folderName + '/' + emoji.name + '.gif'
                else:
                    fileName = folderName + '/' + emoji.name + '.png'
                if not os.path.exists(fileName):
                    with open(fileName, 'wb') as outFile:
                        req = urllib.request.Request(
                            emoji.url, headers={'user-agent': 'Mozilla/5.0'})
                        data = urllib.request.urlopen(req).read()
                        outFile.write(data)
        except:
            pass

def setup(bot):
    bot.add_cog(UtilCog(bot))