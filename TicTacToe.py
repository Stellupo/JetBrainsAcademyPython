def liste_check(liste, state_game):
    if liste.count("X") == 3:
        #print("X wins")
        state_game.add("X_winner")
    elif liste.count("O") == 3:
        #print("O wins")
        state_game.add("O_winner")
    else:  #mélange de vide, X ou O
        state_game.add("No_winner")

def colonne_check(liste, state_game):
    x = 0
    y = 7
    while x !=3:
        for i in range(x,y,3):
            if answer[i] == "X" or answer[i] == "O" or answer[i] == "_" or answer[i] == " ":
                liste += answer[i]
                continue
            else:
                break
        liste_check(liste, state_game)
        liste = []
        x += 1
        y += 1

def ligne_check(liste, state_game):
    x = 0
    y = 3
    while x < 7:
        for i in range(x,y,1):
            if answer[i] == "X" or answer[i] == "O" or answer[i] == "_" or answer[i] == " ":
                liste += answer[i]
                continue
            else:
                break
        liste_check(liste, state_game)
        liste = []
        x += 3
        y += 3

def diagonalel_check(liste, state_game):
    x = 0
    y = 9
    for i in range(x,y,4):
        if answer[i] == "X" or answer[i] == "O" or answer[i] == "_" or answer[i] == " ":
            liste += answer[i]
            continue
        else:
            break
    liste_check(liste, state_game)

def diagonaler_check(liste, state_game):
    x = 2
    y = 7
    for i in range(x,y,2):
        if answer[i] == "X" or answer[i] == "O" or answer[i] == "_" or answer[i] == " ":
            liste += answer[i]
            continue
        else:
            break
    liste_check(liste, state_game)

def field_printing(field):
    print("---------")
    print("|" + " " + field[0][0] + " " + field[0][1] + " " + field[0][2] + " " + "|")
    print("|" + " " + field[1][0] + " " + field[1][1] + " " + field[1][2] + " " + "|")
    print("|" + " " + field[2][0] + " " + field[2][1] + " " + field[2][2] + " " + "|")
    print("---------")

#état du terrain
answer = input("Enter cells: ")
field = [
        [answer[0], answer[1], answer[2]],
        [answer[3], answer[4], answer[5]],
        [answer[6], answer[7], answer[8]]
        ]
field_printing(field)
while True:
    move = input("Enter the coordinates: ").split(" ")
    if len(move)!=2:  #vérifier qu'on ait le bon nombre d'arguments
        print("You should enter numbers!")
    else:
        row_coordinate = move[0]
        column_coordinate = move[1]
        try:  #vérifier qu'on ait des chiffres
            row_coordinate = int(row_coordinate)
            column_coordinate = int(column_coordinate)
            if row_coordinate not in range(1,4) or column_coordinate not in range(1, 4):
                print("Coordinates should be from 1 to 3!")
            else:
                position = field[3 - int(column_coordinate)][int(row_coordinate) - 1]
                if position == "_" or position == " ":
                    field[3 - int(column_coordinate)][int(row_coordinate) - 1] = "X"
                    field_printing(field)
                    break
                elif position == "X" or position == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
        except ValueError:
            print("You should enter numbers!")




#col = [[row[i] for row in field] for i in range(3)]
#print (col[2])
'''
#main
state_game = set()
global liste
liste = []
colonne_check(liste, state_game)
liste = []
ligne_check(liste, state_game)
liste = []
diagonalel_check(liste, state_game)
liste = []
diagonaler_check(liste, state_game)
liste = []
if "X_winner" in state_game and "O_winner" in state_game:
    print("Impossible")
elif "X_winner" in state_game and "O_winner" not in state_game:
    print ("X wins")
elif "O_winner" in state_game and "X_winner" not in state_game:
    print("O wins")
elif "No_winner" in state_game:
    if abs(answer.count("X")-answer.count("O")) >= 2:
        print("Impossible")
    elif "_" not in answer and " " not in answer:
        print("Draw")
    elif "_" in answer or " " in answer:
        print("Game not finished")'''