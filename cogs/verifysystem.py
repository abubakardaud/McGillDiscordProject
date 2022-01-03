import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext, SlashCommand


bot = commands.Bot(command_prefix='~')
slash = SlashCommand(bot)

accept = "✅"
reject = "❌"

nsfw_role = "NSFW+"

verify_channel_id = 900158437982371880
init_message_id = 927359554348515428 
guild_id = 449822299147862016

class VerificationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        # guild ID check 
        if not payload.guild_id == guild_id :
            return  # Reaction is on a private message
        
        # channel check
        if not payload.channel_id == verify_channel_id:
            return 

        # emoji check 
        if str(payload.emoji) not in [accept, reject]:
            return 


        guild = self.bot.get_guild(payload.guild_id)
        role = discord.utils.get(guild.roles, name=nsfw_role)
        channel = self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        
        if not message.author.id == self.bot.id: 
            return 
              
        if len(message.mentions) == 0:
            return
        member = message.mentions[0]
        if str(payload.emoji) == accept:
          await member.add_roles(role, reason="NSFW Verfied by mod")
          await member.send("You have been verfied for NSFW channels") 
        elif str(payload.emoji) == reject: 
          await member.send("Verification was rejected please try again or DM a moderator.")
          
    #dm handling
    @commands.Cog.listener()
    async def on_message(self, message):
        #testing
        self.verify_channel = self.bot.get_channel(verify_channel_id)
        
        if not(self.verify_channel):
            print("ERROR: No verify channel has been set")

        if not message.guild and not message.author.bot and self.verify_channel:
            if len(message.attachments) > 0:
                message = await self.verify_channel.send(f"Verification for <@{message.author.id}>\n{message.attachments[0].url}")
                await message.add_reaction(accept)
                await message.add_reaction(reject)
            else:
                await message.author.send("To get the NSFW role, please send me an image of an ID as a proof that you are over 18.")
        

# The setup function below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(VerificationCog(bot))


# message that 18-kin will send
# To get access to the NSFW channels, please send me a picture of an ID proving you are over 18 !! A moderator will look at it and approve or reject your submission~~