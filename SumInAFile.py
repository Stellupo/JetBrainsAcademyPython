file = open("sums.txt", "r")
for number in file :
    number1, number2 = number.split()
    print(int(number1) + int(number2))
file.close()  # read sums.txt

'''
You have the file sums.txt. It has multiple lines that contain two numbers separated by whitespace. All numbers are positive.
For example:
9 61
15 47
2 1
Write a program that reads this file and print the sum of numbers on each line. So, if the file has n lines, you should print n sums, each on a separate line.
!'''