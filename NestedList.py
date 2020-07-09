card_number = [4, 0, 0, 0, 0, 0, 9, 4, 1, 4, 6, 6, 9, 6, 9, 1]
print(card_number)
#card_number = ''.join(str(numbers) for numbers in card_number)
print(card_number)
print([card_number.index(x) for x in card_number])
card_number = [2*x if ((card_number.index(x))%2)==0 else x for x in card_number]
print(card_number)