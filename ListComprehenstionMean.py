number = input()
number_list = list(number)
print (number_list)
number_list = [ float(elements) for elements in number_list]
print(number_list)
mean = sum(number_list)/ len(number_list)
print (mean)