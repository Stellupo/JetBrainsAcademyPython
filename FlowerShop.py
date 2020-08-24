import itertools
flower_names = ['rose', 'tulip', 'sunflower', 'daisy']
for i in range(1, 4):
    iter = itertools.combinations(flower_names, i)
    for combo in iter:
        print(combo)

# enonce
'''A flower shop has various flowers available, all listed in the flower_names list. 
You can buy a bouquet containing one, two or three different kinds of flowers.
Considering the list flower_names defined, print out all possible bouquets you can get. 
Note that the length of flower_names is arbitrary, while bouquets you are interested in should only contain from 1 to 3 flowers.'''