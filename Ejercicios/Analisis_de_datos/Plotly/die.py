from random import randint

class Die:
    """A class representing as single die"""
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    
    def roll (self):
        return randint(1, self.num_sides)

# die = Die()     estas tres lineas son solo para probar

# for x in range(100):
#     print (die.roll())