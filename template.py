from discord.ext import commands
from tinydb import TinyDB, Query


class Template(commands.Cog):
    protected_names = ['new', 'edit', 'remove']
    target = Query()

    def __init__(self, bot):
        self.version = "1.0.0"
        self.bot = bot
        self.db = TinyDB('./modules/databases/template')

    async def is_author(self, name, userid):
        return self.db.get(self.target.tag == name)['userid'] == userid

    @commands.group(invoke_without_command=True)
    async def template(self, ctx, name: str):
        if not self.db.get(self.target.name == name):
            await ctx.send("[!] This template does not exist.")
            return
        # TODO: Implement it
        return

    @template.command(name="new")
    async def new(self, ctx, name: str, *, content: str):
        if name in self.protected_names:
            await ctx.send("[!] The tag you are trying to create is a protected name.")
            return
        if not content:
            await ctx.send("[!] No content specified?")
            return
        if self.db.get(self.target.tag == name) is not None:
            await ctx.send("[!] This tag already exists.")
            return
        self.db.insert({'userid': ctx.author.id, 'templatename': name, 'content': content})
        await ctx.send("[:ok_hand:] Template added.")
        return

    @template.command(name="edit")
    async def edit(self, ctx, name: str, *, content: str):
        if not await self.is_author(name, ctx.author.id):
            await ctx.send("[!] You do not have permission to edit this.")
            return
        if self.db.get(self.target.templatename == name) is None:
            await ctx.send("[!] The tag doesn't exist.")
            return
        self.db.update({'content': content}, self.target.templatename == name)
        await ctx.send("[:ok_hand:] Tag updated.")
        return

    @template.command(name="remove")
    async def remove(self, ctx, name: str):
        if not await self.is_author(name, ctx.author.id):
            await ctx.send("[!] You do not have permission to edit this.")
            return
        if self.db.get(self.target.templatename == name) is None:
            await ctx.send("[!] The tag doesn't exist.")
            return
        self.db.remove(self.target.templatename == name)
        await ctx.send("[:ok_hand:] Tag removed.")
        return


def setup(bot):
    bot.add_cog(Template(bot))
