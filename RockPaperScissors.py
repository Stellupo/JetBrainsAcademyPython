import random

def main_game(score):
    move = ""
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
                if move =="rock":
                    if computer_move == "scissors":
                        game_state = "Win"
                    elif computer_move == "paper":
                        game_state = "Lose"
                if move == "paper":
                    if computer_move == "scissors":
                        game_state = "Lose"
                    elif computer_move == "rock":
                        game_state = "Win"
                if move == "scissors":
                    if computer_move == "paper":
                        game_state = "Win"
                    elif computer_move == "rock":
                        game_state = "Lose"
                if move not in choices and move !="!exit":
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


score = int(user())
game_state = main_game(score)