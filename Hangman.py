import random

languages_list = ['python', 'java', 'kotlin', 'javascript']
word_choosen = random.choice(languages_list)
word_list = tuple(word_choosen) #chaque lettre du mot choisi fait partie d'une liste
print("H A N G M A N")
print ("Guess the word "+word_list[0]+word_list[1]+word_list[2]+("-"*(len(word_choosen)-3))+" : ")
word = input()
if word == word_choosen:
    print("You survived!")
else:
    print("You are hanged!")