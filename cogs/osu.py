import discord
import os
from discord.ext import commands
import pymongo
from dotenv import load_dotenv
import json

class osu(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # async def match(self, ctx, round, mp_link):
    #     os.chdir("../")
    #     os.chdir("tayuno")
    #     pool = {}
    #     with open('pool.json', 'r') as f:
    #         pool = json.load(f)
    #     f.close()
    #     pool = pool[round]



def setup(bot):
    load_dotenv()
    bot.add_cog(osu(bot))