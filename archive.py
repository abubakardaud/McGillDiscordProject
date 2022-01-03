"old slash command they not doing anything anymore"
class VerificationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @cog_ext.cog_slash(name="SetVerifyNSFW", description="set the verify NSFW channel")
    async def _test(self, ctx: SlashContext):
        self.verify_channel = ctx.channel
        await ctx.send("The current channel is the NSFW Verification Channel moving forward.")


    @cog_ext.cog_slash(name="verifyNSFW", description="Join the NSFW 18+ Chats,bot will verify you")
    async def _test(self, ctx: SlashContext):
        await ctx.message.author.send("veirfy channell message ")
        await self.verify_channel.send("woooooooo")