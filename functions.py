#Programme contenant les fonctions à utiliser dans le programme principal

#imports

#imports

#Début

#Fonctions utiles
#Affiche tous les livres
def afficherlivres(books):
    with open(books, "r", encoding='utf-8') as f:
        for ligne in f:
            print(ligne)

#Affiche tous les styles de litérature
def afficher_styles():
    styles = ["1-Science-fiction", "2-Biographie,", "3-Horreur", "4-Romance", "5-Fable", "6-Histoire", "7-Comédie"]
    for i in styles:
        print(i)

#crée la liste des livres lus par l'utilisateur
def livres_lus(books,erreur):
    liste_livres = []
    while True:
        try:
            afficherlivres(books)
            livres = int(input("Choisissez le nombre correspondant à un livre déjà lu, ou saisissez le nombre 0 si vous n'avez lu aucun de ces livres \n"))
            while livres != 0:
                while livres < 1 or livres > 19:
                    print(erreur)
                    afficherlivres(books)
                    livres = int(input("Choisissez le nombre correspondant à un livre déjà lu, ou saisissez le nombre 0 si vous n'avez lu aucun de ces livres \n"))
                liste_livres.append(livres)
                afficherlivres(books)
                livres = int(input("Choisissez le nombre correspondant à un livre déjà lu, ou saisissez le nombre 0 si vous n'avez lu aucun de ces livres \n"))
            break
        except ValueError:
            print(erreur)

    if liste_livres != []:
        lelivres = []
        for i in liste_livres:
            i = str(i)
            if i not in lelivres:
                lelivres.append(i)
    else :
        lelivres = []


    return lelivres

#renvoie le numéro d'une ligne dans un fichier
def alleralaligne(n,fichier):
    with open(fichier, "r", encoding='utf-8') as f:
        for i in range(n):
            line = f.readline()
    return line

#retourne True si le pseudo est dans le fichier, False sinon
def pseudoin(fichier,pseudo):
    liste_tempo = []
    rep = False
    with open(fichier,"r") as f:
        line = f.readline()
        while line != '':
            liste_tempo = line.split(", ")
            if pseudo in liste_tempo:
                rep = True
            line = f.readline()
    return rep

#Fonction du projet
#crée un nouveau profil de lecteur
def ajoutelecteur(readers,books,booksread):
    #Messages réutilisables et variables
    erreur = "Réponse invalide, veuillez réessayer"
    genres = "1 - Homme , 2 - Femme , 3 - Autre"
    ages =""
    #pseudo
    pseudo = input("Choisissez un Pseudonyme :\n")
    pseudo = pseudo.lower()
    rep = pseudoin(readers,pseudo)
    if rep == False:
        # genre
        print(genres)
        while True:
            # au cas ou il ne mette pas un entier
            try:
                genre = int(input("Choisissez le nombre correspondant à votre genre \n"))
                # au cas ou il mette un entier diférent de 1,2 ou 3
                while genre not in [1, 2, 3]:
                    print(erreur)
                    genre = int(input("Choisissez le nombre correspondant à votre genre \n"))
                break
            except ValueError:
                print(erreur)
        # age
        while True:
            # au cas ou il ne mette pas un entier
            try:
                age = int(input("Quel âge avez vous ? \n"))
                break
            except ValueError:
                print(erreur)
        if age <= 18:
            # age inférieur ou égal à 18 ans : 1
            age = 1
        elif age > 25:
            # age supérieur à 25 ans : 3
            age = 3
        else:
            # age entre 18 et 25 and : 2
            age = 2
        # style
        while True:
            try:
                afficher_styles()
                style = int(input("Choisissez le nombre correspondant à votre style de lecture \n"))
                while style < 1 or style > 7:
                    afficher_styles()
                    print(erreur)
                    style = int(input("Choisissez le nombre correspondant à votre style de lecture \n"))
                break
            except ValueError:
                print(erreur)

        # tout écrire dans le fichier
        with open(readers, "a") as f:
            genre = str(genre)
            age = str(age)
            style = str(style)
            f.write(pseudo)
            f.write(", ")
            f.write(genre)
            f.write(", ")
            f.write(age)
            f.write(", ")
            f.write(style + "\n")

        with open(booksread, "a") as s:
            livreslus = livres_lus(books, erreur)
            s.write(pseudo)
            for i in livreslus:
                s.write(", ")
                s.write(i)
            s.write("\n")
    else:
        print("Ce pseudo existe déja.")

#affiche toutes le information du lecteur avec pseudo donné
def afficherlecteur(readers,books,booksread):
    pseud = input("Saisissez le pseudo du lecteur :\n")
    pseud = pseud.lower()
    rep = pseudoin(readers,pseud)
    if rep == True:
        nbligne = 0
        with open(readers, "r") as f:
            ligne = f.readline()
            count = 0
            while ligne != "":
                count += 1
                if pseud in ligne:
                    nbligne = count
                ligne = f.readline()
        if nbligne != 0:
            # transformation de la ligne en une liste avec les infos "genre","âge" et "style" sans le pseudo"
            leligne = alleralaligne(nbligne, readers)
            if leligne[-1:] != "":
                leligne = leligne[:-1]
            leligne = leligne[len(pseud) + 2:]
            leligne = leligne.split(", ")

            # genres

            if leligne[0] == "1":
                genre = "Homme"
            elif leligne[0] == "2":
                genre = "Femme"
            elif leligne[0] == "3":
                genre = "Autre"

            # âge

            if leligne[1] == "1":
                age = "18 ans ou moins"
            elif leligne[1] == "2":
                age = "Entre 18 et 25 ans"
            elif leligne[1] == "3":
                age = "Plus de 25 ans"

            # style

            if leligne[2] == "1":
                style = "Science-fiction"
            elif leligne[2] == "2":
                style = "Biographie"
            elif leligne[2] == "3":
                style = "Horreur"
            elif leligne[2] == "4":
                style = "Romance"
            elif leligne[2] == "5":
                style = "Fable"
            elif leligne[2] == "6":
                style = "Histoire"
            elif leligne[2] == "7":
                style = "Comédie"

            print(pseud, ", ", genre, ", ", age, ", ", style)

            # afficher les livres lus

            laligne = alleralaligne(nbligne, booksread)
            if laligne[-1:] != "":
                laligne = laligne[:-1]
            laligne = laligne[len(pseud) + 2:]
            laligne = laligne.split(", ")
            lavrailigne = []

            # convertis la liste "laligne" de str en liste "lavrailigne" de int
            for i in laligne:
                e = int(i)
                lavrailigne.append(e)

            for j in lavrailigne:
                lelivre = alleralaligne(j, books)
                if j < 10:
                    lelivre = lelivre[4:]
                else:
                    lelivre = lelivre[5:]

                print(lelivre, end="")

    else:
        print("Pseudo non registré")

#modifie toutes les informations sur un lecteur
def modifierlecteur(readers,books,booksread):
    pseudo = input("Saisissez le pseudo du lecteur :\n")
    pseudo = pseudo.lower()
    rep = pseudoin(readers,pseudo)
    if rep == True:

        nbligne = 0
        with open(readers, "r") as f:
            ligne = f.readline()
            count = 0
            while ligne != "":
                count += 1
                if pseudo in ligne:
                    nbligne = count
                ligne = f.readline()
        if nbligne != 0:
            # on stocke les lignes avant et après celle que l'utilisateur veut modifier du fichier readers
            with open(readers, "r") as f:
                apres = f.readlines()
                for i in range(nbligne):
                    apres[i] = 0
            with open(readers, "r") as g:
                avant = g.readlines()
                for j in range(nbligne - 1, len(avant)):
                    avant[j] = 0

            # on stocke les lignes avant et après celle que l'utilisateur veut modifier du fichier booksread
            with open(booksread, "r") as f:
                apres2 = f.readlines()
                for i in range(nbligne):
                    apres2[i] = 0
            with open(booksread, "r") as g:
                avant2 = g.readlines()
                for j in range(nbligne - 1, len(avant2)):
                    avant2[j] = 0

            # on écrit les lignes "avant" dans les fichiers readers et booksread, ce qui éface tout le reste
            with open(readers, 'w') as h:
                for i in avant:
                    if i != 0:
                        h.write(i)
            with open(booksread, 'w') as h:
                for i in avant2:
                    if i != 0:
                        h.write(i)

            ajoutelecteur(readers, books, booksread)

            # on écrit les lignes "apres" dans les fichiers readers et booksread sans efacer ce qu'il y avait avant
            with open(readers, 'a') as j:
                for i in apres:
                    if i != 0:
                        j.write(i)
            with open(booksread, 'a') as j:
                for i in apres2:
                    if i != 0:
                        j.write(i)

    else:
        print("Pseudo non registré")

#suprime les informations sur un lecteur
def suprimerlecteur(readers,booksread):
    pseudo = input("Saisissez le pseudo du lecteur :\n")
    pseudo = pseudo.lower()
    rep = pseudoin(readers,pseudo)
    if rep == True :

        nbligne = 0
        with open(readers, "r") as f:
            ligne = f.readline()
            count = 0
            while ligne != "":
                count += 1
                if pseudo in ligne:
                    nbligne = count
                ligne = f.readline()
        if nbligne != 0:
            # on stocke les lignes avant et après celle que l'utilisateur veut modifier du fichier readers
            with open(readers, "r") as f:
                apres = f.readlines()
                for i in range(nbligne):
                    apres[i] = 0
            with open(readers, "r") as g:
                avant = g.readlines()
                for j in range(nbligne - 1, len(avant)):
                    avant[j] = 0

            # on stocke les lignes avant et après celle que l'utilisateur veut modifier du fichier booksread
            with open(booksread, "r") as f:
                apres2 = f.readlines()
                for i in range(nbligne):
                    apres2[i] = 0
            with open(booksread, "r") as g:
                avant2 = g.readlines()
                for j in range(nbligne - 1, len(avant2)):
                    avant2[j] = 0

            # on écrit les lignes "avant" dans les fichiers readers et booksread, ce qui éface tout le reste
            with open(readers, 'w') as h:
                for i in avant:
                    if i != 0:
                        h.write(i)
            with open(booksread, 'w') as h:
                for i in avant2:
                    if i != 0:
                        h.write(i)

            # on écrit les lignes "apres" dans les fichiers readers et booksread sans efacer ce qu'il y avait avant
            with open(readers, 'a') as j:
                for i in apres:
                    if i != 0:
                        j.write(i)
            with open(booksread, 'a') as j:
                for i in apres2:
                    if i != 0:
                        j.write(i)

            print("Les information du lecteur : ", pseudo, "on été supprimées.")

    else:
        print("Pseudo non registré")

def Ajouter_Livres(fichier):
    with open(fichier, "r") as f:
        Titre=input("Saisissez le titre de livre que vous voulez ajoutez")
        ligne = f.readline()
        NbLigne=1
        count=1
        while ligne!="":
            count+=1
            if Titre in ligne:
                NbLigne=count
                return("Votre livre est deja enregistrée à la ligne", count-1)
            ligne = f.readline()
            NbLigne=count
        else:
            with open(fichier, "a") as f:
                NbLigne=str(NbLigne)
                f.write(NbLigne + " - ")
                f.write(Titre + "\n")

