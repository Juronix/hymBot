from discord import Forbidden
from discord.ext.commands import Cog


class Welcome(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("welcome")

    @Cog.listener()
    async def on_member_join(self, member):
        await self.stdout.send(
            f"Willkommen auf dem Discord der **{member.guild.name}** {member.mention}! Hier gibt es Rollen: <#792420229242159114>")

    @Cog.listener()
    async def on_member_remove(self, member):
        await self.stdout.send(f"{member.display_name} verlässt den Server {member.guild.name}.")

def setup(bot):
    bot.add_cog(Welcome(bot))
