#from gitingore import SECERT
from discord.ext import commands
import discord
bot = commands.Bot(command_prefix='~')

initial_extensions = ['cogs.verifysystem',
                      ]


@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    print(f'Successfully logged in and booted...!')


if __name__ == "__main__":
    key = os.environ["SecertClientKey"]
    # key = SECERT
    for extension in initial_extensions:
        bot.load_extension(extension)

    bot.run(key, bot=True, reconnect=True)
