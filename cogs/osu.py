import discord
import os
from discord.ext import commands
import pymongo
from dotenv import load_dotenv

class osu(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # @commands.has_role("tayuno's")
    # async def stats(self, ctx, round, )

def setup(bot):
    load_dotenv()
    bot.add_cog(osu(bot))