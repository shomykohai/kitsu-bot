import logging
from typing import Optional

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

askitsu_cache_expiration: int = 300 #SECONDS


#-------------LOGGING-------------#
logging_level: int = logging.ERROR