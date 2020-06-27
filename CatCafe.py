word = 0
cafes_list = []
cat_number = []
word_max = ['',0]
while True :
    word=str(input('Tapez le nom du café(Nom nombre de chats): '))
    if word != 'MEOW':
        word = word.split()
        word[1]=int(word[1])
        if word_max[1] >= word[1]:
            #print(word_max[0])
            continue
        else:  #word_max < element
            word_max=word  #c'est a dire word_max=[word[0],word[1]]
        #print(word_max[0])
    else:
        print(word_max[0])
        break