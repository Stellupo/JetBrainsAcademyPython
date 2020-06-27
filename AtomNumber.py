N = int(input())  # amount of atomes
R = int(input())  # resulting quantity
T = 0
while N>R:
    N = N//2
    T += 12
print(T)