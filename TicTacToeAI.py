class TicTacToe :
    def __init__(self, field):
        self.field = field #[[column for column in range(3)] for row in range(3)]x
        self.fieldliste = [" "," "," "," "," "," "," "," "," "]
        self.joueur_state = "X"
        self.state_game = set()
        self.result = ""
        self.field_printing()

    def field_printing(self):
        print("-"*9)
        print("|" + " " + self.field[0][0] + " " + self.field[0][1] + " " + self.field[0][2] + " " + "|")
        print("|" + " " + self.field[1][0] + " " + self.field[1][1] + " " + self.field[1][2] + " " + "|")
        print("|" + " " + self.field[2][0] + " " + self.field[2][1] + " " + self.field[2][2] + " " + "|")
        print("-"*9)

    def main_game(self):
        position = self.field[3 - int(column_coordinate)][int(row_coordinate) - 1]
        if position == "_" or position == " ": #si la place est libre
            if self.joueur_state == "X":
                self.field[3 - int(column_coordinate)][int(row_coordinate) - 1] = "X"
            elif self.joueur_state == "O":
                self.field[3 - int(column_coordinate)][int(row_coordinate) - 1] = "O"
            self.field_printing()


    def update_fieldliste(self):
        self.field_liste = [elements for row in self.field for elements in row]
        return self.field_liste

    def check_game(self):
        if self.field_liste[0] == self.field_liste[4] == self.field_liste[8]:
            if self.field_liste[0] == "X":
                self.state_game.add("X_winner")
            elif self.field_liste[0] == "O":
                self.state_game.add("O winner")
        elif self.field_liste[2] == self.field_liste[4] == self.field_liste[6]:
            if self.field_liste[2] == "X":
                self.state_game.add("X_winner")
            elif self.field_liste[2] == "O":
                self.state_game.add("O winner")
        else:
            for i in range(0,9,3): #check ligne
                if self.field_liste[i] == self.field_liste[i+1] == self.field_liste[i+2]:
                    if self.field_liste[i] == self.field_liste[i+1] == self.field_liste[i+2] == "X":
                        self.state_game.add("X_winner")
                    elif self.field_liste[i] == self.field_liste[i+1] == self.field_liste[i+2] == "O":
                        self.state_game.add("O winner")
            for i in range (3): #check colonne
                if self.field_liste[i] == self.field_liste[i+3] == self.field_liste[i+6]:
                    if self.field_liste[i] == self.field_liste[i+3] == self.field_liste[i+6] == "X":
                        self.state_game.add("X_winner")
                    elif self.field_liste[i] == self.field_liste[i+3] == self.field_liste[i+6] == "O":
                        self.state_game.add("O winner")


    def state_game_func(self):
        if "X_winner" in self.state_game:
            print ("X wins")
            return "stop"
        elif "O winner" in self.state_game:
            print("O wins")
            return "stop"
        else:
            if "_" not in self.field_liste and " " not in self.field_liste:
                print("Draw")
                return "stop"
            elif "_" in self.field_liste or " " in self.field_liste:
                print("Game not finished")
                return "stop"


    def game(self):
        self.field_liste = self.update_fieldliste()
        if abs(self.field_liste.count("X") > self.field_liste.count("O")):
            self.joueur_state = "O"
        if abs(self.field_liste.count("X") == self.field_liste.count("O")):
            self.joueur_state = "X"
        while self.result != "stop":
            self.main_game()
            self.field_liste = self.update_fieldliste()
            self.check_game()
            self.result = self.state_game_func()



answer = input("Enter cells: ")
field = [[answer[0], answer[1], answer[2]],[answer[3], answer[4], answer[5]],[answer[6], answer[7], answer[8]]]
game_instance = TicTacToe(field)

#appel de la fonction principale
while True:
    move = input("Enter the coordinates: ").split(" ")
    if len(move) != 2:  # vérifier qu'on ait le bon nombre d'arguments
        print("You should enter numbers!")
        continue
    else:
        row_coordinate = move[0]
        column_coordinate = move[1]
        try:  # vérifier qu'on ait des chiffres
            row_coordinate = int(row_coordinate)
            column_coordinate = int(column_coordinate)
        except ValueError:
            print("You should enter numbers!")
            continue
        if row_coordinate not in range(1, 4) or column_coordinate not in range(1,4):  # vérifier qu'on ait les bons chiffres
            print("Coordinates should be from 1 to 3!")
            continue
        else:
            position = field[3 - int(column_coordinate)][int(row_coordinate) - 1]
            if position == "X" or position == "O":
                print("This cell is occupied! Choose another one!")
                continue
            if position == "_" or position == " ":  # si la place est libre
                game_instance.game()
                break