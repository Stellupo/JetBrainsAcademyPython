def number_row_col(number):  # liste clean du nombre de lignes,colonne sous cette forme [num, num]
    number = number.split()
    row_count, col_count = int(number[0]), int(number[1])
    # print(row_count)  print(col_count)
    return row_count, col_count


def matrice_user(row_count, col_count):  # création d'une matrice à partir des inputs du users
    liste = []
    counter = 0
    while counter != row_count:
        liste += list(input())
        liste = [x for x in liste if x != " "]
        counter += 1
    matrice = ([liste[i:i + col_count] for i in range(0, len(liste), col_count)])
    return matrice


def matrice_add(matrice_1, matrice_2):  # somme de deux matrices de même taille
    matrice_summed = []
    for num in range(len(matrice_1)):
        for i in range(len(matrice_1[0])):
            elements = str(int(matrice_1[num][i]) + int(matrice_2[num][i]))
            matrice_summed.append(elements)
    # print(matrice_summed)
    return matrice_summed


# main
# création de la matrice 1

input_1 = input() #list(input())
row_count, col_count = number_row_col(input_1)
matrice_1 = matrice_user(row_count, col_count)
# print(matrice_1)
# création de la matrice 2
input_2 = input()
row_count, col_count = number_row_col(input_2)
matrice_2 = matrice_user(row_count, col_count)
# print(matrice_2)
# Somme des deux matrices conditionnellement à leurs tailles
if input_1 == input_2:
    matrice_summed = matrice_add(matrice_1, matrice_2)
    matrice_summed = ([matrice_summed[i:i + col_count] for i in range(0, len(matrice_summed), col_count)])
    for num in range(len(matrice_summed)):
        print((' '.join(matrice_summed[num])))
else:
    print('ERROR')