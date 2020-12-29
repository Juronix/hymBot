import asyncio
from asyncio import sleep

import discord
from discord import Intents
from discord.ext import commands
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

    async def status_task(self):
        while True:
            await bot.change_presence(activity=discord.Game('/help für Hilfe'), status=discord.Status.online)
            await sleep(5)
            await self.change_presence(activity=discord.Game('HymBot ist online'), tatus=discord.Status.online)
            await sleep(5)


bot = HymBot()


@bot.command(name='offline', help='HymBot needs some sleep too...')
async def offline(ctx):
    print('bot goes off')
    await ctx.send('bot goes off')
    await bot.change_presence(activity=discord.Game('HymBot geht offline'), status=discord.Status.offline)
    exit()


# TODO !help
# TODO scribble comms
# TODO role admin
# TODO music bot

'''
@bot.event
async def on_message(message):
    # tach auch!
    if message.author.id == bot.user.id:
        return
    msg = message.content.lower()
    if msg.startswith('tach'):
        await message.channel.send('Tach auch!')

'''
