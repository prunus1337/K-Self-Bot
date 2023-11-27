import discord
from discord.ext import commands

class ModCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason):
        await ctx.message.delete()
        await member.ban(reason=reason)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason):
        await ctx.message.delete()
        await member.kick(reason=reason)


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def ar(self, ctx, member: discord.Member, role: discord.Role):
        await ctx.message.delete()
        await member.add_roles(role)


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def tr(self, ctx, member: discord.Member, role: discord.Role):
        await ctx.message.delete()
        await member.remove_roles(role)


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member):
        await ctx.message.delete()
        try:
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            await member.add_roles(role)
        except discord.errors.NotFound:
            await ctx.send("Muted Role Not Found!")


    @commands.command()
    async def purge(self, ctx, amount: int):
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)

def setup(bot):
    bot.add_cog(ModCog(bot))