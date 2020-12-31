from asyncio import sleep

import discord
from discord import Intents
from discord.ext.commands import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from glob import glob

COGS = [path.split("\\")[-1][:-3] for path in glob("cogs/*.py")]


class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f" {cog} cog ready")

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])


class HymBot(Bot):
    def __init__(self):
        self.ready = False
        self.cogs_ready = Ready()
        self.scheduler = AsyncIOScheduler()

        super().__init__(command_prefix='/')

    def setup(self):
        for cog in COGS:
            self.load_extension(f"cogs.{cog}")

    def run(self):
        self.setup()
        self.TOKEN = open("C:/Users/JoNi/Desktop/Bot/token.txt", "r").readline()
        super().run(self.TOKEN)

    async def on_connect(self):
        print(" bot connected")

    async def on_disconnect(self):
        print("bot disconnected")

    async def on_ready(self):
        if not self.ready:
            self.stdout = self.get_channel(792789962185113650)
            self.loop.create_task(self.status_task())
            while not self.cogs_ready.all_ready():
                await sleep(0.5)

            await self.stdout.send("Now online!")
            self.ready = True
            print(" bot ready")
        else:
            print("bot reconnected")

    async def on_message(self, message):
        if not message.author.bot:
            # tach auch!
            msg = message.content.lower()
            if msg.startswith('tach'):
                await message.channel.send('Tach auch!')
                pass
            await self.process_commands(message)

    async def status_task(self):
        while True:
            await self.change_presence(activity=discord.Game('HymBot ist online'), status=discord.Status.online)
            await sleep(5)
            await bot.change_presence(activity=discord.Game('/help für Hilfe'))
            await sleep(5)
            await bot.change_presence(activity=discord.Game('Neu: Sag "tach" im Chat'))
            await sleep(5)
            await bot.change_presence(activity=discord.Game('Neu: /w2g'))
            await sleep(5)



bot = HymBot()


# TODO !help
# TODO scribble comms
# TODO custum welcome messages
# TODO role admin
# TODO music bot

