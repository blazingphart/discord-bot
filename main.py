import discord
import os
from discord.ext import commands


TOKEN = os.environ["TOKEN"]


bot = commands.Bot(command_prefix="b!")


@bot.event
async def on_ready():
    print('BlazingFart is ready, version ' + str(discord.__version__))


bot.run(TOKEN, bot=True, reconnect=True)