dict = {'Jack':11, 'Queen':12,  'King':13, 'Ace':14}
liste = []
for i in range (0,6):
    liste += input().split("\n")
#print(liste)
for i in range (0,6):
    if liste[i].isdigit():
        liste[i] = int(liste[i])
    else:
        for key in dict.items():
            if liste[i] == key[0]:
                liste[i] = key[1]
    #print(liste)
print(sum(liste)/6)
