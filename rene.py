import discord
from discord.ext    import commands
from discord.ext.commands   import Bot
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
        jeux = (
          "réinstaller son OS",
          "réinstaller Eowalim",
          "repeindre la chambre d'Eowalim",
          "souhaiter la fête des pères à Eowalim",
          "bugger pour embêter Eowalim",
          "dézinguer du zombie",
          "chercher son bot-sœur",
          "regarder Terraria",
          "Me Soûle Pas 3",
          "faire la sieste",
          "se débarrasser de Google",
          "ramasser des bigorneaux",
          "tu m'vois, tu m'vois pas",
          "installer TOR",
          "Banal Fantasy XXXIV",
          "Rambo Six : Tabouret",
          "Terrariarghh",
          "construire un mur",
          "chercher Mona",
          "grinder le wither boss",
          "chercher Excalibur",
          "déjeuner avec King Knight",
          
        )
        rjeux = random.choice(jeux)
        await bot.change_presence(game=discord.Game(name=rjeux))
        await asyncio.sleep(10800)

client.loop.create_task(on_ready())

     
@client.event
async def falcoday():
    await client.wait_until_ready()
    while not client.is_closed:
        channel = client.get_channel("562392613932630076")
        time = [86400, 172800, 259200, 345600, 432000, 518400, 604800] # 1j / 2j / 3j / 4j/ 5j / 6j/ 7j
        await client.send_message(channel, "Aujourd'hui c'est **Falconia Day** ! Joyeux **Falconia Day** à tous !")
        await asyncio.sleep(random.choice(time))

client.loop.create_task(falcoday())





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



        blague = ["!blague", "blague"]
        for x in blague:
         if x in message.content:
          if message.author != bot.user:
            variable2 = (
'''Quelle est la plus intelligente, la blonde, la rousse ou la brune ? **La rousse parce que c’est un dictionnaire.**''',

'''Un chien et un homme son sur un bateau. Le chien pète, l'homme tombe à l'eau et se noie. Quelle est la race du chien ? Un pékinois. (un pet qui noie)''',

'''Je suis inquiet, je vois des points noirs.
- Tu a vu l'oculiste ?
- Non, des points noirs !''',

'''Une femme discute avec une amie :
- "J'ai un mari en or."
 L'autre lui répond :
- "moi, le mien, il est en taule."''',

'''Sur le bord du Nil, trois gars voyant un crocodile dans l'eau se mettent à lui jeter des cailloux. À un moment, le crocodile, en colère, s'approche de la rive, prêt à monter sur la berge. Deux des gars se sauvent et montent dans un arbre. Le troisième, impassible, ne bouge pas. Les autres l'appellent et lui disent de se sauver. Alors l'autre leur répond : Ben pourquoi ? J'ai pas jeté de cailloux moi !''',

'''Un gars dit à un autre dans un troquet :
- T'es con toi ! T'es vraiment con ! C'est pas possible ce que t'es con ! J'ai jamais vu un con pareil ! Tiens, c'est simple, s'il existait un concours de cons, tu finirais deuxième !
- Pourquoi deuxième ?
- Parce que t'es trop con pour finir premier !''',

'''À la maternité un nouveau père, inquiet, demande à la sage-femme:
- Trouvez-vous que mon fils me ressemble ?
- Oui, mais c'est pas grave, l'essentiel c'est qu'il soit en bonne santé''',

'''Que dit Frodon devant sa maison?
C'est là que j'hobbit...''',

'''Qu'est-ce qui est vert et qui pousse sous l'eau ?
**Un chou marin**''',

'''Au cinéma, deux bavardes n’arrêtent pas de discuter. Excédé, leur voisin proteste :
- S’il vous plaît, je n’entends rien du tout.
- Et alors, ça vous regarde, ce qu'on raconte ?''',

'''Sur une petite île perdue au milieu de l'océan, un homme barbu agite désespérément les bras en direction d'un bateau. Sur le pont, un passager demande au capitaine :
- Qui est-ce...?
- Aucune idée. On passe tous les ans devant son île, et à chaque fois ça le rend fou !''',

'''- Allô Police ! Je viens d'écraser un poulet. Que dois-je faire ?
- Plumez-le et faites-le cuire…
- Ah bon ! Et qu'est-ce que je fais de la moto ?''',


'''- Bonjour, avez-vous amené au zoo le pingouin que vous avez trouvé dans la rue ?
- Oui, il a bien aimé, mais aujourd'hui on va au cinéma.''',


'''- J'ai aperçu ta copine l'autre jour, mais elle ne m'a pas vu !
- Je sais, elle me l'a dit.''',

'''Deux puces sortent du cinéma, l'une dit à l'autre :
- On rentre à pied ou on prend un chien ?''',

'''Un type voit un agent dans la rue et lui demande, tout rouge et essoufflé :
- Pardon monsieur l'agent, vous n'avez pas vu passer un camion de singes ?
- Pourquoi ? Vous êtes tombé ?''',

'''C'est quoi un canife ?
- Un petit fien.''',

'''Le Père Noël est le seul barbu qui peut survoler les États-Unis sans problème.''',

'''- Pilote à contrôle... pilote à contrôle... Je suis à 300 miles des côtes... 600 pieds au-dessus de l'eau... et à cours de carburant... qu'est-ce que je fais ?
- Contrôle à pilote... contrôle à pilote... répétez après moi : Notre Père qui est aux Cieux...''',

'''Dans un restaurant, un client dit :
- Garçon, que fait cette mouche dans ma soupe ?
- Je pense que c'est de la brasse... mais je peux me tromper...''',

'''En croisière dans l'Atlantique, le capitaine prend le micro et annonce aux 2 000 passagers :
- Mesdames et messieurs, j'ai une bonne et une mauvaise nouvelle à vous annoncer. Par laquelle je commence ?
Les gens veulent la bonne... Alors le capitaine répond :
- Nous allons gagner onze oscars...''',

'''Des deux maux qui frappent notre siècle, lequel est le plus terrible, l'ignorance ou l'apathie ?
Je sais pas et je m'en fous.''',

'''Un asticot rencontre un autre asticot
- Ça va ?
- Ouais ! J'ai la pêche !''',

'''Qu'est-ce qui est rouge avec des bandes blanches et qui sort de la pelouse à 200 km/h ?
**Une taupe en Ferrari.**''',

'''- T'aimes bien manger épicé ?
- En même temps ?''',

            )
            await bot.send_message(message.channel, (random.choice(variable2)))
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


bot.run(token)
