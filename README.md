# ChatGPT-Bypass

# Disclaimer: This tool is for educational purposes only!

This tool leverages the [text-davinci-003](https://platform.openai.com/docs/models/gpt-3-5) API model and it does not restric malicous contents referring to this [blog](https://arstechnica.com/information-technology/2023/02/now-open-fee-based-telegram-service-that-uses-chatgpt-to-generate-malware/).


You will need to add a API key from your OpenAI account as blow shown

![Figure 4](https://github.com/JimSolomon/ChatGPT-Bypass/blob/main/API.png)

Then replce the `API-KEY` value with the key in below line

```js
    'Authorization': 'Bearer ' + 'API-KEY' # Your API Key here
```

# Some Installations for Windows if you want to run `Python`, or you could just run the [PowerShell](https://github.com/JimSolomon/ChatGPT-Bypass/blob/main/chatbypass.ps1) script

1. Download `Python`

https://www.python.org/downloads/

2. Install `requests` via CMD

```powershell

C:\Users\user> pip3 install requests

```
3. Install `jq`

3.1 Download from below link to install
https://github.com/stedolan/jq/releases/download/jq-1.6/jq-win64.exe

or Install from `PowerShell`

run Powershell as Administrator then run

```powershell

PS C:\Windows\system32> choco install jq -y 

```

if choco is not installed then run

```powershell


PS C:\Windows\system32> Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1')) 


```


# Demo

1. Before ask ChatGPT


![Figure 2](https://github.com/JimSolomon/ChatGPT-Bypass/blob/main/Figure%202.png)


2. After run the tool

![Picture3.png](https://github.com/JimSolomon/ChatGPT-Bypass/blob/main/Figure%203.png)

3. Running `Python` from Windows CMD

![Picture4.png](https://github.com/JimSolomon/ChatGPT-Bypass/blob/main/Windows.png)

4. Running `PowerShell` 

![Powershell.png](https://github.com/JimSolomon/ChatGPT-Bypass/blob/main/powershell.png)


Credit: [GrimOutlaw](https://github.com/GrimOutlaw/ChatGPT-Bypass)
