import nextcord
from nextcord.ext import commands
import utils.server_handler as server
import logging
import os

TESTING_GUILDS = []

class PluginClass(commands.Cog):

    _LOG_ERROR: bool
    _config: dict
    _bot: commands.Bot
    _path: str

    def __init__(self,bot,config) -> None:
        self._bot = bot
        self._LOG_ERROR = bool(config['OPTIONS']['LOG_ERROR'])
        self._config = config
        self._path = os.getcwd()
            

def setup(bot, **kwargs):
    bot.add_cog(PluginClass(bot,kwargs))