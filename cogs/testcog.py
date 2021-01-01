from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Game
from discord import Status


class Testcog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("testcog")


    @command(name="testcom", aliases=["t", "tc"], hidden=True, help="test")
    async def testcom(self, ctx):
        await ctx.send(f"hi {ctx.author.mention}!")


    @command(name='offline', hidden=True)
    async def offline(self, ctx):
        print('bot goes off')
        await ctx.send('bot goes off')
        await self.bot.change_presence(activity=Game('HymBot geht offline'), status=Status.dnd)
        exit()


def setup(bot):
    bot.add_cog(Testcog(bot))

