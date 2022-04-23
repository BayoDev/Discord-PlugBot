import utils.config_handler as ch
import utils.server_handler as sh
import discord
from discord.ext import commands
import logging
import os

def get_plugins() -> list:
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
    intents = discord.Intents.default()
    bot = commands.Bot(command_prefix=conf.get_data('OPTIONS','PREFIX'),intents=intents)

    LOG_ERROR = True if conf.get_data('OPTIONS','LOG_ERROR') == 'True' else False

    #
    # Setup logging
    #

    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    #
    # Import plugins
    #

    for plug in get_plugins():
        try:
            os.chdir(f'./plugins/{plug}')
            bot.load_extension(f'plugins.{plug}.main')
            os.chdir('../..')
        except:
            logging.error(f"Unable to load plugin located in './plugins/{plug}'",exc_info=LOG_ERROR)

    #
    # Run bot
    #
    
    try:
        logging.info('Bot started')
        bot.run(conf.get_data('AUTH','BOT_TOKEN'))
    except:
        logging.error('An error occurred while starting the bot',exc_info=LOG_ERROR)



if __name__ == '__main__':
    main()