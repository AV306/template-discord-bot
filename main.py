"""Begin imports"""
import discord # Discord library
from discord.ext import *
from discord.ext import commands
from config import Config
import logging # Logging


# Intents (Remember to enable the two sliders in Bot Options!)
intents = discord.Intents.default()
intents.members = True
intents.guilds = True

# Stuff
description = 'noice'
bot = commands.Bot(command_prefix='$', description=description, intents=intents)


# Logger
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='application.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



"""Login event"""
@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game(
            name="$hallo",
            type=0
        ),
    )
    print("We have logged in as {0.user}!".format(bot))


"""Commands"""
# Example command
@bot.command()
async def hallo(ctx):
    await ctx.send('Hallo!')




# Run bot!
bot.run('''Insert your bot token here (In quotes)''')
