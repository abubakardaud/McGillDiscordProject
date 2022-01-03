import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext, SlashCommand
import logging
import tracemalloc





bot = commands.Bot(command_prefix='~')
slash = SlashCommand(bot)

class VerificationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @cog_ext.cog_slash(name="ping")
    async def _test(self, ctx: SlashContext):
        print("working")

        try: 
          await ctx.send("pong")
        except Exception as e:
            print('other error', e)
            queue.task_done()

            





    @commands.command()
    @commands.guild_only()
    async def joined(self, ctx, *, member: discord.Member):
        """New Memeber verification System"""

        await ctx.send(f'{member.display_name} joined on {member.joined_at}')


    # here 
    @cog_ext.cog_slash(name="ping")
    async def _test(self, ctx: SlashContext):
        print("working")

        try: 
          await ctx.send("pong")
        except Exception as e:
            print('other error', e)
            queue.task_done()


    @commands.command(name='creator')
    async def creator(self, ctx):
        """Is the bot cool?"""
        await ctx.send('Made with ❤️ by Abu and Diego~!! ')

    @commands.command(name='opensource')
    async def opensource(self, ctx):
        """text for open source link"""
        await ctx.send('Project is completely **open source**, \n\n check out the ✨github: https://github.com/abubakardaud/McGillDiscordProject')

    


    


    @commands.command(name='top_role', aliases=['toprole'])
    @commands.guild_only()
    async def show_toprole(self, ctx, *, member: discord.Member = None):
        """Simple command which shows the members Top Role."""

        if member is None:
            member = ctx.author

        await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')

    @commands.command(name='perms', aliases=['perms_for', 'permissions'])
    @commands.guild_only()
    async def check_permissions(self, ctx, *, member: discord.Member = None):
        """A simple command which checks a members Guild Permissions.
        If member is not provided, the author will be checked."""

        if not member:
            member = ctx.author

        # Here we check if the value of each permission is True.
        perms = '\n'.join(perm for perm, value in member.guild_permissions if value)

        # And to make it look nice, we wrap it in an Embed.
        embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))

        # \uFEFF is a Zero-Width Space, which basically allows us to have an empty field name.
        embed.add_field(name='\uFEFF', value=perms)

        await ctx.send(content=None, embed=embed)
        # Thanks to Gio for the Command.


# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(VerificationCog(bot))
