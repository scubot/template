from discord.ext import commands
from tinydb import TinyDB


class Template(commands.Cog):
    def __init__(self, bot):
        self.version = "1.0.0"
        self.bot = bot
        self.db = TinyDB('./modules/databases/template')


def setup(bot):
    bot.add_cog(Template(bot))
