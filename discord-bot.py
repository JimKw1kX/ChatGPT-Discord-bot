#!/usr/bin/python3



import nest_asyncio
nest_asyncio.apply()
import os
import discord
from discord.ext import commands
import openai
import asyncio




os.environ['OPENAI_API_KEY'] = 'API-KEY'


# Set up the Discord bot
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!',intents=intents)

# Set up the OpenAI API
openai.api_key = os.environ['OPENAI_API_KEY']

# Define a coroutine to handle incoming messages
async def my_coroutine(message):
    # Ignore messages sent by the bot itself
    if message.author == bot.user:
        return

    # Generate a response using OpenAI API
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.content,
        max_tokens=4000,
        temperature=1.0,
    )

    # Send the response back to the user
    await message.channel.send(response.choices[0].text)

# Define an event handler to call the coroutine when a message is received
@bot.event
async def on_message(message):
    await my_coroutine(message)



bot.run('BOT-TOKEN')
