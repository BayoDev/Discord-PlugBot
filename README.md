# <div align='center'>Discord PlugBot</div>

 #### <div align='center'>A Discord bot that you can easily deploy and extend with plugins based on your needs</div>

 ## Table of content
 
 1. [Installation](#install)
 2. [Usage](#usage)
 3. [Add plugins](#add_plugins)
 4. [Development guide](#dev)

<a id='install'></a>
## Installation

### 1. Clone the directory

```git
git clone https://github.com/BayoDev/Discord-PlugBot.git
```

### 2. Install requirements

```pip
pip install -r requirements.txt
```

### 3. Run it
> Run the bot for the first time to setup all the folders and file

```py
python main.py
```

#### Your bot should be ready to run now!!!

<a id='usage'></a>
## Usage

Run the bot *while being in the same directory*:
```python
python main.py
```

<a id='add_plugins'></a>
## Add plugins

You can find plugins hosted on github <a href='https://github.com/topics/plugbot-plugin'>here</a>

To add the plugin to your bot you just need to download it inside the 'plugins' folder

<a id='dev'></a>
## Development guide

The plugins will be integrated using the official ['load_extension'](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=load_extension#discord.ext.commands.Bot.load_extension) function of discord py.

The plugins must be a folder inside the 'plugins' folder and it must contain a file called 'main.py' with a setup function that takes 'bot' as a parameter. Check [this](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=load_extension#discord.ext.commands.Bot.load_extension) for official docs.

The use of [Cogs](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#cogs) are strongy recommended

Other than that you can as many files as you want inside the folder.

When the setup function is called the working directory is set to the local plugin folder. But when the events or commands are called the working directory will be the one containing the 'main.py' file