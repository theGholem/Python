# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 11:03:09 2024

@author: Konan
"""

name="hello"
print(bool(name)) # permet d'evaluer l'expression en parametre 
# tous ce qui es vide est false, tandis que tous ce qui n'est pas vide est true
print("\n")

print(bool(0)) # is False
print(bool(1)) # is True

print(bool("")) # is False
print(bool("Dutexte")) #is True

print(bool([])) # is False
print(bool([1,"deux"])) # is True

print(bool(False)) # is False
print(bool(True)) # is True


# avec des valeurs
print("\navec des valeurs\n")

print(1=="1") # false
print("1"==" 1") # false(ya un nespace de trop)
print("1"=="1") # true
print(23<29) # true
print(23>29) # false
print(23<=23) # true
print(23>=23) # true
print(23!=29) # true 
print([1,2,3]==(1,2,3)) # false
print((1,2,3)==(1,2,3)) # true
print((1,2,9)==(1,2,3)) # false
print((1,2,3,"n")==(1,2,3)) # false

# Dans le code ASCII, tous les caracteres ont une valeur numerique 
# par exemple A=65 et a=97
print("A"<"a") # is true

# is/is not
print("\nis/is not\n")

a=[1,2,3]
b=[1,2,3]

print(id(a)) 
print(id(b)) # a et b on des differents id, 

# En fait "is" verifie si les deux objet sont tocké de la meme facon en memoire

# on utilise "id" pour verifier l'emplacement(id) d'une variable 

print(a==b) # true
print(a is b) # false

# is not est juste la reciproque 
print(a is not b) # true

b=a # permutation

print(id(a))
print(id(b)) # a et b ont exactement les memes id, d'ou ils sont exactemrnt identique
print(a is b) # true , car b a pris exactement la place de a de maniere a avoir les memes id
print(a is not b) # false

# Condition
print("\nCondition\n")

your_age=input("print your age please\n")
your_age=int(your_age) # conversion en entier

if your_age < 16 : 
    print(" Your bill  will be 1 $")
elif your_age >= 60 :
    print("Your are an senior. Is free for you!")
elif 16 <= your_age < 60 :
    print("You must by a regular price please")
else :          # ici le else ne sera jamais appelé
    print("you don't print your true old.")

# remark: la saisie du user est toujours un str. Donc si on dois faire des comparaison
#         avec des entiers,soit on convertir en str ces entiers, ou la variable en entier 

# on peut verifier les valeur de verité des expressions.
# en effet, on sait que lorsque une variable est vide, is false, et sinon is true

name=input("\nPrint your name dude\n")

if name :
    print("Vous avez bien saisi : "+name)
else :
    print("Dude, you don't write anythings") # puisque quand c est vide, c est faux
    
# c est aussi possible d'utiliser "or"(pour ou) et " and"(pout et) dans nos conditions
print("\n")

n1=23
n2=20
n3=10

if n1 >50 and n2 <50:
    print("The both is goood") # false(f and t == true=false)
elif n1 == 30 or n1 < 50:
    print("is not bad") # true(f or t == true) ; celui qui sera affiché
elif n1 == 23 and n3 ==10:
    print("is good") # true(t and t == true)
    
# on affiche le premier true 
    
    
    
    
    
    