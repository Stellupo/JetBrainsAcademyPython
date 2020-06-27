word=input()
if word.islower():
    print(word)
else:   #il y a des lettres en majuscule dans le mot
    for char in word:
        if char.isupper(): #char est une majuscule
            #char= char.lower() = faux parce qu'on ne modifie que la copie de ma valeur str, pour la modifier il faut que je la rattache à word!
            word=word.replace(char,'_'+char.lower()) #replace ne marque que pour les str pas pour les lettres solution
        else:
            continue
        print(word)

#placEscape = camelCase
#plac_escape = snake_case