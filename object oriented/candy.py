class Candy:
    '''
    A class to represent a piece of candy
    Attributes: flavour, colour, brand
    Methods: eat(), throwOut()
    '''
    def __init__(self, flavour, colour, brand):
        self.flavour = flavour
        self.colour = colour
        self.brand = brand
    def __str__(self) -> str:
        # string base ovveride for the object
        return f'A {self.colour}, {self.flavour} {self.brand}'
    def __repr__(self) -> str:
        return self.__str__()
    
    def eat(self):
        return 