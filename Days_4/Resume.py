
tab=["anne",34.6,"gregoire","nicapole"]

#pour afficher la liste
print(tab)
#pour afficher le 2 eme element de la liste (indice 1)
print(tab[1])
#pour afficher le dernier element de la liste
print(tab[-1])
#pour afficher "gregoire"
print(tab[2])

# .append(i) permet d ajouter un element en derniere position dans notre liste
tab.append("Simon")
print(tab) # on aura egalement Simon qui sera ajouté en dernier 
# on peut utiliser l'operateur +
print(tab+["leon",12]) # affiche une nouvelle liste avec ces deux elements en plus
print(tab) # la valeur de notre liste reste inchangé pour l'instant
# si on veut inserer un element a une position specifique 
#on utilise .insert(index, element)
num=[1,2,4,5] 
num.insert(2, 3) # insert 3 a la position 2
print(num)

#pour supprimer un element de la liste
tab.remove(34.6) # retire un element en fonction de son nom
print(tab)# retire 34.6 de la liste tab
del tab[-1] # retire un element en fonction de sa position
print(tab) # retire simon
tab.pop() # par defaut retire le dernier element de la liste
print(tab) #retire nicapole
#revenons une liste normale
tab=tab+["leonard",20.08,"raphael"]
print(tab)
# on peut preciser un indexe pour pop afin de supprimer un elt a une position precise
tab.pop(2) # retire leonard
print(tab)
# '.clear()' permet de supprimer tous ce qui se trouve dans la liste
tab.clear()
print("Reinitialisation de la liste ",tab)

#Les tuples
# exemple de tuple :
tab2=("moore","beltic","celtique") # tab2="moore","beltic","celtique"
print(tab2)
#tuple a l'interieur d une liste 
#toutes les propriétés des liste s'appliquent aux tuples sauf que les tuples sont
#des valeurs imuable. On ne peux plus les modifier une fois qu on les a definis.
#On ne peut donc utiliser les methodes tel que pop(), append(), ou encore del tab[i]
tab2=["elene",
      ("sadi",1998),
      ("kadi",20.05),
      "hygar",
      (23,24,25)]
print(tab2)
#si on veux recuper des elements dans notre liste 
print(tab2[1])# nous affiche le 1er tuple
#si on veut recuperer la date de sadi dans le 1er tuple, on joue avec les index
print(tab2[1][1]) #affiche 1998
#si on veut recuperer 24 dans le dernier tuple
print(tab2[4][1]) # affiche 24