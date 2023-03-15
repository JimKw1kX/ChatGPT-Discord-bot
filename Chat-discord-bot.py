import nest_asyncio
import os
import discord
from discord.ext import commands
import openai
import asyncio


nest_asyncio.apply()


async def my_coroutine():

    os.environ['OPENAI_API_KEY'] = 'API-KEY'


    # Set up the Discord bot
    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    # Set up the OpenAI API
    openai.api_key = os.environ['OPENAI_API_KEY']

    # Define a command for the bot to generate text using GPT-3
    @bot.command()
    async def talk(ctx, *, prompt):
        # Generate text from the prompt using the OpenAI API
        response = openai.Completion.create(
            model =  'text-davinci-003',    
            prompt= prompt,
            max_tokens=  4000,
            temperature=  1.0,
        )
        # Send the generated text back to the user
        await ctx.send(response.choices[0].text)

    # Start the bot
    bot.run('BOT-TOKEN')
    
loop = asyncio.get_event_loop()
loop.run_until_complete(my_coroutine())
