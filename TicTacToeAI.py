import random


class TicTacToe:
    def __init__(self, field):
        self.field = field  # [[column for column in range(3)] for row in range(3)]x
        self.field_liste = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.joueur_state = "X"
        self.state_game = set()
        self.result = ""
        self.field_printing()

    def field_printing(self):
        print("-" * 9)
        print("|" + " " + self.field[0][0] + " " + self.field[0][1] + " " + self.field[0][2] + " " + "|")
        print("|" + " " + self.field[1][0] + " " + self.field[1][1] + " " + self.field[1][2] + " " + "|")
        print("|" + " " + self.field[2][0] + " " + self.field[2][1] + " " + self.field[2][2] + " " + "|")
        print("-" * 9)

    def main_game(self, row_coordinate, column_coordinate):
        if self.joueur_state == "X":
            self.field[3 - int(column_coordinate)][int(row_coordinate) - 1] = "X"
            self.joueur_state = "O"
        elif self.joueur_state == "O":
            self.field[3 - int(column_coordinate)][int(row_coordinate) - 1] = "O"
            self.joueur_state = "X"
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
            for i in range(0, 9, 3):  # check ligne
                if self.field_liste[i] == self.field_liste[i + 1] == self.field_liste[i + 2]:
                    if self.field_liste[i] == self.field_liste[i + 1] == self.field_liste[i + 2] == "X":
                        self.state_game.add("X_winner")
                    elif self.field_liste[i] == self.field_liste[i + 1] == self.field_liste[i + 2] == "O":
                        self.state_game.add("O winner")
            for i in range(3):  # check colonne
                if self.field_liste[i] == self.field_liste[i + 3] == self.field_liste[i + 6]:
                    if self.field_liste[i] == self.field_liste[i + 3] == self.field_liste[i + 6] == "X":
                        self.state_game.add("X_winner")
                    elif self.field_liste[i] == self.field_liste[i + 3] == self.field_liste[i + 6] == "O":
                        self.state_game.add("O winner")

    def state_game_func(self):
        if "X_winner" in self.state_game:
            print("X wins")
            return "stop"
        elif "O winner" in self.state_game:
            print("O wins")
            return "stop"
        else:
            if "_" not in self.field_liste and " " not in self.field_liste:
                print("Draw")
                return "stop"
            elif "_" in self.field_liste or " " in self.field_liste:
                return ""

    def game(self, row_coordinate, column_coordinate):
        self.main_game(row_coordinate, column_coordinate)
        self.field_liste = self.update_fieldliste()
        self.check_game()
        self.result = self.state_game_func()
        return self.result

    def user_move(self):
        if self.joueur_state == 'X':  # si c'est au tour du joueur de jouer
            move = input("Enter the coordinates: ").split(" ")
            if len(move) != 2:  # vérifier qu'on ait le bon nombre d'arguments
                print("You should enter numbers!")
            else:
                row_coordinate = move[0]
                column_coordinate = move[1]
                try:  # vérifier qu'on ait des chiffres
                    row_coordinate = int(row_coordinate)
                    column_coordinate = int(column_coordinate)
                except ValueError:
                    print("You should enter numbers!")
                if row_coordinate not in range(1, 4) or column_coordinate not in range(1,
                                                                                       4):  # vérifier qu'on ait les bons chiffres
                    print("Coordinates should be from 1 to 3!")
                else:
                    position = field[3 - int(column_coordinate)][int(row_coordinate) - 1]
                    if position == "X" or position == "O":
                        print("This cell is occupied! Choose another one!")
                    if position == "_" or position == " ":  # si la place est libre
                        self.result = self.game(row_coordinate, column_coordinate)
            return self.result
        if self.joueur_state == 'O':
            print('Making move level "easy"')
            while True:
                row_coordinate, column_coordinate = random.randint(1, 3), random.randint(1, 3)
                position = field[3 - int(column_coordinate)][int(row_coordinate) - 1]
                if position == "_" or position == " ":  # si la place est libre
                    self.result = self.game(row_coordinate, column_coordinate)
                    break
                else:  # si la place est prise
                    continue
        return self.result


field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
game_instance = TicTacToe(field)

# appel de la fonction principale
result = ""
while result != 'stop':
    result = game_instance.user_move()