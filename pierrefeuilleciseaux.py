import random

def main_game():
    move =""
    choices = ['rock', 'paper', 'scissors']
    while move != "!exit":
        move = input('Make your move (r for rock, s for scissors, p for paper) :')
        computer_move = random.choice(["scissors","paper","rock"])
        game_state = ""
        if (move == "r" and computer_move == "rock") or (move == "p" and computer_move == "paper") or (move =="s" and computer_move == "scissors"):
            game_state = "Draw"
        elif move != computer_move:
            if move =="r":
                if computer_move == "scissors":
                    game_state = "Win"
                elif computer_move == "paper":
                    game_state = "Lose"
            if move == "p":
                if computer_move == "scissors":
                    game_state = "Lose"
                elif computer_move == "rock":
                    game_state = "Win"
            if move == "s":
                if computer_move == "paper":
                    game_state = "Win"
                elif computer_move == "rock":
                    game_state = "Lose"
            if move not in choices and move !="!exit":
                print("Invalid input")
                continue
        game_state_func(game_state,move,computer_move)
    else:
        print("Bye!")

def game_state_func(game_state,move,computer_move):
    if game_state == "Draw":
        print('There is a draw (' + computer_move + ')')
    if game_state == "Win":
        print('Well done. Computer chose ' + computer_move + ' and failed')
    if game_state == "Lose":
        print("Sorry, but computer chose " + computer_move)


game_state = main_game()