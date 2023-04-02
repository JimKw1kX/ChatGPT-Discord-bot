#!/usr/bin/python3

import nest_asyncio
import os
import discord
from discord.ext import commands
import openai
import textwrap
import asyncio


nest_asyncio.apply()

async def time_consuming_operation():
    # Perform time-consuming operation here
    await asyncio.sleep(10)

os.environ['OPENAI_API_KEY'] = 'API-KEY'
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
    print(message)
    
# Generate a response using OpenAI API
    try:
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=message.content,
            max_tokens=4000,
            temperature=1.0,
            n =1,
    )
    
    except Exception as e:
        print(e)
        print(e.__dict__)
    
    # Split the response into chunks of 2000 characters or less and send each chunk as a separate message
    response_text = response.choices[0].text
    while len(response_text) > 0:
        await message.channel.send(response_text[:2000])
        response_text = response_text[2000:]

    await task
            
@bot.event
async def on_message(message):
    await my_coroutine(message)
    

bot.run('bot-token')
loop = asyncio.get_event_loop()
loop.run_until_complete(my_coroutine())
