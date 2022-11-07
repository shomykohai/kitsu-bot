import asyncio
import config
import discord
from core.bot import KitsuBot

intents = discord.Intents.default()
intents.message_content = True
data = {"status": discord.Status.online, "intents": intents, "case_insensitive": True}

discord.utils.setup_logging(level=config.logging_level, root=False)

async def run_bot():
    bot = KitsuBot(**data)
    await bot.start()


if __name__ == "__main__":
    asyncio.run(run_bot())