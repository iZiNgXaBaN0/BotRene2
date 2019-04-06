import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import os

token = os.environ.get("api_key")

bot = commands.Bot(command_prefix='!')
client = discord.Client()


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

@bot.event
async def on_message(message):

  #  Les deux channel


  if(message.channel.id == "562392613932630076" or "562395596317524011"):
       bn = ["Ca va René?", "ca va René?", "Ca va René ?", "ca va René ?", "Ça va René ?", "ça va René ?", "Ça va René?" ,"ça va René ?", "ça va rené ?"]
       for x in bn:
        if x in message.content:
         if message.author != bot.user:
          variable = (
            "Très bien et toi {0.author.mention} ?".format(message),
            "Nope, j'ai fait la teuf hier soir, j'ai un peu la 🤢, là…",
            "Yeah !! C'est la teuf 🥳 !",
            "Chuut ! Je 😴...",
            "Bof, je suis fauché… T'as pas 10 balles ? 😋"
            "Chuis pas là, j'ai aqua-poney 😈",
            "Hé tu vois pas que je joue à FORTNITE ??!",
            "Ça fait pas 4 fois que tu demandes, toi ?",
            "Ça irait mieux si on me fichait un peu la paix, mais bon…",
            "Trop bien ! Je ramasse des bigorneaux !",
            "Bah mieux que toi, je dirais ! Noraj, hein",
            "J'ai battu le Moon Lord ! J'ai battu le Moon Lord ! \o/",
            "Pas trop, j'ai pris une flèche dans le genou… Je vais finir garde, c'est sûr 😱 ",
            "Chais pas, j'ai envie de rien aujourd'hui…",
            "C'est cool que t'arrives, {0.author.mention}, je commençais à m'ennuyer !".format(message),
            "Sekiro est enfin sorti, tout baigne, merci !",
            "Naaaaan ! Eowalim arrête pas de m'embêter !",
            "Bah moyen en fait… C'est quand Terraria ??!",
            "_Parti en vacances_",
            "Hein ?! Non, je dors pas ! 😝",
          )

          await bot.send_message(message.channel, (random.choice(variable)))
          await bot.remove_reaction(message, "😡")


        

        bigre = ["bigre", "Bigre", "BIGRE"]
        for x in bigre:
          if x in message.content:
            if message.author != bot.user:
              msg = "Bigre {0.author.mention} ! ".format(message)
              await bot.send_message(message.channel, msg)
              x = x+1

        bonjour = ["bonjour", "Bonjour", "BONJOUR"]
        for x in bonjour:
          if x in message.content:
            if message.author != bot.user:
              msg = "☀ Bonjour {0.author.mention}, comment vas-tu aujourd'hui ?".format(message)
              await bot.send_message(message.channel, msg)
              x = x+1


        bonsoir = ["bonsoir", "Bonsoir", "BONSOIR"]
        for x in  bonsoir:
          if x in message.content:
            if message.author != bot.user:
              msg = "Bonsoir {0.author.mention} j'espère que t'as passé une bonne journée 🌄".format(message)
              await bot.send_message(message.channel, msg)
              x = x+1



        bn = ["bonne nuit", "Bonne nuit", "BONNE NUIT"]
        for x in bn:
          if x in message.content:
            if message.author != bot.user:
              msg = "Bonne nuit {0.author.mention} fais de beaux rêves 🌙".format(message)
              await bot.send_message(message.channel, msg)
              x = x+1


        gh = ["GH", "Gh", "gh", "gH"]
        for x in gh:
          if x in message.content:
            if message.author != bot.user:
              await bot.add_reaction(message, ":VargSmile:414056117291974656")
              x = x+1


        goldhawk = ["Gold Hawk", "gold hawk", "Gold hawk", "GOLD HAWK", "GoldHawk", "goldhawk", "Goldhawk", "GOLDHAWK"]
        for x in goldhawk:
          if x in message.content:
            if message.author != bot.user:
              await bot.send_message(message.channel, "Notre grand maître à tous")
              x = x+1

  #  Juste le channel GRR


  if(message.channel.id == "562395596317524011"):
    if message.author != bot.user:
     await bot.add_reaction(message, "😡")

    grr = ["grr", "GRR", "Grr"]
    for x in grr:
      if x in message.content:
        if message.author != bot.user:
          await bot.add_reaction(message, "😡")
          x = x+1
   

    malade = ["malade", "malades", "Malade", "Malades", "MALADE", "MALADES"]
    for x in malade:
        if x in message.content:
          if message.author != bot.user:
            await bot.add_reaction(message, "🤢")
            msg = "Sorry {0.author.mention}, rétablis-toi bien. Je suis sûr que tu vas surmonter ça. YOU CAN DO IT !!!".format(message)
            await bot.send_message(message.channel, msg)
            x = x+1


  # Juste le channel YES


  if(message.channel.id == "562392613932630076"):
    if message.author != bot.user:
     await bot.add_reaction(message, "😄")

    grr = ["yes", "YES", "Yes"]
    for x in grr:
      if x in message.content:
        if message.author != bot.user:
          await bot.add_reaction(message, "😄")
          x = x+1

  await bot.process_commands(message)


bot.run(token)
