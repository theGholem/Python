#1.Crée une liste de films (movies) contenant un seul tuple. Le tuple doit contenir le 
# titre du film, le nom du réalisateur, l’année de sortie du film et le budget du film.

#2.Utilise la fonction d’entrée input pour recueillir des informations sur un autre film.
#  Tu as besoin du titre, du nom du réalisateur, de l’année de sortie et du budget.

#3.Crée un nouveau tuple à partir des valeurs que tu as recueillies à l’aide de la fonction
#  input. Assure-toi qu’elles sont dans le même ordre que le tuple que tu as écrit dans 
#  la liste des films (movies).

#4. Utilise une f-string pour imprimer le nom du film et l’année de sortie en accédant à 
#   ton nouveau tuple de film.

#5 Ajoute le nouveau tuple de film à la collection movies en utilisant append.

#6 Imprime les deux films de la collection movies.

#7. Supprime le premier film de movies. Utilise la méthode de ton choix.

# 1.
movie=[("Piège de crystal","John McTiernan",1988,3.6)]
print(movie)

# 2.
info_1=input("Saisir le nom du film : \n")
info_2=input("Saisir le nom du realisateur du film : \n")
info_3=input("Saisir la date de parution du film : \n")
info_4=input("Saisir le budjet du film : \n")

# 3.
movie_2=info_1, info_2, info_3, info_4
print(movie_2)

# 4.
rst=f"\nnom du film : {movie_2[0]},\nannée de sortie : {movie_2[2]}"
print(rst)

# 5.
movie.append(movie_2)
print(movie)

# 6.
print("\nPremier film : ",movie[0][0])
print("Deuxieme film : ",movie[1][0])

# 7.
