import discord
from colorama import Fore, Style
from discord import app_commands
from discord.ext import commands
from cogs.kitsu.views.buttons import KitsuStreamLinks
from core.bot import KitsuBot
from core.embed import KitsuEmbed
from core.kitsu_client import KitsuClient
from .views.select import AnimeMangaDropdownView


class Kitsu(commands.Cog):
    def __init__(self, bot: KitsuBot):
        self.bot = bot
        self.bot.kitsu = KitsuClient(session=bot.session)

    async def cog_load(self) -> None:
        print(
            f"{Fore.LIGHTYELLOW_EX}[API] {Style.RESET_ALL}Askitsu client initialized."
        )
        return await super().cog_load()

    async def cog_unload(self) -> None:
        return await super().cog_unload()

    @app_commands.command(name="anime", description="Get anime description from Kitsu")
    async def anime(self, interaction: discord.Interaction, name: str):
        result = await self.bot.kitsu.search_anime(name, limit=10)
        if result is None:
            return await interaction.response.send_message(
                "Anime was not found in DB.", ephemeral=True
            )
        select_embed = discord.Embed(
            title="**Select an anime from the list below**",
            timestamp=interaction.created_at,
            colour=0x1658FF,
        )
        view = AnimeMangaDropdownView(result, interaction.user, timeout=15)
        await interaction.response.send_message(embed=select_embed, view=view)
        view.message = await interaction.original_response()
        await view.wait()
        if not view.option:
            return await interaction.edit_original_response(
                content="Oops.. You didn't chose in time, try again"
            )
        result = await self.bot.kitsu.get_anime_entry(view.option)
        categories = [category.title for category in await result.categories]
        embed = KitsuEmbed.kitsu(interaction=interaction, entry=result)
        embed.add_field(
            name=f"📚 **Info**",
            value=f"**→ 🔍 Status:** {result.status.capitalize()}"
            f"\n**→ 🎞️ Episodes:** {result.episode_count}"
            f"\n**→ ⏰ Episode lenght:** {result.episode_length}",
            inline=True,
        )
        embed.add_field(
            name="\u200b",
            value=f"**→ 💭 ID:** `{result.id}`"
            f'\n**→ 🔞 NSFW:** {"Yes" if result.nsfw else "No"}'
            f"\n**→ 📊 Ranking:** {result.rating}/100",
            inline=True,
        )
        if result.yt_id:
            embed.add_field(
                name="<:youtube:992506608829603971> **Trailer**",
                value=f"Watch the trailer on youtube [here]({result.youtube_url})",
                inline=False,
            )
        if categories:
            embed.add_field(
                name="🗃️ **Categories**", value=", ".join(categories), inline=False
            )
        embed.set_image(url=result.cover_image.large)
        await interaction.edit_original_response(
            embed=embed, view=KitsuStreamLinks(await result.stream_links)
        )

    @app_commands.command(name="manga", description="Get manga description from Kitsu")
    async def manga(self, interaction: discord.Interaction, name: str):
        result = await self.bot.kitsu.search_manga(name, limit=10)
        if result is None:
            return await interaction.response.send_message(
                "Manga was not found in DB.", ephemeral=True
            )
        select_embed = discord.Embed(
            title="**Select an manga from the list below**",
            timestamp=interaction.created_at,
            colour=0x1658FF,
        )
        view = AnimeMangaDropdownView(result, interaction.user, timeout=15)
        await interaction.response.send_message(embed=select_embed, view=view)
        view.message = await interaction.original_response()
        await view.wait()
        if not view.option:
            return await interaction.edit_original_response(
                content="Oops.. You didn't chose in time, try again"
            )
        result = await self.bot.kitsu.get_manga_entry(view.option)
        categories = [category.title for category in await result.categories]
        embed = KitsuEmbed.kitsu(interaction=interaction, entry=result)
        embed.add_field(
            name="📚 **Info**",
            value=f"**→ 🔍 Status:** {result.status.capitalize()}"
            f"\n**→ 📒 Volumes:** {result.volume_count}"
            f"\n**→ 📑 Chapters**: {result.chapter_count}",
        )
        embed.add_field(
            name="\u200b",
            value=f"**→ 💭 ID:** `{result.id}`"  # f"\n**→ 📰 Publisher:** {result.serialization}" \
            f"\n**→ 📊 Ranking:** {result.rating}/100",
            inline=True,
        )
        if categories:
            embed.add_field(
                name="🗃️ **Categories**", value=f", ".join(categories), inline=False
            )
        embed.set_image(url=result.cover_image.large)
        await interaction.edit_original_response(embed=embed, view=None)