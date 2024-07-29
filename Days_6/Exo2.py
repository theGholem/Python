# ENONCE :

# Vous avez une liste de tuples contenant des informations sur les produits vendus dans un magasin. Chaque tuple contient le nom du produit, 
# la quantité vendue et le prix unitaire. Vous devez accomplir les tâches suivantes :

#    1- Imprimer le montant total des ventes pour chaque produit dans un format agréable et lisible.
#    2- Calculer la moyenne des prix unitaires de tous les produits.
#    3- Imprimer les produits dont le prix unitaire est supérieur à la moyenne calculée.

# DONNÉES :

# products = [
#    ("Pommes", 50, 0.75),
#    ("Bananes", 30, 0.50),
#    ("Cerises", 20, 1.25),
#    ("Dattes", 15, 1.75)
# ]

# Exemple de Sortie Attendue :

    #Montant total des ventes pour chaque produit :

#Pommes: 37.50 $
#Bananes: 15.00 $
#Cerises: 25.00 $
#Dattes: 26.25 $

    #Produits avec un prix unitaire supérieur à la moyenne :


# La moyenne des prix unitaires est 1.06 $
# Produits avec un prix unitaire supérieur à la moyenne :
# Cerises: 1.25 $
# Dattes: 1.75 $

products = [
    ("Pommes", 50, 0.75),
    ("Bananes", 30, 0.50),
    ("Cerises", 20, 1.25),
    ("Dattes", 15, 1.75)
]

# 1. montant total des ventes pour chaque produit dans un format agréable et lisible
# le cas de la pomme : on a 50 pommes qui ont été vendus a 0.75, soit un montant total de 0.75*50

for product in products :
    total_sale=product[1]*product[2]
    print(f"{product[0]} : {total_sale:.2f} $")


# 2. moyenne des prix unitaires de tous les produits.

total_product=0
number_product=len(products)

for product in products :
    total_product+=product[2]    

average_rate=total_product/number_product

print(f"la moyenne des prix unitaires est : {average_rate:.2f}")


# 3. Imprimer les produits dont le prix unitaire est supérieur à la moyenne calculée

for product in products :
    if product[2] > average_rate :
        print(f"{product[0]} : {product[2]:.2f} $")


# remark : je trouve qu'il est plus optimal d'utiliser les indexes et declarer qu'une seule variable dans notre boucle