# <div align='center'>Discord PlugBot</div>

 #### <div align='center'>A Discord bot that you can easily deploy and extend with plugins based on your needs</div>

 ## Table of content
 
 1. [Installation](#install)
 2. [Usage](#usage)
 3. [Add plugins](#add_plugins)
 4. [Development guide](#dev)
 5. [Examples](#examples)

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

1. [Good practices](#dev_gp)
2. [Storing data](#dev_sd)
3. [Handling imports](#dev_imp)
4. [Included utilities](#dev_util)
5. [Publishing the plugin](#dev_pub)

The plugins will be integrated using the official ['load_extension'](https://docs.nextcord.dev/en/stable/ext/commands/extensions.html#primer) function of discord py.

The plugins must be a folder inside the 'plugins' folder and it must contain a file called 'main.py' with a setup function that takes 'bot' as a parameter. Check [this](https://docs.nextcord.dev/en/stable/ext/commands/extensions.html#primer) for official docs.

The bot includes some utilities that can be used by the plugins.

<a id='dev_gp'></a>

### Good practices

1. The scope and functionality of your plugin should be as narrow as possible to be aligned with the plugins-based design of the bot.

2. Use [Cogs](https://docs.nextcord.dev/en/stable/ext/commands/api.html#nextcord.ext.commands.Cog)

3. Save the current directory in the setup function, when commands/tasks/events are called the value of the working directory isn't guaranteed so it is good practice to change the working directory every time a function is called. [EXAMPLE](#wd_ex)

4. If you use the [shared database](#storing_data) make sure to use names tied to the name of your plugin to avoid conflicting names

5. Logging is strongly reccomended using the ['logging'](https://docs.python.org/3/library/logging.html) python package 


<a id='dev_sd'></a>

### Storing data

The bot offers a shared database that can be used by the plugins.

It is located in the data/ folder under the name 'database.db' the database can be accessed using the 'sqlite3' package or by using the prebuilt functions  of 'utils/server_handler.py'.

It's strongly reccomended to create tables with names that are tied to your plugin to avoid conflicting names.

<a id='dev_imp'></a>

### Handling imports

You should instruct your users on how to import the required packages.

<a id='dev_utils'></a>

### Included utilities

The bot offers some utilities that plugins developers can use. Those utilities are located in the 'utils' folder

#### server_handler

Functions:

```python
# Run a query and get the response in a list format
def query(query: str) -> list
```
```python
# Returns 'True' if table exists else 'False'
def table_exists(table_name: str) -> bool
```

<a id='dev_pub'></a>

### Publising the plugin

Hosting your plugin on GitHub is highly reccomended. This allows better discoverability for your plugin and ease of use for the users. If you host your plugin on GitHub make sure to add the **'plugbot-plugin'** tag to the repository.

<a id='examples'></a>
## Examples

<a id='wd_ex'></a>

### Directory Handling

>Example of working directory handling:

```python
import os
import nextcord
from nextcord.ext import commands

localDir: str

@commands.command()
async def example(ctx):
    global localDir
    os.chdir(localDir)

    ...Your code here...

    return

def setup(bot):
    global localDir
    localDir = os.getcwd()
    bot.add_command(example)
```


<a id='cogs_ex'></a>

### Cogs
>Example of a simple plugin that uses Cogs can be found [here](https://github.com/BayoDev/CuteGifs-PlugBot)
