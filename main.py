import utils.config_handler as ch
import utils.server_handler as sh
import nextcord
from nextcord.ext import commands
import logging
import os

def get_plugins() -> list:
    '''Get a list of the plugins

    This function should only be used by the main function

    Return:
        list: List of paths of the plugins
    '''
    plugins = []
    for element in os.scandir('./plugins'):
        if element.is_dir() and 'main.py' in os.listdir('./plugins/'+element.name):
            plugins.append(element.name)
    return plugins

def main():
    
    #
    # Folders config
    #

    if not os.path.isdir('data/'):
        os.mkdir('data/')

    if not os.path.isdir('plugins/'):
        os.mkdir('plugins/')

    #
    # Setup server_handler
    #

    os.chdir('utils/')
    sh.setup()
    os.chdir('..')

    #
    # Setup Config
    #

    conf = ch.Config()
    config_data = conf.get_config()
    intents = nextcord.Intents.all()
    bot = commands.Bot(command_prefix=config_data['OPTIONS']['PREFIX'],intents=intents)

    # Preventing plugins from being able to access token directly

    __token = config_data['AUTH']['BOT_TOKEN']
    config_data['AUTH']['BOT_TOKEN'] = 'None'

    LOG_ERROR = bool(config_data['OPTIONS']['LOG_ERROR'])


    # Disable standard help command
    bot.help_command = None

    #
    # Setup logging
    #

    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(pathname)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    #
    # Import plugins
    #

    current_dir = os.getcwd()

    for plug in get_plugins():
        try:
            os.chdir(f'{current_dir}/plugins/{plug}')
            bot.load_extension(f'plugins.{plug}.main',extras=dict(config_data))
            os.chdir(current_dir)
        except:
            logging.error(f"Unable to load plugin located in './plugins/{plug}'",exc_info=LOG_ERROR)

    #
    # Run bot
    #
    
    try:
        logging.info('Bot started')
        bot.run(__token)
    except:
        logging.error('An error occurred while starting the bot',exc_info=LOG_ERROR)



if __name__ == '__main__':
    main()