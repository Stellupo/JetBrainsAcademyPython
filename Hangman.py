import random
import string


def game(guess, count, word_choosen, word_list, guess_list, answer_list, menu_answer):
    while count != 8:
        print(guess)
        answer = input("Input a letter: ")
        if len(list(answer)) > 1 or len(list(answer)) == 0:
            print('You should input a single letter')
        elif answer not in string.ascii_lowercase:
            print("It is not an ASCII lowercase letter")
        else:
            if answer not in word_choosen:  # si la lettre n'appartient pas au mot
                if answer in answer_list:
                    print('You already typed this letter')
                else:
                    print("No such letter in the word")
                    count += 1
            elif answer in word_choosen:  # s'il y a une ou (plusieurs) lettre qui appartient au mot
                if answer in guess:
                    print('You already typed this letter')
                else:
                    for elements in range(len(word_list)):
                        if word_list[elements] == answer:  # si le joueur a la bonne réponse
                            guess_list[elements] = answer
                            guess = ''.join(guess_list)
                        else:
                            continue
        answer_list.add(answer)
        if count == 8:
            if "-" not in guess:
                print('You guessed the word ' + word_choosen + '!')
                print('You survived!')
                break
            if "-" in guess:
                print("You are hanged!")
        print("")


# main variables
languages_list = ['python', 'java', 'kotlin', 'javascript']
word_choosen = random.choice(languages_list)
word_list = list(word_choosen)  # chaque lettre du mot choisi fait partie d'une liste
guess = "-" * (len(word_choosen))
guess_list = list(guess)  # chaque lettre du mot avec - est un élément de cette liste
count = 0  # compteur du nombre de tours
answer_list = set()
menu_answer = ""

# main
print("H A N G M A N")
while menu_answer != "exit":
    print('Type "play" to play the game, "exit" to quit: ')
    menu_answer = input()
    print("")
    if menu_answer == "play":
        game(guess, count, word_choosen, word_list, guess_list, answer_list, menu_answer)
    else:
        continue