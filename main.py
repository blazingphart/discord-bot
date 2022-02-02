from lib2to3.pgen2 import token
import discord
import os
from discord.ext import commands
import pymongo
from dotenv import load_dotenv

from database import MONGO_CLIENT


load_dotenv()
TOKEN = os.getenv("TOKEN")
MONGO_CLIENT = os.getenv("MONGO_CLIENT")

bot = commands.Bot(command_prefix="b!")


@bot.event
async def on_ready():
    print('BlazingFart is ready, version ' + str(discord.__version__))


bot.run(TOKEN, bot=True, reconnect=True)