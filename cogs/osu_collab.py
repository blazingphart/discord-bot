import discord
from discord.ext import commands
from urllib.request import Request, urlopen
from PIL import Image


class osu_collab(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def makecollab(self, ctx, link, row, col):
        filename = str(link.split('/')[-1])
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req)
        image = response.read()

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
                # img_part.save(fp="{}{}.png".format(filename[:-3], col_num+(row_num-1)*col), format="PNG")
                await ctx.send(file=img_part)


def setup(bot):
    bot.add_cog(osu_collab(bot))