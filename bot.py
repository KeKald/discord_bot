import discord
from discord.ext.commands import Bot
import dotenv
import os

dotenv.load_dotenv()

TOKEN = os.getenv("DISCORD_AUTH_TOKEN")
BOT_PREFIXES = ("!")
MyBot = Bot(command_prefix = BOT_PREFIXES)

# Startup message
@MyBot.event
async def on_ready():
    print("\nBot active...\n")


# Simple Hello world text
@MyBot.command(aliases = ["helloworld", "hiworld", "heyworld", "hey", "hi"], pass_context = True)
async def hello_world(context):

    print("\nHello world!")

    channel = context.channel
    await channel.send("Hello world!")

#
@MyBot.event
async def message():

    print(message(content))

MyBot.run(TOKEN)
