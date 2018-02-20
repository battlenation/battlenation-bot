import discord
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix="*")

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name:  {}".format(client.user.name))
    print("ID:  {}".format(client.user.id))
    
    
@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")
    
client.run("NDE0ODc1MTUwNDg4NDM2NzM2.DWyDBw.D5PXg7Z8KSnUo5ejme3k0PTCwUc")
