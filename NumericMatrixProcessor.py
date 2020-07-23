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
    print('1. Add matrices', '2. Multiply matrix by a constant', '3. Multiply matrices', '0. Exit', sep='\n')
    user_choice = input('Your choice: > ')
    return user_choice

# fonctions permettant de réaliser les 3 actions demandées par l'utilisateur


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


def multiply_constant():
    # création de la matrice 1
    try:
        input_1 = input('Enter size of matrix > ').split()  # list(input())
        row_count, col_count = int(input_1[0]), int(input_1[1])
    except IndexError:
        print('You should input two numbers separated by a space. Please try again !')
        quit()
    print('Enter matrix:')
    matrice_1 = matrice_user(row_count, col_count)
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
            multiply_constant()
            print('')
        if user_choice == 3:
            input_1, input_2, matrice_1, matrice_2, col_count, row_count_2 = two_matrices()
            multiply_matrice(matrice_1, matrice_2, col_count, row_count_2)
            print('')
        else:
            print('Your answer should be a number between 0 and 3')
            print('')
    else:
        print('Your answer should be a number between 0 and 3')
        print('')
else:
    quit()







