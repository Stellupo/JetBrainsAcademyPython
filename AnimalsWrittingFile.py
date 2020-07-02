file = open("animals.txt", "r")
animals_new = open("animals_new.txt", "w")
for animal in animals:
    animal = animal.replace("\n", " ")
    animals_new.write(animal)
file.close()
animals_new.close()

# énoncé
'''The file animals.txt has a list of animals, each written on a new line.
For example:
rabbit
cat
turtle
Create a new file, animals_new.txt, where those animals are written on a single
line and separated by whitespace'''