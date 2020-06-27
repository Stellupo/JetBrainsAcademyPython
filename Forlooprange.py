a = int(input())
b = int(input())
b = b+1
liste = []
count = 0
total = 0
for i in range (a,b):
    if i%3==0:  #si i est divisble par 3
        count += 1
        total = total+i
print (total/count)