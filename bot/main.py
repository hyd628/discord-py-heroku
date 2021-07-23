import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID=os.getenv("CHANNEL_ID")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.event
async def on_message(message):

    # Checking if its a dm channel
    if isinstance(message.channel, discord.DMChannel):
        # Getting the channel
        channel = bot.get_channel(int(CHANNEL_ID))
        await channel.send(f"{{{message.author}}} sent:\n```{message.content}```")

        await message.channel.send('Thanks! I will process your request.')
        
    # Processing the message so commands will work
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

if __name__ == "__main__":
    bot.run(TOKEN)
