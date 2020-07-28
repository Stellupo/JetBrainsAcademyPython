import math
# fonctions permettant de créer les matrices


def matrice_user(row_count, col_count):  # création d'une matrice à partir des inputs du users
    liste = []
    counter = 0
    while counter != row_count:
        liste += input().split(" ")
        liste = [x for x in liste if x!= " "]
        counter += 1
    matrice = ([liste[i:i + col_count] for i in range(0, len(liste), col_count)])
    return matrice


def one_matrix(): #fonction appelée pour récupérer de l'utilisateur 1 matrice
    # création de la matrice 1
    try:
        input_1 = input('Enter size of matrix > ').split()  # list(input())
        row_count, col_count = int(input_1[0]), int(input_1[1])
    except IndexError:
        print('You should input two numbers separated by a space. Please try again !')
        quit()
    print('Enter matrix:')
    matrice_1 = matrice_user(row_count, col_count)
    return matrice_1, col_count


def two_matrices(): #fonction appelée pour récupérer de l'utilisateur 2 matrices
    # création de la matrice 1
    try:
        input_1 = input('Enter size of first matrix > ').split()  # list(input())
        row_count, col_count = int(input_1[0]), int(input_1[1])
    except IndexError:
        print('You should input two numbers separated by a space. Please try again !')
        quit()
    print('Enter first matrix:')
    matrice_1 = matrice_user(row_count, col_count)
    # création de la matrice 2
    input_2 = input('Enter size of second matrix > ').split()
    row_count_2, col_count_2 = int(input_2[0]), int(input_2[1])
    print('Enter second matrix:')
    matrice_2 = matrice_user(row_count_2, col_count_2)
    return input_1, input_2, matrice_1, matrice_2, col_count, row_count_2

# fonction d'affichage du menu


def menu():
    print('1. Add matrices', '2. Multiply matrix by a constant', '3. Multiply matrices', '4. Transpose matrix', '5. Calculate a determinant', '6. Inverse matrix:', '0. Exit', sep='\n')
    user_choice = input('Your choice: > ')
    print(" ")
    return user_choice

# fonctions permettant de réaliser les 5 actions possibles demandees par l'utilisateur


def matrice_add(input_1, input_2, matrice_1, matrice_2, col_count): # Somme des deux matrices conditionnellement à leurs tailles
    if input_1 == input_2:
        matrice_summed = []
        for num in range(len(matrice_1)):
            for i in range(len(matrice_1[0])):
                elements = str(float(matrice_1[num][i]) + float(matrice_2[num][i]))
                matrice_summed.append(elements)
        matrice_summed = ([matrice_summed[i:i + col_count] for i in range(0, len(matrice_summed), col_count)])
        print('The result is:')
        for num in range(len(matrice_summed)):
            print((' '.join(matrice_summed[num])))
    else:
        print('ERROR')


def multiply_constant(matrice_1, col_count):
    # multiplication
    input_2 = float(input('Enter constant : > '))
    matrice_multiplied = []
    print('The result is:')
    for num in range(len(matrice_1)):
        for i in range(len(matrice_1[0])):
            elements = str(float(matrice_1[num][i]) * input_2)
            matrice_multiplied.append(elements)
    matrice_multiplied = ([matrice_multiplied[i:i + col_count] for i in
                           range(0, len(matrice_multiplied), col_count)])  # transformation de la liste en matrice
    for num in range(len(matrice_multiplied)):  # affichage de la liste de string avec un espace entre chaque élement de ligne
        print((' '.join(matrice_multiplied[num])))


def multiply_matrice(matrice_1, matrice_2, col_count, row_count_2):
    if col_count == row_count_2: #si la taille des matrices permet la multiplication
        matrice_multiplied = []
        #transposition de la matrice 2
        matrice_transposed = [[matrice_2[y][x] for y in range(len(matrice_2))] for x in range(len(matrice_2[0]))]
        for num in range(len(matrice_1)): #lignes de la matrice 1
            j = 0
            while j != len(matrice_2[0]) :
                result = []
                for i in range(len(matrice_1[0])) : #éléments dans la ligne
                    result += [float(matrice_1[num][i]) * float(matrice_transposed[j][i])]
                j += 1
                elements = sum(result)
                matrice_multiplied.append(str(elements))
        matrice_multiplied = ([matrice_multiplied[i:i + len(matrice_2[0])] for i in range(0, len(matrice_multiplied), len(matrice_2[0]))])
        print('The result is:')
        for num in range(len(matrice_multiplied)):  # affichage de la liste de string avec un espace entre chaque élement de ligne
            print((' '.join(matrice_multiplied[num])))
    else:
        print('The number of columns in the first matrix shoud be equal to the number of rowds of the second matrix')

def transpose_matrix():
    print('1. Main diagonal', '2. Side diagonal', '3. Vertical line', '4. Horizontal line', sep='\n')
    user_choice = input('Your choice: > ')
    print(" ")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        matrice_1, col_count = one_matrix()
        if user_choice not in [1, 2, 3, 4]:
            print('Your answer should be a number between 0 and 4')
            print('')
        if user_choice in [1, 2, 3, 4]:
            if user_choice == 1:
                matrice_transposed = [[matrice_1[y][x] for y in range(len(matrice_1))] for x in
                                      range(len(matrice_1[0]))]
            if user_choice == 2:
                matrice_transposed = [[matrice_1[y][x] for y in range(len(matrice_1))] for x in
                                      range(len(matrice_1[0]))]
                matrice_transposed.reverse()
                matrice_transposed.reverse()
                matrice_transposed.reverse()
                for l in matrice_transposed:
                    l.reverse()
            if user_choice == 3:
                matrice_transposed = matrice_1
                for l in matrice_transposed:
                    l.reverse()
            if user_choice == 4:
                matrice_transposed = matrice_1
                matrice_transposed.reverse()
        print('The result is:')
        for num in range(len(matrice_transposed)):  # affichage de la liste de string avec un espace entre chaque élement de ligne
            print((' '.join(matrice_transposed[num])))
    else:
        print('Your answer should be a number between 0 and 4')
        print('')


def determinant(matrice_1):
    #base case
    if len(matrice_1) == 1:
        return matrice_1[0][0]
    if len(matrice_1) == 2:
        result = (matrice_1[0][0]) * (matrice_1[1][1]) - ((matrice_1[0][1]) * (matrice_1[1][0]))
        return result
    else:  #recursive step
        result = 0
        for j in range(len(matrice_1[0])):
            copy = [row[:] for row in matrice_1]  # copie de matrice_1
            copy.pop(0) # suppression d'une ligne de la matrice_1, il est plus simple que ce soit la première comme ça on a (-1)^(1+col)
            for item in copy:  # pour les lignes dans copy
                item.pop(j)  # suppression d'une colonne. Attention numéro de colonne = j + 1 car j est l'index
            if j%2==0:  # si j est pair, on aura (-1)^(1+(j+1)))=1 * Minor
                result += ((matrice_1[0][j]) * determinant(copy))
            else:  # si j est impair, on aura (-1)^(1+(j+1)))=-1 * Minor
                result -= ((matrice_1[0][j]) * determinant(copy))
        return result

def inverse(matrice_1, col_count):
    det = determinant(matrice_1)
    if det == 0:
        print("This matrix doesn't have an inverse.")
    else:
        constant = round(1/(det),4)  # inverse du determinant
        #calcul de la comatrice:
        comatrix = [row[:] for row in matrice_1]
        for m in range(col_count):
            for j in range(len(matrice_1[0])):
                copy = [row[:] for row in matrice_1]  # copie de matrice_1
                copy.pop(m) # suppression d'une ligne de la matrice_1, il est plus simple que ce soit la première comme ça on a (-1)^(1+col)
                for item in copy:  # pour les lignes dans copy
                    item.pop(j)  # suppression d'une colonne. Attention numéro de colonne = j + 1 car j est l'index
                comatrix[m][j] = (-1)**(m+1+j+1)*determinant(copy)
        #print(comatrix)
        comatrix = [[comatrix[y][x] for y in range(len(comatrix))] for x in range(len(comatrix[0]))]
        '''for num in range(len(comatrix)):  # affichage de la liste de string avec un espace entre chaque élement de ligne
            print(comatrix[num])'''
        #main diagonal transposition
        # multiplication de la comatrice par l'inverse du déterminant
        matrice_multiplied = []
        print('The result is:')
        for num in range(len(comatrix)):
            for i in range(len(comatrix[0])):
                elements = str(float(round((comatrix[num][i]) * constant,3)))
                matrice_multiplied.append(elements)
        matrice_multiplied = ([matrice_multiplied[i:i + col_count] for i in
                               range(0, len(matrice_multiplied), col_count)])  # transformation de la liste en matrice
        for num in range(len(matrice_multiplied)):  # affichage de la liste de string avec un espace entre chaque élement de ligne
            print((' '.join(matrice_multiplied[num])))

# main
user_choice = ""
while user_choice != 0:
    user_choice = menu()
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice == 1:
            input_1, input_2, matrice_1, matrice_2, col_count, row_count_2 = two_matrices()
            matrice_add(input_1, input_2, matrice_1, matrice_2, col_count)
            print('')
        if user_choice == 2:
            matrice_1, col_count = one_matrix()
            multiply_constant(matrice_1, col_count)
            print('')
        if user_choice == 3:
            input_1, input_2, matrice_1, matrice_2, col_count, row_count_2 = two_matrices()
            multiply_matrice(matrice_1, matrice_2, col_count, row_count_2)
            print('')
        if user_choice == 4:
            transpose_matrix()
            print('')
        if user_choice == 5:
            matrice_1, col_count = one_matrix()
            for x in range(len(matrice_1)): # transformation de la matrice de string en matrice numérique
                matrice_1[x] = [int(i) if i.isdigit() else float(i) for i in matrice_1[x]]
            if col_count == len(matrice_1):    # condition de matrices carrées
                print('The result is:')
                print(determinant(matrice_1))
                print('')
            else:
                print('Your matrix should be a sqare matrix')
                break
        if user_choice == 6:
            matrice_1, col_count = one_matrix()
            for x in range(len(matrice_1)): # transformation de la matrice de string en matrice numérique
                matrice_1[x] = [int(i) if i.isdigit() else float(i) for i in matrice_1[x]]
            inverse(matrice_1, col_count)
            print('')
        elif user_choice not in [0,1,2,3,4,5,6]:
            print('Your answer should be a number between 0 and 4')
            print('')
    else:
        print('Your answer should be a number between 0 and 4')
        print('')
else:
    quit()