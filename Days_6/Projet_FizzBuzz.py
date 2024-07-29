# ENONCÉ : Le jeux du FIZZ-BUZZ

# Un joueur commence par dire le chiffre 1.
# Chaque joueur dit ensuite à tour de rôle le chiffre suivant, en comptant un par un.
# Si le nombre est divisible par 3, au lieu de dire le nombre, le joueur doit dire « Fizz ».
# Si le nombre est divisible par 5, au lieu de dire le nombre, le joueur doit dire « Buzz ».
# Si le nombre est divisible par 3 et 5, au lieu de dire le nombre, le joueur doit dire « Fizz Buzz ».
# Si tu commets une erreur, tu es généralement éliminé du jeu, et le jeu continue jusqu’à ce qu’il ne reste plus qu’un seul joueur.

# EXEMPLE `:
# S’il n’y a pas d’erreur, les 15 premiers tours de Fizz Buzz devraient ressembler à ceci :
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# Fizz Buzz

# NB : un nombre X est divisible par 'n' lorsque X % n = 0, ou tous simplement lorsque X est divisible par n de telle sorte que le reste soit 1
# modulo (%) est in operateur qui permet de trouver le reste de la division 

for number in range(1, 101, 1) :
    if number % 3 == 0 and number % 5 == 0 : 
        print(f"Fizz Buzz")
    elif number % 3 == 0 :
        print(f"Fizz")
    elif number % 5 == 0 : 
        print(f"Buzz")
    else :
        print(f"{number}")
