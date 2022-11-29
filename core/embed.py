from typing import Union
import askitsu
import config
import discord


class KitsuEmbed(discord.Embed):
    def __init__(
        self, color=0xE91E63, timestamp=None, fields=(), fd_inline=False, **kwargs
    ):
        super().__init__(color=color, timestamp=timestamp, **kwargs)
        for n, v in fields:
            self.add_field(name=n, value=v, inline=fd_inline)

    @classmethod
    def kitsu(
        cls,
        interaction: discord.Interaction,
        entry: Union[askitsu.Anime, askitsu.Manga],
        **kwargs,
    ):
        isinstance = cls(
            title=entry.title.en,
            url=entry.url,
            timestamp=interaction.created_at,
            color=config.embed_color,
            **kwargs,
        )
        desc = entry.description
        if len(desc) > 1024:
            desc = desc[:1024] + f"...\n[Read more on kitsu]({entry.url})"
        isinstance.description = desc
        isinstance.set_author(
            name="Kitsu",
            icon_url="https://cdn.discordapp.com/emojis/985198297427902484.webp",
        )
        isinstance.set_thumbnail(url=entry.poster_image.original)
        isinstance.set_footer(
            text=f"Requested by {interaction.user.name} • Fetched from Kitsu.io",
            icon_url=interaction.user.display_avatar.url,
        )
        return isinstance