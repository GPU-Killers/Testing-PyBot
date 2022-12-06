import discord
import dotenv
import os

dotenv.load_dotenv()

token = os.getenv("TOKEN")
client=discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
  print(f'{client.user.name} is online!')

async def on_message(message):
  if message.author == client.user:
    return

  elif message.content.startswith("!hello") or message.content.startswith("/hello"):
    await message.channel.send("Hello is an odd greeting.")

client.run(token)