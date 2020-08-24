import itertools

main_courses = ['beef stew', 'fried fish']
price_main_courses = [28, 23]

desserts = ['ice-cream', 'cake']
price_desserts = [2, 4]

drinks = ['cola', 'wine']
price_drinks = [3, 10]

for a,b,c in itertools.product(zip(main_courses, price_main_courses), zip(desserts, price_desserts), zip(drinks, price_drinks)):
    if a[1] + b[1] + c[1] <= 30 :
        print(a[0],b[0],c[0],a[1] + b[1] + c[1])

#enonce :
'''Imagine you are having dinner in a very fancy restaurant, but unfortunately you don't have a lot of money with you.
You want to have a main course, a dessert and a drink, but all that together shouldn't cost more than $30.
The names of the main courses, desserts and drinks are stored in the lists main_courses, desserts and drinks respectively.
The corresponding prices can be found in the lists price_main_courses, price_desserts and price_drinks.
Consider each possible combination of a main course, dessert and a drink from those offered by the restaurant
and print out only those meals that satisfy your budget, along with their total costs.'''