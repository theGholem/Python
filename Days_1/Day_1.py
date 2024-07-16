# 1- Imprime ton âge dans la console.

# 2- Calcule et imprime le nombre de jours, de semaines et de mois dans 27 ans. Ne t’inquiètes pas des années bissextiles !

# 3- Calcule et imprime l’aire d’un cercle dont le rayon est de 5 unités. Tu peux être aussi précis que tu le souhaites avec la valeur de pi.

# 1.
old = 23
print('1. \nI am ', old, 'years old!')

# 2.
#for 1 year
days = 365
weeks = 52
months = 12
#for 27 year
days = 365 * 27
weeks = 52 * 27
months = 12 * 27

print('\n2.\nIn 27 years , we have : \n', days, 'days \n', weeks, 'weeks \n',
      months, 'months')

# 3.
# area of circle = pi*r^2 & r=5
pi = 3.14159
r = 5
areaOfCircle = pi * r * r

print('\n3.\nArea of circle with radius 5 is : ', areaOfCircle, ' m2')

#pow(R, N) ==>RpuissanceN <==> R**N