def range_sum(numbers, start, end):
    result = 0
    for n in numbers:
        if end >= n >= start:
            result += n
        else:
            result += 0
    return result

input_numbers = input().split(' ')
input_numbers = [int(x) for x in input_numbers if x != ' ']
input =  input().split()
a, b = int(input[0]), int(input[1])
print(range_sum(input_numbers, a, b))