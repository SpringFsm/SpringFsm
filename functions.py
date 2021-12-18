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

#retourne True si le titre est dans le fichier books, False sinon
def livrein(books,titre):
    liste_tempo = []
    rep = False
    with open(books, "r", encoding='utf-8') as f:
        line = f.readline()
        while line != '':
            line = line[:-1]
            liste_tempo = line.split(" _ ")
            if titre == liste_tempo[1]:
                rep = True
            line = f.readline()
    return rep

#simple affichage de matrice
def affichermatrice(m):
    for i in m:
        print(i)

#Fonction du projet
#crée un nouveau profil de lecteur
def ajouterlecteur(m,readers,books,booksread):
    #Messages réutilisables et variables
    erreur = "Réponse invalide, veuillez réessayer"
    genres = "1 - Homme , 2 - Femme , 3 - Autre"
    ages =""
    #pseudo
    pseudo = input("Choisissez un Pseudonyme :\n")
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

        updateajouterlecteur(m, books)

    else:
        print("Ce pseudo existe déja.")

#affiche toutes le information du lecteur avec pseudo donné
def afficherlecteur(readers,books,booksread):
    pseud = input("Saisissez le pseudo du lecteur :\n")
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

            ajouterlecteur(readers, books, booksread)

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
def suprimerlecteur(m,readers,booksread):
    pseudo = input("Saisissez le pseudo du lecteur :\n")
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

        updatesupprimerlecteur(m,nbligne)

    else:
        print("Pseudo non registré")

#ajoute un livre à la fin du fichier books si il n'existe pas encore
def ajouterlivre(m,books,readers):
    titre = input("Titre ?\n")
    rep = livrein(books,titre)
    if rep == False:
        with open(books,"r") as f:
            nblignes = len(f.readlines())
        with open(books,"a") as a:
            leligne = str(nblignes+1) + " _ " + titre + "\n"
            a.write(leligne)

        updateajouterlivre(m,readers)
    else:
        print("Ce livre existe déjà.")

#modifie le titre d'un livre dont on donne le numéro
def modifierlivre(books):
    titre = input("Saisissez le livre que vous voulez supprimer:\n")
    rep = livrein(books, titre)
    if rep == True:
        nvtitre = input("Titre ?\n")

        with open(books, "r", encoding='utf-8') as f:
            ligne = []
            line = f.readline()
            while line != "":
                line = line[:-1]
                line = line.split(" _ ")
                line = line[1:]
                line = line[0]
                ligne.append(line)
                line = f.readline()

            count = 0
            for i in ligne:
                if i == titre:
                    nbligne = count
                count += 1
            nbligne += 1

            # on stocke les lignes avant et après celle que l'utilisateur veut modifier du fichier books
            apres = ligne.copy()
            for i in range(nbligne):
                apres[i] = 0
            avant = ligne.copy()
            for j in range(nbligne - 1, len(avant)):
                avant[j] = 0

            # on écrit les lignes avant en effaçant le fichier + le numéro du livre
            count = 1
            with open(books, "w", encoding="utf-8") as f:
                for i in avant:
                    if i != 0:
                        ligne = str(count) + " _ " + i + "\n"
                        f.write(ligne)
                        count += 1

            with open(books, "a", encoding="utf-8") as g:
                ligne = str(count) + " _ " + nvtitre + "\n"
                g.write(ligne)

            # on écrit les lignes apres + le numéro du livre
            with open(books, "a", encoding="utf-8") as h:
                for i in apres:
                    if i != 0:
                        ligne = str(count + 1) + " _ " + i + "\n"
                        h.write(ligne)
                        count += 1

    else:
        print("Ce livre n'est pas registré.")

#supprime un livre choisis du fichier et décale les numéros des livres
def suprimerlivre(m,books,booksread):
    titre = input("Saisissez le livre que vous voulez supprimer:\n")
    rep = livrein(books, titre)
    if rep == True:
        with open(books,"r",encoding='utf-8') as f:
            ligne = []
            line = f.readline()
            while line != "":
                line = line[:-1]
                line = line.split(" _ ")
                line = line[1:]
                line = line[0]
                ligne.append(line)
                line = f.readline()

        count = 0
        for i in ligne:
            if i == titre:
                nbligne = count
            count+=1
        nbligne += 1

        # on stocke les lignes avant et après celle que l'utilisateur veut modifier du fichier books
        apres = ligne.copy()
        for i in range(nbligne):
            apres[i] = 0
        avant = ligne.copy()
        for j in range(nbligne - 1, len(avant)):
            avant[j] = 0

        #on écrit les lignes avant en effaçant le fichier + le numéro du livre
        count = 1
        with open(books, "w",encoding="utf-8") as f:
            for i in avant:
                if i!=0:
                    ligne = str(count) + " _ " + i + "\n"
                    f.write(ligne)
                    count += 1
        #on écrit les lignes apres + le numéro du livre
        with open(books, "a",encoding="utf-8") as f:
            for i in apres:
                if i!=0:
                    ligne = str(count) + " _ " + i + "\n"
                    f.write(ligne)
                    count += 1

        ligne = []
        listelignes = []

        with open(booksread, "r") as f:
            lignes = f.readlines()
            for i in lignes:
                i = i[:-1]
                l = i.split(', ')
                for j in l:
                    if j != str(nbligne):
                        ligne.append(j)
                listelignes.append(ligne)
                ligne = []

        with open(booksread, "w") as f:
            for i in listelignes:
                i = ', '.join(i)
                f.write(i)
                f.write('\n')

        print(titre, " a été supprimé.")

        updatesupprimerlivre(m,nbligne)

    else:
        print("Ce livre n'est pas registré.")

#création d'une matrice (init à 0) en fonction du nombre de livres et lecteurs
def matricedenotes(books,readers):
    with open(readers, "r") as f:
        ligne=f.readlines()
    with open(books, "r") as f:
        colonnes = f.readlines()
    M=[]
    for i in range(len(ligne)):
        L=[]
        for j in range(len(colonnes)):
            L.append(0)
        M.append(L)
    return M

#ajoute une note dans la matrice
def notationlivres(m,readers,books,booksread):
    pseudonyme = input("Saisissez votre pseudonyme:\n")
    rep = pseudoin(readers,pseudonyme)
    if rep == True:
        titre = input("Saisissez le titre du livre que vous voulez noter:\n")
        rep2 = livrein(books,titre)
        if rep2 == True:
            with open(books, "r", encoding='utf-8') as f:
                ligne = []
                line = f.readline()
                while line != "":
                    line = line[:-1]
                    line = line.split(" _ ")
                    line = line[1:]
                    line = line[0]
                    ligne.append(line)
                    line = f.readline()

            count = 0
            for i in ligne:
                if i == titre:
                    nbligne = count
                count += 1
            nbligne += 1

            with open(booksread, "r") as f:
                ligne = f.readline()
                count = 0
                while ligne != "":
                    count += 1
                    if pseudonyme in ligne:
                        nbpseudo = count
                    ligne = f.readline()

            rep3 = False
            leligne = alleralaligne(nbpseudo, booksread).split(', ')
            leligne[-1] = leligne[-1][:-1]

            for i in leligne:
                if i == str(nbligne):
                    rep3 = True

            if rep3 == True:
                while True:
                    try:
                        note = int(input("Donnez une note entre 1 et 5 à ce livre :\n1 : Vous n'avez pas aimé le livre\n5 : Vous adorez le livre\n"))
                        while note < 1 or note > 5:
                            print("Votre réponse est invalide. Donnez une note entre 1 et 5")
                            note = int(input("Donnez une note entre 1 et 5 à ce livre :\n1 : Vous n'avez pas aimé le livre\n5 : Vous adorez le livre\n"))
                        break
                    except ValueError:
                        print("Réponse invalide")

                nbligne -= 1
                nbpseudo -= 1
                m[nbpseudo][nbligne] = note

            else:
                print("Le lecteur na pas encore lu ce livre")

        else:
            print("Ce livre n'est pas enregistré.")

    else:
        print("Pseudo non registré.")

#fonctions d'update de la matrice
#ajoute une ligne à la matrice quand on ajoute un lecteur
def updateajouterlecteur(m,books):
    with open(books,"r") as f:
        total = f.readlines()
        nblignes = len(total)
    liste_tempo = []
    for i in range(nblignes):
        liste_tempo.append(0)
    m.append(liste_tempo)

#supprime une ligne à la matrice quand on supprime un lecteur
def updatesupprimerlecteur(m,nbligne):
    del m[nbligne - 1]

#ajoute une colonne à la matrice quand on ajoute un livre
def updateajouterlivre(m,readers):
    with open(readers,"r") as f:
        total = f.readlines()
        nbreaders = len(total)
        for i in range(nbreaders):
            m[i].append(0)

#supprime dans la matrice la colonne du livre suprimé
def updatesupprimerlivre(m,nbligne):
    for i in m:
        del i[nbligne - 1]



def suggererlivre(m,readers,books):
    print(m,readers,books)


#fonction qui lance le menu et permet à l'utilisateur d'utiliser toutes les fonctions que nous avons construit précédement
def main(m,books,booksread,readers):
    options = int(input("Que voulez vous faire \n1 : Apporter des modifications aux lecteurs\n2 : Apporter des modifications aux livres\n3 : Noter des livres\n4 : Sortir\n"))
    if options == 1:
        optionslecteur = int(input("Que voulez vous faire :\n1 : Ajouter lecteur\n2 : Afficher lecteur\n3 : Modifier lecteur\n4 : Supprimer lecteur\n5 : Revenir en arrière\n"))
        if optionslecteur == 1:
            ajouterlecteur(m,readers, books, booksread)
            main(m,books,booksread,readers)
        elif optionslecteur == 2:
            afficherlecteur(readers,books,booksread)
            main(m,books,booksread,readers)
        elif optionslecteur == 3:
            modifierlecteur(readers,books,booksread)
            main(m, books, booksread, readers)
        elif optionslecteur == 4:
            suprimerlecteur(m,readers,booksread)
            main(m, books, booksread, readers)
        elif optionslecteur == 5:
            main(m,books,booksread,readers)

    elif options == 2:
        optionslivres = int(input("Que voulez vous faire :\n1 : Ajouter un livre\n2 : Modifier un livre\n3 : Supprimer un livre\n4 : Revenir en arrière\n"))
        if optionslivres == 1:
            ajouterlivre(m,books,readers)
            main(m, books, booksread, readers)
        elif optionslivres == 2:
            modifierlivre(books)
            main(m, books, booksread, readers)
        elif optionslivres == 3:
            suprimerlivre(m,books,booksread)
            main(m, books, booksread, readers)
        elif optionslivres == 4:
            main(m, books, booksread, readers)

    elif options == 3:
        optionrecomendation = int(input("Que voulez vous faire :\n1 : Afficher la matrice des notes\n2 : Ajouter une note à un livre\n3 : Suggérer un livre\n4 : Revenir en arrière\n"))
        if optionrecomendation == 1:
            affichermatrice(m)
            main(m, books, booksread, readers)
        elif optionrecomendation == 2:
            notationlivres(m,readers,books,booksread)
            main(m, books, booksread, readers)
        elif optionrecomendation == 3:
            suggererlivre(m,readers,books)
            main(m, books, booksread, readers)
        elif optionrecomendation == 4:
            main(m, books, booksread, readers)
    elif options == 4:
        sortir = int(input("Etes vous sur de vouloir sortir :\n1 : Oui\n2 : Non\n"))
        if sortir == 1:
            print("Au revoir !\n")
        elif sortir == 2:
            main(m, books, booksread, readers)