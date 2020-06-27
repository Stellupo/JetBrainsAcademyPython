word = input()
liste = list(word)  #fct list convertit la séquence en liste  #liste=[word] :def une liste avec une seule variable
liste_inverse = liste[::-1]
while len(word) % 2 == 0:  #si la longueur du mot est paire
    for letter in range (len(liste)):  #pour chaque lettre présente dans mon mot
        if liste[letter] != liste_inverse[letter]:
            print('Not palindrome')
            break
    else:
        print('Palindrome')
    break
else:
    print('Not palindrome')