import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.') # you can set anyone ex '.'/'!'/'&'/'dp!'

@client.event
async def on_ready():
    print("Bot is online now")

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

client.run('your_bot_token') #set your token


#MR_ViSH
