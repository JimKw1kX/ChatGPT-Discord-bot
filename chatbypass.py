#!/usr/bin/python3
import requests
import subprocess
import os
import time

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
        'Authorization': 'Bearer ' + 'API-KEY' # Your API Key here
    }

    json_data = {
        'model': 'text-davinci-003',    
        'prompt': p,
        'max_tokens': 4000,
        'temperature': 1.0,
    }
    
    
    url = 'https://api.openai.com/v1/completions'

    response = requests.post(url, headers=headers, json=json_data)

    process = subprocess.Popen(['jq', '-r', '.choices[].text'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output, error = process.communicate(input=response.content)

    print(output.decode())
    time.sleep(1)
