import discord
from discord.ext import commands

from src.utils import title

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.message.edit(
                content = f"{title('Help')}\n" \
                          f"*[] Is Required, <> Is Optional*\n" \
                          f"`{ctx.prefix}help`\n" \
                          f"`{ctx.prefix}help math`\n" \
                          f"`{ctx.prefix}help guild`\n" \
                          f"`{ctx.prefix}help mod`\n" \
                          f"`{ctx.prefix}help nuke`\n" \
                          f"`{ctx.prefix}help status`\n" \
                          f"`{ctx.prefix}help utility`\n" \
                          f"`{ctx.prefix}help personal`\n"
            )

    @help.command()
    async def math(self, ctx):
        await ctx.message.edit(
            content = f"{title('Math Commands')}\n" \
                      f"*[] Is Required, <> Is Optional*\n" \
                      f"`{ctx.prefix}add [number] [number]`\n" \
                      f"`{ctx.prefix}subtract [number] [number]`\n" \
                      f"`{ctx.prefix}multiply [number] [number]`\n" \
                      f"`{ctx.prefix}divide [number] [number]`\n" \
                      f"`{ctx.prefix}calculator [number] [number]`\n" \
        )

    @help.command()
    async def guild(self, ctx):
        await ctx.message.edit(
            content = f"{title('Guild Commands')}\n" \
                      f"*[] Is Required, <> Is Optional*\n" \
                      f"`{ctx.prefix}servericon`\n" \
                      f"`{ctx.prefix}serverbanner`\n" \
                      f"`{ctx.prefix}servername`\n" \
                      f"`{ctx.prefix}serverinfo`\n" \
                      f"`{ctx.prefix}serverroles`\n" \
                      f"`{ctx.prefix}serverchannels`\n" \
                      f"`{ctx.prefix}copy`\n" \
                      f"`{ctx.prefix}leave`\n" \
                      f"`{ctx.prefix}invite`\n" \
                      f"`{ctx.prefix}clonechannel`\n"
        )

    @help.command()
    async def misc(self, ctx):
        await ctx.message.edit(
            content = f"{title('Misc Commands')}\n" \
                      f"*[] Is Required, <> Is Optional*\n" \
                      f"`{ctx.prefix}hug [@user] <@user>`\n" \
                      f"`{ctx.prefix}kiss [@user] <@user>`\n" \
                      f"`{ctx.prefix}ascii [text]`\n" \
                      f"`{ctx.prefix}wizz`\n" \
                      f"`{ctx.prefix}dmlist [message]`\n" \
                      f"`{ctx.prefix}dmfriends [message]`\n" \
                      f"`{ctx.prefix}deletedms`\n"
        )

    @help.command()
    async def status(self, ctx):
        await ctx.message.edit(
            content = f"{title('Status Commands')}\n" \
                      f"*[] Is Required, <> Is Optional*\n" \
                      f"`{ctx.prefix}status`\n" \
                      f"`{ctx.prefix}status [game/stream/listen/watch]`\n"
        )
    
    @help.command()
    async def nuke(self, ctx):
        await ctx.message.edit(
            content = f"{title('Nuke Commands')}\n" \
                      f"*[] Is Required, <> Is Optional*\n" \
                      f"`{ctx.prefix}ball`\n" \
                      f"`{ctx.prefix}kall`\n" \
                      f"`{ctx.prefix}dchan`\n" \
                      f"`{ctx.prefix}drole`\n" \
                      f"`{ctx.prefix}dellall`\n" \
                      f"`{ctx.prefix}roles`\n" \
                      f"`{ctx.prefix}spam [count] [text]`\n" \
                      f"`{ctx.prefix}anticrash`\n" \
                      f"`{ctx.prefix}auto`\n" \
                      f"`{ctx.prefix}hookall`\n" \
                      f"`{ctx.prefix}bypass_spam [count] [text]`\n" \
                      f"`{ctx.prefix}spamall [count] [text]`\n" \
                      f"`{ctx.prefix}fastauto`\n" \
                      f"`{ctx.prefix}threadspam [count]`\n" \
                      f"`{ctx.prefix}massreport [user] [count]`\n"
        )

    @help.command()
    async def personal(self, ctx):
        await ctx.message.edit(
            content = f"{title('Personal Commands')}\n" \
                      f"*[] Is Required, <> Is Optional*\n" \
                      f"`{ctx.prefix}prefix`\n" \
                      f"`{ctx.prefix}guilds`\n" \
                      f"`{ctx.prefix}myroles`\n" \
                      f"`{ctx.prefix}nick [nickname]`\n" \
                      f"`{ctx.prefix}nickreset`\n" \
                      f"`{ctx.prefix}friendbackup`\n" \
                      f"`{ctx.prefix}reactionall [count]`\n" \
                      f"`{ctx.prefix}create_guild`\n" \
                      f"`{ctx.prefix}delguild`\n" \
        )

    @help.command()
    async def utility(self, ctx):
        await ctx.message.edit(
            content = f"{title('Utility Commands')}\n" \
                      f"*[] Is Required, <> Is Optional*\n" \
                      f"`{ctx.prefix}ping`\n" \
                      f"`{ctx.prefix}avatar [user]`\n" \
                      f"`{ctx.prefix}info`\n" \
                      f"`{ctx.prefix}tts <lang> <text>`\n" \
                      f"`{ctx.prefix}dumpemojis <server_id>`\n" \
        )

    @help.command()
    async def mod(self, ctx):
        await ctx.message.edit(
            content = f"{title('Moderation Commands')}\n" \
                      f"*[] Is Required, <> Is Optional*\n" \
                      f"`{ctx.prefix}kick [user] [reason]`\n" \
                      f"`{ctx.prefix}ban [user] [reason]`\n" \
                      f"`{ctx.prefix}ar [member] [role]`\n" \
                      f"`{ctx.prefix}tr [member] [role]`\n" \
                      f"`{ctx.prefix}mute [member]`\n" \
                      f"`{ctx.prefix}purge <amount>`\n"
        )

def setup(bot):
    bot.add_cog(HelpCog(bot))