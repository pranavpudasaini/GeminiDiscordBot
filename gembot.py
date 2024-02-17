#!/usr/bin/env python3

import discord
import requests
import json
import dotenv
from os import environ

dotenv.load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}')
        if (message.author == self.user):
            return
        if message.content.startswith(">> "):
            query = message.content.split(">> ")[1] + " . Please answer in less than 500 characters."
            print('Running inference ...')
            result = requests.post(url=f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={environ["GEMINI_API_KEY"]}', json={"contents":[{"parts":[{"text":f"{query}"}]}]})
            jsonResult = json.loads(result.text)
            output = jsonResult['candidates'][0]['content']['parts'][0]['text']
            print(output)
            print('Sending to Discord ...')
            await message.channel.send(
f"""
# Your Question:

`{query}`

# Answer:

{output}
""")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(environ['DISCORD_BOT_TOKEN'])
