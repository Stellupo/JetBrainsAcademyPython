print('''
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
''')


print('Write how many ml of water the coffee machine has:')
water_machine = int(input())
print('Write how many ml of milk the coffee machine has:')
milk_machine = int(input())
print('Write how many grams of coffee beans the coffee machine has:')
coffee_machine = int(input())
stock_ingredients = [water_machine, milk_machine, coffee_machine]
number_cups=int(input(("Write how many cups of coffee you will need:")))
ingredients = [200,50,15]
N=0  #nombre de café que la machine peut faire
while water_machine!=0 or milk_machine!=0 or coffee_machine!=0:
    if water_machine<ingredients[0] or milk_machine<ingredients[1] or coffee_machine<ingredients[2]:
        break
    water_machine=water_machine-ingredients[0]
    milk_machine=milk_machine-ingredients[1]
    coffee_machine=coffee_machine- ingredients[2]
    stock_ingredients = [water_machine, milk_machine, coffee_machine]
    N+=1
print(N)
if N < number_cups :
    print("No, I can make only",N,"cup(s) of coffee")
elif N == number_cups:
    print("Yes, I can make that amount of coffee")
else:  #N>number_cups
    print("Yes, I can make that amount of coffee (and even "+str(N-number_cups)+" more than that)")