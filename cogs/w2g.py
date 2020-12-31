from discord.ext.commands import Cog
from discord.ext.commands import command
import requests


class W2g(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("w2g")

    @command(name='w2g', help="Erstellt einen Watch2Gether Raum.")
    async def w2g2(self, ctx):
        self.api_key = open("C:/Users/JoNi/Desktop/Bot/w2g_api_key.txt", "r").readline()
        payload = {
            "w2g_api_key": self.api_key,
            "share": "https://www.youtube.com/watch?v=p64W9QQiBr8"
        }
        r = requests.post('https://w2g.tv/rooms/create.json', json=payload)
        streamkey = r.json()['streamkey']
        link = f"https://w2g.tv/rooms/{streamkey}"
        await ctx.send(link)


def setup(bot):
    bot.add_cog(W2g(bot))
