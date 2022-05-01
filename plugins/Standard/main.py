import nextcord
from nextcord.ext import commands
import os
import json
import logging
from utils.config_handler import Config

#https://zira.bot/embedbuilder/

class Standard(commands.Cog):

    _bot: commands.bot
    _info_template: nextcord.Embed
    _LOG_ERROR: bool

    def __init__(self,bot,kwargs) -> None:
        super().__init__()
        self.__init_templates()
        self._LOG_ERROR = kwargs['LOG_ERROR']
        self._bot = bot

    def __init_templates(self) -> bool:
        '''Check and load templates files

        Returns:
            bool: True if everything worked, False if not
        '''
        if not os.path.isfile('Templates/info.json'):
            logging.error("File 'stats.json' not found in the 'Templates' folder",exc_info=self._LOG_ERROR)
            return False
        try:
            with open('Templates/info.json') as file:
                self._info_template = nextcord.Embed.from_dict(json.load(file))
        except:
            logging.error("Unable to open the 'stats.json' template file",exc_info=self._LOG_ERROR)
            return False
        return True

    @nextcord.slash_command(
        name='ping',
        description='Get ping of the bot',
        guild_ids=[882689173247655966,968911738399502389]
    )
    async def ping(self,interaction: nextcord.Interaction): 
        ping = round(self._bot.latency * 1000) 
        await interaction.send(f"Ping is {ping}ms",ephemeral=True)

    @nextcord.slash_command(
        name='info',
        description='Get info about the bot',
        guild_ids=[882689173247655966,968911738399502389]
    )
    async def info(self,inter: nextcord.Interaction):
        await inter.send(embed=self._info_template,ephemeral=True)

def setup(bot: commands.Bot, **kwargs):
    bot.add_cog(Standard(bot,kwargs))