import random
from math import inf as infinity

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


    def check_game(self, liste): # verifie s'il y a un gagnant et stocke le résultat dans state_game
        # check diagonale principale
        if "_" not in liste and " " not in liste:
            self.state_game.add("Draw")
        elif liste[0] == liste[4] == liste[8]== self.joueur_state:
            self.state_game.add(self.joueur_state + "winner")
        # check diagonale secondaire
        elif liste[2] == liste[4] == liste[6]== self.joueur_state:
            self.state_game.add(self.joueur_state + " winner")
        else:
            for i in range(0, 9, 3):  # check ligne
                if liste[i] == liste[i + 1] == liste[i + 2] == self.joueur_state:
                    self.state_game.add(self.joueur_state + " winner")
            for i in range(3):  # check colonne
                if liste[i] == liste[i + 3] == liste[i + 6]== self.joueur_state:
                    self.state_game.add(self.joueur_state + " winner")
                elif liste[i] == liste[i + 3] == liste[i + 6] == "O":
                    self.state_game.add("O winner")

    def state_game_func(self): # affiche le résultat du jeu ou renvoie un resultat vide
        if ("O winner") in self.state_game or ("X winner") in self.state_game:
            print(self.joueur_state, "wins")
            return "stop"
        elif "Draw" in self.state_game:
            print("Draw")
            return "stop"
        else:
            return ""

    def game(self, position):  #
        self.field_liste[position] = self.joueur_state # place le pion
        self.field_printing()  # affiche le terrain mis à jour
        self.check_game(self.field_liste) # verifie s'il y a un gagnant ou non
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

    def AI_move_hard(self):
        print('Making move level "hard"')
        if self.field_liste.count(' ') == 9 :
            self.random_move()
        else:
            index = self.minimax(self.field_liste, self.joueur_state)[0]
            self.game(index)


    def minimax(self, board,player):
        # verifie s'il y a un gagnant ou non
        self.check_game(board)

        if self.state_game == str(player + " winner"): # si je perds
            return ['index', -10]
            self.state_game = set()  # reinitialisation
        if len(self.available_spots(board)) == 0:
            return ['index', 0]
            self.state_game = set()  # reinitialisation
        if self.state_game != set() and self.state_game != "Draw": # si je gagne
            return ['index', 10]
            self.state_game = set()  # reinitialisation


        moves = []

        for elements in self.available_spots(board):
            move = {
                'index': elements,
                'score': None
            }  # on enregistre les index
            newboard = self.copy_game_state(board)    # place le pion
            newboard[elements] = player

            # changement de profil
            if player == "X":
                move['score'] = self.minimax(newboard, 'O')[1]
            elif player == "O": # AI
                move['score'] = self.minimax(newboard, 'X')[1]

            moves.append(move)

        index = None
        if player == 'X':
            bestscore = -infinity
            for number_of_specific_move in range(len(moves)):
                if moves[number_of_specific_move]['score'] > bestscore:
                    index = moves[number_of_specific_move]['index']
                    bestscore = moves[number_of_specific_move]['score']
        else:
            bestscore = +infinity
            for number_of_specific_move in range(len(moves)):
                if moves[number_of_specific_move]['score'] < bestscore:
                    index = moves[number_of_specific_move]['index']
                    bestscore = moves[number_of_specific_move]['score']
        return [index, bestscore]



    def copy_game_state(self, board):
        newboard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        for i in range(len(board)):
            newboard[i] = board[i]
        return newboard

    def available_spots(self,board):
        #check les places libres
        availablepositions = []
        for i in range(len(board)):  # on parcourt les valeurs de field_liste
            if board[i] == " ":  # si la place est libre
                availablepositions.append(i)  # on ajoute l'index à la liste availablepositions
        return availablepositions


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
                    self.reinitialisation()
                    continue
            except IndexError:
                print('Bad parameters')
                self.reinitialisation()
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
            elif self.command[1] == 'easy' and self.command[2] == 'hard':
                self.start(self.AI_move_easy, self.AI_move_hard)
       if self.command[1] == 'medium' or self.command[2] == 'medium':
           if self.command[1] == 'user' and self.command[2] == 'medium':
               self.start(self.user_move, self.AI_move_medium)
           elif self.command[1] == 'medium' and self.command[2] == 'user':
               self.start(self.AI_move_medium, self.user_move)
           elif self.command[1] == 'medium' and self.command[2] == 'medium':
               self.start(self.AI_move_medium, self.AI_move_medium)
           elif self.command[1] == 'medium' and self.command[2] == 'easy':
               self.start(self.AI_move_medium, self.AI_move_easy)
           elif self.command[1] == 'medium' and self.command[2] == 'hard':
               self.start(self.AI_move_medium, self.AI_move_hard)
       if self.command[1] == 'hard' or self.command[2] == 'hard':
           if self.command[1] == 'user' and self.command[2] == 'hard':
               self.start(self.user_move, self.AI_move_hard)
           elif self.command[1] == 'hard' and self.command[2] == 'user':
               self.start(self.AI_move_hard, self.user_move)
           elif self.command[1] == 'hard' and self.command[2] == 'hard':
               self.start(self.AI_move_hard, self.AI_move_hard)
           elif self.command[1] == 'hard' and self.command[2] == 'easy':
               self.start(self.AI_move_hard, self.AI_move_easy)
           elif self.command[1] == 'hard' and self.command[2] == 'medium':
               self.start(self.AI_move_hard, self.AI_move_medium)

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