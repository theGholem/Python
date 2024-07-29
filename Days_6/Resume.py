# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:47:29 2024

@author: Konan
"""

# boucle for
print("\n___Boucle for___\n")

# par exemple, on peut afficher tous les elements d'une liste

print("\n___Avec une liste\n___")

array=[0,1,2,3]

for i in array : #ici le compteur 'i' parcourt toute la liste et imprime les elements qu'il rencontre
    print(i)

print("\n___Avec une liste de tuple c'est pareil___\n")

array=[
    (1,2,3),
    ("a","b","c"),
    (1,"2",3)
]

for cpt in array :
    print(cpt) # va afficher nos 3 tuples, car ce sont nos 3 elements

print("\n")
# maintenant si on aimerais lister un element precis de nos tuples, 

for cpt in array :
    print(cpt[0]) # ici il va recuperer tous les elements qui se trouve a la position 0 dans nos tuples

print("\n")
# si on veut pas tous les elements a la position 0 mais plutot un seul elements

for cpt in array :
    print(cpt[2]) # ici il va recuperer tous les elements qui se trouve a la position 2 (soit la derniere) dans nos tuples

print("\n___Autre exemple___\n")
# liste de tuple
movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

# on veut afficher les titres des films
for title in movies :
    print("title : ", title[0])
print("\n")
# on veut afficher les dates de parution
for releaseDate in movies :
    print("Date de parution : ", releaseDate[2])
print("\n")
# on veut afficher les noms des realisateurs
for realisatorName in movies :
    print("Nom du realisateur : ", realisatorName[1])
print("\n")
# on veut afficher les titres, les dates et les realisateurs ensemble :
for globalInformation in movies :
    print(globalInformation[0]," (",globalInformation[2],") ; realisé par : ",globalInformation[1])
print("\n")
# avec un f-string :
for globalInformation in movies :
    print(f"{globalInformation[0]} ({globalInformation[2]}); realisé par {globalInformation[1]}")

print("\n__Utilisation de 'break'___\n")
# on l utilise toujours avec une condition afin de ne pas bloquer le code des le debut
# break peut nous permettre de retrouver par exemple un element dans une liste. En effet, lorsque on parcourt notre boucle et que on retrouve 
# l'element(condition respecté), alors la bloucle s'arrete automatiquement et on passe au code suivant

# par exemple dans notre liste de film on a "Memento", et on va essayer de le retrouver

for findMovie in movies :
    if findMovie[0]=="Memento" :  # ici movies[0] parcourt tous les films et lorsqu'il retrouve Momento, il break
        # si le titre est Momento, informer l'utilisateur
        print("'Momento' est bien dans vos favoris")
        break # notre boucle n'evolue plu. On stop ici
    # si notre condition est respecté, alors tous ce qui est dans la condition sera executé avant le break

print("\n___La foncion range____\n")

# range(a, b, c) ; avec 'a' le point de depart(par defaut=0), 'b' le point d'arrivé, et 'c' le pas(et par deafaut=1)
# [a, b[, cad 'a' inclut et 'b' non inclut(soit 'b-1' inclut)

# range(0, 10, 2)  --> 0, 2, 4, 6, 8
# range(2, 10, 3)  --> 2, 5, 8

# nous pouvons egalement specifier le pas avec une valeur negative. Cela signifie que on evolut dans le sens contraire
# de la plus grande valeur à la plus petite

# range(depart, arrivé, pas+), et si pas<0 --> range(arrivé, depart, pas-)
# range(1, 12, -2) --> donne rien
# range(12, 1, -2) --> 12, 11, 9, 7, 5, 3, 1 

# en utilisant la fonction range(a, b, b), les valeurs ne seront pas visible. Pour les voir, il faudra utiliser 
# les fonction 'list' pour afficher les valeurs sous forme de liste et 'tuple' pour afficher les valeurs sous forme de tuple

print(range(10)) # cela va afficher juste range(0, 10) mais pas les valeurs
print("\nlist\n")
print(list(range(0, 10))) # cela va afficher une liste de valeur de 0 à (10-1)=9 separé de 1 en 1
print(list(range(3, 12, 2))) # cela va afficher une liste de valeur de 3 à (12-1)=11 separé de 2 en 2

print("\ntuple\n")
print(tuple(range(0, 10))) # cela va afficher un tuple de valeur de 0 à (10-1)=9 separé de 1 en 1
print(tuple(range(3, 12, 2))) # cela va afficher un tuple de valeur de 3 à (12-1)=11 separé de 2 en 2
print("list-tuple\n")
print(list(range(10, 1, -1))) # cela affiche une liste de valeur des nombre de 10 à 1 dans le sens decroissant et de 1 en 1
print(tuple(range(10, 1, -1))) # cela affiche un tuple de valeur des nombre de 10 à 1 dans le sens decroissant et de 1 en 1

print("\nLes nombres paire de 0 à 50 sous forme de list : ")
# par exemple si on veux afficher tous les nombre paire de 0 à 50 
number=list(range(0, 51, 2))
print(number)

print("\nLes nombres paire de 0 à 50 sous forme de tuple : ")
number=tuple(range(0, 51, 2))
print(number)

# Use range in for 
print("\n__Utilisation de range dans la boucle for__\n")

for number in range(11) :
    print(number)

print("\n")

for number in range(11) :
    print("hello") # on remarque la variable 'number', n'a pas été utilisé dans la boucle. Mais c'est grace a elle que 'hello' s'affiche 10 fois

# au lieu de declarer dans la boucle une variable qui ne sera jamais utilisé dans le corps de la boucle, on peut utiliser la notation : "_"
# cette notation indique une variable non utilisé
print("\nNotation '_' :\n")
for _ in range(10) :
    print(_) # ici va afficher les 10 elements

print("\n")

for _ in range(10) :
    print("hello world !")

# mais il es toujours preferable de nommer les variables de facon intuitive
