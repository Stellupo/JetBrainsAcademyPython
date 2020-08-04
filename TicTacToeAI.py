import random


class TicTacToe:
    def __init__(self):
        self.reinitialisation()
        #self.field_printing()


    def reinitialisation(self):
        self.field = [[" ", " ", " "], [" ", " ", " "],[" ", " ", " "]]  # [[column for column in range(3)] for row in range(3)]x
        self.field_liste = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.joueur_state = "X"
        self.state_game = set()
        self.result = ""
        self.game_level = ['easy', 'medium', 'hard']
        self.command = ""


    def field_printing(self): # affiche le terrain en table
        print("-" * 9)
        print("|" + " " + self.field[0][2] + " " + self.field[1][2] + " " + self.field[2][2] + " " + "|")
        print("|" + " " + self.field[0][1] + " " + self.field[1][1] + " " + self.field[2][1] + " " + "|")
        print("|" + " " + self.field[0][0] + " " + self.field[1][0] + " " + self.field[2][0] + " " + "|")
        print("-" * 9)

    def update_fieldliste(self): # met a jour la liste des cases du terrain
        self.field_liste = [elements for row in self.field for elements in row]
        return self.field_liste

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

    def game(self, row_coordinate, column_coordinate):  #
        self.field[int(row_coordinate) - 1][int(column_coordinate) - 1] = self.joueur_state # place le pion
        self.field_printing()  # affiche le terrain mis à jour
        self.field_liste = self.update_fieldliste() # met a jour la liste des cases
        self.check_game() # verifie s'il y a un gagnant ou non
        self.result = self.state_game_func() # renvoie le resultat (Win, Draw ou Vide)
        return self.result

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
                position = self.field[int(row_coordinate) - 1][int(column_coordinate)-1]
                if position == "X" or position == "O":
                    print("This cell is occupied! Choose another one!")
                if position == "_" or position == " ":  # si la place est libre
                    self.result = self.game(row_coordinate, column_coordinate)
        return self.result

    def AI_move_easy(self):
        print('Making move level "easy"')
        while True:
            row_coordinate, column_coordinate = random.randint(1, 3), random.randint(1, 3)
            position = self.field[int(row_coordinate) - 1][int(column_coordinate)-1]
            if position == "X" or position == "O": # si la place est prise
                continue
            elif position == "_" or position == " ":  # si la place est libre
                self.result = self.game(row_coordinate, column_coordinate)
                break
        return self.result

    def AI_move_medium(self):
        print('Making move level "medium"')
        # check diagonale principale
        main_diag = [self.field[0][2],self.field[1][1],self.field[2][0]]
        if main_diag.count("X") == 2 or main_diag.count("O") == 2:
            for m in range(3):
                if self.field[m][2-m] == " " or self.field[m][2-m] == "_":
                    self.game(m+1,2-m+1)
        # check diagonale secondaire
        diag_sec = [self.field[0][0],self.field[1][1],self.field[2][2]]
        if diag_sec.count("X") == 2 or diag_sec.count("O") == 2:
            for m in range(3):
                if self.field[m][m] == " " or self.field[m][m] == "_":
                    self.game(m+1,m+1)
        # check ligne
        for i in range(3):
            if self.field[i].count("X") == 2 or self.field[i].count("O")==2:
                for j in range(3):
                    if self.field[i][j] == "_"  or self.field[i][j]== " " :
                            self.game(i+1,j+1)
        # check colonne
            column = [self.field[0][i],self.field[1][i],self.field[2][i]]
            if column.count("X") == 2 or column.count("O") == 2 :
                for k in range(3):
                    if column[k] == "_" or column[k] == " ":
                        self.game(k+1,i+1)

    def main_menu(self):
        while True:
            self.command = input('Input command: > ').split(' ')
            try: # on verifie qu'on ait tous les éléments de commande
                if self.command[0] == 'start':
                    if self.command[1] == 'easy' or self.command[2] == 'easy':
                        if self.command[1] == 'user' and self.command[2] == 'easy':
                            self.start(self.user_move, self.AI_move_easy)
                        elif self.command[1] == 'easy' and self.command[2] == 'user':
                            self.start(self.AI_move_easy, self.user_move)
                        elif self.command[1] == 'easy' and self.command[2] == 'easy':
                            self.start(self.AI_move_easy, self.AI_move_easy)
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

    def start(self,func1, func2):
        self.field_printing()
        while self.result != 'stop':
            if abs(self.field_liste.count("X") == self.field_liste.count("O")):
                self.joueur_state = 'X'
                func1()
            elif abs(self.field_liste.count("X") > self.field_liste.count("O")):
                self.joueur_state = "O"
                func2()






game_instance = TicTacToe()

# appel de la fonction principale

game_instance.main_menu()
#todo définir une fonction medium qui fasse réagir l'ordi selon la difficulté (2 pions)
# intégrer dans la fonction Ai move la différence entre niveaux
# segementer dans main menu pour plus de clarté