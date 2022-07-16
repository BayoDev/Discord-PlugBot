import nextcord
from nextcord.ext import commands
import os
import json
import logging

#https://zira.bot/embedbuilder/

TESTING_GUILDS = []



class Standard(commands.Cog):

    _bot: commands.bot
    _info_template: nextcord.Embed
    _LOG_ERROR: bool
    _commands_list: list[nextcord.BaseApplicationCommand]
    _config: dict

    def __init__(self,bot,kwargs) -> None:
        super().__init__()
        self.__init_templates()
        self._config = kwargs
        self._LOG_ERROR = bool(kwargs['OPTIONS']['LOG_ERROR'])
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

    # Events Listeners

    @commands.Cog.listener()
    async def on_ready(self):
        self._commands_list = self._bot.get_all_application_commands()

    # Commands

    @nextcord.slash_command(
        name='ping',
        description='Get ping of the bot',
        guild_ids=TESTING_GUILDS
    )
    async def ping(self,interaction: nextcord.Interaction): 
        ping = round(self._bot.latency * 1000) 
        await interaction.send(f"Ping is {ping}ms",ephemeral=True)

    @nextcord.slash_command(
        name='info',
        description='Get info about the bot',
        guild_ids=TESTING_GUILDS
    )
    async def info(self,inter: nextcord.Interaction):
        await inter.send(embed=self._info_template,ephemeral=True)

    @nextcord.slash_command(
        name='help',
        description='Get commands of the bot',
        guild_ids=TESTING_GUILDS
    )
    async def help(self,inter: nextcord.Interaction):

        dict_emebed = {
            "color": int(self._config['COLORS']['info'][1:],16),
            "author": {
                "name": self._config['INFO']['bot_name'],
                "url": self._config['INFO']['bot_website'],
                "icon_url": self._config['INFO']['bot_icon_url']
            },
            "title": "Help",
            "description": "List of commands: ",
            "fields": []
        }

        for i in self._commands_list:
            dict_emebed['fields'].append(
                {
                    "name": '/'+i.name,
                    "value": i.description,
                    "inline": False
                }
            )    

        embed = nextcord.Embed.from_dict(dict_emebed)
        
        await inter.send(embed=embed,ephemeral=True)


    @nextcord.slash_command(
        name='clear',
        description='Clear messages of a channel',
        guild_ids=TESTING_GUILDS,
        default_member_permissions=8
    )
    async def clear(self,
        inter: nextcord.Interaction,
        limit: str = nextcord.SlashOption(name='limit',description='The number of messages that will be deleted',required=False,default=None)
    ):
        try:
            await inter.channel.purge(limit=limit)
        except nextcord.Forbidden:
            inter.send("I don't have the required permissions (Manage messages)",ephemeral=True)
        except:
            inter.send("Something went wrong while running the command",ephemeral=True)


    

def setup(bot: commands.Bot, **kwargs):
    bot.add_cog(Standard(bot,kwargs))