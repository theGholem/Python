# on ne peut pas concatener une str avec un int

# n=12
# print("Hello"+n) --> error 
# print("Hello", n)--> Hello 12

# n='12'
# print("hello"+n) --> hello 12

# Donc si on veut associer une str avec un int, on utilise une virgule(,)
# Par contre si on utilise (+), on associe que str+str

# n=12 -->produit une errreur , faut la convertir en entier
# n=str(12)
# print("Mon age est : "+n)

# Si je veux convertir str en entier
# n2="18"
# n2=int("18") #-->Conversion
# print(n2)

# Avec un nombre flottant
# n3="19.8"
# print(n3)
# Pour la conversion faut preciser le type float
# n3=float("19.8")
# print(n3)

# Interpollation de chaine de caractere avec .format()

# eg='Selina a 24 ans'
# print(eg)
# eg='{} a {} ans'
# print(eg)
# rst=eg.format('Selina',24) #remplace les trous manquants
# print(rst)
# snt='Le canada se trouve en {}'
# n1=input("Ou se trouve le canada\n")
# rst=snt.format(n1)
# print(rst)
# On peut numeroter nos placeholder
# ' serena a 24 ans et serena travaille au USA et vis en France'
# output=' {0} a {1} ans et {0} travaille au {2} et vis en {3}'
# print(output.format('Serena',24,'USA','France'))
# On peut utiliser des variables pour nos placeholder

# output=' serena a 24 ans et serena travaille au USA et vis en France'
# output=' {name} a {old} ans et {name} travaille au {country1} et vis en {country2}'
# print(output.format(name='Serena',old=24,country1='USA',country2='France'))

# Les f-string
# old=24
# name='stephanie'
# rst=f"je suis {name} et j'ai {old} ans"
# print(rst)
# et si on divisait l'age par 2?
# rst2=f"je suis {name} et j'ai {old/2} ans"
# print(rst2)

