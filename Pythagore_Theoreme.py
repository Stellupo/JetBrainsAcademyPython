class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.S = (1/2 * (leg_1 * leg_2))

# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]
c_aucarre = ((input_c**2))
somme_ab = ((input_a**2 + input_b**2))
S = (1/2 * (input_a * input_b))

if c_aucarre == somme_ab:
    right_triangle = RightTriangle(input_c, input_a, input_b,)
    print (right_triangle.S)
else:
    print ('Not right')