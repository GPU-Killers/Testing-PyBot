import discord
import dotenv
import os
import sentry_sdk

dotenv.load_dotenv()

token = os.getenv("TOKEN")
client = discord.Client(intents=discord.Intents.all())

sentry_sdk.init(
    dsn= "https://fd0c4fb898af479b9a25e06df1fcc335@o1236511.ingest.sentry.io/4504282752811008",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate= 1.0,
    _experiments= {
        "profiles_sample_rate": 1.0
    },
    auto_enabling_integrations= True
)

@client.event
async def on_ready():
    print(f'{client.user.name} is online!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not message.content.startswith("?"):
        return

    match message.content.replace("?", ""):
        # What does this do?
        # It checks if the message starts with "?"
        # If it does, it removes the "?" and then checks the message
        # If the message is "hello", it will send "Hello!"
        # If the message is "bye", it will send "Bye!"
        # If the message is "ping", it will send "pong"
        # If the message is anything else, it will send "I don't understand"
        case "hello":
            await message.channel.send("Hello!")
            return
        case "bye":
            await message.channel.send("Bye!")
            return
        case "ping":
            await message.channel.send("pong")
            return
        case _:
            await message.channel.send("I don't understand")
            return

client.run(token)

1/0