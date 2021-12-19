#Programme contenant les fonctions à utiliser dans le programme principal

#imports
from math import sqrt
from time import time
#imports

#Début

#Fonctions utiles
def afficherlivres(books):
    '''
    Affiche le fichier books ligne par ligne
    :param books: fichier txt
    :return: None
    On imprime directement le résultat dans la console
    '''
    with open(books, "r", encoding='utf-8') as f:
        for ligne in f:
            print(ligne[:-1])

def afficher_styles():
    '''
    Affiche la liste des styles de lecture. On pourrais rajouter manuellement des styles en modifiant la liste si dessous
    :return: None
    On imprime directement le résultat dans la console
    '''
    styles = ["1-Science-fiction", "2-Biographie,", "3-Horreur", "4-Romance", "5-Fable", "6-Histoire", "7-Comédie"]
    for i in styles:
        print(i)

def livres_lus(books,erreur):
    '''
    Renvoie une liste avec les numéros des livres lus pas le lecteur
    :param books: fichier txt
    :param erreur: str
    :return: list
    '''
    liste_livres = []
    with open(books,"r",encoding='utf-8') as f:
        taille = len(f.readlines())-1

    while True:
        try:    #try sert ici à empecher le programme de s'arreter si le lecteur met une valeur autre que "int" et de lui redemander
            afficherlivres(books)
            livres = int(input("Choisissez le nombre correspondant à un livre déjà lu, ou saisissez le nombre 0 si vous n'avez lu aucun de ces livres \n"))
            while livres != 0:                          #Si l'utilisateur saisi 0, on ne lui demande plus quels livres il a lus
                while livres < 1 or livres > taille:    #On vérifie que le lecteur rentre des données compatibles avec le programme (saisie sécurisée)
                    print(erreur)
                    afficherlivres(books)
                    livres = int(input("Choisissez le nombre correspondant à un livre déjà lu, ou saisissez le nombre 0 si vous n'avez lu aucun de ces livres \n"))
                liste_livres.append(livres)     #On stocke les numéros des livres dans cette liste
                afficherlivres(books)           #Puis on redemande au lecteur le numéro d'un livre qu'il a lu
                livres = int(input("Choisissez le nombre correspondant à un livre déjà lu, ou saisissez le nombre 0 si vous n'avez lu aucun de ces livres \n"))
            break
        except ValueError:
            print(erreur)

    #On enleve les doublons de la liste et transforme ses valeurs en int
    if liste_livres != []:
        lelivres = []
        for i in liste_livres:
            i = str(i)
            if i not in lelivres:
                lelivres.append(i)
    else :
        lelivres = []

    return lelivres

def alleralaligne(n,fichier):
    '''
    Renvoie la ligne "n" du "fichier"
    :param n: int
    :param fichier: fichier txt
    :return: str
    '''
    with open(fichier, "r", encoding='utf-8') as f:
        for i in range(n):
            line = f.readline()
    return line

def pseudoin(fichier,pseudo):
    '''
    Retourne True si le pseudo est dans le fichier, False sinon
    :param fichier: fichier txt
    :param pseudo: str
    :return: bool
    '''
    rep = False
    with open(fichier,"r",encoding='utf-8') as f:
        line = f.readline()
        while line != '':
            liste_tempo = line.split(", ") #on parcours une ligne d'un fichier sous forme de liste
            if pseudo in liste_tempo:      #on cherche le pseudo dans cette liste
                rep = True
            line = f.readline()    #on parcours la prochaine ligne
    return rep

def livrein(books,titre):
    '''
    Retourne True si le titre est dans le fichier books, False sinon
    :param books: fichier txt
    :param titre: str
    :return: bool
    '''
    rep = False
    with open(books, "r", encoding='utf-8') as f:
        line = f.readline()
        while line != '':
            line = line[:-1]    #on enleve le "\n" à la fin de la ligne
            liste_tempo = line.split(" _ ") #on sépare le numéro du livre de son titre
            if titre == liste_tempo[1]:  #on ne regarde que le titre du livre et non son numéro
                rep = True
            line = f.readline()
    return rep

#Fonction du projet
def ajouterlecteur(m,readers,books,booksread):
    '''
    Crée un nouveau profil de lecteur
    :param m: list
    :param readers: fichier txt
    :param books: fichier txt
    :param booksread: fichier txt
    :return: None
    On modifie un fichier, on ne renvoie rien
    '''
    #Messages réutilisables et variables
    erreur = "Réponse invalide, veuillez réessayer"
    genres = "1 - Homme , 2 - Femme , 3 - Autre"
    #pseudo
    pseudo = input("Choisissez un Pseudonyme :\n")
    rep = pseudoin(readers,pseudo)
    if rep == False:
        # genre
        print(genres)
        while True:
            # au cas ou le lecteur ne rentre pas un entier
            try:
                genre = int(input("Choisissez le nombre correspondant à votre genre \n"))
                # au cas ou le lecteur rentre un entier diférent de 1,2 ou 3
                while genre not in [1, 2, 3]:
                    print(erreur)
                    genre = int(input("Choisissez le nombre correspondant à votre genre \n"))
                break
            except ValueError:
                print(erreur)
        # age
        while True:
            # au cas ou le lecteur ne rentre pas un entier
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
        with open(readers, "a",encoding='utf-8') as f:
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

        with open(booksread, "a",encoding='utf-8') as s:
            livreslus = livres_lus(books, erreur)
            s.write(pseudo)
            for i in livreslus:
                s.write(", ")
                s.write(i)
            s.write("\n")

        updateajouterlecteur(m, books) #on update la matrice des notes

    else:
        print("Ce pseudo existe déja.")

def afficherlecteur(readers,books,booksread):
    '''
    Affiche toutes le information du lecteur avec pseudo donné
    :param readers: fichier txt
    :param books: fichier txt
    :param booksread: fichier txt
    :return: None
    On imprime directement le résultat dans la console
    '''
    pseud = input("Saisissez le pseudo du lecteur :\n")
    rep = pseudoin(readers,pseud)
    if rep == True:
        nbligne = 0
        with open(readers, "r") as f: #apres s'être assuré que le pseudo est bien registré, on cherche la ligne ou il se trouve
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


            # on sort les numéros des livres lus par le lecteur, sans le pseudo
            laligne = alleralaligne(nbligne, booksread)
            if laligne[-1:] != "":
                laligne = laligne[:-1]
            laligne = laligne[len(pseud) + 2:]
            laligne = laligne.split(", ")
            lavrailigne = []


            for i in laligne: # convertis la liste "laligne" de str en liste "lavrailigne" de int
                e = int(i)
                lavrailigne.append(e)

            for j in lavrailigne: #affiche le titre des livres lus par le lecteur (sans leurs numéros)
                lelivre = alleralaligne(j, books)
                if j < 10:
                    lelivre = lelivre[4:]
                else:
                    lelivre = lelivre[5:]

                print(lelivre, end="")

    else:
        print("Pseudo non registré")

def modifierlecteur(m,readers,books,booksread):
    '''
    Modifie toutes les informations d'un lecteur
    :param readers: fichier txt
    :param books: fixhier txt
    :param booksread: fichier txt
    :return: None
    On modifie un fichier, on ne renvoie rien
    '''
    pseudo = input("Saisissez le pseudo du lecteur :\n")
    rep = pseudoin(readers,pseudo)
    if rep == True:

        nbligne = 0
        with open(readers, "r",encoding='utf-8') as f:
            ligne = f.readline()
            count = 0
            while ligne != "":
                count += 1
                if pseudo in ligne:
                    nbligne = count
                ligne = f.readline()
        if nbligne != 0:
            # on stocke les lignes avant et après celle que l'utilisateur veut modifier du fichier readers
            with open(readers, "r",encoding='utf-8') as f:
                apres = f.readlines()
                for i in range(nbligne):
                    apres[i] = 0
            with open(readers, "r",encoding='utf-8') as g:
                avant = g.readlines()
                for j in range(nbligne - 1, len(avant)):
                    avant[j] = 0

            # on stocke les lignes avant et après celle que l'utilisateur veut modifier du fichier booksread
            with open(booksread, "r",encoding='utf-8') as f:
                apres2 = f.readlines()
                for i in range(nbligne):
                    apres2[i] = 0
            with open(booksread, "r",encoding='utf-8') as g:
                avant2 = g.readlines()
                for j in range(nbligne - 1, len(avant2)):
                    avant2[j] = 0

            # on écrit les lignes "avant" dans les fichiers readers et booksread, ce qui éface tout le reste
            with open(readers, 'w',encoding='utf-8') as h:
                for i in avant:
                    if i != 0:
                        h.write(i)
            with open(booksread, 'w',encoding='utf-8') as h:
                for i in avant2:
                    if i != 0:
                        h.write(i)

            ajouterlecteur(m,readers,books,booksread)

            # on écrit les lignes "apres" dans les fichiers readers et booksread sans efacer ce qu'il y avait avant
            with open(readers, 'a',encoding='utf-8') as j:
                for i in apres:
                    if i != 0:
                        j.write(i)
            with open(booksread, 'a',encoding='utf-8') as j:
                for i in apres2:
                    if i != 0:
                        j.write(i)

    else:
        print("Pseudo non registré")

def suprimerlecteur(m,readers,booksread):
    '''
    Suprime les informations sur un lecteur
    :param m: list
    :param readers: fichier txt
    :param booksread: fichier txt
    :return: None
    On modifie un fichier, on ne renvoie rien
    '''
    pseudo = input("Saisissez le pseudo du lecteur :\n")
    rep = pseudoin(readers,pseudo)
    if rep == True :
        nbligne = 0
        with open(readers, "r",encoding='utf-8') as f:
            ligne = f.readline()
            count = 0
            while ligne != "":
                count += 1
                if pseudo in ligne:
                    nbligne = count
                ligne = f.readline()
        if nbligne != 0:
            # on stocke les lignes avant et après celle que l'utilisateur veut modifier du fichier readers
            with open(readers, "r",encoding='utf-8') as f:
                apres = f.readlines()
                for i in range(nbligne):
                    apres[i] = 0
            with open(readers, "r",encoding='utf-8') as g:
                avant = g.readlines()
                for j in range(nbligne - 1, len(avant)):
                    avant[j] = 0

            # on stocke les lignes avant et après celle que l'utilisateur veut modifier du fichier booksread
            with open(booksread, "r",encoding='utf-8') as f:
                apres2 = f.readlines()
                for i in range(nbligne):
                    apres2[i] = 0
            with open(booksread, "r",encoding='utf-8') as g:
                avant2 = g.readlines()
                for j in range(nbligne - 1, len(avant2)):
                    avant2[j] = 0

            # on écrit les lignes "avant" dans les fichiers readers et booksread, ce qui éface tout le reste
            with open(readers, 'w',encoding='utf-8') as h:
                for i in avant:
                    if i != 0:
                        h.write(i)
            with open(booksread, 'w',encoding='utf-8') as h:
                for i in avant2:
                    if i != 0:
                        h.write(i)

            # on écrit les lignes "apres" dans les fichiers readers et booksread sans efacer ce qu'il y avait avant
            with open(readers, 'a',encoding='utf-8') as j:
                for i in apres:
                    if i != 0:
                        j.write(i)
            with open(booksread, 'a',encoding='utf-8') as j:
                for i in apres2:
                    if i != 0:
                        j.write(i)

            print("Les information du lecteur : ", pseudo, "on été supprimées.")

        updatesupprimerlecteur(m,nbligne) #on update la matrice des notes

    else:
        print("Pseudo non registré")

def ajouterlivre(m,books,readers):
    '''
    Ajoute un livre à la fin du fichier books si il n'existe pas encore
    :param m: list
    :param books: fichier txt
    :param readers: fichier txt
    :return: None
    On modifie un fichier, on ne renvoie rien
    '''
    titre = input("Saisissez le titre du nouveau livre :\n")
    rep = livrein(books,titre)
    if rep == False:
        with open(books,"r",encoding='utf-8') as f:
            nblignes = len(f.readlines())
        with open(books,"a",encoding='utf-8') as a:
            leligne = str(nblignes) + " _ " + titre + "\n" #on écrit dans le fichier le numéro du livre (num livre précédent + 1) puis le titre
            a.write(leligne)

        updateajouterlivre(m,readers) #on update la matrice des notes
    else:
        print("Ce livre existe déjà.")

def modifierlivre(books):
    '''
    Modifie le titre d'un livre dont on donne le numéro
    :param books: fichier txt
    :return: None
    On modifie un fichier, on ne renvoie rien
    '''
    titre = input("Saisissez le livre que vous voulez modifier:\n")
    rep = livrein(books, titre)
    if rep == True:
        nvtitre = input("Saisissez le titre du nouveau livre:\n")

        with open(books, "r", encoding='utf-8') as f:
            ligne = []
            line = f.readline()
            while line != "":
                line = line[:-1] #on enleve le "\n"
                line = line.split(" _ ") #on sépare le numéro du livre et le titre
                line = line[1:] #on enleve le numéro du livre
                line = line[0] #line est donc simplement le titre en str
                ligne.append(line) #on crée une liste avec tous les titres
                line = f.readline()

            count = 0
            for i in ligne:
                if i == titre:
                    nbligne = count #on trouve la ligne ou se trouve le livre
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

def suprimerlivre(m,books,booksread):
    '''
    Supprime un livre choisis du fichier et décale les numéros des livres
    :param m: list
    :param books: fichier txt
    :param booksread: fixhier txt
    :return: None
    On modifie un fichier, on ne renvoie rien
    '''
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
                ligne.append(line) #comme pour la fonction précédente
                line = f.readline()

        count = 0
        for i in ligne:
            if i == titre:
                nbligne = count #comme pour la fonction précédente
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

        with open(booksread, "r",encoding='utf-8') as f:
            lignes = f.readlines()  #on crée un liste de toutes les lignes du fichier booksread
            for i in lignes:        #puis dans cette liste on supprime les numéros des livres modifiés par le lecteur précédemment
                i = i[:-1]
                l = i.split(', ')
                for j in l:
                    if j != str(nbligne):
                        ligne.append(j)
                listelignes.append(ligne)
                ligne = []

        with open(booksread, "w",encoding='utf-8') as f: #on écrit la liste créée précédemment avec les bonnes ponctuations
            for i in listelignes:
                i = ', '.join(i)
                f.write(i)
                f.write('\n')

        print(titre, " a été supprimé.")

        updatesupprimerlivre(m,nbligne) #on update la matrice des notes

    else:
        print("Ce livre n'est pas registré.")

def affichermatrice(m):
    '''
    Simple affichage de matrice
    :param m: list
    :return: None
    On imprime directement le résultat dans la console
    '''
    for i in m:
        print(i)

def matricedenotes(books,readers):
    '''
    Création d'une matrice (init à 0) en fonction du nombre de livres et lecteurs
    :param books: fichier txt
    :param readers: fichier txt
    :return: list
    '''
    with open(readers, "r",encoding='utf-8') as f: #nb lignes = nb lignes du fichier readers
        ligne = f.readlines()
    with open(books, "r",encoding='utf-8') as f: #nb colonnes = nb lignes du fichier books
        colonnes = f.readlines()
    M=[]
    for i in range(len(ligne)): #on crée une matrice avec les dimensions trouvées qu'on remplit de zeros
        L=[]
        for j in range(len(colonnes)):
            L.append(0)
        M.append(L)
    return M

def notationlivres(m,readers,books,booksread):
    '''
    Ajoute une note dans la matrice
    :param m: list
    :param readers: fichier txt
    :param books: fichier txt
    :param booksread: fichier txt
    :return: None
    On modifie la matrice ou on imprime directement dans la console
    '''
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
                    ligne.append(line) #comme la dernière fois, on crée une liste avec les livres sans leurs numéros
                    line = f.readline()

            count = 0
            for i in ligne:
                if i == titre:
                    nbligne = count  #on cherche la ligne ou se trouve le titre
                count += 1
            nbligne += 1

            with open(booksread, "r",encoding='utf-8') as f: #on cherche la ligne ou se trouve le pseudonyme
                ligne = f.readline()
                count = 0
                while ligne != "":
                    count += 1
                    if pseudonyme in ligne:
                        nbpseudo = count
                    ligne = f.readline()

            rep3 = False
            leligne = alleralaligne(nbpseudo, booksread).split(', ') #leligne est la liste avec les informations du lecteur dans le fichier booksread
            leligne[-1] = leligne[-1][:-1] #on enleve de cette liste le pseudonyme, on a plus que la liste des numéros des livres lus par le lecteur

            for i in leligne:
                if i == str(nbligne): #rep3 = True si le lecteur à déja lu le livre qu'il a donné (il ne doit pas etre capable de noter un livre qu'il n'a pas lu)
                    rep3 = True

            if rep3 == True: # on demande une note entre 1 et 5 au lecteur
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
                m[nbpseudo][nbligne] = note #on écrit la note à la bonne position dans la matrice des notes

            else:
                print("Le lecteur na pas encore lu ce livre")

        else:
            print("Ce livre n'est pas enregistré.")

    else:
        print("Pseudo non registré.")

#fonctions d'update de la matrice
def updateajouterlecteur(m,books):
    '''
    Ajoute une ligne à la matrice quand on ajoute un lecteur
    :param m: list
    :param books: fichier txt
    :return: None
    On modifie la matrice m en ajoutant une ligne à chaque nouveau livre
    '''
    with open(books,"r",encoding='utf-8') as f:
        nblignes = len(f.readlines())
    liste_tempo = []
    for i in range(nblignes):
        liste_tempo.append(0)
    m.append(liste_tempo)

def updatesupprimerlecteur(m,nbligne):
    '''
    Supprime une ligne à la matrice quand on supprime un lecteur
    :param m: list
    :param nbligne: entier
    :return: None
    On supprime une ligne de la matrice m
    '''
    del m[nbligne - 1]

def updateajouterlivre(m,readers):
    '''
    Ajoute une colonne à la matrice quand on ajoute un livre
    :param m: list
    :param readers: fichier txt
    :return: None
    On modifie la matrice m en ajoutant une colonne à chaque nouveau livre
    '''
    with open(readers,"r",encoding='utf-8') as f:
        total = f.readlines()
        nbreaders = len(total)
        for i in range(nbreaders):
            m[i].append(0)

def updatesupprimerlivre(m,nbligne):
    '''
    Supprime dans la matrice la colonne du livre suprimé
    :param m: list
    :param nbligne: entier
    :return: None
    On supprime la colonne correspondant au livre qu'on veut supprimer
    '''
    for i in m:
        del i[nbligne - 1]

#Fonctions pour suggerer livre
def sommelignes(l1,l2,taille):
    '''
    Somme de la multiplication de deux lignes
    :param l1: list
    :param l2: list
    :param taille: entier
    :return: somme: entier
    '''
    somme = 0
    for i in range(taille):
        mult = l1[i] * l2[i]
        somme += mult
    return somme

def sommecarreligne(l):
    '''
    Somme d'une ligne au carré
    :param l:list
    :return: somme: entier
    '''
    lcarre = []
    for i in range(len(l)):
        lcarre.append(l[i]**2)
    somme = 0
    for i in lcarre:
        somme += i
    return somme

def matricesimilirarite(m,readers):
    '''
    Crée la matrice de similarité
    :param m: list
    :param readers: fichier txt
    :return: similariter: list
    '''
    rep = True
    somme = 0
    for i in m:  #on vérifie que dans la matrice on n'ait pas une ligne entière de zeros (division par zero impossible dans la formule)
        for j in i:
            somme += j
        if somme == 0:
            rep = False
        somme = 0
    if rep == True:
        debut = time()
        with open(readers, "r",encoding='utf-8') as f:
            taille = len(f.readlines())
        similarite = []
        liste_tempo = []
        for x in range(taille):
            for y in range(taille):
                if x == y:
                    liste_tempo.append(1)
                else:
                    val = sommelignes(m[x], m[y], taille) / (sqrt(sommecarreligne(m[x])) * sqrt(sommecarreligne(m[y]))) #formule de similarité de cosinus
                    val = round(val, 2) #on arrondit la valeur obtenue à 2 chiffres après la virgule
                    liste_tempo.append(val) #on remplit une ligne de la matrice de similarité
            similarite.append(liste_tempo)  #on remplit la matrice de similarité avec cette ligne
            liste_tempo = []

        fin = time()
        temps = (fin-debut) * 1000
        print("La matrice de similarite à été calculée en",round(temps),"mili secondes") #on affiche le temps écoulé pendant le calcul de la matrice

        return similarite
    else:
        return False

def suggererlivre(m,readers,books,booksread):
    '''
    Suggère à un lecteur, les livres qu'il na pas encore lu qui pourraient lui plaire (lus par le lecteur le plus similaire)
    :param m: list
    :param readers: fichier txt
    :param books: fichier txt
    :param booksread: fichier txt
    :return: None
    On affiche directement dans la console quel livre pourrait plaire à l'utilisateur
    '''
    pseudo = input("Saisissez le pseudo du lecteur :\n")
    rep = pseudoin(readers, pseudo)
    if rep == True:
        similarite = matricesimilirarite(m, readers)
        if similarite == False:
            print("Un lecteur n'a encore noté aucun livre.") #si une ligne de la matrice des notes n'a pas encore de notes, on ne peut pas calculer la matrice de similarité
        else:
            nbligne = 0
            with open(readers, "r",encoding='utf-8') as f:
                ligne = f.readline()
                count = 0
                while ligne != "":
                    count += 1
                    if pseudo in ligne:
                        nbligne = count
                    ligne = f.readline()
            nbligne -= 1

            max = 0
            for i in similarite[nbligne]: #on cherche dans la matrice de similarité, dans la ligne correspondante au lecteur, le valeur la plus haute et différente de 1 (1 = lui même)
                if i != 1:
                    if i > max:
                        max = i
            count = 0
            for i in similarite[nbligne]: #on cherche la ligne/colonne du lecteur le plus similaire
                if i == max:
                    lignedesimilarite = count
                count += 1

            lignedesimilarite += 1
            nbligne += 1

            livressimilaires = alleralaligne(lignedesimilarite, booksread)[:-1]
            livressimilaires = livressimilaires.split(', ')[1:] #liste avec les livres lus par le lecteur similaire
            livreslecteur = alleralaligne(nbligne, booksread)[:-1]
            livreslecteur = livreslecteur.split(', ')[1:] #liste avec les livres lus par le lecteur lui même


            suggestion = []
            for i in livressimilaires:
                if i not in livreslecteur:
                    suggestion.append(i) #on crée la liste des livres lus par le lecteur similaire mais pas lus par le lecteur lui même

            if suggestion == []: #si le lecteur a lu tous les livres du lecteur similaire on ne peut lui conseille aucun livre
                print("Vous avez lus tous les livres qui pourraient vous plaire dans nos registres. N'hésitez pas à ajouter des nouveaux livres à nos registres et à noter d'autres livres pour améliorer nos suggestions.")
            else:
                suggestionfinale = []
                for i in suggestion:
                    suggestionfinale.append(alleralaligne(int(i), books)[:-1])
                for i in suggestionfinale:
                    print("Le livre : ", i ,", pourrais vous plaire.")  #on affiche le numéro et le titre du livre qu'on suggère au lecteur



                while True:  # selection est le numéro du livre que le lecteur vas lire ensuite
                    try:
                        selection = int(input("Saisissez le numéro du livre parmis ceux-là que vous allez lire en premier. Saisissez 0 si vous ne comptez pas les lire.\n"))
                        while str(selection) not in suggestion and selection != 0:
                            print("Réponse invalide.")
                            selection = int(input("Saisissez le numéro du livre parmis ceux-là que vous allez lire en premier. Saisissez 0 si vous ne comptez pas les lire.\n"))
                        break
                    except ValueError:
                        print("Réponse invalide.")

                if selection == 0:
                    print("Si vous voulez de meilleures suggestions, n'hésitez pas à noter les livres que vous avez lus.")
                else:
                    # On crée une liste qui stocke toutes les informations de booksread
                    with open(booksread, "r", encoding='utf-8') as f:
                        livreslus = []
                        line = f.readline()[:-1]
                        while line != "":
                            line = line.split(", ")
                            livreslus.append(line)
                            line = f.readline()[:-1]
                        livreslus[nbligne - 1].append(str(selection))

                    with open(booksread, "w",
                              encoding='utf-8') as f:  # on réecrit cette liste dans le fichier booksread en ajoutant le livre à la ligne du lecteur
                        for i in livreslus:
                            w = ', '.join(i)
                            f.write(w + '\n')

                    noter = input("Voulez vous noter le livre que vous avez choisis ?\nRépondez par oui ou non\n")
                    while noter.lower() not in ["oui", "non"]:
                        print("Réponse invalide.")
                        noter = input("Voulez vous noter le livre que vous avez choisis ?\nRépondez par oui ou non\n")

                    if noter.lower() == "oui":
                        while True:
                            try:
                                note = int(input("Donnez une note entre 1 et 5 à ce livre :\n1 : Vous n'avez pas aimé le livre\n5 : Vous adorez le livre\n"))
                                while note < 1 or note > 5:
                                    print("Votre réponse est invalide. Donnez une note entre 1 et 5")
                                    note = int(input("Donnez une note entre 1 et 5 à ce livre :\n1 : Vous n'avez pas aimé le livre\n5 : Vous adorez le livre\n"))
                                break
                            except ValueError:
                                print("Réponse invalide")

                        m[nbligne - 1][selection - 1] = note
                        print("La note a bien été enregistrée.\n")

                    else:
                        print("Pensez à noter les livres quand vous les finissez pour que nos suggestions soient plus précises.")

    else:
        print("Pseudo non registré")

def main(m,books,booksread,readers):
    '''
    Fonction qui lance le menu et permet à l'utilisateur d'utiliser toutes les fonctions que nous avons construit précédement
    :param m: list
    :param books: fichier txt
    :param booksread: fichier txt
    :param readers: fichier txt
    :return: None
    On affiche un menu dans la console, on ne renvoie rien
    '''
    erreur = "Réponse invalide.\n"
    while True:
        try :
            options = int(input("Que voulez vous faire \n1 : Profils des lecteurs\n2 : Visiter le dépôt des livres\n3 : Recommandation\n4 : Sortir\n"))
            while options not in [1, 2, 3, 4]:
                print(erreur)
                options = int(input("Que voulez vous faire \n1 : Profils des lecteurs\n2 : Visiter le dépôt des livres\n3 : Recommandation\n4 : Sortir\n"))
            break
        except ValueError:
            print(erreur)

    if options == 1:
        while True:
            try :
                optionslecteur = int(input("Que voulez vous faire :\n1 : Ajouter lecteur\n2 : Afficher lecteur\n3 : Modifier lecteur\n4 : Supprimer lecteur\n5 : Revenir en arrière\n"))
                while optionslecteur not in [1, 2, 3, 4, 5]:
                    print(erreur)
                    optionslecteur = int(input("Que voulez vous faire :\n1 : Ajouter lecteur\n2 : Afficher lecteur\n3 : Modifier lecteur\n4 : Supprimer lecteur\n5 : Revenir en arrière\n"))
                break
            except ValueError:
                print(erreur)

        if optionslecteur == 1:
            ajouterlecteur(m,readers, books, booksread)
            print()
            print()
            main(m,books,booksread,readers)
        elif optionslecteur == 2:
            afficherlecteur(readers,books,booksread)
            print()
            print()
            main(m,books,booksread,readers)
        elif optionslecteur == 3:
            modifierlecteur(m,readers,books,booksread)
            print()
            print()
            main(m, books, booksread, readers)
        elif optionslecteur == 4:
            suprimerlecteur(m,readers,booksread)
            print()
            print()
            main(m, books, booksread, readers)
        elif optionslecteur == 5:
            print()
            print()
            main(m,books,booksread,readers)

    elif options == 2:
        while True:
            try :
                optionslivres = int(input("Que voulez vous faire :\n1 : Afficher tous les livres\n2 : Ajouter un livre\n3 : Modifier un livre\n4 : Supprimer un livre\n5 : Revenir en arrière\n"))
                while optionslivres not in [1,2,3,4,5]:
                    print(erreur)
                    optionslivres = int(input("Que voulez vous faire :\n1 : Afficher tous les livres\n2 : Ajouter un livre\n3 : Modifier un livre\n4 : Supprimer un livre\n5 : Revenir en arrière\n"))
                break
            except ValueError:
                print(erreur)
        if optionslivres == 1:
            afficherlivres(books)
            print()
            print()
            main(m, books, booksread, readers)
        elif optionslivres == 2:
            ajouterlivre(m,books,readers)
            print()
            print()
            main(m, books, booksread, readers)
        elif optionslivres == 3:
            modifierlivre(books)
            print()
            print()
            main(m, books, booksread, readers)
        elif optionslivres == 4:
            suprimerlivre(m,books,booksread)
            print()
            print()
            main(m, books, booksread, readers)
        elif optionslivres == 5:
            print()
            print()
            main(m, books, booksread, readers)

    elif options == 3:
        while True:
            try :
                optionrecomendation = int(input("Que voulez vous faire :\n1 : Afficher la matrice des notes\n2 : Ajouter une note à un livre\n3 : Suggérer un livre\n4 : Revenir en arrière\n"))
                while optionrecomendation not in [1,2,3,4]:
                    print(erreur)
                    optionrecomendation = int(input("Que voulez vous faire :\n1 : Afficher la matrice des notes\n2 : Ajouter une note à un livre\n3 : Suggérer un livre\n4 : Revenir en arrière\n"))
                break
            except ValueError:
                print(erreur)

        if optionrecomendation == 1:
            affichermatrice(m)
            print()
            print()
            main(m, books, booksread, readers)
        elif optionrecomendation == 2:
            notationlivres(m,readers,books,booksread)
            print()
            print()
            main(m, books, booksread, readers)
        elif optionrecomendation == 3:
            suggererlivre(m,readers,books,booksread)
            print()
            print()
            main(m, books, booksread, readers)
        elif optionrecomendation == 4:
            print()
            print()
            main(m, books, booksread, readers)

    elif options == 4:
        while True:
            try :
                sortir = int(input("Etes vous sur de vouloir sortir :\n1 : Oui\n2 : Non\n"))
                while sortir not in [1, 2]:
                    print(erreur)
                    sortir = int(input("Etes vous sur de vouloir sortir :\n1 : Oui\n2 : Non\n"))
                break
            except ValueError:
                print(erreur)

        if sortir == 1:
            print("Au revoir !\n")
        elif sortir == 2:
            print()
            print()
            main(m, books, booksread, readers)