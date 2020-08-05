import random


class TicTacToe:
    def __init__(self):
        self.reinitialisation()

    def reinitialisation(self):
        self.field_liste = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.joueur_state = "X"
        self.state_game = set()
        self.result = ""
        self.game_level = ['easy', 'medium', 'hard']
        self.command = ""


    def field_printing(self): # affiche le terrain en table
        print("-" * 9)
        print("|" + " " + self.field_liste[0] + " " + self.field_liste[1] + " " + self.field_liste[2] + " " + "|")
        print("|" + " " + self.field_liste[3] + " " + self.field_liste[4] + " " + self.field_liste[5] + " " + "|")
        print("|" + " " + self.field_liste[6] + " " + self.field_liste[7] + " " + self.field_liste[8] + " " + "|")
        print("-" * 9)


    def check_game(self): # verifie s'il y a un gagnant et stocke le résultat dans state_game
        # check diagonale principale
        if self.field_liste[0] == self.field_liste[4] == self.field_liste[8]=="X":
            self.state_game.add("X_winner")
        elif self.field_liste[0] == self.field_liste[4] == self.field_liste[8]=="O":
            self.state_game.add("O winner")
        # check diagonale secondaire
        elif self.field_liste[2] == self.field_liste[4] == self.field_liste[6]=="X":
            self.state_game.add("X_winner")
        elif self.field_liste[2] == self.field_liste[4] == self.field_liste[6] == "O":
            self.state_game.add("O winner")
        else:
            for i in range(0, 9, 3):  # check ligne
                if self.field_liste[i] == self.field_liste[i + 1] == self.field_liste[i + 2] == "X":
                    self.state_game.add("X_winner")
                elif self.field_liste[i] == self.field_liste[i + 1] == self.field_liste[i + 2] == "O":
                    self.state_game.add("O winner")
            for i in range(3):  # check colonne
                if self.field_liste[i] == self.field_liste[i + 3] == self.field_liste[i + 6]=="X":
                    self.state_game.add("X_winner")
                elif self.field_liste[i] == self.field_liste[i + 3] == self.field_liste[i + 6] == "O":
                    self.state_game.add("O winner")

    def state_game_func(self): # affiche le résultat du jeu ou renvoie un resultat vide
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

    def game(self, position):  #
        self.field_liste[position] = self.joueur_state # place le pion
        self.field_printing()  # affiche le terrain mis à jour
        self.check_game() # verifie s'il y a un gagnant ou non
        self.result = self.state_game_func() # renvoie le resultat (Win, Draw ou Vide)

    def user_move(self): # verifie que les coordonnees sont correctement rentrees
        move = input("Enter the coordinates: ").split(" ")
        if len(move) != 2:  # vérifier qu'on ait le bon nombre d'arguments
            print("You should enter numbers!")
        else:
            row_coordinate, column_coordinate = move[0], move[1]
            try:  # vérifier qu'on ait des chiffres
                row_coordinate = int(row_coordinate)
                column_coordinate = int(column_coordinate)
            except ValueError:
                print("You should enter numbers!")
            if row_coordinate not in range(1, 4) or column_coordinate not in range(1,
                                                                                   4):  # vérifier qu'on ait les bons chiffres
                print("Coordinates should be from 1 to 3!")
            else:
                position = (3 - column_coordinate) * 3 + (row_coordinate - 1)
                if self.field_liste[position] == "X" or self.field_liste[position] == "O":
                    print("This cell is occupied! Choose another one!")
                if self.field_liste[position] == "_" or self.field_liste[position] == " ":  # si la place est libre
                    self.game(position)

    def random_move(self):
            while True:
                row_coordinate, column_coordinate = random.randint(1, 3), random.randint(1, 3)
                position = (3 - column_coordinate) * 3 + (row_coordinate - 1)
                if self.field_liste[position] == "X" or self.field_liste[position] == "O":  # si la place est prise
                    continue
                elif self.field_liste[position] == "_" or self.field_liste[position] == " ":  # si la place est libre
                    self.game(position)
                    break

    def AI_move_easy(self):
        print('Making move level "easy"')
        self.random_move()

    def AI_move_medium(self):
        print('Making move level "medium"')
        AI_move = self.win_in_one_move()
        if AI_move is None:
            self.random_move()
        else:
            self.game(AI_move)


    def win_in_one_move(self):
        main_diag = [self.field_liste[0],self.field_liste[4],self.field_liste[8]]
        diag_sec = [self.field_liste[2], self.field_liste[4], self.field_liste[6]]
        # check diagonale principale
        if (main_diag.count(" ") == 1 ) and (main_diag.count("X") == 2 or main_diag.count("O") == 2):
            return main_diag.index(' ') * 4
        # check diagonale secondaire
        if (diag_sec.count(" ") == 1 )and (diag_sec.count("X") == 2 or diag_sec.count("O") == 2):
            return diag_sec.index(' ') * 2 + 2
        # check ligne
        rows = ((self.field_liste[0], self.field_liste[1], self.field_liste[2]),
                 (self.field_liste[3], self.field_liste[4], self.field_liste[5]),
                 (self.field_liste[6], self.field_liste[7], self.field_liste[8]))
        for i in range(len(rows)):
            if (rows[i].count(" ") == 1) and (rows[i].count("X") == 2 or rows[i].count("O") == 2):
                return rows[i].index(' ') + (3 * i)
        # check colonne
        columns = ((self.field_liste[0], self.field_liste[3], self.field_liste[6]),
                   (self.field_liste[1], self.field_liste[4], self.field_liste[7]),
                   (self.field_liste[2], self.field_liste[5], self.field_liste[8]))
        for j in range(len(columns)):
            if (columns[j].count(" ") == 1) and (columns[j].count("X") == 2 or columns[j].count("O") == 2):
                return columns[j].index(' ') * 3 + j

    def main_menu(self):
        while True:
            self.command = input('Input command: > ').split(' ')
            try: # on verifie qu'on ait tous les éléments de commande
                if self.command[0] == 'start':
                    if (self.command[1] in self.game_level or self.command[2] in self.game_level) or (self.command[1] in self.game_level and self.command[2] in self.game_level):
                        self.gamelevel()
                    elif self.command[1] == self.command[2] == 'user':
                        self.start(self.user_move, self.user_move)
                    else:
                        print('Bad parameters')
                    self.reinitialisation()
                elif self.command[0] == 'exit':
                    break
                else:
                    print('Bad parameters')
                    continue
            except IndexError:
                print('Bad parameters')
                continue

    def gamelevel(self):
       if self.command[1] == 'easy' or self.command[2] == 'easy':
            if self.command[1] == 'user' and self.command[2] == 'easy':
                self.start(self.user_move, self.AI_move_easy)
            elif self.command[1] == 'easy' and self.command[2] == 'user':
                self.start(self.AI_move_easy, self.user_move)
            elif self.command[1] == 'easy' and self.command[2] == 'easy':
                self.start(self.AI_move_easy, self.AI_move_easy)
            elif self.command[1] == 'easy' and self.command[2] == 'medium':
                self.start(self.AI_move_easy, self.AI_move_medium)
       if self.command[1] == 'medium' or self.command[2] == 'medium':
           if self.command[1] == 'user' and self.command[2] == 'medium':
               self.start(self.user_move, self.AI_move_medium)
           elif self.command[1] == 'medium' and self.command[2] == 'user':
               self.start(self.AI_move_medium, self.user_move)
           elif self.command[1] == 'medium' and self.command[2] == 'medium':
               self.start(self.AI_move_medium, self.AI_move_medium)
           elif self.command[1] == 'medium' and self.command[2] == 'easy':
               self.start(self.AI_move_medium, self.AI_move_easy)

    def start(self,func1, func2):
        self.field_printing()
        while self.result != 'stop':
            if int(self.field_liste.count("X")) == int(self.field_liste.count("O")):
                self.joueur_state = 'X'
                func1()
            elif int(self.field_liste.count("X")) > int(self.field_liste.count("O")):
                self.joueur_state = "O"
                func2()


game_instance = TicTacToe()

# appel de la fonction principale
game_instance.main_menu()