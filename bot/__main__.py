"""
Launches the bot, starts the asyncio loop when called.
"""
from bot.meme_api import memegen
from . import settings
from .bot import Bot

if __name__ == "__main__":
    bot = Bot(command_prefix=settings.COMMAND_PREFIX)

    # load in basic commands
    bot.load_extension("bot.cogs.greetings")
    bot.load_extension("bot.cogs.utilities")
    bot.load_extension("bot.cogs.source")

    # load in image segmentation commands
    bot.load_extension("bot.cogs.image_segmentation")

    # load in Meme commands
    bot.load_extension("bot.cogs.memes")

    # load in Admin commands
    bot.load_extension("bot.cogs.admin")
    
    #load in Trivia commands
    bot.load_extension("bot.cogs.trivia")
    
    #load in weather command
    bot.load_extension("bot.cogs.weather")

    # load in Fun commands
    bot.load_extension("bot.cogs.fun")

    bot.run(settings.TOKEN)
    
 
    
