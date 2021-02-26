import discord
from discord.ext import commands
import random
from discord.ext.commands import Bot
import asyncio
from async_timeout import timeout

TOKEN = " " #insert token given by discord here

client= discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is online")

@client.event
async def on_message(message):
    #if message is from bot, do nothing
    if message.author ==client.user:
        return
    #if message is not from bot, reply with one of these strings at random
    elif message.content.startswith("!8ball"):
        await message.channel.send(random.choice(["Soft no.",
                                    "Hard no.",
                                    "Yes... but sometimes no.",
                                    "Hell yeah!",
                                    "Hell no!",
                                    "Probably.",
                                    "Probably not.",
                                    "Maybe.",
                                    "I don't know, man.",
                                    "How does that make _you_ feel?",
                                    "/shrug",
                                    "Yup."]))

client.run(TOKEN)
