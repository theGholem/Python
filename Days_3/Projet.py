# Notre application doit fonctionner comme suit :

# L’utilisateur doit recevoir trois invites lui demandant de fournir différentes 
# informations sur un employé. Une invite doit demander le nom de l’employé, une autre 
# doit demander son salaire horaire, et la dernière doit demander combien d’heures 
# l’employé a travaillé cette semaine.
# Le nom de l’employé doit être traité pour s’assurer qu’il est dans un format 
# particulier. Tous les noms d’employés doivent être dépourvus de tout espace blanc 
# superflu et doivent être en majuscules. Cela signifie que chaque mot a sa première 
# lettre en majuscule et que toutes les autres lettres sont en minuscules. Par exemple, 
# si l’employeur a accidentellement activé le verrouillage des majuscules et qu’il 
#écrit "rEGINA gEORGE", le nom sera quand même correctement enregistré sous la 
# forme « Regina George ».
# La rémunération totale de l’employé pour la semaine doit être calculée en multipliant 
# les heures travaillées par son salaire horaire.
# Rappelle-toi que toute entrée utilisateur que nous recevons sera une chaîne de 
# caractères. Bien que nous puissions multiplier des chaînes de caractères, cela ne 
# donnera pas tout à fait ce que tu veux dans ce cas. Il est également utile de garder 
# à l’esprit que le salaire de l’employé, ou le nombre d’heures travaillées, peut ne pas 
# être un nombre entier.
# Après avoir traité le nom de l’employé et calculé son salaire pour la semaine, le 
# programme doit afficher ces informations sous la forme d’une chaîne unique. 
# Par exemple, une sortie comme celle-ci serait appropriée :
# -->Regina George a gagné 800 € cette semaine.

name=input("saisir le nom de l'employé : ")
name=name.title().strip() # va respecter les majuscules en debut de nom et retirer les spaces

salaireByHour=input("Saisir le salaire que gagne l'employé par heure : ")

workHour=input("Saisir le nombre d'heure travaillé par l'employé : ")

# puisque nos variables enregistre toutes les saisies en str, alors si on veux
# les multiplier, il faut les convertir en entier ou float
totalPaid=float(salaireByHour)*float(workHour)

print(f"{name} a gagné {totalPaid} $ cette semaine")


