import discord
import dotenv
import os
import requests
import shutil
from discord.ext.commands import Bot

dotenv.load_dotenv()

TOKEN = os.getenv("DISCORD_AUTH_TOKEN")
BOT_PREFIXES = ("!")
MyBot = Bot(command_prefix=BOT_PREFIXES)

# Startup message
@MyBot.event
async def on_ready():
    print("\nBot active...\n")


# Simple Hello world text
@MyBot.command(aliases=["helloworld", "hiworld", "heyworld", "hey", "hi"], pass_context=True)
async def hello_world(context):

    print("\nHello world!")

    channel = context.channel
    await channel.send("Hello world!")

# Event which prints out every message sent in channel
# @MyBot.event
# async def on_message(message):
#
#    print(message.content)
#
#    await MyBot.send_message(message.channel, message.content)


# Command which downloads image with provided URL and saves it with requested filename
@MyBot.command(aliases=["downloadimage", "dimage", "dim", "dimg"], pass_context=True)
async def download_image(context, URL, output_file_char):

    output_file_format = ".png"
    output_file_name = output_file_char + output_file_format

    # Image downloading part
    img_info = requests.get(URL, stream=True)
    if img_info.status_code == 200:
        with open("images\\" + output_file_name, "wb") as output_file:
            shutil.copyfileobj(img_info.raw, output_file)

    del img_info

    print("\nAction: Image has been downloaded and saved")
    print("Debug: Saved image filename: {}".format(output_file_name))

    channel = context.channel
    await channel.send("Image downloaded and saved...")


# Command for uploading images from discord bot hosting server, from "\\images\\"" folder
@MyBot.command(aliases=["upload", "ul", "u", "uload", "l"], pass_context=True)
async def upload_image(context, requested_filename):

    channel = context.channel

    try:
        await channel.send(file=discord.File("images\\" + requested_filename + ".png"))
        await context.message.delete()

    except:
        print("\nDebug: Requested file does not exist!")
        await channel.send("Requested file does not exist!")


# Command for deleting multiple messages
@MyBot.command(aliases=["delete", "d", "del", "delete_all"], pass_context=True)
async def delete_messages(context):

    channel = context.channel
    messages = await channel.history().flatten()

    await channel.delete_messages(messages)
 

MyBot.run(TOKEN)
