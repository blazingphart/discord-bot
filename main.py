import discord
import os
from discord.ext import commands
import pymongo
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TOKEN")
MONGO_CLIENT = os.getenv("MONGO_CLIENT")

bot = commands.Bot(command_prefix="b!")


@bot.command()
async def load(ctx, extension):
    bot.load_extension('cogs.{}'.format(extension))
    await ctx.send('Loaded extension "{}"'.format(extension))

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension('cogs.{}'.format(extension))
    await ctx.send('Unloaded extension "{}"'.format(extension))

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension('cogs.{}'.format(extension))
    bot.load_extension('cogs.{}'.format(extension))
    await ctx.send('Reloaded extension "{}"'.format(extension))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension('cogs.{}'.format(filename[:-3]))


bot.run(TOKEN, bot=True, reconnect=True)