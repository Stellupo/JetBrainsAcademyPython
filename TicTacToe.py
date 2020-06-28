def field_printing(field):
    print("-"*9)
    print("|" + " " + field[0][0] + " " + field[0][1] + " " + field[0][2] + " " + "|")
    print("|" + " " + field[1][0] + " " + field[1][1] + " " + field[1][2] + " " + "|")
    print("|" + " " + field[2][0] + " " + field[2][1] + " " + field[2][2] + " " + "|")
    print("-"*9)

def main_game(move,field,joueur_state):
    if len(move)!=2:  #vérifier qu'on ait le bon nombre d'arguments
        print("You should enter numbers!")
        return joueur_state
    else:
        row_coordinate = move[0]
        column_coordinate = move[1]
        try:  #vérifier qu'on ait des chiffres
            row_coordinate = int(row_coordinate)
            column_coordinate = int(column_coordinate)
            if row_coordinate not in range(1,4) or column_coordinate not in range(1, 4): #vérifier qu'on ait les bons chiffres
                print("Coordinates should be from 1 to 3!")
                return joueur_state
            else:
                position = field[3 - int(column_coordinate)][int(row_coordinate) - 1]
                if position == "_" or position == " ": #si la place est libre
                    if joueur_state == "X":
                        field[3 - int(column_coordinate)][int(row_coordinate) - 1] = "X"
                        change_state = "O"
                    elif joueur_state == "O":
                        field[3 - int(column_coordinate)][int(row_coordinate) - 1] = "O"
                        change_state = "X"
                    field_printing(field)
                    return change_state
                elif position == "X" or position == "O":
                    print("This cell is occupied! Choose another one!")
                    return joueur_state
        except ValueError:
            print("You should enter numbers!")
            return joueur_state

def update_fieldliste(field):
    field_liste = [elements for row in field for elements in row]
    return field_liste

def check_game(state_game, field_liste):
    if field_liste[0] == field_liste[4] == field_liste[8]:
        if field_liste[0] == "X":
            state_game.add("X_winner")
        elif field_liste[0] == "O":
            state_game.add("O winner")
    elif field_liste[2] == field_liste[4] == field_liste[6]:
        if field_liste[2] == "X":
            state_game.add("X_winner")
        elif field_liste[2] == "O":
            state_game.add("O winner")
    else:
        for i in range(0,9,3): #check ligne
            if field_liste[i] == field_liste[i+1] == field_liste[i+2]:
                if field_liste[i] == field_liste[i+1] == field_liste[i+2] == "X":
                    state_game.add("X_winner")
                elif field_liste[i] == field_liste[i+1] == field_liste[i+2] == "O":
                    state_game.add("O winner")
        for i in range (3): #check colonne
            if field_liste[i] == field_liste[i+3] == field_liste[i+6]:
                if field_liste[i] == field_liste[i+3] == field_liste[i+6] == "X":
                    state_game.add("X_winner")
                elif field_liste[i] == field_liste[i+3] == field_liste[i+6] == "O":
                    state_game.add("O winner")


def state_game_func(state_game,field_liste):
    if "X_winner" in state_game:
        print ("X wins")
        return "stop"
    elif "O winner" in state_game:
        print("O wins")
        return "stop"
    else:
        if "_" not in field_liste and " " not in field_liste:
            print("Draw")
            return "stop"


def game():
    field = [[" "," "," "],[" "," "," "],[" "," "," "]] #[[column for column in range(3)] for row in range(3)]
    field_liste = [" "," "," "," "," "," "," "," "," "]
    field_printing(field)
    joueur_state = "X"
    result = ""
    state_game = set()
    while result != "stop":
        move = input("Enter the coordinates: ").split(" ")
        change_state_game = main_game(move,field,joueur_state)
        joueur_state = change_state_game
        field_liste = update_fieldliste(field)
        check_game(state_game, field_liste)
        result = state_game_func(state_game, field_liste)


#appel de la fonction principale
game()