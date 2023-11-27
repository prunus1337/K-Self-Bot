import discord
from discord.ext import commands

class MathCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, number1, number2):
        x = f"{number1}+{number2}"
        await ctx.message.edit(content = 
                f"""**Question:** {number1} + {number2}\n**Answer:** {eval(x)}""")


    @commands.command()
    async def subtract(self, ctx, number1, number2):
        x = f"{number1} - {number2}"
        await ctx.message.edit(content = 
                f"""**Question:** {number1} - {number2}\n**Answer:** {eval(x)}""")


    @commands.command()
    async def multiply(self, ctx, number1, number2):
        x = f"{number1}*{number2}"
        await ctx.message.edit(content = 
                f"""**Question:** {number1} * {number2}\n**Answer:** {eval(x)}""")


    @commands.command()
    async def divide(self, ctx, number1, number2):
        x = f"{number1} / {number2}"
        await ctx.message.edit(content = 
                f"""**Question:** {number1} / {number2}\n**Answer:** {eval(x)}""")


    @commands.command()
    async def calculator(self, ctx, *, x):
        await ctx.message.edit(content = f"""**Question:** {x}\n**Answer:** {eval(x)}""")

def setup(bot):
    bot.add_cog(MathCog(bot))