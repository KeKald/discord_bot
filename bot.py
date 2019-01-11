import discord
from discord.ext.commands import Bot
import dotenv
import os
import requests

dotenv.load_dotenv()

TOKEN = os.getenv("DISCORD_AUTH_TOKEN")
BOT_PREFIXES = ("!")
MyBot = Bot(command_prefix = BOT_PREFIXES)

#Startup message
@MyBot.event
async def on_ready():
    print("\nBot active...\n")


# Simple Hello world text
@MyBot.command(aliases = ["helloworld", "hiworld", "heyworld", "hey", "hi"], pass_context = True)
async def hello_world(context):

    print("\nHello world!")

    channel = context.channel
    await channel.send("Hello world!")


#@MyBot.event
#async def on_message(message):
#
#    print(message.content)
#    
#    await MyBot.send_message(message.channel, message.content)

@MyBot.command(aliases=["downloadimage", "dimage", "downimage", "dimg"], pass_context = True)
async def download_image(context):

    test = message.attachments
    print(test)

    channel = context.channel
    await channel.send(test)

MyBot.run(TOKEN)
