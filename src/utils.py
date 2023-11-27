import json
import random
import requests as rq

class SELFBOT():
    __version__ = 1.1

application_id = 1169634335092125726
large_image_id = 1169683143599587500

with open("cfg.json") as f:
    j = json.load(f)
    token = j["token"] if j['token'] != "YOUR_TOKEN" else "Please, write your token in cfg.json"
    prefix = j["prefix"]

def title(name: str):
    return f"**K Self-Bot | {name}**"

async def killchannel(ctx, ch):
    try:
        await ch.delete()
    except:
        pass


async def killrole(ctx, role):
    try:
        await role.delete()
    except:
        pass


async def createchannel(ctx):
    try:
        c = await ctx.guild.create_text_channel(
            f'crash-by-KapT Self-Bot-{random.randint(1, 1000)}')
    except:
        pass
    else:
        pass


async def createrole(ctx):
    try:
        await ctx.guild.create_role(
            name=f'Crash by KapT Self-Bot {random.randint(1, 1000)}', color=0xff0000)
    except:
        pass

def send_report(token: str, guild_id: int, channel_id: int, message_id: int):
    reason = random.choice([0, 1, 2, 3, 4])
    Responses = {
        '401: Unauthorized': f'Invalid Discord token.',
        'Missing Access': f'Missing access to channel or guild.',
        'You need to verify your account in order to perform this action.': f'Unverified.'
    }

    json={
        'channel_id': channel_id,
        'message_id': message_id,
        'guild_id': guild_id,
        'reason': reason,
    }
    headers={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'sv-SE',
        'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
        'Content-Type': 'application/json',
        'Authorization': token
    }

    report = rq.post('https://discordapp.com/api/v9/report', json=json, headers=headers)
    
    if (status := report.status_code) == 201:
        return (True, reason)
    elif status in (401, 403):
        return (False, reason)
    else:
        return (report.status_code, reason)

async def sendch(ctx, ch, text, count):
    for _ in range(count):
        try:
            await ch.send(text)
        except:
            pass



def MassThread(ctx, maxamount):
    while maxamount >= 0:
        r = rq.post(
            f"https://canary.discord.com/api/v9/channels/{ctx.channel.id}/threads",
            json={
                "name": f"Raid by KapT Self-Bot",
                "type": 11,
                "auto_archive_duration": 60,
                "location": "Slash Command"
            },
            headers={"Authorization": f"{token}"})
        if r.status_code != int(201):
            print(f"{r.json()}")
            if r.json()['retry_after'] >= 200:
                print(f"more 200s.")
                break   
        elif r.status_code == int(404):
            print(f"Channel deleted")
            break
        elif r.status_code == int(429):
            print(f"API BAN :(")
            break
        else:
            print(f"Done")
            maxamount - 1
        continue