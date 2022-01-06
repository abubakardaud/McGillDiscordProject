#from gitingore import SECERT
import setuptools

from discord.ext import commands #upm package(discord)
import discord  #upm package(discord.py)
import os
from discord_slash import SlashCommand, SlashContext #upm package(discord_slash)
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='~~!~~!~~',intents=intents)
slash = SlashCommand(bot, sync_commands=True)

    
initial_extensions = ['cogs.verifysystem']

rules_channel_id = 763227838462820484

@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    print(f'Successfully logged in and booted...!')

    channel = bot.get_channel(763227838462820484)
    # await channel.send("You must be 18+ to participate in the NSFW channels. If you wish to participate, please DM  <@900107528107597834> *with an image containing your ID (McGill ID, etc). You can cover up your name to make it more anonymous*. No ID image will be kept, sent images will be deleted as soon as the verification process is done. You can also DM any of our mods if you feel more comfortable. Abusing the verification system will result in a warning or ban.")

if __name__ == "__main__":
    key = os.environ["SecretClientKey"]
    # key = SECERT
    for extension in initial_extensions:
        bot.load_extension(extension)
        # change load_extension to add_cog
    bot.run(key, bot=True, reconnect=True)
