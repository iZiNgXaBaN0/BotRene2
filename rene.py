import discord
from discord.ext import commands
from discord.ext.commands import Bot

import asyncio
import json
import os
import random
import re

token = os.environ.get("api_key")

bot = commands.Bot(command_prefix='!')
client = discord.Client()

messages_reactions = json.load(open("messages_reactions.json", "r", encoding = "utf-8"))

@bot.event
async def on_ready():
    print ("Prêt, authentifié en tant que :")
    print (" - Name: " + bot.user.name)
    print (" - ID: " + bot.user.id)
    while not client.is_closed:
        jeu = random.choice([line.strip() for line in open("games.txt", "r", encoding = "utf-8").readlines()])
        await bot.change_presence(game = discord.Game(name = jeu))
        await asyncio.sleep(10800)

client.loop.create_task(on_ready())

     
@client.event
async def falcoday():
    await client.wait_until_ready()
    while not client.is_closed:
        channel = client.get_channel("562392613932630076")
        await client.send_message(channel, "Aujourd'hui c'est **Falconia Day** ! Joyeux **Falconia Day** à tous !")
        await asyncio.sleep(random.randint(1, 7) * 86400) # 1-7 jours

client.loop.create_task(falcoday())

@bot.command()
async def blague(message):
    jokes = open("jokes.txt", "r", encoding = "utf-8").read().split("\n---\n")
    bot.say(random.choice(jokes))

async def react(message):
    for mr in messages_reactions:
        if re.compile("(?i)" + mr["trigger"]).search(message.content) is not None:
            if mr["possible_answers"]:
                await bot.send_message(message.channel, random.choice(mr["possible_answers"]).format(message))
            for reaction in mr["reactions"]:
                await bot.add_reaction(message, reaction)
            return True
    return False

@bot.event
async def on_message(message):

    has_reacted = False
    
    #  Les deux channels
    if message.channel.id in ("562392613932630076", "562395596317524011"):
        has_reacted = await react(message)
       
    #  Juste le channel GRR
    if not has_reacted and message.channel.id == "562395596317524011":
        if message.author != bot.user:
            await bot.add_reaction(message, "😡")

    # Juste le channel YES
    if not has_reacted and message.channel.id == "562392613932630076":
        if message.author != bot.user:
            await bot.add_reaction(message, "😄")

    await bot.process_commands(message)


bot.run(token)
