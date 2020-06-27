word=input()
if word.islower():
    print(word)
else:   #il y a des lettres en majuscule dans le mot
    for char in word:
        if char.isupper(): #char est une majuscule
            char=char.replace(char,'_'+char.lower()) #solution word=word.replace(char,'_'+cahr.lower())
        else:
            continue
        print(word)

#placEscape = CamelCase
#plac_escape = snake_case