from discord.ext import commands
from tinydb import TinyDB, Query


class Template(commands.Cog):
    def __init__(self, bot):
        self.version = "1.0.0"
        self.bot = bot
        self.db = TinyDB('./modules/databases/template')

    @commands.group(invoke_without_command=True)
    async def template(self, ctx, name: str):
        target = Query()
        if not self.db.get(target.temp == name):
            await ctx.send("[!] This template does not exist.")
            return
        # TODO: Implement it
        return

    @template.command(name="new")
    async def new(self, ctx, name: str, *, content: str):
        # TODO: Implement it
        pass

    @template.command(name="edit")
    async def edit(self, ctx, name: str, *, content: str):
        # TODO: Implement it
        pass

    @template.command(name="remove")
    async def remove(self, name: str):
        # TODO: Implement it
        pass


def setup(bot):
    bot.add_cog(Template(bot))
