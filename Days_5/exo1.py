# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 13:21:32 2024

@author: Konan
"""

# 1) Essaye d’approcher le comportement de l’opérateur is en utilisant ==. 
# Rappelle-toi que nous disposons de la fonction id pour trouver l’adresse mémoire 
# d’une valeur donnée, et que nous pouvons comparer les adresses mémoire pour 
# vérifier l’identité.

# 1) Essaye d’utiliser l’opérateur is ou la fonction id pour étudier la différence 
# entre les deux :

# numbers = [1, 2, 3, 4]
# new_numbers = numbers + [5]

# Et ça :
    
# numbers = [1, 2, 3, 4]
# numbers.append(5)
# Est-ce que new_numbers et numbers sont la même chose ? Qu’en est-il de numbers 
# avant et après l’ajout de 5 ?

# 2) Demande à l’utilisateur de saisir un nombre. Indique à l’utilisateur si le 
#    nombre est positif, négatif ou nul.

# 3) Écris un programme pour déterminer si des heures supplémentaires sont dues 
#    à un employé. Tu dois demander à l’utilisateur combien d’heures l’employé a 
#    travaillé cette semaine, ainsi que le salaire horaire de cet employé.

# Si l’employé a travaillé plus de 40 heures, tu dois imprimer un message indiquant 
# que l’employé doit recevoir une rémunération supplémentaire, ainsi que le montant dû. 
# Le montant supplémentaire dû est de 10% du salaire horaire de l’employé pour chaque 
# heure travaillée au-delà des 40 heures. En fait, les employés sont payés 110% de 
# leur salaire horaire pour toute heure supplémentaire.

# 1.
print("\n___1___\n")
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

print(new_numbers) # il possede une tout autre id

print(id(numbers))
print(id(new_numbers)) # les 2 id differents, donc il y a difference

print(numbers is new_numbers) # false, d'ou il y a difference

numbers = [1, 2, 3, 4]
numbers.append(5)

print(numbers)
print(id(numbers))
print(id(new_numbers)) # id differente, donc les 2 ne sont pas identique


print(numbers is not new_numbers) # true, ce qui confirme la difference


# 2.
print("\n___2___\n")
number_random=input("print an number please\n")
number_random=float(number_random)

if number_random > 0 :
    print("Your number is positive")
elif number_random == 0 :
    print(str(number_random)+" is not evaluable.") # str(number_random)," is not evaluable."
else :
    print("Your number is negative")


# 3. 
print("\n___3___\n")

worked_hours=input("Print how many hours your employe has working this week : \n")
paid_by_hours=input("how many $ your employe get by hour ?\n")

worked_hours=float(worked_hours)
paid_by_hours=float(paid_by_hours)

if worked_hours > 40 :
    print("your employe need to get : ",worked_hours*paid_by_hours ," $ " )
    extra_paid=(worked_hours*paid_by_hours) + (10/100)*(worked_hours-40) 
    print("Because his work more than 40h, he will get extra paid : ",extra_paid," $")
else :
    print("Employe's paid for this week is ", paid_by_hours*worked_hours," $")
    



