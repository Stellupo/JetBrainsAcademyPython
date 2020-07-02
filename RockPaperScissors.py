import random

def main_game(score):
    while True:
        move = input('> ')
        if move == "!exit":
            print("Bye!")
            break
        if move == "!rating":
            print(score)
        else:
            choices = ['rock', 'paper', 'scissors']
            computer_move = random.choice(["scissors","paper","rock"])
            game_state = ""
            if move == computer_move:
                game_state = "Draw"
            elif move != computer_move:
                if (move =="rock" and computer_move == "scissors") or (move == "paper" and computer_move == "scissors") or (move == "scissors" and computer_move == "paper"):
                    game_state = "Win"
                else:
                    game_state = "Lose"
                if move not in choices and move !="!exit" and move !="!rating":
                    print("Invalid input")
                    continue
            score = game_state_func(game_state,move,computer_move,score)

def game_state_func(game_state,move,computer_move,score):
    if game_state == "Draw":
        print('There is a draw (' + move + ')')
        score += 50
    if game_state == "Win":
        print('Well done. Computer chose ' + computer_move + ' and failed')
        score += 100
    if game_state == "Lose":
        print("Sorry, but computer chose " + computer_move)
    return score

def user ():
    user_name = input("Enter you name: ")
    print("Hello, "+user_name)
    file = open("rating.txt", "r")
    file_list = file.readlines()
    dico = {}
    score = 0
    for elements in file_list:
        elements = elements.split()
        elements[1] = elements[1].rstrip('\n')
        dico[elements[0]] = elements[1]
        if user_name == elements[0]:
            score = elements[1]
    file.close()
    return score

def start_menu(score):
    user_output = input().split(",")
    print("Okay, let's start")
    if user_output == [""]:
        main_game(score)
    else:
        options(user_output, score)

def options(user_output, score):
    while True:
        move = input('> ')
        if move == "!exit":
            print("Bye!")
            break
        if move == "!rating":
            print(score)
        else:
            if move in user_output:
                user_output_copy = ((user_output[user_output.index(move) + 1:]) + user_output[0:user_output.index(move)])
                computer_move = random.choice(user_output)
                game_state = ""
                if move == computer_move:
                    game_state = "Draw"
                elif move != computer_move:
                    if move not in user_output and move != "!exit" and move != "!rating":
                        print("Invalid input")
                        continue
                    if computer_move in user_output_copy[0:int((len(user_output_copy)/2))]:
                        game_state = "Lose"
                    else:
                        game_state = "Win"
                score = game_state_func(game_state, move, computer_move, score)



score = int(user())
game_state = start_menu(score)
