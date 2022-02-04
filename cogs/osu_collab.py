from discord.ext import commands
from urllib.request import Request, urlopen
from PIL import Image
import discord
import datetime
import os

class osu_collab(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def makecollab(self, ctx, link, row, col):
        row = int(row)
        col = int(col)
        filename = str(link.split('/')[-1])
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req)
        image = response.read()

        newpath = "{}{}{}{}{}{}{}_collab".format(filename[:-4], datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year, datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        os.chdir(newpath)

        with open(filename, "wb") as f:
            f.write(image)

        img = Image.open(filename)
        width, height = img.size
        delta_x = int(round(width/col))
        delta_y = int(round(height/row))
        for row_num in range(1, 1+row):
            for col_num in range(1, 1+col):
                left = (col_num-1)*delta_x
                top = (row_num-1)*delta_y
                right =  col_num*delta_x
                bottom = delta_y
                if row_num == row:
                    bottom = height

                img_part = img.crop((left, top, right, bottom))
                img_name = "{}{}.png".format(filename[:-4], col_num+(row_num-1)*col)
                img_part.save(fp=img_name, format="PNG")
                await ctx.send(file=discord.File("{}".format(img_name)))

        os.chdir("../")

        f = open(".gitignore", "a")
        f.write("\n{}/".format(newpath))
        f.close()


def setup(bot):
    bot.add_cog(osu_collab(bot))