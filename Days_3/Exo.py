# Enonce
#
# 1. En utilisant la variable ci-dessous, imprime « Hello, world ! ».
# -->  greeting = "Hello, world"
# Tu peux ajouter le point d’exclamation manquant à l’aide de la concaténation 
# de chaînes de caractères, format ou des f-string. C’est à toi de choisir.
#
# 2. Demande à l’utilisateur son nom, puis salue-le en utilisant son nom comme partie 
# de la salutation (greeting). Le nom doit avoir sa première lettre en majuscule et 
# ne doit pas être entouré d’espace blanc excessif.
# Par exemple, si l’utilisateur saisit -->"lewis ", le résultat devrait être 
# quelque chose comme ceci : -->Hello, Lewis!
#
# 3. Concatène la chaîne de caractères « J’ai  » et le nombre entier 29 pour produire 
# une chaîne de caractères qui se lit « J’ai 29 ».
# Rappelle-toi que nous ne pouvons concaténer que des chaînes de caractères à 
# d’autres chaînes de caractères. Tu devras donc convertir le nombre entier en chaîne 
# de caractères avant de pouvoir effectuer la concaténation.
#
# 4. Formate et imprime les informations ci-dessous en utilisant l’interpolation de 
# chaînes de caractères :
# -->title = "Joker"
# -->director = "Todd Phillips"
# -->release_year = 2019
# Le résultat devrait ressembler à ceci :
# -->Joker (2019), réalisé par Todd Phillips

# 1.

# avec un format()
greeting="Hello, world {symbol}"
rst=greeting.format(symbol='!')
print(rst)
# avec un f-string
symb='!'
rst=f"Hello, world {symb}"
print(rst)

# 2.

greeting=input("What is your name?\n")
print("Hello, "+greeting.strip().title())

# 3.

number=str(29)
text="j'ai "
rst=text+number
print(rst)

# 4.
title = "Joker"
director = "Todd Phillips"
release_year = 2019
rst=f"{title} ({release_year}), realise par {director}"
print(rst)