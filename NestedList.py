#Let's write a program that will read a positive integer n from the input and create a nested
#list containing the inner list [1, 2] repeated n times.
n = int(input())
number = [1,2]
my_list = [number for x in range(n)]
print(my_list)