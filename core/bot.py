import aiohttp
import config
import logging
from discord.ext import commands #type: ignore
from .kitsu_client import KitsuClient


class KitsuBot(commands.Bot):
    def __init__(self, **data) -> None:
        self.logger = logging.getLogger("discord")
        self.kitsu: KitsuClient = None 
        self.prefix = config.prefix
        self.token = config.token
        super().__init__(command_prefix=self.prefix, **data)

    async def on_ready(self):
        print(
            "#################################################################\n"
            f"Ready. Logged in as {self.user} ({self.user.id})\n"
            "#################################################################"
        )
        print(f"Made by ShomyKohai (https://github.com/ShomyKohai)")
        await self.load_extension("cogs.kitsu")
        await self.load_extension("cogs.owner")

    async def start(self) -> None:
        self.session = aiohttp.ClientSession()
        self.kitsu = KitsuClient(
            session=self.session
        )
        await super().start(self.token, reconnect=True)

    async def shutdown(self) -> None:
        await self.session.close()
        await self.close()