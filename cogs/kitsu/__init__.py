from .kitsu import Kitsu


async def setup(bot):
    await bot.add_cog(Kitsu(bot))
