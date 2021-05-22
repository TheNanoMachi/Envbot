import os
import discord


Client = discord.Client()

@Client.event
async def on_ready():
  print("we have logged in as {0.user}.format(Client)")

@Client.event
async def on_message(message):
  if message.authro == Client.user:
    return
  
  if message.content.startswith('$hello'):
    await message.channel.send("Hello!")

Client.run()

Client.run(os.getenv('TOKEN'))