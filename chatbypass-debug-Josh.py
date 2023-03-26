#!/usr/bin/python3


import requests
import subprocess
import os
import time
import readline

print("-" * 120)
print("                                                                                                      ") 
print("░█████╗░██╗░░██╗░█████╗░████████╗░██████╗░██████╗░████████╗  ██████╗░██╗░░░██╗██████╗░░█████╗░░██████╗░██████╗")
print("██╔══██╗██║░░██║██╔══██╗╚══██╔══╝██╔════╝░██╔══██╗╚══██╔══╝  ██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝")
print("██║░░╚═╝███████║███████║░░░██║░░░██║░░██╗░██████╔╝░░░██║░░░  ██████╦╝░╚████╔╝░██████╔╝███████║╚█████╗░╚█████╗░")
print("██║░░██╗██╔══██║██╔══██║░░░██║░░░██║░░╚██╗██╔═══╝░░░░██║░░░  ██╔══██╗░░╚██╔╝░░██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗")
print("╚█████╔╝██║░░██║██║░░██║░░░██║░░░╚██████╔╝██║░░░░░░░░██║░░░  ██████╦╝░░░██║░░░██║░░░░░██║░░██║██████╔╝██████╔╝")
print("░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░░░░╚═╝░░░  ╚═════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░")
print("                                                                                                      ")
print("                             A project by Jim Solomon              ")
print("-" * 120)



while True:

    p = input('Please enter your question here $: ')  

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + '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' # Your API Key here
    }

    json_data = {
        'model': 'text-davinci-003',    
        'prompt': p,
        'max_tokens': 4000,
        'temperature': 1.0,
    }
    
    
    url = 'https://api.openai.com/v1/completions'

    print('Contacting server...')

    response = requests.post(url, headers=headers, json=json_data, timeout=60)

    print('Processing response...')

    if response.content:
        process = subprocess.Popen(['jq', '-r', '.choices[].text'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output, error = process.communicate(input=response.content)

        print(output.decode())
    else:
        print('OpenAI coudn\'t generate a response :(')
