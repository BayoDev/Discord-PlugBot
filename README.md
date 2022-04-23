# <div align='center'>Discord PlugBot</div>

 #### <div align='center'>A Discord bot that you can easily deploy and extend with plugins based on your needs</div>

 ## Table of content

 1. [Usage](#usage)
 2. [Development guide](#dev)


 <a id='usage'></a>
 ## Usage

Download the file and run the 'main.py' file while being in the same directory


 <a id='dev'></a>
 ## Development guide

 The plugins will be integrated using the official ['load_extension'](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=load_extension#discord.ext.commands.Bot.load_extension) function of discord py.

 The plugins must be a folder inside the 'plugins' folder and it must contain a file called 'main.py' with a setup function that takes 'bot' as a parameter. Check [this](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=load_extension#discord.ext.commands.Bot.load_extension) for official docs.

 The use of [Cogs](https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#cogs) are strongy recommended

 Other than that you can as many files as you want inside the folder.

 When the setup function is called the working directory is set to the local plugin folder. But when the events or commands are called the working directory will be the one containing the 'main.py' file