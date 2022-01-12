import discord
import requests, json
from datetime import datetime

verification_tag_original = "True"
verification_tag_ultimate = "True"
f = open("language.txt", "r")
language = f.read()
f.close()
score = 0
default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)


@client.event
async def on_ready():
    print("Le bot est prêt !")


@client.event
async def on_message(message):
    print(message.content)
    global language, x
    f = open("language.txt", "r")
    language = f.read()
    f.close()
    auteur = message.author.id
    try:
        global score
        f = open(str(auteur) + ".txt", "r")
        score = int(f.readline())
        f.close()
    except:
        f = open(str(auteur) + ".txt", "w")
        f.write("0")
        f.close()
    f = open(str(auteur) + ".txt", "r")
    score = int(f.read())
    f.close()
    f = open(str(auteur) + ".txt", "w")
    score_add = int(len(message.content) // 5)
    if 25 <= score_add:
        score_add = 25
    score = score + score_add
    f.write(str(score))
    f.close()
    general_channel: discord.TextChannel = client.get_channel(message.channel.id)
    if message.content.startswith("$xp <"):
        f = open(str(message.content[7:25]) + ".txt", "r")
        lecture_xp = f.read()
        if language == "Français":
            embed4 = discord.Embed(description="Les points d'expérience de  " + message.content[
                                                                                4:26] + "sur ce serveur sont " + lecture_xp + " :blue_circle:",
                                   title="Points d'expérience d'un membre du serveur", color=0x04ff00)
        if language == "English":
            embed4 = discord.Embed(description="The experience points of " + message.content[
                                                                             4:26] + "on this server are " + lecture_xp + " :blue_circle:",
                                   title="XP points of a server member", color=0x04ff00)
        await general_channel.send(embed=embed4)
        await message.delete()
    if message.content.startswith("$add"):
        identifiant = message.content[8:26]
        f = open(str(identifiant) + ".txt", "r")
        valeur2 = message.content[27:].strip()
        print(valeur2)
        lecture2 = f.read()
        new_value = int(lecture2) + int(valeur2)
        print(new_value)
        f.close()
        f = open(str(identifiant) + ".txt", "w")
        f.write(str(new_value))
        f.close()
        await message.delete()

    if message.content.startswith("$language"):
        langue_choisie = message.content[10:].strip()
        if language == "Français":
            w = open("language.txt", "w")
            if langue_choisie == "Français" or langue_choisie == "FRANCAIS" or langue_choisie == "FR" or langue_choisie == "FRENCH" or langue_choisie == "French" or langue_choisie == "fr" or langue_choisie == "Fr":
                embed5 = discord.Embed(
                    description="Le français est déjà sélectionné en tant que langue principale du bot sur ce serveur !")
                await general_channel.send(embed=embed5)
                w.write("Français")
            if langue_choisie == "Anglais" or langue_choisie == "ANGLAIS" or langue_choisie == "UK" or langue_choisie == "ENGLISH" or langue_choisie == "English" or langue_choisie == "uk" or langue_choisie == "Uk":
                w.write("English")
                embed8 = discord.Embed(description="The language has been set to English !")
                await general_channel.send(embed=embed8)
            if langue_choisie != "Anglais" and langue_choisie != "ANGLAIS" and langue_choisie != "UK" and langue_choisie != "ENGLISH" and langue_choisie != "English" and langue_choisie != "uk" and langue_choisie != "Uk" and langue_choisie != "Français" and langue_choisie != "FRANCAIS" and langue_choisie != "FR" and langue_choisie != "FRENCH" and langue_choisie != "French" and langue_choisie != "fr" and langue_choisie != "Fr":
                embed9 = discord.Embed(description="La langue que vous souhaitez définir n'est pas reconnue !")
                await general_channel.send(embed=embed9)
                w.write("Français")
            w.close()
        if language == "English":
            w = open("language.txt", "w")
            if langue_choisie == "Anglais" or langue_choisie == "ANGLAIS" or langue_choisie == "UK" or langue_choisie == "ENGLISH" or langue_choisie == "English" or langue_choisie == "uk" or langue_choisie == "Uk":
                embed5 = discord.Embed(
                    description="The English language is already selected as the main language of the bot on this server !")
                await general_channel.send(embed=embed5)
                w.write("English")
            if langue_choisie == "Français" or langue_choisie == "FRANCAIS" or langue_choisie == "FR" or langue_choisie == "FRENCH" or langue_choisie == "French" or langue_choisie == "fr" or langue_choisie == "Fr":
                w.write("Français")
                embed7 = discord.Embed(description="La langue a bien été définie sur Français !")
                await general_channel.send(embed=embed7)
            if langue_choisie != "Anglais" and langue_choisie != "ANGLAIS" and langue_choisie != "UK" and langue_choisie != "ENGLISH" and langue_choisie != "English" and langue_choisie != "uk" and langue_choisie != "Uk" and langue_choisie != "Français" and langue_choisie != "FRANCAIS" and langue_choisie != "FR" and langue_choisie != "FRENCH" and langue_choisie != "French" and langue_choisie != "fr" and langue_choisie != "Fr":
                embed9 = discord.Embed(description="The language you want to select does'nt exist !")
                await general_channel.send(embed=embed9)
                w.write("English")
            w.close()
        await message.delete()

    if message.content.startswith("$my_xp"):
        f = open(str(auteur) + ".txt", "r")
        lecture = f.read()
        if language == "Français":
            embed3 = discord.Embed(
                description="Vos points d'expérience sur ce serveur sont " + lecture + " :blue_circle:",
                title="Points d'expérience de " + str(message.author.name), color=0x04ff00)
        if language == "English":
            embed3 = discord.Embed(
                description="Your experience points on this server are " + lecture + " :blue_circle:",
                title="XP points of " + str(message.author.name), color=0x04ff00)
        await general_channel.send(embed=embed3)
        await message.delete()
    if message.content.startswith("$help") or message.content.startswith("$Help"):
        if language == "Français":
            embed1 = discord.Embed(
                description="**Pour obtenir les statistiques d'un joueur (Ultimate)**" + "\n" + '`/{tag sans #}`' + " :arrow_forward: `/HFFJkR5Q`" + "\n" + '\n' + "**Pour obtenir les statistiques d'un joueur (Original)**" + "\n" + '`{tag}`' + " :arrow_forward: `#HFFJkR5Q`" + '\n' + "\n" + "**Pour me faire dire quelque chose**" + '\n' + "`$say {texte}` :arrow_forward: `$say Bonjour`" + '\n' + "\n" + "**Pour supprimer des messages**" + '\n' + "`$del {nombre}` :arrow_forward: `$del 5`" + '\n' + "\n" + "**Pour connaître votre propre niveau d'expérience sur le serveur**" + '\n' + "`$my_xp` :arrow_forward: `$my_xp`" + '\n' + "\n" + "**Pour connaître le niveau d'expérience d'un membre du serveur**" + '\n' + " `$xp {utilisateur}` :arrow_forward: `$xp @[☠]The Blizzard[☠]`" + "\n" + '\n' + "**Pour mofifier la langue du bot par défaut**" + "\n" + "`$language {langue}` :arrow_forward: `$language English`",
                title="Commandes du Bot",
                url="https://discord.com/api/oauth2/authorize?client_id=896471724588163082&permissions=8&scope=bot",
                color=0x04ff00)
        if language == "English":
            embed1 = discord.Embed(
                description='**To get informations about a player (Ultimate)**' + "\n" + '`/{tag without #}`' + " :arrow_forward: `/HFFJkR5Q`" + "\n" + '\n' + '**To get informations about a player (Original)**' + "\n" + '`{tag}`' + " :arrow_forward: `#HFFJkR5Q`" + '\n' + "\n" + "**To make me say something**" + '\n' + "`$say {text}` :arrow_forward: `$say hello`" + '\n' + "\n" + "**To delete messages**" + '\n' + "`$del {number}` :arrow_forward: `$del 5`" + '\n' + "\n" + "**To know your own experience level on the server**" + '\n' + "`$my_xp` :arrow_forward: `$my_xp`" + '\n' + "\n" + "**To know the experience level of someone on the server**" + '\n' + " `$xp {user}` :arrow_forward: `$xp @[☠]The Blizzard[☠]`" + "\n" + "\n" + "**To set the bot language**" + "\n" + "`$language {language}` :arrow_forward: `$language FR`",
                title="Bot Commands",
                url="https://discord.com/api/oauth2/authorize?client_id=896471724588163082&permissions=8&scope=bot",
                color=0x04ff00)
        await general_channel.send(embed=embed1)
        await message.delete()
    if message.content == "Arès" or message.content == "Ares" or message.content == "arès" or message.content == "Ar€$" or message.content == "ares" or message.content == "Are$" or message.content == "Ar€s" or message.content == "are$" or message.content == "ar€$" or message.content == "ARES":
        if language == "Français":
            embed2 = discord.Embed(
                description="Mon préfixe sur le serveur est `$`" + "\n" + "\n" + "utilise la commande `$help` pour plus d'informations.",
                title="Préfixe du Bot", color=0x04ff00)
        if language == "English":
            embed2 = discord.Embed(
                description="My prefix on this server is `$`" + "\n" + "\n" + 'use `$help` command for more informations.',
                title="Bot Prefix", color=0x04ff00)
        await general_channel.send(embed=embed2)
        await message.delete()
    if message.content.startswith("<@!896471724588163082>"):
        if language == "Français":
            embed2 = discord.Embed(
                description="Mon préfixe sur le serveur est `$`" + "\n" + "\n" + "utilise la commande `$help` pour plus d'informations.",
                title="Préfixe du Bot", color=0x04ff00)
        if language == "English":
            embed2 = discord.Embed(
                description="My prefix on this server is `$`" + "\n" + "\n" + 'use `$help` command for more informations.',
                title="Bot Prefix", color=0x04ff00)
        await general_channel.send(embed=embed2)
        await message.delete()
    if message.content.startswith("$say"):
        message_to_send = str(message.content)
        await message.delete()
        await general_channel.send(content=message_to_send[4:])
    if message.content.startswith("$del"):

        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()

        for each_message in messages:
            await each_message.delete()

    if message.content.startswith("$top original"):
        f = open("Atrasis_original_player_tags.txt", "r")
        liste_de_meilleurs_joueurs_original_tr = []
        o = 0
        for line in f:
            if o < 100:
                The_Tag = line.strip()
                url = requests.get(f"https://api.magic.atrasis.net/original/users/%23{The_Tag}")
                data = json.loads(url.text)
                Record_de_Tr = data["bestTrophies"]
                liste_de_meilleurs_joueurs_original_tr.append([The_Tag, Record_de_Tr])
                o = o + 1

        def age(M):
            return M[1]

        f.close()
        sorted(liste_de_meilleurs_joueurs_original_tr, key=age)
        nombre_valeurs_original_tr = len(liste_de_meilleurs_joueurs_original_tr)
        nombre_valeurs_original_tr_1_perm = nombre_valeurs_original_tr - 1
        liste_tag_original_ordre = []
        liste_valeurs_trophies_original = []
        x = 0
        for i in range(nombre_valeurs_original_tr):
            liste_tag_original_ordre.append(sorted(liste_de_meilleurs_joueurs_original_tr, key=age)[x][0])
            liste_valeurs_trophies_original.append(sorted(liste_de_meilleurs_joueurs_original_tr, key=age)[x][1])
            x = x + 1
        r = 0
        liste_name_original_ordre = []
        for i in range(nombre_valeurs_original_tr):
            The_Tag = liste_tag_original_ordre[r]
            url = requests.get(f"https://api.magic.atrasis.net/original/users/%23{The_Tag}")
            data = json.loads(url.text)
            nom = str(data["name"])
            liste_name_original_ordre.append(nom)
            r = r + 1
        if language == "English":
            r = open("temp_file.txt", "w")
            r.write("")
            r.close()
            for i in range(nombre_valeurs_original_tr):
                t = open("temp_file.txt", "a")
                t.write(f'`{str(liste_name_original_ordre[nombre_valeurs_original_tr_1_perm])}` (#{liste_tag_original_ordre[nombre_valeurs_original_tr_1_perm]}) \n **{str(liste_valeurs_trophies_original[nombre_valeurs_original_tr_1_perm])}** :trophy:' + "\n")
                t.write("――――――――――――――――――――" + "\n")
                nombre_valeurs_original_tr_1_perm = nombre_valeurs_original_tr_1_perm - 1
            h = open("temp_file.txt", "r")
            lecture_embed = h.read()
            embed10 = discord.Embed(description=str(lecture_embed), title="Ranking of the best Atrasis Original players in function of their trophy record (in main village)")
            h.close()
            t.close()
        if language == "Français":
            r = open("temp_file.txt", "w")
            r.write("")
            r.close()
            for i in range(nombre_valeurs_original_tr):
                t = open("temp_file.txt", "a")
                t.write(f'`{str(liste_name_original_ordre[nombre_valeurs_original_tr_1_perm])}` (#{liste_tag_original_ordre[nombre_valeurs_original_tr_1_perm]}) \n **{str(liste_valeurs_trophies_original[nombre_valeurs_original_tr_1_perm])}** :trophy:' + "\n")
                t.write("――――――――――――――――――――" + "\n")
                h = open("temp_file.txt", "r")
                lecture_embed = h.read()
                nombre_valeurs_original_tr_1_perm = nombre_valeurs_original_tr_1_perm - 1
            h.close()
            t.close()

            embed10 = discord.Embed(description=str(lecture_embed), title="Classement des meilleurs joueurs Atrasis Original en fonction de leurs records de trophées (dans le village principal)")
        await general_channel.send(embed=embed10)
        await message.delete()

    if message.content.startswith("$top ultimate"):
        f = open("Atrasis_ultimate_player_tags.txt", "r")
        liste_de_meilleurs_joueurs_ultimate_tr = []
        u = 0
        for line in f:
            if u < 100:
                The_Tag = line.strip()
                url = requests.get(f"https://api.magic.atrasis.net/ultimate/users/%23{The_Tag}")
                data = json.loads(url.text)
                Record_de_Tr = data["bestTrophies"]
                liste_de_meilleurs_joueurs_ultimate_tr.append([The_Tag, Record_de_Tr])
                u = u + 1

        def age(M):
            return M[1]

        f.close()
        sorted(liste_de_meilleurs_joueurs_ultimate_tr, key=age)
        nombre_valeurs_ultimate_tr = len(liste_de_meilleurs_joueurs_ultimate_tr)
        nombre_valeurs_ultimate_tr_1_perm = nombre_valeurs_ultimate_tr - 1
        liste_tag_ultimate_ordre = []
        liste_valeurs_trophies_ultimate = []
        x = 0
        for i in range(nombre_valeurs_ultimate_tr):
            liste_tag_ultimate_ordre.append(sorted(liste_de_meilleurs_joueurs_ultimate_tr, key=age)[x][0])
            liste_valeurs_trophies_ultimate.append(sorted(liste_de_meilleurs_joueurs_ultimate_tr, key=age)[x][1])
            x = x + 1
        r = 0
        liste_name_ultimate_ordre = []
        for i in range(nombre_valeurs_ultimate_tr):
            The_Tag = liste_tag_ultimate_ordre[r]
            url = requests.get(f"https://api.magic.atrasis.net/ultimate/users/%23{The_Tag}")
            data = json.loads(url.text)
            nom = str(data["name"])
            liste_name_ultimate_ordre.append(nom)
            r = r + 1
        if language == "English":
            r = open("temp_file.txt", "w")
            r.write("")
            r.close()
            for i in range(nombre_valeurs_ultimate_tr):
                t = open("temp_file.txt", "a")
                t.write(f'`{str(liste_name_ultimate_ordre[nombre_valeurs_ultimate_tr_1_perm])}` (#{liste_tag_ultimate_ordre[nombre_valeurs_ultimate_tr_1_perm]}) \n **{str(liste_valeurs_trophies_ultimate[nombre_valeurs_ultimate_tr_1_perm])}** :trophy:' + "\n" + "――――――――" + "\n")
                t.write("――――――――――――――――――――" + "\n")
                h = open("temp_file.txt", "r")
                lecture_embed = h.read()
                nombre_valeurs_ultimate_tr_1_perm = nombre_valeurs_ultimate_tr_1_perm - 1
            embed10 = discord.Embed(description=str(lecture_embed), title="Ranking of the best Atrasis Ultimate players in function of their trophy record (in main village)")
            h.close()
            t.close()
        if language == "Français":
            r = open("temp_file.txt", "w")
            r.write("")
            r.close()
            for i in range(nombre_valeurs_ultimate_tr):
                t = open("temp_file.txt", "a")
                t.write(f'`{str(liste_name_ultimate_ordre[nombre_valeurs_ultimate_tr_1_perm])}` (#{liste_tag_ultimate_ordre[nombre_valeurs_ultimate_tr_1_perm]}) \n **{str(liste_valeurs_trophies_ultimate[nombre_valeurs_ultimate_tr_1_perm])}** :trophy:' + "\n")
                t.write("――――――――――――――――――――" + "\n")
                h = open("temp_file.txt", "r")
                lecture_embed = h.read()
                nombre_valeurs_ultimate_tr_1_perm = nombre_valeurs_ultimate_tr_1_perm - 1
            h.close()
            t.close()

            embed10 = discord.Embed(description=str(lecture_embed), title="Classement des meilleurs joueurs Atrasis Ultimate en fonction de leurs records de trophées (dans le village principal)")
        await general_channel.send(embed=embed10)
        await message.delete()

    if message.content.lower().startswith("$rank original"):
        try:
            rank = int(message.content[15:].strip())
            f = open("Atrasis_original_player_tags.txt", "r")
            u = 1
            for line in f:
                The_Tag = line.strip()
                if u == rank:
                    url = requests.get(f"https://api.magic.atrasis.net/original/users/%23{The_Tag}")
                    data = json.loads(url.text)
                    Record_de_Tr = data["bestTrophies"]
                    if language == "Français":
                        embed11 = discord.Embed(description="`" + data["name"] + "` #" + The_Tag + "\n" + str(Record_de_Tr),title=f"Joueur classé #{str(rank)}:earth_americas:  monde (Atrasis Original)")
                    if language == "English":
                        embed11 = discord.Embed(description="`" + data["name"] + "` #" + The_Tag + "\n" + str(Record_de_Tr), title=f"PLayer ranked #{str(rank)}:earth_americas:  world (Atrasis Original)")
                    await general_channel.send(embed=embed11)
                u = u + 1
            f.close()
        except:
            f = open("Atrasis_original_player_tags.txt", "r")
            t = 0
            for line in f:
                t = t + 1
            if language == "Français":
                await general_channel.send(content=f"Le classement ne comprend pas les joueurs en dessous du top {str(t)} mondial.")
            if language == "English":
                await general_channel.send(content=f"Ranking does not include players below world top {str(t)}.")
            f.close()
        await message.delete()

    if message.content.lower().startswith("$rank ultimate"):
        try:
            rank = int(message.content[15:].strip())
            f = open("Atrasis_ultimate_player_tags.txt", "r")
            u = 1
            for line in f:
                The_Tag = line.strip()
                if u == rank:
                    url = requests.get(f"https://api.magic.atrasis.net/ultimate/users/%23{The_Tag}")
                    data = json.loads(url.text)
                    Record_de_Tr = data["bestTrophies"]
                    if language == "Français":
                        embed11 = discord.Embed(description="`" + data["name"] + "` #" + The_Tag + "\n" + str(Record_de_Tr),title=f"Joueur classé #{str(rank)}:earth_americas:  monde (Atrasis Ultimate)")
                    if language == "English":
                        embed11 = discord.Embed(description="`" + data["name"] + "` #" + The_Tag + "\n" + str(Record_de_Tr), title=f"PLayer ranked #{str(rank)}:earth_americas:  world (Atrasis Ulimate)")
                    await general_channel.send(embed=embed11)
                u = u + 1
            f.close()
        except:
            f = open("Atrasis_ultimate_player_tags.txt", "r")
            t = 0
            for line in f:
                t = t + 1
            if language == "Français":
                await general_channel.send(content=f"Le classement ne comprend pas les joueurs en dessous du top {str(t)} mondial.")
            if language == "English":
                await general_channel.send(content=f"Ranking does not include players below world top {str(t)}.")
            f.close()
        await message.delete()

    if message.content.startswith("/"):
        try:
            my_date = str(datetime.now())
            heure = str(my_date[11:16])
            auteur = message.author
            hashtag = message.content[1:].strip()
            url = requests.get(f"https://api.magic.atrasis.net/ultimate/users/%23{hashtag}")
            text = url.text

            data = json.loads(text)
            if language == "Français":
                embed = discord.Embed(title="Statistiques pour " + data["name"],
                                      url="https://link.ultimate.atrasis.cc/fr?action=OpenPlayerProfile&tag=" + hashtag,
                                      description=("**" + data["name"] + " - " + data[
                                          "tag"] + "**" + "\n" + ""
                                                                 "`Trophées: ` " + "**" + str(
                                          data[
                                              "trophies"]) + "**" + " :trophy:" + "\n" + "`Record de trophées: `" + "**" +
                                                   str(data[
                                                           "bestTrophies"]) + "** " + ":trophy:" + "\n" + "`Niveau: ` " + "**" + str(
                                                  data["expLevel"])) +
                                                  "** " + ":blue_circle:" + "\n" + "`Niveau d'hôtel de ville : `" + "**" + str(
                                          data["townHallLevel"]) + "** " +
                                                  ":house:" + "\n", color=0x04ff00)
                embed.set_author(name="Atrasis Ultimate")
                embed.add_field(name="demandé par " + str(auteur), value="Aujourd'hui à " + heure, inline=False)
            if language == "English":
                embed = discord.Embed(title="Statistics for " + data["name"],
                                      url="https://link.ultimate.atrasis.cc/fr?action=OpenPlayerProfile&tag=" + hashtag,
                                      description=("**" + data["name"] + " - " + data[
                                          "tag"] + "**" + "\n" + ""
                                                                 "`Trophies: ` " + "**" + str(
                                          data["trophies"]) + "**" + " :trophy:" + "\n" + "`Best Trophies: `" + "**" +
                                                   str(data[
                                                           "bestTrophies"]) + "** " + ":trophy:" + "\n" + "`Level: ` " + "**" + str(
                                                  data["expLevel"])) +
                                                  "** " + ":blue_circle:" + "\n" + "`Town Hall level : `" + "**" + str(
                                          data["townHallLevel"]) + "** " +
                                                  ":house:" + "\n", color=0x04ff00)
                embed.set_author(name="Atrasis Ultimate")
                embed.add_field(name="requested by " + str(auteur), value="Today at " + heure, inline=False)
            await general_channel.send(embed=embed)
            f = open("Atrasis_ultimate_player_tags.txt", "r")
            global verification_tag_ultimate
            verification_tag_ultimate = "True"
            for line in f:
                tag = line.strip()
                if tag == hashtag:
                    verification_tag_ultimate = "False"
            if verification_tag_ultimate == "True":
                h = open("Atrasis_ultimate_player_tags.txt", "a")
                h.write(hashtag + "\n")
                h.close()
                f.close()

        except:
            await general_channel.send("Check if you used the great tag.")
        await message.delete()

    if message.content.startswith("#"):
        try:
            my_date = str(datetime.now())
            heure = str(my_date[11:16])
            auteur = message.author
            hashtag = message.content[1:].strip()
            url = requests.get(f"https://api.magic.atrasis.net/original/users/%23{hashtag}")
            text = url.text

            data = json.loads(text)
            if language == "Français":
                embed = discord.Embed(title="Statistiques pour " + data["name"],
                                      url="https://link.original.atrasis.cc/fr?action=OpenPlayerProfile&tag=" + hashtag,
                                      description=("**" + data["name"] + " - " + data[
                                          "tag"] + "**" + "\n" + ""
                                                                 "`Trophées: ` " + "**" + str(
                                          data[
                                              "trophies"]) + "**" + " :trophy:" + "\n" + "`Record de trophées: `" + "**" +
                                                   str(data[
                                                           "bestTrophies"]) + "** " + ":trophy:" + "\n" + "`Niveau: ` " + "**" + str(
                                                  data["expLevel"])) +
                                                  "** " + ":blue_circle:" + "\n" + "`Niveau d'hôtel de ville : `" + "**" + str(
                                          data["townHallLevel"]) + "** " +
                                                  ":house:" + "\n", color=0x04ff00)
                embed.set_author(name="Atrasis Original")
                embed.add_field(name="demandé par " + str(auteur), value="Aujourd'hui à " + heure, inline=False)
            if language == "English":
                embed = discord.Embed(title="Statistics for " + data["name"],
                                      url="https://link.original.atrasis.cc/fr?action=OpenPlayerProfile&tag=" + hashtag,
                                      description=("**" + data["name"] + " - " + data[
                                          "tag"] + "**" + "\n" + ""
                                                                 "`Trophies: ` " + "**" + str(
                                          data["trophies"]) + "**" + " :trophy:" + "\n" + "`Best Trophies: `" + "**" +
                                                   str(data[
                                                           "bestTrophies"]) + "** " + ":trophy:" + "\n" + "`Level: ` " + "**" + str(
                                                  data["expLevel"])) +
                                                  "** " + ":blue_circle:" + "\n" + "`Town Hall level : `" + "**" + str(
                                          data["townHallLevel"]) + "** " +
                                                  ":house:" + "\n", color=0x04ff00)
                embed.set_author(name="Atrasis Original")
                embed.add_field(name="requested by " + str(auteur), value="Today at " + heure, inline=False)
            await general_channel.send(embed=embed)
            f = open("Atrasis_original_player_tags.txt", "r")
            global verification_tag_original
            verification_tag_original = "True"
            for line in f:
                tag = line.strip()
                if tag == hashtag:
                    verification_tag_original = "False"
            if verification_tag_original == "True":
                h = open("Atrasis_original_player_tags.txt", "a")
                h.write(hashtag + "\n")
                h.close()
                f.close()
        except:
            await general_channel.send("Check if you used the great tag.")
        await message.delete()


client.run("ODk2NDcxNzI0NTg4MTYzMDgy.YWHmWg.uEsVZv5h4aP5taaVT2x4w6P6GSE")
