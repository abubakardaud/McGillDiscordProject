#from gitingore import SECERT
from discord.ext import commands #upm package(discord)
import discord  #upm package(discord.py)
import os
from discord_slash import SlashCommand, SlashContext #upm package(discord_slash)
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='~',intents=intents)
slash = SlashCommand(bot, sync_commands=True)

    
initial_extensions = ['cogs.verifysystem']

@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    print(f'Successfully logged in and booted...!')

if __name__ == "__main__":
    key = os.environ["SecretClientKey"]
    # key = SECERT
    for extension in initial_extensions:
        bot.load_extension(extension)
        # change load_extension to add_cog
    bot.run(key, bot=True, reconnect=True)
