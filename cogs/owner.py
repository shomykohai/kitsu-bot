from core.bot import KitsuBot
from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, bot: KitsuBot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def synctree(self, ctx, arg1: str = None) -> None:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild if arg1 else None)

        await ctx.send(
            f'Synced {len(fmt)} commands {"to the current guild." if arg1 else "globally"}'
        )

    @commands.command(aliases=["sd"])
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send("Shutting down...")
        return await self.bot.shutdown()

async def setup(bot: KitsuBot):
    await bot.add_cog(Owner(bot))