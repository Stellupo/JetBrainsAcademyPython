def even(j):
    a = 0
    i = 1
    while i <= j:
        yield a
        i += 1
        a += 2

n = int(input())
generator = even(n)
for i in generator:
    print(i)



# énoncé :
'''Define a generator even that produces even numbers (0, 2, 4, 6, ...).
For a given number n, print out the first n ones on separate lines.'''