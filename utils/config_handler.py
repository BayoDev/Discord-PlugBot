import os
import configparser as cp

class Config:
    _parser: cp.ConfigParser

    def __init__(self,path='./data/config.ini') -> None:
        if not os.path.isfile(path):
            with open(path,'w') as file:
                self.__standard_config().write(file)
                print('Config file created, set your discord bot token to continue')
                exit()
        self._parser = cp.ConfigParser()
        self._parser.read(path)

    def get_config(self):
        return self._parser

    def __standard_config(self):
        config = cp.ConfigParser()
        config['AUTH'] = {
            'BOT_TOKEN' : 'YOUR TOKEN HERE'
        }
        config['OPTIONS'] = {
            'PREFIX' : '-',
            'LOG_ERROR': 'False'
        }
        config['COLORS'] = {
            'error': '#b80000',
            'warning': '#ffeb3',
            'info':'#388e3c'
        }
        config['INFO'] = {
            'bot_name': 'PlugBot',
            'bot_website': 'https://github.com/BayoDev/Discord-PlugBot',
            'bot_icon_url': ''
        }
        return config
