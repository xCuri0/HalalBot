#!/usr/bin/python3
"""
Halal bot
"""
import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="?")

@bot.event
async def on_ready():
    print("Bot running")

    activity = discord.Activity(name="infidels", type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)

@bot.event
async def on_message(message):
    for word in message.content.split():
        haram = open('haram.txt').read().splitlines()

        if (word.lower() in haram or word.lower()[:-1] in haram) and not \
        message.author.id == bot.user.id:
            await message.channel.send("%s BRO THATS HARAM" % message.author.mention)

if __name__ == "__main__":
    bot.run(os.environ['TOKEN'])
