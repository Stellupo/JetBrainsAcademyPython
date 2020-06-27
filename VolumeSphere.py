class Sphere:
    PI = 3.1415

    def __init__(self,radius):
        self.radius = radius
        self.volume = 4/3 * Sphere.PI * radius**3

input_r = input()
triangle_a = Sphere (4)
print (triangle_a.volume)
