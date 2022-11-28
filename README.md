<h1  align="center">
🦊 Kitsu Bot 🦊
</h1>

[![TwitterShomy](https://img.shields.io/badge/-shomykohai-1DA1F2?style=flat&logo=twitter&logoColor=white&labelColor=1DA1F2)](https://twitter.com/shomykohai)
[![Python](https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10-yellow?style=flat&logo=python&logoColor=white&color=FFD43B&labelColor=306998)](https://www.python.org/downloads/)
[![askitsu](https://img.shields.io/pypi/v/askitsu?label=askitsu&logo=pypi&logoColor=white&labelColor=blue&color=9cf)](https://github.com/ShomyKohai/askitsu)
[![Discord Py](https://img.shields.io/pypi/v/discord.py?label=discord.py&logo=pypi&logoColor=white&labelColor=blue&color=9cf)](https://github.com/Rapptz/discord.py)


##  A discord bot to get information from Kitsu.io 
A discord bot written in Python useful to get directly informations about an anime or a manga inside of discord.

* Customizable prefix (default: `!`)
* Supports token authentication to Kitsu API
* Slash Commands


# ⭐ Prerequisites
- [askitsu](https://github.com/ShomyKohai/askitsu) (the master release)
- [discord.py 2.0+](https://pypi.org/project/discord.py/)
- [aiohttp](https://pypi.org/project/aiohttp/)
- [colorama](https://pypi.org/project/colorama/)


# 🔧 Setup

1. Clone the repository and install the dependencies
    ```shell
    git clone https://github.com/ShomyKohai/kitsu-bot
    cd kitsu-bot
    pip install -r requirements.txt
    ```

2. Create a discord bot on [Discord Developer Portal](https://discord.com/developers/applications) (For more info on [how to create a bot account](https://discordpy.readthedocs.io/en/stable/discord.html))

3. Copy the Bot token and paste it inside `config.py` in the bot folder 
    ```python
    token: str = "INSERT_TOKEN_HERE"
    ```
    **Optional**: [Get a Kitsu token](https://askitsu.readthedocs.io/en/master/token.html)

4. Start the bot with `launcher.py` in bot folder
    ```py
    #Linux/MacOS
    python3 launcher.py


    #Windows
    py launcher.py
    ```

5. Run `!synctree` to sync shash commands
# 💎 Commands

* 🦊 Kitsu
    ```html
    /anime <name>
    /manga <name>
    ```

* ❓ Owner
    ```py
    !synctree #Sync global slash commands
    ```

# License
This project is under the GPL-3.0 license, see [LICENSE.md](LICENSE) file for details

