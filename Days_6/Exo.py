# ENONCÉ:

# 1) Nous avons fourni ci-dessous une liste de tuples, où chaque tuple contient des détails sur un employé d’un 
#    magasin : son nom, le nombre d’heures travaillées la semaine dernière et son taux horaire. Imprime le montant 
#    que chaque employé doit recevoir à la fin de la semaine dans un format agréable et lisible.

# employees = [
#   ("Antoine Renard", 35, 8.75),
#   ("Anne Chardy", 30, 12.50),
#   ("Charlie Lee", 50, 15.50),
#   ("Lennie Smith", 20, 7.00)
#     ]

# 2) Pour les employés ci-dessus, imprime ceux qui gagnent un salaire horaire supérieur à la moyenne.

# Conseil : tu peux utiliser une boucle for et deux variables pour garder la trace du salaire total et du nombre d’employés. 
# Ensuite, utilise ces deux variables pour calculer la moyenne. Enfin, ajoute une autre boucle qui parcourt à nouveau la liste 
# des employés et n’imprime que ceux dont le salaire horaire est supérieur à la moyenne calculée.

employees = [

    ("Antoine Renard", 35, 8.75),
    ("Anne Chardy", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Lennie Smith", 20, 7.00)

]

print(f"\n")
# 1. Calcul et affichage du montant que chaque employé doit recevoir

# name : 1ere ligne  --> cpt[0]
# hours : 2eme ligne --> cpt[1]
# rate : 3eme ligne  --> cpt[2]

for name, hours, rate in employees :                  # j aurais pu utiliser une seule variable, mais dans ce cas, j'aurais utilisé les notation des position [n]
    salary=hours*rate
    print(f"{name} doit recevoir : {salary:.2f} $ pour sa derniere semaine") # x:.nf signifie que la variable x va prendre un float de 2 chiffres apres la virgule

# calcul de la moyenne du salaire horaire

total_salary= 0                                       # initialement a 0
num_employees= len(employees)                         # grace a la fonction len on peut compter le nombre d'employé de la liste
 
for _, _, rate in employees :                         # name, hours n'ont pas été utilisé dans le bloc de la boucle, donc on a preferé utilisé le symbole '_'
    total_salary+=rate

average_rate=total_salary/num_employees               # on sort de la boucle et on peut appliquer simplement notre formule

# affichage du salaire horaire moyen
print(f"\nle salaire horaire moyen est : {average_rate:.2f} $/heure")  

print(f"\n")
# 2. Affichage des employés dont le salaire horaire est supérieur à la moyenne

for name, _, rate in employees :                      # on a pas eu besoin d'utiliser la variable hours dans notre bloc
    if rate > average_rate :
        print(f"{name} à un salaire horaire superieur à la moyenne({rate:.2f} $/heure)")   

                

