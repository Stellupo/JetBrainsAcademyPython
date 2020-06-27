word = 0
cafes_list = []
cat_number = []
while True :
    word=str(input('Tapez le nom du café(Nom nombre de chats): '))
    if word != 'MEOW':
        word = word.split()
        #print (word)
        cafes_list += [word[0]]
        cat_number += [word[1]]  #faut créer une séquence qui ne contient qu'un seul élément
        # car += va appeler la fonction list() dans ce cas. Car l'élément à droite et à gauche
        #doivent être du même type. Donc il convertit word en list, en séparant chaque élément. Il ne le fera pas avec une liste.
        #print (cafes_list)
        #print (cat_number)

    else:
        break
m = 0
index_dumax = 0
for index,number in enumerate(cat_number) :
    number = int(number)
    if m >= number:
        continue
    else:  #m < number
        m = number
        index_dumax = index
#print ('index :'+str(index_dumax)+',max chat: '+str(m))
print (cafes_list[index_dumax])