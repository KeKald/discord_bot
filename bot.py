import discord
from discord.ext.commands import Bot
import dotenv
import os

dotenv.load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
BOT_PREFIXES = ("!")
MyBot = Bot(command_prefix = BOT_PREFIXES)

#Simple Hello world text
@MyBot.command(aliases = ["helloworld", "hiworld", "heyworld", "hey", "hi"], pass_context = True)
async def hello_world(context):

    print("\nHello world!")

    channel = context.channel
    await channel.send("Hello world!")

#Deleting messages
@MyBot.command(aliases = ["del", "delete", "clear"], pass_context = True)
async def delete_message(context):

    channel = context.channel
    await channel.delete_messages()


MyBot.run(TOKEN)