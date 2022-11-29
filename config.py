import logging
from discord import Status

#-------------SECRET-------------#

token: str = "INSERT_TOKEN_HERE"

kitsu_token: str = "" 
"""
INSERT KITSU TOKEN HERE (Optional).
TO KNOW HOW YOU CAN OBTAIN IT, CHECK:
https://askitsu.readthedocs.io/en/master/token.html
""" 

#-------------SETTINGS-------------#
prefix: str = "!"

status = Status.online
"""
Possible options:
- 'online'
- 'offline'
- 'idle'
- 'dnd'
"""

embed_color = 0x1658FF

askitsu_cache_expiration: int = 300 #SECONDS


#-------------LOGGING-------------#
logging_level: int = logging.ERROR