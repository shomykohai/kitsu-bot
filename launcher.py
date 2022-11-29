import asyncio
import config
import discord
from core.bot import KitsuBot

intents = discord.Intents.default()
intents.message_content = True
data = {"status": config.status, "intents": intents, "case_insensitive": True}

discord.utils.setup_logging(level=config.logging_level, root=False)

async def run_bot():
    if not config.status in discord.Status:
        data["status"] = discord.Status.online
    bot = KitsuBot(**data)
    await bot.start()


if __name__ == "__main__":
    asyncio.run(run_bot())