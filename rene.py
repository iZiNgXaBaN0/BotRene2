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
minesweeper_emojis = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

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
async def blague():
    jokes = open("jokes.txt", "r", encoding = "utf-8").read().split("\n---\n")
    await bot.say(random.choice(jokes))

@bot.command()  
async def code():
    await bot.say("Voici le code du BOT : https://github.com/Eowalim/BotRene2 et merci à QUATRE de m'avoir aidé et compacté le code 🎇 !")
    
@bot.command(pass_context = True)
async def mariage(ctx):
    role = [role for role in ctx.message.server.roles if role.name == "Random"][0]
    eligibleMembers = [member for member in ctx.message.server.members if role in member.roles]
    random.shuffle(eligibleMembers)
    await bot.say(f" René a décidé de lier a vie **{eligibleMembers[0].mention}** et **{eligibleMembers[1].mention}**")

@bot.command()
async def demineur(height : int = 12, width : int = 12, bombs : int = 30):
    if any(not 1 < a < 41 for a in (width, height)) or bombs < 1:
        await bot.say("Erreur : les dimensions de la grille doivent être comprises entre 2 et 40 inclus, et elle doit contenir au moins 1 bombe.")
        return
    if bombs > width * height - 1:
        await bot.say("Erreur : la grille doit contenir au moins un espace libre !")
        return
    
    board = [True] * bombs + [False] * (width * height - bombs)
    random.shuffle(board)
    board = [board[x:x + width] for x in range(0, len(board), width)]
    
    output = ""
    for i, line in enumerate(board):
        for j, square in enumerate(line):
            if square:
                output += "||:bomb:|| "
            else:
                sum = 0
                for k in range(max(i - 1, 0), min(i + 2, len(board))):
                    for l in range(max(j - 1, 0), min(j + 2, len(line))):
                        sum += 1 if board[k][l] else 0
                output += f"||:{minesweeper_emojis[sum]}:|| "
        output += "\n"
    
    await bot.say(f"Dimensions : {width}x{height} ; Bombes : {bombs}")
    await bot.say(output)

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

    if message.author.bot:
        return

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
