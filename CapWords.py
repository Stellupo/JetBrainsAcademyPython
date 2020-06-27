names = str(input())
new_liste = []
liste = (names.split("_"))  #ex : BIRD appartient à la liste même si il n'y a pas de _
for i in range(len(liste)):
    elements = (str(liste[i]).capitalize())
    new_liste += [elements]
print(" ".join(new_liste))

# ou plus simple : print("".join([x.lower().capitalize() for x in input().split('_')]))