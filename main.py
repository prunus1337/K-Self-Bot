import discord
from discord.ext import commands
from src.utils import token, prefix, application_id, large_image_id
from colorama import Fore, Style
import os
import traceback

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=prefix, 
            self_bot=True,
            help_command=None
        )

    async def on_guild_join(self, guild):
        print(Fore.GREEN + f"Joined {guild.name}!{Fore.RESET}")
        await guild.fetch_members()
        await guild.fetch_channels()
        await guild.fetch_emojis()
        await guild.fetch_stickers()
        await guild.fetch_roles()
        await guild.fetch_voice_regions()
        await guild.fetch_voice_states()

    async def on_ready(self):
        os.system("cls" if os.name == "nt" else "clear")
        await self.change_presence(
		activity = discord.Activity(
			type=discord.ActivityType.streaming,
			application_id = application_id,
			name = "Created by KapT and Weever",
            details = "K Self-Bot",
			assets = {
			  'large_image' : str(large_image_id),
			  'large_text':f'https://t.me/kapt_self_bot'
			},
			url = "https://twitch.tv/kapt",
			)
		)
        print(Fore.GREEN + f"""
        _____________________________________________________________________________
        |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        |                                                                           |
        |  ██╗░░██╗░░░░░░██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗  |
        |  ██║░██╔╝░░░░░░██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝  |
        |  █████═╝░█████╗██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░  |
        |  ██╔═██╗░╚════╝██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░  |
        |  ██║░╚██╗░░░░░░██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░  |
        |  ╚═╝░░╚═╝░░░░░░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░  |
        |                                                                           |
        |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
        |                       https://t.me/kapt_self_bot                          |
        |                       {Fore.RED}By KaptaBka and Weever{Fore.GREEN}                              | 
        |___________________________________________________________________________|{Fore.RESET}
        """)
        for filename in os.listdir("src/cogs"):
            if filename.endswith(".py"):
                try:
                    self.load_extension(f"src.cogs.{filename[:-3]}")
                except Exception as e:
                    print(f"{Fore.RED}Failed to load {filename[:-3]}\n\n{traceback.print_exception(e)}{Fore.RESET}")
                    continue

Bot().run(token, bot=False)