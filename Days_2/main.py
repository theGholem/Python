# 1- Demande à l’utilisateur son nom et son âge, attribue ces valeurs à deux variables, puis imprime-les.

# 2- Cherche à savoir ce qui se passe lorsque tu essayes d’attribuer une valeur à une variable que tu as déjà définie. Essaye d’imprimer la variable avant et après avoir réutilisé le nom.

# 3- Correct the following code : 
#  hourly_wage = input("Veuillez saisir votre salaire horaire : ')
#  prnt("Salaire horaire : ")
#  print(hourlywage)
#  print("Heures travaillées : ")
#  print(hours_worked)
#  hours_worked = input("Combien d'heures avez-vous travaillé cette semaine ? ")
 
# 1.
print('\n1. \n')
name=input('What is your name?\n')
old=input('How old are you?\n')

print('Great, your name is ' + name + ' and your age is '+ old)

# 2.
print('\n2. \n')
name1='India' # at the beginnnig
print(name1)
name1='Pakistan' # replace first name by second name
print(name1) # we get a new name

# 3.
print('\n3. \n')
hourly_wage = input("Veuillez saisir votre salaire horaire : ")
print("Salaire horaire : ")
print(hourly_wage)

hours_worked = input("Combien d'heures avez-vous travaillé cette semaine ? ")
print("Heures travaillées : ")
print(hours_worked)
