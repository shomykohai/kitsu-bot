import askitsu
import discord
from typing import List, Any


class KitsuStreamLinks(discord.ui.View):
    def __init__(self, stream_links: List[askitsu.StreamLink], *args, **kwargs):
        super().__init__(*args, **kwargs)
        if stream_links is not None:
            for stream in stream_links:
                self.add_item(
                    discord.ui.Button(
                        label=stream.name,
                        style=discord.ButtonStyle.link,
                        url=stream.url,
                    )
                )

    async def on_error(
        self,
        interaction: discord.Interaction,
        error: Exception,
        item: discord.ui.Item[Any],
    ) -> None:
        return await super().on_error(interaction, error, item)
