import asyncio
import discord
import os
from discord import Intents
from discord.ext import commands

# get token from file
TOKEN = open("C:/Users/JoNi/Desktop/Bot/token.txt", "r").readline()

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    bot.loop.create_task(status_task())


@bot.event
async def on_connect():
    print("bot connected")


@bot.event
async def on_disconnect():
    print("bot disconnected")


@bot.event
async def on_message(message):
    # tach auch!
    if message.author.id == bot.user.id:
        return
    msg = message.content.lower()
    if msg.startswith('tach'):
        await message.channel.send('Tach auch!')


@bot.command(name='offline', help='HymBot needs some sleep too...')
async def offline(ctx):
    print('bot goes off')
    await ctx.send('bot goes off')
    await bot.change_presence(activity=discord.Game('HymBot ist offline'), status=discord.Status.offline)


# TODO !help
# TODO scribble comms
# TODO role admin
# TODO music bot

async def status_task():
    while True:
        # await bot.change_presence(activity=discord.Game('!help für Hilfe'), status=discord.Status.online)
        # await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game('HymBot ist online'), status=discord.Status.online)
        # await asyncio.sleep(10)


bot.run(TOKEN)
