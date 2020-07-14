def number_row_col(number_rows_column):
    number_rows_column.remove(" ")
    #print(number_rows_column)
    row_count, col_count = int(number_rows_column[0]), int(number_rows_column[1])
    #print(row_count)
    #print(col_count)
    return row_count, col_count

def matrice_user(row_count, col_count):
    liste = []
    counter = 0
    while counter != row_count:
        element = list(input())
        liste += element
        liste = [x for x in liste if x != " "]
        counter += 1
    '''for num in range(len(liste)):
        liste[num] = int(liste[num])'''
    matrice = creatMatrix(row_count, col_count, liste)
    return matrice

def creatMatrix(row_count, col_count, liste):
    matrice=([liste[i:i+col_count] for i in range(0,len(liste),col_count)])
    '''for i in range(row_count):
        matrice.append([])
        if col_count >= 2:
            for j in range(col_count):
                matrice[i].append(liste[row_count * i + j])  #liste[(row_count) * i + j])
        elif col_count ==1:
            matrice[i].append(liste[j])
            j += 1
        #matrice.append(rowList)'''
    return matrice

def matrice_add(matrice_1, matrice_2):
    matrice_summed = []
    for num in range(len(matrice_1)):
        for i in range(len(matrice_1[0])):
            elements = str(int(matrice_1[num][i]) + int(matrice_2[num][i]))
            matrice_summed.append(elements)
    #print(matrice_summed)
    return matrice_summed


#main
number_rows_column_1 = list(input())
row_count, col_count = number_row_col(number_rows_column_1)
matrice_1 = matrice_user(row_count, col_count)
#print(matrice_1)
number_rows_column_2 = list(input())
row_count, col_count = number_row_col(number_rows_column_2)
matrice_2 = matrice_user(row_count, col_count)
#print(matrice_2)
if number_rows_column_1 == number_rows_column_2:
    matrice_summed = matrice_add(matrice_1,matrice_2)
    matrice_summed = creatMatrix(row_count, col_count, matrice_summed)
    for num in range(len(matrice_summed)):
        print((' '.join(matrice_summed[num])))
else:
    print('ERROR')