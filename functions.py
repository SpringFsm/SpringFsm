#Programme contenant les fonctions à utiliser dans le programme principal

#imports

#imports

#Début

def afficherlivres():
    with open("C:/Users/Fabio Malta/PycharmProjects/projetPython1/books.txt", "r") as f:
        for ligne in f:
            print(ligne)

def ajoutelecteur():
    #Messages réutilisables et variables
    erreur = "Réponse invalide, veuillez réessayer"
    genres = "1 - Masculin , 2 - Féminin , 3 - Autre"
    ages =""
    #pseudo
    pseudo = input("Choisissez un Pseudonyme :\n")
    #genre
    print(genres)
    while True :
        #au cas ou il ne mette pas un entier
        try :
            genre = int(input("Choisissez le nombre correspondant à votre genre \n"))
            #au cas ou il mette un entier diférent de 1,2 ou 3
            while genre not in [1,2,3]:
                print(erreur)
                genre = int(input("Choisissez le nombre correspondant à votre genre \n"))
            break
        except ValueError:
            print(erreur)
    #age
    while True :
        #au cas ou il ne mette pas un entier
        try :
            age = int(input("Quel âge avez vous ? \n"))
            break
        except ValueError:
            print(erreur)
    if age <= 18 :
        #age inférieur ou égal à 18 ans : 1
        age = 1
    elif age > 25 :
        #age supérieur à 25 ans : 3
        age = 3
    else:
        #age entre 18 et 25 and : 2
        age = 2
    #style
    while True:
        try :
            style = int(input("Choisissez le nombre correspondant à votre style de lecture \n"))
            while style < 1 or style > 7:
                afficher_styles()
                style = int(input("Choisissez le nombre correspondant à votre style de lecture \n"))
            break
        except ValueError:
            print(erreur)



    print(pseudo,genre,age,style)


def afficher_styles():
    styles = ["1-Science-fiction", "2-Biographie,", "3-Horreur", "4-Romance", "5-Fable", "6-Histoire", "7-Comédie"]
    for i in styles:
        print(i)

