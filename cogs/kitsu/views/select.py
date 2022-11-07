from typing import Union, List
import discord
import askitsu


class AnimeMangaDropdown(discord.ui.Select):
    def __init__(self, result: Union[List[askitsu.Anime], dict]):
        options = [
            discord.SelectOption(
                label=f"{res.canonical_title} → {res.subtype.capitalize()}",
                value=res.id,
            )
            for res in result
        ]
        super().__init__(
            custom_id="Anime-Manga-Dropdown",
            placeholder="Choose an option",
            min_values=1,
            max_values=1,
            options=options,
        )
        self.option = None

    async def callback(self, interaction: discord.Interaction):
        self.option = self.values[0]
        await interaction.response.defer()


class AnimeMangaDropdownView(discord.ui.View):
    def __init__(
        self,
        result: Union[List[askitsu.Anime], dict],
        author: discord.User = None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        dropdown = AnimeMangaDropdown(result)
        self.option: str = dropdown.option
        self.add_item(dropdown)
        self.author: discord.User = author
        self.message: discord.InteractionMessage = None

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if self.author.id == interaction.user.id:
            children = self.children[0]
            self.option = children.values[0]
            children.disabled = True
            await self.message.edit(view=self)
            self.stop()
            return True
        return False

    async def on_timeout(self) -> None:
        self.children[0].disabled = True
        await self.message.edit(view=self)
        self.stop()
