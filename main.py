#Programme principal

#imports
from functions import *

#variables
books = "C:/Users/Fabio Malta/PycharmProjects/SpringFsm/books.txt"
booksread = "C:/Users/Fabio Malta/PycharmProjects/SpringFsm/booksread.txt"
readers = "C:/Users/Fabio Malta/PycharmProjects/SpringFsm/readers.txt"

#Début

print("Début du programme.\n")
m = matricedenotes(books,readers)
main(m,books,booksread,readers)

#Fin