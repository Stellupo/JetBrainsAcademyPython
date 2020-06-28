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

#main
state_game = set()
global liste
liste = []
answer = input("Enter cells: ")
print("---------")
print("|" + " " + answer[0] + " " + answer[1] + " " + answer[2] + " " + "|")
print("|" + " " + answer[3] + " " + answer[4] + " " + answer[5] + " " + "|")
print("|" + " " + answer[6] + " " + answer[7] + " " + answer[8] + " " + "|")
print("---------")

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
        print("Game not finished")