#!/usr/bin/python3


import nest_asyncio
import os
import discord
from discord.ext import commands
import openai
import asyncio


nest_asyncio.apply()

async def time_consuming_operation():
    # Perform time-consuming operation here
    await asyncio.sleep(10)

os.environ['OPENAI_API_KEY'] = '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'
# openai.api_base = "https://api.openai.com/v1/completions"


# Set up the Discord bot
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!',intents=intents)

# Set up the OpenAI API
openai.api_key = os.environ['OPENAI_API_KEY']

# Define a coroutine to handle incoming messages
async def my_coroutine(message):
    # Ignore messages sent by the bot itself
    if message.author == bot.user:
        return
    task = asyncio.create_task(time_consuming_operation())

    # Generate a response using OpenAI API
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.content,
        max_tokens=4000,
        temperature=1.0,
        n =1,
    )

    # Send the response back to the user
    print("Doing other things while time-consuming operation runs...")
    await message.channel.send(response.choices[0].text)
    await task
    print("Time-consuming operation is complete.")

# Define an event handler to call the coroutine when a message is received
@bot.event
async def on_message(message):
    await my_coroutine(message)

bot.run('MTA4NTMxOTM4MjExNDIzODU5NQ.GIiaqM.MBvdP2kftSrL977r3yRVTM99ozbJkNX_iQ4aoY')
loop = asyncio.get_event_loop()
loop.run_until_complete(my_coroutine())





